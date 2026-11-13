# For AI agents, cost is the canary and evidence is the grade

Conf42 Blog, 2026-08-12. https://www.conf42.com/blog/obs2026/cost-is-the-canary-for-ai-agents

In short: Sabith K Soopy of StackGen at Conf42 Observability 2026 on spend caps, plan-gather-present traces and grading agents on evidence.

Agents rarely crash. They loop, burn tokens and write a fluent root cause analysis about the wrong service. At Conf42 Observability 2026, Sabith K Soopy, Principal Software Engineer at StackGen, shared what his team instruments on its DevOps and SRE agents, and his headline lesson came from invoices rather than white papers: watch spend first, because cost is the earliest signal that an agent has gone sideways.

## Green APM, wrong answer

The scenario is familiar to anyone who has tried an SRE agent. A 3 a.m. page, the agent reads logs, metrics and traces, and produces a confident RCA with all the right service names. Then the human on-call looks and says it is the wrong service. Nothing crashed. CPU, memory and p99 were all fine. What changed was that yesterday's run cost a few thousand tokens and today's cost three times that, and five tool calls became fifteen.

Traditional APM answers whether the service is up. Soopy's point is that agents need extra primitives to answer why the agent did that: session traces across multi-step reasoning, per-tool attribution of cost and latency, token budgets as first-class signals, and evidence checks.

## Put a hard stop in the path before you scale

Soopy describes runaway retry loops as the failure that shows up on the bill. A few hundred near-identical calls in ten minutes add up, and normal rate limits do not fire because each call looks legitimate. StackGen's answer is a set of limits: max steps, max spend per tool, a page when one run looks odd next to last week's average for that agent, and an alert on tool call count as well as dollars. A healthy run makes a handful of calls; a sick one makes dozens, each fine on its own. Ship the spend cap and the loop cap before you scale the traffic.

## Plan, gather, present

StackGen models an agent run as three chapters: plan what problem to solve, gather by calling tools, and present an answer. Most of the work and most of the trouble live in the middle. The team stitches hops with OpenTelemetry and inspects the LLM trees in Langfuse. If you only instrument the final HTTP response, he warns, you will never find where the reasoning went wrong.

The correlation details are the kind you only learn by getting them wrong. The agents are written in Go and send data to three places on purpose: the LLM trace store gets the chat and tool tree, the normal metrics stack gets budget and health counters, and logs carry the same OpenTelemetry trace ID. Use the real OpenTelemetry hex ID in logs, not your web framework's request ID, because the two look alike and break the join. Tool and agent names are fine as metric labels; a session ID in Prometheus is not. And add business labels to child spans (session, workflow, stage, agent) when you start, because retrofitting them after an incident is painful.

## Missing data is not a passing grade

The best story in the talk is a failure. The team built an agent quality scorecard that looked professional and was wrong. The formulas were fine; the population was not. Most of the spans it scored were tiny helper calls with almost no session context, and the healthy score nearly became an argument that the fleet was ready. The rule they took from it: measure telemetry quality before agent quality, and when data is incomplete, report unknown instead of a high score.

The grading itself is about evidence, not prose. In the present step the question is whether the answer cites what the gather step actually returned. Soopy notes they had seen automated graders score polished answers highly when the trace showed the tool was never called. For support, StackGen bundles a whole conversation into one debug zip (manifest with agent version, the execution DAG, the event stream) so a bad session can be replayed offline and batch-graded.

## Who should watch

Teams running LLM agents in operations, or anyone who has opened an LLM bill and winced. The talk is grounded in StackGen's own setup, with Langfuse and Grafana as the examples, but nothing depends on those tools. The two things to do next week, per Soopy: alert on sessions that cost far more than the agent's average or make far more tool calls than normal, and do not mark a run good unless the answer cites what was gathered.

[Watch Sabith K Soopy's talk](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) ([YouTube](https://youtu.be/JT9mhxn8SgY)).

## Related Conf42 talks

- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty and Karthik Akula (AWS), AI Agents 2026.
- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) by Michael Levan (Solo.io), DevOps 2026.
- [Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) by Elizabeth Fuentes Leone (AWS), AI Agents 2026.

## Watch the talk

[You Can't Debug What You Can't See: Observability for AI Agents](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) at Conf42 Observability 2026.
