# A quantum-safe cloud starts with knowing where your crypto lives

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-safe-cloud-starts-with-crypto-inventory

In short: Pavan Nutalapati at Conf42 Quantum Computing 2025 on how Shor's algorithm threatens cloud encryption and the five moves to make before it lands.

The data an attacker steals from your cloud today doesn't have to be readable today. At Conf42 Quantum Computing 2025, Pavan Nutalapati, a senior technical lead, argued that cloud teams should start their post-quantum migration now, and that the first step is an unglamorous one: a cryptographic inventory of where RSA and ECC actually sit in your stack.

It's a short, structured talk, close to a briefing you could hand a security lead. The value is in the ordering: the threat, five strategies, three obstacles, and a to-do list.

## Shor breaks the keys, Grover dents the rest

Nutalapati starts from the mechanics. Qubits in superposition and entanglement let quantum machines run algorithms that are fundamentally different from classical ones, and two of them matter for security. Shor's algorithm factors large numbers exponentially faster than classical methods, which is a direct hit on RSA and ECC, the public-key cryptography behind identity, key exchange and TLS in nearly every cloud system. Grover's algorithm weakens symmetric encryption too, though less dramatically.

His point is that the cloud is built on exactly these primitives. Once a sufficiently powerful machine exists, the protections around RSA-2048 stop meaning much.

## Harvest now, decrypt later is the urgent part

Of the three risks he lists, Nutalapati calls the third the scariest. Attackers are already collecting encrypted traffic and archives, betting that a future quantum computer will open them. That makes the deadline for long-lived data (healthcare records, financial data, government secrets) much earlier than the arrival of the hardware. If your data needs to stay secret for ten years, your migration timeline is set by the attacker's storage budget, not by IBM's roadmap.

## Five strategies, from standards to inventory

The core of the talk is a five-part playbook:

- **Post-quantum cryptography.** NIST selected four algorithms in 2022: CRYSTALS-Kyber for key exchange, and CRYSTALS-Dilithium, Falcon and SPHINCS+ for digital signatures.
- **Quantum key distribution.** Secure by physics, since eavesdropping disturbs the quantum state, but expensive and range-limited. He sees it mostly in defence, finance and government.
- **Hybrid cryptography.** Pair a classical algorithm with a quantum-safe one for backward compatibility. He points to Google and Microsoft testing Kyber alongside traditional TLS in Chrome and Azure environments.
- **Cloud vendor initiatives.** Azure's quantum-safe VPN options, IBM Cloud's post-quantum testing, AWS's inventory tools and migration guidance.
- **Cryptographic inventory and risk assessment.** Find where encryption is used, which keys and algorithms are in place, and where sensitive data resides, then prioritise long-lived data. He adds zero trust as the safety net for weak spots you haven't fixed yet.

## The hard part is legacy, not math

Nutalapati is candid about why this is slow. Many quantum-safe algorithms don't play well with legacy systems and devices, and migration is a significant investment. His counter is the cost of doing nothing: he cites an average cloud breach at around $4.4 million before quantum attacks are even practical. "So doing nothing is the riskiest choice."

The path forward is four concrete steps: implement hybrid encryption, track the NIST standards as they mature, work with your cloud vendors, and run crypto audits.

## Who should watch

Security architects and platform leads who need a vocabulary and a plan to bring to a steering meeting. It's an overview, not an implementation guide; you won't see code or a migration of a real service. If you want the engineering detail, pair it with the talks below.

## Related Conf42 talks

- Mathilde Raynal on [Quantum-Resistant Native Go Programs](https://www.conf42.com/Golang_2021_Mathilde_Raynal_quantumresistant_native_go_programs), post-quantum crypto at the code level.
- Derek Asir Muthurajan Caleb on [Quantum-Resistant Kubernetes](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure), the same migration inside a cluster.
- Robert Slade on [Quantum Computing: Implications for Security](https://www.conf42.com/Quantum_Computing_2022_Robert_Slade_implications_for_security).

[Watch Pavan Nutalapati's talk](https://www.conf42.com/Quantum_Computing_2025_Pavan_Nutalapati_quantum_cloud_security)

[Watch the talk on YouTube](https://youtu.be/m1veul-6zy0).

## Watch the talk

[Preparing for the Impact of Quantum Computing on Cloud Security](https://www.conf42.com/Quantum_Computing_2025_Pavan_Nutalapati_quantum_cloud_security) at Conf42 Quantum Computing 2025.
