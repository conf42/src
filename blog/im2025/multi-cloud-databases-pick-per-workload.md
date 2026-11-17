# Multi-cloud databases work when you pick per workload, not per vendor

Conf42 Blog, 2025-09-22, updated 2026-11-09. https://www.conf42.com/blog/im2025/multi-cloud-databases-pick-per-workload

In short: Adithya Sirimalla (Enliven Technologies) at Conf42 Incident Management 2025 compares Oracle Autonomous Database, Azure SQL and RDS for SQL Server resilience.

Running Oracle and SQL Server across AWS, Azure and Oracle Cloud is not a strategy anyone chose on purpose, but plenty of DBAs live there anyway. At Conf42 Incident Management 2025, Adithya Sirimalla, software developer and DBA at Enliven Technologies, gave a practical overview of how to keep that estate resilient, and his headline advice is refreshingly blunt: choose the database platform per workload, not out of vendor loyalty or habit.

This is an overview talk for DBAs and platform engineers rather than a deep technical session. It covers four things in order: the three managed platforms, resilience strategy, automation and observability.

## Three managed platforms, three personalities

Adithya's comparison is the most useful part for anyone mid-decision.

Oracle Autonomous Database is the self-managing one: automated patching, upgrades and tuning, machine learning for performance optimisation, and automatic scaling. It can run serverless for variable workloads, or on dedicated infrastructure for steady, predictable ones.

Azure SQL Database leans on intelligent performance: AI-based recommendations and automatic tuning, with a Hyperscale tier that lets a database grow to 100 TB. Transparent data encryption and Azure identity integration cover security, and pricing comes as DTU-based, vCore-based or serverless.

Amazon RDS for SQL Server is the enterprise-reliability option: automated backups, point-in-time recovery, Multi-AZ deployments for high availability, read replicas, and support for SQL Server features such as Always On availability groups, SSIS and SSRS, with reserved or on-demand pricing.

His summary: Oracle for self-management, Azure for intelligent performance, RDS for dependable enterprise service. Each has a lane.

## A backup you have not restored is a rumour

The resilience section covers what goes wrong in practice. Multi-cloud backup with cross-cloud replication, scheduled to avoid performance impact, and validated regularly by actually restoring. Failover through active-passive setups with automated health checks and DNS-based routing, or active-active architectures if you need zero downtime.

Compliance gets equal billing with uptime. Data residency rules, encryption standards, centralised audit logging and consistent controls across clouds keep the auditors happy and stop the second cloud from becoming the compliance gap.

## Automate the toil, then watch everything

On automation, Adithya focuses on Terraform for infrastructure as code, keeping database infrastructure version-controlled and reproducible, combined with the AWS CLI, Azure CLI and OCI CLI to script snapshots, scaling, patching and performance checks. His framing is that automation is about cutting human error and making operations repeatable, not only about speed.

For monitoring, the question he poses is the right one: will you know something broke before your customers do? Track CPU, memory, I/O, availability and response times, plus threat detection, and build a unified view from tools like CloudWatch, Azure Monitor, Prometheus, Grafana, Datadog or Splunk. The more ambitious step is automated performance tuning: establish baselines, add ML-based anomaly detection, and wire predefined responses for common issues, with the goal of pushing MTTR down until incidents are barely noticeable.

## Who should watch

DBAs and platform engineers who inherited databases on more than one cloud, and architects deciding where the next Oracle or SQL Server workload should land. If you already run cross-cloud DR drills, the comparison section is the part to take away.

## Related Conf42 talks

- [Optimizing Oracle & SQL Server in the Cloud](https://www.conf42.com/Robotics_2025_Adithya_Sirimalla_oracle_azure_cloud) by Adithya Sirimalla himself, a companion talk on performance management for the same two databases.
- [Building Bulletproof Database Platforms: Engineering 99.98% Availability in Oracle Cloud](https://www.conf42.com/Platform_Engineering_2025_Sunil_Yadav_availability_oracle_database) by Sunil Yadav, for the availability engineering in depth.
- [Terraform for Secure Multi-Cloud DevSecOps](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) by Perumalsamy Ravindran, on the Terraform side of the story.

[Watch Adithya Sirimalla's talk](https://www.conf42.com/Incident_Management_2025_Adithya_Sirimalla_multicloud_databases_resilience)

[Watch the talk on YouTube](https://youtu.be/NiJ3KtbZjG8).

## Watch the talk

[Mastering Multi-Cloud Database Resilience: Oracle & SQL Server in a Cloud-Native World](https://www.conf42.com/Incident_Management_2025_Adithya_Sirimalla_multicloud_databases_resilience) at Conf42 Incident Management 2025.
