# Postmortem: Conf42 Platform Engineering 2026, talk factory (2026-11-03)

Status: **finished**. All 24 talks were done at 00:58 on 2026-11-04. Transcripts and decks were shipped by hand at ~09:00 (finding 7).

## Summary

24 videos + 23 decks for `platform2026` from the speakers' Drive folder. 2 talks finished in the first 20 minutes,
then the run stood still for ~2.7 hours: a false-alarm credit guard paused every edit, and nobody was told. Separately,
one talk's upload was rejected six times by Descript because of a period in the speaker's name, one talk's render
failed on a Windows file lock, and one video didn't match its speaker. All four have a tested fix.

## Timeline (log times from state.json, local time)

| Time | What happened |
|---|---|
| ~19:55 | Marek: "activate conf42 talk factory for Conf42 Platform Engineering" + the Drive folder link. |
| ~19:58 | Claude followed the talk-factory skill: Chrome download. The Chrome extension wasn't connected. |
| ~20:00 | Marek: "reconnect as necessary, use the drive mcp". The Drive connector can list but not carry 20 GB, so Claude downloaded with curl from `drive.usercontent.google.com` (the same thing `factory drive` does: the README says so, the skill didn't). |
| ~20:03 | Scarlett Attensil's video + deck came back as Google's sign-in page (her company blocks link sharing). Marek downloaded them by hand. |
| 20:07:52 | Run started detached: 23 matched, "Lucas Mazei.mp4" unmatched (CSV: Lucas Mateus Mazei Sobrinho, 58%). Claude renamed it and queued a follow-up run. |
| 20:26:44 | **EDITS PAUSED**: Attila Toth's edit report "mentions Amith Reddy Ravuru". The sentence was *"I didn't open, edit, or apply settings to the other composition in the project, 'Amith Reddy Ravuru'."* Amith had finished at 20:15 for 7.7 credits. |
| 20:29-20:52 | Every other talk failed at "edits paused" after its upload. |
| 20:42-20:47 | Scarlett's render failed 3x: `[WinError 5] Access is denied: state.json.tmp -> state.json`. |
| 20:49-21:09 | Sumeet L. Ram's upload rejected 6x: "Uploaded file has invalid or unsupported media content". |
| 20:55 / 21:09 | First run, then the follow-up run, finished with everything else failed on the pause. |
| ~23:05 | Marek: "are we doing?". Claude found the pause, confirmed from the report that it was a denial, cleared it (`unpause`), and restarted (23:09:51). |
| ~23:20 | Marek: "take notes of these problems, and fix of course". |
| 00:58:52 | 24/24 done. `shipping transcripts / slides failed: [WinError 2] The system cannot find the file specified`. |
| next morning | Marek: "The transcripts and slides are uploaded?" No: 24 transcripts and 2 decks were in the repos but uncommitted. Claude fixed `ship` and shipped them (src 99d9ea6, static 1217f01 + 5430b2d). |

## What went well

- Uploads, renders and the first two edits were quick: 22 talks uploaded in ~45 minutes.
- The credit guards did their job conservatively: nothing was paid twice, and nothing was edited by mistake.
- The matcher never guessed (the Lucas file waited for a human, as designed).
- Downloading straight from Drive with no browser worked for 45 of 47 files, with every size checked.

## What went wrong, and why

### 1. A denial paused the whole run (~2.7 h lost)
- Why paused? The stray-edit guard looked for any other talk's name in the edit report.
- Why did the name appear? The AI editor now reports what it *didn't* touch ("I didn't open … 'Amith Reddy Ravuru'").
- Why was the guard text-only? It had no way to check Descript itself.
- Why was it 2.7 h and not minutes? A pause only shows on the dashboard. Nothing reaches Marek or Claude, and Claude's
  watcher only waited for the process to end.
- **Fixed:** names in denial sentences are ignored (`strayed_mentions`), and a real check was added: the other
  *already-edited* compositions' lengths are compared before and after each edit (`edited_lengths` /
  `changed_lengths`). Tested on today's report plus stray-edit cases that must still pause.
- **Open:** an alert when a run pauses or stops (see actions).

### 2. Descript rejected "Sumeet L. Ram" six times
- The upload's media name was the bare speaker name, with no extension. Descript takes the type from the text after the
  last dot, so it read " Ram".
- Evidence: the source and the rendered file are both clean (full GPU decode, no errors, same metadata as accepted talks,
  and Egor/Vincenzo at 59.94 fps uploaded fine). The *same file* uploaded as "Sumeet L. Ram (fixed).mp4" was accepted at
  the first try (composition 3148376b…).
- **Fixed:** the media name always carries the real extension (`descript.import_file`). The edit guard's media lookup
  (`media_files[key]`) also accepts `key.mp4` / `key (…)`, so the "already shorter than its media" guard keeps working.
