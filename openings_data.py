"""
Chess Openings Database
Contains popular chess openings with moves and annotations.

After import, this module automatically enriches each move with:
- piece:       "Pawn" / "Knight" / "Bishop" / "Rook" / "Queen" / "King"
- from_square: e.g. "g1"
- to_square:   e.g. "f3"
- move:        human-readable "Knight g1 -> f3"

The SAN notation is kept in `san`, e.g. "Nf3" or "Qxf7#".
"""

# =========================
# Raw openings data (SAN)
# =========================

OPENINGS_DATABASE = {
    "queens-gambit": {
        "name": "Queen's Gambit",
        "side": "white",
        "description": (
            "Offering the c-pawn to gain a long-term central advantage. "
            "Statistically one of the best-scoring openings for White."
        ),
        "eco": "D06",
        "lines": [
            {
                "name": "Accepted",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn opening"},
                    {"move": "d5", "san": "d5", "comment": "Black stakes claim in the center"},
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "The Queen's Gambit! Offer the c-pawn to deflect Black's d-pawn",
                    },
                    {"move": "dxc4", "san": "dxc4", "comment": "Black accepts the gambit"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and prepare to recapture on c4"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and fight for the e4 square"},
                    {"move": "e3", "san": "e3", "comment": "Open the diagonal for the bishop to recapture on c4"},
                    {"move": "e6", "san": "e6", "comment": "Solid development, support d5 and prepare to castle"},
                    {
                        "move": "Bxc4",
                        "san": "Bxc4",
                        "comment": "White calmly regains the pawn with a lead in development",
                    },
                ],
            }
        ],
    },

    "queens-gambit-declined": {
        "name": "Queen's Gambit Declined",
        "side": "black",
        "description": "Black declines the pawn and builds a rock-solid center with ...d5 and ...e6.",
        "eco": "D30",
        "lines": [
            {
                "name": "Orthodox Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn opening"},
                    {"move": "d5", "san": "d5", "comment": "Black occupies the center"},
                    {"move": "c4", "san": "c4", "comment": "The Queen's Gambit"},
                    {"move": "e6", "san": "e6", "comment": "The classical Queen's Gambit Declined"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Increase pressure on d5"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and defend d5"},
                    {"move": "Bg5", "san": "Bg5", "comment": "Pin the knight, increasing pressure on d5"},
                    {"move": "Be7", "san": "Be7", "comment": "Break the pin and prepare to castle"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Complete kingside development"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle and finish development"},
                ],
            }
        ],
    },

    "sicilian-defense": {
        "name": "Sicilian Defense",
        "side": "black",
        "description": (
            "The most popular response to 1.e4; creates an imbalanced position where "
            "Black scores very well in practice."
        ),
        "eco": "B20",
        "lines": [
            {
                "name": "Open Sicilian",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn opening"},
                    {"move": "c5", "san": "c5", "comment": "Sicilian Defense - fight for d4 from the flank"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight, prepare d4"},
                    {"move": "d6", "san": "d6", "comment": "Support c5 and control e5"},
                    {"move": "d4", "san": "d4", "comment": "Open the center"},
                    {"move": "cxd4", "san": "cxd4", "comment": "Capture and open the c-file"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "Recapture with the knight"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and attack e4"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4 and develop another piece"},
                ],
            }
        ],
    },

    "ruy-lopez": {
        "name": "Ruy Lopez",
        "side": "white",
        "description": "The Spanish Opening - strategic pressure on Black's center and queenside.",
        "eco": "C60",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "e5", "san": "e5", "comment": "Symmetric response"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and attack e5"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Defend the pawn"},
                    {"move": "Bb5", "san": "Bb5", "comment": "The Ruy Lopez! Pressure on the c6 knight"},
                    {"move": "a6", "san": "a6", "comment": "Question the bishop"},
                    {"move": "Ba4", "san": "Ba4", "comment": "Maintain the pin on the knight"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and attack e4"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle for king safety"},
                    {"move": "Be7", "san": "Be7", "comment": "Prepare to castle"},
                    {"move": "Re1", "san": "Re1", "comment": "Support the e4 pawn and prepare d4"},
                ],
            }
        ],
    },

    "italian-game": {
        "name": "Italian Game",
        "side": "white",
        "description": "One of the oldest openings, leading to rich attacking and positional ideas.",
        "eco": "C50",
        "lines": [
            {
                "name": "Giuoco Piano",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn opening"},
                    {"move": "e5", "san": "e5", "comment": "Black mirrors"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight, attack center"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Black develops knight"},
                    {"move": "Bc4", "san": "Bc4", "comment": "Italian bishop to active square, targeting f7"},
                    {"move": "Bc5", "san": "Bc5", "comment": "Black mirrors the setup"},
                    {"move": "d3", "san": "d3", "comment": "Solid pawn structure and support for e4"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Black completes kingside development"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle kingside for safety"},
                ],
            }
        ],
    },

    "london-system": {
        "name": "London System",
        "side": "white",
        "description": "A solid system with Bf4/Bg3, very popular and scoring well at all levels.",
        "eco": "D02",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "d5", "san": "d5", "comment": "Mirror in the center"},
                    {"move": "Bf4", "san": "Bf4", "comment": "The London System! Develop bishop early"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop knight"},
                    {"move": "e3", "san": "e3", "comment": "Support the center and open the bishop"},
                    {"move": "e6", "san": "e6", "comment": "Prepare bishop development"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight"},
                    {"move": "Bd6", "san": "Bd6", "comment": "Challenge the bishop on f4"},
                    {"move": "Bg3", "san": "Bg3", "comment": "Retreat, maintaining the strong bishop"},
                ],
            }
        ],
    },

    "caro-kann": {
        "name": "Caro-Kann Defense",
        "side": "black",
        "description": "Very solid defense to 1.e4; Black keeps a healthy structure and good long-term chances.",
        "eco": "B10",
        "lines": [
            {
                "name": "Classical Variation",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "c6", "san": "c6", "comment": "Caro-Kann - support d5"},
                    {"move": "d4", "san": "d4", "comment": "White grabs central space"},
                    {"move": "d5", "san": "d5", "comment": "Challenge the center"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4"},
                    {"move": "dxe4", "san": "dxe4", "comment": "Exchange in the center"},
                    {"move": "Nxe4", "san": "Nxe4", "comment": "Recapture, keeping space"},
                    {"move": "Bf5", "san": "Bf5", "comment": "Develop bishop outside the pawn chain"},
                    {"move": "Ng3", "san": "Ng3", "comment": "Attack the bishop"},
                    {"move": "Bg6", "san": "Bg6", "comment": "Retreat while maintaining development"},
                ],
            }
        ],
    },

    "french-defense": {
        "name": "French Defense",
        "side": "black",
        "description": "A solid defense, challenging the center with ...d5 and aiming for queenside counterplay.",
        "eco": "C00",
        "lines": [
            {
                "name": "Classical Variation",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White's King's Pawn"},
                    {"move": "e6", "san": "e6", "comment": "The French Defense - prepare d5"},
                    {"move": "d4", "san": "d4", "comment": "White builds a strong center"},
                    {"move": "d5", "san": "d5", "comment": "Directly challenge the center"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend the e4 pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4 again"},
                    {"move": "Bg5", "san": "Bg5", "comment": "Pin the knight to increase pressure"},
                    {"move": "Be7", "san": "Be7", "comment": "Break the pin"},
                    {"move": "e5", "san": "e5", "comment": "Advance in the center, gaining space"},
                    {
                        "move": "Nfd7",
                        "san": "Nfd7",
                        "comment": "Retreat the knight, preparing c5 and f6 breaks",
                    },
                ],
            }
        ],
    },

    "nimzo-indian": {
        "name": "Nimzo-Indian Defense",
        "side": "black",
        "description": "Top-tier defense to 1.d4, pinning the c3 knight and fighting for dark squares.",
        "eco": "E20",
        "lines": [
            {
                "name": "Classical e3 Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn opening"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and control e4"},
                    {"move": "c4", "san": "c4", "comment": "Grab more central space"},
                    {"move": "e6", "san": "e6", "comment": "Prepare to develop the dark-squared bishop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Support the center"},
                    {"move": "Bb4", "san": "Bb4", "comment": "The Nimzo-Indian! Pin the c3 knight"},
                    {"move": "e3", "san": "e3", "comment": "Reinforce the center and open the bishop"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle and keep options flexible"},
                    {"move": "Bd3", "san": "Bd3", "comment": "Develop and eye the h7 square"},
                    {"move": "d5", "san": "d5", "comment": "Strike back in the center"},
                ],
            }
        ],
    },

    "slav-defense": {
        "name": "Slav Defense",
        "side": "black",
        "description": "A very reliable response to the Queen's Gambit, keeping the light-squared bishop free.",
        "eco": "D10",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "d5", "san": "d5", "comment": "Black mirrors in the center"},
                    {"move": "c4", "san": "c4", "comment": "The Queen's Gambit"},
                    {
                        "move": "c6",
                        "san": "c6",
                        "comment": "The Slav - support d5 without locking in the bishop",
                    },
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and support d4"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and pressure e4"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Increase pressure on d5"},
                    {"move": "dxc4", "san": "dxc4", "comment": "Capture the pawn, entering mainline theory"},
                    {"move": "a4", "san": "a4", "comment": "Prevent ...b5 and plan e3 to recapture"},
                    {"move": "Bf5", "san": "Bf5", "comment": "Develop the queen's bishop actively"},
                ],
            }
        ],
    },

    "kings-indian": {
        "name": "King's Indian Defense",
        "side": "black",
        "description": "A hypermodern defense allowing White a big center, then attacking it later.",
        "eco": "E60",
        "lines": [
            {
                "name": "Classical Variation",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop knight"},
                    {"move": "c4", "san": "c4", "comment": "Claim central space"},
                    {"move": "g6", "san": "g6", "comment": "Prepare to fianchetto the bishop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Develop knight"},
                    {"move": "Bg7", "san": "Bg7", "comment": "Fianchetto the bishop"},
                    {"move": "e4", "san": "e4", "comment": "Build a strong pawn center"},
                    {"move": "d6", "san": "d6", "comment": "Solid pawn structure and prepare ...e5"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Complete kingside development"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle for safety"},
                ],
            }
        ],
    },

    "grunfeld-defense": {
        "name": "Grünfeld Defense",
        "side": "black",
        "description": "A dynamic hypermodern defense where Black attacks White's large center.",
        "eco": "D70",
        "lines": [
            {
                "name": "Exchange Variation",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and control e4"},
                    {"move": "c4", "san": "c4", "comment": "Support d4 and grab space"},
                    {"move": "g6", "san": "g6", "comment": "Prepare to fianchetto the bishop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Reinforce the center"},
                    {"move": "d5", "san": "d5", "comment": "The Grünfeld! Hit the center immediately"},
                    {"move": "cxd5", "san": "cxd5", "comment": "Exchange in the center"},
                    {"move": "Nxd5", "san": "Nxd5", "comment": "Recapture and increase piece activity"},
                    {"move": "e4", "san": "e4", "comment": "Push the central majority forward"},
                    {"move": "Nxc3", "san": "Nxc3", "comment": "Eliminate a defender of the center"},
                    {"move": "bxc3", "san": "bxc3", "comment": "White keeps a huge pawn center"},
                    {
                        "move": "Bg7",
                        "san": "Bg7",
                        "comment": "Bishop targets the long diagonal and the center",
                    },
                ],
            }
        ],
    },

    "english-opening": {
        "name": "English Opening",
        "side": "white",
        "description": (
            "A flexible flank opening with excellent practical results and huge "
            "transpositional potential."
        ),
        "eco": "A10",
        "lines": [
            {
                "name": "Reversed Sicilian",
                "moves": [
                    {"move": "c4", "san": "c4", "comment": "The English - control d5 from the flank"},
                    {"move": "e5", "san": "e5", "comment": "Reversed Sicilian setup"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Develop and hit d5"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and attack e4"},
                    {"move": "g3", "san": "g3", "comment": "Plan to fianchetto the bishop"},
                    {"move": "d5", "san": "d5", "comment": "Immediate central strike"},
                    {"move": "cxd5", "san": "cxd5", "comment": "Exchange in the center"},
                    {"move": "Nxd5", "san": "Nxd5", "comment": "Recapture and gain activity"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Complete kingside fianchetto"},
                ],
            }
        ],
    },

    "scotch-game": {
        "name": "Scotch Game",
        "side": "white",
        "description": "An aggressive opening that strikes in the center with d4 early.",
        "eco": "C45",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "e5", "san": "e5", "comment": "Mirror response"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Defend e5"},
                    {"move": "d4", "san": "d4", "comment": "The Scotch Game! Strike in the center"},
                    {"move": "exd4", "san": "exd4", "comment": "Accept the challenge"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "Recapture centrally"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and attack e4"},
                    {"move": "Nxc6", "san": "Nxc6", "comment": "Trade knights"},
                    {
                        "move": "bxc6",
                        "san": "bxc6",
                        "comment": "Recapture, accepting doubled pawns for central control",
                    },
                ],
            }
        ],
    },

    "kings-gambit": {
        "name": "King's Gambit",
        "side": "white",
        "description": (
            "A very aggressive gambit where White sacrifices the f-pawn for rapid "
            "development and attack."
        ),
        "eco": "C30",
        "lines": [
            {
                "name": "King's Knight Gambit",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "e5", "san": "e5", "comment": "Black mirrors"},
                    {"move": "f4", "san": "f4", "comment": "The King's Gambit! Offer the f-pawn"},
                    {"move": "exf4", "san": "exf4", "comment": "Black accepts the gambit"},
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Attack the pawn on f4 and prepare to castle",
                    },
                    {"move": "g5", "san": "g5", "comment": "Defend the extra pawn and gain space"},
                    {"move": "h4", "san": "h4", "comment": "Challenge the g5 pawn and open the h-file"},
                    {"move": "g4", "san": "g4", "comment": "Advance, kicking the knight"},
                    {"move": "Ne5", "san": "Ne5", "comment": "Centralize the knight and target f7"},
                ],
            }
        ],
    },

    "vienna-game": {
        "name": "Vienna Game",
        "side": "white",
        "description": (
            "Flexible alternative to 2.Nf3, often allowing gambit-style play or "
            "quiet development."
        ),
        "eco": "C25",
        "lines": [
            {
                "name": "Vienna with Bc4",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "e5", "san": "e5", "comment": "Symmetric reply"},
                    {"move": "Nc3", "san": "Nc3", "comment": "The Vienna Game"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4 and develop"},
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "comment": "Develop, eyeing f7 (can transpose to Bishop's Opening systems)",
                    },
                    {"move": "Nc6", "san": "Nc6", "comment": "Reinforce e5 and develop"},
                    {"move": "d3", "san": "d3", "comment": "Support e4 and prepare Nf3"},
                ],
            }
        ],
    },

    "trompowsky-attack": {
        "name": "Trompowsky Attack",
        "side": "white",
        "description": "An offbeat yet strong system, forcing Black to decide about the f6 knight early.",
        "eco": "A45",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Natural development"},
                    {"move": "Bg5", "san": "Bg5", "comment": "The Trompowsky! Immediately attack the knight"},
                    {"move": "e6", "san": "e6", "comment": "Solid setup, preparing ...c5 or ...d5"},
                    {"move": "e4", "san": "e4", "comment": "Grab space and threaten e5"},
                    {"move": "h6", "san": "h6", "comment": "Ask the bishop the question"},
                    {"move": "Bxf6", "san": "Bxf6", "comment": "Double Black's pawns and give up the bishop pair"},
                    {"move": "Qxf6", "san": "Qxf6", "comment": "Recapture with the queen"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and prepare Bd3, O-O"},
                ],
            }
        ],
    },

    "kings-indian-attack": {
        "name": "King's Indian Attack",
        "side": "white",
        "description": (
            "A system for White resembling the King's Indian Defense setup, "
            "playable against many replies."
        ),
        "eco": "A07",
        "lines": [
            {
                "name": "Barcza System",
                "moves": [
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Flexible first move, avoiding early commitments",
                    },
                    {"move": "d5", "san": "d5", "comment": "Black occupies the center"},
                    {"move": "g3", "san": "g3", "comment": "Prepare to fianchetto the bishop"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and control e4"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Fianchetto the bishop"},
                    {"move": "e6", "san": "e6", "comment": "Solid development for Black"},
                    {"move": "O-O", "san": "O-O", "comment": "Castle kingside"},
                    {"move": "Be7", "san": "Be7", "comment": "Black prepares to castle"},
                    {"move": "d3", "san": "d3", "comment": "Support e4 and build the typical KIA structure"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles"},
                    {
                        "move": "Nbd2",
                        "san": "Nbd2",
                        "comment": "Reinforce e4 and prepare a kingside attack",
                    },
                ],
            }
        ],
    },

    "stafford-gambit": {
        "name": "Stafford Gambit",
        "side": "black",
        "description": "A very risky but popular blitz gambit arising from the Petrov Defense.",
        "eco": "C42",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "White opens with the King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Black mirrors with the King's Pawn",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "White develops the knight, attacking e5",
                    },
                    {"move": "Nf6", "san": "Nf6", "comment": "Black plays the Petrov Defense"},
                    {
                        "move": "Nxe5",
                        "san": "Nxe5",
                        "comment": "White accepts the gambit (the critical test)",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "The Stafford! Counterattack the knight on e5",
                    },
                    {"move": "Nxc6", "san": "Nxc6", "comment": "White grabs the knight"},
                    {"move": "dxc6", "san": "dxc6", "comment": "Black recaptures, opening the d-file"},
                    {
                        "move": "d3",
                        "san": "d3",
                        "comment": "White consolidates and opens the diagonal for the bishop",
                    },
                    {
                        "move": "Bc5",
                        "san": "Bc5",
                        "comment": "Develop with tempo, eyeing the f2 square",
                    },
                    {
                        "move": "Be2",
                        "san": "Be2",
                        "comment": "White defends and prepares to castle",
                    },
                    {
                        "move": "h5",
                        "san": "h5",
                        "comment": "Black starts the aggressive h-pawn march on the kingside",
                    },
                ],
            }
        ],
    },

    "fried-liver": {
        "name": "Fried Liver Attack",
        "side": "white",
        "description": (
            "Aggressive knight sacrifice against the Two Knights Defense; "
            "dangerous if Black misplays."
        ),
        "eco": "C57",
        "lines": [
            {
                "name": "Main Line (after the mistake 5...Nxd5)",
                "moves": [
                    {
                        "move": "e4",
                        "san": "e4",
                        "description": "Pawn to e4",
                        "comment": "King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "description": "Pawn to e5",
                        "comment": "Symmetric response",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "description": "Knight to f3",
                        "comment": "Develop knight",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "description": "Knight to c6",
                        "comment": "Black develops",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "description": "Bishop to c4",
                        "comment": "Italian Game setup",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "description": "Knight to f6",
                        "comment": "Two Knights Defense",
                    },
                    {
                        "move": "Ng5",
                        "san": "Ng5",
                        "description": "Knight to g5",
                        "comment": "Attack f7 again!",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "description": "Pawn to d5",
                        "comment": "Counter in the center (best)",
                    },
                    {
                        "move": "exd5",
                        "san": "exd5",
                        "description": "Pawn takes d5",
                        "comment": "Accept the pawn",
                    },
                    {
                        "move": "Nxd5",
                        "san": "Nxd5",
                        "description": "Knight takes d5",
                        "comment": "A natural but inaccurate recapture; 5...Na5 is the main defense",
                    },
                    {
                        "move": "Nxf7",
                        "san": "Nxf7",
                        "description": "Knight takes f7!",
                        "comment": "The Fried Liver! Sacrifice the knight",
                    },
                    {
                        "move": "Kxf7",
                        "san": "Kxf7",
                        "description": "King takes f7",
                        "comment": "Black is forced to accept the sacrifice",
                    },
                    {
                        "move": "Qf3+",
                        "san": "Qf3+",
                        "description": "Queen to f3 check",
                        "comment": "Attack the exposed king on the f-file and diagonal",
                    },
                ],
            }
        ],
    },

    "scholars-mate": {
        "name": "Scholar's Mate (Trap)",
        "side": "white",
        "description": "A quick 4-move checkmate pattern against f7; strong only if Black blunders.",
        "eco": "C20",
        "lines": [
            {
                "name": "Classic 4-Move Mate",
                "moves": [
                    {
                        "move": "e4",
                        "san": "e4",
                        "description": "Pawn to e4",
                        "comment": "Open with King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "description": "Pawn to e5",
                        "comment": "Black mirrors",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "description": "Bishop to c4",
                        "comment": "Attack the weak f7 square",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "description": "Knight to c6",
                        "comment": "Black develops normally",
                    },
                    {
                        "move": "Qh5",
                        "san": "Qh5",
                        "description": "Queen to h5",
                        "comment": "Threaten Qxf7# with queen and bishop",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "description": "Knight to f6??",
                        "comment": "A blunder that ignores the mate threat; better is 5...Qe7 or 5...g6",
                    },
                    {
                        "move": "Qxf7#",
                        "san": "Qxf7#",
                        "description": "Queen takes f7 - Checkmate!",
                        "comment": "Scholar's Mate: the queen is backed by the bishop on c4",
                    },
                ],
            }
        ],
    },

    # =======================
    # Extra openings (update)
    # =======================

    "pirc-defense": {
        "name": "Pirc Defense",
        "side": "black",
        "description": (
            "A hypermodern defense to 1.e4 where Black allows White a big center "
            "and later counterattacks it."
        ),
        "eco": "B08",
        "lines": [
            {
                "name": "Classical (Two Knights) System",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White grabs central space"},
                    {"move": "d6", "san": "d6", "comment": "Black avoids symmetry and prepares ...Nf6"},
                    {"move": "d4", "san": "d4", "comment": "White builds a strong pawn center"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack the e4 pawn and develop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4 and add more central control"},
                    {"move": "g6", "san": "g6", "comment": "Prepare to fianchetto the bishop on g7"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and protect the center"},
                    {"move": "Bg7", "san": "Bg7", "comment": "Fianchettoed bishop targets the center"},
                    {"move": "Be2", "san": "Be2", "comment": "Simple development, preparing to castle"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles kingside"},
                    {"move": "O-O", "san": "O-O", "comment": "White castles; both sides have flexible plans"},
                ],
            }
        ],
    },

    "modern-defense": {
        "name": "Modern Defense",
        "side": "black",
        "description": (
            "A flexible hypermodern system with ...g6 and ...Bg7, delaying the fight "
            "for the center."
        ),
        "eco": "B06",
        "lines": [
            {
                "name": "Standard Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White occupies the center"},
                    {"move": "g6", "san": "g6", "comment": "Modern Defense - prepare ...Bg7"},
                    {"move": "d4", "san": "d4", "comment": "Space advantage in the center"},
                    {"move": "Bg7", "san": "Bg7", "comment": "Fianchetto the bishop on the long diagonal"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Reinforce the center"},
                    {"move": "d6", "san": "d6", "comment": "Support e5 and c5 breaks"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and prepare to castle"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4 and complete kingside development"},
                ],
            }
        ],
    },

    "scandinavian-defense": {
        "name": "Scandinavian Defense",
        "side": "black",
        "description": (
            "An immediate challenge to White's e-pawn with 1...d5, leading to active piece play."
        ),
        "eco": "B01",
        "lines": [
            {
                "name": "Main Line (3...Qa5)",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White starts with the King's Pawn"},
                    {"move": "d5", "san": "d5", "comment": "Scandinavian! Directly challenge the center"},
                    {"move": "exd5", "san": "exd5", "comment": "White accepts the pawn"},
                    {"move": "Qxd5", "san": "Qxd5", "comment": "Black recaptures with the queen"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Develop with tempo, attacking the queen"},
                    {"move": "Qa5", "san": "Qa5", "comment": "Main line square for the queen"},
                    {"move": "d4", "san": "d4", "comment": "White claims more central space"},
                    {"move": "c6", "san": "c6", "comment": "Support d5 and prepare ...Bf5 or ...Bg4"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and protect d4"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and attack e4/d5"},
                ],
            }
        ],
    },

    "alekhine-defense": {
        "name": "Alekhine Defense",
        "side": "black",
        "description": (
            "Provocative defense where Black lets White advance central pawns to later attack them."
        ),
        "eco": "B02",
        "lines": [
            {
                "name": "Modern Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White occupies the center"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Alekhine Defense - attack e4 immediately"},
                    {"move": "e5", "san": "e5", "comment": "White chases the knight and gains space"},
                    {"move": "Nd5", "san": "Nd5", "comment": "Knight hops into the center"},
                    {"move": "d4", "san": "d4", "comment": "Support the center and gain more space"},
                    {"move": "d6", "san": "d6", "comment": "Strike at the pawn chain"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and reinforce e5/d4"},
                    {"move": "Bg4", "san": "Bg4", "comment": "Pin the knight and add pressure on d4"},
                ],
            }
        ],
    },

    "petrov-defense": {
        "name": "Petrov Defense (Russian Game)",
        "side": "black",
        "description": "Ultra-solid symmetrical defense to 1.e4, aiming for equality.",
        "eco": "C42",
        "lines": [
            {
                "name": "Classical Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White occupies the center"},
                    {"move": "e5", "san": "e5", "comment": "Black mirrors in the center"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Attack the e5 pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Petrov Defense - counterattack e4"},
                    {"move": "Nxe5", "san": "Nxe5", "comment": "Critical test: White grabs the pawn"},
                    {"move": "d6", "san": "d6", "comment": "Chase the knight and free the bishop"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Retreat to safety"},
                    {"move": "Nxe4", "san": "Nxe4", "comment": "Black recaptures in the center"},
                    {"move": "d4", "san": "d4", "comment": "White challenges the knight on e4"},
                    {"move": "d5", "san": "d5", "comment": "Support the knight and claim space"},
                    {"move": "Bd3", "san": "Bd3", "comment": "Develop and eye the h7 square"},
                    {"move": "Be7", "san": "Be7", "comment": "Black prepares to castle"},
                ],
            }
        ],
    },

    "philidor-defense": {
        "name": "Philidor Defense",
        "side": "black",
        "description": "A compact but somewhat passive defense with 2...d6.",
        "eco": "C41",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "White occupies the center"},
                    {"move": "e5", "san": "e5", "comment": "Black mirrors"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Attack the e5 pawn"},
                    {"move": "d6", "san": "d6", "comment": "Philidor - solid but cramped"},
                    {"move": "d4", "san": "d4", "comment": "White challenges the pawn on e5"},
                    {"move": "exd4", "san": "exd4", "comment": "Black exchanges in the center"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "White keeps central presence"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and hit e4"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4 and develop"},
                    {"move": "Be7", "san": "Be7", "comment": "Prepare to castle and complete development"},
                ],
            }
        ],
    },

    "four-knights-game": {
        "name": "Four Knights Game",
        "side": "white",
        "description": "Classical development for both sides, very solid and easy to learn.",
        "eco": "C47",
        "lines": [
            {
                "name": "Spanish Variation",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "e5", "san": "e5", "comment": "Symmetrical reply"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight, attack e5"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Defend e5 and develop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Four Knights structure"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Black completes the four knights"},
                    {"move": "Bb5", "san": "Bb5", "comment": "Spanish Variation, pinning the knight"},
                    {"move": "Bb4", "san": "Bb4", "comment": "Double pin, mirroring the idea"},
                    {"move": "O-O", "san": "O-O", "comment": "White castles into safety"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles; balanced position"},
                ],
            }
        ],
    },

    "reti-opening": {
        "name": "Réti Opening",
        "side": "white",
        "description": (
            "Hypermodern system starting with 1.Nf3, controlling the center from the flanks."
        ),
        "eco": "A04",
        "lines": [
            {
                "name": "Classical Réti",
                "moves": [
                    {"move": "Nf3", "san": "Nf3", "comment": "White develops a knight and keeps flexibility"},
                    {"move": "d5", "san": "d5", "comment": "Black occupies the center"},
                    {"move": "c4", "san": "c4", "comment": "Attack the d5 pawn from the flank"},
                    {"move": "e6", "san": "e6", "comment": "Support d5 and open the dark-squared bishop"},
                    {"move": "g3", "san": "g3", "comment": "Prepare to fianchetto the bishop"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and pressure e4"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Fianchetto bishop, eyeing the long diagonal"},
                    {"move": "Be7", "san": "Be7", "comment": "Black continues development"},
                    {"move": "O-O", "san": "O-O", "comment": "White castles"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles; flexible middlegame ahead"},
                ],
            }
        ],
    },

    "dutch-defense": {
        "name": "Dutch Defense",
        "side": "black",
        "description": (
            "Asymmetrical response to 1.d4 with 1...f5, aiming for kingside play and "
            "control of e4."
        ),
        "eco": "A80",
        "lines": [
            {
                "name": "Classical Dutch",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "White plays Queen's Pawn"},
                    {"move": "f5", "san": "f5", "comment": "Dutch Defense - fight for e4 immediately"},
                    {"move": "c4", "san": "c4", "comment": "Gain space and hit d5/e5"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and protect d5"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Natural development"},
                    {"move": "e6", "san": "e6", "comment": "Support d5 and open bishop"},
                    {"move": "g3", "san": "g3", "comment": "White prepares a king-side fianchetto"},
                    {"move": "Be7", "san": "Be7", "comment": "Black prepares to castle"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Fianchetto and pressure the long diagonal"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles; dynamic fight ahead"},
                ],
            }
        ],
    },

    "benko-gambit": {
        "name": "Benko Gambit",
        "side": "black",
        "description": (
            "A queenside pawn sacrifice against 1.d4, giving Black long-term pressure on "
            "the a- and b-files."
        ),
        "eco": "A57",
        "lines": [
            {
                "name": "Main Line Accepted",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "White plays Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and keep options"},
                    {"move": "c4", "san": "c4", "comment": "Support d4 and gain space"},
                    {"move": "c5", "san": "c5", "comment": "Benoni-style counter in the center"},
                    {"move": "d5", "san": "d5", "comment": "Advance and gain space"},
                    {"move": "b5", "san": "b5", "comment": "The Benko Gambit! Pawn sacrifice on the queenside"},
                    {"move": "cxb5", "san": "cxb5", "comment": "White accepts the gambit pawn"},
                    {"move": "a6", "san": "a6", "comment": "Offer a second pawn to open files"},
                    {"move": "bxa6", "san": "bxa6", "comment": "White keeps the extra pawn"},
                    {"move": "Bxa6", "san": "Bxa6", "comment": "Black gains active piece play"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Develop and support d5"},
                    {"move": "d6", "san": "d6", "comment": "Reinforce c5 and prepare ...g6, ...Bg7"},
                ],
            }
        ],
    },

    "modern-benoni": {
        "name": "Modern Benoni",
        "side": "black",
        "description": (
            "A dynamic defense where Black accepts a space disadvantage for active "
            "piece play and a queenside pawn majority."
        ),
        "eco": "A60",
        "lines": [
            {
                "name": "Fianchetto Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "White starts with Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and control e4"},
                    {"move": "c4", "san": "c4", "comment": "Gain central space"},
                    {"move": "c5", "san": "c5", "comment": "Benoni structure"},
                    {"move": "d5", "san": "d5", "comment": "Advance and gain space"},
                    {"move": "e6", "san": "e6", "comment": "Prepare to capture on d5"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Develop and support d5"},
                    {"move": "exd5", "san": "exd5", "comment": "Exchange and create pawn imbalances"},
                    {"move": "cxd5", "san": "cxd5", "comment": "White recaptures"},
                    {"move": "d6", "san": "d6", "comment": "Set up the typical Benoni structure"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight"},
                    {"move": "g6", "san": "g6", "comment": "Prepare to fianchetto the bishop"},
                ],
            }
        ],
    },

    "catalan-opening": {
        "name": "Catalan Opening",
        "side": "white",
        "description": (
            "Combines Queen's Gambit and Réti ideas with g3/Bg2, very popular at "
            "top level."
        ),
        "eco": "E04",
        "lines": [
            {
                "name": "Closed Catalan, Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "White plays Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Black develops"},
                    {"move": "c4", "san": "c4", "comment": "Queen's Gambit style setup"},
                    {"move": "e6", "san": "e6", "comment": "Prepare ...d5 and control d5"},
                    {"move": "g3", "san": "g3", "comment": "Catalan - prepare to fianchetto"},
                    {"move": "d5", "san": "d5", "comment": "Black occupies the center"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Bishop on long diagonal"},
                    {"move": "Be7", "san": "Be7", "comment": "Solid development"},
                    {"move": "Nf3", "san": "Nf3", "comment": "White develops and prepares to castle"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles"},
                    {"move": "O-O", "san": "O-O", "comment": "White castles; long-term pressure on queenside"},
                ],
            }
        ],
    },

    "queens-indian": {
        "name": "Queen's Indian Defense",
        "side": "black",
        "description": (
            "Solid Indian defense with ...b6 and ...Bb7/Ba6, fighting for light squares."
        ),
        "eco": "E12",
        "lines": [
            {
                "name": "Fianchetto Main Line",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop knight"},
                    {"move": "c4", "san": "c4", "comment": "Gain space and support d5"},
                    {"move": "e6", "san": "e6", "comment": "Prepare to develop the queen's bishop"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Flexible development"},
                    {"move": "b6", "san": "b6", "comment": "The Queen's Indian - fianchetto on b7"},
                    {"move": "g3", "san": "g3", "comment": "White fianchetto setup"},
                    {"move": "Bb7", "san": "Bb7", "comment": "Bishop eyes the e4 square"},
                    {"move": "Bg2", "san": "Bg2", "comment": "Both sides have fianchettoed bishops"},
                    {"move": "Be7", "san": "Be7", "comment": "Prepare to castle"},
                    {"move": "O-O", "san": "O-O", "comment": "White castles"},
                    {"move": "O-O", "san": "O-O", "comment": "Black castles; very solid structure"},
                ],
            }
        ],
    },

    "bogo-indian": {
        "name": "Bogo-Indian Defense",
        "side": "black",
        "description": "A flexible Indian defense with ...Bb4+ instead of ...b6.",
        "eco": "E11",
        "lines": [
            {
                "name": "Main Line with 4.Bd2",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop knight"},
                    {"move": "c4", "san": "c4", "comment": "Occupy the center"},
                    {"move": "e6", "san": "e6", "comment": "Prepare ...Bb4+ or ...b6"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Avoid the Nimzo-Indian"},
                    {"move": "Bb4+", "san": "Bb4+", "comment": "Check and pin the knight if Nc3"},
                    {"move": "Bd2", "san": "Bd2", "comment": "Block the check and attack the bishop"},
                    {"move": "Qe7", "san": "Qe7", "comment": "Defend b4 bishop and prepare ...d6/...d5"},
                    {"move": "g3", "san": "g3", "comment": "White prepares a kingside fianchetto"},
                    {"move": "Bxd2+", "san": "Bxd2+", "comment": "Exchange bishop for knight"},
                    {"move": "Qxd2", "san": "Qxd2", "comment": "Recapture, keeping a solid center"},
                ],
            }
        ],
    },

    "colle-system": {
        "name": "Colle System",
        "side": "white",
        "description": "System opening with a solid d4-e3-c3 structure aiming for an e4 break.",
        "eco": "D05",
        "lines": [
            {
                "name": "Main Setup",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "White plays Queen's Pawn"},
                    {"move": "d5", "san": "d5", "comment": "Black mirrors in the center"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and support d4"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop and fight for e4"},
                    {"move": "e3", "san": "e3", "comment": "Support d4 and open the diagonal for Bd3"},
                    {"move": "e6", "san": "e6", "comment": "Prepare ...c5 or ...Bd6"},
                    {"move": "Bd3", "san": "Bd3", "comment": "Typical Colle bishop, eyeing h7"},
                    {"move": "c5", "san": "c5", "comment": "Black strikes in the center"},
                    {"move": "c3", "san": "c3", "comment": "Support d4 and prepare Nbd2"},
                    {"move": "Nc6", "san": "Nc6", "comment": "More pressure on d4"},
                    {"move": "Nbd2", "san": "Nbd2", "comment": "Complete the Colle setup and prepare e4"},
                ],
            }
        ],
    },

    "stonewall-attack": {
        "name": "Stonewall Attack",
        "side": "white",
        "description": (
            "A setup based on pawns on d4-e3-f4-c3 and a kingside attack with Ne5 and Qf3."
        ),
        "eco": "D00",
        "lines": [
            {
                "name": "Typical Setup",
                "moves": [
                    {"move": "d4", "san": "d4", "comment": "Queen's Pawn"},
                    {"move": "d5", "san": "d5", "comment": "Black mirrors in the center"},
                    {"move": "e3", "san": "e3", "comment": "Support d4 and open bishop"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Develop knight"},
                    {"move": "Bd3", "san": "Bd3", "comment": "Eye the h7 square"},
                    {"move": "e6", "san": "e6", "comment": "Black develops solidly"},
                    {"move": "f4", "san": "f4", "comment": "Stonewall pawn structure forms"},
                    {"move": "c5", "san": "c5", "comment": "Black strikes at the center"},
                    {"move": "c3", "san": "c3", "comment": "Reinforce d4 and control b4"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Pressure on d4"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop knight, aiming for Ne5"},
                ],
            }
        ],
    },

    "sicilian-najdorf": {
        "name": "Sicilian Defense: Najdorf",
        "side": "black",
        "description": (
            "The iconic Sicilian branch with ...a6, one of the most heavily analyzed "
            "openings in chess."
        ),
        "eco": "B90",
        "lines": [
            {
                "name": "Main Starting Position",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "c5", "san": "c5", "comment": "Sicilian Defense"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and hit d4/e5"},
                    {"move": "d6", "san": "d6", "comment": "Support ...Nf6 and ...e5"},
                    {"move": "d4", "san": "d4", "comment": "Open Sicilian"},
                    {"move": "cxd4", "san": "cxd4", "comment": "Exchange in the center"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "White recaptures with the knight"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4 and develop"},
                    {"move": "a6", "san": "a6", "comment": "Najdorf! Control b5 and keep options"},
                ],
            }
        ],
    },

    "sicilian-dragon": {
        "name": "Sicilian Defense: Dragon",
        "side": "black",
        "description": (
            "Sharp Sicilian with ...g6 and ...Bg7; the Yugoslav Attack is one of the "
            "most dangerous replies."
        ),
        "eco": "B70",
        "lines": [
            {
                "name": "Yugoslav Attack Starting Position",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "c5", "san": "c5", "comment": "Sicilian Defense"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop and prepare d4"},
                    {"move": "d6", "san": "d6", "comment": "Dragon setup"},
                    {"move": "d4", "san": "d4", "comment": "Open Sicilian"},
                    {"move": "cxd4", "san": "cxd4", "comment": "Exchange in the center"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "White recaptures"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4 and develop"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4 and develop"},
                    {"move": "g6", "san": "g6", "comment": "Dragon - fianchetto the bishop"},
                    {"move": "Be3", "san": "Be3", "comment": "Yugoslav Attack setup"},
                ],
            }
        ],
    },

    "sicilian-sveshnikov": {
        "name": "Sicilian Defense: Sveshnikov",
        "side": "black",
        "description": (
            "Very modern, dynamic Sicilian line with ...Nc6 and ...e5, popular at the top level."
        ),
        "eco": "B33",
        "lines": [
            {
                "name": "Main Line",
                "moves": [
                    {"move": "e4", "san": "e4", "comment": "King's Pawn"},
                    {"move": "c5", "san": "c5", "comment": "Sicilian Defense"},
                    {"move": "Nf3", "san": "Nf3", "comment": "Develop"},
                    {"move": "Nc6", "san": "Nc6", "comment": "Sveshnikov move order"},
                    {"move": "d4", "san": "d4", "comment": "Open Sicilian"},
                    {"move": "cxd4", "san": "cxd4", "comment": "Exchange in the center"},
                    {"move": "Nxd4", "san": "Nxd4", "comment": "White recaptures"},
                    {"move": "Nf6", "san": "Nf6", "comment": "Attack e4"},
                    {"move": "Nc3", "san": "Nc3", "comment": "Defend e4"},
                    {"move": "e5", "san": "e5", "comment": "Kick the d4 knight and seize space"},
                    {"move": "Ndb5", "san": "Ndb5", "comment": "Knight heads for d6"},
                    {"move": "d6", "san": "d6", "comment": "Support the e5 pawn and open lines"},
                ],
            }
        ],
    },
}

