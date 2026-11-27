# Graph topology plus learned baselines for financial anomaly detection

Conf42 Blog, 2025-06-05. https://www.conf42.com/blog/obs2025/graph-topology-and-baselines-for-fintech-anomalies

In short: Siva Prakash at Conf42 Observability 2025 on dependency graphs and behavioural baselines replacing static thresholds in financial system monitoring.

Static thresholds do not know that a Monday morning looks different from a Friday afternoon during options expiry. Siva Prakash, who has spent two decades in IT and the last four years in financial and insurance systems, made that the starting point of his Conf42 Observability 2025 talk: combine a live dependency graph of your services with machine-learned behavioural baselines, and you catch anomalies thresholds miss while sending fewer false alerts.

The talk's headline claims are big: 99.4% anomaly detection accuracy and 87% fewer false alerts. They come from the speaker's own solution and unnamed case studies, so read the method as the takeaway and the figures as claims.

## Why thresholds fail in finance

Prakash's diagnosis has four parts. Low detection rates for critical anomalies, so issues surface after customers or financial processes are hit. Alert fatigue, with operators he describes as drowning in false positives and missing the real alert. System complexity, with thousands of interdependencies across microservices, APIs and distributed databases. And the financial impact: downtime, reputational damage and regulatory penalties. Static limits on CPU or response time ignore context and relationships, which is exactly what a distributed system is made of.

## Step one: a living graph of the system

The first technique is graph-based topology analysis. Collect logs, metrics and traces from every application, microservice, database and infrastructure component. Build a graph of service dependencies from that telemetry; he compares it to a social network for your services, showing who talks to whom and how often. Then analyse interaction patterns to spot deviations, such as a service suddenly calling another it has never talked to, or a critical path with unusual latency. Because the graph knows the relationships, alerts carry blast radius and upstream and downstream impact, which helps with prioritisation and root cause.

## Step two: baselines instead of thresholds

The second technique is behavioural analytics as a continuous loop. Collect hundreds of system metrics in real time. Use machine learning to learn what normal looks like for your environment, with dynamic baselines that adapt to seasonality. Evaluate deviations in context: is this an isolated blip or part of a pattern? Then flag subtle anomalies early, often before anything would breach a static limit. The graph says how components connect; the baselines say how they should behave within that structure.

## Data volume is its own engineering problem

Financial systems are data factories, as he puts it, so the platform needs intelligent filtering to prioritise relevant telemetry, adaptive compression to keep storage costs down while preserving history, and real-time analysis on top. Integration covers AWS, Azure, GCP and on-prem, language-agnostic instrumentation with OpenTelemetry support to avoid lock-in, SQL and NoSQL connectors, and security requirements that are non-negotiable in the sector: SOC 2, PCI and GDPR alignment, end-to-end encryption and role-based access.

## A phased rollout

His implementation plan is concrete in its timing: an assessment phase of two to three weeks for topology mapping and a monitoring gap analysis, a pilot of three to four weeks on the most critical services to set baselines, an expanded rollout of four to six weeks with alert tuning, and ongoing optimisation. The case studies he cites, a global investment bank, a regional credit union and an insurer, are presented as anonymised examples of reduced MTTR and fewer false alerts.

## Who should watch

SREs and platform teams in banking, payments or insurance who are still alerting on fixed thresholds, and anyone wondering how topology and ML baselines fit together. Expect a solution pitch in the second half rather than code.

## Related Conf42 talks

- [Advancing Financial Fraud Detection with Graph Databases](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu at Conf42 Machine Learning 2025.
- [Accelerating Incident Response with Distributed Graph Technology](https://www.conf42.com/Incident_Management_2025_Pushap_Goyal_graph_spanner_security) by Pushap Goyal at Conf42 Incident Management 2025.
- [Enhancing Banking Security: Leveraging AI and Data Engineering for Effective Fraud Detection](https://www.conf42.com/Observability_2024_Giriprasad_Manoharan_ai_fraud_detection) by Giriprasad Manoharan at Conf42 Observability 2024.

[Watch Siva Prakash's talk](https://www.conf42.com/Observability_2025_Siva_Prakash_financial_anomaly_graph) or the [YouTube recording](https://youtu.be/JFh9g7y8g6o).

## Watch the talk

[Cloud-Native Observability for Financial Systems: Implementing Graph-Based Monitoring and Behavioral Analytics for 99% Anomaly Detection Accuracy](https://www.conf42.com/Observability_2025_Siva_Prakash_financial_anomaly_graph) at Conf42 Observability 2025.
