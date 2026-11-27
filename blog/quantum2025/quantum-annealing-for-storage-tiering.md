# Storage tiering is a QUBO problem, and annealers can take a swing

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-annealing-for-storage-tiering

In short: Gopinath Govindarajan of Deloitte Consulting maps quantum annealing, QML and post-quantum crypto onto enterprise storage at Conf42 Quantum Computing 2025.

Deciding which data block lives on NVMe and which goes to tape is an optimisation problem, and optimisation is the thing quantum annealers are built for. At Conf42 Quantum Computing 2025, Gopinath Govindarajan, Senior Solutions Specialist for Cloud Managed Services at Deloitte Consulting, laid out how quantum techniques could slot into enterprise storage: annealing for tiering, quantum machine learning for retrieval, and post-quantum cryptography for the data at rest.

Govindarajan brings 17 years of data engineering across healthcare, insurance and financial services, and the talk reads like an architect's reference deck: broad, layered, and with a phased roadmap at the end.

## The crisis is scale, retrieval and energy

He starts with why classical storage is straining. Architectures designed for sequential, predictable workloads now face petabytes a day from big data, IoT and real-time analytics. He names three limits: scaling bottlenecks where more storage brings more latency and management overhead, inefficient retrieval over high-dimensional or fragmented data, and the energy and infrastructure cost of keeping it all spinning.

## Tiering as a cost function

The most concrete idea is storage tiering. Tier 0 is NVMe for caching and real-time streams, tier 1 is SSD for frequently accessed files, tier 2 is HDD for archives and backups, and the last stop is tape or cold storage. The hard part is assigning each data object to the right tier dynamically.

Govindarajan frames that assignment as a QUBO (quadratic unconstrained binary optimisation) problem: minimise total storage cost and access latency by mapping data blocks to tiers, subject to performance requirements and capacity limits. Quantum annealing, which finds low-energy states through tunnelling and superposition, is the solver he points to, with D-Wave-style systems as the example. Anyone who has hand-tuned a lifecycle policy in S3 will see why a solver is attractive.

## QML for retrieval, PQC for the archive

Two more pieces round out the architecture. On the machine learning side he covers quantum k-nearest neighbours for similarity-based retrieval and quantum support vector machines for classifying data for compression, deduplication or hot-versus-cold tiering.

On security, the argument is about long-lived data. Stored data might be decrypted later by a quantum computer, so storage systems should adopt post-quantum cryptography (lattice-based schemes such as CRYSTALS, plus code-based, multivariate and hash-based families), quantum random number generation for better keys, and quantum watermarking for tamper detection and provenance.

He is careful that hybrid systems "do not store quantum data directly", since quantum memory doesn't scale yet. The quantum part optimises and secures classical storage; it doesn't replace it.

## Results and a roadmap

The talk reports implementation results by industry, including, for financial services, a 41% reduction in operational storage spending while handling four times the transaction volume at sub-5 ms retrieval latency. Treat those as the speaker's figures: the talk doesn't walk through the benchmark setup, and the case studies elsewhere describe quantum-inspired algorithms running on classical hardware.

The roadmap is the most reusable part. Phase one is awareness: assess risks, find sensitive workloads, train teams, set goals. Phase two is a proof of concept, such as lattice-based encryption for backups, watermarks on sensitive files, or annealing for tiering. Phase three is testing for latency, throughput, compatibility and security under simulated threats. Phase four is enterprise rollout, starting from low-risk targets like archival storage and backups.

## Who should watch

Storage and data platform architects who want a map of where quantum ideas touch their systems, and anyone writing a quantum-readiness plan for a data estate. It's a survey, not a demo; you won't see a QUBO formulated line by line.

## Related Conf42 talks

- Peter den Haan on [Quantum and Quantum-Inspired Annealing: the State of Play](https://www.conf42.com/Quantum_Computing_2023_Peter_den_Haan_annealing_state_of_play), the solver itself in depth.
- Trista Pan on [Dynamic data masking and encryption for MySQL/PostgreSQL](https://www.conf42.com/Quantum_Computing_2023_Trista_Pan_dynamic_data_masking_encryption_mysql_postgresql).
- Nehal Singh on [Securing Robot Networks for the Quantum Era](https://www.conf42.com/Robotics_2025_Nehal_Singh_robotics_quantum_security).

[Watch Gopinath Govindarajan's talk](https://www.conf42.com/Quantum_Computing_2025_Gopinath_Govindarajan_quantum_storage_systems)

[Watch the talk on YouTube](https://youtu.be/KNMTfPKawIQ).

## Watch the talk

[Quantum-Accelerated Storage Systems: Revolutionizing Enterprise Data Architectures Through Quantum Computing](https://www.conf42.com/Quantum_Computing_2025_Gopinath_Govindarajan_quantum_storage_systems) at Conf42 Quantum Computing 2025.
