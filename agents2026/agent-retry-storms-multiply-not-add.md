# In agent systems, retries multiply. Give every request a budget

Conf42 Blog, 2026-09-18, updated 2026-11-09. https://www.conf42.com/agents2026/agent-retry-storms-multiply-not-add

In short: Yamini Rathamsetty and Karthik Akula (AWS) at Conf42 AI Agents 2026: how nested retries and fan-out burn agent budgets, and the fixes.

At 2 a.m., with no customers online and every dashboard green, the bill was climbing by multiples. At Conf42 AI Agents 2026, Yamini Rathamsetty, Senior Delivery Tech Leader at AWS Professional Services, and Karthik Akula, Senior Technical Account Manager at AWS, traced that kind of overnight spend to three ordinary things combined: nested retries, agent fan-out and no per-request budget. Their fix list fits on one slide.

## Fan-out is cheap only while everything succeeds

The system in the story was a multi-agent design that worked beautifully on stage. An orchestrator split a goal into pieces for specialist agents, each called tools, and some spawned workers of their own. One request became three agents, three became nine. That parallelism is the point, but it rests on a hidden assumption: almost every call succeeds on the first try. A demo runs the happy path twice; production runs it millions of times and hits every slow, flaky dependency along the way.

Then add retries. There were three layers, each sensible on its own. The AWS SDK retries failed calls by default with backoff. The application wrapped calls in its own resilience logic. And the agent itself, when a call failed, re-reasoned with a fresh model turn and often spawned a helper. Stack those and you don't add, you multiply.

## A dependency that stayed up and still did the damage

The speakers stress that their figures are illustrative, but they are the shape of what they saw: a steady few hundred dollars a day jumping to roughly twenty times normal overnight, with a single traced request fanned out into thousands of downstream calls. The trigger was not an outage. An outage would have paged someone. It was a dependency that was slow and failing about one call in five, up enough that no alarm fired, broken enough that every agent independently decided to try harder at the same moment.

That's the part that makes this an agent problem rather than an old retry problem. In a classic system, a retry reruns a cheap code path. In an agentic system, it reruns the model's reasoning, which is the most expensive thing you do, and that reasoning can decide to create more work. Autonomy is the feature you wanted, and it is also the multiplier.

## Your error rate is hiding the failures

The storm was hard to find for two reasons. The cost was smeared across dozens of agents, each doing a small, reasonable amount of extra work, so no single one looked guilty. And retried calls eventually succeeded, so the failures sat inside the success numbers. The breakthrough was to stop counting errors and start counting volume: agent turns per request and tool calls per request. One request with thousands of calls was the fingerprint.

Akula's organisational lesson is the most quotable part: nobody did anything wrong. Three teams made three locally sensible decisions at different times, and no one owned retries end to end. The real fix is to create an owner, one budget and one witness for the whole request path.

## The playbook

- **Budget every request**: a ceiling on total agent turns, tool calls and spawns. Not a timeout, a limit on the things that cost money.
- **Cap fan-out depth centrally**: the orchestrator may spawn workers, but a worker three levels down doesn't get its own tree.
- **Fail loud**: when a request hits its budget, stop and surface it. A loud failure is a page; a silent overrun is a mystery.
- **One retry layer**: pick the SDK, the app or the agent, and turn the other two off.
- **Circuit breakers** on every external dependency, with a half-open probe before closing again.
- **Idempotency keys**, so repeated work returns the cached result instead of paying again.
- **Cost as a first-class signal**: tokens and tool calls per request emitted live next to latency and errors, one trace spanning the whole agent tree, and alerts on volume rather than failures alone.

Their summary is that agents don't fall over the way old systems do. They get quietly, enthusiastically busy all night and hand you the bill in the morning.

## Who should watch

Anyone running autonomous or multi-agent workloads in production, and anyone whose cloud bill is reviewed monthly while latency is reviewed every minute. It's a story-driven talk with no live demo, and the checklist is ready to apply.

## Related talks

- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) by Michael Levan
- [Life of a token: from agents to silicon and back](https://www.conf42.com/MLOps_2026_Alessandro_Vozza_token_silicon_agents) by Alessandro Vozza
- [From Agents to Systems: Orchestration, Recovery, and Economics](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) by Rajesh Gupta

[Watch Yamini Rathamsetty and Karthik Akula's talk](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens)

[Watch the talk on YouTube](https://youtu.be/6cfk3YbKLzE).

## Watch the talk

[The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) at Conf42 AI Agents 2026.
