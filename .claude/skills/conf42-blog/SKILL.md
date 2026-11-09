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

Images: leave `ThumbnailPath` empty and the build picks the right existing asset (talk/sponsored -> the video's 16:9 YouTube
thumbnail, before the video is out the teaser page's rendered thumbnail, never the headshot; roundup -> event
splash, webinar -> its splash, plug -> the sister site's hero photo). The planner suggests an existing
`<EVENT><YEAR>_<Sponsor>.png` for sponsored posts - use it when given. Never make new art.

## The run ("run blog maintenance")

1. `git pull --rebase` in conf42 and the four sister repos (stash local changes in conf42 first, pop after).
2. `env/bin/python -m build.blog_plan plan > /tmp/plan.json` (also refreshes `_db/sister_events.json`). Read:
   - `orphaned` -> `python -m build.blog_plan orphan` (sets Status=orphaned; the build already hides them). Purged videos
     go too (Marek 2026-11-09; speakers ask years later): `orphan` also orphans a talk whose YouTube cell was emptied
     and any post whose linked video YouTube no longer has (oEmbed 404). Run it every maintenance run; the rollout
     scripts run it before each slice. The build hides an emptied-link post on its own.
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
   `<event short_url>/lowercase-words` (conf42.com/prompt2026/agent-prompt-is-one-layer), Marek 2026-11-09: the
   conference is always in the URL, so similar talks at two events (Remix re-airs, a sponsor's repeat talk) never
   look like duplicates. The build writes `docs/<event>/<slug>.html` with `<base href="/">` and a redirect stub at the
   old root URL `<Date>-<slug>`. Plugs and webinars (no Event) stay `YYYY-MM-DD-lowercase-words` at the root.
5. Plugs for paid events: CONF42 (42% off) is a **calendar-level** Luma coupon (Marek 2026-11-09), valid on every
   event of the calendar - `list_coupons` with the event's `calendar_id`, not just `event_id`. Only if it is missing
   there: `create_coupon` CONF42, 42% off. Free events: skip.
6. `python -m build.blog_plan check <drafts>` lints drafts in memory without touching the CSV - parallel writers
   (one sub-agent per batch, each told to run only `check`) use it. Then `python -m build.blog_plan add blog/drafts/*.md`
   and `python -m build.blog_plan lint` until it reports 0. The linter also rejects links to talks the repo no
   longer has: local `docs/` keeps pages of removed talks, so "the file exists" is not proof.
   Big batches (backfills, dozens of posts at once): `add` them, then set `Status: queued` on the new rows - never
   push hundreds of live posts in one go. Marek starts `caffeinate -i blog/rollout.sh` (72 newest every 4 h, ~3 days
   for 1,300) or `blog/release.sh N` (`blog_plan release N`) when he wants them out. Google-safe = gradual.
7. `env/bin/python -m build.generate` once (no loops) and open one new post's HTML to eyeball title/meta.
8. Commit (`_db/blog.csv`, `_db/sister_events.json`, `blog/CHANGELOG.md`) and push main directly.
9. Mirror to the Sheet: `python -m build.blog_plan export /tmp/blog.json`, then Sheets connector `update_values` on
   spreadsheet `1_-90A9g5_ACqeZl9bQuIHwfox2_-2gGh3cJMNjBrsHs`, tab `blog`, starting at `A1` (values only, never
   formatting; clear rows below the new end if the CSV shrank). Cells over 50,000 chars: say so, don't truncate.
   Size: the export is ~1 MB (post bodies) and grows each run - too big to push through the connector by hand.
   `=IMPORTDATA(raw CSV)` does NOT work (#REF!, quoted newlines). Until Marek picks a route, report it as pending.
10. Append a dated entry to `blog/CHANGELOG.md`: what was published/scheduled/orphaned/enriched, what's next.
11. Tell Marek in a few lines: N posts written (by type), next due dates, anything skipped and why.

## House voice (read `blog/STYLE.md` before writing - it has the good-vs-slop examples)

Witty, nerdy, smart. A senior engineer telling a peer about a talk worth their evening. Lead with the most surprising
concrete thing in the source. Full names: people, companies, tools, versions. One on-topic joke per section, max.
Short paragraphs, plain verbs, real numbers only. Answer-first: the first two sentences say who, what, at which
Conf42 event, and the takeaway (that's the passage search engines and AI answers quote).

## Hard rules

- A hand-written 2025+ post already covering the same talk/event (the 2025-26 Harness recaps): don't write a second
  one. Give the old row its Type/Event/Ref/Sponsor and leave its text alone (lint then checks only its Ref).
- Paid plug whose CONF42 coupon couldn't be created: add it with `Status: hidden` and tell Marek; flip to empty once
  the coupon exists. Never publish a code that doesn't work.
- Never invent a quote, number, feature, customer or result. Quotes are verbatim from the transcript/abstract (the
  linter checks). No transcript yet? Write from the abstract and say "in the talk" without quoting.
- Never touch legacy rows dated before 2025 (no Ref; the linter refuses). Typed rows dated Dec 2024 (DevOps 2025
  talk posts) are ours and editable.
- Transcript is a different talk than the CSV row (wrong srt/YouTube): skip that post and report it. Abstract
  promises more than the talk delivers: write from the transcript and say so.
- Talk/sponsored posts end with `[Watch the talk on YouTube](<url>).` once the video exists (that clears `enrich`).
- Company1 empty or holding a job title/university is deliberate (the speaker doesn't want the employer shown):
  never name an employer from the transcript, never mention "the CSV"/"listed with" (lint rejects it), never report
  it as a data problem.
- A sponsored speaker with two similar talks at two events is normal (slow-producing sponsors): both posts stay.
- Never edit the talk CSVs, metadata.yml lineups or WEBINARS.csv to make the blog work - report the data problem.
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

Cards are 16:9, cropped to fill, with a "BLOG" pill in the corner; /blog shows 4 a row, picture + title only
(Marek 2026-11-09). The home page keeps its 2 bigger cards.
