# Amazon Braket makes quantum hardware a pay-as-you-go AWS service

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/amazon-braket-hybrid-quantum-on-aws

In short: Naga Murali Krishna Koneru of Hexaware Technologies tours Amazon Braket at Conf42 Quantum Computing 2025, from hybrid jobs to shots and hardware.

You don't need a dilution refrigerator in the server room to run a quantum circuit; you need an AWS account. At Conf42 Quantum Computing 2025, Naga Murali Krishna Koneru, Technical Architect at Hexaware Technologies, gave a cloud engineer's introduction to quantum computing through Amazon Braket, AWS's managed service for running quantum algorithms on real hardware and simulators. It's an intro talk and says so: the value is in how cleanly it maps quantum vocabulary onto things an AWS person already knows.

Koneru comes at the subject with 11 years of AWS, DevOps and automation behind him, and it shows. Superposition and qubits get a slide each; the architecture diagram gets the attention.

## The classical computer stays in charge

The most useful framing in the talk is the hybrid model. A classical machine does the setup, the pre-processing and the final analysis, and drives the quantum device like a co-processor. The quantum side only gets the routines where superposition and entanglement help, then hands results back for interpretation. If you have ever offloaded a hot loop to a GPU, the shape is familiar.

Koneru also gives the scaling argument in one line: doubling a classical computer's power means doubling its bits, while a quantum computer gains that with one more qubit. That's the pitch for why anyone bothers with hardware this fragile.

## One SDK, several kinds of qubits

The talk lists the four SDKs most people will meet: Qiskit from IBM (which he calls the most used), Q# from Microsoft, Cirq from Google, and the Amazon Braket SDK. Then it walks the hardware Braket fronts:

- **Superconducting qubits**, among the most mature technologies, from IQM and Rigetti.
- **Ion traps** from IonQ.
- **Neutral-atom processors**, arrays of atoms manipulated by lasers, from QuEra.
- **Managed simulators** from AWS itself, for checking an algorithm before paying for real hardware time.

The practical point: Braket is a single front door to several qubit technologies, so you can switch hardware with minor code changes and compare results. Koneru also mentions AWS's February 2025 chip announcement (Ocelot), built on cat qubits that resist errors better than regular ones, which the talk credits with cutting error correction by 90%.

## Shots, tasks and hybrid jobs

The section worth bookmarking explains Braket's units of work. A shot is a single execution of a circuit on a device. A task bundles a series of shots and submits them together. A hybrid job is the classical-plus-quantum loop from earlier, run as one managed unit. You reach all of it through managed notebooks, the SDK or the Braket console, and it plugs into the usual AWS services: CloudWatch for notifications, S3 for results, IAM for permissions, KMS for encryption.

The billing model is pay as you go, which is the real democratisation argument here. No upfront hardware, no lab, just a bill that grows with the number of shots. Plan your experiments the way you plan your Lambda invocations.

## Who should watch

Cloud and platform engineers who have been asked whether the company should look at quantum and want a mental model in under half an hour. It's light on algorithms and heavy on service anatomy, which is exactly right for that audience. If you already write Qiskit for fun, skip to the Braket console walkthrough near the end, then go back to work.

The closing section looks ahead: fault-tolerant systems with fewer errors, cryptography use cases, quantum education and workforce development, and one day a quantum computer that fits on a desk.

## Related Conf42 talks

- Vincent van Wingerden on [High level programming for quantum circuits](https://www.conf42.com/Quantum_Computing_2024_Vincent_van_Wingerden_programming_quantum_circuits), the step after "hello, qubit".
- Daniel Goldsmith and Pippa Spencer-Williams on [Journey into Quantum](https://www.conf42.com/Quantum_Computing_2023_Daniel_Goldsmith_Pippa_Spencer_Williams_business_benefits), the business side of getting started.
- Abhinav Chunchu on [Quantum Leap: Rust Software Development with Quantum Computing](https://www.conf42.com/Rustlang_2024_Abhinav_Chunchu_quantum_software_development_computing).

[Watch Naga Murali Krishna Koneru's talk](https://www.conf42.com/Quantum_Computing_2025_Naga_Murali_Krishna_Koneru_cloud_aws)

[Watch the talk on YouTube](https://youtu.be/2t0g-I-vhBk).

## Watch the talk

[Quantum Computing Meets the Cloud: Harnessing AWS for the Next Computing Revolution](https://www.conf42.com/Quantum_Computing_2025_Naga_Murali_Krishna_Koneru_cloud_aws) at Conf42 Quantum Computing 2025.
