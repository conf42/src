# Shor's algorithm is coming for RSA, and the migration starts now

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/post-quantum-crypto-migration-primer

In short: Cloud advisor Vishnuvardhana Reddy Veeraballi gave a primer on post-quantum cryptography, QKD and the NIST picks at Conf42 Machine Learning 2025.

RSA rests on how hard it is to factor large numbers, and ECC on discrete logarithms over elliptic curves; Shor's algorithm solves both efficiently on a big enough quantum computer. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Vishnuvardhana Reddy Veeraballi, a cloud advisor, gave a compact primer on what replaces them: post-quantum cryptography you can run today, quantum key distribution that needs new hardware, and the NIST standards that tie it together.

It's a short overview talk, around 12 minutes, so treat it as an orientation map rather than an implementation guide.

## Three families of math that quantum computers don't break

Post-quantum cryptography (PQC) means algorithms that resist both classical and quantum attacks and still run on ordinary hardware. Veeraballi walks through three families:

- **Code-based cryptography** builds on the difficulty of decoding messages deliberately corrupted with errors, with security resting on problems like syndrome decoding and learning parity with noise.
- **Hash-based signatures** rely only on the strength of cryptographic hash functions, not on factoring, which makes them a conservative choice.
- **Lattice-based cryptography** uses hard problems over lattices, the grids you get by combining vectors. The textbook pictures are in 2D or 3D; real schemes use far more dimensions than anyone can draw.

The catch is cost. PQC typically needs more processing power and memory, and keys and signatures are larger, which hits bandwidth and storage. His comparison table puts it plainly: traditional crypto is efficient and well studied but quantum-vulnerable; PQC resists quantum attacks but is younger and heavier.

## QKD detects eavesdroppers, but only within range

Quantum key distribution takes the physics route. In his walkthrough, Alice encodes random bits into photon states and sends them to Bob, who measures with randomly chosen bases. They compare basis choices over a classical channel, keep the matching results, and check error rates. Any interception disturbs the quantum states, so an eavesdropper shows up as a raised error rate before the key is finalised with error correction and privacy amplification.

The flagship deployment is China's 2,000 km Beijing-Shanghai quantum link, alongside satellite-based QKD. The limits are real: distance constrained by quantum state degradation, slower key generation, specialised and expensive hardware, side-channel risk in the classical components, and awkward integration with existing networks.

## NIST has picked, so the excuses are shrinking

The standardisation timeline is the most actionable slide. NIST launched its post-quantum process in 2016, collected and evaluated candidates from 2017 to 2022, and in July 2022 announced its first selections: CRYSTALS-Kyber for encryption, and CRYSTALS-Dilithium, Falcon and SPHINCS+ for digital signatures. Kyber and Dilithium are lattice-based with good performance and reasonable key sizes, Falcon gives compact lattice signatures, and SPHINCS+ is the conservative hash-based option.

## Hybrid first, and test before you trust

For organisations, the hurdles are legacy compatibility, the performance hit of bigger keys, the risk of the transition period itself, and a shortage of people who can implement this correctly. His recommended path is hybrid encryption that combines a classical and a post-quantum algorithm, so you're protected against both today's and tomorrow's attackers, and still covered if a newer algorithm turns out to have a flaw. Adopt a forward-looking plan for data that could be harvested now and decrypted later, but test PQC carefully before full rollout so you don't swap one weakness for another.

## Who should watch

Security engineers and architects who need a fast refresher before a crypto-agility discussion, and anyone who has heard Kyber mentioned and wants the context. Skip it if you've already started a PQC migration; the related talks go further.

## Related Conf42 talks

- [Quantum Cybersecurity: Securing the Future in the Age of Quantum Computing](https://www.conf42.com/Quantum_Computing_2023_Husayn_Gokal_securing_future) by Husayn Gokal covers the same threat from a strategy angle.
- [Preparing for the Impact of Quantum Computing on Cloud Security](https://www.conf42.com/Quantum_Computing_2025_Pavan_Nutalapati_quantum_cloud_security) by Pavan Nutalapati maps it onto cloud estates.
- [AI-Driven Cybersecurity: Intelligent Threat Detection and Privacy in the Post-Quantum Era](https://www.conf42.com/MLOps_2025_Arfi_Siddik_Mollashaik_ai_driven_cybersecurity) by Arfi Siddik Mollashaik joins post-quantum privacy with ML defence.

[Watch Vishnuvardhana Reddy Veeraballi's talk](https://www.conf42.com/Machine_Learning_2025_Vishnuvardhana_Reddy_Veeraballi_cloud_security_cspm)

[Watch the talk on YouTube](https://youtu.be/11Lvsi_GIOw).

## Watch the talk

[Quantum Computing Encryption: Trends in Cybersecurity & the Race for Quantum-Safe Solutions](https://www.conf42.com/Machine_Learning_2025_Vishnuvardhana_Reddy_Veeraballi_cloud_security_cspm) at Conf42 Machine Learning 2025.
