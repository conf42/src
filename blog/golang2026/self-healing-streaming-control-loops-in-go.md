# Put the AI in the control plane, not the business logic

Conf42 Blog, 2026-05-10, updated 2026-11-09. https://www.conf42.com/blog/golang2026/self-healing-streaming-control-loops-in-go

In short: Yogesh Pugazhendhi Duraisamy Rajamani of Ford at Conf42 Golang 2026 on self-healing streaming pipelines built from Go control loops and an RL control plane.

By the time a human answers the page, the consumer lag has already piled up. At Conf42 Golang 2026, Yogesh Pugazhendhi Duraisamy Rajamani, Senior Data Engineer at Ford Motor Company, presented an architecture for streaming pipelines that detect, diagnose and recover from failures on their own, with Go supervisor loops doing the fast recovery and an AI control plane making the operational calls.

His starting point is that streaming pipelines are static while their environment is not. Nodes die mid-stream, schema changes silently break downstream consumers, bursts overload systems sized for average load, and congestion spreads backpressure across the stack. Reactive alerting plus a manual ops team means the damage is done before anyone acts: lag grows, data drops, SLAs slip.

## Three layers, one rule about where intelligence lives

The framework stacks an ingestion layer (Kafka, Pulsar, IoT telemetry, edge events), a processing layer (Go stream processors, Flink jobs, enrichment services), and an AI control plane on top that watches throughput, latency, queue depth, node health, schema integrity and error rates. The control plane acts like an autonomous operator: scale, reroute, restart, throttle.

The principle Yogesh keeps coming back to is separation of concerns. Business logic stays in the processing layer; operational intelligence lives in the control plane. It is the cleanest idea in the talk and the one most worth stealing even if you never train a model.

On the Go side, he does not expose raw broker APIs to developers. Channel-oriented abstractions wrap Kafka and friends, so consumers pull, workers process, supervisors monitor, and backpressure propagates naturally through the channels.

## Recovery belongs in a Go loop, not a round trip to Kubernetes

The self-healing cycle is detection, diagnosis, remediation. Detection uses deliberately lightweight models inline with the stream (statistical models, small anomaly classifiers, streaming feature extraction) rather than giant transformers in the hot path. Schema drift gets special attention because it fails silently: a producer changes a payload and consumers start breaking unpredictably.

For remediation, Yogesh argues for native Go supervisor loops over relying entirely on an external orchestrator. Kubernetes reconciliation, container scheduling and API propagation can make the recovery path take seconds; an in-process supervisor can react in microseconds to milliseconds. Actions include restarting workers, rerouting partitions, circuit breaking unhealthy dependencies, and replaying offsets safely.

Scaling is predictive. A reinforcement learning controller learns from bursts, regional spikes, usage cycles and deployment behaviour, and provisions capacity before saturation. Ingestion, processing and sink tiers get separate policies, with cool-down and back-off constraints so the autoscaler does not oscillate itself into a second incident.

## Exactly-once is a design choice you make early

The consistency section is refreshingly concrete. Failures can land during writes, commits, retries or checkpoints, so he combines idempotent producers, transactional consumers that commit offsets with downstream writes, and custom Go checkpoint hooks that capture state before recovery actions. The rule underneath it all: never acknowledge work until the durable downstream write has succeeded.

## Patterns you can use without the RL part

The most practical slide lists four patterns for Go engineers:

- Standardise pipeline stages behind small interfaces so the control plane can swap implementations.
- Wrap every downstream dependency in a circuit breaker and export its state as Prometheus metrics.
- Put heartbeats inside worker goroutines and let supervisor goroutines trigger recovery when they stop.
- Never over-commit offsets; commit only after the sink has persisted, so replay is deterministic.

Observability ties it together. Every goroutine pool exposes backlog, health and throughput metrics, trace context rides in Kafka headers, and the control plane logs each decision with the evidence that triggered it, which gives you auditability and training data in one go.

## Who should watch

Data and platform engineers running Kafka, Pulsar or Flink with Go services in between. The talk is architectural and does not show code or benchmark numbers, so treat the RL control plane as a direction and the four patterns as the immediately useful part.

## Related Conf42 talks

- [Karthik Reddy Beereddy on self-healing streaming with Redis](https://www.conf42.com/Kube_Native_2025_Karthik_Reddy_Beereddy_streaming_redis_selfhealing) at Conf42 Kube Native 2025
- [Shalini Katyayani Koney on scalable Kafka streaming](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable) at Conf42 Kube Native 2025
- [Ankit Virmani on streaming data pipelines](https://www.conf42.com/Cloud_Native_2024_Ankit_Virmani_streaming_data_pipelines) at Conf42 Cloud Native 2024

[Watch Yogesh Pugazhendhi Duraisamy Rajamani's talk](https://www.conf42.com/Golang_2026_Yogesh_Pugazhendhi_Duraisamy_Rajamani_building_self_healing)

[Watch the talk on YouTube](https://youtu.be/fFgQvozMapQ).

## Watch the talk

[Building Self-Healing Real-Time Streaming Pipelines with Go and AI](https://www.conf42.com/Golang_2026_Yogesh_Pugazhendhi_Duraisamy_Rajamani_building_self_healing) at Conf42 Golang 2026.
