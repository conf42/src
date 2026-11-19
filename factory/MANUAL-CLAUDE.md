# Conf42 talk factory - with Claude

<p class="tag-good">Recommended!</p>

The same job as the **No Claude, manual** tab, but you talk to Claude and it runs the factory for you: it fetches the speakers'
videos from the event's Drive folder, matches them to the talks, sends them through Descript, checks the results and
writes the YouTube texts. You check the results and do the YouTube upload.

Claude knows the factory through the **conf42-factory skill** that comes with the conf42 repo, so any teammate's Claude
works the same way.

---

## 1. One-time setup

1. **Claude Code**: install it from https://claude.com/claude-code (the desktop app, or in a terminal
   `npm install -g @anthropic-ai/claude-code`) and sign in with your Claude account.
2. **The repo** - a slim copy is enough:

    ```
    git clone --depth 1 --filter=blob:none --sparse https://github.com/conf42/src
    cd src
    git sparse-checkout set factory _db .claude
    ```

3. **The factory itself**, once - run it yourself, because it asks for your Descript API token (Descript → Settings →
   API tokens), which should never go through a chat:

    - Windows: double-click `factory\setup.cmd`
    - Mac / Linux: `bash factory/setup.sh`

4. **Start Claude in the `src` folder**: open a terminal there and run `claude`. Check it with: *"Is the Conf42
   factory ready on this computer?"*

---

## 2. Process an event - what to say

| Step | Say to Claude | What happens |
|---|---|---|
| Start | *"Activate the factory for Feature Flags 2026: https://drive.google.com/drive/folders/…"* | Claude fetches the Drive folder (only new or changed files), matches every video to its talk and starts the whole run in the background. |
| Another computer ran it | *"Reactivate the factory for Cynthia: <Drive link>"* | Before anything starts, Claude reads the event's launch log (`_db/factory_runs/<event>/LAUNCHES.md`, written by the factory on every launch, on every computer) and the Descript project, and tells you what is already done. Finished talks are not downloaded again on the new computer. |
| Fast track | *"Factory fast track for MLOps"* - nothing else | For a talk that must go out now (a sponsor's video, a last-minute upload). Claude looks on your **Desktop** for the newest videos and decks, matches them to the event's speakers by name and content (asks only when it cannot tell), renames them to the speaker's name, and sends them straight from the terminal (`factory/fasttrack.sh`) to the cloud factory, which runs just that event. No Drive upload by you. Claude watches the run and gives you the YouTube link. |
| Watch | *"How is it going?"* - or open http://localhost:8042 | Per talk: render, upload, Descript edit, publish, download, subtitles, chapters, loudness, QA. |
| Unmatched files | Claude asks you which speaker a file belongs to | It renames it and runs it. |
| Check | *"What needs my attention?"* | Talks with QA or health flags (loudness, too much cut, setup the speaker talks over), talks that **need a new video** (no or muted sound - not sent to Descript), failed talks, and the **no video yet** follow-up list. Watch the flagged ones. |
| New upload | *"Some speakers uploaded new versions - check the Drive again."* | Claude fetches the folder again; re-uploaded talks are done again from scratch. |
| New folder | *"Activate the factory again for Prompt Engineering 2026: <new Drive link>"* | Claude switches the event to the new folder. Files it already has (same size) are not downloaded again and finished talks are not redone; only new or re-uploaded videos run. Claude checks every finished talk is still in the new folder - the old folder is no longer watched. |
| Slides | *"Prepare the slides."* | Decks matched, converted to PDF, renamed for the site, compressed. |
| YouTube | *"Write the YouTube items."* | Titles, descriptions and chapters, ready to paste. Thumbnails: conf42.com/<event>/teasers#thumbnails. You upload. |

## 3. Handy things to ask

- *"Retry Emmy Eide."* / *"Redo Girish Konda with his current video."*
- *"Edits are paused - what happened?"* - Claude reads the edit report and tells you what to check in Descript.
- *"Publish the status."* - updates the Factory logs tab of this page.
- *"Proofread the transcripts of DevOps 2026."* - Claude checks the event's transcripts on the site again and fixes misheard words.
- *"Which talks still have no video, and how many days are left?"*

## 4. What Claude won't do on its own

- Download through your browser, or ask you to download - it fetches the Drive folder itself.
- Handle your Descript token or any password.
- Take over an event another computer is running - unless you tell it that computer is off.
- Upload to YouTube.

---

**Disk full?** Claude offers to clean up junk and cache files on your drive (the Trash, app and browser caches, old
installers). It shows you what they are and how big, and deletes only what you pick. Your videos and documents are never
on the list.

## Changelog

- **2026-11-19** - **Factory fast track**: `factory/fasttrack.sh <short_url> <files>` (Mac, `gh` only - no Python deps or
  secrets on the Mac) puts the files in a draft release of conf42/src plus `names.json` (GitHub dots the spaces) and
  dispatches factory cloud with `fasttrack=<tag>`. The workflow downloads the draft, `python -m factory fasttrack-in`
  uploads each file to `cloud_manual_folder` under its real name (`gdrive.Drive.upload`, resumable 64 MB pieces),
  deletes the draft, then runs the normal pass for that event (Manual upload folder claims by speaker name). Trigger
  phrase "factory fast track <event>" - manual only, Claude never starts it unasked: Claude looks on ~/Desktop itself (newest mp4/mov + pdf/pptx), renames files to
  "<Speaker> - ... .ext" so the claim is exact, never asks for paths. Test: `tests/test_fasttrack.py`.

- **2026-11-18** - `ytupload.playlist_for` prefers metadata `playlist_url` (list=); `playlist_order` runs at the end of
  every `event()` pass: `readd_plan` on the playlist items sorted by publishedAt (date added) keeps the in-order
  prefix and removes + re-adds the rest in `site_order` (Marek's workaround: add in website order, no "Manual"
  needed; 50 + 50 units a talk). `site_order` (= build/events.py + event.html: Featured, Panel, tracks by first appearance, banished last, test
  talk never). `events._row` now keeps featured/panel/track. `tests/test_playlist.py`.
  Same day: `YouTube.playlist(title, name, year)` matches exact normalized title, else the one title with conf42 +
  name + year (several -> RuntimeError, nothing made); no `playlist_url` -> `wire_site` fills metadata.yml
  (`set_playlist_url`: empty value or missing key only) and pushes with gc.auto=0.
- **2026-11-18** - `sheetcsv.py`: after `sheet_links` writes a link (real sheet only, `post is None`), the tab is
  exported (Drive token from UPLOAD_FEED, Sheets API for the gid, `docs.google.com/.../export?format=csv&gid=`), the
  email column(s) dropped in memory, and `db_path` committed + pushed. Never writes to the sheet. Guards: an email address left in
  another column, Name1/Title/YouTube missing, fewer than half the repo's rows. Byte-identical to Drive's own CSV
  (CRLF rows, no final newline); `tests/test_sheetcsv.py` checks it on the real MLOPS_2026.csv. Same day:
  `ytupload.repair` retries captions that are False or None and falls back to the shipped `srt/` transcript.
- **2026-11-16** - After the cloud factory's first outage (postmortem: `postmortems/2026-11-15-conf42-cloud-factory.md`):
  - A talk goes up to YouTube the moment it is finished. There are two passes a day now (05:30 and 22:30 UTC).
  - The same talk in several places is normal: conf42.com/record wins over the Manual upload folder, which wins over
    an event's old folder. The Manual upload folder is read by the cloud pass.
  - A talk recorded with the wrong conference picked is moved to the right event by itself when the deck and the
    speaker both say so, and gets the right overlay. One sign only: it waits, with "which conference?".
  - A video whose owner's company blocks link sharing is fetched anyway, through the upload script's Drive access.
  - Upload folders are emptied 120 days after a conference's kick-off (ours to Drive's bin, speakers' own files out of
    the folder; anything not sorted out is listed instead). Ask *"What would the clean-up do?"* for a dry run.
  - Older videos get the site's transcript as captions, 15 a pass, never more than 50 a day, and only when the day's
    talks are out of the way. Ask *"How far are the captions?"*.
  - One broken upload no longer stops a pass; the pass ends red and its summary says what broke.

