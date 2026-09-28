#!/usr/bin/env bash
# Conf42 factory - one-time setup on a new macOS / Linux machine:  bash factory/setup.sh
# Installs what is missing (venv packages, ffmpeg, LibreOffice), asks for the Descript token once, puts a
# "Conf42 factory" launcher on the Desktop, checks the machine, then opens the dashboard.
set -e
cd "$(dirname "$0")/.."
export PYTHONUTF8=1

command -v python3 >/dev/null || { echo "Install Python 3 first (macOS: brew install python)"; exit 1; }
[ -x env/bin/python ] || { echo "Creating the Python environment ..."; python3 -m venv env; }
echo "Installing Python packages ..."
env/bin/python -m pip install -q --upgrade pip
env/bin/python -m pip install -q -r factory/requirements.txt

have() { env/bin/python -c "import sys;sys.path.insert(0,'factory');from factory import machine;sys.exit(0 if machine.$1 else 1)"; }
if ! have "find_tool('ffmpeg')"; then
  echo "Installing ffmpeg ..."
  if command -v brew >/dev/null; then brew install ffmpeg; else sudo apt-get install -y ffmpeg; fi
fi
if ! have "soffice()"; then
  echo "Installing LibreOffice (converts PPTX decks to PDF) ..."
  if command -v brew >/dev/null; then brew install --cask libreoffice; else sudo apt-get install -y libreoffice; fi
fi

chmod +x factory/run.sh
cd factory
../env/bin/python -m factory setup || { echo; echo "Fix the items marked FIX above, then run setup.sh again."; exit 1; }
echo; echo "All set. Opening the dashboard ..."
./run.sh
