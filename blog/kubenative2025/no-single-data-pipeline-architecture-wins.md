# No single data pipeline architecture wins, so migrate in pieces

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/no-single-data-pipeline-architecture-wins

In short: Vamsi Pulusu (Ford Motor Company) at Conf42 Kube Native 2025 compares medallion, Lambda, Kappa, lakehouse and data mesh, then lays out how to leave legacy ETL.

Remember waiting overnight for the batch job so the morning report would exist? Vamsi Pulusu, Technical Architect and lead data engineer at Ford Motor Company with 16 years in the field, used that memory to open his Conf42 Kube Native 2025 talk, then compared the five architecture patterns that replaced it and argued that the right answer is a combination chosen per business context, reached incrementally.

The abstract is blunter: "Legacy ETL is dead." The talk itself is more nuanced, and better for it.

## Why the nightly batch had to go

Vamsi lists the constraints of traditional ETL: overnight batch windows that kept data stale when the business wanted real-time monitoring; single points of failure where recovery often meant reprocessing everything; scaling by buying bigger hardware; tools built for structured data facing logs, device streams and web events; and lock-in through proprietary query extensions.

The turning point, in his telling, was cloud object storage decoupling storage from compute. Before, more processing meant buying more storage, and vice versa. After, cheap and practically unlimited storage scales on its own, costs move from capital spend to pay-as-you-go, and schema-on-read lets you land raw data first and transform it later.

## Five patterns, five philosophies

The core of the talk is a side-by-side:

- **Medallion**: bronze for raw data as landed, silver for standardised and quality-checked data, gold for business-ready structures like star schemas and pre-aggregated metrics. Clear quality boundaries; a good fit where governance is strict.
- **Lambda**: a batch path for complete historical accuracy plus a speed path for fast preliminary answers. The cost is two code bases for the same transformation logic.
- **Kappa**: stream first, one processing engine, an append-only event log as the system of record. Batch is just streaming over a longer window. Simpler to maintain.
- **Lakehouse**: warehouse features such as ACID transactions and schema enforcement on top of cheap lake storage, so BI, ML and streaming share one copy of the data.
- **Data mesh**: less an architecture than an org chart. Domain teams own data as products on a self-serve platform under federated governance. Vamsi is clear that it is a socio-technical change, and that is the hard part.

The Lambda-versus-Kappa comparison alone is worth the time if your team keeps maintaining the same logic twice.

## Governance becomes a runtime job

Distributed pipelines make old periodic checks inadequate. Vamsi wants automated lineage at dataset, column and even record level, continuous quality validation at every transformation boundary, and data contracts between producers and consumers, implemented with versioned schema registries that check proposed changes against historical usage before they break someone downstream.

He also covers the tools timeline, from DataStage and Informatica through Hadoop to Airflow, Prefect, Kafka, Spark streaming and Flink, and argues that tool choice should weigh team skills, operational needs, cost model and integration, not just feature lists. Feature stores get a mention as the bridge between pipelines and ML, with point-in-time correctness as the requirement that matters.

## Migrate domain by domain

Big-bang replacement is rarely feasible, so his migration strategies are all incremental: modernise by recurring pattern, run hybrid behind gateway components that keep interfaces stable, bridge to existing sources with adapters, and go domain by domain starting with non-critical ones. Inventory your current state, pick a target pattern such as medallion or lakehouse, invest in lineage and quality early, and build streaming skills in the team.

## Who should watch

Data engineers and architects planning a move off batch ETL, and platform engineers who host those pipelines on Kubernetes and want to know why the data team keeps saying "medallion". It is a survey talk; you will leave with a map, not a migration runbook.

## Related Conf42 talks

- [Building Modern Data Streaming Apps with Python](https://www.conf42.com/DevOps_2023_Tim_Spann_modern_data_streaming_apps) by Tim Spann (StreamNative), streaming made concrete.
- [What is a Data mesh for god's sake !?](https://www.conf42.com/Cloud_Native_2023_Ismael_Hommani_CharlesAlban_Benezech_data_mesh) by Ismael Hommani (Wescale), more on the organisational pattern.
- [Build cloud native open format data lakehouse](https://www.conf42.com/Cloud_Native_2023_Satish_Mane_Rajeev_Jaiiswal_build_open_format_data_lakehouse) by Satish Mane (AWS), the lakehouse built out.

[Watch Vamsi Pulusu's talk](https://www.conf42.com/Kube_Native_2025_Vamsi_Pulusu_datapipeline_streaming_modern)

[Watch the talk on YouTube](https://youtu.be/P0z7za4xN0g).

## Watch the talk

[Demystifying Modern Data Pipeline Architecture: From Legacy ETL to Cloud-Native Streaming at Scale](https://www.conf42.com/Kube_Native_2025_Vamsi_Pulusu_datapipeline_streaming_modern) at Conf42 Kube Native 2025.
