# Banks should run AI governance as microservices next to the models

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/run-ai-governance-as-microservices-in-banking

In short: Ashish Dibouliya (Webster Bank) at Conf42 Kube Native 2025 on a Kubernetes-native framework for AI metadata, lineage, drift and regulatory compliance.

Governance built for a static data warehouse cannot keep up with fraud models that retrain continuously and run on containers that come and go by the minute. Ashish Dibouliya, Managing Director of Data Architecture at Webster Bank, used his Conf42 Kube Native 2025 talk to propose the fix: deploy governance itself as cloud-native microservices on Kubernetes, so it scales and moves at the same speed as the AI it watches.

It is an architecture talk with a case study at the end, pitched at the people who have to satisfy both the innovation team and the regulator.

## Containers made AI fast and governance blind

Ashish describes the dual pressure every bank feels: compliance failures cost money and reputation, while the business wants AI shipped quickly. Kubernetes gave AI workloads hybrid-cloud deployment, dynamic scaling and blue-green or canary updates. It also brought dynamic service meshes, distributed clusters and short-lived workloads that traditional monitoring and governance tools struggle to follow.

He lists four places the old model breaks: metadata (AI produces huge volumes of it, constantly changing), lineage (tracing where each model feature came from is nearly impossible at scale), real-time compliance (regulators expect continuous monitoring of bias, drift and quality), and regulatory complexity (explainable, fair AI as a standing obligation rather than a one-time box to tick).

## Three services do the governing

His unified AI data governance framework runs as microservices integrated with Kubernetes orchestration, built from three components:

- A **metadata orchestration engine**, the central nervous system, managing thousands of metadata events per second.
- An **intelligent lineage tracker**, using graph algorithms and instrumentation to trace dependencies across distributed AI systems.
- A **real-time compliance monitor**, checking AI decisions against internal policy and regulation as they happen.

The metadata layer has to be fast to be useful: relational and graph stores for different query types, hot data in memory, indexes for time-based, graph and full-text queries, and federation so you can query across sources without centralising everything.

## Drift and bias checks run all the time

The automation layer watches for data, concept and performance drift, checks fairness across demographic groups for protected attributes, and uses unsupervised ML for anomaly detection in models and data. Security is defence in depth: integration with enterprise IAM, attribute-based access control for fine-grained permissions, every governance operation logged with full context, and encryption including field-level encryption and tokenisation.

## Mapped to the rules banks actually face

The regulatory mapping is concrete. For GDPR, consent tracking and the right to be forgotten, which means finding every model trained on a given person's data. For CCPA, automated consumer-rights requests and data-sharing tracking. For Basel III, risk model validation tracking and stress testing. And it anticipates the EU AI Act by classifying AI systems by risk level and applying matching controls.

## The case study numbers

A global tier-one bank rolled the framework out in phases, starting with fraud detection, credit risk and regulatory reporting. Ashish reported 68% faster time to market for new AI models, roughly 75% less audit preparation time through automated reporting, and 42% fewer risk events thanks to earlier detection. His reading: good governance speeds innovation up rather than slowing it down.

The roadmap adds serverless compliance functions triggered by events, policies deployed alongside workloads, human-readable explanations of AI decisions, and federated governance across clouds and organisations.

## Who should watch

Data architects, AI platform owners and risk or compliance leads in banking, plus anyone who has been asked to list every model trained on one customer's data and could not.

## Related Conf42 talks

- [Simplifying Kafka Governance for Developers](https://www.conf42.com/DevSecOps_2023_Muralidhar_Basani_simplifying_kafka_governance) by Muralidhar Basani (Aiven), governance for the event streams these models feed on.
- [Designing a Scalable Data Governance Framework for Multi-Tenant Cloud Contract Management](https://www.conf42.com/Machine_Learning_2025_Kushal_Shah_governance_framework_cloud) by Kushal Shah, another framework built for scale.
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu (Church Mutual Insurance Company), the data-quality half of the problem.

[Watch Ashish Dibouliya's talk](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance)

[Watch the talk on YouTube](https://youtu.be/bskB5_8MpWI).

## Watch the talk

[Kube-Native AI Data Governance for Scalable Compliance in Modern Banking](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance) at Conf42 Kube Native 2025.
