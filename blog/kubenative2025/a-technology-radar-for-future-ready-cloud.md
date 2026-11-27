# From monoliths to edge and quantum, a radar for future-ready cloud

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/a-technology-radar-for-future-ready-cloud

In short: Surya Prabha Busi of Ford Credit tours microservices, edge, serverless and quantum at Conf42 Kube Native 2025, with a plan for adopting them in stages.

Every architecture decision ages; the trick is knowing which ones will age badly first. At Conf42 Kube Native 2025, Surya Prabha Busi, Technical Lead at Ford Credit with 18 years in IT and 11 in the automotive industry, gave a guided tour from monoliths through microservices and edge computing to serverless and quantum, ending with a plan for adopting them in stages instead of all at once.

This is a broad overview talk. It suits people who need the whole map on one page, and it says plainly where each technology still hurts.

## Monoliths aren't wrong, just tightly wound

Busi gives the monolith a fair hearing. One codebase, one deployment and simple development make it a good fit for small apps and startup prototypes. The costs arrive later: you scale everything to scale anything, a framework upgrade touches the whole application, and every release carries the full deployment risk.

Microservices split that into autonomous units, each with its own business responsibility and data store, talking over HTTP or message queues. The adoption figures he cites are steep: from 45% in 2019 to 91% in 2024. He also cites a 76% cut in deployment time, up to 50% lower cost, 62% better resource utilisation and 83% fewer system-wide failures thanks to fault isolation.

## The bill for microservices comes in four parts

The section on challenges is the most useful. Technical debt: he says 67% of enterprises are held back by legacy code that is hard to split. Service decomposition: without real domain knowledge, the boundaries land in the wrong places. Operational complexity: 71% report harder monitoring, debugging and maintenance. Data: 64% struggle with consistency across services.

His foundations to pay that bill are the standard ones, and he lists them clearly: Kubernetes for orchestration, a service mesh for routing and observability, API gateways for client traffic and auth, centralised logging and metrics. On the design side: domain-driven design for boundaries, event-driven architecture for loose coupling, CQRS for heavy data, and circuit breakers so one failure doesn't cascade.

## Edge moves the compute to the data

Edge computing processes data near where it is produced (IoT devices, sensors, local servers) instead of shipping everything to a central cloud. His figures: 45% lower latency, 78% bandwidth savings and 56% faster emergency response in healthcare; in manufacturing, 33% efficiency gains, 87% better defect detection and 41% lower predictive maintenance costs. The constraints are real: limited CPU and storage (K3s and MicroK8s exist for exactly this), patchy connectivity and a bigger attack surface, which calls for zero trust, hardware-backed security and strong encryption.

## Serverless now, quantum later

Serverless gets the pay-per-use pitch, with organisations reporting 61% shorter development cycles and 45% less operational overhead. Quantum computing gets an honest one: promising for materials science, pharmaceuticals and machine learning, but early, expensive and not something to plan production on yet.

For distributed security he lists zero trust with least privilege, secret management (GCP Secret Manager as the example), service mesh mTLS, runtime anomaly detection and supply-chain checks on builds and dependencies.

## Adopt in stages, measure with DORA

The closing advice is the practical part. Assess your actual requirements, keep a technology radar, prove each technology on a less critical workload, then spread it through a platform engineering team that bakes in the lessons. Measure with DORA metrics, cost efficiency and your own KPIs, not enthusiasm.

## Who should watch

Architects and tech leads who must explain these trade-offs to stakeholders, and engineers moving from monoliths who want the full list of what microservices will cost them. If you already run edge Kubernetes in production, you'll know most of this.

## Related talks

- Lerna Ekmekcioglu tells the migration story in practice: [Journey from monolith to microservices on AWS](https://www.conf42.com/Cloud_Native_2022_Lerna_Ekmekcioglu_monolith_microservices_aws).
- Venukumar Chirlawar on performance and safety at the edge: [Rust in Edge Computing: Enhancing Performance and Security](https://www.conf42.com/Rustlang_2024_Venukumar_Chirlawar_edge_computing_security).
- Where quantum meets the edge: Anushree Nagvekar's [hybrid quantum-classical talk on edge AI](https://www.conf42.com/Quantum_Computing_2025_Anushree_Nagvekar_quantum_edge_ai).

[Watch Surya Prabha Busi's talk](https://www.conf42.com/Kube_Native_2025_Surya_Prabha_Busi_microservices_edge_future)

[Watch the talk on YouTube](https://youtu.be/vAhZSDP5BRg).

## Watch the talk

[Future-Ready Cloud: Microservices, Edge, and Emerging Tech at Scale](https://www.conf42.com/Kube_Native_2025_Surya_Prabha_Busi_microservices_edge_future) at Conf42 Kube Native 2025.
