# From firefighting to forecasting, a DBA's roadmap for AI ops

Conf42 Blog, 2026-05-11, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/database-devops-predictive-to-semi-autonomous

In short: Ellavarasan Asokan of Capital One at Conf42 Database DevOps 2026 on forecasting, RL indexing and anomaly detection on the way to semi-autonomous databases.

Index maintenance, capacity planning and alert triage are still mostly manual for DBAs, even when the application around them ships through CI/CD. At Conf42 Database DevOps 2026, Ellavarasan Asokan, Software Consultant at Capital One Bank and an Oracle DBA of fourteen-plus years, mapped the four AI capabilities he sees moving database operations from reactive to predictive, and the four stages to get there without losing control.

This is an overview talk, written from the DBA's chair rather than the data scientist's. It names techniques (LSTM forecasting, reinforcement learning for indexes, clustering for anomalies) without code or benchmarks, which makes it a good orientation for a team deciding where to start.

## The traditional DBA day is reactive by design

Ellavarasan has done the full range: installs, patching, upgrades, performance work and migrations of databases from 5 TB to around 50 TB, on-premises and in AWS and Azure. His description of the old model will be familiar: manual query profiling, manually maintained indexes and storage, threshold alerts that start the work only after something breaks, and root cause analysis as post-mortem. Continuous deployment multiplies database change, cloud workloads shift dynamically, and manual tuning cannot keep pace with DevOps velocity.

## Four capabilities, each aimed at a specific pain

- **Predictive workload forecasting.** Models such as LSTM networks learn from historical workload patterns, CPU, IO throughput, deployment schedules, traffic and seasonality, so resources are allocated before the spike. Flash sales, batch scheduling, canary planning and cloud right-sizing are the use cases he lists.
- **Automated indexing with reinforcement learning.** Static indexes age badly as a database grows from a couple of terabytes to ten. An RL agent watches query behaviour and recommends, creates and retires indexes, cutting latency and freeing the storage that redundant indexes waste.
- **AI anomaly detection.** Time series analysis, clustering and deep learning models over query latency, execution behaviour, CPU, memory, IO and transaction patterns, filtering the noise so the critical alert is not buried among a hundred harmless ones. Deadlocks, plan regressions and unusual access patterns are the catches he highlights. Anyone who has been woken at 3am by a disk alert that cleared itself will get the appeal.
- **AI in CI/CD.** Database changes validated before release, performance baselines enforced automatically, and rollback decisions that keep the blast radius small. Reliability shifts left.

## Stale models and patchy telemetry are the real blockers

The challenges section is candid. Models need regular retraining as workloads change, and a stale one produces misleading advice. Inconsistent telemetry and fragmented monitoring degrade accuracy. Legacy platforms without modern APIs limit automation without serious re-engineering. And teams will not trust autonomous recommendations without transparent reasoning and oversight.

So his position on full automation is cautious: wrong decisions in edge cases and regressions that are hard to trace are real risks. Keep a human in the loop, surface recommendations with context and confidence scores, require explicit approval for high-risk changes, test in shadow mode in lower environments, and limit the blast radius of every rollout.

## A four-stage roadmap

The plan is deliberately incremental: observability first (telemetry and baseline behaviour models across all database tiers), then AI recommendations that humans review and approve, then low-risk routine tasks automated without approval, and finally semi-autonomous operation with AI-driven scaling, self-optimizing indexes and predictive remediation inside governance guardrails. Note the word semi: his closing picture is humans setting intent and AI executing it.

## Who should watch

DBAs and database platform leads looking for a vocabulary and a sequence for introducing AI into operations. If you want implementation detail or measured results, pair it with a talk that shows a system end to end. This one tells you which questions to ask first.

## Related Conf42 talks

- [Birol Yildiz on cutting alert noise with AIOps](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) at Conf42 DevSecOps 2024.
- [Yoav Nordmann on anomaly detection with Apache Pinot and ThirdEye](https://www.conf42.com/Cloud_Native_2023_Yoav_Nordmann_anomaly_detection_apache_pinot_thirdeye) at Conf42 Cloud Native 2023.
- [Piotr Stepinski on time series forecasting](https://www.conf42.com/Machine_Learning_2024_Piotr_Stepinski_forecasting_timeseries) at Conf42 Machine Learning 2024.

[Watch Ellavarasan Asokan's talk](https://www.conf42.com/Database_DevOps_2026_Ellavarasan_Asokan_monitoring_reliability_platform)

[Watch the talk on YouTube](https://youtu.be/uhhQr4Kuf_I).

## Watch the talk

[AI-Driven Database DevOps: From Predictive Tuning to Autonomous Operations in Production](https://www.conf42.com/Database_DevOps_2026_Ellavarasan_Asokan_monitoring_reliability_platform) at Conf42 Database DevOps 2026.
