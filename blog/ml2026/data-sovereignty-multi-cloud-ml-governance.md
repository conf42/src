# Multi-cloud ML meets data sovereignty law, and governance has to adapt

Conf42 Blog, 2026-01-21, updated 2026-11-09. https://www.conf42.com/blog/ml2026/data-sovereignty-multi-cloud-ml-governance

In short: EY's Sapna Pillai at Conf42 Machine Learning 2026 on keeping multi-cloud ML compliant with GDPR, the CLOUD Act and data localisation rules.

Running machine learning across several clouds is the easy part now. Doing it while every jurisdiction tightens the rules on where data lives and who can reach it is harder. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Sapna Pillai of EY's Technology Consulting practice gave a compact tour of where governance breaks down in distributed, multi-cloud ML systems, and the four tools she reaches for to fix it: sovereign cloud zones, zero trust, compliance automation and unified cross-region governance.

It's a short talk and an overview, not a build-along. Its value is the map: which laws pull in which direction, which standards give you a shared vocabulary, and where in the ML lifecycle the gaps open up.

## Why multi-cloud makes compliance harder

Pillai starts with the case for multi-cloud ML: best-of-breed services, less vendor lock-in, better disaster recovery and the ability to shift resources with demand. The cost of that flexibility is governance complexity. Governments increasingly assert control over where data is stored, processed and accessed, especially when it crosses borders, and that collides with workloads designed to move freely.

She names three recurring problems. Keeping data residency lawful across several providers. Keeping full auditability of data movement when lineage spans clouds. And staying consistent when the laws themselves disagree.

## Three laws that pull in different directions

The examples are the ones that keep architects awake. GDPR sets strict data protection standards in the EU and has shaped governance practice well beyond it. The US CLOUD Act lets law enforcement reach data held by US-based companies even when that data is stored overseas. China's Cybersecurity Law imposes strong localisation and cross-border transfer requirements. Put a training pipeline, a feature store and an inference endpoint in three regions and you can trip over all three.

For a common language across platforms she points to ISO 27018 for personal data in public clouds, the Cloud Security Alliance STAR programme for evaluating and certifying cloud controls, and NIST 800-53 for security and privacy controls in regulated and government-aligned systems.

## Visibility first, then controls

The gap she keeps returning to is visibility. Many organisations can't say how data moves between providers, and without that, unauthorised access, accidental cross-border transfers and failed audits become likely. Her toolkit, in order:

- **Sovereign cloud zones** keep storage and processing inside a jurisdiction while still giving you cloud scale, and they help with trust from local customers and partners.
- **Zero trust** assumes no implicit trust and verifies every access request, so data stays protected as it moves across clouds and regions, with least-privilege access throughout.
- **Compliance automation** covers real-time monitoring of regulatory requirements, consistent policy enforcement across providers and automatically generated audit trails, because manual compliance doesn't scale across clouds.
- **Cross-region ML governance** means one framework for residency, access and security from training to inference to retraining, not a separate patchwork per region.

Her balancing rule is worth pinning above the architecture board: "Compliance should enable the business not slow it down." Governance has to bend with new regulations instead of freezing the platform.

## Who should watch

Platform and ML engineers who have just been told the next model must serve EU and US customers from shared infrastructure, and architects who need a quick refresher on which regulations and standards matter before a design review. If you already run sovereign regions in production, this one will mostly confirm your checklist.

## Related Conf42 talks

- [GDPR and beyond: demystifying data governance challenges](https://www.conf42.com/Machine_Learning_2024_Antonio_Murgia_Francesco_Valentini_gdpr_beyond_data), Antonio Murgia and Francesco Valentini (Agile Lab), Conf42 Machine Learning 2024
- [Designing a scalable data governance framework for multi-tenant cloud contract management](https://www.conf42.com/Machine_Learning_2025_Kushal_Shah_governance_framework_cloud), Kushal Shah, Conf42 Machine Learning 2025
- [AI for autonomous threat defense in multi-cloud security](https://www.conf42.com/Machine_Learning_2025_Pradeep_Kurra_threat_defense_autonomous), Pradeep Kurra (Trace3), Conf42 Machine Learning 2025

[Watch Sapna Pillai's talk](https://www.conf42.com/Machine_Learning_2026_Sapna_Pillai_search_semantic_retrieval)

[Watch the talk on YouTube](https://youtu.be/DU5LXy2xqAw).

## Watch the talk

[Governing Data Sovereignty in Distributed Multi-Cloud Machine Learning Systems](https://www.conf42.com/Machine_Learning_2026_Sapna_Pillai_search_semantic_retrieval) at Conf42 Machine Learning 2026.
