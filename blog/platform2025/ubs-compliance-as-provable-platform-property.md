# Architect for Provability, Not Just Compliance

Conf42 Blog, 2025-08-27, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ubs-compliance-as-provable-platform-property

In short: UBS's Satish Manchana at Conf42 Platform Engineering 2025: policy engines, golden images and CI gates that make compliance provable in hybrid cloud.

Satish Manchana, a product owner at UBS with more than two decades in financial organisations, put the core idea of his Conf42 Platform Engineering 2025 talk in one sentence: we architect for high availability and performance, so we should also architect for provability. Applying a control is half the job; the platform has to show how and when it was applied, to a regulator, on demand.

Most platform engineers already know how to automate infrastructure. His point is that the hard part is doing it under SOX, GDPR, MiFID II and DORA at the same time, across continents.

## Regulations turn into engineering requirements

The talk gets specific fast. MiFID II wants trade events timestamped with millisecond accuracy, which means "NTP is running" is not an answer. You need timestamp logging, regular validation of NTP drift and retained logs for audit. Nobody verifies that by hand across hundreds of thousands of servers, so Satish's framing is that compliance is a data problem: the right telemetry, stored the right way, at the right time.

He's also honest about how they got here. Silos first, then shadow PowerShell scripts and Ansible roles to dodge the bottlenecks, then DevOps pipelines that were fast but each one bespoke (Jenkins here, GitLab there, AWS and VMware in between). At audit time there was no single baseline to point at. Platform engineering was the step that made the baseline a product.

## Four building blocks

**Provisioning frameworks.** Nothing gets deployed outside a policy-enforced path. Requests are declared as code (Terraform, plus Bicep and ARM templates on Azure) and pass through a policy engine: encryption at rest disabled means rejected; a public IP on a regulated subnet means rejected. Predefined landing zones ship with network topology, IAM, monitoring and logging already wired in. The lesson he stresses most: keep the policy engine independent of the IaC code, in its own repository, so when a regulator changes an encryption rule you update one place instead of rewriting Terraform modules everywhere.

**Golden images.** The pipeline starts from a vendor ISO, applies CIS Level 1 hardening and logging configuration, embeds agents for malware, file integrity, time sync, backup and endpoint protection, then runs vulnerability scans. Only passing images get versioned, signed, timestamped and published. Images rebuild on a fixed cadence (every two weeks in his example) with emergency rebuilds for events like WannaCry, so live servers get replaced rather than patched in place. Drift control uses PowerShell DSC, Azure DSC and Ansible.

**CI/CD gates.** Policy tests run like unit tests on every IaC change and fail with a precise reason, which also teaches engineers the regulatory intent. The same policies run periodically against deployed workloads to catch drift.

**Policy as code.** Rules live in Git with pull requests, reviews and tests, using tools such as HashiCorp Sentinel, OPA, AWS Config and Azure Policy. When a regulator asks when a rule changed and why, the answer is the commit history. A nice side effect: risk teams and engineers finally share one artifact, so neither has to read the other's native format.

## Self-service is the enforcement mechanism

The catalog offers pre-approved environment types, each a wrapper around the compliant provisioning path, golden image and policy runtime. Every resource carries metadata: who requested it, which policy version applied, which controls ran. His sharpest observation is that the faster self-service gets, the less incentive anyone has to bypass it.

In the case study, one type of server had been built at least six different ways depending on the region. Consolidating into one image pipeline and one policy engine cut provisioning from days to under an hour and reduced audit findings, and the risk function grew comfortable delegating control to engineering.

## Who should watch

Platform teams in banking, insurance, healthcare or anywhere with external auditors. If you're designing a policy-as-code rollout, the "separate policy from IaC" advice alone justifies the time.

## Related Conf42 talks

- [Sumeet L Ram: The Paved Road Had a Compliance Gate](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved), the same idea a year later.
- [Ara Pulido on policy-as-code for Kubernetes with OPA and Gatekeeper](https://www.conf42.com/Cloud_Native_2021_Ara_Pulido_poilcyascode_kubernetes_opa_gatekeeper).
- [Manisha Ponugoti on scaling compliant ML workloads in regulated industries](https://www.conf42.com/Kube_Native_2025_Manisha_Ponugoti_microservices_regulated_scalable).

[Watch Satish Manchana's talk](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid)

[Watch the talk on YouTube](https://youtu.be/TllEZtvROpk).

## Watch the talk

[Compliance-Aware Platform Engineering: Scaling Hybrid Cloud Automation in Regulated Financial Environments](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) at Conf42 Platform Engineering 2025.
