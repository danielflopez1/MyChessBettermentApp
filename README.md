# Chess Betterment

A Flask-based chess application that lets you play against Stockfish engine with move analysis and PGN game review capabilities.

## Features

- 🎮 **Play vs Stockfish**: Interactive chessboard with drag-and-drop pieces
- 📊 **Move Analysis**: Get real-time feedback on your moves (Brilliant, Best, Good, Inaccuracy, Mistake, Blunder)
- 💡 **Hints**: Click the Help button to see the best move
- 📁 **PGN Analysis**: Upload and analyze complete chess games
- 📈 **Evaluation Graph**: Visualize game progress with interactive charts
- ⏮️ **Undo**: Take back moves and try different lines

## Requirements

- Python 3.8 or higher
- Stockfish chess engine
- Modern web browser (Chrome, Firefox, Edge, Safari)

## Quick Start (Automated)

### Option 1: Use Setup Script (Recommended)
```bash
# 1. Run the setup script
python setup.py
```

The script will:
- Check Python version
- Install required packages
- Verify project structure
- Check for Stockfish engine
- Offer to download missing static files

### Option 2: Manual Installation

See detailed instructions below.

---

## Manual Installation

### 1. Install Python Dependencies

#### Using pip:
```bash
pip install -r requirements.txt
```

#### Or install manually:
```bash
pip install Flask==3.1.2
pip install chess==1.11.2
```

#### Using Conda:
```bash
conda create -n chessbetterment python=3.10
conda activate chessbetterment
pip install -r requirements.txt
```

### 2. Download Stockfish Engine

#### Windows:
1. Go to https://stockfishchess.org/download/
2. Download "Stockfish for Windows" (e.g., `stockfish-windows-x86-64-avx2.zip`)
3. Extract to `Stock/` folder in the project directory
4. Update `app.py` line 20 with your Stockfish path:
```python
   STOCKFISH_PATH = r"Stock\stockfish-windows-x86-64-avx2.exe"
```

#### macOS:
```bash
brew install stockfish
```

#### Linux:
```bash
sudo apt-get install stockfish
```

### 3. Download Static Files (if missing)

If you don't have the static files, download them using PowerShell (Windows):
```powershell
# Create directories
mkdir static\css
mkdir static\js

# Download CSS files
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" -OutFile "static\css\bootstrap.min.css"
Invoke-WebRequest -Uri "https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css" -OutFile "static\css\chessboard-1.0.0.min.css"

# Download JS files
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" -OutFile "static\js\bootstrap.bundle.min.js"
Invoke-WebRequest -Uri "https://code.jquery.com/jquery-3.7.1.min.js" -OutFile "static\js\jquery-3.7.1.min.js"
Invoke-WebRequest -Uri "https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js" -OutFile "static\js\chessboard-1.0.0.min.js"
Invoke-WebRequest -Uri "https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js" -OutFile "static\js\chess.min.js"
Invoke-WebRequest -Uri "https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js" -OutFile "static\js\chart.min.js"
```

Or use curl (macOS/Linux):
```bash
# Create directories
mkdir -p static/css static/js

# Download files
curl -o static/css/bootstrap.min.css https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
curl -o static/css/chessboard-1.0.0.min.css https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css
curl -o static/js/bootstrap.bundle.min.js https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js
curl -o static/js/jquery-3.7.1.min.js https://code.jquery.com/jquery-3.7.1.min.js
curl -o static/js/chessboard-1.0.0.min.js https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js
curl -o static/js/chess.min.js https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js
curl -o static/js/chart.min.js https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js
```

---

## Running the Application

### Start the Flask Server
```bash
python app.py
```

