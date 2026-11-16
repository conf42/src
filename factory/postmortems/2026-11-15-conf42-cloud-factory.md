# Postmortem: Conf42 cloud factory, the first outage and the first full run (2026-11-14 to 16)

Status: **running again**. 16 MLOps 2026 talks went through the cloud factory and are on YouTube (15 in the first
run, plus one that had first been filed and uploaded as a Chaos Engineering talk, finding 4). One pass was still
running when this was written (Phoebe Wang and a new upload, finding 6).

All times UTC, from the GitHub Actions API, the job logs, `git log` and the state files in `_db/factory_runs/`.
Commit ids are the ones on `main` today (the branch's history was rewritten at 02:03 on Nov 16, finding 8).

## Summary

The cloud factory was switched on on Nov 13. Its next two scheduled passes (Nov 14 and 15) both died about five
minutes in, before Descript or YouTube were touched, and nobody was told. Marek noticed on Nov 15: "I can't see any
new videos, when there's many uploaded". Cause: the first upload that needed Claude's look went through
`faster-whisper`, installed unpinned, whose own file reading had broken with a new PyAV; the error was not caught and
one upload stopped the whole pass. After the fix, one pass processed everything that had piled up (6 recordings from
conf42.com/record, 10 from the old MLOps folder). The day then turned up a recording made under the wrong conference,
a talk the factory could not see at all, and several slips in how Claude worked next to running jobs.

## Timeline

| Time | What happened |
|---|---|
| Nov 13 14:13-14:31 | Last green pass before the outage (run 43440700056): the test talk, end to end. |
| Nov 14 12:23-12:33 | Scheduled pass **failed** (run 43594585843). Cron is 05:30; GitHub started it ~7 h late. |
| Nov 15 12:53-13:03 | Scheduled pass **failed** (run 43716162060), again ~7 h late. Step "Factory pass", after 5.5 min. |
| Nov 15 ~21:00 | Marek: "analyse why it's not working and let's fix it together". No `gh` here and the job logs need a login, so Claude listed the runs through the public API and reproduced locally: a dry run passed, the Claude step on one held video crashed with `open() got an unexpected keyword argument 'metadata_errors'`. |
| Nov 15 21:26 | Fix pushed (`efb395ac3e42`). Marek: "don't be silly, let me let you do it" - Claude starts passes with the stored git login from then on. |
| Nov 15 21:29 | Run 43763961948 started. 21:44 intake done (6 accepted; Claude cleared two "picture never changes" holds). 21:58 first video on YouTube. |
| Nov 15 21:36 | Marek: duplicates across folders are normal, order "automated>manual>old folder" (`ca22740a44d2`). |
| Nov 15 ~22:50 | Marek: Ajay Munjuluru recorded his MLOps talk "using the overlay from Chaos Engineering"; "Whatever he says, goes". Claude confirmed from the original file: deck page 1, the deck's file name and the greeting all say MLOps - and the proofreader had rewritten his "welcome to Conf42 MLOps" to "Conf42 Chaos Engineering 2026" (`d31553c8c40a`). |
| Nov 15 23:04 | Detection + re-filing + overlay swap pushed (`df49023efe2f`). |
| Nov 15 23:42 - Nov 16 02:11 | Marek: "proof-read all available conf42 transcripts ... with opus". 41 events, see Numbers. |
| Nov 16 00:02 | Marek: "upload videos as they are finished, rather than batched in the end" (`93eab2eaf62f`). |
| Nov 16 00:26-00:30 | Run 43763961948: all 15 MLOps talks edited, then uploaded as one batch. Green. |
| Nov 16 00:27 | 120-day clean-up pushed (`3b3089c7a186`); Marek first said 90 days, then "let's make the delete happen after 120 days". |
| Nov 16 00:34-01:12 | Run 43781166515: Ajay's upload re-filed to MLOps, overlay swapped, edited, on YouTube at 01:11. Run **red**: `KeyError: 'source'` in chaos2026 (finding 5). |
| Nov 16 01:15-01:20 | Fix `e95496592d26`; run 43785209623 green. |
| Nov 16 02:03 | `main` force-updated by someone else: history rewritten (finding 8). |
| Nov 16 ~02:05 | Captions job tested on two older videos; YouTube then answered "quota exceeded" for the day (finding 7). |
| Nov 16 02:16 | Phoebe Wang's video put into Manual upload from Marek's Desktop file; run 43791197705 started. |

## What went well

- After `efb395ac3e42` a failure stays where it happens: run 43781166515 failed in chaos2026 and still finished
  MLOps (re-file, edit, upload).
- Claude's look in the intake worked on its first cloud run: two uploads flagged "the picture never changes" were
  accepted with a reason ("slides do change, pages 02 to 17 of 18").
- The priority rule and the Manual upload folder worked on their first pass: Bhavik Thakkar's deck came from Manual
  upload, the old-folder copies were ignored, nothing was edited twice.
- The wrong-conference fix worked on its first real run, checked on YouTube itself: title, a frame with the MLOps
  overlay, and a transcript that opens "welcome to Conf42 MLOps".
- Nothing was paid twice in Descript.

## What went wrong, and why

### 1. One unclear upload stopped every pass for two days
`first_words()` handed a WAV to `faster-whisper`, which opened it with PyAV. The workflow installed `faster-whisper`
unpinned; its newest PyAV no longer accepts `metadata_errors`. The call had no `try/except`, `ask_claude` did not
catch it, and neither did the intake's loop over uploads or over events. Why it showed only on Nov 14: the Nov 13
passes had no upload that needed Claude's look (the test talk was accepted by hand), so that path had never run in
the cloud. Reproduced locally with a clean venv; fixed and re-run on the same video.

### 2. Two failed days nobody saw
A red scheduled run tells nobody (and the rule for this flow is no emails). The status pages show talks, not the
pass. Not fixed: needs Marek's choice (open action 2).

### 3. The proofreader rewrote what the speaker said
Its prompt said: this event is "X", write it like that when the speaker names it. A talk filed under the wrong event
therefore got the wrong conference written into its transcript. Prompt changed: a different conference or year the
speaker names is kept.

### 4. A talk recorded under the wrong conference went all the way to YouTube
A speaker on two lineups picked the other conference in the recorder. Nothing compared what the recording says with
where it was filed, so it was edited (one Descript edit spent), shipped to the wrong talk page and uploaded as the
wrong talk (`vaF9myP5UCQ`). Now the intake compares the deck and the greeting with each of the speaker's talks
before anything is spent, re-files on two signs, and lays the right overlay over the video.

### 5. Claude's slips next to running jobs
- **A hand reset broke a pass.** Resetting the speaker's Chaos talk in `state.json`, Claude removed its `source`
  name. `cloud.one_event` then tested `os.path.exists(os.path.join(run.inp, t.get("source") or ""))` - the input
  FOLDER - took the talk for work, and `process()` hit `KeyError`. Fixed (`isfile`), record repaired.
- **`git pull --rebase --autostash` in a folder another job was writing to** parked 41 in-progress proofread files in
  a stash whose re-apply failed. All 41 restored and checked (no conflict markers, identical to the stash).
- **Untracked copies of files already pushed** (the captions work, committed with a temporary index) made the
  proofread job's last two pushes fail. Synced by hand; nothing lost.
- **The proofread run was started without git on PATH** (PowerShell `Start-Process`): its first event was proofread
  but not committed. Committed by hand, run restarted; that event's fix count was lost (the fixes were not).
- **A local `cloud --dry-run` wrote `intake.json`** with every upload marked done; committed, it would have made the
  factory skip real uploads. Reverted before any commit; fixed (`ca3f9a80b171`).

### 6. Files a company keeps off the public link are invisible
The factory read old folders through Drive's public folder view. A file whose owner's company blocks link sharing is
not in that view, and its download asks for a sign-in: no line in the summary, no talk. Phoebe Wang (MLOps 2026) was
missed this way; Scarlett Attensil on 2026-11-03 was the same and was then solved by hand. The account that owns the
folder can list and download such files. Fixed (`d3b180f28b43`); Marek also handed over her video himself.

### 7. YouTube's daily allowance was used up, with a test
16 uploads and their captions, thumbnails and playlist entries had used most of the day; Claude's test of the new
captions job (two tracks, plus listings) took the rest at ~02:05. Until ~08:00 no upload can go through. The size of
the allowance is **not known** (the API does not tell; the Google Cloud console does). Captions for older videos now
only run when the talks' own rollout is confirmed done and it is the end of YouTube's day (`050b001817ef`).

### 8. `main` was rewritten while two jobs were pushing to it
At 02:03:27 the remote `main` was force-updated: 6 commits from 2023-24 are gone from the history and
`_db/JS_2023.csv` differs in the old commits (the unlabelled e-mail column). The tree at the tip is identical, and
no commit of this session is missing (subjects compared one by one). Who did it is not known from here. Effects:
every commit id quoted before 02:03 is a different id now; the Actions runs point at ids that are no longer on
`main`. Nothing to fix in the factory; noted so nobody looks for the old ids.

### 9. The schedule runs ~7 hours late
Both scheduled passes started ~7 h after their cron time. Cause on GitHub's side, not known. A second schedule was
added so that one pass a day lands in the captions window either way (`ca3f9a80b171`).

## The same bug elsewhere

- Unpinned installs in the cloud workflow: `faster-whisper` (now pinned to 1.2.1) and `npm install -g
  @anthropic-ai/claude-code` (still unpinned - open action 6). `requirements.txt` itself is unpinned (requests,
  pyyaml, pypdf, pillow, psutil): listed, not changed.
- `os.path.exists(os.path.join(<folder>, x or ""))`: grepped `factory/factory/*.py`, the one in `cloud.one_event`
  was the only one.
- Uncaught errors that stop a whole pass: the intake's per-upload and per-event loops and `cloud.main`'s per-event
  loop now catch, log, and carry on; the pass ends red.

## Actions

### Done now (each tested; `tests/test_intake.py`, `test_legacy.py`, `test_sources.py`, `test_cleanup.py`, `smoke.py --no-whisper` pass)

| Commit | What | Finding |
|---|---|---|
| `efb395ac3e42` | First words read from ffmpeg's WAV (no PyAV); Claude trouble = hold; one upload or event that breaks never stops the others | 1 |
| `ca22740a44d2` | conf42.com/record > Manual upload > old folder; the Manual upload folder is read by the cloud pass | Marek's rule |
| `d31553c8c40a` | Proofread: what the speaker says, goes | 3 |
| `df49023efe2f` | Wrong conference: detection in the intake, re-filing, overlay swap (`python -m factory overlay`) | 4 |
| `93eab2eaf62f` | A talk goes up to YouTube the moment it is finished | Marek's rule |
| `3b3089c7a186` | Upload folders emptied 120 days after the kick-off, with guardrails | Marek's rule |
| `e95496592d26` | A talk with no source file is not work; the overlay swap is written into the intake record | 5 |
| `87445230758e` `98edd7d752df` `050b001817ef` | Captions on older videos: 15 a pass, never more than 50 a day, only when the rollout is clear and at the end of YouTube's day | 7, Marek's rules |
| `d3b180f28b43` | Files off the public link come through the upload script's access | 6 |
| `ca3f9a80b171` | Second pass a day (22:30), `faster-whisper==1.2.1`, a dry run writes nothing | 1, 5, 9 |

### Open

| # | Action | Owner | Finding |
|---|---|---|---|
| 1 | Delete the wrong video `vaF9myP5UCQ` in YouTube Studio (the factory never deletes) | Marek | 4 |
| 2 | Decide how a failed pass should be seen. Proposal: "last pass failed" + the reason on conf42.com/factory, no email | Marek | 2 |
| 3 | Re-file automatically on two signs (built) or always hold for a look? | Marek | 4 |
| 4 | Phoebe Wang's deck is in the old folder as `Conf42 MLOps 2026 - Build ML Workflows with Codex, Flyte, and MCP (1).pdf`: it names no speaker, so it is not taken. Rename it with her name, or say so and Claude files it | Marek | 6 |
| 5 | Look up the YouTube API allowance of the "Conf42 factory" project in the Google Cloud console, so the factory can be told how many uploads a day fit | Marek | 7 |
| 6 | Pin the Claude Code CLI version in the workflow, after checking which flags the factory uses still work | Claude | 1 |
| 7 | The recorder asks "which talk are you recording?" when a speaker is on two lineups (prevention, before the intake has to catch it) | Claude | 4 |
| 8 | `_db/factory_runs/ledger.json` has no entry since 2026-10-14 although the cloud passes paid for edits: find out whether the cloud is meant to write it (a credit guard reads it) | Claude | - |
| 9 | Watch the first real captions batch, and the first 120-day clean-up (MLOps 2026: 2027-03-19) | Claude | 7 |
| 10 | Three videos to look at: Deborah Adedigba and Reza Amini ("picture changes at 0:00 / 0:10 - setup screen?"), Jose Manuel Ortega (distorted sound, 3.1 % clipping) | Marek | - |

## Numbers

- Outage: 2 scheduled passes lost (Nov 14, Nov 15); uploads waited up to ~2.5 days (first one Nov 13 16:45).
- Run 43763961948: 3 h 01 min, 16 talks (1 Chaos Engineering, 15 MLOps), 16 YouTube uploads, 0 errors.
- Descript, MLOps 2026 project: 177.7 credits for 17 edits (state.json, incl. the test talk and the re-filed talk),
  plus ~5.8 per talk for chapters. One edit (the wrongly filed talk, in the Chaos project) was spent for nothing.
- Transcripts proofread with Opus: 41 events, ~40,300 fixes in 1,563 of 1,624 transcripts (one event's count lost),
  0 failed files, ~2.5 h, about $186 of notional usage on the subscription.
- Captions for older videos: 1,633 videos found by the dry run, 2 done.

## Lessons folded in

- `factory/MANUAL-CLAUDE.md` changelog (what changed for the person asking) and `factory/README.md` ("Learned from
  a real day").
- Claude's notes: start passes and read job logs with the stored git login; never `pull --autostash` or leave
  untracked copies of pushed files in a folder another job writes to (commit with a temporary index instead); keep a
  `source` name when resetting a talk by hand; write patch scripts as files, not shell heredocs (backslashes are
  halved on the way).
