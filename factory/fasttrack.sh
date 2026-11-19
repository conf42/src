#!/bin/bash
# Factory fast track (Marek 2026-11-19): talk files from this Mac straight into the cloud factory, no Drive upload.
#   factory/fasttrack.sh <short_url> <file> [<file>...]
# The files go to a draft release of conf42/src (only people with write access can see a draft); the workflow
# "factory cloud" (input fasttrack) puts them in the Manual upload folder under their real names, runs the event
# and deletes the draft. File names must carry the speaker's name, like the Manual upload folder wants.
set -euo pipefail
ev="$1"; shift
[ $# -gt 0 ] || { echo "usage: fasttrack.sh <short_url> <file>..."; exit 1; }
tag="fasttrack-$ev-$(date -u +%Y%m%d%H%M%S)"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
python3 - "$tmp/names.json" "$@" <<'PY'
import json, os, re, sys
# GitHub's asset name: anything outside [A-Za-z0-9._-] becomes ".", runs of dots collapse
names = {re.sub(r"\.+", ".", re.sub(r"[^A-Za-z0-9._-]", ".", os.path.basename(f))): os.path.basename(f) for f in sys.argv[2:]}
json.dump(names, open(sys.argv[1], "w"), ensure_ascii=False)
PY
gh release create "$tag" --repo conf42/src --draft --title "$tag" --notes "factory fast track for $ev (deleted by the pass)" "$@" "$tmp/names.json"
gh workflow run factory-cloud.yml --repo conf42/src -f event="$ev" -f fasttrack="$tag"
echo "fast track $tag started: https://github.com/conf42/src/actions/workflows/factory-cloud.yml"
