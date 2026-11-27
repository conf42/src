# FinTech databases need different consistency for different money

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/fintech-databases-mix-consistency-models

In short: Karthickram Vailraj of Charles Schwab covers sharding, replication and consistency choices for FinTech platforms at Conf42 Platform Engineering 2025.

In most systems, eventual consistency means a like count is briefly wrong. In finance it can mean a balance is briefly wrong, which is a very different support ticket. At Conf42 Platform Engineering 2025, Karthickram Vailraj, Senior Manager at Charles Schwab, walks platform engineers through how distributed databases in FinTech are sharded, replicated and given different consistency guarantees depending on what the data is for.

The talk is a structured survey: foundations, sharding, replication, consistency, architecture patterns, security and a few case studies. It is a good refresher for anyone about to design storage for payments, trading or digital banking.

## Why finance is a special case

Vailraj sets the requirements first. Calculations allow zero margin for error and regulators require comprehensive logging. Load spikes come from market events, product launches, tax season and heavy trading days. Data residency laws vary by country while customers still expect low latency everywhere. High-frequency trading wants microseconds, digital banks want millions of concurrent users, and payment processors settle across currencies and jurisdictions. Monolithic databases do not stretch that far, which is how the industry ended up with distributed ones.

## Three ways to slice the data

Sharding enables linear scaling, and the hard part is keeping transactions intact across shard boundaries. He describes three strategies:

- **User-based sharding** keeps all of one customer's data on one shard, so most operations stay local. The catch is the operation finance exists for: moving money from one account to another, which may cross shards and needs distributed transaction management.
- **Geographic or regulatory sharding** aligns data placement with residency law. Cross-border payments then need routing logic and coordination protocols.
- **Time-based sharding** partitions historical transactions by date range, keeping recent data on fast shards while statements, tax records and archives live elsewhere.

He flags rebalancing as one of the hardest operational problems, because user bases grow unevenly and transaction patterns shift.

## Synchronous where it hurts, asynchronous where it doesn't

Replication gets the same trade-off treatment. Synchronous replication means every replica confirms before a transaction completes, so any replica can take over without data loss, at the cost of latency, especially across regions, and with extra conflict-resolution pain in multi-master setups. Asynchronous replication commits to the primary and propagates later, cutting write latency and enabling geographic read distribution, but you must monitor replication lag and handle conflicts.

The pattern he recommends is hybrid, based on data classification: critical financial data replicates synchronously within a region and asynchronously across regions, while less critical data can be asynchronous throughout. Consistency follows the same logic. Strong consistency for core banking, trading and payments; eventual consistency for analytics, reporting and customer-facing views; and causal consistency as a middle ground for multi-step workflows where related operations must stay ordered but unrelated ones need not.

## Patterns that come with an audit trail

On architecture, he groups event-driven design with Kafka at the centre, microservices with domain-driven boundaries and a service mesh, and CQRS paired with event sourcing. The FinTech-specific selling point of event sourcing is that the event log is the audit trail regulators ask for, and you can rebuild new read models from history later. Security covers encryption at rest and in transit, hardware security modules for keys, role- and attribute-based access, MFA and row- and column-level security.

The case studies are anonymised: an investment bank combining synchronous replication within a region and asynchronous across regions, a digital bank sharding by geography and account type with event sourcing, and a payment network sharding by geography and merchant with real-time fraud detection.

## Who should watch

Backend and platform engineers designing or reviewing storage for anything that moves money, and SREs who want the vocabulary to argue about replication lag with their DBAs. It is an overview rather than a deep implementation talk, so pair it with something hands-on.

## Related Conf42 talks

- [Kube-Native Sharding: Multi-Zone Service Architecture for 99.99% Uptime](https://www.conf42.com/Kube_Native_2025_Rahul_Singh_Thakur_sharding_uptime_architecture) by Rahul Singh Thakur, Conf42 Kube Native 2025
- [An Introduction to Saga Pattern for Distributed Transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) by Dmitry Khorev, Conf42 Cloud Native 2023
- [Zero Downtime, Zero Excuses: Scaling Fintech Infrastructure That Never Blinks](https://www.conf42.com/Golang_2025_Srinivas_Reddy_Mosali_fintech_infrastructure_scaling) by Srinivas Reddy Mosali, Conf42 Golang 2025

[Watch Karthickram Vailraj's talk](https://www.conf42.com/Platform_Engineering_2025_Karthickram_Vailraj_sharding_replication_database)

[Watch the talk on YouTube](https://youtu.be/EE5FcTA_n7w).

## Watch the talk

[Platform Engineering for FinTech: Database Sharding, Replication & Scale](https://www.conf42.com/Platform_Engineering_2025_Karthickram_Vailraj_sharding_replication_database) at Conf42 Platform Engineering 2025.
