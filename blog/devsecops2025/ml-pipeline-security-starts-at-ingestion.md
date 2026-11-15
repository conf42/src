# Your ML pipeline needs a security gate before the model exists

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/ml-pipeline-security-starts-at-ingestion

In short: Rajkumar Sukumar of AT&T at Conf42 DevSecOps 2025 on an AI-native DevSecOps framework, from trusted data ingestion to bias tests and audit trails.

A handful of manipulated images slipped into a training set can sink a multimillion-dollar model, and a standard CI/CD pipeline will wave it straight through. At Conf42 DevSecOps 2025, Rajkumar Sukumar, Lead Data/AI Engineering at AT&T Services, laid out a layered DevSecOps framework for machine learning that starts checking at data ingestion, long before anyone trains anything.

## Fast AI deployments ship their own failure modes

Rajkumar opens with a retail story: a visual quality inspection model works fine at launch, then product defects climb for weeks. The cause turns out to be a small amount of deliberately poisoned training data, and nobody noticed because the pipeline had no controls aimed at the model itself.

His second example is a 2023 loan approval system pulled within weeks because it kept rejecting applicants from one group. Nothing was broken in the code. The model had simply been trained on too narrow a set of people. Data poisoning, adversarial attacks, prompt injection, privacy leaks and ethical risk all arrive bundled with the speed of modern AI rollout, he argues, and classic DevOps has no gate for any of them.

## Six layers, starting with the data

The framework has six parts: secure data ingestion, privacy-preserving training, automated security testing, protected inference endpoints, ethical governance gates and continuous monitoring.

Ingestion is where trust starts. That means cryptographic verification of data sources, real-time anomaly detection, automatic PII detection and redaction, audit logs and data lineage. His lineage anecdote is the most relatable moment in the talk: an enterprise traced a model failure back to a single corrupted CSV file whose origin nobody could name.

For training on sensitive data he walks through three techniques: differential privacy (add noise so the model cannot memorise individuals), federated learning (the data stays at the source and only model updates travel, like learning from ten hospitals without moving patient records) and homomorphic encryption (banks collaborating on fraud detection without sharing raw customer data).

## Test the model like you test the code

The ML-specific CI stage adds adversarial testing that generates hostile inputs, static analysis, model hardening, input validation and dependency scanning of the ML frameworks. At inference time, he puts a web application firewall in front of the endpoint to filter bots, injection attempts and malformed requests, and to defend against model extraction.

## Ethics as a pipeline gate

The part that separates this from a generic security talk is governance by design. Rajkumar adds a pre-training ethical review, bias testing across demographic groups rather than in one isolated slice, and human-in-the-loop approval until the model is stable. One recent deployment he cites performed about 20% worse for a minority group; neither the data scientists nor the business knew why until they checked how little training data that group had.

To make governance scale he suggests policy as code with version-controlled rules and automated compliance checks on every ML pipeline, plus immutable audit trails (he mentions blockchain) so lineage is tamper-proof and regulator-ready evidence exists before anyone asks for it. A healthcare company that adopted the approach, he reports, saw zero security incidents, faster deployments and clean HIPAA and SOC audits.

His one-line takeaway: security and ethics cannot be bolted on to AI systems, they have to be built in.

## Who should watch

Platform and MLOps engineers who own the path from data lake to endpoint, security teams asked to sign off on a model they cannot read, and anyone who still treats the training set as somebody else's problem. It is a framework talk, so expect checklists rather than code.

## Related talks

- [DevSecOps for AI: Introducing MLSecOps for Software 2.0](https://www.conf42.com/DevSecOps_2022_Eugene_Neelou_ai_introducing_mlsecops_for_software_20) by Eugene Neelou, an earlier take on the same problem.
- [A Beginner's Guide to Adversarial Machine Learning](https://www.conf42.com/Machine_Learning_2024_Anmol_Agarwal_beginners_guide_adversarial) by Anmol Agarwal, for the attacks the testing stage should simulate.
- Lianne Potter on [the history of bias in AI and who built it](https://www.conf42.com/Machine_Learning_2025_Lianne_Potter_bias_builders_history).

[Watch Rajkumar Sukumar's talk](https://www.conf42.com/DevSecOps_2025_Rajkumar_Sukumar_ai_ml_ethics)

[Watch the talk on YouTube](https://youtu.be/2cGCqpuZoNU).

## Watch the talk

[DevSecOps for AI: Embedding Security and Ethics into the Machine Learning Pipeline](https://www.conf42.com/DevSecOps_2025_Rajkumar_Sukumar_ai_ml_ethics) at Conf42 DevSecOps 2025.
