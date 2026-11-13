# Adding nodes made p99 worse, so they routed to the data instead

Conf42 Blog, 2026-05-31, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/route-requests-to-node-owning-data

In short: Ritvik Pandya (JP Morgan Chase) at Conf42 Database DevOps 2026 on deterministic routing and thread affinity that cut p99 from 47 ms to 19 ms on the same hardware.

When p99 latency quadrupled at peak and the team added nodes, it got slightly worse. At Conf42 Database DevOps 2026, Ritvik Pandya, Engineering Manager at JP Morgan Chase, explains why: the problem wasn't capacity but coordination. Routing each transaction to the node that already owns its data, plus a few unglamorous Kubernetes settings, took p99 from 47 ms to 19 ms on the same hardware and database.

This is one of the most concrete talks of the event: a production story with a latency breakdown, the fix, the numbers and the places it doesn't work.

## The cluster was busy coordinating, not working

The baseline p99 was about 12 ms; at peak it hit 47 ms. Around 3.2% of requests timed out, clients retried, and the retries piled into a retry storm. With transaction volume expected to roughly double and the infrastructure budget not doubling with it, more hardware wasn't the answer anyway.

Tracing showed where the 47 ms went: roughly 12 ms resolving metadata to find where the data lived, 18 ms on cross-node coordination and replication acknowledgements, about 8 ms on lock contention, and about 4 ms on connections and network. Ritvik is careful to call these representative attributions from span-level analysis rather than exact maths, but the proportions were reproducible. Very little of the request path was actual transaction work. His analogy is a hospital where each visit gets a random doctor who first has to fetch your file from another department.

## Hash the key, land on the owner

The fix is deterministic routing: hash the transaction's primary key with the same partition key the database uses, and send it to the node most likely to hold that range. He's clear the idea isn't new; Dynamo-style partition-aware routing and Calvin's deterministic scheduling came first. What's different is applying it early, at the application and routing layer. The database (CockroachDB in their case, but the principle carries to Spanner, YugabyteDB, TiDB and DynamoDB) still handles correctness, replication and consensus. Routing just makes expensive coordination rarer on the hot path.

Two details matter. Use consistent hashing with virtual nodes, not modulo, so adding a node doesn't remap most of the keyspace and churn every cache. And choose the key carefully: stable, high cardinality, aligned with access patterns.

## Shared connection pools ate the gains

Routing was half the story. Their first multithreaded version shared a connection pool across threads and performed worse than the single-threaded baseline, because threads spent their time fighting over pooled connections. The fix was thread-to-node affinity: each worker thread owns a dedicated pool for its node group, with round-robin scheduling, async I/O and persistent connections.

## Burstable QoS was the hidden 15 ms

The best debugging story: staging benchmarks looked excellent, but production ran about 15 ms slower at comparable traffic. After weeks chasing network paths, database tuning and garbage collection, the culprit was Linux CPU throttling of containers in burstable QoS. Setting CPU requests equal to limits (guaranteed QoS) for latency-sensitive pods stabilised the tail. They also used StatefulSets for the database layer, co-located application pods near database nodes (same zone, sometimes same rack) and scaled on latency-aware signals instead of CPU.

The results: p50 from 18 ms to 8 ms, p95 from 34 ms to 14 ms, p99 from 47 ms to 19 ms, with throughput improving even more.

## Where determinism hurts

Ritvik spends real time on limits. Routing without resilience is fragile: when a node failed, every request mapped to it failed within seconds, so they added replica-aware failover and small queues for in-flight requests. Hot partitions still hash to one place and need splitting or dedicated capacity. Leaseholders move during rebalancing, so routing works on probability and must tolerate misses. Multi-key transactions see smaller gains. His homework for viewers: check your partition strategy, set requests equal to limits on latency-critical pods, measure p95 and p99 before and after, and track the share of requests landing on the right node.

## Who should watch

Anyone running a distributed SQL database behind a random load balancer, and anyone whose staging and production latencies mysteriously disagree on Kubernetes.

## Related Conf42 talks

- [Why Kubernetes Default Load Balancing Doesn't Work for HTTP/2 Traffic](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Mariem_Sboui_kubernetes_default_load) by Mariem Sboui, another case of default routing hurting latency.
- [Enhancing a Distributed SQL Database Engine: A Case Study on Performance Optimization](https://www.conf42.com/DevOps_2024_Alexey_Ozeritskiy_distributed_sql_database_optimization) by Alexey Ozeritskiy, the same problem from inside the engine.
- [When Gremlins Play with Cockroaches: A Chaos Experiment](https://www.conf42.com/Chaos_Engineering_2022_Rain_Leander_when_gremlins_play_with_cockroaches_a_chaos_experiment) by Rain Leander, for testing the failure cases Ritvik warns about.

[Watch Ritvik Pandya's talk](https://www.conf42.com/Database_DevOps_2026_Ritvik_Pandya_monitoring_telemetry_reliability)

[Watch the talk on YouTube](https://youtu.be/m7kohrY4oTM).

## Watch the talk

[Database DevOps at Scale: Deterministic Routing, Data Locality, and Performance Gains](https://www.conf42.com/Database_DevOps_2026_Ritvik_Pandya_monitoring_telemetry_reliability) at Conf42 Database DevOps 2026.
