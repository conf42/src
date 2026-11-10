# Living blog: run log

Newest first. One entry per maintenance run (skill conf42-blog): published / scheduled / orphaned / enriched, and
what's next.

## 2026-11-10 - Post page redesign ("Post A")
- Post pages are the talk page's twin: hero in the event colour (navy without one) with Blog / event / read-time chips,
  speaker card and byline; the art in a glass frame over the curve linking the talk; narrow reading column opened by
  "In short"; sticky rail with contents (from the h2s), topic hubs and the talk; "More from <event>" frost cards.
- The /blog index redesign is undecided (mockups Blog A-C on Marek's Desktop).

## 2026-11-10 - AI discoverability (GEO)
- robots.txt allows every AI crawler incl. training bots; Cloudflare managed robots.txt / Block AI bots to be turned
  off by Marek in the dashboard.
- JSON-LD everywhere: Organization + WebSite (SearchAction /blog?q=), VideoObject + transcript + speakers + event,
  ProfilePage on speaker pages, Event performers + ItemList, BlogPosting mentions/isBasedOn. 27k blocks, all parse.
- Sitemap lastmod on 5,523 of 5,684 URLs (release day; was 191). IndexNow also on the 17:30 run for released talks.
- Posts: visible byline + updated date, "In short" line (= Description), fixed "Watch the talk" card. Talk pages link
  their write-up and up to 3 topic hubs. Lint: talk/sponsored Description must name Conf42.
- 45 topic hubs at /topics (_db/topics.yaml, intros written from the talks) + /topics index.
- Markdown twins for talk pages and posts; llms.txt gets Topics + llms/<event>.txt per event (96).
- Parked: rewriting YouTube descriptions to link conf42.com (backpocket).

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

## 2026-11-09 (evening: hold + URLs + privacy)
- Backfill held: 1,294 talk posts are `Status: queued` (live for ~1 h, then pulled). Marek rolls them out with
  `caffeinate -i blog/rollout.sh` (72 newest every 4 h, ~3 days) or `blog/release.sh N` (`blog_plan release N`).
- Event posts now live under their event: conf42.com/<event>/<slug> (1,441 rows moved, drafts too); the build writes a
  redirect stub at each old root URL <Date>-<slug> and `<base href="/">` on nested pages. Plugs/webinars stay at root;
  the 6 hand-written Harness recaps keep their URLs.
- Speaker privacy: empty/non-employer Company1 is deliberate. 52 posts edited to drop employers named only in the
  recording and every "listed with"/"the CSV" phrasing; lint now rejects that phrasing.
- 3 plugs unhidden: CONF42 is a calendar-level Luma coupon.

## 2026-11-09 (midday) - cards + purged videos
- Cards: 16:9 YouTube thumbnail for talk posts (teaser-page thumbnail before the video is out), never the headshot;
  every card 16:9; "BLOG" pill; /blog = 4 a row, titles only.
- Purged videos take their post: the build hides a talk whose YouTube link was emptied; `blog_plan orphan` also
  checks every linked video on YouTube and orphans dead ones; rollout/release run it before each slice.
- Orphaned: ml2025/llms-translate-cobol-humans-sign-off (Sandeep Gourneni, video gone from YouTube).
- YouTube ids with a `?si=` share tail are cleaned in the build (one ML talk).

## 2026-11-09 (afternoon) - thumbnails, plugs, duplicates
- YouTube thumbnails: cut shoulders carried on with LaMa (36 photos; hair keeps its fade). Only those redraw.
- Plugs show the sister event's own splash (og:image), not a venue photo.
- 21 Jan-2026 event overviews of 2025-26 events -> `replaced:` by their roundups (old URLs redirect).
- No same picture on two cards in a row (build check + swap within a day).
- Held (hidden) for a wrong video link in the sheet: platform2026 Sergey Pronin (links Shem Magnezi's),
  sre2026 Bhargavaram Potharaju (links Abhiram's), sre2025 Sujeeth Manchikanti (links Vishal Jaiswal's).


## 2026-11-09 (evening) - wrong links fixed, search
- Audit of every 2025+ talk link vs the event playlists/YouTube: 3 wrong links fixed in Excels_for_WWW + the CSVs
  (Sergey Pronin, Bhargavaram Potharaju, Sujeeth Manchikanti); their posts link the right video and are back.
- The 9 "wrong transcript" talks: transcripts match the published videos to the second (Descript agrees for the 2026
  ones) - the speakers recorded a different talk than the sheet title. 8 posts written from the recordings (queued);
  Krishna Rao Vemula Golang 2025 skipped: same recording as his SRE 2025 video.
- Sandeep Gourneni (ML 2025): video gone; not among the channel's 3,849 public uploads. Post stays orphaned.
- /blog search field (the conference pages' talk search).