# =====================================
# Minimal SAN -> from/to converter
# =====================================

FILES = "abcdefgh"
RANKS = "12345678"

PIECE_LETTER_TO_NAME = {
    "K": "King",
    "Q": "Queen",
    "R": "Rook",
    "B": "Bishop",
    "N": "Knight",
}

def square_to_coords(square: str):
    file_idx = FILES.index(square[0])
    rank_idx = RANKS.index(square[1])
    return file_idx, rank_idx

def coords_to_square(file_idx: int, rank_idx: int) -> str:
    return FILES[file_idx] + RANKS[rank_idx]

def initial_board():
    """Return starting position as dict: square -> (color, piece_name)."""
    board = {}
    # Pawns
    for f in FILES:
        board[f + "2"] = ("white", "Pawn")
        board[f + "7"] = ("black", "Pawn")
    # White pieces
    board["a1"] = ("white", "Rook")
    board["b1"] = ("white", "Knight")
    board["c1"] = ("white", "Bishop")
    board["d1"] = ("white", "Queen")
    board["e1"] = ("white", "King")
    board["f1"] = ("white", "Bishop")
    board["g1"] = ("white", "Knight")
    board["h1"] = ("white", "Rook")
    # Black pieces
    board["a8"] = ("black", "Rook")
    board["b8"] = ("black", "Knight")
    board["c8"] = ("black", "Bishop")
    board["d8"] = ("black", "Queen")
    board["e8"] = ("black", "King")
    board["f8"] = ("black", "Bishop")
    board["g8"] = ("black", "Knight")
    board["h8"] = ("black", "Rook")
    return board

