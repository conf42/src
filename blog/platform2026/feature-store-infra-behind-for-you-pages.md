# The feature store behind every For You feed, explained

Conf42 Blog, 2026-10-10, updated 2026-11-09. https://www.conf42.com/blog/platform2026/feature-store-infra-behind-for-you-pages

In short: Attila Toth of ScyllaDB at Conf42 Platform Engineering 2026 on online feature stores, P99 tail latency, query-first data models and pluggable stores.

Every swipe on a For You feed is an event, and the next item you see depends on features fetched in a few milliseconds. At Conf42 Platform Engineering 2026, Attila Toth, developer advocate at ScyllaDB and a contributor to the Feast feature store project, walked through the infrastructure behind those feeds: offline and online stores, why P99 rules everything, and how to model data so one request hits one partition.

It's a vendor talk in the honest sense. The examples come from ScyllaDB users like ShareChat and its short-video app Moj, Medium, Tripadvisor and Agoda, and the design advice holds whichever database you pick.

## Two stores, two very different jobs

A feature is a signal the model uses to predict, attached to an entity: likes on a post in the last 10 minutes, shares in the last seven days. Attila's point is that you can invent endless variations (why 10 minutes and not 60?), so teams need one place to create, store and query them.

A feature store splits into an offline store for training, holding huge historical datasets, and an online store for real-time inference, serving a small feature vector per request under a strict latency SLA. He cites Tripadvisor at about 125 TB offline against 9 TB online in ScyllaDB. The organisational wins are reuse (one team's feature serves every model) and self-service: data scientists ship features without waiting on an engineering team.

## The page is as fast as its slowest lookup

The best slide is the tail latency maths. One user action fans out to many API calls and many database reads, and the page waits for the slowest. If a page does 100 lookups and each beats P99 with 99% probability, the chance all 100 are fast is 0.99 to the power 100, so about 63% of page loads wait for at least one slow lookup. That's why online stores are judged on P99, and why Attila recommends the Google paper The Tail at Scale.

## Design the table for the query

For low latency he flips relational habits. Start from the screen, write the queries it needs, then design one table per query, denormalising freely. Medium's published schema is his example: a narrow table with entity ID, feature key and value, so adding or dropping a feature never means a schema migration.

The primary key does the heavy lifting. Feature key plus entity ID form the composite partition key, so a query lands on exactly one partition. A clustering key sorted descending keeps the most recent items first on disk, so nothing gets re-sorted at read time.

He adds three more levers. Treat vector embeddings as features, stored in the same table with a vector index, instead of standing up a separate vector database. Use TTL so expired rows leave the hot store and history lives in cheaper storage like Parquet on S3. Pre-aggregate counts into time buckets with a stream processor such as Flink, as ShareChat does, instead of scanning raw events.

## Cache layers and spiky bills

On caching, Attila is candid about his bias: an external cache like Redis or DAX in front of a database means two systems to pay for and run, and ScyllaDB's pitch is an embedded cache in a persistent database. On cost, he points to autoscaling against a target utilisation so a sporting-event spike doesn't mean paying for peak capacity all year.

## Keep the online store pluggable

The Feast section ties it together. Feast keeps feature definitions in one place with one API, lets you plug in different offline stores (S3, Snowflake) and online stores (ScyllaDB, Redis, DynamoDB), and now supports vector search. His final takeaway is to keep the online store swappable: if it can't meet your P99, you want to change the database, not the whole architecture.

## Who should watch

Platform and data engineers building recommendation or personalisation backends, and anyone who has watched a feed page stall on one slow read. The CQL examples are ScyllaDB and Cassandra flavoured; the reasoning travels.

## Related Conf42 talks

- [ML-Powered Search & Recommendation 101: From Core Concepts to Scalable Systems](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) by Sergey Polyashov at Conf42 Machine Learning 2025.
- [RAG in production: challenges, techniques and solutions](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) by Alejandro Duarte at Conf42 Database DevOps 2026.

[Watch Attila Toth's talk](https://www.conf42.com/Platform_Engineering_2026_Attila_Toth_personalization_infra_pages) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/KCmFRH9CVwo).

## Watch the talk

[The hidden infra behind "For You" pages: Real-time AI personalization](https://www.conf42.com/Platform_Engineering_2026_Attila_Toth_personalization_infra_pages) at Conf42 Platform Engineering 2026.
