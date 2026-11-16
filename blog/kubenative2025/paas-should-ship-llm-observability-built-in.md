# Platforms should ship LLM-powered observability built in

Conf42 Blog, 2025-10-12, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/paas-should-ship-llm-observability-built-in

In short: Srinivas Pagadala Sekar of Karsun Solutions argues at Conf42 Kube Native 2025 that PaaS providers should offer LLM-driven diagnostics as a native service.

A dashboard that says "latency is high" during an outage is a smoke alarm with no map of the building. At Conf42 Kube Native 2025, Srinivas Pagadala Sekar, Senior Site Reliability Manager at Karsun Solutions, made the case that platform-as-a-service providers should ship LLM-driven observability as part of the platform, so every tenant gets correlated, explained incidents without building their own AI stack.

It is a framework talk drawn from 14 years in cloud and SRE work: the argument, the implementation steps and, usefully, how to prove it works before you roll it out.

## Alerts without context slow recovery

Sekar's starting point will be familiar to anyone on call. Microservices on a PaaS fail in tangled ways: one service falters, a cascade follows, and the SRE team gets a flood of alarms with no correlation. Pods scale in and out within seconds and IPs change, so yesterday's troubleshooting assumptions stop holding. He walks through examples from fintech trading, healthcare records and e-commerce on a busy sale day to show how small changes ripple.

Observability grew from CPU graphs to the three pillars of metrics, logs and traces, but those still need a human to stitch them together. His claim is that LLMs can do the stitching: link a recent deployment, a memory spike in one service and an odd error pattern in another, then suggest the rollback or scale-up.

## Start with the alerts you already have

The implementation path is incremental. Feed existing monitoring signals to the model and enrich them with context so alerts read like narratives. Fine-tune on your own telemetry, deployment history and failure patterns. Add predictive checks for failing nodes and bottlenecks. Give engineers a chat interface to ask why latency is spiking. Correlate apparently unrelated signals (API errors, pod churn, config changes) before they cascade.

The technical framework below that is plain engineering: ingest and normalise metrics, logs, traces and CI/CD events; pick and tune models for platform workloads; keep inference latency low; deliver different outputs to SREs, developers and managers; and expose it all through APIs and the platform console. He also suggests storing cleaned telemetry in vector databases as the baseline the model works from.

## Prove it before you scale it

The section worth the watch is the evaluation method. Build a staging environment that mimics production, multi-tenant Kubernetes and service mesh included, then inject pod crashes, cascading degradation and traffic surges. Run your current stack and the LLM-enhanced one through the same failures. Measure MTTD, MTTR, false positives and root-cause accuracy. Survey the SREs on alert clarity and trust. Then apply statistical tests, A/B comparisons and effect sizes so the improvement isn't one lucky incident. That is the bar more AIOps pitches should clear.

He pairs it with guardrails: collect only the telemetry you need, anonymise, comply with HIPAA and GDPR, keep critical remediation human-verified, and make outputs explainable so engineers trust them.

## Who should watch

Platform teams running a multi-tenant PaaS, and SRE leads evaluating AI-assisted incident tooling who want a way to test vendor claims. If you want a demo of a specific product, this talk doesn't name one.

## Related talks

- Birol Yildiz on the noise half of the problem: [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise).
- Nishanth Vepachedu takes it agentic in [Scaling Microservices Observability with Agentic LLMs](https://www.conf42.com/MLOps_2026_Nishanth_Vepachedu_microservices_observability_llms).
- When the telemetry itself misleads: David McNerney and Daniel Raskin in [When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems).

[Watch Srinivas Pagadala Sekar's talk](https://www.conf42.com/Kube_Native_2025_Srinivas_Pagadala_Sekar_observability_llms_paas)

[Watch the talk on YouTube](https://youtu.be/ob-8Hqga7so).

## Watch the talk

[AI-Powered Observability with LLMs: Accelerating Resilience in Cloud-Native PaaS Architectures](https://www.conf42.com/Kube_Native_2025_Srinivas_Pagadala_Sekar_observability_llms_paas) at Conf42 Kube Native 2025.
