#!/bin/bash
# Factory fast track (Marek 2026-11-19; manual only - when Marek says "fast track"): talk files from this Mac straight
# into the cloud factory, no Drive upload by hand.
#   factory/fasttrack.sh <short_url> <file> [<file>...]
# The files go to a draft release of conf42/src (a draft and its files are seen only by people with write access),
# as f00.mp4, f01.pdf ... + names.json with their real names (GitHub would mangle spaces and accents). The workflow
# "factory cloud" puts every fasttrack-* draft in the Manual upload folder under the real names, deletes it, and runs
# the event. File names must carry the speaker's name, like the Manual upload folder wants. GitHub: 2 GiB a file.
set -euo pipefail
[ $# -ge 2 ] || { echo "usage: fasttrack.sh <short_url> <file>..."; exit 1; }
ev="$1"; shift
for f in "$@"; do
  [ -f "$f" ] || { echo "no file: $f"; exit 1; }
  [ "$(stat -f %z "$f")" -lt 2147483648 ] || { echo "over GitHub's 2 GiB: $f - use the Drive upload"; exit 1; }
done
tag="fasttrack-$ev-$(date -u +%Y%m%d%H%M%S)"
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
python3 - "$tmp" "$@" <<'PY'
import json, os, sys
tmp, names = sys.argv[1], {}
for i, f in enumerate(sys.argv[2:]):
    neutral = "f%02d%s" % (i, os.path.splitext(f)[1].lower())
    os.symlink(os.path.abspath(f), os.path.join(tmp, neutral))      # no copy of a 1 GB video
    names[neutral] = os.path.basename(f)
json.dump(names, open(os.path.join(tmp, "names.json"), "w"), ensure_ascii=False)
PY
gh release create "$tag" --repo conf42/src --draft --title "$tag" --notes "factory fast track for $ev (deleted by the pass)" "$tmp"/*
if ! gh workflow run factory-cloud.yml --repo conf42/src -f event="$ev" -f fasttrack="$tag"; then
  echo "could not start the workflow - the draft $tag stays; the next factory pass picks it up anyway"
  exit 1
fi
echo "fast track $tag started: https://github.com/conf42/src/actions/workflows/factory-cloud.yml"
