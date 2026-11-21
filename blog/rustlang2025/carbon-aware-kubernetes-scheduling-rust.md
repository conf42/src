# A carbon-aware Kubernetes scheduler in Rust, rolled out in four phases

Conf42 Blog, 2025-08-13. https://www.conf42.com/blog/rustlang2025/carbon-aware-kubernetes-scheduling-rust

In short: Bandhavi Sakhamuri, Senior SRE at SolarWinds, at Conf42 Rustlang 2025 on a Rust scheduler that places Kubernetes workloads by carbon intensity.

The default Kubernetes scheduler knows about CPU, memory and affinity rules, and nothing about whether the node it picks runs on wind or coal. At Conf42 Rustlang 2025, [Bandhavi Sakhamuri](https://www.conf42.com/Rustlang_2025_Bandhavi_Sakhamuri_cloud_ai_rust), a Senior Site Reliability Engineer at SolarWinds, presented a framework she has been researching: a Rust-based, carbon-aware scheduler that uses carbon intensity data and ML energy forecasts to decide where and when workloads run.

It is a design talk. The architecture, the algorithms and the rollout plan are clear; the savings figures are targets for a full deployment, not measured results, and there is no code walkthrough.

## What the default scheduler ignores

Her starting point: data centers already use roughly 1% of global electricity, AI training is pushing cloud usage up, and schedulers optimise only for performance and availability. Idle instances sit around costing money and emitting carbon. Whether you run EKS, AKS, GKE or bare metal, the scheduler has no carbon signal to work with.

## Three components, all in Rust

The framework has three parts:

- **A carbon-aware scheduler** that replaces the default kube-scheduler and pulls real-time data from carbon intensity APIs, so it knows which energy source sits behind each node.
- **A workload analyzer** that classifies workloads (batch, stateless, critical production) and estimates their energy consumption.
- **A metrics collector** that records CPU, memory and energy use per workload, along with the energy source it actually consumed.

Rust is there for the usual reasons she lists: memory safety without a garbage collector, predictable performance and a small footprint, so the scheduler itself does not become a resource hog. It plugs into the existing scheduler interface, the metrics server, custom resource definitions and an operator.

## Move work in time and in space

The scheduling logic combines two kinds of optimisation. Temporal: shift flexible jobs to periods of low carbon intensity or high renewable availability. Spatial: place non-critical workloads on nodes powered by lower-carbon sources, while critical, high-availability workloads stay where they are guaranteed to run. SLAs act as the hard constraint throughout.

Energy predictions come from gradient-boosted trees, RNNs for temporal patterns, and reinforcement learning that keeps adjusting toward lower carbon use.

## A rollout an SRE would sign off on

The four-phase plan is the most practical part:

1. Batch and non-time-sensitive jobs only, collecting baseline metrics.
2. Production in monitoring-only mode, so you learn what would move without moving it.
3. Carbon preferences for stateless services with some SLA leeway, behind canary or rolling deployments.
4. Full rollout, only after reviewing data from both non-prod and prod with the teams involved.

Her projections for a full rollout are a 40% carbon reduction and about 15% lower cost.

## Who should watch

SREs and platform engineers who are being asked about sustainability targets and want a concrete shape for carbon-aware scheduling. If you need benchmarks or source code, this talk gives you the design to evaluate rather than a tool to install.

## Related Conf42 talks

- [From Error Budgets to Carbon Budgets: Empowering SREs for Eco-Efficiency](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pini_Reznik_error_carbon_empowering) by Pini Reznik (re:cinq) at Conf42 SRE 2024.
- [Green DevOps: Building Sustainable Software](https://www.conf42.com/DevOps_2024_Neel_Shah_green_sustainable_software) by Neel Shah (Internauts Infotech) at Conf42 DevOps 2024.
- [How to build your own green observability pipeline](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) by Diana Todea (VictoriaMetrics) at Conf42 Observability 2026.

[Watch Bandhavi Sakhamuri's talk](https://www.conf42.com/Rustlang_2025_Bandhavi_Sakhamuri_cloud_ai_rust) or the [YouTube recording](https://youtu.be/DcOwzf6QfKc).

## Watch the talk

[Rust-Based AI-Driven Carbon-Aware Kubernetes Scheduling for Sustainable Cloud Infrastructure](https://www.conf42.com/Rustlang_2025_Bandhavi_Sakhamuri_cloud_ai_rust) at Conf42 Rustlang 2025.
