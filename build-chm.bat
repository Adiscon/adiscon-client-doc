@echo off
REM Compile all CHM files from build/chm/*/*.hhp
REM Requires: HTML Help Workshop (hhc.exe). Run 'make all-htmlhelp' first.
REM Override: set HHC=C:\path\to\hhc.exe

REM Change to script directory (repo root) before enabling delayed expansion
cd /d "%~dp0"
setlocal EnableDelayedExpansion

REM HTML Help Compiler - try HHC env var, then common install paths
REM Use short path (PROGRA~2) to avoid (x86) parsing issues in batch
if defined HHC (
    set "HHC_PATH=!HHC!"
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

set "BUILDDIR=build\chm"
if not exist "%BUILDDIR%" (
    echo Error: Build directory not found: %BUILDDIR%
    echo Run 'make all-htmlhelp' first to generate HTMLHelp files.
    exit /b 1
)

echo Compiling CHM files...
echo.

set "COUNT=0"
for /d %%D in ("%BUILDDIR%\*") do (
    for %%F in ("%%~D\*.hhp") do (
        set /a COUNT+=1
        echo [%%~nxD] Compiling %%~nF.hhp...
        "!HHC_PATH!" "%%~F"
        if !errorlevel! equ 0 (
            echo   OK: CHM created
            copy /y "%%~dpnF.chm" "build\" >nul 2>&1
        ) else (
            echo   Warning: CHM compilation failed
        )
        echo.
    )
)

if !COUNT! equ 0 (
    echo No .hhp files found. Run 'make all-htmlhelp' first.
    exit /b 1
)

echo Done. Compiled !COUNT! CHM file(s).
exit /b 0
