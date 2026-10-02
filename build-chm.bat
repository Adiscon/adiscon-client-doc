@echo off
REM Build HTMLHelp sources and compile all CHM files under build\chm\*\*.hhp
REM Requires: Windows venv (setup_venv.bat), hhc.exe
REM Optional: sibling ..\adiscon-client checkout for five client output copies
REM Override: set HHC=C:\path\to\hhc.exe
REM After a WSL source build, run: build-chm.bat --compile-only

cd /d "%~dp0"

REM Paths under D:\!cvsroot\... break when delayed expansion is enabled ("!c" -> "").
REM Never enable delayed expansion in this script; disable it even if a parent enabled it.
setlocal DisableDelayedExpansion

set "VENV_PY=%~dp0venv\Scripts\python.exe"
set "CHM_ROOT=%~dp0build\chm"
for %%I in ("%~dp0..\adiscon-client") do set "CLIENT_ROOT=%%~fI"
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

set "CLIENT_AVAILABLE=0"
if exist "%CLIENT_ROOT%\AdisconClient.sln" set "CLIENT_AVAILABLE=1"
if "%CLIENT_AVAILABLE%"=="0" (
    echo Warning: sibling adiscon-client repository not found: %CLIENT_ROOT%
    echo Client manual copies will be skipped; CHM files will still be built here.
)

if /i "%~1"=="--compile-only" goto :compile_chm_files

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

:compile_chm_files
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
if exist "%~dpn1.chm" (
    echo   Error: Could not remove previous CHM: %~dpn1.chm
    exit /b 1
)
echo [%~2] Compiling %~n1.hhp...
"%HHC_PATH%" "%~1"
if exist "%~dpn1.chm" (
    echo   OK: CHM created
    if /i "%~2"=="winsyslog-j" (
        copy /y "%~dpn1.chm" "%~dp0build\WinSyslog-J.chm" >nul
    ) else (
        copy /y "%~dpn1.chm" "%~dp0build\%~n1.chm" >nul
    )
    if errorlevel 1 (
        echo   Error: Could not copy CHM to build output.
        exit /b 1
    )
    call :copy_to_client "%~dpn1.chm" "%~2"
    if errorlevel 1 exit /b 1
    echo.
    exit /b 0
)
echo   Error: CHM compilation failed
echo.
exit /b 1

:copy_to_client
call :set_client_destination "%~2"
if not defined CLIENT_CHM (
    if "%CLIENT_AVAILABLE%"=="1" (
        echo   No client destination configured for %~2; copy skipped.
    ) else (
        echo   Client checkout unavailable; copy skipped for %~2.
    )
    exit /b 0
)

for %%I in ("%CLIENT_CHM%") do if not exist "%%~dpI" mkdir "%%~dpI"
for %%I in ("%CLIENT_CHM%") do if not exist "%%~dpI" (
    echo   Error: Could not create destination folder for %CLIENT_CHM%.
    exit /b 1
)

copy /y "%~1" "%CLIENT_CHM%" >nul
if errorlevel 1 (
    echo   Error: Could not copy CHM to %CLIENT_CHM%.
    exit /b 1
)
if not exist "%CLIENT_CHM%" (
    echo   Error: Client CHM is missing after copy: %CLIENT_CHM%.
    exit /b 1
)
echo   Copied to %CLIENT_CHM%
exit /b 0

:set_client_destination
set "CLIENT_CHM="
if not "%CLIENT_AVAILABLE%"=="1" exit /b 0
if /i "%~1"=="eventreporter" set "CLIENT_CHM=%CLIENT_ROOT%\CFGEvntSLog\bin\Release\manual\EventReporter.chm"
if /i "%~1"=="mwagent" set "CLIENT_CHM=%CLIENT_ROOT%\MWAgent\bin\Release\manual\MonitorWareAgent.chm"
if /i "%~1"=="rsyslog" set "CLIENT_CHM=%CLIENT_ROOT%\RSyslogConfigClient\bin\Release\manual\RSyslogWindowsAgent.chm"
if /i "%~1"=="winsyslog" set "CLIENT_CHM=%CLIENT_ROOT%\WINSyslogClient\bin\Release\manual\WinSyslog.chm"
if /i "%~1"=="winsyslog-j" set "CLIENT_CHM=%CLIENT_ROOT%\WINSyslogClient\bin\Release.JP\manual\WinSyslog.chm"
exit /b 0
