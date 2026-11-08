# Living blog: run log

Newest first. One entry per maintenance run (skill conf42-blog): published / scheduled / orphaned / enriched, and
what's next.

## 2026-11-08 - system set up
- build/blog.py: visibility = Status ok + Date <= today (UTC) + Ref resolves; Atom feed /blog.xml, robots.txt,
  llms.txt, IndexNow key + morning ping; per-post title/description/canonical/og/twitter + BlogPosting, BreadcrumbList,
  VideoObject JSON-LD; VideoObject on every released talk page; Event JSON-LD made valid; canonical host = www.
- build/blog_plan.py: plan / lint / add / orphan / export.
- _db/blog.csv: 8 new columns (Type, Event, Ref, Sponsor, Author, Updated, Status, Tags); the 112 legacy rows untouched.
- Next: first run - MLOps 2026 (Nov 19) talk posts, Platform 2026 sponsored + roundup, sister plugs from Nov 8.
