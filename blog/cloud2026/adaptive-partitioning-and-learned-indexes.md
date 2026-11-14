# Static partitions and B-trees assume a workload the cloud won't give you

Conf42 Blog, 2026-04-03, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/adaptive-partitioning-and-learned-indexes

In short: Purushotham Jinka of Citi at Conf42 Cloud Native 2026 on adaptive partitioning, learned indexes and ML query engines, plus guardrails for self-tuning databases.

Classic database design assumes stable workloads, fixed hardware and a DBA who retunes things every quarter; a cloud-native system offers none of the three. At Conf42 Cloud Native 2026, Purushotham Jinka, Vice President at Citi focused on large-scale data and cloud platforms, traced how partitioning and indexing are moving from one-time design decisions to adaptive, increasingly self-optimizing mechanisms, with machine learning moving into the query engine.

It is a survey of where database architecture is heading rather than a hands-on tuning session, and it ends with a sensible order of operations for adopting automation.

## The mismatch

Traditional databases were built for predictability. Cloud environments are the opposite: workloads shift constantly, infrastructure is elastic, and availability expectations are very high. Purushotham's list of symptoms is short and recognizable: latency spikes, operational overhead and manual tuning that never catches up.

## Partitioning that keeps moving

His first claim is that partitioning is no longer a one-time decision. Range, hash or list partitions chosen up front go stale as query patterns drift and traffic creates hotspots. Newer systems watch real-time query patterns and rebalance data placement without downtime.

The strategies themselves are not exotic: range partitioning for time-based queries, hash for even distribution, composite schemes for mixed workloads. The change is combining them deliberately rather than picking one. Add partition-level replication, dynamic shard splitting and geo-aware placement, and you get horizontal scaling where capacity is added without repartitioning the whole dataset or taking it offline.

## Indexes stop being a static guess

Static B-tree indexes force teams to predict query patterns in advance and then maintain the structures by hand as schemas evolve. He describes a progression from static indexes, to adaptive ones (partial indexing, automated suggestions, online rebuilds), to learned indexes, where a model replaces part of the tree. In between sit the tools many teams already have: partial, covering, multi-column, spatial and inverted indexes, chosen from observed query behaviour.

The reminder engineers need most: indexes are not free. Every index speeds up reads and costs storage and write overhead, so indexing is an ongoing optimization problem. Cloud-native engines increasingly run index advisors that suggest additions and removals and rebuild in the background without blocking live transactions.

## ML inside the engine

The third chapter covers machine learning in the database itself. Workload managers classify queries and allocate resources before contention builds, and spot anomalies early, which matters most in multi-tenant systems. Adaptive query processing learns from execution history instead of trusting static cost models whose statistics go stale. To measure any of this he points to OLTP-Bench for simulating realistic workloads and iTuned for ML-driven configuration tuning. The pieces reinforce each other: partitioning reduces skew, indexing speeds queries, and ML keeps tuning both.

## Let it observe before it acts

The section that keeps this grounded is on guardrails. Self-optimizing systems bring new failure modes along with their benefits, so production adoption needs governance over when the system may act on its own: rollback safety, a human-in-the-loop mode, threshold guardrails and an observation-first stance. His rollout path is three steps: observe, then enable advisory mode, then automate selectively. That is the right order for any team that has watched an automatic tuner make a confident, wrong decision at peak load.

The abstract lists a set of benchmark percentages for these techniques; the recording does not walk through them, so check the slides if you need the figures.

## Who should watch

Backend engineers and DBAs moving workloads to managed or distributed databases, and architects deciding how much autonomy to grant a self-tuning engine. If you want query plans and EXPLAIN output, this talk stays at the architecture level.

## Related Conf42 talks

- [Karthickram Vailraj on database sharding and replication for fintech platforms](https://www.conf42.com/Platform_Engineering_2025_Karthickram_Vailraj_sharding_replication_database) at Conf42 Platform Engineering 2025.
- [Amarachi Iheanacho's 30-day experiment on whether a Kubernetes operator can replace a DBA](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning) at Conf42 Database DevOps 2026.
- [Ahmed Tariq on when AI helps and hurts with schema migrations in CI/CD](https://www.conf42.com/Database_DevOps_2026_Ahmed_Tariq_postgres_mysql_scaling) at Conf42 Database DevOps 2026.

[Watch Purushotham Jinka's talk](https://www.conf42.com/Cloud_Native_2026_Purushotham_Jinka_ai_llm_optimization)

[Watch the talk on YouTube](https://youtu.be/Lb4yWF46NhY).

## Watch the talk

[Database Evolution: Partitioning and Indexing for Cloud-Native Systems](https://www.conf42.com/Cloud_Native_2026_Purushotham_Jinka_ai_llm_optimization) at Conf42 Cloud Native 2026.
