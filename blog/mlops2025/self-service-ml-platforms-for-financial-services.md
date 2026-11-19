# Self-service ML platforms work when governance is built in first

Conf42 Blog, 2025-08-28, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/self-service-ml-platforms-for-financial-services

In short: Rajeev Chevuri (Freddie Mac) at Conf42 MLOps 2025 on self-service ML platforms for financial services, with governance designed into every layer.

Data scientists want to ship models without filing tickets, and regulators want to know who approved every model and which data trained it. Rajeev Chevuri, a senior cloud DevOps engineer on Freddie Mac's enterprise data science platform, argues at Conf42 MLOps 2025 that a self-service ML platform can satisfy both, as long as governance is designed in from the start rather than bolted on later.

It is an architecture talk aimed at banks and other regulated institutions, with a build-versus-buy section and a 90-day roadmap at the end.

## From laptop experiments to platforms

Rajeev describes the usual maturity path in financial services. Teams start with siloed experiments: models built in isolation with no path to production, manual and error-prone deployments, and results nobody can reproduce, because what worked on one laptop fails in production. Governance is ad hoc. Integrated platforms that cover the whole ML lifecycle bring consistency, automation and auditability, and he credits them with big reductions in data preparation time and training cost and better deployment success rates.

## Three layers and four pillars

His reference architecture has three layers. The foundation is infrastructure: scalable CPUs and GPUs, resilient storage and secure networking, with Kubernetes doing the standardising whether you run in the cloud, on-premises or hybrid. Above it sits data and feature management: ingestion, validation, versioning and a feature store for consistency and reuse, all auditable. On top is ML lifecycle management: experimentation, training, versioning, deployment and monitoring.

Four components carry the weight. Container orchestration schedules ML workloads as custom resources so they run the same everywhere, with isolation between tenants. Distributed compute with Spark and Dask handles large data with lineage tracking, so every transformation can be traced. A model registry stores models with compliance metadata (who trained them, on what data, when) and cryptographic checks so nothing tampered goes live. CI/CD gates deployments behind tests, security scans and approvals.

## Governance is a layer, not a review meeting

The governance layer has three parts. Automated policy enforcement applies access controls and security at runtime, so a misconfiguration by a data scientist does not become a compliance incident. Compliance documentation, including model cards, lineage diagrams and validation reports, is generated automatically as evidence instead of written by hand. Audit observability captures logs, monitoring data and explainability outputs, so when a regulator asks why a model made a decision, the answer is already there.

For developers, the experience is curated environments with pre-approved packages, templates for consistency, and one-click deployment to staging with compliance checks and monitoring wired in.

## Build, buy or both

Rajeev's build-versus-buy comparison is useful for planning. Building in-house gives full customisation and legacy integration but typically takes 12 to 18 months and a specialised team. Commercial platforms deliver in three to six months with compliance features built in, at the price of vendor lock-in. A hybrid (vendor core plus your own governance and integrations) lands in six to nine months, and he sees it as the best balance for most financial organisations.

He closes with what is next, including edge inference, enterprise AutoML with explainability built in, serverless training and privacy-preserving ML with federated learning. His 90-day roadmap is practical: audit current ML workflows and compliance gaps, design requirements with both technical and regulatory teams, prototype with a small team, and deliver a minimum viable platform focused on the highest-friction areas, measured by deployment time and user satisfaction.

## Who should watch

Platform engineers and ML infrastructure leads in banking, insurance or any audited industry, and anyone writing the business case for an internal ML platform. If you already run one, the governance layer and build-buy numbers make a good checklist.

## Related Conf42 talks

- [George Hantzaras and Dan McKean (MongoDB) on building a self-service DBaaS for an internal developer platform](https://www.conf42.com/Cloud_Native_2023_George_Hantzaras_Dan_Mckean_self_service_dbaas_internal_developer_platform) at Conf42 Cloud Native 2023.
- [Batchu Krishna (Fidelity Investments) on self-service data platforms](https://www.conf42.com/Platform_Engineering_2025_Batchu_Krishna_etl_service_experience) at Conf42 Platform Engineering 2025.
- [Zhiya Zang (TikTok) on an affordable ML platform](https://www.conf42.com/Machine_Learning_2024_Zhiya_Zang_affordable_platform) at Conf42 Machine Learning 2024.

[Watch Rajeev Chevuri's talk](https://www.conf42.com/MLOps_2025_Rajeev_Chevuri_scaling_mlops_self) for the full architecture.

[Watch the talk on YouTube](https://youtu.be/4U1PCM8oYBw).

## Watch the talk

[Scaling MLOps with Self-Service Platforms: Architectures for Automation, Governance, and Velocity](https://www.conf42.com/MLOps_2025_Rajeev_Chevuri_scaling_mlops_self) at Conf42 MLOps 2025.
