# ML threat detection and crypto agility for the post-quantum era

Conf42 Blog, 2025-09-16, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/ml-threat-detection-post-quantum-readiness

In short: Arfi Siddik Mollashaik of Securiti at Conf42 MLOps 2025 on multimodal ML threat detection, privacy-preserving training and post-quantum readiness.

Signature-based security tools struggle against zero-days, polymorphic and fileless malware and supply chain attacks, because there is no signature yet. At Conf42 MLOps 2025, Arfi Siddik Mollashaik, a solution architect in professional services at Securiti (securiti.ai) with 18-plus years in data security and privacy, made the case for layered ML threat detection, privacy-preserving training, and building crypto agility into ML pipelines before quantum computers force the issue.

It is a broad survey that covers a lot of ground quickly: detection architecture, feature engineering, privacy techniques, a rollout plan and a post-quantum outlook. Good as a map of the problem space; thin on implementation detail.

## No single model catches everything

Arfi's detection architecture combines three families. Supervised learning (random forests, gradient boosting, support vector machines) classifies known threats from labelled data. Unsupervised learning (isolation forests, one-class SVMs, DBSCAN clustering) flags deviations from normal behaviour, the route to catching what nobody has labelled yet. Deep learning (LSTMs, transformers, convolutional networks) handles complex patterns. Combining them, he argued, gives higher accuracy and fewer false positives than any one alone, and he cited a 93% detection rate for the combined approach.

The ML layer does four jobs: behavioural detection of anomalous users and systems, prediction of emerging threats from threat intelligence, adaptive response as the models learn from new data, and resource optimisation by prioritising alerts on risk and context.

## Features come from three places

Network traffic features cover protocol anomalies, flow metadata and volumes, temporal bursts and new destinations. User behaviour features look at authentication patterns, when people access what, data movement and command frequency. Host features watch process execution chains, system call sequences, resource usage, and registry and file system changes. Good feature selection, by his figure, raises model performance by 40% while cutting compute overhead. The real-time pipeline then runs ingestion from sensors, logs and network taps, streaming feature extraction, ensemble scoring into risk scores, and automated responses.

## Train on sensitive data without moving it

Security telemetry is full of sensitive data under GDPR, HIPAA, PCI and CCPA, so Arfi covered three privacy-preserving techniques. Federated learning trains on local data and exchanges no raw records. Differential privacy adds calibrated noise so outputs carry mathematical privacy guarantees while remaining useful. Homomorphic encryption allows computation on encrypted data without decrypting it.

## Shadow mode first, then post-quantum planning

His rollout is three phases: build data collection, labelling and feature engineering and integrate with existing SOC tools; deploy models in shadow mode next to current systems, tune thresholds against baselines and train the security team; then retire legacy detection gradually with CI/CD-driven model updates and automated retraining. The KPIs he tracks: classification latency, false positive rate, coverage of known attack vectors and zero-day detection success.

The post-quantum section looks further ahead. Shor's algorithm threatens RSA, ECC and Diffie-Hellman, NIST has standardised post-quantum algorithms (he named the CRYSTALS key encapsulation and Dilithium signature schemes), and he expects the transition over the next five to six years. His advice is crypto agility and hybrid classical plus post-quantum approaches, wired into ML pipelines now.

## Who should watch

Security engineers evaluating ML-based detection, and ML teams asked to work with security telemetry under privacy rules. If you need a deep treatment of any one area, use this as the index and follow up elsewhere.

## Related Conf42 talks

- Derek Asir Muthurajan Caleb (Broadcom) on [Quantum-Resistant Kubernetes](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure).
- Rajasingh Gandhi Ramdas (IBM) on [Post-Quantum Cryptography: Securing Multi-Cloud APIs Against Quantum Threats](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture).
- Chakradhar Sunkesula (Compass) on [AI-Driven Threat Detection and Multi-Layered Defense with Python](https://www.conf42.com/Python_2025_Chakradhar_Sunkesula_cloud_security_defense).

[Watch Arfi Siddik Mollashaik's talk](https://www.conf42.com/MLOps_2025_Arfi_Siddik_Mollashaik_ai_driven_cybersecurity)

[Watch the talk on YouTube](https://youtu.be/2wMBKhYm3hI).

## Watch the talk

[AI-Driven Cybersecurity: Intelligent Threat Detection and Privacy in the Post-Quantum Era](https://www.conf42.com/MLOps_2025_Arfi_Siddik_Mollashaik_ai_driven_cybersecurity) at Conf42 MLOps 2025.
