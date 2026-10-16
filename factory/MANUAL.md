# Conf42 talk factory - team manual

Turns the talk videos speakers upload for a Conf42 event into finished, YouTube-ready files: it matches each video to
its talk, has Descript clean it up, and hands you an MP4, subtitles and the YouTube title, description and chapters.
It also prepares the slide decks for the site.

```
speakers' Drive folder  →  match to the talks  →  Descript (Studio Sound, fillers, pauses)  →  MP4 + subtitles  →  loudness + QA  →  YouTube
```

The live status of every event is at the top of this page. The technical details live in `factory/README.md` in the
conf42 repo. When the tool changes, this manual changes with it - see **Changelog** at the bottom.

---

## 1. One-time setup on your computer

You need: a Windows PC, a Mac or Linux, about **50 GB free** for an event, Git, and Python 3.9 or newer (the setup
installs the rest: ffmpeg and LibreOffice).

1. **Get the repo** - a slim copy is enough (a few MB instead of 12 GB):

    ```
    git clone --depth 1 --filter=blob:none --sparse https://github.com/conf42/src
    cd src
    git sparse-checkout set factory _db
    ```

2. **Run the setup**, once:

    - **Windows:** double-click `factory\setup.cmd`
    - **Mac / Linux:** `bash factory/setup.sh`

    It asks for a name for your computer and a **Descript API token**: in Descript go to **Settings → API tokens →
    Create** (the team's Descript account). The token stays on your computer, never in git. It puts a
    **Conf42 factory** launcher on your Desktop, checks the machine and opens the app.

3. To push the status page and claim events (so two people never process the same one), you need to be signed in to
    GitHub on that computer (`gh auth login`). Without it everything works, but only on your machine.

**Start the app:** double-click **Conf42 factory** on your Desktop. It opens http://localhost:8042.

Health check any time: `python -m factory doctor` from the `factory` folder (with the repo's `env`).

---

## 2. Process an event, step by step

Each event has a short name - its `short_url`, e.g. `devsecops2026` or `featureflags2026` (the end of its conf42.com
address).

### Step 1 - Get the videos

Speakers upload their videos (and decks) to the event's Google Drive folder, shared as "anyone with the link".
Copy that folder's link, then from the `factory` folder:

```
../env/bin/python -m factory drive featureflags2026 https://drive.google.com/drive/folders/<folder id>
```

(Windows: `..\env\Scripts\python`.)

The factory lists the folder, downloads only what is new or changed, matches every video to its talk and starts the
whole run. The link is remembered: next time just `... factory drive featureflags2026`.

No Drive link? Download the folder as zip(s) and use the app (step 2) or
`python -m factory run featureflags2026 C:\Users\you\Downloads\drive-download-*.zip`.

### Step 2 - Watch it run

In the app, pick the event. You see:

- every talk with its steps - **render → upload → edit → publish → download → srt → chapters → loudness → QA** - and
    what it is doing right now ("uploading 45% of 1.2 GB", "Descript is busy, waiting in line");

- **NOT MATCHED** files - videos whose name matches no speaker. Rename the file to the speaker's name as on the site
    and run again;

- **No video yet** - talks with nothing uploaded. Normal for a remote conference; chase those speakers.

You can close the app - the run continues in the background. **Start / resume** in the app (re)starts the run; finished steps
are never redone.

What Descript does to every talk: **Studio Sound 80%**, limiter, volume, filler words removed, pauses over 2 s
shortened to 1 s. Then the factory sets YouTube's loudness and trims the video to the first and last word.

### Step 3 - Check the results

When a talk shows **QA** done, look at its flags:

- **loudness off** or **the edit removed more than 25%** - watch it;
- **picture changes in the first 12 seconds - check the start** - often the speaker's OBS or desktop before the
    slides. It is never cut automatically: trim it by hand if needed.

The finished videos are in `Desktop/talk-factory/final videos for YouTube/`, named
`<speakers> - Conf42 <Event> <Year>.mp4`. Subtitles are in the event folder's `srt/`.

### Step 4 - Slides

Decks from the Drive folder are matched to the talks like the videos, converted to PDF, renamed for the site and
compressed under 5 MB. They are in the event folder's `slides/`. Only decks: `python -m factory slides <short_url>`.

### Step 5 - YouTube

The app's **YouTube items** button (or `python -m factory chapters <short_url>`) writes `YouTube items.txt` in the
event folder: per talk the **title** (`<short title> | <speakers> | Conf42 <CODE><YEAR>`, at most 100 characters) and
the **description** (abstract link, event, CFP, Discord, chapters). The thumbnails are on the event's teasers page:
`conf42.com/<event>/teasers#thumbnails`.

### Step 6 - A speaker uploads a new version

Run `drive <short_url>` again: a video uploaded after its talk was finished is flagged **newer video on Drive - redo**,
downloaded, and the talk is done again from scratch. The old finished video moves to `out/replaced/` (kept).
Redo one talk with the video it has: `python -m factory redo <short_url> "<speaker>"`.

### Step 7 - Share progress

**Publish to conf42.com/factory** in the app updates the table at the top of this page (it also happens by itself every 20 minutes
during a run).

---

## 3. When something goes wrong

| What you see | What to do |
|---|---|
| A talk **failed** | Press **Retry** (it was already retried 3 times automatically). |
| **Not started: this event is running on another computer** | Someone else is processing it. If that computer is really off, Shift + click **Start / resume** to take over. |
| **EDITS PAUSED** | An edit cost unusually many credits, or its report mentioned other talks. Check the talk in Descript; if it's fine: `python -m factory unpause <short_url>`, then **Start / resume**. |
| Descript says **402** | Out of Descript credits or media minutes. Top up, then **Start / resume** - nothing is paid twice. |
| **NOT MATCHED** video | Rename it to the speaker's name as on the site (`Name1` or `Name1 & Name2`), run again. |
| Descript seems stuck ("waiting in line") | Descript runs one job per project at a time - talks take turns. A job left over from a stopped run is cancelled at the next **Start / resume**. |
| The app doesn't open | Double-click the launcher again; then `python -m factory doctor`. |

**One computer per event** - the factory claims each event so a second computer refuses to start it.

---

## 4. Where things are

`Desktop/talk-factory/<short_url>/` on the computer that runs the event:

| Folder / file | What's in it |
|---|---|
| `in/` | the speakers' videos, renamed to the speakers |
| `out/_descript/` | Descript's downloads (not for YouTube) |
| `srt/` | subtitles, named for the site |
| `slides/` | decks ready for the site |
| `YouTube items.txt` | titles, descriptions, chapters |
| `state.json` | progress of every step |

Finished videos of every event: `Desktop/talk-factory/final videos for YouTube/`.

---

## Changelog

- **2026-10-16** - First version of this manual. `unpause` command added for paused edits.