You should see output like:
```
✓ Stockfish found at: Stock\stockfish-windows-x86-64-avx2.exe
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Open in Browser

Navigate to: **http://localhost:5000**

---

## Usage Guide

### Playing Against the Engine

1. Click **"Play vs AI"** on the home page
2. Choose your color with "New Game (White)" or "New Game (Black)"
3. Drag and drop pieces to make moves
4. Click **💡 Help** to see the best move highlighted
5. Use **Undo** to take back moves

### Move Grading

After each move, you'll receive feedback:
- **Brilliant** (< -50 cp): Better than the engine's choice!
- **Best** (≤ 20 cp): Perfect move
- **Excellent** (≤ 50 cp): Very strong move
- **Good** (≤ 100 cp): Solid move
- **Inaccuracy** (≤ 200 cp): Slight mistake
- **Mistake** (≤ 400 cp): Significant error
- **Blunder** (> 400 cp): Major mistake

### Analyzing PGN Games

1. Click **"Review sample game"** to see an example
2. Or paste/upload your own PGN in the text area
3. View move-by-move analysis with:
   - Interactive board
   - Evaluation graph
   - Best move suggestions
   - Move classifications

---

## Project Structure
```
chessbetterment/
├── app.py                      # Main Flask application
├── setup.py                    # Automated setup script
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── Stock/                      # Stockfish engine (you add this)
│   └── stockfish-windows-x86-64-avx2.exe
├── templates/                  # HTML templates
│   ├── base.html              # Base layout
│   ├── index.html             # Home page
│   ├── play.html              # Play interface
│   └── review.html            # Analysis page
└── static/                     # Static assets
    ├── css/
    │   ├── bootstrap.min.css
    │   └── chessboard-1.0.0.min.css
    └── js/
        ├── bootstrap.bundle.min.js
        ├── jquery-3.7.1.min.js
        ├── chessboard-1.0.0.min.js
        ├── chess.min.js
        └── chart.min.js
```

---

## Configuration

Edit `app.py` to customize:
```python
# Line 20: Stockfish path
STOCKFISH_PATH = r"Stock\stockfish-windows-x86-64-avx2.exe"

# Line 25: Engine thinking time for live play (seconds)
ENGINE_TIME_PER_MOVE = 0.1

# Line 27: Engine thinking time for analysis (seconds, higher = better)
ENGINE_TIME_PER_ANALYSIS = 0.5

# Line 30: Flask secret key (change for production)
SECRET_KEY = "your-secret-key-here"
```

---

## Troubleshooting

### "Stockfish not found" Error

**Problem**: Flask can't find the Stockfish engine

**Solution**:
1. Make sure Stockfish is downloaded and extracted
2. Update `STOCKFISH_PATH` in `app.py` with the correct path
3. Use raw string (prefix with `r`) for Windows paths: `r"C:\path\to\stockfish.exe"`

### Missing Static Files

**Problem**: Board doesn't display or buttons don't work

**Solution**:
1. Run `python setup.py` and choose to download files
2. Or manually download using PowerShell/curl commands above
3. Verify all files exist in `static/css/` and `static/js/`

### "Cannot show hint: chess is not defined"

**Problem**: Old version of play.html template

**Solution**: 
Make sure you're using the updated `play.html` with the `squareIndexToName()` function

### Port Already in Use

**Problem**: `Address already in use` error

**Solution**:
- Stop other Flask instances
- Or change port in `app.py`: `app.run(port=5001)`

---

## Development

### Running in Debug Mode

Debug mode is enabled by default in `app.py`:
```python
app.run(debug=True, threaded=True)
```

This provides:
- Auto-reload on code changes
- Detailed error pages
- Interactive debugger

### Disabling Debug Mode (Production)

For production, use a proper WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## Credits

- **Stockfish**: Open-source chess engine (https://stockfishchess.org)
- **python-chess**: Chess library by Niklas Fiekas
- **Chessboard.js**: Interactive chessboard by Chris Oakman
- **Bootstrap**: Frontend framework
- **Chart.js**: Charting library

---

## License

This project is for educational purposes. Stockfish is licensed under GPL v3.

---

## Support

If you encounter issues:
1. Run `python setup.py` to check your setup
2. Verify all files are present
3. Check that Stockfish path is correct in `app.py`
4. Make sure Python 3.8+ is installed

---

## Future Enhancements

- [ ] Promotion piece selection (currently auto-queens)
- [ ] Opening book database
- [ ] Save/load games
- [ ] Multiple engine difficulty levels
- [ ] Multiplayer mode
- [ ] Mobile app version

---

**Enjoy playing chess! ♟️**
