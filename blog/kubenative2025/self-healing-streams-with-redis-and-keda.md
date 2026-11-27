# Self-healing streaming on Kubernetes with Redis Streams and KEDA

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/self-healing-streams-with-redis-and-keda

In short: Karthik Reddy Beereddy (LexisNexis Risk Solutions) at Conf42 Kube Native 2025 on replayable logs, circuit breakers and lag-driven autoscaling for streams.

CPU is the wrong signal for scaling a stream consumer: the number that matters is how far behind it is. Karthik Reddy Beereddy, Senior Site Reliability Engineer at LexisNexis Risk Solutions, made that case at Conf42 Kube Native 2025 as part of a catalogue of self-healing patterns for streaming systems built on Azure Kubernetes Service, Redis Streams and Azure Event Hub.

The talk is a pattern catalogue drawn from his platform modernisation work, moving nightly batch jobs to event-driven services. It is broad rather than deep, but the pieces fit together into one coherent design.

## Start with a log you can replay

Every streaming system juggles throughput, consistency and availability, and Karthik is upfront that you trade them off rather than max all three. His foundation is Redis Streams as a replayable, append-only event log. Messages carry unique IDs and timestamps, so after a failure the sequence can be rebuilt deterministically.

Two properties make that log a resilience tool rather than just a queue. It buffers temporary downstream failures without losing data, with back-pressure so a long outage does not exhaust memory. And consumer groups distribute load and fail over: a crashed consumer's replacement resumes from the last acknowledged position.

## Replay only works if handlers are idempotent

Replaying events is how the system recovers state, which means handlers will see duplicates. Karthik's rules: use partition keys and sequence numbers to keep ordering deterministic, combine event sourcing with snapshots and incremental replay to shorten recovery, and make every handler idempotent so duplicates have no side effects. That last one is the difference between a clean recovery and a replay that bills every customer twice.

Circuit breakers sit around the downstream calls with the usual three states: closed while things are healthy, open to fail fast once error thresholds trip, half-open to probe recovery and restore traffic gradually.

## Partition for isolation, scale on lag

On Event Hub, partitions are both a performance lever and a failure boundary: each acts as an independent commit log, so a stuck partition or consumer group does not stall the others. In one implementation his team adjusted partition counts based on throughput trends, such as billing events peaking in business hours, to stay clear of throttling without over-provisioning.

Scaling is where KEDA comes in. Instead of the Horizontal Pod Autoscaler watching CPU, KEDA scales consumers on Event Hub consumer lag: backlog grows, pods appear; backlog drains, they go away. He likes that it builds on the HPA, reads Prometheus metrics, and leaves scaling events visible next to the system metrics they reacted to.

## The boring Kubernetes parts do the healing

The self-healing loop is mostly stock Kubernetes, configured with care: liveness probes that restart unresponsive containers, readiness probes that pull unhealthy pods out of service discovery, restart policies with exponential backoff, and HPA policies on custom metrics. A service mesh such as Linkerd adds mTLS, retries and canary routing without application changes.

Observability closes the loop. Baseline message throughput, consumer lag, error rates and resource usage in Prometheus, alert on deviation, and use Grafana heat maps to spot hot partitions and uneven load. Delivery uses blue-green and canary rollouts with Argo Rollouts.

## Who should watch

SREs and platform engineers running consumers on Kubernetes, especially anyone whose stream autoscaling still keys off CPU. It is a good map of the patterns; for implementation detail on any one of them, follow the related talks.

## Related Conf42 talks

- [Self Healing Systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) by Nick Hodges (Rollbar), for the general principles.
- [Go and Redis, better together!](https://www.conf42.com/Golang_2023_Abhishek_Gupta_go_redis_better_together) by Abhishek Gupta (AWS), hands-on Redis from the client side.
- [NATS: The Cloud-Native Challenger to Kafka's Messaging Throne](https://www.conf42.com/Kube_Native_2024_Mohamed_Moussaoui_nats_cloudnative_kafka) by Mohamed Moussaoui (Amadeus), another take on the streaming backbone.

[Watch Karthik Reddy Beereddy's talk](https://www.conf42.com/Kube_Native_2025_Karthik_Reddy_Beereddy_streaming_redis_selfhealing)

[Watch the talk on YouTube](https://youtu.be/ZONIocLvQss).

## Watch the talk

[Self-Healing Patterns for Cloud-Native Streaming: Resilient Architectures with Kubernetes, Redis Streams & Azure Event Hub](https://www.conf42.com/Kube_Native_2025_Karthik_Reddy_Beereddy_streaming_redis_selfhealing) at Conf42 Kube Native 2025.
