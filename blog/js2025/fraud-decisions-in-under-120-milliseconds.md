# Real-time data systems that decide on fraud in milliseconds

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/fraud-decisions-in-under-120-milliseconds

In short: Lakshmi Bhargavi Mullapudi of Techstar Group mapped the Kafka, Flink and ClickHouse stack behind real-time apps at Conf42 JavaScript 2025.

A card transaction can be ingested, enriched, scored by a model and blocked in 80 to 120 milliseconds, if every stage of the pipeline is built for it. At Conf42 JavaScript 2025, Lakshmi Bhargavi Mullapudi, a software engineer at Techstar Group, walked through the architecture that makes that possible, from event ingestion to the WebSocket that updates the dashboard.

It's a short, dense reference talk: one slide per layer, with the trade-offs named.

## Five layers, one latency budget

Her pipeline is ingest, process, store, deliver. For ingestion she compares Apache Kafka (a distributed log with strong ordering per partition and a big connector ecosystem) with AWS Kinesis (managed, auto-scaling, less to operate, built-in retention and replay). Both handle millions of events per second when configured well; the choice comes down to throughput needs, operational appetite and what you already run.

For stream processing: Apache Flink as a true streaming engine with exactly-once semantics, stateful operators and event-time processing, against Spark Structured Streaming's micro-batches with good SQL support for teams already on Spark.

For serving queries, Apache Druid for time-series aggregations across billions of events behind live dashboards, and ClickHouse for analytical SQL at scale with strong compression and vectorised execution.

## The fraud case study

The worked example shows where the milliseconds go. Transactions land in Kafka topics with about 10 ms latency. They're joined in flight with user profiles, historical patterns and risk codes. A lightweight model scores the feature vector within 50 ms. High-risk transactions are blocked and the security team is alerted. End to end: 80 to 120 ms from transaction to decision.

## Where latency actually hides

Her low-latency rules are the part to keep:

- **Minimise network hops.** Each round trip adds roughly 1 to 5 ms, so co-locate processing and storage and avoid cross-datacentre calls.
- **Pick a better serialisation format.** Avro or Protocol Buffers instead of JSON; she noted serialisation can eat 20 to 30% of processing time in high-throughput systems. JavaScript developers, that one is aimed at you.
- **Batch small.** Micro-batches with 10 to 50 ms windows usually balance throughput and latency.
- **Cache strategically.** In-memory caches for hot data and lookup tables serve reads in microseconds.

For scale: partition with consistent hashing or range partitioning, keep services stateless and push state to Redis or a distributed store, and autoscale on consumer lag rather than CPU.

## Pick consistency per data type

She treats consistency as a business decision. Strong consistency for financial transactions, eventual consistency for analytics and recommendations, and tunable quorum reads and writes where the importance of a request varies. Many systems mix all three. Fault tolerance comes from checkpointing, replication, retries and circuit breakers that fail fast when downstream services degrade.

On the frontend, WebSockets or server-sent events push updates to the browser, GraphQL subscriptions fit teams already on GraphQL, and Redux, NgRx or Zustand handle streaming state in React, with normalised data to avoid unnecessary re-renders.

## Who should watch

JavaScript developers who are about to own a real-time feature and need a map of the backend it depends on, and anyone choosing between Kafka and Kinesis or Flink and Spark. Her closing advice works for everyone: define latency targets before picking tools, because not everything needs sub-second processing, and measure every stage, since latency in one component is latency for the whole system.

## Related talks

- [Demystifying Event-Driven Architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) explains the ingestion layer properly.
- [Cloud-Native Analytics: Transforming Big Data into Real-Time Product Insights](https://www.conf42.com/Cloud_Native_2025_Nimit_Bhardwaj_big_data_analytics_realtime_insights) covers the analytics end of the pipeline.
- [Building Real-time Pulsar Apps on K8](https://www.conf42.com/Kube_Native_2022_Tim_Spann_realtime_pulsar_apps_k8) is an alternative streaming stack on Kubernetes.

[Watch Lakshmi Bhargavi Mullapudi's talk](https://www.conf42.com/JavaScript_2025_Lakshmi_Bhargavi_Mullapudi_real_time_engineering)

[Watch the talk on YouTube](https://youtu.be/OlwF7CUHmSs).

## Watch the talk

[Real-Time Data Systems: Engineering for Speed, Scale, and Resilience](https://www.conf42.com/JavaScript_2025_Lakshmi_Bhargavi_Mullapudi_real_time_engineering) at Conf42 JavaScript 2025.
