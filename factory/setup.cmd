@echo off
rem Conf42 factory - one-time setup on a new Windows machine (double-click, or run from a terminal).
rem Installs what is missing (Python venv packages, ffmpeg, LibreOffice), asks for the Descript token once,
rem puts a "Conf42 factory" launcher on the Desktop, checks the machine, then opens the dashboard.
setlocal
cd /d "%~dp0.."
set PYTHONUTF8=1

if exist env\Scripts\python.exe goto :haveenv
call :findpy
if not defined PY (
  echo Installing Python 3.12 ...
  winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
  call :findpy
)
if not defined PY (
  echo.
  echo Python could not be found. Install Python 3.12 from python.org, then run setup.cmd again.
  pause
  exit /b 1
)
echo Creating the Python environment with %PY% ...
"%PY%" -m venv env || goto :fail
:haveenv
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

:findpy
rem A real Python 3.9+ - "python" can be the Microsoft Store stub, so every candidate is actually run.
set "PY="
for /f "delims=" %%p in ('py -3 -c "import sys;print(sys.executable)" 2^>nul') do set "PY=%%p"
if defined PY exit /b 0
for /f "delims=" %%p in ('python -c "import sys;assert sys.version_info>=(3,9);print(sys.executable)" 2^>nul') do set "PY=%%p"
if defined PY exit /b 0
for /d %%d in ("%LOCALAPPDATA%\Programs\Python\Python3*" "%ProgramFiles%\Python3*") do (
  if exist "%%~d\python.exe" set "PY=%%~d\python.exe"
)
exit /b 0
