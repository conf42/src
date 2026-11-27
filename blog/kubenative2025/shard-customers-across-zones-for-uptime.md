# Shard customers across availability zones, and pay for it

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/shard-customers-across-zones-for-uptime

In short: Rahul Singh Thakur (Salesforce) at Conf42 Kube Native 2025 on zone-sharded services, a metadata router, consistent hashing and the cost of 99.99% uptime.

Losing a whole availability zone should be a bad afternoon, not an outage. Rahul Singh Thakur, Lead Member of Technical Staff at Salesforce, walked through how to get there at Conf42 Kube Native 2025: shard customers across zones, route every request through a metadata service that knows who lives where, and accept the extra cost and debugging pain that buys.

Rahul came to this from infrastructure services his team needed to keep up even through a complete zone failure. The talk is a design guide rather than a war story, and it is refreshingly clear about trade-offs.

## A zone is a blast radius

Cloud availability zones are self-contained sets of infrastructure: something going wrong in one should not take down another. Spread a service across several and a single-zone outage leaves the service up. Rahul's principles follow from that: treat each zone independently, keep data from wandering between zones, design for partial failure, and monitor each zone on its own because "the service" is now several services.

Stateful services are where it gets hard. When they scale up or down, the state has to stay with the right customer.

## Something has to know which zone owns which customer

The central component is a metadata service. It assigns each new customer to a shard, remembers the mapping, tracks the health of each zone, and applies routing policy, so it acts as both intelligent router and load balancer. Sharding by customer also shrinks the blast radius: a bad zone affects its customers, not everyone.

Because the number of zones is not fixed, Rahul uses consistent hashing so adding or removing a zone moves only the data that has to move.

On Kubernetes, the supporting pieces are pod distribution across topology with affinity rules, persistent volume management for stateful pods, service registration that carries zone and capacity information, and zone-aware scaling so the survivors can absorb a failed zone's traffic.

## Pick availability, then live with eventual consistency

Rahul is direct about CAP. If every write must replicate to all zones before it succeeds, one unavailable zone blocks writes, and you have traded away the availability you came for. Since the goal is uptime, his recommendation is eventual consistency: let other zones catch up. Keep a customer's data partition inside its zone, and resolve conflicts with last-write-wins or something smarter if the domain needs it.

## High availability means paying for everything twice

The cost section is the most useful part. Going multi-zone duplicates infrastructure, so Rahul suggests rightsizing from load tests, reserved instances, choosing cross-zone communication options with cost in mind, and zone-aware autoscaling that grows only the zone that needs it. Debugging also gets harder, which is why distributed tracing and good logs are on the must-have list.

Operationally: canary deploys to one zone first, and changes that never assume a particular zone.

## Is it worth it?

His conclusion is measured: sharding across zones adds a metadata service to run, extra cost and harder debugging. It pays off for mission-critical and data services, such as a database where a down zone must not mean unreadable data. For a lot of other services, plain replication may be enough.

## Who should watch

Backend and platform engineers designing tenant placement or planning for zone failure, and anyone about to promise four nines without having priced them.

## Related Conf42 talks

- [Fault isolation using shuffle sharding](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrew_Robinson_fault_isolation_shuffle_sharding) by Andrew Robinson (AWS), a sharper blast-radius trick.
- [Optimize end user connectivity for multi-region architectures](https://www.conf42.com/Site_Reliability_Engineering_2022_Christian_Elsen_Lerna_Ekmekcioglu_reliable_multiregion_arch) by Christian Elsen (AWS), the routing problem one level up.
- [Automatically shard and scale-out your traditional databases on Kubernetes](https://www.conf42.com/Cloud_Native_2023_Trista_Pan_automatically_shard_scaleout_databases_kubernetes) by Trista Pan (SphereEx), sharding the data layer itself.

[Watch Rahul Singh Thakur's talk](https://www.conf42.com/Kube_Native_2025_Rahul_Singh_Thakur_sharding_uptime_architecture)

[Watch the talk on YouTube](https://youtu.be/j5un96J72ME).

## Watch the talk

[Kube-Native Sharding: Multi-Zone Service Architecture for 99.99% Uptime](https://www.conf42.com/Kube_Native_2025_Rahul_Singh_Thakur_sharding_uptime_architecture) at Conf42 Kube Native 2025.
