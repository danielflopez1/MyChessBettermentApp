import io
from typing import List, Dict, Any
import chess
import chess.pgn
import chess.engine
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from openings_data import OPENINGS_DATABASE

# -------------------------
# Hardcoded configuration
# -------------------------

# CHANGE THIS if your Stockfish is elsewhere
STOCKFISH_PATH = r".\Stock\stockfish-windows-x86-64-avx2.exe"  # Update this path for Windows
# Example for Mac/Linux:
# STOCKFISH_PATH = "/usr/local/bin/stockfish"

# Time for live play moves
ENGINE_TIME_PER_MOVE = 0.1
# Time for deep analysis of PGNs (higher is better but slower)
ENGINE_TIME_PER_ANALYSIS = 0.5
MATE_SCORE = 100000

SECRET_KEY = "chesskit_python_clone_demo_secret_key_123"

# A sample PGN for the "Review Sample" button
OPERA_GAME_PGN = """
[Event "Opera Game"]
[Site "Paris"]
[Date "1858.??.??"]
[Round "?"]
[White "Paul Morphy"]
[Black "Duke Karl / Count Isouard"]
[Result "1-0"]

1. e4 e5 2. Nf3 d6 3. d4 Bg4 4. dxe5 Bxf3 5. Qxf3 dxe5 6. Bc4 Nf6 7. Qb3
Qe7 8. Nc3 c6 9. Bg5 b5 10. Nxb5 cxb5 11. Bxb5+ Nbd7 12. O-O-O Rd8
13. Rxd7 Rxd7 14. Rd1 Qe6 15. Bxd7+ Nxd7 16. Qb8+ Nxb8 17. Rd8# 1-0
"""

app = Flask(__name__)
app.secret_key = SECRET_KEY


# -------------------------
# Move quality
# -------------------------

def classify_move(cp_loss: int) -> str:
    """
    cp_loss: best_eval_for_side - eval_after_move_for_side (from mover's POV).
    Positive -> worse than best; Negative -> outperforms engine PV ("Brilliant").
    """
    if cp_loss < -50:
        return "Brilliant"
    if cp_loss <= 20:
        return "Best"
    if cp_loss <= 50:
        return "Excellent"
    if cp_loss <= 100:
        return "Good"
    if cp_loss <= 200:
        return "Inaccuracy"
    if cp_loss <= 400:
        return "Mistake"
    return "Blunder"


# -------------------------
# Session helpers for live play
# -------------------------

def _session_get(key: str, default):
    return session.get(key, default)


def _save_session_game(moves_uci: List[str], player_color: str):
    session["moves_uci"] = moves_uci
    session["player_color"] = player_color


def _load_session_game():
    moves_uci = _session_get("moves_uci", [])
    player_color = _session_get("player_color", "white")
    return moves_uci, player_color


def _board_from_moves(moves_uci: List[str]) -> chess.Board:
    board = chess.Board()
    for u in moves_uci:
        board.push(chess.Move.from_uci(u))
    return board


def _engine():
    # Note: For production, you'd initialize this once
    return chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)


def _maybe_engine_start(moves_uci: List[str], player_color: str) -> List[str]:
    """
    If the engine should move first (player picked black), make its opening move.
    """
    board = _board_from_moves(moves_uci)
    player_is_white = (player_color == "white")
    side_to_move_is_player = (board.turn == chess.WHITE and player_is_white) or (
            board.turn == chess.BLACK and not player_is_white)

    if not side_to_move_is_player and not board.is_game_over():
        with _engine() as engine:
            mv = engine.play(board, chess.engine.Limit(time=ENGINE_TIME_PER_MOVE)).move
        board.push(mv)
        moves_uci.append(mv.uci())

    return moves_uci


# -------------------------
# PGN Analysis
# -------------------------

