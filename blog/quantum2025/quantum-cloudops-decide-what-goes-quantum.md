# Quantum CloudOps means deciding which parts of an app go quantum

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-cloudops-decide-what-goes-quantum

In short: Srinivas Sriram Mantrala at Conf42 Quantum Computing 2025 on what DevOps and CloudOps teams must change when quantum joins the cloud.

The most expensive mistake in a hybrid quantum system will be putting the wrong part of the application on the quantum side. Srinivas Sriram Mantrala made that his closing point at Conf42 Quantum Computing 2025, in a talk on "Quantum CloudOps": what DevOps and CloudOps teams need to change as quantum processing arrives through cloud providers, which he expects within about five years.

It's a conceptual talk, delivered conversationally, with no demo. Think of it as an operations team's checklist for a technology that isn't on their pager yet.

## Thinking ten moves ahead

Mantrala explains superposition with chess. A strong player can hold maybe ten candidate moves in their head; then for each one, ten replies, and the tree explodes. His pitch for quantum is the ability to process that whole tree of combinations at once and surface the risky branch early. He applies the idea to security, where you want to anticipate the next attack and the one after it, and to operations, finance and medicine, anywhere a wider search beats a sequential one.

## The hybrid infrastructure has three parts

His architecture keeps today's cloud in charge:

- **Quantum processing units**, built on qubits, superposition and entanglement, for the complex algorithms.
- **Classical infrastructure**, the existing cloud that already handles conventional tasks and orchestration.
- **An integration layer** with translators, workload schedulers and real-time processing that distributes work between the two for the best performance.

The integration layer is where operations teams will spend their time, because load balancing now has two very different kinds of backend.

## What DevOps has to learn

The most useful section lists what changes for the people running the platform:

- **CI/CD** pipelines need quantum deployment and testing stages.
- **Observability** (logs, metrics and the analytics on top) has to cover quantum workloads too.
- **Operating models** need updating, and people need training to run quantum-backed applications.
- **Automation** has to extend to quantum resource allocation.
- **APIs** for quantum processing won't look like today's request-response endpoints, and programming models for concurrency may shift with them.

None of this is exotic; it's the same muscle teams built moving from on-prem to cloud. That is the reassuring subtext.

## Where it pays and how to start

Mantrala's list of beneficiaries: security (quantum-resistant encryption to protect sensitive data against future attacks), AI algorithms redesigned for quantum parallelism, pharmaceuticals (running clinical study computations concurrently instead of step by step) and finance (market prediction, portfolio and risk assessment).

Adoption follows the usual path: partner with a cloud provider that offers quantum infrastructure, build proofs of concept, then build the hybrid integration with APIs between quantum and classical services, find the limits, automate workload distribution, measure and improve.

## The design decision that decides the bill

The closing point is the reason to watch. Not everything should run on quantum. Put too much there and you pay for complexity you don't need; put too little and you miss the speed-up where it matters. The new design skill is drawing that line inside each application, per requirement. Every cloud migration has a team that lifted and shifted everything; this is the warning not to do it again.

## Who should watch

DevOps, SRE and platform engineers who want to know what quantum would mean for their pipelines and runbooks, explained without maths. If you want circuit-level detail or architecture diagrams, pair it with a more technical talk.

## Related Conf42 talks

- [Principium: the quantum hardware ecosystem](https://www.conf42.com/Quantum_Computing_2024_Archit_Srivastava_principium_hardware_ecosystem) by Archit Srivastava, for what sits behind the cloud API.
- [Quantum computing and AI for network management](https://www.conf42.com/Quantum_Computing_2024_Chaitanya_Kadiyala_Sadha_Chilukoori_quantum_network_management) by Chaitanya Kadiyala and Sadha Chilukoori, an operations use case in more depth.
- [Quantum computing for Rust software development](https://www.conf42.com/Rustlang_2024_Abhinav_Chunchu_quantum_software_development_computing) by Abhinav Chunchu, the developer's view of the same shift.

[Watch Srinivas Sriram Mantrala's talk](https://www.conf42.com/Quantum_Computing_2025_Srinivas_Sriram_Mantrala_quantum_cloudops_devops)

[Watch the talk on YouTube](https://youtu.be/krpU5lveOIc).

## Watch the talk

[Quantum CloudOps: Architecting Future-Ready Digital Ecosystems through Quantum-Enhanced DevOps and Hybrid Cloud Integration](https://www.conf42.com/Quantum_Computing_2025_Srinivas_Sriram_Mantrala_quantum_cloudops_devops) at Conf42 Quantum Computing 2025.
