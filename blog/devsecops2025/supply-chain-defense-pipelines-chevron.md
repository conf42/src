# Attackers stopped hitting your app and started hitting your pipeline

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/supply-chain-defense-pipelines-chevron

In short: Gresshma Atluri of Chevron at Conf42 DevSecOps 2025 on defending CI/CD and third-party supply chains with shift-left, RASP, vendor risk and zero trust.

A clean repository can still ship malware if the build runner is compromised. At Conf42 DevSecOps 2025, Gresshma Atluri, Cybersecurity Risk Analyst at Chevron, laid out a five-pillar defence framework for software supply chains, drawing on more than eleven years across investment banking, oil and gas, energy and consulting. Her abstract credits these strategies with reducing supply chain attacks by 57%.

The thread through all of it: it is rarely your own code that gets you into trouble. It is the dependencies, the pipelines and the third parties wrapped around it.

## Why the supply chain is the soft spot

A modern application is open-source libraries, third-party SDKs, cloud services and CI/CD tooling, with hundreds of components, many of them transitive dependencies nobody knows they use. Compromise one trusted delivery channel, such as a build pipeline, a popular package or an update mechanism, and you reach hundreds or thousands of organisations at once. She notes that the OWASP Top 10 and the OWASP CI/CD Top 10 now read like a description of the problem: vulnerable components, integrity failures, dependency chain abuse, poisoned pipeline execution and weak identity management.

Her case studies cover each failure shape. SolarWinds was a build system compromise that pushed a malicious update to around 18,000 customers. Log4j showed how a single buried library becomes a global emergency for teams that did not know they ran it. The 2024 CrowdStrike Falcon content update was not an attack, but from a resilience view it behaved like one: one update pipeline, global impact. And the Snowflake incidents showed attackers abusing stolen credentials at a third-party data platform.

## The attack vectors, in plain terms

She names three modern vectors. Dependency confusion: your CI pulls a public package with the same name as your internal one. Typosquatting: a tired developer mistypes one character and installs the wrong library. CI/CD compromise: the source is perfect and the payload is injected at build or packaging time.

Traditional security misses these, she argues, for three reasons: perimeter thinking assumes the inside is safe, checks happen at the end of the lifecycle while attacks happen mid-pipeline, and signing only proves origin, not safety. A signed artifact from a compromised build is still malicious.

## Five pillars

- **Shift-left DevSecOps.** Security in planning, coding and build, with IDE and pre-commit checks, continuous dependency scanning and SBOMs.
- **Secure CI/CD.** Least privilege for build agents and service accounts, secrets in vaults, ephemeral runners destroyed after each job, network segmentation, and a review process for third-party plugins and actions, since each plugin is code running in your pipeline.
- **Advanced detection.** Behavioural monitoring for odd events, like a pipeline suddenly pulling many new dependencies from unfamiliar sources, using SIEM and user and entity behaviour analytics. Runtime application self-protection (RASP) sits inside the app and can block a compromised dependency that tries to run a suspicious command.
- **Vendor risk management.** SOC 2 Type II, ISO 27001 and PCI DSS reviews where relevant, questions about the vendor's own SBOMs, signing and incident notification, and continuous monitoring rather than a one-time questionnaire.
- **Zero trust.** Strong authentication everywhere, every repo, agent and service proving its identity continuously, hardware-anchored signing and micro-segmentation to limit lateral movement.

## A phased roadmap

Foundation (three to six months): dependency scanning, SBOMs for key apps, code signing for critical artifacts, basic vendor assessment, MFA on platforms. Enhancement (six to twelve months): RASP for critical external services, behavioural monitoring of pipelines, SAST, DAST and container scanning, continuous vendor monitoring. Optimisation (ongoing): tune detections, streamline governance, add attestation and provenance tracking inspired by SLSA. Her closing point is that you do not have to choose between agility and security; you just have to design for both on purpose.

## Who should watch

Security engineers responsible for CI/CD, third-party risk teams who want the engineering view, and anyone who still thinks a signature means safe. It is broad rather than deep, which makes it a good map before picking the first control to build.

## Related talks

- [Supply Chain Attacks: Focused on NPM attacks](https://www.conf42.com/DevSecOps_2023_Danish_Tariq_Hassan_Khan_Yusufzai_supply_chain_npm_attacks) by Danish Tariq and Hassan Khan Yusufzai, for the dependency confusion and typosquatting details.
- [Supply Chain Security for OpenSource Projects](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects) by Sven Ruppert.
- Samikya Reddy Balguri on [incident management with zero trust architecture](https://www.conf42.com/Incident_Management_2024_Samikya_Reddy_Balguri_41_zero_trust_cyber).

[Watch Gresshma Atluri's talk](https://www.conf42.com/DevSecOps_2025_Gresshma_Atluri_supply_chain_threats)

[Watch the talk on YouTube](https://youtu.be/KK3CEw2BKQ0).

## Watch the talk

[DevSecOps Supply Chain Defense: Proactive Strategies Against Modern Cyber Threats](https://www.conf42.com/DevSecOps_2025_Gresshma_Atluri_supply_chain_threats) at Conf42 DevSecOps 2025.
