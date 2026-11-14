# Harvest now, decrypt later means your API traffic is already at risk

Conf42 Blog, 2026-04-19. https://www.conf42.com/blog/cloud2026/post-quantum-migration-for-multicloud-apis

In short: Rajasingh Gandhi Ramdas of IBM at Conf42 Cloud Native 2026 on post-quantum migration for multi-cloud APIs: ML-KEM, hybrid TLS and crypto agility.

If your data has to stay secret for ten years, an attacker recording your TLS traffic today is already a problem. At Conf42 Cloud Native 2026, [Rajasingh Gandhi Ramdas](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture), Senior Technical Architect at IBM, laid out how to move multi-cloud API estates to post-quantum cryptography: what to prioritise, which NIST algorithms to use, and why the answer is hybrid TLS plus crypto agility rather than a big-bang swap.

It's a concise strategy talk, about 15 minutes, aimed at architects planning a multi-year programme.

## The threat is retroactive

The motivation is harvest now, decrypt later: adversaries capture encrypted traffic now and wait for cryptographically relevant quantum computers. RSA and elliptic curve cryptography fall to Shor's algorithm. AES-256 and hash functions hold up if you use larger key sizes. So the urgent work is public-key infrastructure: handshakes, signatures and certificates. Trade secrets, health records and strategic plans with a long confidentiality horizon are at risk today.

## The hallways matter as much as the front door

His best point is about where teams look. Everyone thinks of north-south traffic at the gateway, but east-west traffic inside the network is just as exposed to harvesting by an attacker already inside. Hybrid connectivity from cloud to on-prem often runs on legacy VPNs, among the most neglected parts of the estate. Internal CAs and mTLS have to migrate too, or the trust model collapses from the bottom up. In his words, "a quantum proof front door is useless" if the hallways are wide open.

He also stresses there is no single migration path: cloud platforms, mobile apps, third-party integrations and legacy systems all use different TLS stacks.

## Prioritise on three axes

The risk assessment starts with discovery (find the cryptography you actually use), then prioritisation and a migration backlog. Priority is three-dimensional: confidentiality lifetime of the data, with decades-long secrets first; API criticality, meaning revenue impact, regulatory scope and sensitivity; and migration feasibility, separating near-term items from ones needing vendor coordination or redesign.

## The algorithms are settled

NIST's post-quantum standards are published as FIPS 203, 204 and 205, which he sees as the end of the wait-and-see excuse. The portfolio he walks through: ML-KEM (Kyber) replaces RSA and ECDH for key exchange; ML-DSA (Dilithium) for digital signatures; SLH-DSA (SPHINCS+) as a hash-based backup with different assumptions; and FN-DSA (Falcon) for compact lattice signatures.

His recommendation is hybrid: derive session keys from both ECDH and ML-KEM, so an attacker has to break both. Classical crypto covers you if the new algorithms have an undiscovered flaw, and post-quantum covers you once quantum attacks arrive.

## Crypto agility is the real deliverable

He frames agility as a five-level maturity model: hard-coded algorithms, a library abstraction layer, centralised certificate management, algorithm choice as configuration, and automated agility with full observability. The goal is to change algorithms through configuration, not code rewrites.

Performance isn't free. Bigger keys mean bigger handshakes, which hurt on high-latency links. His abstract cites public keys 3 to 10 times larger than ECC and 10 to 30% latency overhead. Session resumption, connection pooling and HTTP/2 or HTTP/3 multiplexing offset some of it, and he insists on benchmarking in real production conditions.

## A four-phase roadmap, measured in years

Phase one builds the foundation: inventory, frameworks, library choice. Phase two puts hybrid TLS on sensitive external gateways and critical east-west service mesh traffic. Phase three rolls out to lower-priority APIs and partners. Phase four handles legacy systems and long-tail clients. The abstract puts the timeline at 24 to 36 months, and he calls it a programme touching networking, security, platform engineering, development, partner management and procurement.

## Who should watch

Security architects and platform leads who own TLS termination, service meshes or internal PKI and need a defensible order of work.

## Related Conf42 talks

- [Quantum-Resistant Native Go Programs: Taking the (Quantum) Leap](https://www.conf42.com/Golang_2021_Mathilde_Raynal_quantumresistant_native_go_programs) by Mathilde Raynal at Conf42 Golang 2021.
- [Quantum-Resistant Kubernetes: Securing Cloud Native Infrastructure for the Post-Quantum Era](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) by Derek Asir Muthurajan Caleb at Conf42 Kube Native 2025.
- [Quantum Computing: Implications for Security](https://www.conf42.com/Quantum_Computing_2022_Robert_Slade_implications_for_security) by Robert Slade at Conf42 Quantum Computing 2022.

[Watch Rajasingh Gandhi Ramdas's talk](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture) or the [YouTube recording](https://youtu.be/dj5wkGp7uTg).

## Watch the talk

[Post-Quantum Cryptography: Securing Multi-Cloud APIs Against Quantum Threats](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture) at Conf42 Cloud Native 2026.
