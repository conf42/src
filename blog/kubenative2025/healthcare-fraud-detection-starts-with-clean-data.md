# Healthcare fraud detection fails on data before it fails on models

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/healthcare-fraud-detection-starts-with-clean-data

In short: Triveni Kolla (Cotiviti) at Conf42 Kube Native 2025 makes the case for data-centric AI in healthcare fraud detection: clean, governed data first.

A provider bills two insurers for the same service under slightly different patient details, and the duplicate slips through because the identifiers don't match. At Conf42 Kube Native 2025, Triveni Kolla, Senior Business Intelligence Developer at Cotiviti, used scenarios like that to argue that healthcare fraud detection is a data quality problem first. Bigger models on messy claims data hit diminishing returns; governed, clean data is what lets AI deliver.

The talk is a strategy overview from someone with a decade in healthcare data warehousing and BI. It is not a code walkthrough.

## The scale of the problem

Triveni opens with the size of it. She cites estimates of around $300 billion a year lost to healthcare fraud in the US, up to 10% of total healthcare spending, with roughly three quarters of healthcare data unstructured and, in the figure she quotes, four out of five medical bills containing errors. Those errors are not all fraud, but they are all places fraud can hide.

## Model-centric versus data-centric

The central slide contrasts two approaches. The traditional, model-centric one treats data as a fixed input and keeps refining algorithms and adding complexity. The data-centric one treats data quality as the main lever: systematic governance, continuous quality monitoring and proactive enrichment.

Her three failure scenarios make it concrete:

- a duplicate bill missed because patient identifiers are inconsistent across systems
- a model trained on incomplete records that produces skewed risk scores
- a telehealth session billed while the patient record is incomplete, so the fraud goes unnoticed

The line most engineers will nod at: a well-labelled, high-quality dataset can let a simple logistic regression beat a deep neural network trained on messy or biased data. The abstract puts numbers on the payoff, crediting clean, governed datasets with detection accuracy up to 95%, 85% fewer false positives and 70% shorter investigations.

## Data as a living asset

Her continuous quality framework has four steps that loop: profile and assess every source, define quantifiable standards for completeness, accuracy, consistency and timeliness, monitor in real time so deviations are caught before they reach a model, and feed model outcomes back into the quality process.

On the modelling side she favours random forests for this domain, for pattern recognition across many decision trees and, importantly in healthcare, interpretability that survives regulatory review and audit. Other ideas in the toolkit: blockchain-style immutable audit trails for data integrity, and AutoML pipelines that automate preprocessing and model selection for teams without deep in-house ML expertise.

## Where cloud-native fits

The Kubernetes Native angle is the platform under all of this. Elastic scaling lets fraud workloads grow from routine monitoring to an investigation surge. Integration happens through standard healthcare interoperability, FHIR and HL7 messaging, with electronic health records, claims and health information systems. Security and compliance (HIPAA, GDPR) are built into the platform instead of patched on.

Her roadmap is staged: assessment and data audit in the first months, then data quality improvement and governance, then a pilot across key fraud scenarios, then full deployment with continuous monitoring. The KPIs pair financial measures (fraud losses, recoveries, investigation cost) with operational ones (accuracy, false positive rate, investigation cycle time).

## Who should watch

Data engineers and BI teams in healthcare payers and claims processing, and ML engineers who keep getting asked for a better model when the data is the problem. If you need the argument for funding data governance before the next model, Triveni has made it for you.

## Related Conf42 talks

- [AI-Powered Fraud Detection in Cloud-Native Financial Systems](https://www.conf42.com/Cloud_Native_2025_Sandeep_Jarugula_fraud_detection_analytics_security) brings the same problem to payments.
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) gets hands-on with the checks.
- [Beyond Compliance: Architecting Secure Distributed Healthcare Systems](https://www.conf42.com/Machine_Learning_2025_Sachin_Telalwar_compliance_healthcare) covers the compliance-heavy platform side.

[Watch Triveni Kolla's talk](https://www.conf42.com/Kube_Native_2025_Triveni_Kolla_healthcare_fraud_data)

[Watch the talk on YouTube](https://youtu.be/ZU-Uy8biZ6k).

## Watch the talk

[AI-Ready Healthcare Data: Revolutionizing Fraud Detection with Scalable, Data-Centric Intelligence](https://www.conf42.com/Kube_Native_2025_Triveni_Kolla_healthcare_fraud_data) at Conf42 Kube Native 2025.
