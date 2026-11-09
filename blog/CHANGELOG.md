# Living blog: run log

Newest first. One entry per maintenance run (skill conf42-blog): published / scheduled / orphaned / enriched, and
what's next.

## 2026-11-09 - first maintenance run
- Published/scheduled 137 posts: 78 talk (53 MLOps 2026 previews Nov 9-18 from abstracts; 25 Platform Engineering
  2026 from transcripts), 18 sponsored, 34 roundups (every finished 2025+ event + Platform 2026), 7 plugs.
- Six hand-written Harness recaps (2025-12 .. 2026-06) got Type/Ref instead of a duplicate post; text untouched.
- Held (Status hidden): LLMday Hamburg, SREday Campinas, LLMday Montevideo plugs - CONF42 coupon not created on
  those Luma events yet (London LLMday/PEC has it). Flip Status to empty once the coupon exists.
- Skipped: Reliaburger Oct 28 webinar (no Snoop doc - Snoop started Nov 6); MLOps 2026 roundup (Nov 20, after the
  event); 2027 plugs (lineups not final).
- Fixes: headshot og:image was double-prefixed; sponsor splash only from the post's own event; lint rejects links to
  removed talks; new `check` command; planner lists items for the next backfill event.
- Next: MLOps roundup Nov 20; enrich MLOps posts when videos land; backfill talk posts for prompt2026 (17).

## 2026-11-08 - system set up
- build/blog.py: visibility = Status ok + Date <= today (UTC) + Ref resolves; Atom feed /blog.xml, robots.txt,
  llms.txt, IndexNow key + morning ping; per-post title/description/canonical/og/twitter + BlogPosting, BreadcrumbList,
  VideoObject JSON-LD; VideoObject on every released talk page; Event JSON-LD made valid; canonical host = www.
- build/blog_plan.py: plan / lint / add / orphan / export.
- _db/blog.csv: 8 new columns (Type, Event, Ref, Sponsor, Author, Updated, Status, Tags); the 112 legacy rows untouched.
- Next: first run - MLOps 2026 (Nov 19) talk posts, Platform 2026 sponsored + roundup, sister plugs from Nov 8.

## 2026-11-09 (second pass)
- Backfill: 17 talk posts for Conf42 Prompt Engineering 2026 (dated 2026-09-29 to 2026-10-27, written timelessly from the srt transcripts). Lint 0.
- Still held: Hamburg Q4, Campinas Q4, Montevideo Q4 plugs (Status hidden) - no CONF42 coupon on their Luma events yet.
- Still skipped: Reliaburger 0.2.0 webinar (no Snoop doc for 2026-10-28).
- Data notes: Ravi Ray's Company1 in PROMPT_2026.csv is his job title; Sachin Gupta's YouTube link carries ?si=; Kevin Brown's talk is a short founder product demo (post says so).
- Next: MLOps 2026 roundup (Nov 20); next backfill event from backfill_talk_events.

## 2026-11-09 (full backfill, Marek: "ship everything now")
- Talk-post backfill for every finished 2025+ event done in one go: ~1,290 talk posts across 32 events (108 writer batches, `plan --all`), all from the talk transcripts, written timelessly, historical dates. Lint 0.
- Every talk/sponsored post with a video now ends with a "Watch the talk on YouTube" link (enrich queue 1,218 -> 6; the 6 are the hand-written Harness recaps, text untouched).
- Skipped on purpose (transcript is a different talk than the CSV row): obs2026 Ravi Chandra; cloud2026 Elizabeth Fuentes Leone; sre2025 Sidhartha Velishala, Krishna Rao Vemula; golang2025 Krishna Rao Vemula; cloud2025 Sai Prakash Narasingu, Karthik Akinapelli; ce2025 Jaspreet Kumar; python2025 Sushil Prabhu Prabhakaran.
- blog_plan: `plan --all` (items for every backfill event); the pre-2025 freeze now covers legacy rows only (no Ref) - DevOps 2025 talk posts dated Dec 2024 are typed rows and editable.
- Data issues for Marek: scratchpad oddities list (wrong transcripts, copied abstracts, shifted ML 2026 keywords, shared YouTube ids, Company1 holding job titles/universities).
- Next: MLOps 2026 roundup (Nov 20); 2027 plugs; Reliaburger webinar once a Snoop doc exists; 3 held plugs need CONF42 coupons.
