# Your agent's evals passed. The canary is where it actually gets tested

Conf42 Blog, 2026-10-29. https://www.conf42.com/prompt2026/agent-evals-need-a-canary-in-production

In short: Nicolas Zelaya of Harness at Conf42 Prompt Engineering 2026 on offline evals, versioned AI configs and agent canaries as one release loop.

A green eval suite tells you a prompt change is ready for traffic, not that it is better. At Conf42 Prompt Engineering 2026, [Nicolas Zelaya](https://www.conf42.com/Prompt_Engineering_2026_Nicolas_Zelaya_prompt_survive_production), Director of Product Management at Harness, walked one agent change from offline evals through a 20% canary and back, and showed the moment where every trace span was green while the agent still failed its users.

It is a vendor talk and says so: the tooling on screen is Harness Feature Management & Experimentation (FME) with its AI evals and AI configs. The loop he draws, though, is one any team shipping agents has to build somehow.

## The question is "did it work", asked four ways

Zelaya opens with four questions about the last change you shipped to your agent: how did you know it was better, how did you know it was safe, did it move the business the way you expected, and how fast could you iterate if it didn't. He frames the problem with a 2026 survey he cites in which 74% of enterprises had to roll back or shut down an agent rollout. Writing the agent is no longer the bottleneck. Releasing it safely, and knowing what it actually did, is.

His running example is the most common agent change there is: swap to a cheaper model. Usually the bill does go down. The catch is whether quality holds, and his line for it is worth pinning above the desk: cheaper on the test suite does not always map to cheaper in production.

## Evals are the unit tests, and unit tests are not the release

In his framing, evals are the unit tests of your agent: a dataset of golden cases plus the metrics you score against. Harness ships more than fifty built-in metrics, from deterministic checks and policy compliance to prompt-injection validation and LLM-as-a-judge rubrics. In the demo, a fintech-style agent answers "what is the fee on a late payment" under a set of rules; some tests fail, the prompt is iterated, the suite goes green.

Green here means the variation has earned traffic. That is all it means.

## One versioned object for the prompt, the tools and the limits

The piece that makes the canary possible is what Harness calls an AI config: a single versioned object holding the system prompt, user prompt templates, tool access, policy checks and limits, with several variations you can assign traffic to. Your application still executes the agent; the config decides how it runs and for whom. The SDK picks the variation per user, sticky and consistent, while you set the split from the UI, the API or the MCP server.

Every run then sends traces and events back: task success, turns, latency, limit hits, proposed actions, tool use, plus a thumbs up or down at the end of a session. Each property can become a metric compared against the baseline.

## Every span was green and four users got no answer

This is the part to watch. In the canary, every tool call succeeded. Nothing lit up on any dashboard. But four of the five test conversations asked about money coming in, and the tool returned money going out, until the token budget cut the run short. Task completion against the baseline dropped, and the cost per finished session came out higher, the opposite of what the cheaper model promised offline.

Rollback in this world is a traffic edit: move exposure off the candidate variation, no redeploy, and the change lands in the audit history. Then the production sessions that went wrong feed back into the eval dataset, a missing check gets added so the agent recognises when the data isn't there, and the same model with the same limits and tools goes back out to 20%. By the third wave, he showed the business outcome holding and the savings kept.

## Who should watch

Anyone who owns an agent in production and has been treating a passing eval run as a release decision. If you already run feature flags for code, the talk is a useful map of how the same rollout discipline (percentage splits, baselines, guardrail metrics, instant rollback) carries over to prompts and model choices. His homework list for Monday is short and good: what does your eval not check, what is your canary slice, what is your baseline outcome, and what is your rollback.

## Related Conf42 talks

- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz (Arato.ai) at Conf42 LLMs 2025, on whether your eval suite measures what you think it does.
- [From Benchmarks to Business Impact: Evaluating Generative AI in Production](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) by Srikanth Devarakonda (Adobe) at Conf42 Observability 2026, on the gap between offline scores and outcomes.
- [Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda (Microsoft) at Conf42 Feature Flags 2026.

[Watch Nicolas Zelaya's talk](https://www.conf42.com/Prompt_Engineering_2026_Nicolas_Zelaya_prompt_survive_production) or go straight to the [recording on YouTube](https://youtu.be/HDsv3o9Pk54).

## From Harness

Harness was the Diamond sponsor of Conf42 Prompt Engineering 2026. The talk shows Harness Feature Management & Experimentation with AI evals and AI configs; Zelaya's suggested starting point is uploading the prompt of an agent you already run into an AI config.

- [Harness](https://www.harness.io/): the software delivery platform behind the demo; Zelaya points viewers to harness.io to get started
- [All Conf42 Prompt Engineering 2026 talks](https://www.conf42.com/prompt2026)

## Watch the talk

[Your Agent Passed the Prompt Test. Will It Survive Production?](https://www.conf42.com/Prompt_Engineering_2026_Nicolas_Zelaya_prompt_survive_production) at Conf42 Prompt Engineering 2026.
