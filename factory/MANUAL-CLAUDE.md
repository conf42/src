# Conf42 talk factory - with Claude

The same job as the **Manual** tab, but you talk to Claude and it runs the factory for you: it fetches the speakers'
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
| Check | *"What needs my attention?"* | Talks with QA flags (loudness, too much cut, "check the start"), failed talks, and the **no video yet** follow-up list. Watch the flagged ones. |
| New upload | *"Some speakers uploaded new versions - check the Drive again."* | Claude fetches the folder again; re-uploaded talks are done again from scratch. |
| Slides | *"Prepare the slides."* | Decks matched, converted to PDF, renamed for the site, compressed. |
| YouTube | *"Write the YouTube items."* | Titles, descriptions and chapters, ready to paste. Thumbnails: conf42.com/<event>/teasers#thumbnails. You upload. |

## 3. Handy things to ask

- *"Retry Emmy Eide."* / *"Redo Girish Konda with his current video."*
- *"Edits are paused - what happened?"* - Claude reads the edit report and tells you what to check in Descript.
- *"Publish the status."* - updates the Factory tab of this page.
- *"Which talks still have no video, and how many days are left?"*

## 4. What Claude won't do on its own

- Download through your browser, or ask you to download - it fetches the Drive folder itself.
- Handle your Descript token or any password.
- Take over an event another computer is running - unless you tell it that computer is off.
- Upload to YouTube.

---

## Changelog

- **2026-10-16** - First version, with the conf42-factory skill in the conf42 repo.
