# Kafka on Kubernetes lives or dies on storage and consumer lag

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/kafka-on-kubernetes-statefulsets-storage-lag

In short: Shalini Katyayani Koney (Walmart) at Conf42 Kube Native 2025 on Kafka on Kubernetes at 100,000+ msg/s with StatefulSets, fast disks and lag-based scaling.

Running Kafka on Kubernetes is easy to start and easy to get wrong, and the place it usually goes wrong is the disk. At Conf42 Kube Native 2025, Shalini Katyayani Koney, Senior Engineering Manager at Walmart, laid out the patterns behind a Kafka platform that sustains over a hundred thousand messages per second in production, and argued that storage, resource sizing and lag-aware scaling matter more than any single clever trick.

The framing is practical. Kubernetes gives you self-healing, scheduling and autoscaling for free, but Kafka brokers are stateful, and every one of those conveniences has to be bent around that fact.

## Brokers are pets, so give them StatefulSets

The foundation is three pieces. Brokers run as StatefulSets, which gives ordered rollout, stable network identities and a persistent volume that follows each broker. Volumes come from SSD-backed storage classes with high IOPS, because Kafka's log segments want fast sequential writes. And a service mesh handles encrypted pod-to-pod traffic and metrics without touching application code.

On sizing she gave concrete starting points: two to four CPU cores per broker, and 8 to 16 GB of heap, tuned to partition count and retention. Critical Kafka pods run in the Guaranteed QoS class so the scheduler does not evict them when the cluster gets crowded. In a shared cluster, a noisy neighbour is a polite name for an outage.

## Storage is where most deployments fail

This was the most opinionated part of the talk. Size persistent volume claims from your retention policy and replication factor, not from a guess, because undersized volumes lead to disk pressure and unstable brokers. Then tune the file system: Koney reported that XFS with the right mount options can improve write performance by 30 to 40% over default configurations.

Networking gets the same treatment. Isolated network policies for the Kafka namespace, load balancing with session affinity (clients like sticky connections to the brokers that lead their partitions), and TCP buffer tuning or even dedicated interfaces when throughput demands it.

## Scale on lag, and respect partition leadership

CPU and memory do not tell you when Kafka needs help. Her horizontal pod autoscaling keys off Kafka-specific signals such as consumer lag and partition throughput. The catch is that you cannot just kill a broker on scale-down: leadership has to move and replicas have to be reassigned first, and partitions must stay balanced or hotspots eat the capacity you just added.

For multiple clusters she uses Helm charts for consistent installs across regions, MirrorMaker for cross-region replication, and a GitOps workflow where every cluster config lives in Git with automated rollbacks when a change destabilises a cluster.

## Measure lag before your users notice it

The monitoring stack is Prometheus scraping JMX metrics, Grafana dashboards for throughput and latency, and alerts on consumer lag spikes, under-replicated partitions and disk thresholds. Disaster recovery uses Kubernetes operators for backup and failover, cross-region copies of topic configs, consumer offsets and ACLs, and chaos experiments that break components on purpose to prove recovery works.

The headline production numbers she shared: a sustained hundred thousand messages per second, 99.9% availability with zero-downtime rolling upgrades, and P99 latency under five milliseconds even under heavy load. Note that the abstract talks about million+ msg/sec, while the talk itself sticks to the hundred-thousand figure.

## Who should watch

Platform engineers who have been asked to move Kafka off VMs and onto a shared cluster, and SREs who inherited a Strimzi or Helm-based setup that pages on disk pressure. It is an architecture talk with no live demo, so treat it as a checklist to compare against your own cluster rather than a tutorial.

## Related Conf42 talks

- [No JVM, no Kafka: Shape the future of streaming data pipelines](https://www.conf42.com/Kube_Native_2024_Bobur_Umurzokov_jvm_kafka_streaming_data) by Bobur Umurzokov (GlassFlow) makes the case for going the other way entirely.
- [Simplifying Kafka Governance for Developers](https://www.conf42.com/DevSecOps_2023_Muralidhar_Basani_simplifying_kafka_governance) by Muralidhar Basani (Aiven) covers the topics-and-ACLs sprawl that follows scale.
- [Scaling Opentelemetry Collectors using Kafka](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pranay_Prateek_scaling_opentelemetry_kafka) by Pranay Prateek (SigNoz) puts Kafka to work as a buffer for telemetry.

[Watch Shalini Katyayani Koney's talk](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable)

[Watch the talk on YouTube](https://youtu.be/2JiR_gJ5fHg).

## Watch the talk

[Scaling Kafka on Kubernetes: Cloud-Native Streaming for 100,000+ Messages Per Second](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable) at Conf42 Kube Native 2025.