def path_clear(board, from_sq: str, to_sq: str) -> bool:
    fx, fy = square_to_coords(from_sq)
    tx, ty = square_to_coords(to_sq)
    dx = tx - fx
    dy = ty - fy
    step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
    step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
    x, y = fx + step_x, fy + step_y
    while (x, y) != (tx, ty):
        sq = coords_to_square(x, y)
        if sq in board:
            return False
        x += step_x
        y += step_y
    return True

def can_move_piece(board, color: str, piece: str, from_sq: str, to_sq: str, is_capture: bool) -> bool:
    if from_sq not in board:
        return False
    c, p = board[from_sq]
    if c != color or p != piece:
        return False
    if to_sq in board and board[to_sq][0] == color:
        return False

    fx, fy = square_to_coords(from_sq)
    tx, ty = square_to_coords(to_sq)
    dx = tx - fx
    dy = ty - fy
    adx = abs(dx)
    ady = abs(dy)

    if piece == "Knight":
        return (adx, ady) in ((1, 2), (2, 1))
    if piece == "King":
        return max(adx, ady) == 1
    if piece == "Bishop":
        if adx == ady and adx != 0:
            return path_clear(board, from_sq, to_sq)
        return False
    if piece == "Rook":
        if (dx == 0) != (dy == 0):
            return path_clear(board, from_sq, to_sq)
        return False
    if piece == "Queen":
        if (adx == ady and adx != 0) or ((dx == 0) != (dy == 0)):
            return path_clear(board, from_sq, to_sq)
        return False
    return False

