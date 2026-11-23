# Building a data mesh in Rust with Kafka, Arrow and actors

Conf42 Blog, 2025-07-28, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-data-mesh-kafka-arrow-actors

In short: Narendra Reddy Mudiyala of Accenture at Conf42 Rustlang 2025 on the Rust toolkit for data mesh pipelines, from rdkafka and Serde to actors and Wasm.

Data mesh is an org chart idea: give each domain ownership of its data products. Narendra Reddy Mudiyala's talk at Conf42 Rustlang 2025 is about the plumbing that idea needs, and why he builds it in Rust. Narendra, a senior data engineer at Accenture, walked through the crates, patterns and cloud integration choices behind high-throughput, domain-owned pipelines.

It is a toolkit talk. You leave with a list of specific libraries and patterns rather than a single big claim, which is exactly what you want if you are about to start one of these platforms.

## Why the monolith breaks first

Narendra's starting point is familiar: data volumes grow faster than a central platform team can scale, and the monolithic pipeline becomes the bottleneck every domain queues behind. Data mesh decentralizes ownership to the domain experts who understand the data. That only works if each domain's pipelines are fast and reliable enough to run without a central team babysitting them, and that is the job he gives to Rust.

His reasons are the three you would expect, framed for data work: ownership rules out data races in concurrent processing code, zero-cost abstractions keep high-level transformation code fast, and the type system kills null-pointer and data-mismatch bugs that would otherwise show up as 3am pipeline failures.

## The pipeline toolkit, named

The concrete part is the best part. For processing:

- **Tokio** as the async runtime, so ingestion, transformation and output run concurrently without blocking threads.
- **Serde** for serialization with fewer copies, which matters when serialization is the hidden bottleneck.
- **Apache Arrow** for columnar operations, which Narendra uses for fast analytics on large datasets compared to row-based tooling.

For infrastructure:

- **rdkafka**, the Rust wrapper around the battle-tested librdkafka C library, for high-throughput Kafka consumers.
- **Iterators and zero-allocation patterns** for transformations, so data streams through without piles of temporary objects.
- **Axum with Tower middleware** for the HTTP APIs that expose data products to other domains.

## Benchmark honestly, then choose per component

One section deserves more attention than it usually gets. Narendra described running real-world benchmarks on actual production-shaped workloads, comparing Rust against Python, Java and Scala on latency, throughput, memory, startup time and consistency under load.

His conclusion is not "rewrite everything". Rust often wins for the performance-critical parts, such as real-time event processing and heavy transformations, while another language may be the right call for less time-sensitive components where development speed or ecosystem matter more. Benchmarking, in his phrase, keeps you honest.

## Three patterns for a distributed mesh

The advanced section names three patterns that fit a mesh well:

- **Actor model**: each actor owns its state and communicates by message passing, a natural way to isolate domains, made safe by Rust's concurrency guarantees.
- **Custom derive macros**: enforce validation on incoming data structures across the codebase, so every developer gets it for free rather than remembering to write it.
- **WebAssembly sandboxes**: compile parts of the processing into Wasm modules and run them isolated, useful when data crosses domain or even organizational boundaries.

He closed on data contracts enforced at compile time between microservices, which is the most mesh-specific idea in the talk: if the shape of a data product is a Rust type, a breaking change is a build failure, not a downstream incident.

## Who should watch

Data engineers designing domain-owned pipelines or evaluating Rust for the hot paths of an existing platform. It is a broad survey, so expect a map of tools and patterns rather than deep code.

## Related Conf42 talks

- [Data Mesh Unleashed: scalable architectures for AI-driven enterprises](https://www.conf42.com/Golang_2025_Arun_Vivek_Supramanian_data_mesh_ai) by Arun Vivek Supramanian: data mesh from the Go side.
- [Scaling Kafka on Kubernetes for 100,000+ messages per second](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable) by Shalini Katyayani Koney: running the Kafka the consumers read from.
- [Using Rust and WASM](https://www.conf42.com/Rustlang_2024_Andrey_Makarov_wasm_assembly_code_web) by Andrey Makarov: the Wasm half of the sandbox pattern.

[Watch Narendra Reddy Mudiyala's talk](https://www.conf42.com/Rustlang_2025_Narendra_Reddy_Mudiyala_memory_safety_systems)

[Watch the talk on YouTube](https://youtu.be/D3-xe2cxq4U).

## Watch the talk

[Building High-Performance Data Mesh with Rust: From Monolithic Bottlenecks to Distributed Excellence](https://www.conf42.com/Rustlang_2025_Narendra_Reddy_Mudiyala_memory_safety_systems) at Conf42 Rustlang 2025.
