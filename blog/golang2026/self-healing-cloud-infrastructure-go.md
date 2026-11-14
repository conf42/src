# Self-healing infrastructure starts with telemetry, not with AI

Conf42 Blog, 2026-04-29, updated 2026-11-09. https://www.conf42.com/blog/golang2026/self-healing-cloud-infrastructure-go

In short: Sudhakar Pallaprolu at Conf42 Golang 2026 on Go control planes that detect, diagnose and remediate failures, with observability built first.

Systems don't fail politely: they fail at 3am, in cascades, faster than whoever holds the pager can open the runbook. [Sudhakar Pallaprolu](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure), speaking for the Indian Institute of Engineering Science and Technology at Conf42 Golang 2026, asked what it would take for infrastructure to detect, diagnose and repair itself without waiting for a human, and why Go is a good language for the control plane that does it.

It is a fifteen-minute overview of AIOps patterns rather than a build-along, but its ordering of priorities is the useful part, and it puts telemetry first.

## Humans are the slowest step in the loop

The argument opens on reaction time. With a person in the loop for every remediation step, recovery is capped by how fast someone reads an alert. A modern Go deployment is dozens of interdependent microservices, and a failure in one can spread across the dependency graph before detection even fires. The window between incident and resolution is what self-healing tries to shrink.

Sudhakar's model has three pillars: detect (real-time anomaly detection on logs, metrics and traces), diagnose (ML-driven root cause analysis across all those signals at once, rather than a human reading one service at a time), and remediate (automated but policy-gated responses), with a learning loop feeding past resolutions back in.

## Go fits the pipeline, garbage in still wins

The Go case is the concurrency model: goroutines fan out across thousands of concurrent signal streams, channels hand data cleanly between detection, analysis and remediation phases, and context propagation cancels work for an incident that is already handled.

But he is explicit that speed is useless without good input. The observability layer, built with OpenTelemetry in Go services, needs structured, machine-parsable logs, time-series metrics for latency, errors and saturation, and distributed traces that follow one user's transaction across the dependency graph. If the data is incomplete, no pipeline will find the root cause, however fast it runs.

## Predict on trends, not thresholds

The predictive section is the most practical. Rather than alerting when something is already broken, models watch leading indicators such as memory pressure, connection pool saturation and disk I/O trends. Sliding-window aggregations compare each window to the previous one to surface degradation, which is a trend, not an alert. That triggers pre-emptive actions: pod restarts, shifting traffic between nodes or sites, scaling capacity. And the models need continuous retraining, because services change and yesterday's normal drifts.

## From runbooks to closed loops

Orchestration, in his telling, has moved from static IaC templates with manual gates, to event-driven automation on thresholds, to closed-loop orchestration where policies are evaluated against runtime context and corrective actions are dispatched deterministically. Cloud tools such as Azure Automanage, AWS Fault Injection Simulator and GCP Active Assist are presented as building blocks you wire into your own Go control plane. Reconciliation loops written in Go enforce declared state and revert unauthorised drift; policy as code keeps non-compliant deployments out of production. Kubernetes operators have been doing a version of this for years, and the talk extends the same idea upward.

## Who should watch

SREs and platform engineers sketching the case for automated remediation, and teams who want an ordered checklist: observability, then policy, then prediction. It stays at the pattern level, with no code or incident numbers, so experienced operator authors will find it familiar.

## Related Conf42 talks

- [Self Healing Systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) by Nick Hodges, the earlier, broader take on the same goal.
- [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws) by Indika Wimalasuriya, AIOps applied on one cloud in detail.
- [Chaos Engineering + Generic Mitigations: The Path to Self-Healing Systems](https://www.conf42.com/Chaos_Engineering_2021_Leonid_Belkind_generic_mitigations_self_healing_systems) by Leonid Belkind, on testing the remediations you automate.

[Watch Sudhakar Pallaprolu's talk](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure)

[Watch the talk on YouTube](https://youtu.be/PT274TuaM2o).

## Watch the talk

[Autonomous Cloud Infrastructure with Go: Building Self-Healing Systems](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure) at Conf42 Golang 2026.
