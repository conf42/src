# An observability maturity roadmap written for analytics leaders

Conf42 Blog, 2025-05-14. https://www.conf42.com/blog/obs2025/observability-maturity-for-analytics-leaders

In short: Raghavender Puchhakayala of JPMorgan Chase at Conf42 Observability 2025 on four pillars, four pitfalls and a reactive-to-predictive maturity path for distributed systems.

Most observability talks are pitched at the engineer holding the pager. Raghavender Puchhakayala's talk at Conf42 Observability 2025 is pitched at the person who has to justify the budget. Puchhakayala, of JPMorgan Chase and a Senior Member of the IEEE, treats observability as a strategic data product and offers analytics leaders a four-stage maturity roadmap, from reactive to predictive, for distributed systems.

Honest scope: this is a short overview, not a hands-on session. It is useful as a shared vocabulary for a planning meeting, less so as a how-to.

## Monitoring knows what to look for; observability doesn't need to

The framing is the standard distinction, stated cleanly. Traditional monitoring watches known issues with predefined metrics and threshold alerts. Observability aims at the unknown unknowns, through high-cardinality telemetry and context-rich data. He also puts a number on why the distinction matters: a 99.99% availability target leaves roughly 22 minutes of downtime a month, which is not much time to discover you were watching the wrong graph.

He splits the value three ways: business insight into user journeys, operational intelligence for spotting anomalies, and the telemetry foundation that feeds both.

## Four pillars, with events added

Puchhakayala uses four pillars rather than three. Metrics for quantities over time like CPU, memory, latency and throughput. Logs for timestamped, structured event records. Traces for request flows across services. And events for state changes such as deployments and configuration changes, the pillar that most often explains why the other three suddenly look different.

On top of the pillars he places analytics: interactive exploration across all telemetry, ML-driven pattern recognition for anomalies, correlation of business and technical data for impact, and predictive analytics.

## A reference architecture in four layers

The architecture slide is a tidy checklist. An instrumentation layer with OpenTelemetry agents and SDKs. A collection and transport layer using streaming tools such as Kafka and Flink. A storage and processing layer of time-series databases and tracing backends. And an analysis layer of dashboards, notebooks and alerting. He then surveys the usual tools (Prometheus, Grafana, Elasticsearch, OpenTelemetry, Jaeger, Datadog, New Relic, Dynatrace) and suggests choosing by ease of use, scalability, integrations and overall cost and complexity.

## The four pitfalls

This is the slide to bring to your next retro. Data deluge: collecting everything without a purpose, so signal drowns in noise. Tool sprawl: fragmented visibility across platforms that do not correlate. Siloed ownership: platform teams working in isolation from the people who need the insight. And alert fatigue: too many low-value notifications, so the important one gets ignored.

## The maturity path and the leader's job

The roadmap has four stages: reactive (respond after impact), proactive (catch issues as they emerge), analytical (understand patterns and dependencies) and predictive (forecast before they occur). The leader's role, as he describes it, is translating telemetry into business impact, building feedback loops from insight to action, and driving data literacy across teams. His closing advice is to define business outcomes first, start with high-impact services, build teams that mix analytics and operations, and climb the maturity ladder one step at a time.

## Who should watch

Analytics and engineering leaders who need a framework to explain observability to the business, and teams writing their first observability strategy document. Practitioners who already run OpenTelemetry in production can skip to the pitfalls slide.

## Related Conf42 talks

- [Techniques for SLOs and Error Budgets at Scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) by Fred Moyer at Conf42 Observability 2023.
- [Mastering OpenTelemetry Collector Configuration](https://www.conf42.com/Observability_2024_Steve_Flanders_Curtis_Robert_mastering_collector_configuration) by Steve Flanders and Curtis Robert at Conf42 Observability 2024.
- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) by Mandi Walls at Conf42 Site Reliability Engineering 2025.

[Watch Raghavender Puchhakayala's talk](https://www.conf42.com/Observability_2025_Raghavender_Puchhakayala_tools_mastering_techniques) or the [YouTube recording](https://youtu.be/zmSi2jdtPLo).

## Watch the talk

[Mastering Observability in Distributed Systems: Tools, Techniques, and Lessons Learned](https://www.conf42.com/Observability_2025_Raghavender_Puchhakayala_tools_mastering_techniques) at Conf42 Observability 2025.
