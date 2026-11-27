# AI workloads break networks that were built for web apps

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-workloads-break-networks-built-for-web

In short: Bhaskararao Vakamullu of Hewlett Packard Enterprise at Conf42 Platform Engineering 2025 on spine-leaf, ECMP, RDMA and network observability for AI scale.

A web app talks to a handful of backends and shrugs at a few hundred milliseconds of latency. A distributed training job talks to hundreds of nodes at once and stalls if the fabric hiccups. At Conf42 Platform Engineering 2025, Bhaskararao Vakamullu, Senior Network Software Engineer at Hewlett Packard Enterprise, argued that this gap makes the network a core platform capability, and walked through the design principles that keep it from becoming the weakest link.

It is a compact talk, close to a lecture in data-centre networking for platform people, and it moves fast.

## East-west traffic changed the shape of the network

Vakamullu traces the evolution from the classic three-tier core, distribution and access design to spine-leaf, which is optimised for east-west traffic between servers. AI made that traffic dominant: before a response ever goes back to the user, a lot of computation happens inside the data centre.

He contrasts the two worlds. Web applications typically need two to four backend connections and predictable traffic. AI workloads span 128 to 256 or more nodes, need terabit-scale bandwidth, want latency under 10 milliseconds, and are bursty and unpredictable. Software-defined networking and purpose-built ASICs with low-latency fabrics are the response.

## Incast is the failure you should know by name

His cascading-failure example is a financial AI platform hitting timeouts under peak load. The culprit is TCP incast: many servers answer one aggregator node at the same moment, buffers overflow, packets drop, retransmissions pile up and the service degrades. The fix he describes is RDMA over Converged Ethernet (RoCE) with flow control, so the fabric prevents the collapse instead of reacting to it.

The other bottlenecks on his list are worth checking against your own network: bufferbloat adding latency, switches that cannot process enough packets per second, oversubscription ratios that break AI workloads, and ML training saturating links within seconds.

## Design for the link that will fail

The fault-tolerance principles are classic, and stated crisply:

- **Path diversity** with ECMP (equal-cost multipath), so traffic spreads across several routes.
- **Fast failure detection** with BFD (bidirectional forwarding detection), so a dead link is noticed in under a second and traffic moves.
- **Segment routing** for traffic engineering.
- **Isolated failure domains** and graceful degradation, so a fault hits a slice of traffic rather than all of it.

For spine-leaf specifically: keep oversubscription below 3:1, size buffers for microbursts, and consider RDMA where latency really matters.

## Find problems before users do

On observability he recommends regular-interval telemetry, watching latency distributions, utilisation and retransmissions, ML-based anomaly detection, and digital twins for what-if analysis before you change production.

His case for caring is cost. He cited figures on how small amounts of latency add minutes to training runs, waste GPU cycles and multiply infrastructure cost, and an e-commerce platform that moved to a spine-leaf design with a 400 Gbps backbone and cut incidents by 98.5%. The talk gives the numbers without the methodology, so take them as illustrations of the direction. The underlying point holds regardless: idle GPUs waiting on a congested network are the most expensive way to do nothing.

## Who should watch

Platform engineers who own Kubernetes or ML infrastructure but treat the network as somebody else's box will get a fast vocabulary for that conversation: incast, oversubscription, ECMP, BFD, RoCE. Network engineers will know all of it already.

## Related Conf42 talks

- Bhaskararao Vakamullu's own follow-up, [observability in AI-era networking infrastructure](https://www.conf42.com/Observability_2025_Bhaskararao_Vakamullu_networking_era_highways), at Observability 2025.
- Ravi Theja Kambhampati on [routing and switching foundations for resilient networks](https://www.conf42.com/Kube_Native_2024_Ravi_Theja_Kambhampati_routing_switching_network_infrastructures) at Kube Native 2024.
- Maksim Kupriianov on [network incidents](https://www.conf42.com/Incident_Management_2024_Maksim_Kupriianov_solving_network_incidents) at Incident Management 2024.

[Watch Bhaskararao Vakamullu's talk](https://www.conf42.com/Platform_Engineering_2025_Bhaskararao_Vakamullu_legacy_network_modern)

[Watch the talk on YouTube](https://youtu.be/bCylzkDFljI).

## Watch the talk

[Building Resilient Network Infrastructure for Modern Platform Engineering: From Legacy Systems to AI-Scale Architecture](https://www.conf42.com/Platform_Engineering_2025_Bhaskararao_Vakamullu_legacy_network_modern) at Conf42 Platform Engineering 2025.