def can_move_pawn(board, color: str, from_sq: str, to_sq: str, is_capture: bool) -> bool:
    if from_sq not in board:
        return False
    c, p = board[from_sq]
    if c != color or p != "Pawn":
        return False
    if to_sq in board and board[to_sq][0] == color:
        return False

    fx, fy = square_to_coords(from_sq)
    tx, ty = square_to_coords(to_sq)
    dx = tx - fx
    dy = ty - fy
    direction = 1 if color == "white" else -1

    if is_capture:
        # diagonal capture
        if dy == direction and abs(dx) == 1 and to_sq in board and board[to_sq][0] != color:
            return True
        return False
    else:
        # forward move
        if dx != 0:
            return False
        # one step
        if dy == direction and to_sq not in board:
            return True
        # two steps from starting rank
        start_rank = "2" if color == "white" else "7"
        mid_sq = coords_to_square(fx, fy + direction)
        if dy == 2 * direction and from_sq[1] == start_rank and to_sq not in board and mid_sq not in board:
            return True
        return False

def apply_castling(board, color: str, side: str):
    if color == "white":
        king_from = "e1"
        if side == "king":
            king_to, rook_from, rook_to = "g1", "h1", "f1"
        else:
            king_to, rook_from, rook_to = "c1", "a1", "d1"
    else:
        king_from = "e8"
        if side == "king":
            king_to, rook_from, rook_to = "g8", "h8", "f8"
        else:
            king_to, rook_from, rook_to = "c8", "a8", "d8"

    board[king_to] = (color, "King")
    if king_from in board:
        del board[king_from]
    board[rook_to] = (color, "Rook")
    if rook_from in board:
        del board[rook_from]
    return "King", king_from, king_to

