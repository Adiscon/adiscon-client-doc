#!/bin/bash
# Unix Shell Script to run Prompt Maker GUI
# This script will create a virtual environment if needed and run the application

set -e

echo "🚀 Starting Prompt Maker GUI..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or later"
    echo "On Ubuntu/Debian: sudo apt install python3 python3-venv python3-tk"
    echo "On CentOS/RHEL: sudo yum install python3 python3-tkinter"
    echo "On macOS: brew install python3-tk"
    exit 1
fi

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/venv"

# Check if we're already in a virtual environment
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "✅ Already running in virtual environment"
    python3 "$SCRIPT_DIR/prompt_maker.py"
    exit $?
fi

# Create virtual environment if it doesn't exist
if [[ ! -d "$VENV_DIR" ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"

    if [[ $? -ne 0 ]]; then
        echo "❌ Failed to create virtual environment"
        exit 1
    fi

    echo "✅ Virtual environment created successfully"

    # Upgrade pip in the virtual environment
    echo "🔧 Upgrading pip..."
    "$VENV_DIR/bin/pip" install --upgrade pip

    if [[ $? -ne 0 ]]; then
        echo "⚠️  Warning: Failed to upgrade pip, but continuing..."
    fi
fi

# Check if tkinter is available
echo "🔍 Checking for tkinter..."
python3 -c "import tkinter; print('✅ tkinter is available')" 2>/dev/null

if [[ $? -ne 0 ]]; then
    echo "❌ tkinter is not available"
    echo ""
    echo "Please install tkinter:"
    echo "Ubuntu/Debian: sudo apt install python3-tk"
    echo "CentOS/RHEL: sudo yum install tkinter"
    echo "macOS: brew install python3-tk"
    exit 1
fi

# Activate virtual environment and run the application
echo "🚀 Activating virtual environment and starting Prompt Maker..."
"$VENV_DIR/bin/python3" "$SCRIPT_DIR/prompt_maker.py"

RET_CODE=$?

if [[ $RET_CODE -eq 0 ]]; then
    echo ""
    echo "✅ Prompt Maker completed successfully"
else
    echo ""
    echo "❌ Prompt Maker exited with error code: $RET_CODE"
fi

exit $RET_CODE