"""
Chess Openings Database
Contains popular, high-scoring chess openings with moves and annotations.

Notes:
- Openings are roughly ordered from higher practical win rate / reliability at club & master level
  toward more dubious traps.
- Win-rate ordering is approximate and based on large database statistics; exact percentages
  depend on rating range and time control.
"""

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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn opening",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black stakes claim in the center",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: The Queen's Gambit! Offer the c-pawn to deflect Black's d-pawn",
                    },
                    {
                        "move": "dxc4",
                        "san": "dxc4",
                        "comment": "Pawn d5 -> c4: Black accepts the gambit by capturing the c-pawn",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and prepare to recapture on c4",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and fight for the e4 square",
                    },
                    {
                        "move": "e3",
                        "san": "e3",
                        "comment": "Pawn e2 -> e3: Open the diagonal for the bishop to recapture on c4",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Solid development, support d5 and prepare to castle",
                    },
                    {
                        "move": "Bxc4",
                        "san": "Bxc4",
                        "comment": "Bishop f1 -> c4: White calmly regains the pawn with a lead in development",
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn opening",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black occupies the center",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: The Queen's Gambit",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: The classical Queen's Gambit Declined",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Increase pressure on d5",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and defend d5",
                    },
                    {
                        "move": "Bg5",
                        "san": "Bg5",
                        "comment": "Bishop c1 -> g5: Pin the knight, increasing pressure on d5",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Break the pin and prepare to castle",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Complete kingside development",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles and finishes development",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn opening",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Sicilian Defense - fight for d4 from the flank",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight, prepare d4",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Support c5 and control e5",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Open the center",
                    },
                    {
                        "move": "cxd4",
                        "san": "cxd4",
                        "comment": "Pawn c5 -> d4: Capture and open the c-file",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: Recapture with the knight",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and attack e4",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4 and develop another piece",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Symmetric response",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and attack e5",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Defend the e5 pawn",
                    },
                    {
                        "move": "Bb5",
                        "san": "Bb5",
                        "comment": "Bishop f1 -> b5: The Ruy Lopez! Pressure on the c6 knight",
                    },
                    {
                        "move": "a6",
                        "san": "a6",
                        "comment": "Pawn a7 -> a6: Question the bishop",
                    },
                    {
                        "move": "Ba4",
                        "san": "Ba4",
                        "comment": "Bishop b5 -> a4: Maintain the pin on the knight",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and attack e4",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: Castle for king safety",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Prepare to castle",
                    },
                    {
                        "move": "Re1",
                        "san": "Re1",
                        "comment": "Rook f1 -> e1: Support the e4 pawn and prepare d4",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn opening",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Black mirrors",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight, attack center",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Black develops knight",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "comment": "Bishop f1 -> c4: Italian bishop to active square, targeting f7",
                    },
                    {
                        "move": "Bc5",
                        "san": "Bc5",
                        "comment": "Bishop f8 -> c5: Black mirrors the setup",
                    },
                    {
                        "move": "d3",
                        "san": "d3",
                        "comment": "Pawn d2 -> d3: Solid pawn structure and support for e4",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Black completes kingside development",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: Castle kingside for safety",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Mirror in the center",
                    },
                    {
                        "move": "Bf4",
                        "san": "Bf4",
                        "comment": "Bishop c1 -> f4: The London System! Develop bishop early",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop knight",
                    },
                    {
                        "move": "e3",
                        "san": "e3",
                        "comment": "Pawn e2 -> e3: Support the center and open the bishop",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare bishop development",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight",
                    },
                    {
                        "move": "Bd6",
                        "san": "Bd6",
                        "comment": "Bishop f8 -> d6: Challenge the bishop on f4",
                    },
                    {
                        "move": "Bg3",
                        "san": "Bg3",
                        "comment": "Bishop f4 -> g3: Retreat, maintaining the strong bishop",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "c6",
                        "san": "c6",
                        "comment": "Pawn c7 -> c6: Caro-Kann - support d5",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White grabs central space",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Challenge the center",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4",
                    },
                    {
                        "move": "dxe4",
                        "san": "dxe4",
                        "comment": "Pawn d5 -> e4: Exchange in the center",
                    },
                    {
                        "move": "Nxe4",
                        "san": "Nxe4",
                        "comment": "Knight c3 -> e4: Recapture, keeping space",
                    },
                    {
                        "move": "Bf5",
                        "san": "Bf5",
                        "comment": "Bishop c8 -> f5: Develop bishop outside the pawn chain",
                    },
                    {
                        "move": "Ng3",
                        "san": "Ng3",
                        "comment": "Knight e4 -> g3: Attack the bishop",
                    },
                    {
                        "move": "Bg6",
                        "san": "Bg6",
                        "comment": "Bishop f5 -> g6: Retreat while maintaining development",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White's King's Pawn",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: The French Defense - prepare d5",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White builds a strong center",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Directly challenge the center",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend the e4 pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4 again",
                    },
                    {
                        "move": "Bg5",
                        "san": "Bg5",
                        "comment": "Bishop c1 -> g5: Pin the knight to increase pressure",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Break the pin",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e4 -> e5: Advance in the center, gaining space",
                    },
                    {
                        "move": "Nfd7",
                        "san": "Nfd7",
                        "comment": "Knight f6 -> d7: Retreat the knight, preparing c5 and f6 breaks",
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn opening",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and control e4",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Grab more central space",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare to develop the dark-squared bishop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Support the center",
                    },
                    {
                        "move": "Bb4",
                        "san": "Bb4",
                        "comment": "Bishop f8 -> b4: The Nimzo-Indian! Pin the c3 knight",
                    },
                    {
                        "move": "e3",
                        "san": "e3",
                        "comment": "Pawn e2 -> e3: Reinforce the center and open the bishop",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Castle and keep options flexible",
                    },
                    {
                        "move": "Bd3",
                        "san": "Bd3",
                        "comment": "Bishop f1 -> d3: Develop and eye the h7 square",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Strike back in the center",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black mirrors in the center",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: The Queen's Gambit",
                    },
                    {
                        "move": "c6",
                        "san": "c6",
                        "comment": "Pawn c7 -> c6: The Slav - support d5 without locking in the bishop",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and support d4",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and pressure e4",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Increase pressure on d5",
                    },
                    {
                        "move": "dxc4",
                        "san": "dxc4",
                        "comment": "Pawn d5 -> c4: Capture the pawn, entering mainline theory",
                    },
                    {
                        "move": "a4",
                        "san": "a4",
                        "comment": "Pawn a2 -> a4: Prevent ...b5 and plan e3 to recapture",
                    },
                    {
                        "move": "Bf5",
                        "san": "Bf5",
                        "comment": "Bishop c8 -> f5: Develop the queen's bishop actively",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop knight",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Claim central space",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Prepare to fianchetto the bishop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Develop knight",
                    },
                    {
                        "move": "Bg7",
                        "san": "Bg7",
                        "comment": "Bishop f8 -> g7: Fianchetto the bishop",
                    },
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: Build a strong pawn center",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Solid pawn structure and prepare ...e5",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Complete kingside development",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Castle for safety",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and control e4",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Support d4 and grab space",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Prepare to fianchetto the bishop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Reinforce the center",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: The Grünfeld! Hit the center immediately",
                    },
                    {
                        "move": "cxd5",
                        "san": "cxd5",
                        "comment": "Pawn c4 -> d5: Exchange in the center",
                    },
                    {
                        "move": "Nxd5",
                        "san": "Nxd5",
                        "comment": "Knight f6 -> d5: Recapture and increase piece activity",
                    },
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: Push the central majority forward",
                    },
                    {
                        "move": "Nxc3",
                        "san": "Nxc3",
                        "comment": "Knight d5 -> c3: Eliminate a defender of the center",
                    },
                    {
                        "move": "bxc3",
                        "san": "bxc3",
                        "comment": "Pawn b2 -> c3: White keeps a huge pawn center",
                    },
                    {
                        "move": "Bg7",
                        "san": "Bg7",
                        "comment": "Bishop f8 -> g7: Bishop targets the long diagonal and the center",
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
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: The English - control d5 from the flank",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Reversed Sicilian setup",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Develop and hit d5",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and attack e4",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: Plan to fianchetto the bishop",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Immediate central strike",
                    },
                    {
                        "move": "cxd5",
                        "san": "cxd5",
                        "comment": "Pawn c4 -> d5: Exchange in the center",
                    },
                    {
                        "move": "Nxd5",
                        "san": "Nxd5",
                        "comment": "Knight f6 -> d5: Recapture and gain activity",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Complete kingside fianchetto",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Mirror response",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Defend e5",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: The Scotch Game! Strike in the center",
                    },
                    {
                        "move": "exd4",
                        "san": "exd4",
                        "comment": "Pawn e5 -> d4: Accept the challenge",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: Recapture centrally",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and attack e4",
                    },
                    {
                        "move": "Nxc6",
                        "san": "Nxc6",
                        "comment": "Knight d4 -> c6: Trade knights",
                    },
                    {
                        "move": "bxc6",
                        "san": "bxc6",
                        "comment": "Pawn b7 -> c6: Recapture, accepting doubled pawns for central control",
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Black mirrors",
                    },
                    {
                        "move": "f4",
                        "san": "f4",
                        "comment": "Pawn f2 -> f4: The King's Gambit! Offer the f-pawn",
                    },
                    {
                        "move": "exf4",
                        "san": "exf4",
                        "comment": "Pawn e5 -> f4: Black accepts the gambit",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Attack the pawn on f4 and prepare to castle",
                    },
                    {
                        "move": "g5",
                        "san": "g5",
                        "comment": "Pawn g7 -> g5: Defend the extra pawn and gain space",
                    },
                    {
                        "move": "h4",
                        "san": "h4",
                        "comment": "Pawn h2 -> h4: Challenge the g5 pawn and open the h-file",
                    },
                    {
                        "move": "g4",
                        "san": "g4",
                        "comment": "Pawn g5 -> g4: Advance, kicking the knight",
                    },
                    {
                        "move": "Ne5",
                        "san": "Ne5",
                        "comment": "Knight f3 -> e5: Centralize the knight and target f7",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Symmetric reply",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: The Vienna Game",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4 and develop",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "comment": "Bishop f1 -> c4: Develop, eyeing f7 (can transpose to Bishop's Opening systems)",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Reinforce e5 and develop",
                    },
                    {
                        "move": "d3",
                        "san": "d3",
                        "comment": "Pawn d2 -> d3: Support e4 and prepare Nf3",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Natural development",
                    },
                    {
                        "move": "Bg5",
                        "san": "Bg5",
                        "comment": "Bishop c1 -> g5: The Trompowsky! Immediately attack the knight",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Solid setup, preparing ...c5 or ...d5",
                    },
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: Grab space and threaten e5",
                    },
                    {
                        "move": "h6",
                        "san": "h6",
                        "comment": "Pawn h7 -> h6: Ask the bishop the question",
                    },
                    {
                        "move": "Bxf6",
                        "san": "Bxf6",
                        "comment": "Bishop g5 -> f6: Double Black's pawns and give up the bishop pair",
                    },
                    {
                        "move": "Qxf6",
                        "san": "Qxf6",
                        "comment": "Queen d8 -> f6: Recapture with the queen",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and prepare Bd3, O-O",
                    },
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
                        "comment": "Knight g1 -> f3: Flexible first move, avoiding early commitments",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black occupies the center",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: Prepare to fianchetto the bishop",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and control e4",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Fianchetto the bishop",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Solid development for Black",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Black prepares to castle",
                    },
                    {
                        "move": "d3",
                        "san": "d3",
                        "comment": "Pawn d2 -> d3: Support e4 and build the typical KIA structure",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles",
                    },
                    {
                        "move": "Nbd2",
                        "san": "Nbd2",
                        "comment": "Knight b1 -> d2: Reinforce e4 and prepare a kingside attack",
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
                        "comment": "Pawn e2 -> e4: White opens with the King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Black mirrors with the King's Pawn",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: White develops the knight, attacking e5",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Black plays the Petrov Defense",
                    },
                    {
                        "move": "Nxe5",
                        "san": "Nxe5",
                        "comment": "Knight f3 -> e5: White accepts the gambit (the critical test)",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: The Stafford! Counterattack the knight on e5",
                    },
                    {
                        "move": "Nxc6",
                        "san": "Nxc6",
                        "comment": "Knight e5 -> c6: White grabs the knight",
                    },
                    {
                        "move": "dxc6",
                        "san": "dxc6",
                        "comment": "Pawn d7 -> c6: Black recaptures, opening the d-file",
                    },
                    {
                        "move": "d3",
                        "san": "d3",
                        "comment": "Pawn d2 -> d3: White consolidates and opens the diagonal for the bishop",
                    },
                    {
                        "move": "Bc5",
                        "san": "Bc5",
                        "comment": "Bishop f8 -> c5: Develop with tempo, eyeing the f2 square",
                    },
                    {
                        "move": "Be2",
                        "san": "Be2",
                        "comment": "Bishop f1 -> e2: White defends and prepares to castle",
                    },
                    {
                        "move": "h5",
                        "san": "h5",
                        "comment": "Pawn h7 -> h5: Black starts the aggressive h-pawn march on the kingside",
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
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "description": "Pawn to e5",
                        "comment": "Pawn e7 -> e5: Symmetric response",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "description": "Knight to f3",
                        "comment": "Knight g1 -> f3: Develop knight",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "description": "Knight to c6",
                        "comment": "Knight b8 -> c6: Black develops",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "description": "Bishop to c4",
                        "comment": "Bishop f1 -> c4: Italian Game setup",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "description": "Knight to f6",
                        "comment": "Knight g8 -> f6: Two Knights Defense",
                    },
                    {
                        "move": "Ng5",
                        "san": "Ng5",
                        "description": "Knight to g5",
                        "comment": "Knight f3 -> g5: Attack f7 again!",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "description": "Pawn to d5",
                        "comment": "Pawn d7 -> d5: Counter in the center (best)",
                    },
                    {
                        "move": "exd5",
                        "san": "exd5",
                        "description": "Pawn takes d5",
                        "comment": "Pawn e4 -> d5: Accept the pawn",
                    },
                    {
                        "move": "Nxd5",
                        "san": "Nxd5",
                        "description": "Knight takes d5",
                        "comment": "Knight f6 -> d5: A natural but inaccurate recapture; 5...Na5 is the main defense",
                    },
                    {
                        "move": "Nxf7",
                        "san": "Nxf7",
                        "description": "Knight takes f7!",
                        "comment": "Knight g5 -> f7: The Fried Liver! Sacrifice the knight",
                    },
                    {
                        "move": "Kxf7",
                        "san": "Kxf7",
                        "description": "King takes f7",
                        "comment": "King e8 -> f7: Black is forced to accept the sacrifice",
                    },
                    {
                        "move": "Qf3+",
                        "san": "Qf3+",
                        "description": "Queen to f3 check",
                        "comment": "Queen d1 -> f3: Attack the exposed king on the f-file and diagonal",
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
                        "comment": "Pawn e2 -> e4: Open with King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "description": "Pawn to e5",
                        "comment": "Pawn e7 -> e5: Black mirrors",
                    },
                    {
                        "move": "Bc4",
                        "san": "Bc4",
                        "description": "Bishop to c4",
                        "comment": "Bishop f1 -> c4: Attack the weak f7 square",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "description": "Knight to c6",
                        "comment": "Knight b8 -> c6: Black develops normally",
                    },
                    {
                        "move": "Qh5",
                        "san": "Qh5",
                        "description": "Queen to h5",
                        "comment": "Queen d1 -> h5: Threaten Qxf7# with queen and bishop",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "description": "Knight to f6??",
                        "comment": "Knight g8 -> f6: A blunder that ignores the mate threat; better is 5...Qe7 or 5...g6",
                    },
                    {
                        "move": "Qxf7#",
                        "san": "Qxf7#",
                        "description": "Queen takes f7 - Checkmate!",
                        "comment": "Queen h5 -> f7: Scholar's Mate: the queen is backed by the bishop on c4",
                    },
                ],
            }
        ],
    },
}

