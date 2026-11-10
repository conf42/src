# Record, replay, fork: debugging an agent that failed mid-run

Conf42 Blog, 2026-11-09. https://www.conf42.com/mlops2026/record-replay-fork-failed-agent-runs

In short: Reza Amini (Flashback) at Conf42 MLOps 2026 on saving agent runs as cassettes so you can rewind to the bad step and fork a fix instead of re-running.

Logs tell you an agent broke. They do not hand you the run back. At Conf42 MLOps 2026 on November 19, Reza Amini, Senior Software Engineer at Flashback, argues for a habit that will look familiar to anyone who has used HTTP test fixtures: record the full agent run as a cassette, replay it to find the bad step, then fork from that step with a fix.

## The expensive default: run it all again

Multi-step agents fail in the middle. A bad tool call, a wrong intermediate answer, a broken handoff between steps. The usual response is to re-run the whole thing and hope the failure shows up again. Reza lists what that costs: more time, more tokens, and the same live side effects again.

That last item is the one that should worry you. If step three sent an email or wrote to a database, re-running the pipeline to debug step seven sends the email again. Nobody wants to explain to a customer that they got three identical messages because someone was investigating a parsing bug.

And non-determinism makes it worse. The second run may take a different path entirely, succeed, and leave you with a bug you can no longer see.

## A cassette is a run you can hold

The proposal is simple enough to fit on a sticky note: record, replay, fork.

- **Record** the full run locally as a cassette: prompts, tool calls and their results.
- **Replay** the same steps exactly, so you can walk to the point where it went wrong.
- **Fork** from that step with a change, and check the fix before you touch production again.

If you have used VCR-style fixtures for HTTP tests, the shape will be familiar. The twist is applying it to a whole agent trajectory, where the "responses" include model outputs that you could never reproduce by calling the model again.

Reza draws a clean line between this and tracing. Traces help you observe a run. A cassette lets you reproduce it and change one decision. They sit next to each other in your toolkit, alongside logs and plain re-runs, rather than replacing anything.

## The demo: rewind, fork, recover

The talk includes a live demo of a failed multi-step agent run. Reza rewinds to the bad step, forks a fix, and shows the recovery without re-running the whole pipeline. That is the part to watch closely, because the interesting questions are in the details: what exactly gets captured, and what happens to the steps after the fork.

## Honest scope

Reza works at Flashback, and Flashback is one way to keep these cassettes. The abstract is upfront that the session teaches the habit and is not a product pitch, so expect the pattern first and the tool as one possible implementation.

## Who should watch

Engineers who own agents with side effects: anything that writes, sends, books or pays. Also anyone who has burned a pile of tokens re-running a twenty-step workflow to look at step nineteen. If your agents are read-only chatbots, the payoff is smaller, though the reproducibility argument still applies.

## Related Conf42 talks

- [Feature Flags as Incident Evidence: Safer AI-Assisted RCA Workflows](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) by Ishan Shah, on keeping AI-assisted incident analysis grounded in evidence.
- [You Can't Debug What You Can't See: Observability for AI Agents](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) by Sabith K Soopy, the tracing side Reza wants cassettes to sit next to.
- [Three Hours Debugging Code I Never Wrote](https://www.conf42.com/Observability_2026_Artemis_Leonardou_debugging_agents_codegeneration) by Artemis Leonardou, a debugging story from the agent-written-code end.

[Watch Reza Amini's talk](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Your Agent Failed Mid-Run. Logs Won't Replay It.](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) at Conf42 MLOps 2026.
