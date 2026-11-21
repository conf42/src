# Scaling a trading platform means optimising for change

Conf42 Blog, 2025-08-07, updated 2026-11-09. https://www.conf42.com/blog/platform2025/athena-trading-platform-scaling-lessons

In short: Aroma Rodrigues at Conf42 Platform Engineering 2025 on how J.P. Morgan's Athena moved from a monolith to dependency graphs, delta storage and parallel books.

In most systems data grows; in finance it mutates, constantly and in dependent chains. At Conf42 Platform Engineering 2025, Aroma Rodrigues, now a software engineer at Microsoft, told the story of Athena, J.P. Morgan's trading platform, and how it went from barely handling thousands of trades to millions a day. Her main lesson for platform engineers: optimize for change, not just scale.

It is one of the more technical talks of the event and worth the full length, mostly because it explains the finance domain well enough that the architecture decisions make sense.

## Trades, deals and books

Aroma starts with vocabulary. A trade is the atomic market event: trader one buys a hundred units of a corporate bond from trader two. That one trade creates multiple deals, mirror images in each side's book. A book is a ledger of credits and debits grouped by desk and product. Each behaves differently: trades are written once and read often, deals update as markets move, books must be aggregated and reported in real time. Then the trade flows through front office (execution), middle office (validation, enrichment, risk), back office (settlement) and books and P&L, each with different performance, consistency and failure profiles.

Her numbers make the point: front-office bursts of around 10,000 transactions per second in volatile markets, middle-office validation within 30 seconds for regulatory reasons, settlement that may take days.

## The monolith with regulators on top

The starting architecture was single everything: one ingestion instance, one app node, one primary database without replicas or sharding, mixed OLTP and OLAP on the same tables, everything synchronous. Heavy recalculations ran as nightly cron batches of eight to 12 hours, so a failure at 3am meant traders started on stale data. There was no backpressure, a single region (painful for London and Hong Kong traders), and compliance data was just extra rows in the operational database. Storing full daily snapshots of every deal meant terabytes of near-duplicates, and peak-hour lock contention did the rest.

## Recalculate only what changed

The first breakthrough was a dependency graph. Functions are marked with dependency decorators: a position value depends on an instrument and market data, a base-currency value depends on that position and FX rates. When an instrument price moves, the graph finds every calculation downstream of it and updates only those. That single change took end-of-day processing from eight hours to five and made near-real-time P&L feasible.

The second was delta storage: keep the full deal record once, then store only changed fields per day, keep the current head state for processing, and rebuild any point-in-time view by applying deltas. Regulators asking for the full history of one deal across a corporate action that turned it into a different instrument get an answer without full snapshots.

## Books in parallel, compliance apart

Data is geo-distributed, with primary hubs in New York and London, each with three local replicas, synchronous replication within a region and asynchronous between regions. Because trading is mostly regional and tied to legal entities, books can be processed independently; cross-entity trades get a third deal stored in a separate instance so the regional sets stay parallel.

End-of-day became a dependency-aware pipeline: reference data for instruments first, then book processing per book, then P&L once all books finish, with retries per failed book using cached results. Compute building blocks, described as Lambda-like nodes that load a book into their own memory and return results, give horizontal scale without loading the main servers. Operational and compliance data were physically separated, with trades and price changes streamed to immutable audit logs.

Why it matters: a buggy Python analytics script once choked a queue, deals missed their regulatory window, and the result was a hundred-thousand-dollar fine.

## Why Python, and the pitfalls

She also defends Python: duck typing handles bonds, swaps and credit default swaps without rigid schemas, and hot paths drop to C++. Her pitfalls list is honest: optimising the wrong bottleneck before profiling, bolting on data lineage late, and underestimating the operational cost of multi-region systems.

## Who should watch

Engineers on financial, ledger or any heavily audited platform, and anyone whose data model keeps fighting their relational schema. Read it as an architecture story, not a product pitch.

## Related Conf42 talks

- [Janardhan Chejarla on event-driven, cloud-native order management for high-frequency trading](https://www.conf42.com/DevSecOps_2025_Janardhan_Chejarla_trading_cloud_scale) at Conf42 DevSecOps 2025.
- [Nikita Melnikov on the actor model in financial transaction systems](https://www.conf42.com/Platform_Engineering_2024_Nikita_Melnikov_concurrency_actor_financial) at Conf42 Platform Engineering 2024.
- [Ganesh Marimuthu on observability in treasury trading platforms](https://www.conf42.com/Observability_2025_Ganesh_Marimuthu_trading_treasury_platforms) at Conf42 Observability 2025.

[Watch Aroma Rodrigues's talk](https://www.conf42.com/Platform_Engineering_2025_Aroma_Rodrigues_morgan_athena_compliant), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/VKnR7nj3968).

## Watch the talk

[Engineering Athena: Building a Scalable, Resilient, and Compliant Financial Platform at J.P. Morgan](https://www.conf42.com/Platform_Engineering_2025_Aroma_Rodrigues_morgan_athena_compliant) at Conf42 Platform Engineering 2025.
