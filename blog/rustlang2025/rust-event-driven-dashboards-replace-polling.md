# Rust event-driven dashboards that stop polling for incidents

Conf42 Blog, 2025-07-22, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-event-driven-dashboards-replace-polling

In short: Tashi Garg of Juniper Networks at Conf42 Rustlang 2025 on replacing polling dashboards with a Rust telemetry pipeline that pushes events to the UI.

A dashboard that polls every 30 seconds is a dashboard that is, by design, up to 30 seconds wrong. At Conf42 Rustlang 2025, Tashi Garg, Senior Staff Software Engineer at Juniper Networks, argued that this staleness is where incidents hide, and that a Rust-built, event-driven telemetry pipeline is how you get the delay out of the loop.

It is a short, focused talk: the problem, why Rust fits, one case study, and a phased rollout plan. Good value for anyone who has watched a graph turn red a few minutes after the customer tickets arrived.

## Polling dashboards are blind by construction

Tashi's framing starts with mechanics. Most static dashboards collect data at a fixed interval, often 30 seconds or a minute depending on the widget, so an event can happen well before it shows up on screen. Add binary or threshold-based health checks on top, and the slow, intermittent failures (packet loss that comes and goes, latency that degrades without crossing a line) never get flagged at all.

Tashi presented figures for both effects: detection delays averaging around 8.5 minutes from onset to first visibility, and a large share of anomalies that threshold checks simply missed. Combine staleness with missed anomalies and you get what the talk calls the reactive monitoring trap: teams only respond once the issue is already hurting customers.

## Why the backend has to be Rust-shaped

The fix is a push model: process telemetry as it arrives and stream updates to the UI instead of waiting for the next poll. That only works if the pipeline keeps latency flat under load, and that is the case Tashi makes for Rust.

The list is the familiar one, but it is pointed at a specific failure mode. No garbage collector means no GC pause at the exact moment a telemetry spike hits. The borrow checker rules out data races in concurrent ingestion code. Zero-cost abstractions let you write readable stream processing without paying for it at runtime.

The ecosystem named in the talk is concrete: Tokio for async ingestion across many concurrent IO-bound tasks, zero-copy serialization for big JSON, protobuf or Avro payloads, a low-latency web framework to push live updates, and crossbeam for multi-core concurrency primitives.

## The reference stack is small and boring, in a good way

The suggested architecture has four layers. Lightweight Rust agents on hosts (the talk cites a target of under 15 MB and under 2% CPU) ship telemetry over gRPC or WebSockets. An async streaming pipeline processes it across cores. A real-time API layer pushes updates to the dashboard within tens of milliseconds. The UI subscribes over WebSockets or server-sent events instead of polling.

In the case study, a global financial services provider running more than 12,000 instances across several clouds, Tashi reported the Rust backend handling 3.2 million telemetry data points per second, with incident detection dropping from about 11 minutes to 47 seconds. Those are the speaker's numbers from that deployment; the talk does not show the code or the methodology in depth.

## Roll it out in phases, not in one heroic rewrite

The most practical slide is the adoption plan. Spend the first month auditing blind spots and recording baseline MTTR and downtime. Run agents in staging for a couple of months and validate latency, throughput and detection accuracy. Roll to production over a quarter, wired into the incident tooling, and only then layer on ML anomaly detection or natural-language query interfaces.

Tashi also named the three predictable obstacles: legacy systems (bridge with FFI or gRPC rather than replacing everything), the Rust skill gap (start with one self-contained component), and data volume (filter and aggregate at the agent before sending upstream).

## Who should watch

SREs and platform engineers who own monitoring and suspect their dashboards are lagging reality. It is more architecture pitch than code walkthrough, so Rust experts looking for implementation detail will want to pair it with something hands-on.

## Related Conf42 talks

- [Perses, the GitOps native dashboard visualization tool](https://www.conf42.com/Kube_Native_2024_Erwin_de_Keijzer_gitops_perses_dashboard_visualization) by Erwin de Keijzer: dashboards as code, the other half of the dashboard problem.
- [The Failures You Don't See on Dashboards](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) by Abhimanyu Narwal: a reliability case study about what graphs hide.
- [Business Insights with OpenTelemetry](https://www.conf42.com/Cloud_Native_2025_Brian_Loomis_observability_insights_telemetry) by Brian Loomis: what to put into the telemetry stream in the first place.

[Watch Tashi Garg's talk](https://www.conf42.com/Rustlang_2025_Tashi_Garg_cloud_ai_rust)

[Watch the talk on YouTube](https://youtu.be/zpii75N7yns).

## Watch the talk

[Beyond Static Dashboards: How Rust-Powered Dynamic UIs Transform Cloud Infrastructure Management](https://www.conf42.com/Rustlang_2025_Tashi_Garg_cloud_ai_rust) at Conf42 Rustlang 2025.
