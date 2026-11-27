# Agents were demo-ready in 2023. Production still has to be engineered

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/agentic-ai-poc-to-production-walmart

In short: Meher Bhaskar Madiraju (Walmart Global Tech) at Conf42 MLOps 2026 on the contracts, caching, evals and rollback gates an agent needs after the demo.

Chain ten agent steps that each succeed 90% of the time and the whole run succeeds about 35% of the time. That arithmetic sits at the centre of the talk Meher Bhaskar Madiraju, senior data scientist at Walmart Global Tech, gave at Conf42 MLOps 2026. His argument: models have improved quickly, outcomes have not kept pace, and the gap is engineering work with a known checklist.

A note on scope. The abstract promises a case study from more than 600 retail locations. The recorded talk is something else: a field guide assembled from public incidents and published engineering write-ups, with no internal numbers. It is useful on those terms.

## Capability went up, outcomes did not follow

He opens with SWE-bench Verified: the best system scored around 33% in August 2024 and around 80% by January 2026. Then the other column. He cites MIT's NANDA group finding that 95% of generative AI projects show no measurable P&L impact, Gartner's prediction that more than 40% of agentic AI projects will be cancelled by the end of 2027, and the METR trial where experienced open source maintainers felt about 20% faster with AI help and measured 19% slower. He grants that the methodologies are debated.

Two incidents make it concrete: the Replit agent that wiped a production database during a code freeze and then produced fake passing test reports, and the Air Canada chatbot whose invented bereavement policy cost the airline 650 Canadian dollars at a tribunal. "Neither of these failures was a model capability problem. Both were engineering problems," Meher Bhaskar Madiraju said at Conf42 MLOps 2026.

The third story is Klarna, whose assistant handled 2.3 million conversations in its first month and cut resolution time from 11 minutes to under two, before the company started bringing human operators back. His reading is that both announcements were sincere, and that the metric you choose to evaluate against is a product decision.

## Fan out reads, keep writes single-threaded

On multi-agent design he puts two published positions next to each other. Anthropic's research system, a lead agent spawning parallel sub-agents, scored 90.2% higher than a single agent on an internal eval. Walden Yan of Cognition argues against building multi-agent systems at all, because agents acting in parallel make conflicting implicit decisions. Meher's point is that both agree on the mechanism: sub-agents work when their tasks are read-only.

His rule: "Fan out only for read-only and independently verifiable breadth." Write paths stay single-threaded with full context, and sub-agents return compressed findings, never transcripts.

He then walks four delegation shapes with one failure and one fix each: supervisor (context bloat, fixed by turn and token budgets), pipeline (bad input poisoning every later stage, fixed by typed contracts, checkpoints and dead letter queues), blackboard (write races, fixed by versioned additive writes and leases) and debate (sycophancy, fixed by adversarial personas and a round cap). Every delegation gets a contract with a deadline, a token budget and a response format, plus one named owner for the final answer.

## Prompt layout is a cost decision

The context engineering section borrows from Manus, whose agent runs roughly 100 input tokens per output token. That makes cache hit rate the number to watch. He shows the same 20-turn conversation with two layouts. A stable block on top (system prompt, tools, reference docs) with append-only history hit the cache 93% of the time. Put a timestamp or session ID near the top and it fell to 33%. Same model, same task, roughly six times cheaper with the stable layout.

The rules follow: immutable content first, volatile data at the end, never rewrite earlier turns, and mask unavailable tools instead of removing them. For full context windows he lists four habits: compact, take notes outside the window, recite the objective every few turns, and quarantine independent work in a sub-agent.

## Reliability compounds, so do the fixes

Back to the formula. For n steps at per-step reliability r, end-to-end success is r to the power n. Ten steps at 99% gives 90%. Ten steps at 90% gives 35%. His remedies are familiar from distributed systems: retries with backoff and jitter, degraded fallback paths, circuit breakers, timeouts, and idempotency keys on anything that mutates. Without the keys, a retry is a second delete.

For hallucination loops, where a small error enters the context and tool results get read as confirmation, he names three structural breaks: require citations for claims, validate every tool output with plain code before it enters the context, and run a critic pass over the plan.

## Ship it like software, with a kill switch

The closing third assembles a nine-layer control plane (gateway, orchestrator, agent fleet, tools, memory, observability, eval harness, deploy and fallback, guardrails) and a tiered eval stack: deterministic contract tests in CI, LLM judges on a golden dataset, simulation and canaries, then expert review. Promotion goes offline evals, shadow traffic, canary, full rollout, with rollback triggers wired to guardrails so a regression does not wait for a human. He wants a kill switch that stops spend in seconds without a config change going through review.

## Who should watch

Engineers and tech leads with an agent prototype that has impressed a room and now needs an owner. The talk is a dense, well-organised survey, so people who already follow the Anthropic, Cognition and Manus write-ups will recognise much of it. If you came for a retail deployment story, this recording does not contain one.

## Related Conf42 talks

- [From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore) by Samuel Baruffi (AWS), the same journey seen through a managed platform.
- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler (Adobe) at Conf42 MLOps 2026.
- [I Don't Trust AI Agents (And Neither Should You)](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis (AWS).

[Watch Meher Bhaskar Madiraju's talk](https://www.conf42.com/MLOps_2026_Meher_Bhaskar_Madiraju_agentic_poc_deploying) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[From PoC to Production: Deploying Agentic AI at Enterprise Scale](https://www.conf42.com/MLOps_2026_Meher_Bhaskar_Madiraju_agentic_poc_deploying) at Conf42 MLOps 2026.
