# Running a 10TB-a-day Databricks pipeline like an SRE service

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/im2025/cross-cloud-databricks-pipeline-sre-playbook

In short: Sruthi Erra Hareram at Conf42 Incident Management 2025 on freshness SLIs, circuit breakers and Z-ordering for a cross-cloud Azure Databricks pipeline.

Data pipelines rarely get the SRE treatment that APIs do, which is odd, because a stale dashboard is an outage to the people staring at it. At Conf42 Incident Management 2025, data engineer Sruthi Erra Hareram walked through a case study of an analytics pipeline on Azure Databricks and Amazon S3 handling more than 10 TB a day, and the single idea that held it together: treat freshness as an SLI with an error budget, and let that budget decide what gets paused.

The workload was ad campaign telemetry, billions of events a day across regions, feeding user-facing dashboards that had to stay fresh within minutes. With many interdependent ETL jobs, one upstream blip could cascade through the lot.

## Freshness is the SLI that matters

The team's working targets were p95 freshness under 15 minutes and p99 under 30, with back-pressure rules when those drift. They tracked three SLIs: freshness from ingest to the gold layer, p95 query latency on key workloads, and end-to-end success rate. Error budgets triggered graceful degradation. If seven-day rolling freshness blew its budget, non-critical enrichments were paused so the core tables kept up.

Toil came first in the backlog. They automated the most common failure classes, aiming to keep auto-resolution above 70%, on the reasoning that humans should not be babysitting pipelines.

## Retries only work when writes are idempotent

The stack is Azure Databricks with Delta Lake for ACID semantics, schema evolution and time travel, Azure Data Factory for orchestration, and S3 for durable versioned storage where it was needed. On top of that she describes four standard patterns:

- **Checkpointing.** Every stage can resume from known offsets, and offsets are committed only after idempotent writes succeed.
- **Circuit breakers at integration points.** One example threshold: trip if the error rate stays above 10% for five minutes, or freshness breaches for three consecutive checks.
- **Exponential backoff with jitter.** Random jitter of up to three seconds, so retries don't stampede.
- **Idempotent writes.** All merges are keyed and retries have no side effects.

Her one-line summary of the section is the bit to pin above your desk: retries only work when your operations are idempotent.

## Z-order from query logs, not intuition

Before tuning, the pipeline did full scans, big shuffles and spiky latencies. The fix was aligning storage to real access patterns: partitioning that prunes (by event date, for instance), Z-ordering on high-selectivity keys queried together (campaign ID, region, device), and regular OPTIMIZE plus small-file compaction so Spark isn't drowning in tiny files.

How they chose Z-order keys is the most transferable detail. They mined query logs for the most frequent multi-column filters with high cardinality, validated with A/B runs on representative workloads, and revisited the keys quarterly because dashboards change what people query. Z-ordering itself ran weekly on hot tables and monthly on warm ones, and compaction kicked in when average file size dropped below 128 MB. Fixed clusters gave way to workload-aware autoscaling with hard cost guards per priority tier.

## An incident, step by step

The playbook runs detection (SLI-driven, freshness and success rate, not just CPU), classification, containment, remediation and recovery. Her example is S3 cross-region replication lag. Freshness monitors flagged the drift, downstream joins paused, users were served the last consistent slice with a clear stale-data banner, and non-critical work was diverted. Once replication recovered, the team validated consistency on boundary tables, burst-scaled to clear the backlog and returned to steady state. On-call only approved predefined steps; everything else was automated.

She also shows how to read metrics together: a rising data-quality error rate with flat compute points at schema drift, not capacity, while a widening p95 at flat volume points at partition skew or small-file bloat.

## Who should watch

Data platform engineers who get paged for late tables, and SREs who inherit a lakehouse and want a vocabulary for it. It is a compact case study, dense with thresholds you can argue about, and light on slides of architecture boxes. The closing blueprint (SLIs and budgets, breakers at every seam, checkpoints at every hand-off, two failure-mode drills per quarter) is a solid starting checklist.

## Related Conf42 talks

- [Bring your DataOps to the Data Lakehouse](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) by Jorge Loaiciga Rodriguez covers the process side of lakehouse operations.
- [Building Resilient Apache Spark Clusters on Kubernetes](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters) by Anant Kumar looks at the compute layer from the platform team's seat.
- [Techniques for SLOs and Error Budgets at Scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) by Fred Moyer goes deeper on the budgeting maths.

[Watch Sruthi Erra Hareram's talk](https://www.conf42.com/Incident_Management_2025_Sruthi_Erra_Hareram_databricks_analytics_reliability)

[Watch the talk on YouTube](https://youtu.be/abO2XM3KzlM).

## Watch the talk

[Resilient Cross-Cloud Analytics Pipelines with Azure Databricks: A 10TB+ Scale Reliability Engineering Case Study](https://www.conf42.com/Incident_Management_2025_Sruthi_Erra_Hareram_databricks_analytics_reliability) at Conf42 Incident Management 2025.
