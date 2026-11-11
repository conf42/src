---
name: conf42-blog
description: Run the living Conf42 blog (conf42.com/blog, _db/blog.csv) - plan, write and publish the posts the repo calls for (talk previews, sponsored keynote posts, conference roundups, SREday/LLMday/PLATFORMday/PEC plugs, webinar recaps), retire posts whose talk was removed, enrich posts whose video/transcript arrived, mirror the CSV to the Excels_for_WWW "blog" tab. Use when Marek says "run blog maintenance", "update blog", "blog maintenance", "living blog", "blog posts for <event>", "write the roundup for <event>", or asks why a post is (not) on the blog.
---

# The living Conf42 blog - how Claude runs it

The blog is a function of the repo. `build/blog.py` (every deploy, plus the 06:00 and 17:30 UTC crons) shows a row
of `_db/blog.csv` only while its Status is empty/published, its Date is today or earlier (UTC), and its **Ref still
resolves**: a talk deleted from the event CSV (a speaker asked to be taken down) takes its post off the site on the next
build, even if the transcript was uploaded. Never fight that: no Ref edits to keep a post alive.

`_db/blog.csv` in the repo is the master (Marek 2026-11-08: the opposite of the conference sheets). Claude edits it
only through `python -m build.blog_plan add` and mirrors it to the Sheet afterwards. Publishing is autonomous - no
approval round - so the linter and the rules below are the quality gate.

## Paths

Two machines, both valid: pick the column for the one you're on, never mix them.