def _analyze_pgn(pgn_string: str) -> Dict[str, Any]:
    """
    The core PGN analysis logic.
    This is a heavy operation!
    """
    try:
        pgn_file = io.StringIO(pgn_string)
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            raise ValueError("Could not parse PGN.")
    except Exception as e:
        return {"error": f"Failed to read PGN: {e}"}

    board = game.board()
    mainline_moves = list(game.mainline_moves())

    fens = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"]
    evals_cp = [0]  # Eval *after* the move (from White's POV)
    move_labels = []  # "1. e4", "1... e5", "2. Nf3"
    analyzed_moves = []

    with _engine() as engine:
        for i, move in enumerate(mainline_moves):
            turn = board.turn
            side_str = "White" if turn == chess.WHITE else "Black"
            move_num = board.fullmove_number

            # 1. Get eval BEFORE this move
            info_before = engine.analyse(board, chess.engine.Limit(time=ENGINE_TIME_PER_ANALYSIS))
            # Get score from the mover's POV
            best_score_before = info_before["score"].pov(turn).score(mate_score=MATE_SCORE)
            best_san = None
            if "pv" in info_before and info_before["pv"]:
                try:
                    best_san = board.san(info_before["pv"][0])
                except Exception:
                    best_san = info_before["pv"][0].uci()

            # 2. Make the move
            san_played = board.san(move)
            board.push(move)

            # 3. Get eval AFTER this move
            info_after = engine.analyse(board, chess.engine.Limit(time=ENGINE_TIME_PER_ANALYSIS))
            # Get score from the *previous* mover's POV
            after_score = info_after["score"].pov(not board.turn).score(mate_score=MATE_SCORE)

            # 4. Calculate loss and classify
            # (Handle mate scores)
            if best_score_before is None: best_score_before = 0
            if after_score is None: after_score = 0

            cp_loss = best_score_before - after_score
            classification = classify_move(cp_loss)

            # Store data for chart/table
            fens.append(board.fen())
            evals_cp.append(info_after["score"].white().score(mate_score=MATE_SCORE))

            label = f"{move_num}. {san_played}" if turn == chess.WHITE else f"{move_num}... {san_played}"
            move_labels.append(label)

            analyzed_moves.append({
                "move_number": move_num,
                "side": side_str,
                "san": san_played,
                "best_san": best_san or "N/A",
                "best_score": best_score_before,
                "after_score": after_score,
                "cp_loss": cp_loss,
                "classification": classification,
            })

    game_info = {
        "white": game.headers.get("White", "Unknown"),
        "black": game.headers.get("Black", "Unknown"),
        "event": game.headers.get("Event", "Unknown Event"),
        "site": game.headers.get("Site", ""),
        "date": game.headers.get("Date", ""),
        "result": game.headers.get("Result", "*"),
    }

    return {
        "ok": True,
        "game_info": game_info,
        "moves": analyzed_moves,
        "fens": fens,
        "evals": evals_cp,
        "move_labels": move_labels,
    }


# -------------------------
# Routes
# -------------------------

@app.route("/", methods=["GET"])
def home():
    """
    Render the main index/menu page.
    """
    return render_template("index.html", default_pgn=OPERA_GAME_PGN)


@app.route("/play", methods=["GET"])
def play():
    """
    Open straight into the playable board.
    Use ?color=white or ?color=black to choose side (default = white).
    """
    color = (request.args.get("color") or "white").lower()
    if color not in ("white", "black"):
        color = "white"

    # Reset the session game and (if needed) let engine start
    moves_uci = []
    moves_uci = _maybe_engine_start(moves_uci, color)
    _save_session_game(moves_uci, color)

    board = _board_from_moves(moves_uci)
    return render_template("play.html", fen=board.fen(), player_color=color)


