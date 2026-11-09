#!/bin/sh
# Slow, Google-safe rollout of the queued blog posts (Status=queued in _db/blog.csv).
# Releases a small slice every few hours instead of one big drop; each slice is a commit + push, the deploy
# puts it live, sitemap/feed grow gradually. Newest posts first. Safe to stop (Ctrl-C) and re-run: it only
# ever releases what is still queued.
#
#   caffeinate -i blog/rollout.sh            default: 72 posts every 4 h (~1,300 posts in ~3 days)
#   caffeinate -i blog/rollout.sh 50 3       50 posts every 3 h
set -e
cd "$(dirname "$0")/.."
N="${1:-72}"
HOURS="${2:-4}"
while :; do
    git pull --rebase --autostash -q
    LEFT=$(env/bin/python -m build.blog_plan release "$N" | tail -1)
    if git diff --quiet _db/blog.csv; then
        echo "$(date '+%F %T') nothing left to release"; break
    fi
    git add _db/blog.csv
    git commit -qm "Blog: release $N queued posts ($LEFT)"
    git push -q
    echo "$(date '+%F %T') released $N, $LEFT"
    case "$LEFT" in *"queued left: 0") break;; esac
    sleep $((HOURS * 3600))
done
