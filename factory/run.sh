#!/usr/bin/env bash
# Conf42 factory dashboard on http://localhost:8042 (macOS / Linux; Windows uses run.cmd)
cd "$(dirname "$0")"
export PYTHONUTF8=1
exec ../env/bin/python -m factory serve
