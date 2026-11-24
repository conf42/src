# Quantum personalisation in banking starts with a customer data platform

Conf42 Blog, 2025-05-24, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-personalization-finance-starts-with-cdp

In short: JPMorganChase's Venkateswarlu Boggavarapu at Conf42 Quantum Computing 2025 on the data engineering under quantum-enhanced, real-time financial personalisation.

Before any qubit touches a bank's recommendation engine, someone has to resolve which of five customer records is the same person. Venkateswarlu Boggavarapu, Vice President and Senior Lead Data Engineer at JPMorganChase, made that the spine of his talk at Conf42 Quantum Computing 2025 on quantum AI-driven personalisation in financial services. The quantum layer sits on top; the customer data platform underneath does most of the work.

## Personalisation as a requirement, not a feature

Boggavarapu's opening argument is commercial: customers expect a bank to anticipate their goals, not just answer their questions. He cites machine learning approaches such as XGBoost and neural networks beating traditional segmentation, and a reference architecture with API-driven microservices serving 15-plus touchpoints in under 200 milliseconds, event processing at more than 50,000 transactions per second and a data lake of five petabytes or more. Those are the targets the rest of the talk designs for.

## The CDP is the central nervous system

The most practical section is the customer data platform. In his telling, a CDP does four jobs:

- **Aggregation**: structured and unstructured data from digital and physical touchpoints, through APIs and ETL.
- **A unified view**: a 360-degree profile built with entity resolution, persistent identifiers and cross-channel attribution.
- **Actionable insight**: recommendations and predictive scoring on top of that profile.
- **Compliance by design**: granular consent management, automated governance workflows and encryption, so GDPR and CCPA are built in, not bolted on.

He calls the CDP the central nervous system for customer data, and every later slide depends on it.

## Where the quantum part comes in

The quantum layer is pitched as pattern recognition across many variables at once. The talk describes a tensor-network architecture analysing hundreds of financial variables simultaneously, quantum annealing for portfolio optimisation and quantum-accelerated gradient descent for faster training. These are presented as capabilities rather than shown in a demo, so this is the part to watch critically.

Generative AI gets equal billing: tailored financial education content, chatbots built on retrieval-augmented generation over a financial knowledge base, and synthetic data generated with differential privacy so models can train without exposing personal data.

## The data engineering problems are the real ones

The section engineers will get the most from is the list of hard problems, all classical:

- **Latency**: memory-mapped databases with non-blocking IO, edge computing and predictive caching.
- **Volume**: auto-scaling microservices on Kubernetes, polyglot storage, stream processing.
- **Security**: post-quantum cryptographic algorithms, zero-knowledge proofs for identity checks and homomorphic encryption.
- **Governance**: graph-based metadata for automated lineage, attribute-based access control and immutable audit trails.

His roadmap is equally grounded: assess the existing data architecture, deploy the CDP and secure API connections, pilot with selected customer segments, then scale across products and channels. If your bank does only the first three steps, you still end up with a better platform, quantum or not.

The talk closes with outcome figures (engagement, conversion and satisfaction gains) presented as results of effective implementations; it doesn't detail the deployments behind them.

## Who should watch

Data engineers and architects at financial institutions planning real-time personalisation, and anyone who wants to see where quantum might plug into an existing data stack. If you came for quantum circuits, this isn't that talk; if you came for how a bank structures customer data, it is.

## Related Conf42 talks

- [Innovating FinTech with AI for financial solutions](https://www.conf42.com/Internet_of_Things_IoT_2024_Andrei_Alekseev_ai_fintech_financial) by Andrei Alekseev, the classical AI view of the same industry.
- [AI-driven insights for customer retention through personalisation](https://www.conf42.com/Incident_Management_2024_Anandakumar_Kumaravelu_4_ai_retention_personalization) by Anandakumar Kumaravelu, personalisation from the operations side.
- [Journey into quantum: getting started on business benefits](https://www.conf42.com/Quantum_Computing_2023_Daniel_Goldsmith_Pippa_Spencer_Williams_business_benefits) by Daniel Goldsmith and Pippa Spencer Williams, for scoping a first quantum project.

[Watch Venkateswarlu Boggavarapu's talk](https://www.conf42.com/Quantum_Computing_2025_Venkateswarlu_Boggavarapu_finance_optimization)

[Watch the talk on YouTube](https://youtu.be/pagMl4qnr9E).

## Watch the talk

[Quantum AI-Driven Personalization in Finance: Real-Time Data Engineering for Customers](https://www.conf42.com/Quantum_Computing_2025_Venkateswarlu_Boggavarapu_finance_optimization) at Conf42 Quantum Computing 2025.
