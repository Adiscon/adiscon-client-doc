@echo off
REM Build HTMLHelp sources and compile all CHM files under build\chm\*\*.hhp
REM Requires: Windows venv (setup_venv.bat), hhc.exe
REM Override: set HHC=C:\path\to\hhc.exe

cd /d "%~dp0"

REM Paths under D:\!cvsroot\... break when delayed expansion is enabled ("!c" -> "").
REM Never enable delayed expansion in this script; disable it even if a parent enabled it.
setlocal DisableDelayedExpansion

set "VENV_PY=%~dp0venv\Scripts\python.exe"
set "CHM_ROOT=%~dp0build\chm"
if defined HHC (
    set "HHC_PATH=%HHC%"
) else (
    set "HHC_PATH="
    if exist "C:\PROGRA~2\HTMLHE~1\hhc.exe" set "HHC_PATH=C:\PROGRA~2\HTMLHE~1\hhc.exe"
    if not defined HHC_PATH if exist "C:\Program Files\HTML Help Workshop\hhc.exe" set "HHC_PATH=C:\Program Files\HTML Help Workshop\hhc.exe"
    if not defined HHC_PATH where hhc.exe >nul 2>&1 && set "HHC_PATH=hhc.exe"
)

if not defined HHC_PATH (
    echo Error: HTML Help Compiler not found.
    echo Install to: C:\Program Files ^(x86^)\HTML Help Workshop\  or set HHC env var
    exit /b 1
)

if not exist "%VENV_PY%" (
    echo Error: Windows virtual environment not found: venv\Scripts\python.exe
    echo Run setup_venv.bat to create a Windows venv.
    echo A WSL/Linux venv ^(venv\bin only^) cannot be used from this .bat script.
    exit /b 1
)

set "PATH=%~dp0venv\Scripts;%PATH%"

echo [DEBUG] Using venv Python: %VENV_PY%

echo [DEBUG] Ensuring pip is available
"%VENV_PY%" -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [DEBUG] pip missing; bootstrapping with ensurepip
    "%VENV_PY%" -m ensurepip --upgrade
    if errorlevel 1 (
        echo Error: pip is not installed and ensurepip failed.
        echo Recreate the venv: delete venv\ and run setup_venv.bat
        exit /b 1
    )
)

echo [DEBUG] Upgrading pip
"%VENV_PY%" -m pip install --upgrade pip
if errorlevel 1 (
    echo Error: pip upgrade failed.
    exit /b 1
)

echo [DEBUG] Installing requirements
"%VENV_PY%" -m pip install -r requirements.txt
if errorlevel 1 (
    echo Error: pip install failed.
    exit /b 1
)

set "SPHINX_BUILD=%~dp0venv\Scripts\sphinx-build.exe"
if not exist "%SPHINX_BUILD%" (
    echo Error: sphinx-build not found in venv\Scripts\
    echo Run setup_venv.bat and pip install -r requirements.txt
    exit /b 1
)

echo [DEBUG] Building HTMLHelp sources for all products
set "SPHINX_BUILDER=htmlhelp"
for %%P in (eventreporter mwagent rsyslog syslogviewer winsyslog winsyslog-j) do (
    echo.
    echo === htmlhelp %%P ===
    if not exist "%CHM_ROOT%\%%P" mkdir "%CHM_ROOT%\%%P"
    "%SPHINX_BUILD%" -b htmlhelp -c %%P -W --keep-going source "%CHM_ROOT%\%%P"
    if errorlevel 1 goto :htmlhelp_failed
)
goto :htmlhelp_done

:htmlhelp_failed
echo Error: htmlhelp build failed. Fix Sphinx errors before compiling CHM files.
exit /b 1

:htmlhelp_done

if not exist "%CHM_ROOT%" (
    echo Error: Build directory not found: %CHM_ROOT%
    exit /b 1
)

echo Compiling CHM files...
echo.

set "COUNT=0"
set "CHM_FAILED=0"
for /d %%D in ("%CHM_ROOT%\*") do (
    for %%F in ("%%~D\*.hhp") do (
        call :compile_chm "%%~F" "%%~nxD"
        if errorlevel 1 set "CHM_FAILED=1"
    )
)

if %CHM_FAILED% neq 0 (
    echo Error: One or more CHM compilations failed.
    exit /b 1
)

if %COUNT% equ 0 (
    echo No .hhp files found under %CHM_ROOT%.
    exit /b 1
)

echo Done. Compiled %COUNT% CHM file(s).
exit /b 0

:compile_chm
set /a COUNT+=1
if exist "%~dpn1.chm" del /f /q "%~dpn1.chm"
if exist "%~dp0build\%~n1.chm" del /f /q "%~dp0build\%~n1.chm"
echo [%2] Compiling %~n1.hhp...
"%HHC_PATH%" "%~1"
if exist "%~dpn1.chm" (
    echo   OK: CHM created
    copy /y "%~dpn1.chm" "%~dp0build\" >nul 2>&1
    echo.
    exit /b 0
)
echo   Error: CHM compilation failed
echo.
exit /b 1
