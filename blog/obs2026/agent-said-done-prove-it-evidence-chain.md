# Your agent said "done". Make it prove it with an evidence chain

Conf42 Blog, 2026-08-11. https://www.conf42.com/blog/obs2026/agent-said-done-prove-it-evidence-chain

In short: Emerson Braun of Plan A Technologies at Conf42 Observability 2026 on tracing agent context, decisions, actions and verified outcomes.

An agent that replies "Done. The issue is resolved." has made a claim, not delivered a result. At Conf42 Observability 2026, Emerson Braun, Staff Engineer and Regional Director at Plan A Technologies and creator of the AgentsKit side project, laid out an observability model for agents built on one rule: record context, decision, action and verified outcome, or you are guessing.

## A confident answer is just a claim

Braun's opening example is a refund. A customer asks for money back on a purchase from 20 days ago. The agent loads a policy with a 30-day window, approves the refund, and everyone is happy. Except the current policy says something else, and the question that matters in production is whether you can prove which version of the policy the agent actually used. If you cannot, you do not have observability.

The same "done" can hide three different failures, he argued: the wrong context (an outdated policy), a failed action (the refund never went through), or an unverified outcome (the customer is still waiting). A trace of the final chat message tells you none of that.

## Technical success and task success are different metrics

Anyone who has consumed a flaky API knows the pattern: a 200 response with a body that is not valid JSON, or valid JSON missing the field you need. Braun applies the same layered check to agent tool calls. Did the call return? Can the response be parsed and used? Does it contain what the workflow expects? And finally, did the intended state actually change in the world? Only the last one counts as the task succeeding.

## Failure is a state, not a conclusion

The most practical part of the talk is the case for state machines. Model each agent step as an explicit state, and a failure stops being the end of the story. You preserve the error and the execution state, classify what failed (timeout or invalid result), check what actually happened, then choose a recovery: retry, reroute, compensate, or escalate to a human.

Two details make this work. Idempotency keys, so a retried refund does not hit the customer twice. And an append-only ledger of every agent action, because if you only update the current state you cannot reconstruct the steps later. His summary of the principle: automate the recovery decisions, not the retries.

The demo makes the point with a scripted adapter, no model calls. The same refund conversation runs twice. Without observability, the agent says the refund happened and you have to take its word for it. With the trace, you see the context version, the policy version, a tool timeout, the agent treating the state as uncertain, and a status check that confirms the refund. Same outcome, but only one of them is evidence.

## Autonomy needs a control boundary

Braun sorts proposed actions by risk. Low-risk reads, searches and classification run autonomously, otherwise why have agents at all. Reversible actions run within limits and budgets. High-impact actions, like a change that touches many users in a database, always go to a human, and the human gets enough context to decide. An agent saying it wants to drop a table is not enough; which table, in which environment, is.

He also warns against the opposite failure: logging everything. Raw executions carry payloads, credentials and PII. Put a privacy boundary in the middle (allowlists, redaction, masking) and keep versions, routes, statuses, validations and outcomes. Collect enough to explain the system, not enough to recreate the user.

The talk closes with a ten-point checklist, from versioning instructions and context, through tracing every external boundary and binding approvals to exact actions, to linking metrics back to traces. Cost gets its own warning: the model call is rarely the whole bill once retries, tool calls and waiting are counted.

## Who should watch

Engineers putting agents in front of customers or production systems, especially anyone whose agent can move money or change data. It is a framework talk with a small scripted demo, not a product pitch; AgentsKit appears as the speaker's own example code. If you already run state machines for workflows, the novelty is applying that discipline to the parts of the agent you cannot see.

[Watch Emerson Braun's talk](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) ([YouTube](https://youtu.be/ZKqDNqO-anM)).

## Related Conf42 talks

- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis (AWS), AI Agents 2026.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar (AuthZed), LLMs 2026: the permissions side of the control boundary.
- [Orchestrating AI Agents with Pattern Matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) by Michael Haim (Zindell Technologies), AI Agents 2026.

## Watch the talk

[Make Agents Observable: Tracing Decisions, Tool Calls and Recovery](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) at Conf42 Observability 2026.
