@echo off
REM Windows Batch Script to run Prompt Maker GUI
REM This script will create a virtual environment if needed and run the application

setlocal enabledelayedexpansion

echo 🚀 Starting Prompt Maker GUI...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or later from https://python.org
    pause
    exit /b 1
)

REM Get the directory of this script
set "SCRIPT_DIR=%~dp0"
set "VENV_DIR=%SCRIPT_DIR%venv"

REM Check if we're already in a virtual environment
if defined VIRTUAL_ENV (
    echo ✅ Already running in virtual environment
    goto :run_app
)

REM Create virtual environment if it doesn't exist
if not exist "%VENV_DIR%" (
    echo 📦 Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )

    echo ✅ Virtual environment created successfully

    REM Upgrade pip in the virtual environment
    echo 🔧 Upgrading pip...
    "%VENV_DIR%\Scripts\pip.exe" install --upgrade pip
    if errorlevel 1 (
        echo ⚠️  Warning: Failed to upgrade pip, but continuing...
    )
)

REM Activate virtual environment and run the application
echo 🚀 Activating virtual environment and starting Prompt Maker...
"%VENV_DIR%\Scripts\python.exe" "%SCRIPT_DIR%prompt_maker.py"

if errorlevel 1 (
    echo ❌ Failed to start Prompt Maker
    pause
    exit /b 1
)

echo.
echo ✅ Prompt Maker completed successfully
pause