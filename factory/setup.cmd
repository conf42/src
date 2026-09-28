@echo off
rem Conf42 factory - one-time setup on a new Windows machine (double-click, or run from a terminal).
rem Installs what is missing (Python venv packages, ffmpeg, LibreOffice), asks for the Descript token once,
rem puts a "Conf42 factory" launcher on the Desktop, checks the machine, then opens the dashboard.
setlocal
cd /d "%~dp0.."
set PYTHONUTF8=1

where py >nul 2>nul || where python >nul 2>nul || (
  echo Installing Python 3.12 ...
  winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
  echo.
  echo Python was installed. Close this window and run setup.cmd again.
  pause
  exit /b 1
)
if not exist env\Scripts\python.exe (
  echo Creating the Python environment ...
  where py >nul 2>nul && (py -3 -m venv env) || (python -m venv env)
)
echo Installing Python packages ...
env\Scripts\python.exe -m pip install -q --upgrade pip
env\Scripts\python.exe -m pip install -q -r factory\requirements.txt || goto :fail

env\Scripts\python.exe -c "import sys;sys.path.insert(0,'factory');from factory import machine;sys.exit(0 if machine.find_tool('ffmpeg') else 1)" || (
  echo Installing ffmpeg ...
  winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
)
env\Scripts\python.exe -c "import sys;sys.path.insert(0,'factory');from factory import machine;sys.exit(0 if machine.soffice() else 1)" || (
  echo Installing LibreOffice - converts PPTX decks to PDF ...
  winget install -e --id TheDocumentFoundation.LibreOffice --accept-source-agreements --accept-package-agreements
)

cd factory
..\env\Scripts\python.exe -m factory setup
if errorlevel 1 (
  echo.
  echo Fix the items marked FIX above, then run setup.cmd again.
  pause
  exit /b 1
)
echo.
echo All set. Opening the dashboard ...
start "" "%~dp0run.cmd"
exit /b 0

:fail
echo Setup failed - see the messages above.
pause
exit /b 1