def apply_san(board, san: str, color: str):
    """Apply a very simple SAN-like move to board, return (piece_name, from_sq, to_sq)."""
    raw = san.replace("+", "").replace("#", "")

    # Castling
    if raw in ("O-O", "0-0"):
        return apply_castling(board, color, "king")
    if raw in ("O-O-O", "0-0-0"):
        return apply_castling(board, color, "queen")

    # Piece or pawn?
    first = raw[0]
    is_capture = "x" in raw

    if first in PIECE_LETTER_TO_NAME:
        # Piece move like Nf3, Nxd5, Bxc4, Qxf7
        piece_name = PIECE_LETTER_TO_NAME[first]
        dest = raw[-2:]
        # find candidate pieces
        candidates = []
        for sq, (c, p) in board.items():
            if c == color and p == piece_name:
                if can_move_piece(board, color, piece_name, sq, dest, is_capture):
                    candidates.append(sq)
        if not candidates:
            raise ValueError(f"No legal {piece_name} move for {san}")
        from_sq = candidates[0]
        # update board
        if dest in board:
            del board[dest]
        board[dest] = (color, piece_name)
        del board[from_sq]
        return piece_name, from_sq, dest

    # Pawn move
    # examples: e4, d5, exd5, cxd4
    dest = raw[-2:]
    src_file_hint = None
    if is_capture:
        src_file_hint = raw[0]

    candidates = []
    for sq, (c, p) in board.items():
        if c == color and p == "Pawn":
            if src_file_hint is not None and sq[0] != src_file_hint:
                continue
            if can_move_pawn(board, color, sq, dest, is_capture):
                candidates.append(sq)
    if not candidates:
        raise ValueError(f"No legal pawn move for {san}")
    from_sq = candidates[0]
    if dest in board:
        del board[dest]
    board[dest] = (color, "Pawn")
    del board[from_sq]
    return "Pawn", from_sq, dest

def annotate_openings_with_long_moves():
    """Mutate OPENINGS_DATABASE in place, adding from/to/piece and replacing move text."""
    for opening in OPENINGS_DATABASE.values():
        for line in opening.get("lines", []):
            board = initial_board()
            color = "white"
            for mv in line.get("moves", []):
                san = mv.get("san", mv.get("move"))
                piece_name, from_sq, to_sq = apply_san(board, san, color)
                mv["piece"] = piece_name
                mv["from_square"] = from_sq
                mv["to_square"] = to_sq
                mv["move"] = f"{piece_name} {from_sq} -> {to_sq}"
                color = "black" if color == "white" else "white"

# Run annotation at import time so all moves are already expanded.
annotate_openings_with_long_moves()
