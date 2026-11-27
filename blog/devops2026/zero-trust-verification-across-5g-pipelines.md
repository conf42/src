# Zero trust in a 5G pipeline means every stage proves itself

Conf42 Blog, 2026-01-22. https://www.conf42.com/blog/devops2026/zero-trust-verification-across-5g-pipelines

In short: Vijayakumar Venganti of Cisco at Conf42 DevOps 2026 on embedding zero-trust checks into every CI/CD stage of 5G and cloud-native delivery.

If your pipeline deploys several times a day, a security review at the end is a speed bump nobody slows down for. At Conf42 DevOps 2026, [Vijayakumar Venganti](https://www.conf42.com/DevOps_2026_Vijayakumar_Venganti_zerotrust_security_networks), Software Engineer at Cisco Systems, argued that the only check that keeps up with machine-speed delivery is one that runs at machine speed: zero-trust verification wired into every stage, from the commit to the network slice.

This is a compact framework talk, about a quarter of an hour, with no live demo. Its value is the map: what to verify at each layer, and why 5G makes the old perimeter model collapse faster than it does elsewhere.

## The perimeter dissolved before anyone noticed

Venganti's starting point is that perimeter security assumes threats stay outside, and cloud-native architecture removed the outside. 5G adds edge computing, network slicing and swarms of IoT devices on top, so the attack surface grows with each push. He cites survey figures for the shift (over 60% of organisations adopting zero trust, with plans pointing to 81%) and a private 5G penetration test in which industrial networks without zero trust were exposed to insider threats in under 30 minutes.

The failure modes he lists will be familiar to anyone who has audited an old CI setup: static rule-based access control that can't follow changing infrastructure, one-time authentication that leaves unverified windows, and lateral movement that nobody sees once an attacker is in.

## Verify at four levels, automatically

The core of the talk is a checklist for CI/CD, split by level:

- **Code**: sign every commit, run static analysis, scan dependencies.
- **Container**: scan images, verify provenance, apply runtime policy.
- **Infrastructure**: validate infrastructure as code, detect configuration drift, enforce immutability.
- **Network**: a service mesh with mutual TLS and microsegmentation.

None of that is exotic. The point he presses is that manual review won't work at this scale, so each check has to execute automatically and consistently. Remove static credentials, and have every step produce a cryptographic attestation, so the chain runs unbroken from developer to production. He calls it an immutable chain of custody, which is also a good test for your own pipeline: could you prove, for the artifact running right now, who built it and what checked it?

## A four-layer architecture for 5G

For the 5G side, Venganti proposes four layers. The access layer does continuous identity verification with MFA, mutual TLS, container attestation and behavioural monitoring. The transport and segmentation layer uses 5G slicing policies and zero-trust gateways to stop lateral movement. A policy intelligence layer learns baselines for users, services and infrastructure and adapts policy in real time when behaviour deviates. On top sits a control and orchestration layer: a central zero-trust controller with policy as code, immutable audit records for every run, and a feedback loop so risk insights update the security posture.

He also suggests using 5G slicing itself for pipeline isolation, and edge intelligence for low-latency detection. That is the most telecom-specific idea in the talk, and the one platform teams outside 5G can skip.

## The hard part is people

The talk is honest about cost: operational complexity, new attack surfaces from the AI components themselves, performance overhead, a skills gap and a cultural shift. His answer is training and phased adoption, and a closing line that zero trust is a continuous process rather than a destination. Anyone who has rolled out mTLS across a few hundred services will nod at "phased".

## Who should watch

Engineers building delivery pipelines for telecom or edge workloads, and anyone who needs a one-page mental model of where zero-trust controls belong in CI/CD. If you already run signed commits, SLSA provenance and a mesh with mTLS, treat it as a sanity check rather than new material.

## Related Conf42 talks

- [Beyond Perimeters: Implementing Zero Trust at Enterprise Scale](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust) by Naveen Kumar Birru at Conf42 Platform Engineering 2025.
- [Empowering Cloud-Native Solutions with Software-Defined Networking for IoT and 5G](https://www.conf42.com/Cloud_Native_2025_Sai_Charan_Madugula_networking_iot_5g) by Sai Charan Madugula at Conf42 Cloud Native 2025.
- [Zero Trust Security: From Perimeter Defense to Continuous Verification in the Modern Enterprise](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security) by Vaibhav Anil Vora at Conf42 Machine Learning 2025.

[Watch Vijayakumar Venganti's talk](https://www.conf42.com/DevOps_2026_Vijayakumar_Venganti_zerotrust_security_networks) or the [YouTube recording](https://youtu.be/cIOwsgL4pzM).

## Watch the talk

[Zero-Trust Security in DevOps: Automating Trust Verification Across 5G Pipelines](https://www.conf42.com/DevOps_2026_Vijayakumar_Venganti_zerotrust_security_networks) at Conf42 DevOps 2026.
