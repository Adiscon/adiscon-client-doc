@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Adiscon Documentation Build Environment
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.x from https://python.org
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

:: Check if virtual environment already exists
if exist "venv\Scripts\activate.bat" (
    echo Virtual environment already exists.
    echo.
    echo To activate it, run:
    echo   venv\Scripts\activate.bat
    echo.
    echo To deactivate it, run:
    echo   deactivate
    echo.
    pause
    exit /b 0
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo WARNING: Failed to upgrade pip, continuing anyway...
)

:: Install pinned documentation toolchain
if exist "requirements.txt" (
    echo Installing documentation requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements from requirements.txt
        pause
        exit /b 1
    )
) else (
    echo WARNING: requirements.txt not found. Skipping dependency installation.
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To build documentation, run:
echo   make html-winsyslog
echo   make html-rsyslog
echo   make html-mwagent
echo   make html-eventreporter
echo   make html-syslogviewer
echo.
echo To deactivate the virtual environment, run:
echo   deactivate
echo.
pause 