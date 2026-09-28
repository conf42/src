# factory - Conf42 talk videos and slides, from the Drive download to finished files

Conf42 talk videos, from the Google Drive download to finished, YouTube-ready files on the Desktop:

```
Drive zips  ->  unzip + match to speakers  ->  Descript (upload, AI edit, publish)  ->  MP4 + SRT  ->  loudness  ->  QA
```

Per talk:

1. **Match** the video to its talk in `_db/<EVENT>.csv` and rename it to the speaker(s) exactly as on the site
   (`Name1` or `Name1 & Name2`). Files that match nobody are never guessed; they are listed as "not matched".
2. **Upload** to one Descript project per event, named from `settings.yml` (`Conf42 DevSecOps 2026`), one composition per talk.
3. **Edit** with Descript's AI editor: Studio Sound 80%, limiter, volume 300%, filler words removed, word gaps over 2s cut to 1s.
4. **Publish** (unlisted) at the largest size not above the source or `max_resolution`, and **download** the MP4.
5. **SRT** transcript, named `<short_url>_<Name1>.srt`, which is what the site expects in `src/srt/`.
6. **Loudness**: ffmpeg measures each video and sets it to YouTube's level (-14 LUFS, true peak -1.5 dB).
   The video stream is copied, so there's no quality loss.
7. **QA** measures the result and flags talks whose loudness is off or where the edit cut too much.

Output goes to `Desktop\talk-factory\<short_url>\`:

- `out\<speakers> - Conf42 <Event> <Year>.mp4`: finished videos.
- `srt\`: transcripts.
- `in\`: renamed source videos.
- `slides\`: any decks that were in the zips.
- `state.json`: the progress of every step.

A run can be stopped and started again at any time. Finished steps are skipped, and a failed talk is retried on its own.

## Use

- **App:** double-click `run.cmd` and it opens http://localhost:8042. Pick the event and press Start. The app shows per-talk progress and has Retry, Settings, Open folder and "Publish status" buttons. Publish status updates the hidden page `conf42.com/factory`.
- **Command line** (from this folder, with the site venv and `PYTHONUTF8=1`):

  ```
  ..\env\Scripts\python -m factory match  devsecops2026 C:\Users\<you>\Desktop\drive-download-*.zip
  ..\env\Scripts\python -m factory run    devsecops2026
  ..\env\Scripts\python -m factory status devsecops2026
  ..\env\Scripts\python -m factory retry  devsecops2026 "Emmy Eide"
  ```

- **Watching it:** the app's "Right now" box shows whether a factory run is alive (process + last activity), every Descript job of the event's project with its progress bar (upload, edit, publish, mapped to talk names), the AI credits paid so far, and a link to the project in Descript. Running steps show their live label in the talk table ("uploading 45% of 1.2 GB", "Descript is busy ..."). Running `run.cmd` again when the app is already up just opens the page. conf42.com/factory shows the same table, updated every `status_publish_minutes`.
- **With Claude:** say "here are the drive videos for Conf42 DevSecOps", or share the Drive folder link, and it runs the whole loop, slides included.

## Slides

Decks from the Drive download are matched to talks like the videos, then:
- one deck is kept per talk: a PDF wins over a PPTX, and identical duplicates are dropped
- anything that isn't a PDF is converted with LibreOffice
- the deck is renamed `<Name1>[ & <Name2>] - Conf42 <Event> <Year>.pdf`, the name the site's Slides column and `static/slides` use
- every deck over `slides_max_mb` (5) is compressed; the page count is checked and the original kept in `slides originals`

`python -m factory slides <short_url> [zip ...]` runs just this step.

## Rate limits and credits

Descript runs ONE job per project at a time; anything else gets 429 "A job is already running for this project". The client waits and retries for up to an hour, so talks simply take turns. An upload that died with a stopped run keeps its import job waiting forever and blocks the project: every run starts by cancelling those (`DELETE /jobs/<id>`).

The edit prompt names the talk's composition (`{composition}`). Without that, "apply to all clips" made the AI editor re-edit every talk in the project (48 credits instead of ~8). As a safety net, an edit costing more than `max_edit_credits` pauses all further edits (`edits_paused` in state.json).

Nothing is paid for twice:
- a composition already in the Descript project is reused instead of uploaded again
- an edit is skipped when the ledger of paid edits (`Desktop\talk-factory\ledger.json`) lists it, or when the composition is already shorter than its media

## Setup (any machine: Windows, macOS, Linux)

1. Get the repo. The full `src` history is ~12 GB; the factory needs only `factory/`, `_db/` and `metadata.yml`, so a slim
   clone takes seconds (3.5 MB) and can still push the status page and the machine lock:

   ```
   git clone --depth 1 --filter=blob:none --sparse https://github.com/conf42/src
   cd src && git sparse-checkout set factory _db
   ```
   (Add `conf42/static` next to it only if this machine ships slides.)
2. Run the one-time setup:
   - **Windows:** double-click `factory\setup.cmd`
   - **macOS / Linux:** `bash factory/setup.sh`

   It creates the Python environment, installs what is missing (ffmpeg, LibreOffice), asks for a name for this machine
   and for the Descript API token (Descript > Settings > API tokens), puts a **Conf42 factory** launcher on the Desktop,
   runs the health check and opens the dashboard.
3. Later: double-click the launcher (or `run.cmd` / `run.sh`). `python -m factory doctor` re-runs the health check;
   the dashboard shows a banner when something is off.

Where things live:
- **Descript token:** never in git (this repo is public). Windows: the user environment variable `DESCRIPT_API_TOKEN`;
  macOS/Linux: `~/.conf42-factory/descript_token` (readable by you only). An environment variable always wins.
- **Per-machine settings:** `factory/settings.local.yml` (git-ignored) overrides `settings.yml`: `machine_name`,
  `work_root` (default `<Desktop>/talk-factory`, OneDrive Desktops included), `render_parallel` (`auto` = up to 8 renders
  on an RTX 5090, 3 on other NVIDIA cards, Apple's media engine on Macs, 2 on CPU).
- **Work files** (videos, state, ledger of paid edits) stay on the machine that runs the event.

**One machine per event.** Descript runs one job per project and the factory cancels uploads it does not own, so two
machines on the same event would fight. Every run claims the event through `_db/factory.json` (pushed with the
status page) and a second machine refuses to start it while the first one is alive. If that machine is off, take over
with Shift+click on Start (or `python -m factory run <event> --force`); a lock nobody refreshed for 45 minutes expires.
Moving an event mid-way is safe for credits: talks already in Descript are reused, edited ones are not edited again.

**Credits and minutes:** imports use media minutes and each AI edit about 8-12 AI credits per talk; Descript answers
402 when the plan runs out. The dashboard shows this month's API usage (set `plan_ai_credits_month` /
`plan_media_minutes_month` to see what is left - Descript has no balance endpoint).
