# Same SQL, three engines, three answers

Conf42 Blog, 2026-05-25, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/same-sql-three-engines-three-answers

In short: Muthupalaniappan Ramanathan (DoorDash) at Conf42 Database DevOps 2026 on catching semantic drift across Spark, Trino and Snowflake in CI.

A query that compiles and runs on every engine in your stack can still return a different number on each one. At Conf42 Database DevOps 2026, Muthupalaniappan Ramanathan, Senior Software Developer at DoorDash, makes the case that "SQL compatibility does not equal semantic consistency", and shows a DevOps framework for catching the difference at commit time instead of on a dashboard.

It's a compact talk, under twenty minutes, and it stays at framework level: no code walkthrough, but a clear testing strategy you can copy.

## Why you have three engines in the first place

Muthupalaniappan starts from the multi-engine reality: teams run Spark, Trino and Snowflake side by side because ETL pipelines, ad hoc exploration and real-time dashboards each favour a different runtime. That flexibility is reasonable. The cost is that the same SQL string can produce three answers, and standard SQL linting and schema tests won't notice.

## Where the divergence hides

The engines aren't buggy; they made different, deliberate design choices. He groups the differences into four:

- **Type handling:** implicit casts, numeric precision and integer overflow.
- **Null semantics:** how nulls propagate through joins and aggregations.
- **Aggregation behaviour:** floating point summation order and distinct-count edge cases.
- **Optimizer decisions:** rewrites that can silently change which rows are included or how results are ordered.

Each is small. Compounded across a few hundred pipelines and an engine upgrade or two, they become analytical drift: two teams with two "correct" revenue numbers.

## Write the meaning once

The core idea is analytical intent as a first-class abstraction. Instead of writing engine-specific SQL, you declare what the query means in engine-agnostic terms. A canonical semantic layer translates that intent into each dialect using deterministic rules, and humans never write dialect-specific SQL by hand. That removes handcrafted drift between copies and keeps one source of logical truth.

## Then make CI prove it

A semantic layer alone isn't enough, he argues; it has to be enforced. Every commit or schema change triggers a semantic diff and a cross-engine dry run, and an equivalence assertion has to pass before merge. Drift becomes a PR blocker rather than a production data incident.

The four test types are the most reusable part of the talk:

1. **Equivalence tests** assert identical results across engine pairs on a reference dataset.
2. **Null boundary tests** exercise rare but critical null paths.
3. **Precision regression tests** keep floating point aggregations within a set tolerance across engine upgrades.
4. **Translation snapshot tests** pin the generated SQL so an unintended compiler change shows up as a diff.

Merge-time checks don't end the job. In production he runs queries across engine pairs, compares result fingerprints, alerts on metric divergence and uses lineage-aware attribution to find the source of a drift. Trust in the numbers, in his framing, is an operational property you enforce, not a feature you ship once.

## Who should watch

Data platform engineers running more than one query engine, and anyone planning an engine migration who wants a test harness for "did the numbers change?". If you run a single warehouse, the null and precision tests still make a good checklist for your next upgrade.

## Related Conf42 talks

- [Closing the Semantic Gap with Feedback-Driven Ontology Learning](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) by Ravi Chandra, another approach to keeping analytical meaning consistent.
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu, validation patterns for the data feeding those queries.
- [Effective Observability in PostgreSQL, MySQL, and Other SQL Databases](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql) by Adam Furmanek, for watching what the engines actually do.

[Watch Muthupalaniappan Ramanathan's talk](https://www.conf42.com/Database_DevOps_2026_Muthupalaniappan_Ramanathan_queries_monitoring_sql)

[Watch the talk on YouTube](https://youtu.be/Q53T6LsIp_Y).

## Watch the talk

[Operationalizing Semantic Consistency: A DevOps Framework for Reliable Cross-Engine Analytics](https://www.conf42.com/Database_DevOps_2026_Muthupalaniappan_Ramanathan_queries_monitoring_sql) at Conf42 Database DevOps 2026.