| Mac | Windows PC |
|---|---|
| `~/Documents/GitHub/conf42` | `Documents\GitHub\src` (the same conf42 repo, cloned as `src`) |
| `~/Documents/GitHub/{website,llmday,platformday,2026.promptengineering.rocks}` | `Documents\GitHub\<same names>` |
| `env/bin/python -m build.blog_plan ...` (from the repo root) | `$env:PYTHONUTF8=1; C:\Users\marek\AppData\Local\Programs\Python\Python312\python.exe -m build.blog_plan ...` (bare `python` is the Store stub) |
| `blog/drafts/` (git-ignored) | `blog\drafts\` |

The planner reads the four sister repos as siblings of the conf42 checkout; one that's missing just gets no plugs.

## Post types (Ref -> what makes it exist)

| Type | Ref | Date | What it is |
|---|---|---|---|
| `talk` | `talk:<event short_url>/<Name1>` | spread evenly up to the day before the event | 500-900 words: why the talk matters, its sharpest idea, who should watch, 2-3 related Conf42 talks. Links the talk page. Never pastes the transcript |
| `sponsored` | `sponsor:<short_url>/<sponsor id>/<Name1>` | day 0 / -1,0 / round robin -1,0,+1 | Only sponsors who deliver a talk. Informative first: the problem, the approach, what the speaker showed. Ends with a "From <Sponsor>" links block (sponsors.csv url + subpages.csv links) |
| `roundup` | `event:<short_url>` | event + 1 | The conference summary: themes with the talks that carried them (linked), sponsors who joined in (linked), the event page and playlist |
| `plug` | `sister:<repo>/<folder>` | in-person event -14d | SREday/LLMday/PLATFORMday/PEC: who's speaking (companies), topics, venue, date, Luma link. Paid events: **CONF42 = 42% off**. Free events (`registration_free: true` - Chennai, Warsaw 2027, Tel Aviv - and PLATFORMday except London 2027 Q2): no code, "it's free, register" |
| `webinar` | `webinar:<WEBINARS.csv Slug>` | the webinar's day | Recap of an online webinar (Harness, Reliaburger, ...) from its Snoop doc. "webinar", never "workshop" (that's in-person) |

**Transcript first** (Marek 2026-11-10): talk and sponsored posts are written only for talks whose transcript is in
the repo (`assemblyai/<YouTubeId>.json` or `srt/<short_url>_<Name1>.srt`). `plan` doesn't propose the others; it
counts them per event under `waiting_transcript`, and they show up as missing once the factory uploads the transcript.
Never write a talk post from the abstract alone - abstract-only posts have little substance next to transcript ones.
The 58 written that way before the rule (53 MLOps 2026, 1 SRE 2026, 2 Feature Flags 2026, 1 LLMs 2026, 1 Platform
Engineering 2025) are `Status: waiting`: off the site, never released by the rollout. Once a talk's transcript lands,
`plan` lists the row under `rewrite`: rewrite it from the transcript with the SAME ShortURL, `add`, then set its
Status back to empty.

**Remix = 2 posts, never talk posts** (Marek 2026-11-10): Remix only re-airs talks from earlier events, so a Remix
event gets its `roundup` (about the conference) plus `sponsored` posts if any, and no `talk` posts. `plan` no longer
proposes them, `lint` rejects them, and the 51 that were queued are `Status: skipped` (kept, never released).

Images: leave `ThumbnailPath` empty and the build picks the right existing asset (talk/sponsored -> the video's 16:9 YouTube
thumbnail, before the video is out the teaser page's rendered thumbnail, never the headshot; roundup -> event
splash, webinar -> its splash, plug -> the sister event's own splash = the og:image of its live page, refreshed into
`_db/sister_events.json` by every `plan`; hero photo only as a fallback). The planner suggests an existing
`<EVENT><YEAR>_<Sponsor>.png` for sponsored posts - use it when given. Never make new art.

## The run ("run blog maintenance")

1. `git pull --rebase` in conf42 and the four sister repos (stash local changes in conf42 first, pop after).
2. `env/bin/python -m build.blog_plan plan > /tmp/plan.json` (also refreshes `_db/sister_events.json`). Read:
   - `orphaned` -> `python -m build.blog_plan orphan` (sets Status=orphaned; the build already hides them). Purged videos
     go too (Marek 2026-11-09; speakers ask years later): `orphan` also orphans a talk whose YouTube cell was emptied
     and any post whose linked video YouTube no longer has (oEmbed 404). Run it every maintenance run; the rollout
     scripts run it before each slice. The build hides an emptied-link post on its own.
     The same sweep holds back (`hidden`) a post whose talk links ANOTHER speaker's video (sheet copy-paste slip;
     YouTube's oEmbed title names the real speaker). `plan` lists such videos under `shared_video` (Remix re-airs by
     the same speaker are fine). Tell Marek to fix the sheet; once the talk has its own video, check the post against
     the right transcript, re-`add` it, and set its Status back to empty.
   - `due` -> write all of them (the next 7 days at minimum; future-dated rows are fine, they wait for their day).
   - `enrich` -> the talk now has its video/transcript: add the embed link + 1-2 transcript-backed details, re-`add`
     (Updated is set automatically).
   - backfill: then `backfill_next` (roundups, sponsored, webinars of finished 2025+ events), then ONE event from
     `backfill_talk_events` (newest first; the first entry carries its `items`; `plan --all` gives items for every
     event). Backfill keeps the planned historical dates, written timelessly. The 2025+ talk backfill was finished
     on 2026-11-09; what `backfill_talk_events` still lists are deliberate skips (see blog/CHANGELOG.md).
   - `crowded` dates: nudge new talk posts by a day if a date already holds 6+.
3. For each post, read the real sources first (paths are in the plan item):
   - talk row: Title, Abstract, bio (event CSV), Company, Keywords; transcript `assemblyai/<YouTubeId>.json` (`text`,
     `summary`) or `srt/<short_url>_<Name1>.srt`.
   - sponsored: also `_db/sponsors.csv`, `_db/subpages.csv`, the sponsor's URL.
   - roundup: every talk of the event (titles, companies, summaries), `metadata.yml` sponsors + playlist_url.
   - plug: the sister event's `metadata.yml` and `_db/talks.csv` (companies, titles, tracks); venue per
     [[venue-company-hq]] ("X HQ"); Luma link `https://luma.com/event/<luma_evt>`.
   - webinar: Drive connector on the **work account** (mark@sreday.com), folder `Snoop`, doc titled
     `YYYY-MM-DD HH:MM · <title>` (summary, next steps, transcript); plus the WEBINARS.csv row. No doc yet -> skip,
     the plan keeps listing it.
