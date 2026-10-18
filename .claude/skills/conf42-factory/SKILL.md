---
name: conf42-factory
description: Operate the Conf42 talk factory (factory/ in this repo) - turn the talk videos speakers upload to an event's Google Drive folder into finished YouTube-ready MP4s, subtitles, chapters and slide decks via Descript. Use when someone asks to run / activate the factory for an event, process a Drive folder, check the factory status, retry or redo a talk, handle a re-uploaded video, prepare slides, or write YouTube items.
---

# Conf42 talk factory - how Claude runs it

The team manual is `factory/MANUAL.md` and `factory/MANUAL-CLAUDE.md`, published at conf42.com/factory (password: ask
the person). Technical details: `factory/README.md` - read the section you need before changing anything.

## Basics

- Run from `factory/` with the repo's venv and UTF-8:
  - Mac/Linux: `cd factory && PYTHONUTF8=1 ../env/bin/python -m factory <command> ...`
  - Windows: `cd factory; $env:PYTHONUTF8=1; ..\env\Scripts\python -m factory <command> ...`
- No venv / not set up: the person runs `bash factory/setup.sh` or `factory\setup.cmd` themselves (it asks for their
  Descript token, which never goes through you). Health check: `-m factory doctor`.
- Events are named by their `short_url` (e.g. `featureflags2026`), from `metadata.yml`.
- Long jobs go in the background. The app is http://localhost:8042 (`run.sh` / `run.cmd`).
- **"Launch / activate the factory" always opens the app**: `... -m factory serve` in the background opens
  http://localhost:8042, reusing an app that's current and replacing one running older code - every time
  (Marek, 2026-10-17).
- **Low disk space: offer a junk and cache clean-up** (Marek, 2026-10-17). When a run stops for space, the
  health check says "free some space", or the person mentions a full disk, offer to clean junk and cache files from
  their drive. Never delete on your own:
  1. Measure first (`du -sh` on the Mac, folder sizes on Windows) and show a table: what it is, its size, and whether it
     comes back by itself.
  2. Candidates, all safe to lose:
     - Mac: the Trash; `~/Library/Caches` (quit the apps first); Xcode `DerivedData` and unavailable simulators
       (`xcrun simctl delete unavailable`); `brew cleanup`; `npm cache clean --force`; `pip cache purge`; unused Docker
       data (`docker system prune`); video apps' caches (Descript's local media cache, Adobe Media Cache, DaVinci
       Resolve CacheClip, Final Cut render files).
     - Windows: the Recycle Bin, `%TEMP%`, Disk Cleanup (`cleanmgr`, including Windows Update clean-up), browser caches,
       the same app and developer caches.
     - On either: old installers in Downloads (`.dmg`, `.pkg`, `.exe`, `.msi`, `.zip`) - list them and let the person
       pick.
  3. Delete only what the person picks, say how much was freed, run `doctor` again and carry on with the job.
  - **Never offer:**
    - recordings, event folders, `in/` copies, or anything on the Desktop the person put there;
    - Documents, Photos and Lightroom libraries, iCloud or OneDrive files;
    - git repos and their worktrees - point those out, but the person (or that repo's own session) decides;
    - running VMs.
- **Keep the factories in step with the websites**: when a site change alters something a factory reads (folder
  layout, CSV columns, metadata keys, teaser/thumbnail URLs), adapt this factory and the LIVE factory
  (sreday repo, `live-factory/`) in the same job, test them, and update their manuals (Marek, 2026-10-17).

## The usual job: "activate the factory" + a Drive folder link

1. `drive <short_url> <drive folder link>` (background). It lists the public folder, downloads only new or changed
   videos and decks (size-checked), flags talks whose video was re-uploaded, matches files to speakers and runs the
   whole pipeline. The link is remembered: later just `drive <short_url>`. **Never download through a browser**, never
   ask the person to download.
2. When it ends, report: finished / failed talks, QA and health flags (loudness, >25 % cut, "picture changes in the
   first 12 s - check the start", setup the speaker talks over), what the health check fixed or cut, talks that **need
   a new video** (`needs_new_video` in the status summary: no sound, muted, almost no sound - never uploaded; the
   speaker must re-upload), files NOT MATCHED (ask the person which speaker they belong to, then rename to the speaker's name
   exactly as on the site and run again), and talks with **no video yet** - a normal follow-up list for a remote
   conference (with the days left before the event), never an alarm.
3. Outputs, in the event's folder `<Desktop>/video factory - Conf42 <Event> <Year>/` (one per conference, so several can
   run at once): `final videos for YouTube/`, `srt/`, `slides/`,
   `<event>/YouTube items.txt` (`chapters <short_url>` rewrites it).

Other commands: `run`, `match`, `status`, `retry <short_url> "<speakers>"`, `redo <short_url> "<speakers>"`,
`slides <short_url>`, `drive-check <short_url> listing.json`, `unpause <short_url>`, `serve`.

## Rules

- A speaker's newer upload on Drive means: redo that talk (the drive command does it; the old final moves to
  `out/replaced/`, kept).
- "EDITS PAUSED": look at the edit report in `state.json` (`talks.<name>.steps.edit.report`) and the talk in Descript
  before `unpause` - an edit cost too much or mentioned other talks.
- 402 from Descript = out of credits/minutes: tell the person; nothing is paid twice after a top-up.
- One computer per event (the app claims it through `_db/factory.json`); `--force` only when the person says the other
  computer is off.
- Never put a Descript token or password in a file, commit or the chat. Don't delete work files without asking.
- "Publish to conf42.com/factory" (app) updates the website's Factory logs tab; runs also publish by themselves.
- If you change the factory: update `factory/MANUAL.md` (and `MANUAL-CLAUDE.md`) plus the Changelog in the same commit,
  run `../env/bin/python tests/smoke.py`, and commit only your files.
