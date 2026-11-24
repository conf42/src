# Four patterns for putting quantum inside a multi-tenant SaaS

Conf42 Blog, 2025-05-29, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-saas-multi-tenancy-patterns

In short: Srikar Kompella of Twilio sketches quantum, edge and multi-tenancy patterns for SaaS at Conf42 Quantum Computing 2025, from federated learning onward.

Multi-tenancy started as a way to save money on shared servers; Srikar Kompella thinks its next stage is quantum-aware resource allocation across tenants. At Conf42 Quantum Computing 2025, the Twilio Senior Software Engineer laid out an architecture vision for SaaS built on three pillars (quantum compute, edge processing and advanced multi-tenancy) and four integration patterns that combine them.

It's a forward-looking architecture talk rather than a build log. The value is in the patterns, which are concrete enough to reason about now.

## Three pillars, one platform

Kompella's pillars split the work by what each is good at. Quantum computing, reached on demand through the cloud, takes the optimisation, simulation and pattern-finding problems. Edge processing brings those results close to users so decisions happen in real time and less raw data travels. Multi-tenancy is the delivery framework: fair, cost-effective sharing of scarce quantum processors with strict isolation of each tenant's data in a mixed classical, quantum and edge environment.

The edge piece has one idea worth stealing: train a complex model on the quantum side, then deploy it to local edge runtimes. A factory robot then adjusts on the spot instead of waiting on a central server, and a traffic grid tunes signal timing at each intersection.

## Multi-tenancy grows up in three steps

The talk frames multi-tenancy as an evolution: basic resource sharing with minimal isolation and a focus on cost, then advanced segmentation where tenants share services but keep data and workflows separate, then quantum-aware architectures that allocate resources dynamically across tenant boundaries while still isolating them.

## The four integration patterns

This is the section to watch closely:

1. **Quantum federated learning.** Each tenant (his example: a hospital and a research institute) trains a quantum ML model on its own data inside its own perimeter. Only model updates leave, protected by quantum-resistant cryptography. The platform aggregates them into a better global model and sends it back. Raw data never moves.
2. **Customised quantum edge deployments.** Tenant-specific quantum algorithms go to edge locations based on each tenant's needs, with workloads routed between edge nodes and central quantum machines as demand shifts.
3. **QML-driven resource orchestration.** A quantum ML model forecasts each tenant's resource demand from live metrics, and the platform allocates capacity before the tenant needs it. Think autoscaling that reads ahead.
4. **Secure tenant collaboration.** Quantum-resistant data exchange plus privacy-preserving joint processing, so competitors can pool insights without sharing raw data. His example is rival retailers finding supply-chain inefficiencies that hurt them all, leading to industry consortiums hosted on the platform.

Pattern one is the most grounded: federated learning already exists classically, and the quantum part slots into the model and the crypto rather than the workflow.

## From selling software to selling answers

Kompella's business point is that quantum lets a SaaS company sell results such as optimisation or materials discovery as a service, not just tools. His roadmap is sober: assess the current architecture and find computationally heavy workloads, pick one pattern for a single pilot and measure it, then scale and invest in in-house expertise. He calls it an evolution, not an overnight revolution, which is the right tone.

## Who should watch

SaaS architects and platform engineers who own tenancy, isolation and capacity planning, and who want a vocabulary for where quantum might enter their stack. Skip it if you want benchmarks or code; it's patterns and diagrams.

## Related Conf42 talks

- [Optimizing multi-tenant SaaS: scalable architectures for performance, security and cost](https://www.conf42.com/Cloud_Native_2025_Shinu_Pushpan_saas_multitenancy_security) by Shinu Pushpan, the classical baseline these patterns extend.
- [Quantum-resistant Kubernetes for the post-quantum era](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) by Derek Asir Muthurajan Caleb, on the crypto the patterns assume.
- [Product management with multi-tenancy architecture](https://www.conf42.com/Cloud_Native_2025_Waqas_Khan_multitenancy_optimization_strategy) by Waqas Khan, for the product side of tenancy decisions.

[Watch Srikar Kompella's talk](https://www.conf42.com/Quantum_Computing_2025_Srikar_Kompella_quantum_saas_architecture)

[Watch the talk on YouTube](https://youtu.be/ilAoY7neTJA).

## Watch the talk

[Quantum-Enhanced SaaS Architecture: Convergence of Quantum Computing, Edge Processing, and Multi-Tenancy](https://www.conf42.com/Quantum_Computing_2025_Srikar_Kompella_quantum_saas_architecture) at Conf42 Quantum Computing 2025.
