# Quantum-ready architecture is mostly event queues and job routers

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-ready-enterprise-architecture-patterns

In short: JPMorgan Chase's Laxmikanth Mukund Sethu Kumar at Conf42 Quantum Computing 2025 on hybrid patterns that prepare enterprise systems for quantum.

If your platform already runs on event queues, APIs and Kubernetes jobs, you are closer to quantum-ready than you think. Laxmikanth Mukund Sethu Kumar, Executive Director at JPMorgan Chase, argued exactly that at Conf42 Quantum Computing 2025: quantum will coexist with classical computing, not compete with it, and the work enterprise architects can do today is integration, not physics.

The abstract promises a systems view drawn from platforms built for banks, airlines and government, and the talk sticks to it. Quantum mechanics gets one slide; architecture gets the rest.

## What today's DevOps stack is missing

The useful starting point is the gap list. Quantum workloads don't fit existing DevOps stacks yet, and Sethu Kumar names three missing pieces: job orchestration, state isolation for quantum workloads, and latency tolerance. He also asks architects to stop thinking in either/or terms: a qubit's state is probabilistic, and so are its results, so the systems around it should expect distributions, not single answers.

The supply side is already there. AWS Braket, IBM Quantum and Azure Quantum all expose quantum hardware through cloud-native APIs.

## Three tiers and a clean seam

His hybrid architecture is three layers:

- **Application tier**: microservices and APIs, unchanged.
- **Orchestration tier**: quantum job routers and queues.
- **Backend tier**: classical compute, quantum compute, or both.

The rule for the middle layer is the line to remember: decouple the quantum logic from the orchestration logic. Middleware owns session management, job queuing, error retries and result normalisation, so a flaky quantum backend never leaks into your business code.

## Patterns you already know

The design patterns are deliberately familiar:

- **Quantum as a service**, alongside IaaS and SaaS.
- **Quantum triggers from classical event queues** such as Kafka: a classical service publishes, a quantum consumer reacts.
- **Serverless quantum microservices**, for example an AWS Lambda function that kicks off a Braket job.
- **Cloud-native abstractions**: containers for local quantum simulation, Kubernetes job runners for orchestrating quantum flows, and CI/CD pipelines for quantum kernels.

Tools named include the Braket SDK and gRPC bridges. Security is zero trust across both worlds; interoperability depends on vendor-neutral interfaces and standards such as QIR; and observability means quantum job telemetry flowing into Prometheus and OpenTelemetry like everything else. If your quantum job can't be seen on the same dashboard as the rest of the system, it isn't production-ready, whatever the qubit count.

## A five-step roadmap with a safe middle

The roadmap is the most reusable slide: identify quantum-able problems (scheduling, ML model tuning), build a dev sandbox on emulators, integrate with job orchestration and message buses, pilot a hybrid service on a non-critical path, then promote gradually to production workflows. The goal, in his framing, is to experiment without rewriting the stack, using modular adapter layers, simulators and mature hybrid CI/CD.

## Who should watch

Enterprise and platform architects, engineering leads and anyone who has been asked for a quantum strategy and wants one that fits on an architecture diagram. It's short, clear and free of hype. Physicists will find nothing new; integrators will find a checklist.

## Related Conf42 talks

- [Empowering sector readiness with quantum solutions](https://www.conf42.com/Quantum_Computing_2023_Abdullah_Alsalman_empowering_sector_readiness) by Abdullah Alsalman, readiness from the sector level down.
- [Empowering executives to embrace quantum computing](https://www.conf42.com/Quantum_Computing_2023_Vardaan_Sahgal_empowering_executives) by Vardaan Sahgal, for the conversation with leadership.
- [Quantum computing: building responsive and adaptive systems](https://www.conf42.com/Quantum_Computing_2024_Nitish_Mehrotra_quantum_systems_future) by Nitish Mehrotra, another systems-first view.

[Watch Laxmikanth Mukund Sethu Kumar's talk](https://www.conf42.com/Quantum_Computing_2025_Laxmikanth_Mukund_Sethu_Kumar_classical_quantum_enterprise)

[Watch the talk on YouTube](https://youtu.be/w2ehzwRRpvY).

## Watch the talk

[Bridging Classical and Quantum: Preparing Enterprise Architecture for the Quantum Era](https://www.conf42.com/Quantum_Computing_2025_Laxmikanth_Mukund_Sethu_Kumar_classical_quantum_enterprise) at Conf42 Quantum Computing 2025.
