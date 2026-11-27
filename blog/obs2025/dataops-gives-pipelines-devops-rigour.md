# DataOps treats data pipelines with the rigour of code deploys

Conf42 Blog, 2025-06-05. https://www.conf42.com/blog/obs2025/dataops-gives-pipelines-devops-rigour

In short: Lakshmi Narayana Gupta Koralla of Starbucks at Conf42 Observability 2025 on DataOps principles, governance as code, data CI/CD and observability for pipelines.

DataOps takes the habits that made DevOps work, automation, CI/CD, version control and monitoring, and applies them to data pipelines. At Conf42 Observability 2025, Lakshmi Narayana Gupta Koralla, Senior Data Engineer at Starbucks with 14 years in IT, gave a broad survey of the methodology: where it came from, its core principles, the architecture components and how to measure whether it is working.

It is a wide-angle overview rather than a walkthrough of one Starbucks pipeline. Treat it as a syllabus: each section names the tools and patterns to go and read about.

## Where DataOps came from

Koralla traces the line from centralised data warehouses with rigid ETL, through the big data era that added volume and complexity, to DataOps emerging around 2015 as practitioners borrowed from software engineering. The old model had siloed teams, manual handoffs and data projects that ran for months or years. The new one asks why a schema change should be harder to ship than an API change.

## Four principles

The conceptual core is four principles. Automation and orchestration across the data lifecycle, with dependencies and sequencing managed explicitly. CI/CD for data, so changes are integrated, tested for validity and impact, and deployed through standard processes. Version control and reproducibility for transformation logic and models, so any previous state can be recreated. And quality by design, with validation built into pipelines so anomalies are caught before downstream consumers see them.

## The architecture, component by component

This is the most useful part for practitioners. Monitoring and observability for data covers quality, lineage, performance and business alignment, often with statistical baselines to detect anomalies, and in mature teams as observability as code so monitoring evolves with the pipelines. Governance as code means policies are codified, versioned and enforced inside pipelines, with a federated model where a central team sets frameworks and domain teams own their rules.

For data CI/CD he points to blue-green and canary releases for pipelines and the expand-contract pattern for non-breaking schema changes. The automation layer is the familiar stack: Docker for consistent environments, Apache Airflow, Prefect and Dagster for workflows as code, dbt for transformations, Kafka and Flink for streaming. On organisation, he mentions data mesh, DataOps centres of excellence, data product teams and guilds, all relying on clear ownership and SLAs between producers and consumers.

## Measuring it, and rolling it out

Koralla proposes four measurement areas: pipeline performance, data quality, time to insight and resource utilisation, and a maturity model running from ad hoc at level one to optimised at level five. The rollout runs through assessment, pilot, expansion and maturity phases, starting with a high-value use case that produces proof points for stakeholders. He is clear that executive sponsorship matters because DataOps is a business initiative, not just a technical project, and that legacy integration, skills gaps and cultural resistance are the usual blockers.

## Beyond the basics

The later sections cover the frontier: the overlap with MLOps (feature stores, drift detection, explainability that traces predictions back to data transformations), store-and-forward patterns for edge data, Lambda and Kappa architectures for streaming, and privacy by design with data minimisation, dynamic masking and jurisdiction-aware routing. He also lists emerging trends such as declarative pipelines, data contracts between producers and consumers, and self-healing pipelines.

## Who should watch

Data engineers and platform teams building a DataOps practice from scratch, and engineering managers who need a structured overview to plan against. If you already run dbt with CI and data contracts, you will mostly be nodding along, though the governance-as-code section is a good checklist.

## Related Conf42 talks

- [DevOps best practices for DataOps Mesh](https://www.conf42.com/DevOps_2023_Agita_Jaunzeme_best_practices_dataops_mesh) by Agita Jaunzeme at Conf42 DevOps 2023.
- [Bring your DataOps to the Data Lakehouse](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) by Jorge Loaiciga Rodriguez at Conf42 DevOps 2025.
- [DataOps as a Service](https://www.conf42.com/DevOps_2023_Antoni_Ivanov_dataops_aas) by Antoni Ivanov at Conf42 DevOps 2023.

[Watch Lakshmi Narayana Gupta Koralla's talk](https://www.conf42.com/Observability_2025_Lakshmi_Narayana_Gupta_Koralla_dataops_transformation_datacentric) or the [YouTube recording](https://youtu.be/aBws9lQwyKk).

## Watch the talk

[DataOps: Accelerating Digital Transformation Through Data-Centric Methodologies](https://www.conf42.com/Observability_2025_Lakshmi_Narayana_Gupta_Koralla_dataops_transformation_datacentric) at Conf42 Observability 2025.
