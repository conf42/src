# Protect data in use with confidential VMs, trusted launch and zero trust

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/confidential-vms-trusted-launch-and-zero-trust

In short: Microsoft's Priyadarshni Shanmugavadivelu showed at Conf42 JavaScript 2025 how TEEs, TPM-backed boot and zero trust stack up to secure cloud VMs.

Encryption at rest and in transit stop helping the moment your data is loaded into memory on someone else's hardware. At Conf42 JavaScript 2025, Priyadarshni Shanmugavadivelu, Principal Product Manager at Microsoft, laid out three layers that close that gap for cloud VMs: confidential computing for data in use, trusted launch for boot integrity, and zero trust for everything that talks to the VM afterwards.

It's a security architecture talk drawing on her work on Azure's VM platform, not a JavaScript one, and it works as a clear overview of how the pieces fit.

## Data in use was the missing third

Her framing: cross-tenant attacks, memory scraping and hypervisor breaches all target data while it is being processed, and perimeter-based VM security wasn't built for that. Confidential computing uses hardware trusted execution environments (TEEs) that keep data encrypted while the CPU works on it, invisible even to the cloud provider and system administrators.

The two main technologies she covered:

- **AMD SEV-SNP** (Secure Encrypted Virtualization with Secure Nested Paging): per-VM memory encryption with integrity checks, protection against hypervisor-level attacks, and attestation of boot integrity.
- **Intel TDX** (Trust Domain Extensions): workload isolation at the CPU level, "trust domains" enforced by hardware boundaries, with remote attestation.

Use cases: analytics across organisations that can't share raw data, training models on medical or financial data, and key management where keys never appear in plain text.

## Trusted launch: a chain of trust before the first process runs

TEEs protect a running VM, while trusted launch protects the boot. It builds on four steps: a TPM 2.0 chip as hardware root of trust, measured boot that records every boot component in platform configuration registers, remote attestation that compares those measurements to known-good baselines, and orchestrator policies that only let trusted VMs run. If a component was tampered with, attestation fails and the VM doesn't start. That's how you catch rootkits before the workload is even up.

The DevOps part is the most practical. Put attestation into CI/CD: write policy as code saying which images must be verified, attest each VM automatically before containers are deployed, and monitor continuously so integrity drift raises an alert. Trust becomes something checked on every deployment instead of once at setup.

## Zero trust between VMs

Then the network. "Never trust, always verify" applied to VMs means none is trusted for being on the same network. She gave three mechanisms: microsegmentation tied to workload identities instead of IP addresses, continuous re-authentication of every request with cryptographic identity, and behavioural monitoring that triggers an automated response to unusual connections or privilege escalations. The payoff is limiting lateral movement: an attacker with stolen credentials still can't hop across VMs, and an admin pulling unusual data volumes at odd hours gets noticed.

## What it costs

She tied the layers to compliance: network segmentation and cardholder data protection for PCI DSS 4.0, protected health information under HIPAA, and data minimisation and encryption for GDPR. On performance, she put TEE overhead at roughly 2 to 10 percent depending on workload, with remote attestation adding hundreds of milliseconds that caching and using TEEs only where needed can reduce. Looking ahead: post-quantum cryptography in TEEs, homomorphic encryption for computing on encrypted data, and ML-based anomaly detection for zero-day attacks.

## Who should watch

Cloud and platform engineers handling regulated workloads, security architects comparing SEV-SNP and TDX, and anyone who has to explain to compliance why "encrypted at rest" isn't the whole answer. If you build Node.js services, it's useful context on what your VM is doing underneath, but you won't see code.

## Related talks

- [Scaling Secure Enclaves: Confidential Computing in Go-Powered Distributed Systems](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential) takes TEEs into application code.
- [Cloud Network Segmentation in pursuit of Zero Trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) goes further into the segmentation layer.
- [Real Zero Trust Security for Containerized Environments](https://www.conf42.com/JavaScript_2024_Ammar_Khan_zero_trust_security) applies the same principle to containers.

[Watch Priyadarshni Shanmugavadivelu's talk](https://www.conf42.com/JavaScript_2025_Priyadarshni_Shanmugavadivelu_scaling_trust_security)

[Watch the talk on YouTube](https://youtu.be/93LtQ5pi3Ko).

## Watch the talk

[Scaling Trust: VM Security with Confidential Computing and Zero Trust Architecture](https://www.conf42.com/JavaScript_2025_Priyadarshni_Shanmugavadivelu_scaling_trust_security) at Conf42 JavaScript 2025.
