# NISQ-era quantum value comes from small, well-scoped pilots

Conf42 Blog, 2025-06-12, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/nisq-value-comes-from-small-scoped-pilots

In short: Meta's Sai Kaushik Ponnekanti at Conf42 Quantum Computing 2025 on getting real value from noisy quantum hardware with hybrid workflows and tight scope.

Today's quantum computers are noisy, small and expensive per shot, and they can still earn their keep if you ask them a small enough question. That was the argument Sai Kaushik Ponnekanti, Software Engineer at Meta, made at Conf42 Quantum Computing 2025: in the NISQ era, value comes from slicing a business problem down to tens of qubits, wrapping it in classical pre- and post-processing, and celebrating modest wins.

The abstract promises big gains; the talk itself is refreshingly restrained. Ponnekanti repeatedly stops to say a result was a pilot, a proof of concept, or "small wins", which makes his examples easier to trust.

## Scope the problem until it fits the machine

The core idea is that NISQ hardware (tens to low hundreds of qubits, noisy gates, short coherence times) only helps on scoped problems. A logistics network becomes a regional slice with a dozen stops. A portfolio becomes 30 to 40 assets. A molecule becomes a small one. If a problem needs 60 qubits and the device offers 30 with good fidelity, you find a reduced instance or partition it.

He compares it to learning to sail in calm water before tackling the ocean, and the analogy holds: the point of today's pilots is mostly the skill you build.

## Hybrid is the default, not a compromise

Every example in the talk is a hybrid loop. Classical pre-processing narrows a candidate set, a quantum circuit refines or evaluates the short list, and classical post-processing interprets the output. In the pharma example, classical docking produced 50 candidate ligands, quantum-enhanced evaluation trimmed them to 15, and the top five went to lab assays. In logistics, classical solvers handle the broad layout while quantum routines refine specific legs.

Algorithms like QAOA encode an optimisation objective into a shallow circuit and sample candidate solutions; the classical side keeps the best ones.

## Noise is something you engineer around

The most practical section is on error mitigation. Ponnekanti describes zero-noise extrapolation: run the same circuit with gate durations stretched to amplify noise, then extrapolate back toward a zero-noise estimate. He also mentions randomised compiling. Both cost extra circuit runs and classical compute, which is the price of usable output.

The engineering hygiene list is one any team can adopt today: prototype on simulators with noise models, run only final circuits on hardware, keep circuits in version control, and log run metadata (date, device, calibration metrics, circuit version) so you can compare results as hardware changes. He has juggled SDKs across Qiskit, Cirq and an ion-trap system via AWS, and the quirks are real.

## Pilots need a business metric

The organisational advice is blunt. Pick use cases with clear metrics, build a small team, define success criteria up front. One organisation he describes treated matching classical results within 5% as a worthwhile stepping stone. The anti-pattern is months of random circuits with no business problem attached, ending in reports "full of technical jargon, but little business insight."

## Who should watch

Engineers and tech leads who have been told to "look into quantum" and want a sane way to start: what to pick, how to run it, what to expect. Physicists will find the theory light, by design.

## Related Conf42 talks

- Abhigyan Mishra on [Quantum-inspired algorithms in the NISQ era](https://www.conf42.com/Quantum_Computing_2023_Abhigyan_Mishra_algorithms_quantum_benefit_nisq_era).
- Amit Taneja on [Quantum Advances in Pharma](https://www.conf42.com/Quantum_Computing_2024_Amit_Taneja_quantum_advances_pharma), the drug discovery thread in more depth.
- Carlos Murilo Romero Rocha introducing [QC2, open-source software for quantum chemistry](https://www.conf42.com/Quantum_Computing_2024_Carlos_Murilo_Romero_Rocha_quantum_chemistry_software).

[Watch Sai Kaushik Ponnekanti's talk](https://www.conf42.com/Quantum_Computing_2025_Sai_Kaushik_Ponnekanti_quantum_business_value)

[Watch the talk on YouTube](https://youtu.be/TsX2D5U1iiY).

## Watch the talk

[Quantum Advantage: Unlocking Business Value from Quantum Computing in the NISQ Era](https://www.conf42.com/Quantum_Computing_2025_Sai_Kaushik_Ponnekanti_quantum_business_value) at Conf42 Quantum Computing 2025.
