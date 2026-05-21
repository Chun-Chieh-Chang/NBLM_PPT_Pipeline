@echo off
:: Force native CMD title
title NBLM PPT Pipeline Launcher

echo ======================================================================
echo        NBLM PPT PIPELINE - PowerPoint Generator Workbench
echo ======================================================================
echo [1/3] Detecting Python installation in system...

:: Check python installation
where python >nul 2>nul
if %errorlevel% neq 0 goto :NO_PYTHON

echo [2/3] Found Python environment:
python --version
echo.
echo [3/3] Calling Python dependency auto-installer and server launcher...
echo Please wait while we verify requirements.txt...
echo ----------------------------------------------------------------------

:: Run python GUI starter
python pptmaster_gui.py
if %errorlevel% neq 0 goto :RUN_ERROR

echo.
echo ======================================================================
echo Server shut down cleanly. Thank you for using NBLM PPT Pipeline!
echo ======================================================================
echo.
pause
goto :EOF

:NO_PYTHON
echo.
echo ======================================================================
echo ERROR: Python executable environment was not found on your system!
echo ======================================================================
echo Guideline:
echo   1. Please download and install Python (3.10 or higher recommended)
echo      from the official website: https://www.python.org/
echo   2. CRITICAL: Make sure to check "Add Python to PATH" during installation.
echo   3. After installation, please double-click start.bat again.
echo ======================================================================
echo.
pause
exit /b 1

:RUN_ERROR
echo.
echo ======================================================================
echo ERROR: Flask backend server exited unexpectedly with error code %errorlevel%.
echo ======================================================================
echo Guideline:
echo   Please review the error logs printed in the console above to troubleshoot.
echo ======================================================================
echo.
pause
exit /b %errorlevel%