- **2026-11-13** - The cloud factory also reads old link-shared upload folders: add `<short_url>: <folder link>` under
  `cloud_drive_folders` in `settings.yml` and push (MLOps 2026 is there). Ask *"Plug this Drive folder into the cloud
  factory for <event>"*. Dry run first (Actions > factory cloud > Run workflow, dry run ticked): the summary lists
  every file as TAKE or leave, with the reason. The recorder's upload wins over the old folder for the same talk.
- **2026-11-05** - Every launch writes a short entry to `_db/factory_runs/<event>/LAUNCHES.md` (machine, command,
  Drive fetch, talks processed, ship result, Descript project count). Claude reads it plus the Descript project before
  any launch. A computer picking up an event from another one skips the videos the finished talks were made from.
- **2026-10-31** - Talks dropped from the event CSV come back from its git history while their video exists
  (matching, YouTube items, transcript, deck) - the video outranks the spreadsheet; never ask for the sheet to be fixed.
- **2026-10-29** - Transcripts are proofread before they ship: glossary fixes plus Claude reading each talk in context.
  Ask *"Proofread the transcripts of Feature Flags 2026"* to redo the ones already on the site.
- **2026-10-29** - Finished talks ship by themselves: transcript and slides go to the site at the end of every run
  (a deck that comes later goes with the next run). Ask *"Ship the transcripts and slides"* to do it right away.
- **2026-10-29** - YouTube titles name the event the way earlier editions did on YouTube, in words: `Conf42 Prompt
  2026` rather than `Conf42 PE2026`.
- **2026-10-28** - Videos from conf42.com/record (fragmented MP4, which Descript's import rejects) are rewrapped into a
  plain MP4 before the upload - no re-encode, same quality and size - so they no longer fail at the upload.
- **2026-10-28** - A speaker who sends only the recorder's "safety copy" folder (a recording that never reached Stop)
  gets the parts joined into one video, which runs like any upload.
- **2026-10-27** - A new Drive link for a running event switches its folder without redoing finished talks.
- **2026-10-27** - Drive check no longer flags a talk as "newer video" when it is the very upload the talk was
  made from (a pass done in another time zone made it look newer).
- **2026-10-17** - When the disk is low, Claude offers to clean up junk and cache files and shows you what first.
- **2026-10-17** - Each event gets its own Desktop folder named after the conference (`video factory - Conf42 Prompt
  Engineering 2026`).
- **2026-10-17** - Health check before the upload: one-channel sound fixed, setup junk cut unless the speaker talks
  over it, talks with no usable sound stopped (ask Claude *"Which talks need a new video?"*).
- **2026-10-16** - Tabs renamed and reordered: **Run with Claude** (first), **No Claude, manual**, **Factory logs**.
- **2026-10-16** - First version, with the conf42-factory skill in the conf42 repo.
