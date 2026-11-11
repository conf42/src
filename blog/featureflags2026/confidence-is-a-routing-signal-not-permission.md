# In agentic logistics, confidence is a routing signal, not a permission

Conf42 Blog, 2026-09-19, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/confidence-is-a-routing-signal-not-permission

In short: Walmart's Pavan Boppidi at Conf42 Feature Flags 2026 on combining feature flags with confidence, stakes and novelty gates to grant AI agents authority.

A routing agent proposes a reroute at 99% confidence, built on a thin history, and with no gate in the way, 99% gets treated as permission. At Conf42 Feature Flags 2026, Pavan Boppidi, Staff Software Engineer at Walmart, walked through a control plane for agentic logistics where a feature flag decides whether an autonomous capability is exposed at all, and a separate per-decision gate decides whether the agent may act on this specific case right now. He notes the views are his own, not his employer's.

His framing: the goal isn't full automation, it's controlled autonomy.

## Two questions a Boolean can't answer

Pavan starts from the feature flag crowd's comfort zone: roll out to 1% of traffic, watch telemetry, roll back without redeploying. Now put something else behind the flag. It isn't a button colour anymore; it's an agent that chooses tools, spends money and reroutes a fleet. On or off says nothing about who may act on which decision, with what confidence, under what conditions.

So he splits the problem. Should this capability be exposed? That's a flag question. Given it is exposed, should the agent execute this decision now? That's governance. His airport analogy works: the flag decides whether the terminal is open; the gate checks every boarding pass.

Logistics makes it urgent because decisions chain. A carrier suspends a lane, which changes routing, which changes when inventory arrives, which changes replenishment and what you can promise a customer. One event, four decision loops.

## The autonomy flag is a versioned policy object

The useful flag, in his design, isn't true or false. It's a policy: enabled, a mode such as delegative, a rollout percentage, a confidence floor, an allow-list of tools, a cost ceiling, a kill-switch condition and an expiry date. He's careful to say the schema is a pattern proposed for the talk, not a standard; the standard part is OpenFeature underneath, so the application code stays portable across flag platforms. Once autonomy is a policy, you can review it, diff it, audit who changed it, canary it and roll it back, which looks a lot more like running production config than talking about model behaviour.

## Confidence, stakes and novelty decide together

A governance layer intercepts every agent-proposed action and routes it. Routine, non-safety-critical decisions that clear the threshold execute autonomously. Broader ones go to a person with a structured evidence package. Safety-critical, time-sensitive ones go to a pre-validated edge rule set rather than waiting on a human or a cloud round trip. If a human doesn't respond, the default is safe inaction: silence never turns into permission.

Confidence alone is not the policy. Stakes say how much error you can tolerate; novelty says how far the situation sits from anything the system has seen. A very confident score on an irreversible action should still escalate, and scores are only useful if calibrated and watched for drift. He also lays out four authority modes, from advisory (human decides) to supervised autonomy (people supervise the policy, not every event), instead of a single human-in-the-loop switch. Nobody wants a job clicking approve on whatever the AI says.

## The tool is the trust boundary

Two failure modes from the opening scenario get their own sections. Flipping the flag stops new runs but not the ones in flight, so a real kill switch drains active runs, revokes tool leases, invalidates cached authorisation and then verifies tool calls have actually dropped. And shadow AI: an agent nobody registered calling the same carrier API. His answer is identity at the tool boundary, with a security sidecar doing signed identity, policy checks and MCP schema validation, so the unregistered agent's call is blocked, logged and reported. The model can ask for an action; it can't grant itself the authority.

He closes with a staged rollout (shadow, advisory, guarded delegation to a 1-10% cohort, then scale), an authority trail in every event record (agent identity, flag version, confidence, decision, tool scope, outcome), a 90-day path that starts with the control surface rather than the model, and five SLOs of which only one, decision quality, is a classic model metric. Human review queues get treated as a finite resource too.

## Who should watch

Platform and operations engineers being asked to let agents act on real systems, in logistics or anywhere with expensive side effects. It's architecture-heavy and dense, with a useful six-question self-check near the end.

## Related Conf42 talks

- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis of AWS at Conf42 AI Agents 2026.
- [Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human) by Vishal Shah of Visa at Conf42 SRE 2026.

[Watch Pavan Boppidi's talk](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/h6ugmcYyivY).

## Watch the talk

[Feature-Flagged Autonomy: Confidence-Gated Human-AI Logistics Systems](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) at Conf42 Feature Flags 2026.
