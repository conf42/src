# Zero trust for AI platforms, one layer at a time

Conf42 Blog, 2025-09-01, updated 2026-11-09. https://www.conf42.com/blog/platform2025/zero-trust-layers-for-ai-platforms

In short: JPMorgan Chase's Sudheer Obbu at Conf42 Platform Engineering 2025 on zero trust for ML pipelines, from service identity and mTLS to lineage and runtime monitoring.

A training job that scales from one node to hundreds of workers in a few minutes is a nightmare for an identity system built around people logging in. Sudheer Obbu, Senior Lead Software Engineer at JPMorgan Chase, built his Conf42 Platform Engineering 2025 talk on that mismatch: AI platforms need zero trust, and they need it applied to services, models and data, not just users.

Sudheer has spent 19 years on DevSecOps and multi-cloud architecture, and the talk reads like a layered reference architecture. The abstract's headline figure of 73% fewer incidents is not broken down in the talk itself; what you get instead is the framework and the order to build it in.

## The perimeter assumed your models lived in one building

The old model trusted anything inside the network. AI platforms span clouds, edge locations and hybrid environments, so there is no inside. They also bring their own attacks: model poisoning and data poisoning during training, adversarial inputs designed to force a misclassification, and model extraction, where an attacker rebuilds a proprietary model by watching its outputs. The cost of getting it wrong is a compromised model, stolen IP or a regulatory problem.

The zero trust principles are the standard three: verify explicitly, use least privilege, assume breach. What makes AI different is the shape of the system. One ML pipeline can involve dozens of services, from ingestion and feature stores to training orchestrators and model registries, and every hop needs the principles applied.

## Five layers, in build order

**Identity and access.** Every service gets a cryptographically verifiable identity. Mutual TLS between microservices means only authorised services can talk to each other, and certificate issuance, rotation and revocation have to be automated because the workloads appear and vanish at training-job speed.

**Network segmentation.** Microsegmentation isolates workloads, tenants and processing stages. The catch is that GPU-to-GPU traffic needs high throughput, and traditional network controls can add latency the training job will not tolerate. Sudheer's answer is software-defined networking that opens authorised channels on demand.

**Data and model protection.** This is the layer he calls the most critical, because a model is only as trustworthy as its training data. Lineage tracking with cryptographic integrity checks back to the source is the main defence against poisoning. Feature stores need permissions at the feature level. For the most sensitive computations he points at homomorphic encryption and secure multi-party computation, with the honest caveat that they are complex.

**Runtime security and observability.** AI jobs run long, burn resources and need privileged GPU access, so monitoring has to tell a legitimate burst from a breach. Signals worth watching include model accuracy degradation and unusual query patterns, alongside log aggregation that can cope with the volume from training jobs and model serving.

**Incident response.** Runbooks specific to AI: model rollback, handling a breach that touched training data, and automated quarantine of compromised workloads.

## Start with mTLS, and bring the data scientists

The rollout advice is incremental. Begin with service identity and mutual TLS, which pays off immediately. Move to broad network policies, then tighten into microsegmentation as you learn the traffic. Do data classification and lineage before anything exotic. And remember the cultural half: data scientists may see security controls as obstacles, so the controls have to help their productivity rather than hinder it.

On tooling he names Istio or AWS App Mesh for service-to-service auth, Kubernetes with specialised GPU node pools, and observability that tracks GPU utilisation, training loss and serving latency. Performance gets its own section: hardware-accelerated encryption, cached auth tokens, a trusted proxy for high-frequency calls, and sampling plus asynchronous logging so monitoring does not become the bottleneck. He ends on what is coming: confidential computing, federated learning, AI-assisted policy enforcement, and post-quantum cryptography.

## Who should watch

Platform engineers who just inherited a GPU cluster and a security review, and security engineers who need a map of where ML systems differ from web services. It is a framework talk, so pair it with your own threat model.

## Related Conf42 talks

- [Atif Siddiqui (Silicon Valley Bank) on cloud network segmentation in pursuit of zero trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust), for the network layer in depth.
- [Omer Farooq on LLM SecOps](https://www.conf42.com/Platform_Engineering_2024_Omer_Farooq_llm_secops), the generative AI version of the same problem.
- [Vaibhav Anil Vora (AWS) on zero trust as continuous verification](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security), the enterprise-wide view.

[Watch Sudheer Obbu's talk](https://www.conf42.com/Platform_Engineering_2025_Sudheer_Obbu_incidents_reducing_environments)

[Watch the talk on YouTube](https://youtu.be/kuzT122H6wk).

## Watch the talk

[Building Secure AI Platform Infrastructure: A Zero Trust Framework for Reducing Security Incidents by 73% in Cloud-Native Environments](https://www.conf42.com/Platform_Engineering_2025_Sudheer_Obbu_incidents_reducing_environments) at Conf42 Platform Engineering 2025.
