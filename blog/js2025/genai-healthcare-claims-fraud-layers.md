# A five-layer blueprint for generative AI in healthcare claims

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/genai-healthcare-claims-fraud-layers

In short: Amala Arul Malar Umakanth of McKinsey & Company at Conf42 JavaScript 2025 on layered GenAI for claims processing and multimodal fraud detection.

Static fraud rules, such as flagging any claim above a dollar threshold or any duplicate within 30 days, are easy to write and just as easy to dodge. At Conf42 JavaScript 2025, Amala Arul Malar Umakanth, a principal data engineer at McKinsey & Company, laid out how generative AI can sit inside healthcare insurance workflows, from reading clinical notes to spotting fraud rings, and what has to be true about the data first.

Fair warning for the JavaScript crowd: this is an architecture and strategy talk about healthcare data, not a code walkthrough. Its value is the structure it puts around a messy domain.

## The problem is volume and fragmentation

Amala frames the starting point plainly. Tens of millions of claims move through payers and providers every day, and much of the review is still manual: people reading notes and checking codes line by line. The data lives in PDFs, portals, EHR systems, HL7 messages and DICOM images that don't talk to each other, and fraud detection relies on rigid rules that evolve slower than the fraudsters.

## Five layers, bottom up

Her blueprint stacks five layers:

- **Ingestion and pre-processing.** Pull every format in, then clean, deduplicate and enrich it into structured data. No model rescues dirty inputs.
- **Clinical language understanding.** NLP extracts diagnoses, procedures and medications from physician notes and discharge summaries, and builds context. Her example: telling a follow-up visit for diabetes from a new diabetes diagnosis, a distinction that changes billing.
- **Validation.** Check correctness against medical standards, with the goal of improving claim quality before submission rather than rejecting bad claims after.
- **Risk detection**, where the fraud models live.
- **Orchestration.** High-confidence claims auto-approve; questionable ones escalate to people, so human judgement goes where it is needed.

## Fraud detection gets several lenses at once

The fraud section is the most concrete. Instead of single rules, she describes multimodal analysis that combines structured claim data, narratives and behaviour:

- Graph neural networks map relationships between claims, patients, providers and transactions, so a provider unusually connected to clusters of questionable claims stands out. Her description: a social network for claims data.
- Temporal pattern analysis watches for odd timing, such as charges at strange hours or bursts of identical procedures.
- Document authenticity checks look for tampering or forgery in invoices and paperwork.
- Anomaly scoring combines the signals and ranks claims, so investigators start with the truly suspicious ones instead of drowning in false alarms.

Her favourite idea is synthetic fraud scenario generation: use generative models to invent fraud patterns that haven't happened yet and stress-test the detection pipeline before a new tactic reaches production.

## Responsible AI and a phased rollout

She treats trust as a prerequisite: keep PHI private, explain decisions about denials and fraud alerts, monitor for bias, and meet HIPAA and audit requirements. The adoption hurdles she lists are data silos, model drift (models need retraining as diseases, regulations and populations change, which means a real MLOps practice) and workforce resistance.

The roadmap has four phases: foundation (secure pipelines, NLP models, validation rules), development (fraud models run in shadow mode alongside existing systems, with explainability tools for adjusters and A/B testing), integration (connect to core platforms, automate routing, add dashboards) and optimisation (continuous learning, more claim types, synthetic fraud generation, federated learning). Start small, show value, then grow.

## Who should watch

Data engineers and architects at payers or health-tech vendors, and anyone asked to put AI into claims without a clear picture of the pipeline it needs. Engineers looking for JavaScript, model code or measured results from a specific deployment will not find them here.

## Related Conf42 talks

- [Triveni Kolla of Cotiviti on AI-ready healthcare data for fraud detection](https://www.conf42.com/Kube_Native_2025_Triveni_Kolla_healthcare_fraud_data) at Conf42 Kube Native 2025.
- [Pravesh Nikhare of Delta Dental on AI-powered dental claims processing](https://www.conf42.com/Large_Language_Models_LLMs_2025_Pravesh_Nikhare_dental_claims_fraud) at Conf42 LLMs 2025.
- [Praveen Kumar of AllianzLife on AI and ML for claims processing](https://www.conf42.com/JavaScript_2024_Praveen_Kumar_50_ai_claimsprocessing) at Conf42 JavaScript 2024.

[Watch Amala Arul Malar Umakanth's talk](https://www.conf42.com/JavaScript_2025_Amala_Arul_Malar_Umakanth_clamis_fraud_healthcare), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/xX9mWwYbKP0).

## Watch the talk

[Generative AI for Claims and Fraud: Reshaping Healthcare Insurance Workflows](https://www.conf42.com/JavaScript_2025_Amala_Arul_Malar_Umakanth_clamis_fraud_healthcare) at Conf42 JavaScript 2025.
