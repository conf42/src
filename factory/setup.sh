#!/usr/bin/env bash
# Conf42 factory - one-time setup on a new macOS / Linux machine:  bash factory/setup.sh
# Installs what is missing (venv packages, ffmpeg, LibreOffice), asks for the Descript token once, puts a
# "Conf42 factory" launcher on the Desktop, checks the machine, then opens the dashboard.
# FACTORY_NO_LAUNCH=1 skips opening the dashboard at the end, FACTORY_SKIP_OPTIONAL=1 skips LibreOffice (smoke test).
set -e
cd "$(dirname "$0")/.."
export PYTHONUTF8=1
MAC=0; [ "$(uname)" = "Darwin" ] && MAC=1

install_pkg() {   # install_pkg <brew formula> <brew cask?> <apt package>
  if [ $MAC = 1 ]; then
    if ! command -v brew >/dev/null; then
      echo "Homebrew is needed to install $1. Install it from https://brew.sh (one command), then run setup.sh again."
      exit 1
    fi
    if [ "$2" = "cask" ]; then brew install --cask "$1"; else brew install "$1"; fi
  elif command -v apt-get >/dev/null; then sudo apt-get install -y "$3"
  elif command -v dnf >/dev/null; then sudo dnf install -y "$3"
  else echo "Please install $3 with your package manager, then run setup.sh again."; exit 1
  fi
}

PY="${FACTORY_PYTHON:-}"   # force a specific Python (the smoke test checks macOS's built-in 3.9 this way)
[ -n "$PY" ] || for c in python3.13 python3.12 python3.11 python3.10 python3 python; do
  if command -v $c >/dev/null && $c -c "import sys;sys.exit(0 if sys.version_info>=(3,9) else 1)" 2>/dev/null; then PY=$c; break; fi
done
if [ -z "$PY" ]; then
  if [ $MAC = 1 ]; then install_pkg python "" python3; PY=python3; else echo "Install Python 3.9+ first."; exit 1; fi
fi
[ -x env/bin/python ] || { echo "Creating the Python environment with $($PY --version) ..."; $PY -m venv env; }
echo "Installing Python packages ..."
env/bin/python -m pip install -q --upgrade pip
env/bin/python -m pip install -q -r factory/requirements.txt

have() { env/bin/python -c "import sys;sys.path.insert(0,'factory');from factory import machine;sys.exit(0 if machine.$1 else 1)"; }
if ! have "find_tool('ffmpeg')"; then echo "Installing ffmpeg ..."; install_pkg ffmpeg "" ffmpeg; fi
if [ -z "$FACTORY_SKIP_OPTIONAL" ] && ! have "soffice()"; then
  echo "Installing LibreOffice (converts PPTX decks to PDF) ..."
  install_pkg libreoffice cask libreoffice || echo "LibreOffice not installed - only PPTX decks need it."
fi

chmod +x factory/run.sh factory/setup.sh
cd factory
../env/bin/python -m factory setup || { echo; echo "Fix the items marked FIX above, then run setup.sh again."; exit 1; }
if [ -z "$FACTORY_NO_LAUNCH" ]; then echo; echo "All set. Opening the dashboard ..."; exec ./run.sh; fi
