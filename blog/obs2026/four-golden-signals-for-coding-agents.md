# Your coding agent is a production system. Give it golden signals

Conf42 Blog, 2026-08-15. https://www.conf42.com/blog/obs2026/four-golden-signals-for-coding-agents

In short: Elliot Gardiner of Code Telemetry at Conf42 Observability 2026 maps Google's four golden signals onto AI coding-agent sessions and trajectories.

Most teams measure AI coding assistants by tokens spent and seats used, which is roughly like monitoring a web service by its electricity bill. At Conf42 Observability 2026, Elliot Gardiner, Founding Engineer at Code Telemetry, took the Google SRE four golden signals (latency, traffic, errors, saturation) and applied them to Claude Code and Codex sessions, treating each one as a production system whose trajectory you can measure.

## Why a laptop process counts as production

Gardiner has the SRE background to make the argument, with stints at Capital One, JPMorgan and Mastercard, where he worked on optimising coding assistant usage. His case: coding agents increasingly run unattended, for a long time, against your real repository, and sometimes in the cloud. They call external services (model APIs, MCP servers, package registries, test runners), consume constrained resources (tokens, context window, rate limits), retry failures on their own, carry state that degrades as the context fills, and produce consequential output in the form of commits and pull requests. That is a production system with a terminal attached.

His joke slide puts a normal service dashboard next to what you get out of the box from a coding agent: an agent started 47 minutes ago, and that is about it. He admits the slide is generous.

## The signals, translated

Traffic becomes human prompts, the count and variety of tool calls, tokens produced and the kinds of file edits, all tied to session metadata. Latency becomes checkpoints in the delivery cycle: first prompt to first file edit, to passing tests, to a reviewable change. Saturation covers context pressure, subscription rate limits, rate limits of downstream systems such as dev environments, and concurrency, since parallel agents editing the same file are a merge conflict waiting to happen. Errors are where it gets interesting.

## A failed tool call is a 404, not a 500

Gardiner's best analogy is the old SRE argument about 4xx codes. A 404 on your homepage is an outage; a 404 from a crawler guessing URLs is noise. Agent tool calls work the same way. A grep that returns a non-zero exit code during exploration is the agent learning. In one session he walks through, an early `ls` of node_modules fails, and the agent recovers with a cached `npm ci` seconds later. Not an error worth reporting. Further down the same session, though, the agent says the change still needs a benchmark against real data that it never ran. The task was to bring an API inside a two-second latency target, and nothing proved it did.

So correctness is judged against the outcome: the task intent, a relevant check, an observed result, and a comparison between them. Tool exit codes inform that verdict but do not decide it.

## Converging or stuck

The talk's most reusable slide lists failure patterns worth alerting on. Retry loops, where edit, test, fail repeats without the agent changing approach. Repeated edits with no tests at all. Tool fallback, when an MCP call fails and the agent drops to bash. Spend without progress: tokens burned, files changed, no tests, no pull request. And review rework, the extra cycles after a human or another agent reviews the PR. The summary test is whether retries produce new evidence: an agent hitting different errors and then passing is converging; one hitting the same failure after the same edits is stuck.

Each pattern points to a fix. The node_modules probe suggests a better environment bootstrap or base image. Sessions that always succeed might be running the most expensive model at full effort, a right-sizing job like picking EC2 instance sizes. Changes to agent instruction files can be checked against data instead of vibes. Frequent context overload says the tasks are too big; frequent conflicts say the code needs reorganising for parallel work.

## Who should watch

Platform and developer-experience teams paying for coding agents, and SREs who want a familiar frame for an unfamiliar workload. Gardiner builds Code Telemetry and shows its session UI, so this is partly his own product, but the signal definitions stand on their own. His closing line is the thesis in one sentence: we did not make production reliable by making software stop failing, we made failure observable.

[Watch Elliot Gardiner's talk](https://www.conf42.com/Observability_2026_Elliot_Gardiner_agents_codegeneration_tracing) ([YouTube](https://youtu.be/il86h4NsCEw)).

## Related Conf42 talks

- [The Harness Decides What to Trust: Running AI Coding Loops Without Shipping Fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) by Ruben Marcus Luz Paschoarelli (MultiVM Labs), AI Agents 2026.
- [Who Judges the AI Agent? LLM-as-Judge for Testing Non-Deterministic Code Generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) by Liran Yushinsky (JFrog), AI Agents 2026.
- [AI Coding Agents and how to code them](https://www.conf42.com/Machine_Learning_2025_Alex_Shershebnev_code_agents_coding) by Alex Shershebnev (Zencoder), Machine Learning 2025.

## Watch the talk

[Beyond Token Counts: Observability for AI Coding-Agent Trajectories](https://www.conf42.com/Observability_2026_Elliot_Gardiner_agents_codegeneration_tracing) at Conf42 Observability 2026.
