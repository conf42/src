# Your Agent Failed Mid-Run. Logs Won't Replay It.

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Reza Amini](https://www.conf42.com/speaker_Reza_Amini) (Founder @ Flashback). Page: https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs

## Abstract

In production, a multi-step agent can fail mid-run: a bad tool call, a wrong intermediate answer, a broken handoff. Logs usually confirm that something broke. They rarely give you the run back so you can inspect the exact step and try another path. The usual next move is to re-run everything: more time, more tokens, and the same live side effects again.  This talk is about a practical habit for that failure mode: record → replay → fork. Save the full agent run as a local cassette (e.g. prompts, tool calls, and results). Replay the same steps to find where it went wrong. Fork from that step with a fix, and check it before you re-run in production.  Demo: a failed multi-step agent run. We rewind to the bad step, fork a fix, and show recovery without re-running the whole pipeline. Traces help you observe; a cassette lets you reproduce the run and change one decision. Flashback is one way to keep those cassettes. The talk teaches the habit, not a product pitch.  You leave with: how to treat a failed agent run like a replayable artifact next to logs, traces, and re-runs.