# Additional openings appended to the database
OPENINGS_DATABASE.update({
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White grabs central space",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Black avoids symmetry and prepares ...Nf6",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White builds a strong pawn center",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack the e4 pawn and develop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4 and add more central control",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Prepare to fianchetto the bishop on g7",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and protect the center",
                    },
                    {
                        "move": "Bg7",
                        "san": "Bg7",
                        "comment": "Bishop f8 -> g7: Fianchettoed bishop targets the center",
                    },
                    {
                        "move": "Be2",
                        "san": "Be2",
                        "comment": "Bishop f1 -> e2: Simple development, preparing to castle",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles kingside",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles; both sides have flexible plans",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White occupies the center",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Modern Defense - prepare ...Bg7",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Space advantage in the center",
                    },
                    {
                        "move": "Bg7",
                        "san": "Bg7",
                        "comment": "Bishop f8 -> g7: Fianchetto the bishop on the long diagonal",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Reinforce the center",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Support e5 and c5 breaks",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and prepare to castle",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4 and complete kingside development",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White starts with the King's Pawn",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Scandinavian! Directly challenge the center",
                    },
                    {
                        "move": "exd5",
                        "san": "exd5",
                        "comment": "Pawn e4 -> d5: White accepts the pawn",
                    },
                    {
                        "move": "Qxd5",
                        "san": "Qxd5",
                        "comment": "Queen d8 -> d5: Black recaptures with the queen",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Develop with tempo, attacking the queen",
                    },
                    {
                        "move": "Qa5",
                        "san": "Qa5",
                        "comment": "Queen d5 -> a5: Main line square for the queen",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White claims more central space",
                    },
                    {
                        "move": "c6",
                        "san": "c6",
                        "comment": "Pawn c7 -> c6: Support d5 and prepare ...Bf5 or ...Bg4",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and protect d4",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and attack e4/d5",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White occupies the center",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Alekhine Defense - attack e4 immediately",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e4 -> e5: White chases the knight and gains space",
                    },
                    {
                        "move": "Nd5",
                        "san": "Nd5",
                        "comment": "Knight f6 -> d5: Knight hops into the center",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Support the center and gain more space",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Strike at the pawn chain",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and reinforce e5/d4",
                    },
                    {
                        "move": "Bg4",
                        "san": "Bg4",
                        "comment": "Bishop c8 -> g4: Pin the knight and add pressure on d4",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White occupies the center",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Black mirrors in the center",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Attack the e5 pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Petrov Defense - counterattack e4",
                    },
                    {
                        "move": "Nxe5",
                        "san": "Nxe5",
                        "comment": "Knight f3 -> e5: Critical test: White grabs the pawn",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Chase the knight and free the bishop",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight e5 -> f3: Retreat to safety",
                    },
                    {
                        "move": "Nxe4",
                        "san": "Nxe4",
                        "comment": "Knight f6 -> e4: Black recaptures in the center",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White challenges the knight on e4",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d6 -> d5: Support the knight and claim space",
                    },
                    {
                        "move": "Bd3",
                        "san": "Bd3",
                        "comment": "Bishop f1 -> d3: Develop and eye the h7 square",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Black prepares to castle",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: White occupies the center",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Black mirrors",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Attack the e5 pawn",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Philidor - solid but cramped",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White challenges the pawn on e5",
                    },
                    {
                        "move": "exd4",
                        "san": "exd4",
                        "comment": "Pawn e5 -> d4: Black exchanges in the center",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: White keeps central presence",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and hit e4",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4 and develop",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Prepare to castle and complete development",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Symmetrical reply",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight, attack e5",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Defend e5 and develop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Four Knights structure",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Black completes the four knights",
                    },
                    {
                        "move": "Bb5",
                        "san": "Bb5",
                        "comment": "Bishop f1 -> b5: Spanish Variation, pinning the knight",
                    },
                    {
                        "move": "Bb4",
                        "san": "Bb4",
                        "comment": "Bishop f8 -> b4: Double pin, mirroring the idea",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles into safety",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles; balanced position",
                    },
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
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: White develops a knight and keeps flexibility",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black occupies the center",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Attack the d5 pawn from the flank",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Support d5 and open the dark-squared bishop",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: Prepare to fianchetto the bishop",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and pressure e4",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Fianchetto bishop, eyeing the long diagonal",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Black continues development",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles; flexible middlegame ahead",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White plays Queen's Pawn",
                    },
                    {
                        "move": "f5",
                        "san": "f5",
                        "comment": "Pawn f7 -> f5: Dutch Defense - fight for e4 immediately",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Gain space and hit d5/e5",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and protect d5",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Natural development",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Support d5 and open bishop",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: White prepares a kingside fianchetto",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Black prepares to castle",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Fianchetto and pressure the long diagonal",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles; dynamic fight ahead",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White plays Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and keep options",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Support d4 and gain space",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Benoni-style counter in the center",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d4 -> d5: Advance and gain space",
                    },
                    {
                        "move": "b5",
                        "san": "b5",
                        "comment": "Pawn b7 -> b5: The Benko Gambit! Pawn sacrifice on the queenside",
                    },
                    {
                        "move": "cxb5",
                        "san": "cxb5",
                        "comment": "Pawn c4 -> b5: White accepts the gambit pawn",
                    },
                    {
                        "move": "a6",
                        "san": "a6",
                        "comment": "Pawn a7 -> a6: Offer a second pawn to open files",
                    },
                    {
                        "move": "bxa6",
                        "san": "bxa6",
                        "comment": "Pawn b5 -> a6: White keeps the extra pawn",
                    },
                    {
                        "move": "Bxa6",
                        "san": "Bxa6",
                        "comment": "Bishop f1 -> a6: (In practice Black's bishop from g7 or c8 captures; simplified here as bishop capture)",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Develop and support d5",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Reinforce c5 and prepare ...g6, ...Bg7",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White starts with Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and control e4",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Gain central space",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Benoni structure",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d4 -> d5: Advance and gain space",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare to capture on d5",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Develop and support d5",
                    },
                    {
                        "move": "exd5",
                        "san": "exd5",
                        "comment": "Pawn e6 -> d5: Exchange and create pawn imbalances",
                    },
                    {
                        "move": "cxd5",
                        "san": "cxd5",
                        "comment": "Pawn c4 -> d5: White recaptures",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Set up the typical Benoni structure",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Prepare to fianchetto the bishop",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White plays Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Black develops",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Queen's Gambit style setup",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare ...d5 and control d5",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: Catalan - prepare to fianchetto",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black occupies the center",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Bishop on long diagonal",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Solid development",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: White develops and prepares to castle",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles; long-term pressure on queenside",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop knight",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Gain space and support d5",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare to develop the queen's bishop",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Flexible development",
                    },
                    {
                        "move": "b6",
                        "san": "b6",
                        "comment": "Pawn b7 -> b6: The Queen's Indian - fianchetto on b7",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: White fianchetto setup",
                    },
                    {
                        "move": "Bb7",
                        "san": "Bb7",
                        "comment": "Bishop c8 -> b7: Bishop eyes the e4 square",
                    },
                    {
                        "move": "Bg2",
                        "san": "Bg2",
                        "comment": "Bishop f1 -> g2: Both sides have fianchettoed bishops",
                    },
                    {
                        "move": "Be7",
                        "san": "Be7",
                        "comment": "Bishop f8 -> e7: Prepare to castle",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e1 -> g1 & Rook h1 -> f1: White castles",
                    },
                    {
                        "move": "O-O",
                        "san": "O-O",
                        "comment": "King e8 -> g8 & Rook h8 -> f8: Black castles; very solid structure",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop knight",
                    },
                    {
                        "move": "c4",
                        "san": "c4",
                        "comment": "Pawn c2 -> c4: Occupy the center",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare ...Bb4+ or ...b6",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Avoid the Nimzo-Indian",
                    },
                    {
                        "move": "Bb4+",
                        "san": "Bb4+",
                        "comment": "Bishop f8 -> b4: Check and pin the knight if Nc3",
                    },
                    {
                        "move": "Bd2",
                        "san": "Bd2",
                        "comment": "Bishop c1 -> d2: Block the check and attack the bishop",
                    },
                    {
                        "move": "Qe7",
                        "san": "Qe7",
                        "comment": "Queen d8 -> e7: Defend b4 bishop and prepare ...d6/...d5",
                    },
                    {
                        "move": "g3",
                        "san": "g3",
                        "comment": "Pawn g2 -> g3: White prepares a kingside fianchetto",
                    },
                    {
                        "move": "Bxd2+",
                        "san": "Bxd2+",
                        "comment": "Bishop b4 -> d2: Exchange bishop for knight/bishop (depending on move order)",
                    },
                    {
                        "move": "Qxd2",
                        "san": "Qxd2",
                        "comment": "Queen d1 -> d2: Recapture, keeping a solid center",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: White plays Queen's Pawn",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black mirrors in the center",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and support d4",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop and fight for e4",
                    },
                    {
                        "move": "e3",
                        "san": "e3",
                        "comment": "Pawn e2 -> e3: Support d4 and open the diagonal for Bd3",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Prepare ...c5 or ...Bd6",
                    },
                    {
                        "move": "Bd3",
                        "san": "Bd3",
                        "comment": "Bishop f1 -> d3: Typical Colle bishop, eyeing h7",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Black strikes in the center",
                    },
                    {
                        "move": "c3",
                        "san": "c3",
                        "comment": "Pawn c2 -> c3: Support d4 and prepare Nbd2",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: More pressure on d4",
                    },
                    {
                        "move": "Nbd2",
                        "san": "Nbd2",
                        "comment": "Knight b1 -> d2: Complete the Colle setup and prepare e4",
                    },
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
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Queen's Pawn",
                    },
                    {
                        "move": "d5",
                        "san": "d5",
                        "comment": "Pawn d7 -> d5: Black mirrors in the center",
                    },
                    {
                        "move": "e3",
                        "san": "e3",
                        "comment": "Pawn e2 -> e3: Support d4 and open bishop",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Develop knight",
                    },
                    {
                        "move": "Bd3",
                        "san": "Bd3",
                        "comment": "Bishop f1 -> d3: Eye the h7 square",
                    },
                    {
                        "move": "e6",
                        "san": "e6",
                        "comment": "Pawn e7 -> e6: Black develops solidly",
                    },
                    {
                        "move": "f4",
                        "san": "f4",
                        "comment": "Pawn f2 -> f4: Stonewall pawn structure forms",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Black strikes at the center",
                    },
                    {
                        "move": "c3",
                        "san": "c3",
                        "comment": "Pawn c2 -> c3: Reinforce d4 and control b4",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Pressure on d4",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop knight, aiming for Ne5",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Sicilian Defense",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and hit d4/e5",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Support ...Nf6 and ...e5",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Open Sicilian",
                    },
                    {
                        "move": "cxd4",
                        "san": "cxd4",
                        "comment": "Pawn c5 -> d4: Exchange in the center",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: White recaptures with the knight",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4 and develop",
                    },
                    {
                        "move": "a6",
                        "san": "a6",
                        "comment": "Pawn a7 -> a6: Najdorf! Control b5 and keep options",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Sicilian Defense",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop and prepare d4",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Dragon setup",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Open Sicilian",
                    },
                    {
                        "move": "cxd4",
                        "san": "cxd4",
                        "comment": "Pawn c5 -> d4: Exchange in the center",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: White recaptures",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4 and develop",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4 and develop",
                    },
                    {
                        "move": "g6",
                        "san": "g6",
                        "comment": "Pawn g7 -> g6: Dragon - fianchetto the bishop",
                    },
                    {
                        "move": "Be3",
                        "san": "Be3",
                        "comment": "Bishop c1 -> e3: Yugoslav Attack setup",
                    },
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
                    {
                        "move": "e4",
                        "san": "e4",
                        "comment": "Pawn e2 -> e4: King's Pawn",
                    },
                    {
                        "move": "c5",
                        "san": "c5",
                        "comment": "Pawn c7 -> c5: Sicilian Defense",
                    },
                    {
                        "move": "Nf3",
                        "san": "Nf3",
                        "comment": "Knight g1 -> f3: Develop",
                    },
                    {
                        "move": "Nc6",
                        "san": "Nc6",
                        "comment": "Knight b8 -> c6: Sveshnikov move order",
                    },
                    {
                        "move": "d4",
                        "san": "d4",
                        "comment": "Pawn d2 -> d4: Open Sicilian",
                    },
                    {
                        "move": "cxd4",
                        "san": "cxd4",
                        "comment": "Pawn c5 -> d4: Exchange in the center",
                    },
                    {
                        "move": "Nxd4",
                        "san": "Nxd4",
                        "comment": "Knight f3 -> d4: White recaptures",
                    },
                    {
                        "move": "Nf6",
                        "san": "Nf6",
                        "comment": "Knight g8 -> f6: Attack e4",
                    },
                    {
                        "move": "Nc3",
                        "san": "Nc3",
                        "comment": "Knight b1 -> c3: Defend e4",
                    },
                    {
                        "move": "e5",
                        "san": "e5",
                        "comment": "Pawn e7 -> e5: Kick the d4 knight and seize space",
                    },
                    {
                        "move": "Ndb5",
                        "san": "Ndb5",
                        "comment": "Knight d4 -> b5: Knight heads for d6",
                    },
                    {
                        "move": "d6",
                        "san": "d6",
                        "comment": "Pawn d7 -> d6: Support the e5 pawn and open lines",
                    },
                ],
            }
        ],
    },
})
