@echo off
REM Windows Batch Script to run Prompt Maker CLI

setlocal
set "SCRIPT_DIR=%~dp0"
python "%SCRIPT_DIR%prompt_maker_cli.py" %*
exit /b %errorlevel%