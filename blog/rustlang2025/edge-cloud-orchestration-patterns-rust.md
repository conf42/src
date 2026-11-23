# Two edge-cloud orchestration patterns, and why Rust runs the edge

Conf42 Blog, 2025-07-30, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/edge-cloud-orchestration-patterns-rust

In short: Karthik Mohan Muralidharan of Walmart Global Tech at Conf42 Rustlang 2025 on edge inference with cloud remediation and cloud insight with edge reconfiguration.

A 100 to 200 ms round trip to the cloud sounds fast until a robot needs an answer in under 20. At Conf42 Rustlang 2025, Karthik Mohan Muralidharan, a Software Engineer at Walmart Global Tech, presented two orchestration patterns for splitting work between edge devices and the cloud, and argued that Rust is the right language for the edge half.

The talk is well structured and pattern-first: a problem statement, two named patterns, the case for Rust, then the implementation challenges with candid answers.

## Cloud-only hits three walls

Karthik's problem statement is clean. Latency: a cloud round trip is too long for real-time control or medical monitoring. Bandwidth: streaming every sensor reading to the cloud around the clock congests networks and inflates bills. Availability: if critical operations depend on the internet connection, the connection is your single point of failure. The conclusion is not edge versus cloud, but both, with clear rules about who does what.

## Pattern one: edge inference, cloud remediation

Flip the traditional flow. Instead of shipping raw data up, run lightweight ML models on the edge devices and make the immediate decision locally. Only results, anomalies and exceptions go to the cloud, which runs heavier analysis and decides on larger remediation, such as dispatching a technician or triggering a workflow.

The benefits follow directly: critical decisions are fast, bandwidth drops, and the system keeps working through network outages. Karthik pointed it at manufacturing and predictive maintenance, and any setting where local responsiveness is the requirement.

## Pattern two: cloud insight, edge reconfiguration

The second pattern runs the other way and is about learning. The cloud aggregates data from the whole fleet, giving a view no single device has. Models find optimization opportunities only visible at that scale, turn them into policies tailored to devices or groups, and push them down so devices update their local behaviour on the fly. His examples range from adjusting a price in a retail store to retiming a traffic light. Centralized intelligence, distributed execution: a feedback loop rather than a pipeline.

## Why Rust at the edge

Karthik's Rust case is specific to devices: memory safety without a garbage collector (no surprise pauses on a constrained device), compiler-enforced freedom from data races for devices juggling many tasks, cross-compilation from small ARM sensors to x86 industrial PCs from one codebase, and zero-cost abstractions. He cited lower memory use than managed-language equivalents, better performance per watt on ARM, and sub-millisecond inference jitter, which is the number real-time systems care about most.

## The hard parts, answered

The implementation section is where the talk earns its keep:

- **Distributed state over flaky links**: a hybrid consistency model, strong for critical data like financial transactions, eventual for analytics, with CRDTs to merge conflicting versions.
- **Security on physically exposed devices**: zero trust (authenticate and authorize every request), capability-based permissions so a device can do only what it must, and ML-based threat detection.
- **Performance**: predictive prefetching caches, content-aware compression instead of generic gzip, and SIMD for hot paths.

His four getting-started rules are worth pinning up: start from the business KPI, design for degraded operation, measure everything from day one, and ship edge workloads in containers.

## Who should watch

Architects of IoT, retail or industrial systems deciding what runs where, and Rust developers moving into embedded or edge work. It is pattern-level rather than code-heavy, so it pairs well with a hands-on edge Rust talk.

## Related Conf42 talks

- [From Cloud to Edge computing with WebAssembly](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly) by Alex Casalboni: another way to ship code to the edge.
- [Go-Powered Self-Healing IoT](https://www.conf42.com/Golang_2025_Bhushan_Gopala_Reddy_iot_microservices_resilience) by Bhushan Gopala Reddy: fault recovery for distributed devices.
- [Rust in Edge Computing: Performance and Security](https://www.conf42.com/Rustlang_2024_Venukumar_Chirlawar_edge_computing_security) by Venukumar Chirlawar: the previous year's Rust edge talk.

[Watch Karthik Mohan Muralidharan's talk](https://www.conf42.com/Rustlang_2025_Karthik_Mohan_Muralidharan_edge_cloud_divide)

[Watch the talk on YouTube](https://youtu.be/18dTAtDmMgI).

## Watch the talk

[Bridging the Edge-Cloud Divide: Orchestration Patterns for Real-Time Enterprise Systems](https://www.conf42.com/Rustlang_2025_Karthik_Mohan_Muralidharan_edge_cloud_divide) at Conf42 Rustlang 2025.
