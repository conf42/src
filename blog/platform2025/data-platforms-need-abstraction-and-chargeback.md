# A Data Platform Is Abstraction, Automation and a Chargeback Model

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/data-platforms-need-abstraction-and-chargeback

In short: Meta engineer Rahul Joshi at Conf42 Platform Engineering 2025 on multi-tenant, self-service data platforms from Hadoop to the lakehouse.

Rahul Joshi, a software engineer at Meta, used his Conf42 Platform Engineering 2025 talk to make the case that a shared enterprise data platform lives or dies on four things: abstraction, automation, observability and user experience. Underneath sits a less glamorous requirement that most self-service platforms discover the hard way: a chargeback model, because self-service on a cloud bill with no ceiling is a budget incident waiting to happen.

The talk is a general framework drawn from industry patterns, not a tour of Meta's internal systems, and it's pitched at architects designing or reshaping a multi-tenant data platform.

## Three eras, three lessons

Rahul opens with history. The big data era, from around 2006, built data lakes on Hadoop clusters of commodity hardware, and platform engineers spent their days keeping them running. The cloud era moved that work to managed services such as Redshift, BigQuery and Snowflake, removing operational toil but adding cost optimisation and vendor management. The lakehouse era, with Delta Lake, Iceberg and Hudi, lets one platform serve analytical and operational workloads with strong consistency and governance. Each phase left a lesson that modern designs carry.

## Self-service needs standard patterns and a catalog

The principles section starts with personas: business users, analysts, data scientists and engineers all need interfaces that hide the implementation without hiding the capability. From there:

- **Platform APIs** with clear documentation and versioning, so contracts between producers, consumers and the platform survive schema changes.
- **Standardised processing patterns**, so a thousand use cases don't each re-implement the same reads, joins and flattening.
- **A shared data catalog**, because with hundreds of producing systems, finding data is the first problem.
- **Infrastructure and pipeline automation** for provisioning, promotion from dev through QA and UAT to production, and consistent configuration across environments.

## Tenants, isolation and who pays

Multi-tenancy is the core of the enterprise case: one platform serving many lines of business instead of one platform each. Every tenant gets its own workspace, access controls, compute allocation and data-sharing rules, including geographic restrictions, with both logical and physical isolation of storage and compute where needed.

The cost section names the drivers plainly: compute when data is queried, storage for raw, refined and use-case layers (he references the medallion pattern), and network for transfers. The answer is tracking that attributes cost to teams through chargeback, so each line of business sees what it spends and what it could trim. The levers are scheduling, autoscaling when demand is predictable, and tiered storage such as S3 Intelligent-Tiering or explicit lifecycle and retention rules.

## Observability means data quality, too

Infrastructure monitoring covers health, throughput and utilisation. Data observability adds freshness, schema evolution, missing and duplicate records, schema violations and statistical anomalies, with quality rules run inside the pipelines and tiered alerting by issue type. Security covers encryption at rest, in transit and in memory, masking and tokenisation, and access control from role- and attribute-based down to row and column level. One practical point: SQL access on table formats like Delta Lake or Snowflake gives you usage audit for free, while raw file consumption needs extra tracking.

## Avoid the lock-in you can see coming

For future-proofing, Rahul advises open formats and an abstraction layer so consumers don't notice when storage or compute underneath changes. Plan for terabytes turning into petabytes, as AI workloads keep the data growing, and for governance needs that will change with the business.

## Who should watch

Architects and leads running a central data platform for several teams, especially if the cloud bill and the catalog are both getting out of hand. It's a framework talk; there's no code, but the checklists are solid.

## Related Conf42 talks

- [Satish Mane and Rajeev Jaiiswal: Build cloud native open format data lakehouse](https://www.conf42.com/Cloud_Native_2023_Satish_Mane_Rajeev_Jaiiswal_build_open_format_data_lakehouse).
- [Jorge Loaiciga Rodriguez on bringing DataOps to the lakehouse](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges).
- [Ganeshkumar Palanisamy on optimising multi-cloud data platforms with AIOps and FinOps](https://www.conf42.com/Observability_2025_Ganeshkumar_Palanisamy_platforms_scale_finops).

[Watch Rahul Joshi's talk](https://www.conf42.com/Platform_Engineering_2025_Rahul_Joshi_modern_data_infrastructure)

[Watch the talk on YouTube](https://youtu.be/-oKAk-3Oufw).

## Watch the talk

[Platform Engineering for Modern Data Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Rahul_Joshi_modern_data_infrastructure) at Conf42 Platform Engineering 2025.
