@echo off
rem Conf42 factory local app: http://localhost:8042 (double-click this file)
cd /d "%~dp0"
set PYTHONUTF8=1
"%~dp0..\env\Scripts\python.exe" -m factory serve
