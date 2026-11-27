# Observability costs money, so map it to business KPIs first

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observability-needs-a-business-case-to-survive

In short: Srinivas Sriram Mantrala at Conf42 Observability 2025 traces observability from threshold alerts to AI and GenAI, and why SLOs tied to KPIs fund it.

Srinivas Sriram Mantrala's talk at Conf42 Observability 2025 is a tour of how microservices monitoring grew up, from "the database is down" emails to AI-assisted, self-healing operations. Mantrala, a senior manager, keeps returning to one practical point along the way: observability comes with a cost, and nobody approves that cost unless you can show what it buys in business terms.

It is a conversational, experience-driven talk rather than a technical deep cut, and it works best as a map of where AI fits into an observability practice.

## Four stages, from alerts to self-healing

Mantrala lays the history out as a sequence. Traditional monitoring was threshold alerts for monoliths: something is up or down, an administrator reacts. Basic observability split the data into the familiar three pillars, with metrics for the high-level view, logs for granular events and traces for how a request moves through services. Still reactive, but much richer.

The next step, which he calls AI-enhanced observability, came with cloud platforms: pattern analysis on that data to learn peak hours, quiet hours and sensible maintenance windows, and to plan resources ahead. The last step is self-healing, where the same analysis drives horizontal or vertical autoscaling for events like Thanksgiving traffic without anyone touching a console.

## No KPI mapping, no budget

The section that earns the talk its place is about SLOs. Mantrala argues that unless you correlate technical metrics with business KPIs, there is no buy-in to invest in observability at all. His examples are plain: customer satisfaction depends on latency, so you need latency data to say anything about satisfaction; revenue per transaction depends on knowing how long orders take and whether the system scaled in time. Business approves the spend when it can see that link, and only then can the practice survive past the first budget review. Every SRE who has had a tracing project cut will nod along.

## Make observability part of the build

He describes a layered implementation framework: collect the data, then add validation checks so new microservices cannot reach production without the required logging, metrics and tracing, enforced in CI/CD alongside the usual quality gates. Intelligent analysis with ML models sits on top, and AIOps remediation on top of that. The point is that observability is a discipline applied to every new service, not a one-off project.

For tooling he names Grafana as his personal favourite, mainly for dashboards each role can build for itself and for its query language over historical data.

## Contextual alerts and a chatbot for the on-call

The forward-looking part is about incident response. Contextual alerting, as he describes it, means the alert arrives on your phone with the history of similar incidents, the actions taken last time and the person who fixed it, so the on-call engineer can delegate to someone who has seen it before. Intelligent routing sends specific alerts to the people with the right experience.

Then GenAI: a chatbot over historical incident data that suggests steps, summarises similar incidents and points to the most common fix, so a new team member can get going without weeks of knowledge-transfer sessions.

## Who should watch

Engineering managers building the case for observability investment, and teams early in their AIOps thinking who want a framework for where each capability fits. If you already run SLO-based alerting and incident similarity search, much of this will be familiar.

## Related Conf42 talks

- [Praemonitus praemunitus: use actionable alerts to fix problems quickly](https://www.conf42.com/Observability_2024_Leonid_Yankulin_actionable_alerts_fix) by Leonid Yankulin at Conf42 Observability 2024.
- [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws) by Indika Wimalasuriya at Conf42 DevSecOps 2024.
- [Beyond Monitoring: The Rise of Observability Platform](https://www.conf42.com/Observability_2023_Sameer_Paradkar_beyond_monitoring) by Sameer Paradkar at Conf42 Observability 2023.

[Watch Srinivas Sriram Mantrala's talk](https://www.conf42.com/Observability_2025_Srinivas_Sriram_Mantrala_microservices_metrics_architectures) or the [YouTube recording](https://youtu.be/f6uiLfF9gsE).

## Watch the talk

[Beyond Metrics: AI-Powered Observability in Microservices Architectures](https://www.conf42.com/Observability_2025_Srinivas_Sriram_Mantrala_microservices_metrics_architectures) at Conf42 Observability 2025.
