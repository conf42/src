# Uber's driver onboarding team let agents build test accounts

Conf42 Blog, 2026-09-04, updated 2026-11-09. https://www.conf42.com/blog/agents2026/uber-test-account-agent-onboarding

In short: Kemet Dugue of Uber at Conf42 AI Agents 2026 shows the skills and the test-account agent that took onboarding setup from minutes to under 30 seconds.

Testing a driver onboarding feature at Uber means getting an account into one exact state out of more than 50,000 possible ones. At Conf42 AI Agents 2026, Kemet Dugue, software engineer on Uber's Driver Onboarding team, walked through how the team swapped run books and manual API calls for an agent that does it from a sentence, plus four smaller agent skills that removed everyday friction first.

The useful part of the talk is the order of operations: fix your own developer pain points with small, deterministic skills, then build the bigger agent on a platform that already exists.

## Why onboarding is a hard testing problem

Kemet calls driver onboarding the regulatory gateway to Uber's marketplace. Before anyone earns, they pass compliance and screening (criminal and motor vehicle checks with outside vendors), lifecycle tracking before and after activation, multi-channel onboarding for rideshare, couriers, fleets and rentals across thousands of jurisdictions, and document verification for licences, registrations and inspections. Fifteen-plus background check error states and dozens of document rejection reasons multiply into that state space.

## Four small skills before the big agent

The team first pointed agents at their own workflow:

- **Worktree skill.** Coding agents bottlenecked on one branch in one directory. Stashing Agent A's work so Agent B can make an urgent metadata fix forces language servers to re-index and the agent to rebuild context. A skill built on Git worktrees gives each agent its own directory, so both run in parallel.
- **Branch-to-diff skill.** Uber's pull requests ("diffs") have rigid CI templates demanding test evidence, linked tickets and template-aligned summaries. Generic LLM drafts were verbose and failed formatting checks. The skill inspects the Git changes, pulls context from Jira, checks local unit test coverage and formats the summary so it passes CI the first time.
- **EngiWiki sync.** Agents are only as good as the context they retrieve, and the repo had testing docs from 2023 that no longer matched reality. A sync skill keeps the internal EngiWiki aligned with the code as it changes.
- **Jira lifecycle rule.** Ticket transitions through the Jira REST API, such as moving a ticket to In Review when a diff is generated, plus fetching related historical tickets for context.

None of these is glamorous. All of them are the sort of thing that quietly costs a team hours each week, which is the point.

## The platform underneath

Kemet gives a quick tour of Uber's internal AI stack. At the bottom, an AI platform on Michelangelo, Uber's ML platform, with a model gateway, runtime SDKs and an agent registry. Above it, context engineering: code context infrastructure, memory hierarchies and an MCP gateway. Then industry and custom agents, from Claude Code to internal SDLC agents for test generation and code review. At the top, engineering enablement for cost, token telemetry and adoption.

Two pieces matter for the case study. The Agent Builder is a no-code web workspace where engineers and domain specialists configure agents in plain text, with MCP tools built in and handoffs between sub-agents. The MCP gateway exposes internal RPCs as standard MCP tool schemas, so agents query schemas at runtime and API changes don't require prompt rewrites, with observability and audit trails included.

## The test account agent

Previously, one test account took a multi-page run book and manual calls across several tools: five to ten minutes at minimum. The agent splits the job into two phases. Phase one provisions a base test account. Phase two transitions it into the requested state (a specific document rejection, a background check status), calling the right services through the MCP gateway. The UI is built in Agent Builder.

Results Kemet reports: setup time under 30 seconds, a 95% end-to-end success rate on their evaluation suites, and self-serve use by engineers and product managers.

## The takeaways are the design

Kemet closes with four rules that are worth more than the numbers. Decouple reasoning from state mutation: the LLM maps intent to parameters and a deterministic workflow does the changes. Let agents work in parallel. Benchmark tool calls with deterministic metrics, not vibe checks. And keep safety in code and at the gateway, not in the system prompt.

## Who should watch

Platform and product engineers in large organisations deciding where agents should start, and anyone whose test setup lives in a wiki page nobody trusts. If you only have five minutes, watch the takeaways.

## Related Conf42 talks

- [Agentic Engineering Platforms](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) by Jimmy Caputo at Conf42 Platform Engineering 2026.
- [Operationalizing Agentic LLMs: Building and Evaluating DevMate at Scale](https://www.conf42.com/MLOps_2026_Anay_Paul_devmate_agentic_llms) by Anay Paul at Conf42 MLOps 2026.
- [Beyond the Claw: Building Your Personal Coding Agent](https://www.conf42.com/Platform_Engineering_2026_Erik_Hanchett_coding_agent_claw) by Erik Hanchett at Conf42 Platform Engineering 2026.

[Watch Kemet Dugue's talk](https://www.conf42.com/AI_Agents_2026_Kemet_Dugue_workflows_productivity_onboarding) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/G7W5sQMq5Uk).

## Watch the talk

[Integrating Agentic Workflows: Scaling Engineering Productivity for Uber's Driver Onboarding Team](https://www.conf42.com/AI_Agents_2026_Kemet_Dugue_workflows_productivity_onboarding) at Conf42 AI Agents 2026.
