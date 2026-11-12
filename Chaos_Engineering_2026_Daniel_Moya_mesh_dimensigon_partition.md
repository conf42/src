# Orchestrating Under Fire: Chaos Experiments and Mesh Partition Survival with Dimensigon

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Daniel Moya](https://www.conf42.com/speaker_Daniel_Moya) (Founder @ HeliosDB). Page: https://www.conf42.com/Chaos_Engineering_2026_Daniel_Moya_mesh_dimensigon_partition

## Abstract

Chaos engineering traditionally tests application resilience against infrastructure failures. But what happens when the chaos hits the management and orchestration system itself? If the orchestrator cannot survive network partitioning, automated recovery mechanisms inevitably collapse.  This session shares chaos engineering experiments executed on Dimensigon mesh networks. We will inject simulated link latency, random packet loss, and split-brain network partitions to evaluate message routing resilience, `forward_or_dispatch` recovery, and distributed vault secret access. Attendees will walk away with concrete architectures for building fault-tolerant automation platforms capable of executing amidst severe network degradation.
