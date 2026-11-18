# Dashboards don't act, so eBay built systems that do

Conf42 Blog, 2025-09-02, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ebay-from-dashboards-to-self-defending-systems

In short: eBay's Sureshkumar Karuppuchamy at Conf42 Platform Engineering 2025 on SLO-driven alerts, adaptive rate limiting and auto-rollbacks that earn trust.

Adaptive rate limiting alone prevented nearly 30% of major incidents on the platform Sureshkumar Karuppuchamy works on. Sureshkumar, an Engineering Lead at eBay, told that story at Conf42 Platform Engineering 2025 as part of a bigger argument: dashboards show you problems but never fix them, so at billions of requests the reliability has to live in the system, with humans paged only for what truly needs them.

The talk opens with the scene everyone knows: 2 AM, phone buzzing, squinting at graphs while trying to contain something. Then it spends half an hour explaining how to stop being the control loop.

## Observability built for machines to act on

The old way was to collect everything, build endless dashboards and hope someone noticed the right spike. The new way is SLO-driven signals tied to user experience: p95 latency, availability, checkout success rate. Error budgets decide when to ship fast and when to slow down.

The supporting patterns are concrete. One golden dashboard per service, not ten. OpenTelemetry first, so metrics, traces and logs share a pipeline, with trace IDs on metrics so an engineer can jump from a latency spike straight to the trace behind it. W3C trace context propagated everywhere, with tail-based sampling that keeps the errors and outliers. Structured JSON logs, with sensitive data redacted at the collector and routing by severity. Deployments and feature flag toggles appear as annotations on dashboards. Real user monitoring and CDN metrics extend the view past the backend, and capacity and cost are tracked per owning team.

## Alerts are control signals

Static thresholds fail because normal keeps moving, so the team built anomaly detectors that learn usage patterns and warn before capacity limits, plus models that forecast latency spikes and correlate logs, metrics and traces. The nicest trick is using browser JavaScript errors as a release signal: if a rollout pushes JS errors up, it rolls back before users notice.

From there, alerts trigger actions. A slow dependency trips a circuit breaker. An error budget burning too fast rolls back the deployment. Multi-burn-rate alerts catch both fast spikes and slow leaks, and only real user impact pages a human; the rest goes to chat or tickets.

Automation comes in tiers. Tier one, safe and reversible actions like throttling and circuit breakers, always runs automatically. Tier two, progressive changes like shifting regional traffic, can start on its own but leaves room for human oversight. Tier three, complex or novel incidents, notifies a person and hands them runbooks and context. In his words, automation handles the easy 80% while humans take the hard 20%.

## Every scar becomes a safeguard

Many of their incidents were not infrastructure failures but workload anomalies: a buggy client spamming requests, an internal batch flooding an API. Static limits could not adapt, so they built throttling that learns normal traffic per client and per endpoint and contains runaway workloads automatically. That is the 30% figure above.

The cultural rule behind it is the line worth stealing. Every postmortem asks two questions: could this have been auto-detected, and could it have been auto-mitigated? If yes, they build it. A cascading outage gave them circuit breakers; a bad config rollout gave them progressive deployment. Deployment approval moved from pre-release sign-off to post-deployment analysis, with canaries, progressive rollouts and automatic rollback on SLO breaches doing the gating.

## Trust gets earned, not declared

Engineers worry automation will make things worse, so it ships in stages: first a mode where it only logs what it has done, a suggest mode where it recommends and waits for approval, then autonomous mode within guardrails, with every action transparent, reversible and explainable. Over time the team saw it was more reliable than a tired human at 2 AM. Business KPIs close the loop too: if a release looks fine technically but cart abandonment spikes, it rolls back.

## Who should watch

SREs and platform engineers who own an on-call rotation and want a concrete ladder from dashboards to closed-loop remediation. The tiered automation model and the log, suggest, then act rollout are directly reusable.

## Related Conf42 talks

- [Amith Reddy Ravuru (Reltio) on platform SLOs beyond uptime](https://www.conf42.com/Platform_Engineering_2026_Amith_Reddy_Ravuru_slos_uptime_journey), for SLOs measured from request to value.
- [Rehana Sultana Khan (Versa Networks) on AI-driven rate limiting](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost), the adaptive throttling idea on its own.
- [Nick Hodges (Rollbar) on self-healing systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems), an earlier take on the same destination.

[Watch Sureshkumar Karuppuchamy's talk](https://www.conf42.com/Platform_Engineering_2025_Sureshkumar_Karuppuchamy_defense_dashboard_large)

[Watch the talk on YouTube](https://youtu.be/L5Y4Wt3yP4o).

## Watch the talk

[From Dashboard to Defense: Automating Resilience at Large Scale](https://www.conf42.com/Platform_Engineering_2025_Sureshkumar_Karuppuchamy_defense_dashboard_large) at Conf42 Platform Engineering 2025.
