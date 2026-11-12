# Multi-zone is the sweet spot of high availability, and physics explains why

Conf42 Blog, 2021-10-01. https://www.conf42.com/blog/sre2021/five-levels-of-high-availability-trade-offs

In short: Rafal Leszko (Hazelcast) at Conf42 Site Reliability Engineering 2021 on five high availability levels and what each costs in latency and consistency

Running on two machines technically makes you highly available, and Rafal Leszko, Cloud-Native Tech Lead at [Hazelcast](https://hazelcast.com), spends his Conf42 Site Reliability Engineering 2021 talk on everything that sentence leaves out. He climbs five levels, multi-instance, multi-zone, multi-region, multi-cloud and hybrid cloud, and for each shows what you gain, what you lose, and a latency measurement from Hazelcast deployed that way. His verdict: if you don't know which level you need, it is multi-zone.

## Why is the data the only hard part?

Stateless services, whatever you call them, are easy: replicate them anywhere and they behave the same on a laptop or in a million replicas. The trouble is the stateful things behind them, data stores, queues, other services. Rafal Leszko said at Conf42 Site Reliability Engineering 2021: "So if there is no data, there is no problem in terms of high availability." So every level is really about where the data lives and how it is replicated.

Level zero, a single instance, is not HA at all, but it has the lowest latency and perfect consistency. His baseline measurement, an application with embedded Hazelcast on one machine, was 80 milliseconds per 10,000 entries for reads and writes. An idempotent batch job you can always rerun is a fair use case.

## Multi-instance: active-passive or clustering?

Two machines behind a load balancer, with the data store on at least two machines. He sketches the history: SQL databases used active-passive (master-slave) replication with failover; NoSQL systems moved to clustering, where every node holds primary partitions plus backups of others. In Hazelcast, a partition's backup always lives on a different member than the partition itself.

Then the real question: synchronous or asynchronous backups? With synchronous backups across two machines his test stayed under one millisecond per entry, so most NoSQL stores default to sync. MySQL, by contrast, replicates asynchronously by default and favours latency.

## What does multi-zone change?

Almost nothing in latency: four Hazelcast instances across two availability zones were not even twice as slow as multi-instance, still under a millisecond per entry. But there is a trap. If a partition and its backup sit on two members that happen to share a zone, losing that zone loses the data. Hazelcast's answer is zone-aware partition grouping, with discovery plugins for AWS, Azure, GCP and Kubernetes that ask the cloud API which zone a member is in. His advice applies to any data store: check that it is zone aware, don't assume it.

## Why can't regions be synchronous?

Distance. He uses Finland and Oregon, about 10,000 kilometres apart: light in a vacuum needs 60 milliseconds for the round trip, fibre at least three times that, before any router gets involved. So multi-region needs asynchronous geo-replication (Hazelcast calls it WAN replication), and with it come possible data loss and eventual consistency. Active-active adds conflict resolution, such as last write wins, that your business logic has to understand.

He tried the forbidden version anyway, one Hazelcast cluster with synchronous backups spanning two regions, and the latency landed in an unacceptable range. Rafal Leszko said at Conf42 Site Reliability Engineering 2021: "That is why you will never use synchronous replication across multiple geographical regions." It is also why nobody runs one Kubernetes cluster across regions: etcd is a consistent store and would crawl. Federation is the workaround.

## Is multi-cloud about availability at all?

Mostly not. A whole cloud provider going down is close to unheard of. You lose cloud-native tooling and VPC peering and pay to run the same system twice. The real reasons are avoiding vendor lock-in, leverage in cost negotiations (telling AWS, in his words, "by the way, I'm also deployed on Azure and GCP, so can you lower the bill?"), risk mitigation, data regulations and latency for customers who are themselves spread across clouds. That last one is why Hazelcast Cloud runs on several providers.

Hybrid cloud is driven by regulation (bank data that must stay in one country or building), mid-migration estates, and cost at very large scale. At this level you need an abstraction layer, usually Kubernetes or OpenShift on every environment, and in his words it costs a fortune.

## Which level should you pick?

His complexity chart has big steps from single instance to multi-instance (now you are distributed), from multi-zone to multi-region (async replication) and from multi-cloud to hybrid (your own hardware). Multi-zone is the small step with the best payoff: very available while still allowing a synchronous, consistent data store. Go multi-region when you need low latency worldwide, and multi-cloud or hybrid only with a compliance or business reason.

## Who should watch

Architects deciding how far to take HA, and anyone about to tick the multi-region box in a design doc. Clear diagrams, honest trade-offs, Hazelcast as the worked example.

## Related Conf42 talks

- Rafal Leszko on [architectural caching patterns for Kubernetes](https://www.conf42.com/Cloud_Native_2021_Rafal_Leszko_architectural_caching_patterns_kubernetes) at Conf42 Cloud Native 2021.
- Ana Van Straaten on [going multi-region](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region) at Conf42 Cloud Native 2022.
- Andrew Robinson on [fault isolation with shuffle sharding](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrew_Robinson_fault_isolation_shuffle_sharding), also at SRE 2021.

[Watch Rafal Leszko's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Rafal_Leszko_high_availability_multiinstance_hybrid_cloud)

## From Hazelcast

Hazelcast makes an open source in-memory data store and stream processing platform, also offered as a managed service, Hazelcast Cloud.

- [Hazelcast website](https://hazelcast.com)

[Watch the talk on YouTube](https://youtu.be/N_JC8aX3h9g).

## Watch the talk

[5 Levels of High Availability: from Multi-instance to Hybrid Cloud](https://www.conf42.com/Site_Reliability_Engineering_2021_Rafal_Leszko_high_availability_multiinstance_hybrid_cloud) at Conf42 Site Reliability Engineering 2021.
