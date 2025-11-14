"""
Chess Betterment - Setup Script
This script will help you set up the Chess application.
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"→ {description}...")
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"✓ {description} - Done!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} - Failed!")
        print(f"  Error: {e}\n")
        return False


def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("✗ Python 3.8 or higher is required!")
        return False

    print("✓ Python version is compatible!\n")
    return True


def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Python Dependencies")

    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("✗ requirements.txt not found!")
        return False

    # Install packages
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Flask and chess libraries"
    )


def check_stockfish():
    """Check if Stockfish is available"""
    print_header("Checking Stockfish Engine")

    # Try to find stockfish in PATH
    stockfish_path = shutil.which("stockfish")

    if stockfish_path:
        print(f"✓ Stockfish found in PATH: {stockfish_path}\n")
        return True

    # Check common locations
    common_paths = [
        "Stock/stockfish-windows-x86-64-avx2.exe",  # Project directory
        "C:/stockfish/stockfish.exe",
        "C:/stockfish/stockfish-windows-x86-64-avx2.exe",
        "/usr/local/bin/stockfish",  # Mac/Linux
        "/usr/bin/stockfish",  # Linux
    ]

    for path in common_paths:
        if os.path.exists(path):
            print(f"✓ Stockfish found at: {path}\n")
            return True

    print("✗ Stockfish NOT found!")
    print("\nPlease download Stockfish:")
    print("1. Visit: https://stockfishchess.org/download/")
    print("2. Download the version for your operating system")
    if platform.system() == "Windows":
        print("3. Extract to: Stock/ folder in project directory")
        print("   OR to: C:/stockfish/")
    else:
        print("3. Install using your package manager:")
        print("   - macOS: brew install stockfish")
        print("   - Linux: sudo apt-get install stockfish")

    return False


def verify_structure():
    """Verify project structure"""
    print_header("Verifying Project Structure")

    required_dirs = ['templates', 'static/css', 'static/js']
    required_files = [
        'app.py',
        'templates/base.html',
        'templates/index.html',
        'templates/play.html',
        'templates/review.html',
        'static/css/bootstrap.min.css',
        'static/css/chessboard-1.0.0.min.css',
        'static/js/bootstrap.bundle.min.js',
        'static/js/jquery-3.7.1.min.js',
        'static/js/chessboard-1.0.0.min.js',
        'static/js/chess.min.js',
        'static/js/chart.min.js',
    ]

    all_good = True

    # Check directories
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✓ {directory}/")
        else:
            print(f"✗ {directory}/ - MISSING")
            all_good = False

    # Check files
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} - MISSING")
            all_good = False

    print()
    return all_good


def download_static_files():
    """Offer to download missing static files"""
    print_header("Downloading Static Files")

    response = input("Would you like to download missing static files? (y/n): ").lower()
    if response != 'y':
        print("Skipping static file download.\n")
        return False

    # Create directories
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)

    files_to_download = {
        'static/css/bootstrap.min.css': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
        'static/css/chessboard-1.0.0.min.css': 'https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css',
        'static/js/bootstrap.bundle.min.js': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
        'static/js/jquery-3.7.1.min.js': 'https://code.jquery.com/jquery-3.7.1.min.js',
        'static/js/chessboard-1.0.0.min.js': 'https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js',
        'static/js/chess.min.js': 'https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js',
        'static/js/chart.min.js': 'https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js',
    }

    try:
        import urllib.request

        for filepath, url in files_to_download.items():
            if not os.path.exists(filepath):
                print(f"→ Downloading {filepath}...")
                urllib.request.urlretrieve(url, filepath)
                print(f"✓ Downloaded {filepath}")

        print("\n✓ All static files downloaded!\n")
        return True

    except Exception as e:
        print(f"\n✗ Error downloading files: {e}")
        print("Please download them manually using the PowerShell commands in README.md\n")
        return False


def main():
    """Main setup function"""
    print("\n" + "=" * 60)
    print("  CHESS BETTERMENT - Setup")
    print("=" * 60)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        print("\n⚠️  Warning: Failed to install some dependencies")
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            sys.exit(1)

    # Verify project structure
    structure_ok = verify_structure()

    if not structure_ok:
        # Offer to download static files
        download_static_files()

    # Check Stockfish
    stockfish_ok = check_stockfish()

    # Final summary
    print_header("Setup Summary")

    if structure_ok and stockfish_ok:
        print("✓ Everything is ready!")
        print("\nTo start the application, run:")
        print("  python app.py")
        print("\nThen open your browser to: http://localhost:5000")
    else:
        print("⚠️  Setup completed with warnings:")
        if not structure_ok:
            print("  - Some files are missing")
        if not stockfish_ok:
            print("  - Stockfish engine not found")
        print("\nPlease review the messages above and fix any issues.")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()