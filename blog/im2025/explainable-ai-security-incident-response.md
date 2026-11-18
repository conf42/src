# If your AI triages the breach, it has to show its working

Conf42 Blog, 2025-09-07, updated 2026-11-09. https://www.conf42.com/blog/im2025/explainable-ai-security-incident-response

In short: Vasanth Mudavatu (Dell Technologies) at Conf42 Incident Management 2025 on four pillars that make AI-driven security incident response explainable and auditable.

An AI system that flags an intrusion and can't say why is a pager with opinions. At Conf42 Incident Management 2025, Vasanth Mudavatu, Senior Principal Software Engineer for Gen AI, ML and Application Security Products at Dell Technologies, argued that once AI makes split-second calls in security operations, transparency stops being a compliance checkbox and becomes part of how fast you can respond. He offered a four-pillar framework for getting there.

The talk sits on the security side of incident management: breaches, threat validation, forensics and regulators, rather than latency spikes.

## Opacity costs you time at the worst moment

Mudavatu gives three reasons transparency is non-negotiable. Threats are evolving fast, so defenders need AI they can verify. Regulators in sectors like financial services increasingly require explainable decisions rather than suggesting them. And in the middle of an incident, a black-box recommendation creates hesitation: the analyst stops to second-guess the model, and a small anomaly gets time to become an organisational crisis.

That last point is the useful reframe. We usually talk about explainability as a governance cost. Here it is a speed feature.

## Four pillars

**Explainability, at three levels.** An executive summary for leaders with the high-level risk, analyst detail covering feature importance and the specific decision pathway, and a technical view of model weights and algorithmic logic for the people who own the model. Same decision, three audiences.

**Accountability.** Granular attribution, meaning you can point to the exact inputs, model components and pathways behind each decision. Oversight, giving human operators real-time insight and escalation protocols so they can step in when model confidence drops. And a tamper-proof record of inputs, outputs and human interventions that works as a chain of custody.

**Bias mitigation.** Curate representative training data so the model doesn't have blind spots, monitor live models for emerging bias, and validate threat assessments with objective fairness metrics. In security, bias shows up as threats you never see plus false positives you can't stop seeing.

**Auditability.** Trace each decision from input to recommendation so you can reconstruct why something was flagged, or missed. Version every model so you can roll back when an update raises false positives or opens a gap. Generate compliance reports automatically from decision traces and version history, so post-incident reviews start with evidence instead of archaeology.

## Where it pays off

His examples are critical infrastructure: power grid operators validating network anomalies faster, explainable models catching subtle malicious control patterns in water treatment SCADA systems, and transit security teams coordinating better because everyone can see the AI's reasoning.

He also takes on the objections. Worried that explanations leak proprietary models? Use layered explanations that give insight without exposing IP. Worried that interpretable models detect less? Pair a high-performance model with a dedicated interpretability module. Worried the transparent model goes stale? Run continuous learning while keeping the explanations intact.

Success is measured in faster triage, higher analyst confidence in recommendations, better cross-team coordination and fewer false positives.

## Who should watch

Security engineers and SOC leads evaluating AI triage tools, and anyone writing the procurement checklist for one. It is a framework talk with no tooling demo, so use it to sharpen the questions you put to a vendor: can it show the decision pathway, can it roll back a model, and can it produce the audit trail without a week of log-diving?

## Related Conf42 talks

- [The AI Trust Triad for DevOps](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) by Saideepak Kandibanda covers explainable AI in regulated delivery pipelines.
- [Kube-Native Trust: Architecting Transparent AI Systems](https://www.conf42.com/Kube_Native_2025_Raj_Kommera_trust_transparency_cloudnative) by Raj Kommera takes the same question to cloud-native platforms.
- [Enhancing Healthcare Chatbot Transparency with Explainable AI](https://www.conf42.com/DevSecOps_2024_Abhishek_Vajpayee_Rathish_Mohan_healthcare_chatbot_transparency) by Abhishek Vajpayee and Rathish Mohan applies XAI where security and ethics collide.

[Watch Vasanth Mudavatu's talk](https://www.conf42.com/Incident_Management_2025_Vasanth_Mudavatu_transparency_algorithms_ai)

[Watch the talk on YouTube](https://youtu.be/yZW-FjoXOqQ).

## Watch the talk

[Algorithmic Transparency in Action: Strengthening AI-Driven Incident Management](https://www.conf42.com/Incident_Management_2025_Vasanth_Mudavatu_transparency_algorithms_ai) at Conf42 Incident Management 2025.
