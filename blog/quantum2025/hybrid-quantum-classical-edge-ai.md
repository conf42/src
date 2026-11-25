# Hybrid quantum-classical edge AI, with the numbers on the slides

Conf42 Blog, 2025-05-23, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/hybrid-quantum-classical-edge-ai

In short: Anushree Nagvekar of AEye shows a hybrid quantum-classical split for edge AI at Conf42 Quantum Computing 2025, with latency, power and capacity figures.

Give the quantum side the optimisation and leave the IO and control loops to classical hardware. That is the split Anushree Nagvekar, Manager Software Engineering at AEye, argued for at Conf42 Quantum Computing 2025, in a short, number-dense talk on hybrid quantum-classical processing for edge AI. Her headline claim: neural networks with 3.2x more parameters while staying under 15 milliseconds of latency, against a classical-only ceiling of 1.4x.

## The edge is running out of headroom

The setup is familiar to anyone shipping embedded ML. Nagvekar cites a projection of 75 billion IoT devices by 2027, and data at the edge getting heavier: high-resolution video, medical scans, autonomous vehicle telemetry. Classical edge systems have to trade model complexity against real-time performance, and past a point latency becomes unmanageable. Her framing is that you shouldn't pick a side. The architecture is "not purely classical and not purely quantum", and the division of labour is the interesting part.

## Who does what in the hybrid

The split in the talk is clean enough to sketch on a whiteboard:

- **Quantum**: optimisation-heavy, high-dimensional work such as routing, scheduling and training complex networks.
- **Classical**: deterministic, routine tasks such as IO operations and simple control loops.

The same idea extends to resource allocation. Quantum units optimise across compute, memory, bandwidth and storage, and the talk says they react to changes in under 30 milliseconds, 4.2x faster than classical methods. The pipeline has four steps: detect complex dependencies, explore many configurations in parallel, execute, then predict and adjust as conditions change.

## The numbers, and how to read them

Nagvekar presents a lot of figures: 78% faster optimisation, 67% lower power consumption, latency down to 30 ms from a 120 ms baseline, 41% lower operational cost, and case studies with 82% anomaly detection and 43% fewer false alarms in manufacturing, 91% accuracy in real-time medical imaging with HIPAA compliance maintained, and 37% power savings in smart-infrastructure energy distribution. She says these come from real-world case studies rather than the lab.

The talk doesn't walk through the benchmark setups behind them (hardware, baselines, workloads), so treat them as the claims to go verify, not as a spec sheet. The architecture holds up without them.

On security, the hybrid stack uses lattice-based key exchange, tamper-evident signatures and multivariate polynomial encryption, the post-quantum families that run on ordinary chips, which is the right choice for a device with a battery.

## The roadmap starts on classical hardware

The most useful slide for a team that wants to try this is the rollout plan. Review the current infrastructure and find tasks worth optimising. Then test quantum-inspired algorithms on classical hardware and validate the boost before any real quantum integration. Only then move to hybrid workflows, tune task delegation and data flows, and scale with monitoring feedback loops. It is a gradual, low-risk path, and the classical-first step means you learn something even if the quantum part never pays off.

Future directions in the talk: domain-specific quantum hardware for edge devices, a quantum cloud at the edge, and quantum neural networks.

## Who should watch

Embedded and edge ML engineers who keep bumping into the latency-versus-model-size wall, and architects building industrial, automotive or smart-city systems. It is a quick talk, so it suits a lunch break; budget extra time for checking the numbers.

## Related Conf42 talks

- [Using the FLiPN stack for edge AI](https://www.conf42.com/Internet_of_Things_IoT_2023_Tim_Spann_David_Kjerrumgaard_flipn_stack_edge_ai_flink_nifi_pulsar) by Tim Spann and David Kjerrumgaard, a classical edge pipeline with Flink, NiFi and Pulsar.
- [QML: the next big thing](https://www.conf42.com/Quantum_Computing_2023_Karthiganesh_Durai_qml_next_big_thing) by Karthiganesh Durai, on the quantum machine learning half of the story.
- [At the edge of robotic applications](https://www.conf42.com/Internet_of_Things_IoT_2024_Chiara_Civardi_Petr_Aubrecht_robotics_applications_edge) by Chiara Civardi and Petr Aubrecht, for what edge constraints look like on robots.

[Watch Anushree Nagvekar's talk](https://www.conf42.com/Quantum_Computing_2025_Anushree_Nagvekar_quantum_edge_ai)

[Watch the talk on YouTube](https://youtu.be/nFdfCbQORrs).

## Watch the talk

[Quantum-Enhanced Edge AI: Revolutionizing Embedded Systems Through Hybrid Quantum-Classical Processing](https://www.conf42.com/Quantum_Computing_2025_Anushree_Nagvekar_quantum_edge_ai) at Conf42 Quantum Computing 2025.
