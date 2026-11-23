# How Rust took over the lakehouse, from Arrow to DataFusion

Conf42 Blog, 2025-07-27, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-lakehouse-arrow-datafusion-delta

In short: Rahul Joshi of Capital One at Conf42 Rustlang 2025 traces data platforms from Hadoop to lakehouses and shows where Rust components now sit in the stack.

The JVM carried big data for fifteen years; the newest layer of the lakehouse stack is increasingly written in Rust. At Conf42 Rustlang 2025, Rahul Joshi, Distinguished Data Engineer and Director at Capital One, walked through three eras of enterprise data architecture and showed exactly which pieces of a modern lakehouse Rust now powers.

Rahul brings about 20 years of building data platforms in financial services, and it shows: the talk is a clear history lesson that ends in a practical adoption plan.

## Phase one: Hadoop and the JVM tax

The story starts in the on-premise Hadoop era: HDFS and MapReduce, everything on the JVM. It worked at scale, but Rahul listed the costs plainly. Each task needed its own heap, object headers added bytes to every record, data exchanged between map and reduce tasks had to be serialized and deserialized at every hop, and garbage collection pauses of seconds made run times inconsistent.

His benchmark slide compared word count, the hello world of big data, across Hadoop, Spark and DataFusion, with the Rust engine finishing far ahead. The point is not the toy workload; it is that removing GC and serialization overhead changes the resource profile of the whole job.

## Phase two: warehouses fixed usability and added lock-in

Cloud warehouses such as Snowflake and Redshift solved much of Hadoop's usability problem with SQL-friendly analytics. The catch, as Rahul framed it, was proprietary storage formats: you pay compute to load data, compute to query it, and egress to take it out again. Storage and compute were coupled, and ML workloads usually meant copying data somewhere else, creating silos.

## Phase three: the lakehouse, with Rust in the engine room

The lakehouse merges the two with open table formats (Delta Lake, Apache Iceberg, Apache Hudi) on object storage, ACID transactions, schema evolution, time travel, and separate scaling of storage and compute.

This is where the Rust inventory comes in, and it is the slide worth screenshotting:

- **Table formats**: Rust libraries for Delta and Iceberg that let you read and write tables without spinning up Spark.
- **Columnar storage**: Apache Arrow's Rust implementation for zero-copy columnar memory, plus parquet-rs and Lance for storage.
- **Query processing**: Apache DataFusion for SQL and DataFrame APIs with parallel execution and a small footprint.
- **DataFrames**: Polars on top of Arrow.

Rahul quoted recent benchmarks for these: big query-speed gains for DataFusion over Spark on the same hardware, large memory savings for Polars over pandas on a 100 GB dataset, and much faster Parquet loading with arrow-rs than with PyArrow. These come from published and internal tests rather than a live demo, and as always your workload will have opinions.

## Start with the bottleneck, not the rewrite

The practical section is the strongest. Rahul described three integration styles: Rust microservices for the critical processing components, native extensions for Python or JVM code that keep the existing interface, and full replacement of a pipeline for maximum benefit.

His recommendation is the boring correct one. Most organizations start by replacing components already identified as bottlenecks, such as high-throughput ingestion, heavy feature engineering for ML, or interactive SQL that needs sub-second response, and only then consider rewriting more. Measure first, swap the hot path, repeat.

## Who should watch

Data platform engineers and architects deciding where Rust belongs in their stack, and anyone who wants a crisp narrative of how we got from MapReduce to the lakehouse. It is light on code and heavy on architecture.

## Related Conf42 talks

- [LanceDB: an OSS serverless vector database in Rust](https://www.conf42.com/Rustlang_2023_Lei_Xu_lancedb_oss_serverless_vector_db) by Lei Xu: the Lance format Rahul mentions, from the people who build it.
- [Bring your DataOps to the Data Lakehouse](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) by Jorge Loaiciga Rodriguez: running a lakehouse once it exists.
- [Enterprise Data with Lakehouse Architecture at Scale](https://www.conf42.com/Remix_2026_Richa_Solanki_data_lakehouse_enterprise) by Richa Solanki: another enterprise migration story.

[Watch Rahul Joshi's talk](https://www.conf42.com/Rustlang_2025_Rahul_Joshi_memory_rust_tech)

[Watch the talk on YouTube](https://youtu.be/_ik05WKiMnE).

## Watch the talk

[Rust-Powered Data Lakes: Building High-Performance Infrastructure for the Modern Lakehouse Era](https://www.conf42.com/Rustlang_2025_Rahul_Joshi_memory_rust_tech) at Conf42 Rustlang 2025.
