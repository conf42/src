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
| Watch | *"How is it going?"* - or open http://localhost:8042 | Per talk: render, upload, Descript edit, publish, download, subtitles, chapters, loudness, QA. |
| Unmatched files | Claude asks you which speaker a file belongs to | It renames it and runs it. |
| Check | *"What needs my attention?"* | Talks with QA or health flags (loudness, too much cut, setup the speaker talks over), talks that **need a new video** (no or muted sound - not sent to Descript), failed talks, and the **no video yet** follow-up list. Watch the flagged ones. |
| New upload | *"Some speakers uploaded new versions - check the Drive again."* | Claude fetches the folder again; re-uploaded talks are done again from scratch. |
| Slides | *"Prepare the slides."* | Decks matched, converted to PDF, renamed for the site, compressed. |
| YouTube | *"Write the YouTube items."* | Titles, descriptions and chapters, ready to paste. Thumbnails: conf42.com/<event>/teasers#thumbnails. You upload. |

## 3. Handy things to ask

- *"Retry Emmy Eide."* / *"Redo Girish Konda with his current video."*
- *"Edits are paused - what happened?"* - Claude reads the edit report and tells you what to check in Descript.
- *"Publish the status."* - updates the Factory logs tab of this page.
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

- **2026-10-17** - When the disk is low, Claude offers to clean up junk and cache files and shows you what first.
- **2026-10-17** - Each event gets its own Desktop folder named after the conference (`video factory - Conf42 Prompt
  Engineering 2026`).
- **2026-10-17** - Health check before the upload: one-channel sound fixed, setup junk cut unless the speaker talks
  over it, talks with no usable sound stopped (ask Claude *"Which talks need a new video?"*).
- **2026-10-16** - Tabs renamed and reordered: **Run with Claude** (first), **No Claude, manual**, **Factory logs**.
- **2026-10-16** - First version, with the conf42-factory skill in the conf42 repo.
