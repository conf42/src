# Let the AI propose, let governance decide what actually runs

Conf42 Blog, 2026-02-17, updated 2026-11-09. https://www.conf42.com/blog/sre2026/separate-ai-decisions-from-authorization

In short: Suganya Nagarajan of Amazon at Conf42 SRE 2026 on Human-Governed Automation Loops, which split decision generation from authorization to cap blast radius.

Automation that can act on millions of requests can also break millions of requests, and it does it at network speed. At Conf42 Site Reliability Engineering 2026, Suganya Nagarajan, Software Development Manager at Amazon, presented Human-Governed Automation Loops (HGAL): an architecture where AI components propose actions and a separate, human-defined governance layer decides which of them may execute.

Her framing of the problem is one every SRE will recognise: as systems scale, "manual interventions become a bottleneck, but blind automation is a liability." HGAL is her attempt to keep the speed of the first option without inheriting the second.

## Postmortems are governance that arrives a week late

The reliability gap she describes is about timing. Most governance today is offline or asynchronous: reviews, approvals, the postmortem that explains last week's outage. Useful for next time, useless for the retry storm happening now. Her example is a plain one: an automated service retries failed requests and accidentally DDoSes its own backend, burning the error budget in seconds while the safety net is still reading the ticket.

What she wants instead is governance that watches the service level indicators live, notices that failures jumped after a bad deployment, and reverts the change before the outage lands.

## Proposing and authorizing are two different jobs

The core move in HGAL is separating decision generation from decision authorization. The AI engines keep generating actions continuously, so the system never blocks waiting for a human. A control plane sits between those proposals and production and acts as a gatekeeper for every automated action, which she likens to policy as code.

Her running example is dynamic pricing or traffic shaping: the model proposes shifts every minute to match demand, and the governance layer refuses the ones that would breach the SLOs. The humans never review each decision. They write, observe and evolve the rules that do.

## Delegation boundaries decide who gets paged

Since nobody can approve every action, the interesting design work is in what she calls decision delegation boundaries: the line between acting alone and escalating. The dimensions are confidence, impact, historical reliability and context. A disk cleanup at 80% usage is an independent task. A database failover hits an escalation boundary.

Context is the part people tend to skip. If the system is already fragile, for example running with high latency, HGAL tightens the boundaries and asks for more human authorization. Her policy example is the kind you could paste into a config file: no automated restarts if the error budget is below 10%. In her words, designing these boundaries well "is the difference between building a self-healing system and a runaway failure."

A side benefit she points out: blameless postmortems get better evidence. Instead of asking why the automation failed, you can audit exactly why a decision was authorized or denied, given the SLIs at that moment.

## The honest part: it costs something

The talk does not pretend this is free. She lists latency trade-offs, governance models that have to keep evolving, and the work of training staff to run automation rather than fight fires by hand. Her takeaways boil down to three: monitor continuously, design boundaries around the thresholds that keep you accountable, and embed governance in the control plane rather than bolting it on at the edge.

## Who should watch

This is an architecture talk, not a product demo or a code walkthrough. Watch it if you run auto-remediation, experimentation platforms, recommendations or notification systems and are trying to decide how much autonomy to hand over. If you already have policy-as-code gates in front of your automation, the delegation-boundary vocabulary is still worth stealing for your next design review. It closes on a line worth pinning above the deploy button: "Let's build systems that are safe as they are fast."

## Related Conf42 talks

- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) by Neeraj Kumar Singh Beshane.
- [Feature-Flagged Autonomy: Confidence-Gated Human-AI Logistics Systems](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) by Pavan Boppidi.
- [From Self-Service to Safe Autonomy: The Authority Shift](https://www.conf42.com/Platform_Engineering_2026_Ruby_Agarwal_autonomy_service_authority) by Ruby Agarwal.

[Watch Suganya Nagarajan's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Suganya_Nagarajan_human_governed_automation) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/rT-XNpxYvlc).

## Watch the talk

[Human-Governed Automation Loops for Reliable AI at Planet Scale](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Suganya_Nagarajan_human_governed_automation) at Conf42 Site Reliability Engineering (SRE) 2026.
