# Self-healing infrastructure should automate certainty, escalate ambiguity

Conf42 Blog, 2026-10-07, updated 2026-11-09. https://www.conf42.com/featureflags2026/automate-certainty-escalate-ambiguity-flags

In short: Confluent's Prateek Jindal at Conf42 Feature Flags 2026 on feature flags as infrastructure controls in a detect, decide, recover, validate loop.

Automation can be wrong, and it can be wrong very efficiently. At Conf42 Feature Flags 2026, Prateek Jindal, Staff Software Engineer at Confluent working on distributed systems and control planes, showed how feature flags can act as infrastructure controls (routing policy, caching strategy, fallback dependency, processing path) inside a self-healing loop, and where that loop has to stop and hand the problem to a person.

His guiding rule fits on a sticker: automate certainty, escalate ambiguity.

## The same 2am fix, every time

Traditional operations run alert, investigate, diagnose, remediate by hand. That's right for novel incidents and expensive for predictable ones. A downstream dependency gets unhealthy, retries climb, latency spreads. If the failure is understood and the mitigation is known to be safe, Prateek asks, why should an engineer intervene every single time? The qualifier matters just as much: automation needs clear boundaries and shouldn't act just because a metric crossed a line.

He splits the loop into five separate layers. Observability (metrics, logs, traces and flag change events). Detection (turn telemetry into actionable conditions). Decision (is intervention justified?). Recovery (one bounded action, like disabling a capability or redirecting traffic). Validation (did health actually improve?). Keeping these apart stops every alert from turning into an automatic action. Validation is the one he leans on hardest: a restart can succeed while the dependency behind it stays sick, and automation without a check would report success while users keep failing.

## A flag doesn't have to control a feature

The central idea is that a flag is just a runtime decision, and it can choose infrastructure behaviour as easily as a UI. Ship a new routing strategy disabled by default, activate it for a limited scope, and if it misbehaves, turn off that specific path without redeploying the service. Deployment and activation become different operations, which shortens recovery because you don't have to roll back the whole deploy.

His caveats are the practical ones: the old path must stay safe and usable, the flag must be evaluated consistently wherever the behaviour is controlled, and backward compatibility has to be checked so the prior path still works when you fall back. Scope starts small (environment, service, cluster, region, tenant or availability zone), because pre-production testing, essential as it is, can't reproduce every traffic pattern or customer workload.

When latency rises a few minutes after an activation, the system should correlate it with the flag change, weigh whether the evidence is strong enough, disable the capability if configured conditions are met, and then verify recovery. That needs flag changes emitted as telemetry. He also notes that correlation isn't causation: triggers should be designed so an unrelated incident doesn't reverse a healthy change.

## Four safeguards and a break-glass

Degraded mode beats failure when it's safe. If an external dependency you don't control turns unreliable, aggressive retries only add pressure; disabling that integration and running with reduced capability keeps customers working, as long as data integrity and correctness of critical workloads are preserved.

His safeguards for automated remediation: clear trigger conditions that ignore a one-minute blip, the smallest possible remediation scope, validation of every action, and loop prevention with an audit trail. If repeated attempts fail, the next one probably won't succeed either, so stop and escalate. Record the condition, decision, action, flag change and resulting health. Unclear root causes, simultaneous failures, security concerns and data integrity risks go to humans, and operators must be able to inspect and override any automated decision. A break-glass mechanism for every automation isn't optional.

## Earn the automation in stages

Nobody has to automate everything on day one. Start in detection-only mode with runbooks for the on-call engineer, then automate low-risk cases such as restarting a Kubernetes pod, and expand as evidence builds. Test the recovery path itself regularly, because an untested recovery workflow is an assumption, not a capability. Flags need an owner, a documented purpose, a known default, permissions and a retirement plan, and permanent resilience flags should be labelled as such, or, as he says from experience, you'll later find flags nobody can explain.

## Who should watch

SREs and platform engineers who already use flags for releases and want to extend them to operational controls. It's a clear, principle-first talk; pair it with the API-focused auto-healing talk from the same event for a second take on the same loop.

## Related Conf42 talks

- [Designing a Self-Healing Ops Platform: Telemetry, RAG, and Confidence-Gated AI Agents](https://www.conf42.com/Platform_Engineering_2026_Madhu_Chenna_healing_rag_telemetry) by Madhu Chenna of Electronic Arts at Conf42 Platform Engineering 2026.
- [Autonomous Cloud Infrastructure with Go: Building Self-Healing Systems](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure) by Sudhakar Pallaprolu at Conf42 Golang 2026.
- [Event-Driven Validation for Cloud-Native Resilience](https://www.conf42.com/Cloud_Native_2026_Mohiadeen_Ameer_ai_agents_automation) by Mohiadeen Ameer of Dell Technologies at Conf42 Cloud Native 2026.

[Watch Prateek Jindal's talk](https://www.conf42.com/Feature_Flags_2026_Prateek_Jindal_cloud_infrastructure_flags) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/gKcoOk6s6BU).

## Watch the talk

[Building Self-Healing Cloud Infrastructure with Feature Flags](https://www.conf42.com/Feature_Flags_2026_Prateek_Jindal_cloud_infrastructure_flags) at Conf42 Feature Flags 2026.
