# Your observability stack is an attack surface, so threat model it

Conf42 Blog, 2025-05-11, updated 2026-11-09. https://www.conf42.com/blog/obs2025/threat-modeling-observability-stack

In short: SoFi security engineer Srikanth Potla applies STRIDE to logs, metrics and traces at Conf42 Observability 2025 and sets hard baselines for monitoring pipelines.

The tool that can scrape every environment in your company is also the best lateral movement path an attacker could ask for. At Conf42 Observability 2025, Srikanth Potla, Senior Product Security Engineer at SoFi, turned the threat-modelling lens on observability itself: agents, transport, storage, dashboards and alerting. His argument is that monitoring infrastructure usually sits in a security blind spot, and that a few non-negotiable baselines close most of it.

## Telemetry is reconnaissance for the other side

Potla starts from the attacker's view. Adversaries look for the dark corners where their activity won't be logged. Worse, your observability data is intelligence for them: metrics, logs and traces reveal architecture, service dependencies and entry points. His image: a blueprint of your house left on the front porch. And because systems change, a dashboard deployed six months ago may be exposing data nobody anticipated.

Each of the three pillars leaks differently. Metrics expose architecture, logs may contain sensitive data, and traces reveal business logic and data flows.

## Three layers of risk, four motives

He describes observability pipelines as a three-layer cake. At collection, outdated agents run with excessive privileges and send data unencrypted. In transport, missing TLS, poor certificate management and weak cipher suites invite interception. In storage, the central system becomes a high-value target, with weak access controls and unpatched time series databases.

Attackers come for four reasons: reconnaissance through exposed dashboards; exfiltration of PII and secrets that ended up in logs (he's seen API keys and database credentials in plain text); alert flooding, triggering false positives so the real incident drowns; and living off the land, using your monitoring tools' privileges for lateral movement.

## STRIDE, mapped to monitoring

The centrepiece applies STRIDE to observability:

- **Spoofing**: fake metrics injected to skew data or hide activity. Authenticate every agent.
- **Tampering**: telemetry altered in transit or at rest. Use cryptographic integrity checks.
- **Repudiation**: audit logs deleted or modified. Build immutable logging pipelines.
- **Information disclosure**: sensitive metrics visible to the wrong people. Lock down dashboards and APIs.
- **Denial of service**: overloaded collectors blind you during an attack. Rate limit and add redundancy.
- **Elevation of privilege**: over-permissioned agents. Apply least privilege.

Before STRIDE, he recommends mapping the attack surface: list every observability component and data flow, mark trust boundaries (a Prometheus server reaching into several environments is one), catalogue entry points such as APIs, dashboards, agent channels and webhook receivers, and prioritise by impact, since a compromised central logging system is not the same as a compromised edge agent.

## One plausible breach, four steps

His scenario is uncomfortably believable. An outdated Grafana instance with public dashboards gives initial access and a map of the network. API keys logged in plain text, plus broadly permissioned monitoring service accounts, provide credentials. Prometheus, which already has network access everywhere for scraping, becomes the pivot into production. Then data leaves through custom metric queries, which look exactly like normal monitoring traffic.

## Baselines with numbers on them

Potla's minimums are concrete: 100% of telemetry encrypted in transit, multi-factor authentication on every monitoring dashboard, a 30-day maximum rotation for monitoring credentials, and zero secrets in logs, enforced with scrubbing and secret detection. For alerting, he treats the notification path as critical infrastructure: correlation rules to cut false positives, severity tiers where security alerts bypass throttling, and the same rigour for Slack webhooks, email servers and pagers as for public apps. The action plan: run an observability threat assessment, secure collection, transport and storage by risk, feed observability into the SOC, and track metrics like failed dashboard logins and credential rotation compliance.

## Who should watch

Anyone who runs Grafana, Prometheus or an OpenTelemetry collector fleet, and security engineers who've never been invited into the observability design review. It's a framework talk, but the baselines and the attack chain are easy to turn into tickets this week.

## Related Conf42 talks

- Alberto Gastaldello and Andrea Caretta on [Hacking OpenTelemetry: manipulating the observability pillars](https://www.conf42.com/Observability_2023_Alberto_Gastaldello_Andrea_Caretta_hacking_opentelemetry_manipulating_pillars), the tampering row in practice.
- Krishna Chaitanya Rudraraju on [Threat Modeling in DevOps: A Practical Guide for Developers](https://www.conf42.com/DevOps_2025_Krishna_Chaitanya_Rudraraju_threat_modeling_developers).
- Aleksandra Drobnjak on [Runtime Kubernetes Security: Hands-On Threat Detection with Falcosidekick](https://www.conf42.com/Kube_Native_2024_Aleksandra_Drobnjak_kubernetes_security_falcosidekick_threat_detection).

[Watch Srikanth Potla's talk](https://www.conf42.com/Observability_2025_Srikanth_Potla_modeling_insight_spots)

[Watch the talk on YouTube](https://youtu.be/6_b8I6AtEcg).

## Watch the talk

[Threat Modeling for Observability: From Blind Spots to Actionable Insight](https://www.conf42.com/Observability_2025_Srikanth_Potla_modeling_insight_spots) at Conf42 Observability 2025.
