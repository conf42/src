# IoT devices outlive RSA, so quantum-safe security starts now

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-iot-security-long-lived-devices

In short: Gayathri Jeganmohan of Microsoft maps quantum computing onto IoT intelligence and security at Conf42 Quantum Computing 2025, from QKD to quantum signatures.

A satellite or a medical implant shipped today may still be talking to the network when a quantum computer can read its traffic. That is the sharpest thread in Gayathri Jeganmohan's talk at Conf42 Quantum Computing 2025, where the Microsoft software engineer split the quantum-meets-IoT story into two halves: what quantum computing can do for IoT intelligence, and what it does to (and for) IoT security.

It's a survey talk, broad rather than deep, and a good map for anyone who owns a fleet of connected devices and keeps hearing the word "quantum" in vendor decks.

## IoT has a data problem before it has a quantum problem

Jeganmohan's starting point is that IoT data is huge, unstructured and noisy: temperature, pressure and a dozen other sensor streams per factory, every second. Her claim is that quantum algorithms can find patterns in that kind of high-dimensional data more efficiently than classical ones, and she walks through where that is being tried:

- **Traffic analytics**: Volkswagen using a quantum algorithm to spot dense traffic areas and optimise urban flow.
- **Anomaly detection**: Cambridge Quantum's tooling for spotting unusual patterns in network traffic.
- **Recommendations**: research at Netflix and Amazon into quantum-inspired collaborative filtering.
- **Fraud**: quantum Monte Carlo methods, with Goldman Sachs and JPMorgan investing.
- **Genomics**: D-Wave working with healthcare startups on DNA analysis workflows.

## Keep the edge small, put the heavy model somewhere else

The machine learning section has the most architectural meat. Edge devices have limited power and energy, so today they lean on the cloud for inference and post-processing. Jeganmohan's picture is a backend where quantum resources handle training (quantum support vector machines and quantum kernel estimation get named) and fast inference, with results offloaded back to the device for real-time decisions. Her target use case is predictive maintenance in factories, plus quantum sensors fusing multiple signals for smart cities, agriculture and autonomous vehicles.

## Four security techniques, one deadline

Security is where the talk gets concrete. RSA and ECC, which today's classical machines can't break, become vulnerable to Shor's algorithm on a large enough quantum computer, and IoT was never designed with security in mind to begin with. Jeganmohan lists four responses:

1. **Defence against quantum attacks**: quantum-safe protocols, most urgent for long-lifecycle devices such as vehicles, medical implants and satellites.
2. **Quantum key distribution**: key exchange built on quantum mechanics that detects eavesdropping, with secure links between autonomous vehicles and roadside units as the example.
3. **Quantum random number generation**: truly random keys for secure session start-up on industrial sensors, instead of the pseudo-random output of a `rand` call.
4. **Tamper-proof identity**: quantum signatures, so only authenticated, quantum-signed devices can send actuation signals to critical infrastructure.

One thing worth keeping straight while you watch: post-quantum cryptography runs on ordinary classical chips, while QKD and QRNG need quantum hardware in the loop. For a constrained sensor, that difference decides what you can ship this decade. The talk's first point, protecting long-lived devices against future attacks, is the one you can act on with today's hardware.

## Who should watch

IoT architects, embedded security people and product owners with devices in the field for ten years or more. It is an overview, so expect breadth: if you want protocol detail on QKD, use this as the map and find the specialist talk next.

## Related Conf42 talks

- [Quantum-resistant native Go programs](https://www.conf42.com/Golang_2021_Mathilde_Raynal_quantumresistant_native_go_programs) by Mathilde Raynal, for what post-quantum code looks like in practice.
- [Transforming IoT data management: scalable architectures and security](https://www.conf42.com/DevOps_2025_Gokul_Balaguruswamy_Naidu_iot_data_security) by Gokul Balaguruswamy Naidu, the classical side of the same data problem.
- [Quantum computing: implications for security](https://www.conf42.com/Quantum_Computing_2022_Robert_Slade_implications_for_security) by Robert Slade, a security veteran's view of the threat.

[Watch Gayathri Jeganmohan's talk](https://www.conf42.com/Quantum_Computing_2025_Gayathri_Jeganmohan_quantum_iot_security)

[Watch the talk on YouTube](https://youtu.be/NOpys6h6xMA).

## Watch the talk

[Quantum-Powered IoT: Unlocking the Next Era of Intelligence & Security](https://www.conf42.com/Quantum_Computing_2025_Gayathri_Jeganmohan_quantum_iot_security) at Conf42 Quantum Computing 2025.