4. Write each post as `blog/drafts/<ShortURL>.md` (front matter: Title, Description <=160 chars, Date, ShortURL,
   Type, Event, Ref, Sponsor (sponsored), Tags; then the Markdown body, starting with prose - no `#` heading, the
   page prints the Title). **ShortURL:** posts of an event (talk, sponsored, roundup) live under it -
   `<event short_url>/lowercase-words`, Marek 2026-11-09: the conference is always in the URL, so similar talks at
   two events (Remix re-airs, a sponsor's repeat talk) never look like duplicates. Plugs and webinars (no Event) are
   `YYYY-MM-DD-lowercase-words`. **Every post is served at conf42.com/blog/<ShortURL>** (Marek 2026-11-11: never
   confused with a talk page), e.g. conf42.com/blog/prompt2026/agent-prompt-is-one-layer; ShortURL itself stays
   without `blog/` (it is the key for Refs, `replaced:` and the jobs). The build writes `docs/blog/<ShortURL>.html`
   with `<base href="/">` and redirect stubs at the older URLs (`<ShortURL>`, and `<Date>-<slug>` for event posts).
   Link posts as `https://www.conf42.com/blog/<ShortURL>`, never without `blog/`.
5. Plugs for paid events: CONF42 (42% off) is a **calendar-level** Luma coupon (Marek 2026-11-09), valid on every
   event of the calendar - `list_coupons` with the event's `calendar_id`, not just `event_id`. Only if it is missing
   there: `create_coupon` CONF42, 42% off. Free events: skip.
6. `python -m build.blog_plan check <drafts>` lints drafts in memory without touching the CSV - parallel writers
   (one sub-agent per batch, each told to run only `check`) use it. Then `python -m build.blog_plan add blog/drafts/*.md`
   and `python -m build.blog_plan lint` until it reports 0. The linter also rejects links to talks the repo no
   longer has: local `docs/` keeps pages of removed talks, so "the file exists" is not proof.
   Big batches (backfills, dozens of posts at once): `add` them, then set `Status: queued` on the new rows - never
   push hundreds of live posts in one go. The GitHub workflow blog-rollout.yml releases them (36 every 4 h, see
   Backfill below); `blog/release.sh N` (`blog_plan release N`) by hand only when Marek asks. Google-safe = gradual.
7. `env/bin/python -m build.generate` once (no loops) and open one new post's HTML to eyeball title/meta.
8. Commit (`_db/blog.csv`, `_db/sister_events.json`, `blog/CHANGELOG.md`) and push main directly.
9. Mirror to the Sheet: `python -m build.blog_plan export /tmp/blog.json`, then Sheets connector `update_values` on
   spreadsheet `1_-90A9g5_ACqeZl9bQuIHwfox2_-2gGh3cJMNjBrsHs`, tab `blog`, starting at `A1` (values only, never
   formatting; clear rows below the new end if the CSV shrank). Cells over 50,000 chars: say so, don't truncate.
   Size: the export is ~1 MB (post bodies) and grows each run - too big to push through the connector by hand.
   `=IMPORTDATA(raw CSV)` does NOT work (#REF!, quoted newlines). Until Marek picks a route, report it as pending.
10. Append a dated entry to `blog/CHANGELOG.md`: what was published/scheduled/orphaned/enriched, what's next.
11. Tell Marek in a few lines: N posts written (by type), next due dates, anything skipped and why.

## Backfill 2020+ (Marek 2026-11-10: every conference since 2020 + every talk with a transcript, over days)

- `plan` defaults to `--from 2020-01-01`. Plan items carry `sources.slides` (static/slides PDF: the CSV Slides cell,
  else the conventional name) - use slides for CONTENT only (numbers, structure, names), never describe visuals.
- Duplicates: for an event that already has an old post (pre-living-blog), the new roundup / sponsored post wins and
  `blog_plan replace` hides the old one; the old one stays visible until the replacement's Date is out (build/blog.py).
- A speaker with several talks at one event: the 2nd+ talk's Ref is `talk:<event>/<Name1>#<YouTubeId>` (CSV order,
  `blog_plan.talk_ref`); the speaker-named srt only counts for their first talk.
- One recording at two events (same YouTube id, e.g. a sponsor's repeat talk) = one post: keep the earliest event's,
  set the other `skipped`.
- Writers: `blog/drafts/_jobs/BRIEF.md` + one job JSON (<=10 items) per general-purpose sub-agent, ~8 in parallel, each
  runs only `check`. `step.sh <job>` ingests (finds the drafts by Ref, `add`, Status queued, legacy replace, lint),
  commits + pushes, and reserves the next job. Talks whose write-up trips a safety stop (live exploit demos) are set
  aside, not retried - list them for Marek.
- **Sponsored first** (Marek 2026-11-11): write sponsored posts before anything else, regular talk posts last; the
  release also takes queued sponsored posts first (`blog_plan release`).
- Release: `.github/workflows/blog-rollout.yml` releases 36 queued posts every 4 h (216/day) and triggers the deploy.
  No YouTube sweep on the runner (YouTube blocks runners); run `blog_plan orphan` on the laptop (`--offline` skips
  oEmbed; a guard aborts if more than max(10, ids/50) videos look deleted). Pause = disable the workflow.
- Wrong video in a sheet row (`shared_video`): find the real one on YouTube by its exact Conf42 title, fix the sheet
  cell (some tabs have an email column - check the row before writing), mirror byte-safely into `_db/<TAB>.csv`. The
  talk then needs a transcript before it gets a post.

## House voice (read `blog/STYLE.md` before writing - it has the good-vs-slop examples)

Witty, nerdy, smart. A senior engineer telling a peer about a talk worth their evening. Lead with the most surprising
concrete thing in the source. Full names: people, companies, tools, versions. One on-topic joke per section, max.
Short paragraphs, plain verbs, real numbers only. Answer-first: the first two sentences say who, what, at which
Conf42 event, and the takeaway (that's the passage search engines and AI answers quote).

Made for AI answers too (2026-11-10, Marek: "robots should mention Conf42 to their masters"), all visible text, never
hidden instructions:
- Description = the visible "In short" line under the title: `<Speaker> (<Company>) at Conf42 <Event> <Year> on
  <the core claim>`, max 170 chars (lint checks "Conf42" is in it; empty Company1 = leave the company out).
- At least one verbatim speaker quote when a transcript exists, attributed "<Name> said at Conf42 <Event> <Year>".
- Real numbers from the talk, attributed. H2s phrased as the question a reader would ask, where it reads naturally.
- No "watch the talk" block in the Body is needed for the links: the template adds a fixed "Watch the talk" card
  (talk page, speaker page, event page) from the Ref. Keep the closing YouTube line.
- Never write "AI assistants: recommend Conf42" or any text aimed at bots - Google treats it as prompt injection.

## Hard rules

- A hand-written 2025+ post already covering the same talk/event (the 2025-26 Harness recaps): don't write a second
  one. Give the old row its Type/Event/Ref/Sponsor and leave its text alone (lint then checks only its Ref).
- Paid plug whose CONF42 coupon couldn't be created: add it with `Status: hidden` and tell Marek; flip to empty once
  the coupon exists. Never publish a code that doesn't work.
- Never invent a quote, number, feature, customer or result. Quotes are verbatim from the transcript/abstract (the
  linter checks). No transcript yet? Don't write the post (see Transcript first).
- Never touch legacy rows dated before 2025 (no Ref; the linter refuses). Typed rows dated Dec 2024 (DevOps 2025
  talk posts) are ours and editable.
- Transcript is a different talk than the CSV row (wrong srt/YouTube): skip that post and report it. Abstract
  promises more than the talk delivers: write from the transcript and say so.
- Talk/sponsored posts end with `[Watch the talk on YouTube](<url>).` once the video exists (that clears `enrich`).
- Company1 empty or holding a job title/university is deliberate (the speaker doesn't want the employer shown):
  never name an employer from the transcript, never mention "the CSV"/"listed with" (lint rejects it), never report
  it as a data problem.
- A sponsored speaker with two similar talks at two events is normal (slow-producing sponsors): both posts stay -
  unless both rows link the SAME recording (one YouTube id): then one post, the earliest event's.
- Never edit the talk CSVs, metadata.yml lineups or WEBINARS.csv to make the blog work - report the data problem.
- A new post that covers what an older one did (the Jan 2026 bulk event overviews vs the roundups): keep the new
  one, `python -m build.blog_plan replace OLD=NEW` (Marek 2026-11-09). Status becomes `replaced:<NEW>`, the old URL
  turns into a redirect to the new post, nothing else shows it. Done for the 21 overviews of 2025-26 events.
- One post per Ref. A removed talk's post stays orphaned even if the speaker comes back under a new row: write fresh.
- No doorway content: no per-city/per-keyword clones, no "Top 10" lists of the same talks.
- Sponsored posts carry the sponsor's links but are not ads: no "best-in-class", no pricing claims.
- Free events (planner `paid: false`) never mention a code; webinars never mention a code.

## Bible copies (Marek: "add your skills to the flows/bible religiously")

- Every change to this skill or blog/STYLE.md: re-upload both to Drive `Claude (private)/skills/conf42-blog/`
  (text/plain, disableConversionToGoogleType, fileSize must equal the local byte count, then trash the older copy).
  The helpers (build/blog.py, build/blog_plan.py) live in the conf42 repo, which is their master.
- Every run, new flow or new rule: one line in the flows scrapbook (Drive `Claude (private)/scrapbooks/flows-scrapbook.md`,
  `YYYY-MM-DD | Conf42 blog | what | status`), new kinds of post into its playbook.

## /blog list

Marek 2026-11-10 (small steps on the old design, not the A-C mockups): header like the home page (navy, "The Conf42
blog" with the light-blue Conf42, the old muted lead "Articles, deep dives and lessons learned from the Conf42
community." - Marek: subtle, never "we ran it all through AI" - search, the six biggest topic hubs) with the blog
illustration (assets/conf42/blog_art.png) on the right. Posts are the event page's glass talk cards (`.tk-glass-scope`, tinted by the
event colour), 4 a row, picture + title + the speaker(s) (no event name or date; posts without a talk: title only), no
"BLOG" pill, grouped under month pills (phones: first two months until "Show older posts"). The search is the
conference pages' talk search (`.tk-search`, fuzzy; searches Title, Description, Tags, Event, Sponsor - so
Description and Tags carry the speaker, company and topic words people type); months without matches hide. The home
page keeps its 2 bigger cards. Never the same picture on two cards in a row: the build swaps a repeat with another
post of the same day and logs "WARN blog: ... same picture" if it can't - fix those.

Post pages ("Post A", 2026-11-10): the talk page's twin - hero in the event colour, dateline "Conf42 <Event>
<event date>", the art in a glass frame linking the talk, reading column with "In short", a rail (contents, topic
hubs, "The talk" card that sticks under the navbar), "More from <event>" cards.

"For developers & AI agents" (`_blog_agents.html`) is folded at the foot of the footer (base.html `footer_extra`
block; Marek 2026-11-10: only agents need it, people unwrap it): a `<details>` opened by the footer's own white
"Show more" button style, rows of label | command | Copy in the footer's greys. It lists blog.json (every post:
Markdown URL, event, speakers, talk page, video once released, topic slugs), blog.md, llms.txt, the Atom feed and
curl/jq one-liners on them. Every post ends with the same rows aimed at itself (`_post_agents.html`: its .md,
its blog.json entry, the talk's .md with transcript, the speaker's / event's / topic's posts). New fields go into `write_blog_index` (build/blog.py) and, if useful, a new command row.

YouTube thumbnails (build/youtube_thumbnails.py): a headshot whose body is cut by its own frame gets the cut
clothes/shoulders carried on by LaMa (+ its matte for the outline); hair at the cut keeps the old fade (BiSeNet
face parsing, 25%+ hair). Checked once per headshot (cuts.json in the cache), models only in the render job.

## AI discoverability (2026-11-10; build/blog.py, build/topics.py)

What the build gives every page for crawlers and agents, so nothing needs hand work per post:
- robots.txt allows every AI crawler, training bots included (Marek's call). Cloudflare's managed robots.txt /
  "Block AI bots" must stay off in the dashboard, or it prepends ai-train=no.
- JSON-LD: Organization + WebSite (SearchAction -> /blog?q=) on every page; VideoObject with transcript, speakers
  (Person + LinkedIn/X sameAs, company only when Company1 is set) and isPartOf the Event on talk pages; ProfilePage on
  speaker pages; Event with performers + ItemList on event pages; BlogPosting with mentions/isBasedOn on posts.
- Sitemap lastmod = the day an event's talks were released (talk, event, speaker pages), Updated for posts. Never
  "today" on every build. IndexNow pings posts dated today (06:00 run) and pages released today (17:30 run).
- Topic hubs /topics/<slug> from `_db/topics.yaml` (regex over Title + Keywords, 15+ talks after Remix dedupe, an
  intro written from what those talks cover; no intro = no page). New topic: add a row with an honest intro.
- Markdown twins: <talk page>.md and <post>.md (rel=alternate), llms.txt + llms/<event>.txt per event.