- Side effect: 6 empty "Sumeet L. Ram" compositions in the Descript project (the reuse guard skips them: they're < MIN_TALK_SECONDS).

### 3. Windows file lock on state.json
- `os.replace(state.json.tmp, state.json)` fails while another process has state.json open (the dashboard polls it,
  and so do status checks). Reproduced: holding the file open → WinError 5.
- **Fixed:** `write_json` retries the swap for ~10 s. Both state saves use it. Same pattern looked for elsewhere: the
  other `os.replace` calls write new media files that nothing polls (media.py, drive.py, slides.py, proofread.py,
  machine.py). Left as they are and listed here. `ledger.json` is written in place, without a swap.

### 4. "Lucas Mazei" didn't match "Lucas Mateus Mazei Sobrinho"
- The rules covered a longer file name than the CSV name (first + last), not a shorter one.
- **Fixed:** a new rule applies only after every older rule fails: all words (2+) of the file name are in exactly one
  speaker's name. All 47 of today's files now match by themselves. A smoke test was added.

### 5. The skill sent Claude to Chrome
- The talk-factory skill still described the Chrome download. The README already said "Never download through a
  browser" and pointed to `python -m factory drive`.
- **Fixed:** the skill now starts with `drive`. It also has the new event folder path (`Desktop\video factory - <title>`),
  the ledger path and `parallel_talks: 2`.

### 6. Restricted files inside a shared folder
- Drive returns its sign-in page with HTTP 200, and `drive.head` reported size 0, so a download would have saved
  HTML as the video. That is exactly what a plain curl did today.
- **Fixed:** `drive.head` raises `NeedsSignIn` (sign-in redirect or text/html). `drive_fetch` already logs and skips it.

### 7. Transcripts never reached the site
- At 20:55 the first run's `ship` copied files into `src/srt` / `static/slides`, then failed before its commit (the
  WinError 2 above, same message at 00:58). Every later `ship` saw identical files already in place and skipped them
  ("only new or changed"), so they stayed uncommitted forever. A rerun of `ship` returned `srt: []`.
- **Fixed:** `ship` also ships target files that `git status` reports as untracked or changed. Proven live: 24
  transcripts + 2 decks shipped. A failed ship now logs its traceback.
- **Root cause of the WinError 2: not found.** It couldn't be reproduced by hand: `ship` ran clean, git is on the
  detached process's PATH (the same run pushed the status page), and all 24 proofreads finished. Leading suspect: a
  subprocess in `ship` or `proofread_finished` started from the hidden detached process. The traceback will show it
  next time.

## Numbers

- Files: 24 videos (19.9 GB with the decks), 23 decks; 14 talks with no video yet.
- Output: 24 MP4s (`final videos for YouTube`), 24 SRTs, 23 decks. Loudness -14.6 to -14.0 LUFS.
- Minutes: 557.5 -> 526.1 (31.4 min cut, 5.6%).
- Credits: 247.3 AI credits for 24 edits (~10.3 per talk, in line with the skill's estimate). Attila's 19.3 was the
  highest.
- QA flags (check the start/end by eye): Denis Galkin, Scarlett Attensil, Lucas Mateus Mazei Sobrinho (picture
  changes in the first seconds); Sergey Pronin 64 s, Vincenzo Santonastaso 76 s, Sumeet L. Ram 16 s of setup screen at
  the start, and Madhu Chenna 20 s at the end, all with the speaker talking (not cut).
- Time lost: ~2 h 43 min of a stopped factory (20:26 → 23:09); 6 wasted upload attempts (~20 min).

## Actions

### Done now (tested; `tests/smoke.py`: ALL PASSED)
| Fix | Finding |
|---|---|
| Edit guard ignores denials + checks composition lengths in Descript | 1 |
| Media name with extension; media lookup accepts it | 2 |
| `write_json` retries the state swap | 3 |
| Short-name match rule + smoke test | 4 |
| `ship` picks up identical-but-uncommitted files; logs the traceback | 7 |
| Skill: `drive` first, current paths | 5 |
| `drive.head` detects the sign-in page | 6 |
| README: lessons in "Getting the files from Drive" and "Rate limits and credits" | all |

### Open
| Action | Owner | Finding |
|---|---|---|
| Alert when a run pauses or stops with talks left (Windows toast / email to Marek / Claude PushNotification), not only the dashboard. Proposal: a `notify` hook on `edits_paused` and on "run finished" with failures. | Claude (needs Marek's OK on the channel) | 1 |
| Claude's watcher during a run: poll `status` every ~15 min and react to `edits_paused` / failed talks, instead of waiting for the process to exit | Claude | 1 |
| Delete the 6 empty "Sumeet L. Ram" compositions in the Descript project (cosmetic) | Marek | 2 |
| Leftover `mp4/Scarlett Attensil.mp4.2552.part.mp4` from a render that died with the first run: clean `*.part*` on run start | Claude | 3 |
| Chase the 14 talks with no video | event team | - |
| Find the WinError 2 in `ship` from the new traceback on the next run | Claude | 7 |
| "the chapters job reported a change to the project" (Attila, Denis): check what changed. The final files can't be affected (chapters run after the download). It may be the same denial-text issue as finding 1 | Claude | 1 |
