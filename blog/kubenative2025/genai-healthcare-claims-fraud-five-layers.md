# A five-layer GenAI pipeline for healthcare claims and fraud

Conf42 Blog, 2025-09-17, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/genai-healthcare-claims-fraud-five-layers

In short: Amala Umakanth (McKinsey & Company) at Conf42 Kube Native 2025 on GenAI claims processing, from ingestion and NLP to adjudication, explainability and fraud detection.

Healthcare claims fail in boring ways long before they fail in fraudulent ones: a missing document, an inconsistent code, a follow-up visit billed like a new diagnosis. At Conf42 Kube Native 2025, Amala Umakanth, a data engineer at McKinsey & Company, walked through a five-layer generative AI architecture for claims processing that targets both problems, faster and more accurate claims on one side and proactive fraud detection on the other.

She framed the scale first. Tens of millions of claims move daily through eligibility, coding, validation, adjudication and audit, and each layer adds room for error. She cited studies putting around 15% of claims as denied or delayed, and fraud such as upcoding, phantom billing and collusive provider networks costing the industry over a hundred billion dollars a year. Rule engines with fixed thresholds cannot keep up with patterns that keep changing.

## Clean data first, then understand it

Layer one is ingestion and preprocessing. Claims arrive as PDFs, HL7 messages and DICOM images, and the pipeline converts them into structured data with cleaning, deduplication and enrichment. Without that foundation, as she put it, no model delivers reliable outcomes.

Layer two is semantic understanding. NLP reads physician notes, discharge summaries and claim narratives, extracts diagnosis codes, procedures and medications, and builds context. Her example: telling a follow-up visit for diabetes apart from a new diabetes diagnosis, a subtle difference that changes billing accuracy.

## Validate, decide, and know when to ask a human

Layer three validates claims against ICD-10 and CPT coding standards, cross-checks medical necessity and provider credentials, and enriches each claim with labs and prior encounters. The aim is to fix bad claims before submission, not just reject them.

Layer four is AI-driven adjudication: approve, deny or flag, with reinforcement learning from expert feedback. Edge cases the system cannot decide confidently go to human reviewers. Layer five is orchestration, the control plane that ties models, external data and business rules together, compares AI summaries against source documents and keeps the audit trail regulators expect.

## Fraud moves, so the detector has to

The fraud section is the most interesting part. Static rules (flag claims over a dollar amount, duplicates within 30 days) are easy for fraudsters to step around. Umakanth described three evolving scheme types: pattern evolution, including GenAI-forged MRI scans and clinical notes; collusive networks, caught by mapping relationships between providers, patients and clinics, such as shared addresses or circular referrals; and behavioural anomalies, caught by baselining each provider and flagging sudden spikes in high-cost procedures.

She also proposed using generative models to simulate synthetic fraud scenarios, such as claims from fabricated identities, to stress-test the detection pipeline before attackers try them for real.

## The enterprise part is the hard part

Prototypes are quick; production is not. Her list of hurdles is honest: data silos across legacy systems, the need to explain why a claim was denied, and teams that need data and AI literacy to work with the pipeline. Compliance has to be built in: explainable decisions, federated learning across institutions, bias monitoring and alignment with HIPAA and GDPR.

## Who should watch

Data engineers and architects at payers, providers or insurance tech firms scoping where GenAI fits in a claims workflow. Despite the conference, the talk is light on Kubernetes specifics and heavy on the claims domain and the fraud taxonomy, which is where its value is.

## Related Conf42 talks

- [AI-Driven Claims Adjudication](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Uday_Bag_ai_driven_claims) by Uday Bag (Cognizant) covers the adjudication step in more depth.
- [AI-Powered Dental Claims Processing](https://www.conf42.com/Large_Language_Models_LLMs_2025_Pravesh_Nikhare_dental_claims_fraud) by Pravesh Nikhare (Delta Dental of California) brings the same problem to dental insurance.
- [Advancing Financial Fraud Detection with Graph Databases](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu (JPMorganChase) goes further on network-based fraud detection.

[Watch Amala Umakanth's talk](https://www.conf42.com/Kube_Native_2025_Amala_Umakanth_genai_healthcare_fraud)

[Watch the talk on YouTube](https://youtu.be/1mxcELRm-7k).

## Watch the talk

[GenAI in Healthcare Claims: Accelerating Processing and Detecting Fraud](https://www.conf42.com/Kube_Native_2025_Amala_Umakanth_genai_healthcare_fraud) at Conf42 Kube Native 2025.
