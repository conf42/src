# A plan span catches the agent that got the right answer by luck

Conf42 Blog, 2026-10-21, updated 2026-11-09. https://www.conf42.com/prompt2026/agent-plan-span-catches-lucky-answers

In short: Krishna Chaitanya Balusu (Meta) at Conf42 Prompt Engineering 2026 on OpenTelemetry plan spans for debugging agent prompts, not just answers.

The run that worries Krishna Chaitanya Balusu most is the one where the agent's answer is right and its plan is wrong. At Conf42 Prompt Engineering 2026, Krishna, a Senior Software Engineer at Meta who builds AI agents for incident response, showed how to record an agent's plan as an OpenTelemetry span and check it next to the answer, so a lucky shortcut fails the build before it fails a user.

He has standing to say it: he contributed the plan operation to the OpenTelemetry GenAI semantic conventions, and he built AgentTelemetry, a benchmark for finding faults in agent traces published at ACM AIware.

## Agents break the prompt feedback loop

With a single-turn prompt you change the wording, read the output and judge it, ten rounds in a few minutes. An agent plans, calls tools and then answers, and you still only see the answer. You can't see which tools it chose or which step it skipped, so you tweak the prompt and hope. In the title's words, you cannot fix a prompt you cannot see fail.

## The release helper with two plans

His running example is small enough to hold in your head. A release helper answers "is this release ready to ship?" with three tools: read summary (yesterday's summary, fast but stale), read manifest (today's required checks) and read checks (today's results). Ready if every required check passes, blocked if one fails, unknown if the evidence is missing.

Plan A reads the summary and says ready. Plan B reads the manifest, then the checks, and says ready. Today both pass the answer check. Tomorrow a security check fails: plan B says blocked, plan A still says ready, because it never looked.

## Record the plan, then test it

A plan span records the operation name (plan), the agent's name and the plan itself; in the demo the plan is a list of the tools the agent decided to call. Each tool call then gets its own execute-tool span. He keeps the payload tiny (no full prompts, no long reasoning) and is clear about what it is: the plan your app got back from the model, not a window into the model's mind. The conventions are still marked development, so pin the version.

Once the plan is recorded, checking it is a normal test: does the plan include the manifest and the checks, in that order? Pass or fail. No plan span at all is unknown, never pass.

Why a shared name matters: every framework logs planning its own way, if at all. In his benchmark, standard OpenTelemetry plus the GenAI conventions caught 6 of 14 fault types, and planning failure was among the missed ones because there was nothing to look at. With agent-specific spans including planning, the reference setup caught all 14. He flags that it's a controlled benchmark.

## The demo, in Jaeger

The demo runs the helper five times with scripted plans, real OpenTelemetry spans sent to Jaeger, and no model calls, so it runs on a laptop without an API key. One table, four checks per run: answer, plan, tools, and whether today's evidence was read. The answer-passes row shows the trap: the answer is correct, but the plan span lists only the summary tool.

The other rows separate failures that look the same from outside. A tool timeout has a good plan, an error on the tool span and the honest answer unknown, so you fix the tool, not the prompt. A missing plan span means fixing instrumentation before drawing conclusions. The stale-summary day is when the shortcut finally bites, and the plan check had already flagged that workflow on the good day.

## Turning the trace into a better prompt

The fix maps straight to the trace. Version one only asked the agent to check release readiness and return ready or blocked. It named no source of evidence, so reading the old summary was a fair way to obey it. Version two names the current release manifest, asks for every required check, and says what to return when evidence is missing. Then treat it as an experiment: same model, tools and cases; many runs, since models are random; score plan and answer separately; and keep every failure as a permanent test case.

## Who should watch

Anyone iterating on prompts for agents with a real planning or routing step, and observability folks wondering what GenAI semantic conventions buy them. It's tightly scoped and demo-driven: the plan is scripted, so how often a real model plans correctly is the measurement he leaves to you.

## Related Conf42 talks

- [Make Agents Observable: Tracing Decisions, Tool Calls and Recovery](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) by Emerson Braun (Plan A Technologies) at Conf42 Observability 2026.
- [From Agent Trace to Reproducible Regression Test](https://www.conf42.com/MLOps_2026_Raju_Dandigam_trace_regression_agent) by Raju Dandigam (Navan) at Conf42 MLOps 2026.
- [You Can't Debug What You Can't See: Observability for AI Agents](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) by Sabith K Soopy (Stackgen) at Conf42 Observability 2026.

[Watch Krishna Chaitanya Balusu's talk](https://www.conf42.com/Prompt_Engineering_2026_Krishna_Chaitanya_Balusu_debugging_plan_fail) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/9oRkB-3XWNc).

## Watch the talk

[You Cannot Fix a Prompt You Cannot See Fail: Debugging the Plan, Not Just the Answer](https://www.conf42.com/Prompt_Engineering_2026_Krishna_Chaitanya_Balusu_debugging_plan_fail) at Conf42 Prompt Engineering 2026.
