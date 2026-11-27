# Fraud detection is a platform problem before it is a model problem

Conf42 Blog, 2025-09-04, updated 2026-11-17. https://www.conf42.com/blog/platform2025/real-time-fraud-detection-platforms

In short: Shivam Tiwari at Conf42 Platform Engineering 2025 on the platform under real-time financial crime detection: streaming, graph stores, compliance as code.

Machine learning, graph analytics and behavioural pattern recognition have replaced rules as the front line against financial fraud, and none of them work without the plumbing. That is the argument Shivam Tiwari, who has spent nine years in data science and analytics, makes at Conf42 Platform Engineering 2025. His talk is a checklist of the platform layers a real-time financial crime detection system needs, from event streaming to spot instances.

Set expectations accordingly. This is a survey of patterns. It names no products, shows no architecture from a specific bank and quotes no throughput or latency figures. As a map of what a platform team will be asked to build, it is complete and quick.

## Why rules stopped being enough

Rule-based detection is still useful, he says, but it cannot keep up with the complexity and scale of current fraud. The newer techniques ask more of the infrastructure. "the success of all these advanced techniques really hinges on having the right platform infrastructure underneath them," Shivam Tiwari said at Conf42 Platform Engineering 2025.

He frames four constraints: data arriving from many sources at different speeds, detection that has to be fast and accurate at once, transaction volumes that swing, and regulators who expect audit trails and lineage for every decision. The rest of the talk answers those four.

## Decouple ingestion from analysis

The foundation is event streaming with durable, ordered, exactly-once processing, analytical components run as independent microservices, and a hybrid storage layer that serves both OLTP and OLAP workloads.

Event-driven design earns its place because it separates transaction ingestion from analytical processing, so a traffic spike does not take detection down with it. Two details are worth noting. Event sourcing keeps a complete log, which serves the auditors and also lets a team replay history against a new model before it goes live. And backpressure management stops upstream systems from flooding the analytical services.

For data pipelines he sets Lambda (separate batch and streaming paths) against Kappa (streaming for everything, one system to maintain), and adds lineage tracking and automated data quality checks to both.

## Networks need their own databases

Network analysis is the most compute-hungry part of the job. He recommends graph databases for relationships between accounts, time series databases for how those networks change, and accepting polyglot persistence as the normal state. The platform's task is to hide that variety behind a unified query interface so analysts do not need to know which store holds what.

## Models are workloads with priorities

On deployment, he covers multi-stage container builds to keep runtime images small, semantic versioning with immutable artifacts so a given model version can be reproduced, and explicit CPU, memory and GPU allocations. Quality-of-service policies keep high-priority detection models from being starved by lower-priority jobs.

The resilience section follows the same logic. Circuit breakers stop cascading failures. Bulkheads give fraud models dedicated resources. Retries must respect idempotency, because a transaction processed twice skews the detection results, which is a worse outcome here than in most systems. Multi-region replication covers the data stores. Autoscaling combines predictive scaling from historical patterns with reactive scaling on live metrics, coordinated across tiers that scale differently.

## Compliance belongs in the pipeline

Observability goes past infrastructure metrics into prediction confidence, feature distribution shifts and decision outcomes, with distributed tracing to follow a single transaction through several analytical services. Alerts should catch gradual model degradation without paging on normal variation.

Compliance is automated the same way as everything else: infrastructure as code for security settings and access controls, policy engines that evaluate configurations against regulatory standards, tamper-evident audit logs of every platform change, and automated secret rotation. GitOps handles promotion between environments with approvals, validation and rollback built in.

He ends on cost: tune the analytical workloads, right-size resources, and use spot instances for jobs that can tolerate interruption. An auditor is unlikely to accept the same about the detection path.

## Who should watch

Platform engineers moving into fintech or joining a fraud analytics team, and data scientists who want to understand what they are asking the platform team for. Engineers who already run streaming detection in production will not find new techniques here, and anyone looking for benchmarks or a worked case study should pair it with one of the talks below.

## Related Conf42 talks

- [Rahul Ganti on fraud detection in financial systems](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial) at Conf42 Platform Engineering 2025.
- [Advancing Financial Fraud Detection with Graph Databases: Innovations and Applications](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu (JPMorganChase), for the relationship-heavy side of fraud.
- [Compliance-Aware Platform Engineering: Scaling Hybrid Cloud Automation in Regulated Financial Environments](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) by Satish Manchana.

[Watch Shivam Tiwari's talk](https://www.conf42.com/Platform_Engineering_2025_Shivam_Tiwari_crime_analytics_detection) from [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/y-QRB0dKkIg).

## Watch the talk

[Building Real-Time Analytics Platforms for Financial Crime Detection](https://www.conf42.com/Platform_Engineering_2025_Shivam_Tiwari_crime_analytics_detection) at Conf42 Platform Engineering 2025.
