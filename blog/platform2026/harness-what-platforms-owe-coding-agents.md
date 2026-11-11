# What an engineering platform owes its AI agents

Conf42 Blog, 2026-11-05, updated 2026-11-09. https://www.conf42.com/blog/platform2026/harness-what-platforms-owe-coding-agents

In short: Jimmy Caputo of Harness at Conf42 Platform Engineering 2026 on the context layer, tools, guardrails and observability agents need to ship safely.

Most delivery platforms quietly assume a human is in the loop: someone who knows which test failures are noise, which directory not to touch, and when a deploy looks off. At Conf42 Platform Engineering 2026, Jimmy Caputo, Senior Director of Product Management at Harness, asked what happens to those assumptions once agents write the code, run the tests and open the pull requests. His answer is a platform that hands agents four things: context, tools, guardrails and observability.

It's a compact, opinionated talk from a vendor, and it says so near the end, when Jimmy maps the ideas onto Harness. The first four-fifths stand on their own as a design checklist for any platform team.

## The tribal knowledge has to move out of people's heads

Jimmy's starting point is scale. One agent per developer is manageable. Fleets of agents running in their own sandboxes, around the clock, turn code review into the bottleneck and make relying on someone to notice an unreliable control. Mistakes have to be caught and remediated automatically.

The first thing agents lack is context. Ownership (who to ask, who approves), architecture and dependencies beyond the current repo, coding standards and the definition of done, what is deployed where, whether an incident is in progress, which past changes caused trouble, and the actual intent of the task. If a human developer would have to gather that from ten systems or ten people, an agent won't reconstruct it reliably.

## One context layer beats ten lookups per task

The sharpest argument is about cost. Without a single layer that brokers all this information, every agent session rebuilds the map from scratch: query the observability tool, work out what a service is called there, map it to the repo and the pipeline. It might manage, but it burns tokens and time on every start.

Jimmy's alternative is a platform that syncs with source systems in near real time, builds a knowledge graph of the system and the organisation once, and gives agents that graph as their primary context, with permission to go to the source system when something is missing or stale.

## Agents shouldn't invent the SDLC on every task

The second pillar is tools that cover the whole life cycle, from reading and editing code to building, testing, deploying and checking health. The point isn't more tools; it's fewer, higher-level ones. If an agent stitches its own path from commit to production each time, steps get skipped or reordered, work gets duplicated, and occasionally something reaches production through a path nobody designed.

His fix is deterministic pipelines on an orchestration platform that agents call, so repeatability comes from the pipeline, not from the agent remembering the process.

## Policy in one place, not in a thousand repos

The third pillar is guardrails: scoped access to data and tools, limits on what an agent may change on its own, and human approval where it matters. Jimmy's warning is about sprawl. You can encode rules as skills and conventions per repo or per IDE, but in a large organisation that becomes hundreds of copies of the same policy, some stale, some missing, with no way for the platform team to see what is enforced where. A central policy engine that every agent and tool connects to lets you define rules once.

## Observability closes the loop

The fourth piece is observability that is designed in rather than bolted on: what the agent did, what it changed, why, and what happened next, including rollbacks and outages. Those signals should feed back into the other three pillars. Did the agent fail for lack of context, lack of a tool to check its work, or a missing guardrail that should have forced a human approval?

He adds a practical list for anything agents call: consistent APIs or MCP tools, actionable errors, machine-readable docs, published rate limits so agents back off instead of guessing, safe retries, and clear versioning and deprecation notices. None of it is exotic. All of it is the difference between an agent that recovers on its own and one that hammers an endpoint.

## Autonomy is a dial

Jimmy's closing advice is the most reusable part: treat autonomy as a spectrum from suggestions to agents acting within guardrails, start at the level you are comfortable with, and pick one workflow or repository as the test bed. Build the context layer, tools and guardrails there, watch the outcomes, fill the gaps, then expand to other teams.

## Who should watch

Platform teams being asked to support agents without a clear brief, and engineering leaders deciding how much autonomy to grant. If you want benchmarks or a live demo, this isn't it; it's a concise architecture talk with a product section at the end.

Related talks from other Conf42 events take the guardrail theme further: [Gate the Action, Not the Alert](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou at DevSecOps 2026, [Your Agent Is Confidently Wrong](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda at Feature Flags 2026, and [I Don't Trust AI Agents (And Neither Should You)](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis at AI Agents 2026.

[Watch Jimmy Caputo's talk](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

## From Harness

In the talk, Jimmy describes how Harness covers these pillars: a knowledge graph built from first-party data (the code Harness manages and the build and deployment pipelines that run on it) plus connections to third-party systems; an orchestration engine whose pipelines agents can execute, with optional human approval steps or agent steps inside them; a policy engine that lets central teams restrict what developer teams can do; and observability over what the system is orchestrating. The platform lets each team choose how much autonomy agents get.

- Harness: [harness.io](https://www.harness.io/)
- Harness documentation: [developer.harness.io](https://developer.harness.io/)

[Watch the talk on YouTube](https://youtu.be/Wmfh0QdAvyM).

## Watch the talk

[Agentic Engineering Platforms](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) at Conf42 Platform Engineering 2026.
