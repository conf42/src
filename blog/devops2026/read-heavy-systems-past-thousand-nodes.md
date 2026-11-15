# Past a thousand nodes, more hardware stops buying read throughput

Conf42 Blog, 2026-01-02, updated 2026-11-09. https://www.conf42.com/blog/devops2026/read-heavy-systems-past-thousand-nodes

In short: Ivan Sinitsin (Ozon) at Conf42 DevOps 2026 on tail latency, connection storms, binary formats, CQRS projections and sharded in-process caches.

The standard Kubernetes, microservices and sharded-cache stack scales linearly right up until it doesn't. At Conf42 DevOps 2026, Ivan Sinitsin, Golang tech lead at Ozon, explained what goes wrong in read-intensive systems once you cross roughly a thousand nodes, why the usual painkillers only mask it, and how his target architecture ends up serving most reads from local memory with only about 1% reaching the databases.

This is a dense, opinionated systems talk. It moves from network math to CPU cache lines to data-locality routing, and it ends with an honest bill for the complexity.

## The tax nobody puts on the diagram

Sinitsin's list of large-scale failures starts with tail latency. A single search query might fan out to 50 database shards, and the response is only as fast as the slowest one. At scale, the rare anomaly becomes daily statistics.

Then there is the orchestration tax. Control planes, service discovery and gossip-style protocols eat a growing share of CPU and network, until management traffic competes with users. His example: add 20% more hardware and get only about five percent more performance.

The memorable bit is the connection math. With 1,000 application pods each opening a pool to each of 100 cache nodes, you have around 100,000 open connections, enough to exhaust file descriptors and hammer the top-of-rack switch. The system, as he puts it, chokes itself.

He also reminds SREs where to live on the latency-versus-throughput curve: the linear zone, with enough margin to absorb spikes, well before the inflection point where queues form.

## Painkillers help you survive, not scale

The first response he describes is the familiar one: graceful degradation, circuit breakers, soft timeouts and serving stale data. If a database doesn't answer within 20 milliseconds, kill the connection and serve a partial response. After that comes zonal isolation, duplicating the whole stack per availability zone so a zone failure stays local, at the cost of roughly tripled resources and harder synchronisation.

Sinitsin's warning is that a dashboard full of green after all this is an illusion of stability. The symptoms are masked; the inefficiency underneath is untouched.

## Make the bytes cheaper

The cure starts at the lowest level. He sees waste in three places: processing (CPU spent deserialising more than running business logic), transfer (keys and metadata repeated in every request) and storage (reading a whole row to get one column). His prescriptions are binary formats over text, zero-copy access that maps data straight into memory and skips garbage collection pressure, reading only the fields you need, and stripping schemas and field names out of payloads via a central registry.

He goes one layer further, to memory layout: grouping data into developer-friendly objects often pollutes CPU cache lines. No layout wins everywhere, so profile and pick the one that fits your access pattern.

## Projections, local caches and smart routing

Architecturally, he reaches for CQRS: keep one source of truth and generate read projections tailored to each consumer, carrying only the fields and format that consumer needs. Then move those projections into the service's own memory, where access costs nanoseconds instead of a network hop.

Caching everything in every pod would blow up memory, so pods become shards. Service discovery tracks topology in real time, client-side balancing skips the extra hop, and consistent hashing ensures that requests for a given ID always land on the same pod. Storage formats differ by tier: compact and backward-compatible for external storage, native runtime structures in process. FlatBuffers on the wire, native objects inside, is one of his examples.

## The bill

The result in his comparison: instead of every request hitting external caches, about 85% are served from local memory and only 1% reach the databases, which means far fewer servers and much lower cross-AZ traffic. The cost is a system that is harder to maintain, with a thinner safety margin and monitoring that needs surgical precision. His closing advice is the right one: make sure you are fighting physical hardware limits, not suboptimal code.

## Who should watch

Engineers running high-fanout read paths in Go or any runtime where serialisation shows up in profiles. Small services can skip it with a clear conscience. If you have ever doubled a cache cluster and watched p99 stay put, this explains why.

## Related Conf42 talks

- [High-Load Systems: Overcoming Challenges in Social Network Development](https://www.conf42.com/Platform_Engineering_2024_Alexandr_Kolobov_highload_systems_development) by Alexandr Kolobov (VK) covers similar scale from a social network.
- [Architectural Caching Patterns for Kubernetes](https://www.conf42.com/Cloud_Native_2021_Rafal_Leszko_architectural_caching_patterns_kubernetes) by Rafal Leszko (Hazelcast) is a good primer on where a cache can live in a cluster.
- [Building Self-Healing Cache Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) by Shailin Saraiya (Roku) treats the cache layer as a platform of its own.

[Watch Ivan Sinitsin's talk](https://www.conf42.com/DevOps_2026_Ivan_Sinitsin_architecture_throughput_databases)

[Watch the talk on YouTube](https://youtu.be/wTvEDu-12vQ).

## Watch the talk

[Designing a Read-Intensive Architecture for Information Systems with High Data Throughput](https://www.conf42.com/DevOps_2026_Ivan_Sinitsin_architecture_throughput_databases) at Conf42 DevOps 2026.
