# Users ignore AI they cannot inspect, so build trust into the stack

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/trust-is-architecture-transparent-ai-kubernetes

In short: Raj Kommera (ON24) at Conf42 Kube Native 2025 on five design pillars for trustworthy AI, from contextual confidence scores to OpenTelemetry audit trails.

An accurate model that nobody trusts has the same business value as no model at all. At Conf42 Kube Native 2025, Raj Kommera, Senior Engineer at ON24, presented what he calls Kube-Native Trust: five architectural pillars that make AI recommendations inspectable, and a mapping of each pillar onto tools Kubernetes teams already run.

The pattern he keeps seeing in enterprises is that users quietly ignore AI recommendations because they cannot scrutinise the logic, trace the data or judge how certain the model is. Millions get invested, and the tool ends up sidelined. His diagnosis: the real problem is transparency, not prediction.

## Why enterprise AI gets sidelined

Kommera named four causes. Models act like black boxes. They ignore business context like regulatory limits, budget thresholds and workflow quirks. Observability is too thin to trace an input to a prediction, so nobody can audit or debug it. And there is a trust gap between the engineers who build the model, the data scientists who tune it and the business users who are supposed to act on it. His fix is to treat trust as a first-class architectural concern.

## Five pillars, each one buildable

**Contextualised confidence scoring.** Instead of one flat percentage, tell users how confident the model is for this specific context, how this prediction compares with similar past cases, and how to read the score.

**Source traceability.** For any recommendation, answer which data was used, how it was processed, which features mattered and which business rules were applied. He likened it to turning on version history for every decision.

**Adaptive thresholds.** A static "act above 70%" rule is naive. Thresholds should move with use-case criticality, operational constraints and risk tolerance; a 60% confident prediction may be fine for marketing and unacceptable in healthcare.

**Progressive disclosure in the UI.** Level one is a summary and a confidence score, level two adds key drivers and alternatives, level three shows full lineage, parameters and feature importance. Users pick their depth.

**End-to-end audit trails.** Immutable logs of what was predicted, why and when, with OpenTelemetry integration, captured human feedback, outcome validation and compliance-ready reports.

## Mapping it to Kubernetes tools

The implementation blueprint reuses the platform you probably already have. A service mesh such as Istio or Linkerd captures model traffic, latency and request traces. GitOps with Argo CD or Flux version-controls models, so you can answer which version made which call. OpenTelemetry gives unified tracing from infrastructure up to business outcome. A policy layer enforces governance and adaptive thresholds and secures the pipeline. In his reference architecture, confidence scoring runs as its own microservice, thresholds are policy-driven, the UI exposes layered explanations and everything from prediction to outcome is logged.

His examples cover customer segmentation (why a user falls into a segment), lead routing (why a lead was prioritised), clinical patient risk scoring and infrastructure scaling decisions that show cost context.

## Who should watch

Engineers building AI features into enterprise products who keep hearing that users do not adopt them, and platform teams asked to make models auditable. It is a short framework talk; the starter checklist at the end (audit transparency gaps, add confidence scoring to one model, start tracing with OpenTelemetry, add feedback loops to the UI) is the part to steal.

## Related Conf42 talks

- [I Don't Trust AI Agents (And Neither Should You)](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis (AWS) brings the trust question to agent architectures.
- [Beyond Algorithms: Building Trust in AI-Enhanced Public Sector Systems](https://www.conf42.com/Machine_Learning_2025_Sanjiv_Kumar_Bhagat_algorithms_trust_sector) by Sanjiv Kumar Bhagat looks at transparency where the users are citizens.
- [The AI Trust Triad for DevOps](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) by Saideepak Kandibanda (DISH Network) adds explanation drift monitoring to the pipeline.

[Watch Raj Kommera's talk](https://www.conf42.com/Kube_Native_2025_Raj_Kommera_trust_transparency_cloudnative)

[Watch the talk on YouTube](https://youtu.be/c2KkOjuUf4E).

## Watch the talk

[Kube-Native Trust: Architecting Transparent AI Systems for Cloud-Native Environments](https://www.conf42.com/Kube_Native_2025_Raj_Kommera_trust_transparency_cloudnative) at Conf42 Kube Native 2025.
