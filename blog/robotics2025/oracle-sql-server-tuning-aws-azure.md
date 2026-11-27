# Tuning Oracle and SQL Server on AWS and Azure, layer by layer

Conf42 Blog, 2025-11-20, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/oracle-sql-server-tuning-aws-azure

In short: Adithya Sirimalla of Enliven Technologies at Conf42 Robotics 2025 on a practical framework for Oracle and SQL Server performance and cost in the cloud.

Moving Oracle or SQL Server to the cloud doesn't retire the DBA playbook; it adds a second set of tools on top. At Conf42 Robotics 2025, Adithya Sirimalla, Software Developer and DBA at Enliven Technologies, walked through a framework that pairs classic database tuning with what AWS and Azure provide, framed for automation workloads where every millisecond of latency feeds a real-time decision.

Fair warning on scope: this is a brisk survey, more checklist than demo. As a checklist it's a good one.

## The fundamentals still come first

Before any cloud console, Adithya starts with the tools DBAs already trust: SQL Plan Management and AWR analysis on Oracle, Query Store on SQL Server. They keep plans stable, show where the bottlenecks are and track performance over time. The cloud tools sit on top of that history, they don't replace it.

## Pin the plan before it regresses

Plan stability gets its own slide, and rightly so. Capturing and enforcing known-good plans with SQL Plan Management in Oracle and Query Store plan forcing in SQL Server prevents the classic regression where a statistics refresh picks a worse plan on a busy Tuesday. Pinning the plan is the database equivalent of a lockfile.

The rest of the toolkit is a tour of the levers you'd expect:

- **Query work.** Find slow queries with AWR and Performance Insights, read the execution plan, then index or rewrite.
- **Resources.** Balance memory, IO and CPU, and use connection pooling to cut latency under high concurrency.
- **Partitioning.** Range, hash or list partitioning to target data sets and shrink maintenance windows.
- **Governance.** Oracle Resource Manager and SQL Server Resource Governor to guarantee CPU, memory and sessions for critical workloads.

## Each cloud brings a different lens

On the cloud side, Adithya contrasts AWS Performance Insights, which visualizes database load in real time, and Aurora Serverless with Azure's intelligent tuning, which uses machine learning to adjust performance automatically, and Hyperscale for very large workloads. To decide where a workload belongs, the talk recommends cross-platform benchmarks on the same KPIs, query response time and transactions per second, instead of trusting a feature matrix.

## The bill is a performance metric too

Cost gets equal billing: right-size instances, commit to reserved capacity where the load is steady, optimize storage, and set monitoring alerts before the invoice does it for you. The roadmap is assess, take the quick wins, set up governance, then plan the strategic work. His summary line: "optimization is a continuous process", because data and infrastructure keep growing after the migration party ends.

## Who should watch

DBAs and platform engineers mid-migration or newly responsible for managed Oracle or SQL Server, who want a one-page view of which knobs exist on each side. Seasoned performance engineers will find it a refresher rather than new ground.

## Related Conf42 talks

- [Adithya Sirimalla: Mastering Multi-Cloud Database Resilience](https://www.conf42.com/Incident_Management_2025_Adithya_Sirimalla_multicloud_databases_resilience) is the same speaker on keeping these databases up across clouds.
- [Sunil Yadav: Building Bulletproof Database Platforms](https://www.conf42.com/Platform_Engineering_2025_Sunil_Yadav_availability_oracle_database) covers availability engineering in Oracle Cloud.
- [Andrew Pruski: Chaos Engineering for SQL Server](https://www.conf42.com/Chaos_Engineering_2020_Andrew_Pruski_sql_server) breaks SQL Server on purpose so you learn how it fails.

[Watch Adithya Sirimalla's talk](https://www.conf42.com/Robotics_2025_Adithya_Sirimalla_oracle_azure_cloud)

[Watch the talk on YouTube](https://youtu.be/AGYd8ZU6Ja8).

## Watch the talk

[Optimizing Oracle & SQL Server in the Cloud: A Practical Framework for High-Performance Database Management on AWS & Azure](https://www.conf42.com/Robotics_2025_Adithya_Sirimalla_oracle_azure_cloud) at Conf42 Robotics 2025.