@app.route("/review-sample", methods=["GET"])
def review_sample():
    """
    Analyzes the hardcoded sample PGN and shows the review page.
    """
    analysis_data = _analyze_pgn(OPERA_GAME_PGN)
    if not analysis_data.get("ok"):
        return f"Error analyzing sample PGN: {analysis_data.get('error')}", 500

    return render_template("review.html", **analysis_data)


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyzes a user-submitted PGN (from text or file) and shows review page.
    """
    pgn_string = ""

    # Try to get from file upload first
    if "pgn_file" in request.files:
        file = request.files["pgn_file"]
        if file.filename != "":
            try:
                pgn_string = file.read().decode("utf-8")
            except Exception as e:
                return f"Error reading file: {e}", 400

    # If no file, try to get from textarea
    if not pgn_string:
        pgn_string = request.form.get("pgn", "")

    # If still no PGN, use the sample as a fallback
    if not pgn_string.strip():
        pgn_string = OPERA_GAME_PGN

    analysis_data = _analyze_pgn(pgn_string)
    if not analysis_data.get("ok"):
        return f"Error analyzing PGN: {analysis_data.get('error')}", 500

    return render_template("review.html", **analysis_data)


# -------------------------
# API Routes (for live play)
# -------------------------

@app.route("/api/new", methods=["POST"])
def api_new():
    color = (request.json or {}).get("color", "white")
    if color not in ("white", "black"):
        color = "white"

    moves_uci = []
    moves_uci = _maybe_engine_start(moves_uci, color)
    _save_session_game(moves_uci, color)
    board = _board_from_moves(moves_uci)
    return jsonify({"ok": True, "fen": board.fen(), "player_color": color})


@app.route("/api/move", methods=["POST"])
def api_move():
    """
    Accept a player's UCI move, grade it, make engine reply, return updated FEN + info.
    """
    data = (request.json or {})
    uci = data.get("uci", "")

    moves_uci, player_color = _load_session_game()
    board = _board_from_moves(moves_uci)

    player_is_white = (player_color == "white")
    side_to_move_is_player = (board.turn == chess.WHITE and player_is_white) or (
            board.turn == chess.BLACK and not player_is_white)
    if not side_to_move_is_player:
        return jsonify({"ok": False, "error": "Not player's turn"}), 400

    try:
        move = chess.Move.from_uci(uci)
    except Exception:
        return jsonify({"ok": False, "error": "Bad UCI"}), 400

    if move not in board.legal_moves:
        return jsonify({"ok": False, "error": "Illegal move"}), 400

    with _engine() as engine:
        # Eval BEFORE (mover's POV)
        info_before = engine.analyse(board, chess.engine.Limit(time=ENGINE_TIME_PER_MOVE))
        best_score_before = info_before["score"].pov(board.turn).score(mate_score=MATE_SCORE)
        best_san = None
        if "pv" in info_before and info_before["pv"]:
            try:
                best_san = board.san(info_before["pv"][0])
            except Exception:
                best_san = None

        # Apply player's move
        san_played = board.san(move)
        board.push(move)

        # Eval AFTER from mover's POV
        info_after = engine.analyse(board, chess.engine.Limit(time=ENGINE_TIME_PER_MOVE))
        after_score = info_after["score"].pov(not board.turn).score(mate_score=MATE_SCORE)

        # Handle mate scores
        if best_score_before is None: best_score_before = 0
        if after_score is None: after_score = 0

        cp_loss = best_score_before - after_score
        classification = classify_move(cp_loss)

        # Engine reply
        engine_san = None
        if not board.is_game_over():
            reply = engine.play(board, chess.engine.Limit(time=ENGINE_TIME_PER_MOVE)).move
            engine_san = board.san(reply)
            board.push(reply)

    # Persist new state
    moves_uci = [m.uci() for m in board.move_stack]
    _save_session_game(moves_uci, player_color)

    return jsonify({
        "ok": True,
        "fen": board.fen(),
        "player_move": san_played,
        "engine_move": engine_san,
        "classification": classification,
        "cp_loss": cp_loss,
        "best_move": best_san,
        "game_over": board.is_game_over(),
        "result": board.result() if board.is_game_over() else None,
    })


@app.route("/api/undo", methods=["POST"])
def api_undo():
    """
    Retract the last full turn (engine reply + your previous move if present).
    """
    moves_uci, player_color = _load_session_game()
    board = _board_from_moves(moves_uci)

    if not board.move_stack:
        return jsonify({"ok": False, "error": "No moves to undo"}), 400

    # Pop two plies (full turn) if available; pop one if only one exists
    for _ in range(2):
        if board.move_stack:
            board.pop()

    moves_uci = [m.uci() for m in board.move_stack]

    # ***FIX***: If we undid back to the engine's turn (e.g., player is Black),
    # we must make the engine move again.
    moves_uci = _maybe_engine_start(moves_uci, player_color)

    _save_session_game(moves_uci, player_color)
    board = _board_from_moves(moves_uci)  # Re-create board from new stack

    return jsonify({"ok": True, "fen": board.fen()})


@app.route("/api/hint", methods=["POST"])
def api_hint():
    """
    Return the best move for the current position (player's turn).
    """
    moves_uci, player_color = _load_session_game()
    board = _board_from_moves(moves_uci)

    player_is_white = (player_color == "white")
    side_to_move_is_player = (board.turn == chess.WHITE and player_is_white) or (
            board.turn == chess.BLACK and not player_is_white)

    if not side_to_move_is_player:
        return jsonify({"ok": False, "error": "Not player's turn"}), 400

    if board.is_game_over():
        return jsonify({"ok": False, "error": "Game is over"}), 400

    with _engine() as engine:
        info = engine.analyse(board, chess.engine.Limit(time=ENGINE_TIME_PER_ANALYSIS))

        best_move = None
        best_san = None
        eval_cp = None

        if "pv" in info and info["pv"]:
            best_move = info["pv"][0]
            best_san = board.san(best_move)
            eval_cp = info["score"].pov(board.turn).score(mate_score=MATE_SCORE)

    if not best_move:
        return jsonify({"ok": False, "error": "Could not find best move"}), 500

    return jsonify({
        "ok": True,
        "best_move_uci": best_move.uci(),
        "best_move_san": best_san,
        "from_square": best_move.from_square,
        "to_square": best_move.to_square,
        "eval_cp": eval_cp
    })


# -------------------------
# Opening Trainer Routes
# -------------------------

@app.route("/openings", methods=["GET"])
def openings_list():
    """
    Show list of available openings to practice.
    """
    return render_template("openings.html", openings=OPENINGS_DATABASE)


@app.route("/openings/<opening_id>", methods=["GET"])
def opening_trainer(opening_id):
    """
    Practice a specific opening.
    """
    if opening_id not in OPENINGS_DATABASE:
        return "Opening not found", 404

    opening = OPENINGS_DATABASE[opening_id]
    # Use the first line for now (can be extended for multiple variations)
    line = opening["lines"][0]

    return render_template(
        "opening_trainer.html",
        opening_id=opening_id,
        opening=opening,
        line=line
    )


# -------------------------
# Opening Trainer API
# -------------------------

@app.route("/api/openings/<opening_id>/check", methods=["POST"])
def check_opening_move(opening_id):
    """
    Check if the player's move matches the opening line.
    """
    if opening_id not in OPENINGS_DATABASE:
        return jsonify({"ok": False, "error": "Opening not found"}), 404

    data = request.json or {}
    move_san = data.get("move_san", "")
    move_index = data.get("move_index", 0)

    opening = OPENINGS_DATABASE[opening_id]
    line = opening["lines"][0]  # Using first line

    if move_index >= len(line["moves"]):
        return jsonify({
            "ok": True,
            "correct": True,
            "completed": True,
            "message": "Congratulations! You've completed this opening!"
        })

    expected_move = line["moves"][move_index]
    is_correct = move_san == expected_move["san"]

    response = {
        "ok": True,
        "correct": is_correct,
        "expected_move": expected_move["san"],
        "comment": expected_move.get("comment", ""),
        "completed": False
    }

    if not is_correct:
        response["message"] = f"Not quite! The correct move is {expected_move['san']}"

    return jsonify(response)


@app.route("/api/openings/<opening_id>/next-move", methods=["POST"])
def get_next_opening_move(opening_id):
    """
    Get the next move in the opening (for computer moves).
    """
    if opening_id not in OPENINGS_DATABASE:
        return jsonify({"ok": False, "error": "Opening not found"}), 404

    data = request.json or {}
    move_index = data.get("move_index", 0)

    opening = OPENINGS_DATABASE[opening_id]
    line = opening["lines"][0]

    if move_index >= len(line["moves"]):
        return jsonify({
            "ok": True,
            "completed": True
        })

    next_move = line["moves"][move_index]

    return jsonify({
        "ok": True,
        "move": next_move["move"],
        "san": next_move["san"],
        "comment": next_move.get("comment", ""),
        "completed": False
    })

if __name__ == "__main__":
    app.run(debug=True, threaded=True)  # Threaded for concurrent requests