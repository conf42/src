# Batch SIEM gives attackers a head start; shard the compute instead

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/sre2026/streaming-siem-beats-the-batch-window

In short: Abhishek Suman of Microsoft at Conf42 SRE 2026 on compute-sharded stream processing with consistent hashing for petabyte-scale security detection.

"A bad actor does not wait for your batch job." That is the premise of Abhishek Suman's talk at Conf42 Site Reliability Engineering 2026. Suman, a Senior Software Engineer at Microsoft who works on real-time data pipelines and security analytics infrastructure, argues that detection latency in a batch-based SIEM is architectural, and the fix is a compute-sharded stream processing design where every event is evaluated as it arrives.

## The latency is baked in, not tunable

Lateral movement, credential harvesting and persistence can be done in minutes, often inside a single batch window. By the time a scheduled cycle runs and an alert fires, the attacker may already be settled in. Suman's point is that you cannot tune this away. Scheduled batch cycles put structural latency into every layer, and at petabyte volume the problems compound: ingestion queues back up, correlation windows grow, and alert fidelity drops under load. These pipelines were designed for gigabyte-scale data, and it shows.

## Shard the compute, not only the data

The core design distributes both data and computation across independent processing nodes using consistent hashing. Streams and compute workloads get mapped onto nodes in a virtual ring, which buys a few properties SREs care about:

- Deterministic shard assignment, so you can predict where a key lives.
- Elasticity: adding or removing a node remaps only a small subset of keys, so scaling out does not mean a full reshuffle.
- Fault isolation: a failed node affects only its own key range.
- Stateful correlation per shard, without a global correlation step that becomes the next bottleneck.

Each shard runs on its own, which is how the design avoids a central choke point and scales horizontally as volume grows. If you have ever watched one overloaded correlator hold a whole SOC hostage, this is the part to rewind.

## Schema-agnostic ingestion keeps coverage moving

Security telemetry is a zoo: firewall logs, EDR events, cloud audit trails, network flows, identity signals. Requiring predefined schemas for each one turns every new source into a project. Suman's design infers structure at runtime and applies only lightweight normalization at the ingestion boundary, so new sources can be onboarded without pipeline halts or schema migration cycles. Faster onboarding is a reliability concern here, because a source you cannot ingest is a blind spot.

## Rules for the known, ML for the novel

Detection is hybrid. Rule-based detection covers known signatures, compliance checks and thresholds, with low latency and high precision. An ML anomaly layer adds behavioural baselines, statistical deviation and unsupervised clustering to catch novel behaviour and zero-day techniques that have no signature yet.

Multi-region deployment is treated as both a resilience and a compliance requirement: region failure isolation so one outage does not blind global detection, localized processing for data residency, distributed consensus to keep detection rules and state consistent across regions, and automatic shard reassignment and failover for node or zone failures.

## What it delivered, and the SRE checklist

The results are reported qualitatively: detection latency down by an order of magnitude against scheduled batch cycles, stable throughput as workload grew, better compute utilization per unit of telemetry than centralized designs, and measurably faster time to respond across the case-study deployments. The talk does not share exact figures.

His four lessons are the reusable part. Design for horizontal scale from day one, because sharding is hard to retrofit. Decouple ingestion from processing. Alert on SLO metrics such as processing lag, shard rebalance duration and pipeline depth, and define those SLOs before rollout. Test failure modes, not just the happy path: node loss, region partitions and back-pressure cascades. Or, as he put it, "resilience is not emergent, it is engineered."

## Who should watch

Engineers building or operating security analytics pipelines, and anyone running stream processing at serious volume, will get a compact architecture overview. It is a design talk with no code or product demo, so treat it as a blueprint to compare against your own pipeline.

## Related Conf42 talks

- [Streaming Aggregation on Cloud Scale Telemetry](https://www.conf42.com/Chaos_Engineering_2023_Shay_Lin_streaming_aggregation_cloud_scale_telemetry) by Shay Lin.
- [Defender XDR in the Real World: From Alert Fatigue to Measurable Risk Reduction](https://www.conf42.com/DevOps_2026_Nikolay_Milyaev_xdr_security_analytics) by Nikolay Milyaev.
- [Runtime Kubernetes Security: Hands-On Threat Detection with Falcosidekick](https://www.conf42.com/Kube_Native_2024_Aleksandra_Drobnjak_kubernetes_security_falcosidekick_threat_detection) by Aleksandra Drobnjak.

[Watch Abhishek Suman's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhishek_Suman_compute_sharded_stream) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/2JW7cLLQ4QU).

## Watch the talk

[Compute-Sharded Stream Processing for Petabyte-Scale Real-Time Cybersecurity Analytics](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhishek_Suman_compute_sharded_stream) at Conf42 Site Reliability Engineering (SRE) 2026.
