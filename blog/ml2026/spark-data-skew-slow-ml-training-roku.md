# Your ML pipeline is slow because of data skew, not bad code

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/spark-data-skew-slow-ml-training-roku

In short: Srihari Godleti (Roku) at Conf42 Machine Learning 2026 shows how repartitioning, key salting and broadcast joins tame Spark data skew in ML pipelines.

A Spark stage finishes when its slowest task finishes, and in a streaming company one power user can be that task. At Conf42 Machine Learning 2026, Srihari Godleti, a data and ML engineering leader at Roku, explained how data skew turned retraining jobs that ran in about 40 minutes into nearly three-hour runs with no code or infrastructure change, and the three techniques his team uses to fix it.

This is a practical, code-snippet talk about Apache Spark in ML feature pipelines. Bring your Spark UI.

## The symptom is one executor doing all the work

Roku processes billions of watch events and ad impressions a day, and every play, pause and ad click feeds Spark pipelines for personalisation, embedding generation and ad ranking. When the jobs slowed down, the Spark UI told the story: around 95% of tasks finished quickly while one executor ran far longer, processing more than ten times the shuffle data of its peers. Shuffle spills went up, garbage collection paused, that one CPU sat at 100% and everyone else idled.

The cause is the mismatch between Spark's hash partitioning and real behaviour, which follows a power law. One viewer has two interactions, another has 150. Group by user and the heavy one owns a partition. Godleti adds that in ad ranking his team has seen skew cost around 20% efficiency, which at that scale becomes a real line on the cloud bill, plus stale recommendations because retraining finishes late.

## Skew comes from three places

He sorts root causes into natural imbalance, join and aggregation keys, and computational skew. Natural imbalance is the world being lumpy: the Super Bowl, a Formula One race, a viral show, regional and seasonal patterns. Join-key skew appears when user features meet behavioural data and a few very active IDs dominate, and groupBy or reduceByKey aggregations (especially daily and weekly rollups) concentrate it further. Computational skew is the sneaky one: even with evenly sized partitions, variable-length documents, embedding generation or high-cardinality transformations make some rows far more expensive than others.

His point is that skew is a property of the data, not a bug in the system, so it belongs in the pipeline design from the start.

## Three fixes, in order of escalation

**Repartition** for moderate skew: explicitly redistribute on a column with a chosen partition count before expensive joins and aggregations. His rules of thumb are a partition count of two to three times the total cores and partitions of roughly 100 to 200 MB. It adds a shuffle and does nothing about key frequency, but his team saw about a 30% improvement in preprocessing stages.

**Salt the hot keys** when one value dominates: append a small random suffix to heavy user IDs so a single key becomes several, aggregate, then aggregate again. That second stage is the price. In Roku's case a large partition dropped from about 8 GB to around 600 MB and some training runtimes fell by nearly half.

**Broadcast the small side** of a join so the large behavioural table never shuffles. Keep the broadcast table small (he cites 10 MB as the typical limit) and below roughly a fifth to a quarter of executor memory to avoid GC pressure. One enrichment stage went from about 90 minutes to close to 10.

The abstract's headline is pipeline times cut by about 40%. The talk's own advice is to apply these selectively to the stages that are actually skewed instead of over-engineering the whole pipeline.

## Where it goes next

Godleti closes with work in progress: models trained on historical Spark metrics to predict skew risk before a stage runs and recommend partition counts, salting factors and broadcast strategies. It is framed as an experiment, so treat it as a direction rather than a result.

## Who should watch

Data and ML engineers who own Spark feature pipelines and keep seeing one task bar stretch across the timeline. If you already salt keys in your sleep, the numbers are still a nice sanity check. If you have never opened the Spark UI's stage view, watch this and then open it.

## Related Conf42 talks

- [Optimising Apache Spark and SQL for improved performance](https://www.conf42.com/Machine_Learning_2024_Marcin_Szymaniuk_apache_spark_sql) by Marcin Szymaniuk (TantusData) covers the wider Spark tuning toolbox.
- [Enriching the data vs Filtering in Spark](https://www.conf42.com/Cloud_Native_2024_Gokul_Prabagaren_enriching_datasets_apache) by Gokul Prabagaren (Capital One) looks at another join-heavy design choice.
- [Cloud-Native ML Infrastructure: Building Resilient Apache Spark Clusters on Kubernetes for AI Workloads](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters) by Anant Kumar (Salesforce) is about the clusters underneath.

[Watch Srihari Godleti's talk](https://www.conf42.com/Machine_Learning_2026_Srihari_Godleti_fairness_bias_mitigation)

[Watch the talk on YouTube](https://youtu.be/3v0HBn70M3Q).

## Watch the talk

[Taming Data Skew in Production ML Pipelines: Practical Apache Spark Optimization Techniques](https://www.conf42.com/Machine_Learning_2026_Srihari_Godleti_fairness_bias_mitigation) at Conf42 Machine Learning 2026.
