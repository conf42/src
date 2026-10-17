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

## The usual job: "activate the factory" + a Drive folder link

1. `drive <short_url> <drive folder link>` (background). It lists the public folder, downloads only new or changed
   videos and decks (size-checked), flags talks whose video was re-uploaded, matches files to speakers and runs the
   whole pipeline. The link is remembered: later just `drive <short_url>`. **Never download through a browser**, never
   ask the person to download.
2. When it ends, report: finished / failed talks, QA flags (loudness, >25 % cut, "picture changes in the first 12 s -
   check the start"), files NOT MATCHED (ask the person which speaker they belong to, then rename to the speaker's name
   exactly as on the site and run again), and talks with **no video yet** - a normal follow-up list for a remote
   conference (with the days left before the event), never an alarm.
3. Outputs: `<Desktop>/talk-factory/final videos for YouTube/`, `<event>/srt/`, `<event>/slides/`,
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
- "Publish to conf42.com/factory" (app) updates the website's Factory tab; runs also publish by themselves.
- If you change the factory: update `factory/MANUAL.md` (and `MANUAL-CLAUDE.md`) plus the Changelog in the same commit,
  run `../env/bin/python tests/smoke.py`, and commit only your files.
