# Trace the risk score, not just the request

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observable-pipeline-for-bankruptcy-risk

In short: Diliprao Boinapally of G2 Risk Solutions at Conf42 Observability 2025 on rebuilding bankruptcy monitoring as a traced, serverless pipeline.

A bankruptcy filing that reaches the analyst two days late is a loss nobody pages for. At Conf42 Observability 2025, Diliprao Boinapally of G2 Risk Solutions showed how his team rebuilt bankruptcy monitoring from a slow, reactive black box into a serverless pipeline where every risk score can be traced back to the documents that produced it. The idea worth stealing: instrument the business signal (case type, risk level, client) with the same care as latency and errors.

## The before picture was a visibility crisis

Diliprao is candid about where they started. Legacy systems were siloed and manual. When something broke, nobody could trace the root cause. Risk signals took hours or days to surface, and compliance teams spent weeks stitching together audit trails after the fact. Every blind spot, in his framing, was a chance to lose money.

That crisis forced the mindset shift that runs through the whole talk: observability could not be bolted on later. It had to be part of the architecture from the first commit.

## The pipeline, layer by layer

The architecture is a familiar data-engineering stack, which is part of why the talk is useful:

- **Ingestion**: serverless, event-driven functions pull legal filings, credit scores, transactional databases and third-party feeds, normalising data as it arrives. Each document gets quality metrics: format issues, missing fields, delays.
- **Entity resolution**: Apache Spark matches names, identifiers and patterns across data sets to produce risk scores. Every transformation is traced, so the team can watch matching precision and spot bottlenecks.
- **Orchestration**: Apache Airflow runs the dependencies and schedules, and each step logs its validation status, error category, retry rate and regulatory checkpoints.

Across all three, OpenTelemetry carries a trace from the entry point to the final risk score. That is the detail that turns "the score looks wrong" from a week of archaeology into a query.

## Logs that speak compliance

The second move is enriching logs with business context instead of leaving them as purely technical records. A log line that says which client, which case type and which risk level it belongs to is one a compliance officer can read. Diliprao ties system KPIs such as latency and throughput to business outcomes such as detection accuracy and compliance completeness, so engineering and compliance end up looking at the same dashboards and arguing about the same numbers.

Dashboards are split by audience: executives get KPIs and financial impact, engineers get task failures and latency, compliance gets traceability and alert logs. One pane of glass, three different windows.

## The numbers he reports

The talk is generous with results from the rollout. Average processing time fell from two hours 40 minutes to 31 minutes. Risk alerts reach decision makers in under 45 seconds. False positives dropped by 87% and false negatives, which he rightly calls the dangerous ones, by 94%. On the compliance side, he reports documentation completeness at 97% and audit preparation time down by 71%. These are his team's figures for their system; treat them as a direction of travel rather than a benchmark for yours.

## Roll it out in four steps

The implementation roadmap is the most reusable part: a telemetry gap assessment across technical and business layers, then instrumentation (logging, tracing, metrics across the serverless, Spark and Airflow pieces), then role-specific dashboards built with stakeholder feedback, then enablement through training and playbooks. Each step is meant to pay for itself before the next starts.

## Who should watch

Data engineers running Spark or Airflow pipelines in regulated industries, and anyone who has had to rebuild an audit trail from Slack history. It is a short, architecture-level talk rather than a code walkthrough, so come for the design and the framing, not the config files.

## Related Conf42 talks

- [Sandeep Jarugula on AI-powered fraud detection in cloud-native financial systems](https://www.conf42.com/Cloud_Native_2025_Sandeep_Jarugula_fraud_detection_analytics_security) at Conf42 Cloud Native 2025.
- [Nicolas Frankel's practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing), if the tracing layer is the part you need to build first.
- [Anant Kumar on resilient Apache Spark clusters on Kubernetes](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters) at Conf42 Cloud Native 2025.

[Watch Diliprao Boinapally's talk](https://www.conf42.com/Observability_2025_Diliprao_Boinapally_financial_risk_cloudnative)

[Watch the talk on YouTube](https://youtu.be/JadAZVXVFMU).

## Watch the talk

[Observing the Invisible: Cloud-Native Observability for Real-Time Financial Risk Detection](https://www.conf42.com/Observability_2025_Diliprao_Boinapally_financial_risk_cloudnative) at Conf42 Observability 2025.
