#!/bin/sh
# Publish the next N queued blog posts (newest Date first) and push; the deploy puts them live.
# Big backfills go out over 2-3 days instead of all at once (Marek 2026-11-09).
#   blog/release.sh 450        (~1,300 queued -> three runs, e.g. one a day)
set -e
cd "$(dirname "$0")/.."
N="${1:-450}"
git pull --rebase --autostash -q
env/bin/python -m build.blog_plan release "$N" | tail -1
git add _db/blog.csv
git commit -qm "Blog: release $N queued posts" && git push -q
