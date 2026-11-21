# Secure multi-tenant platforms for banks start at the admission controller

Conf42 Blog, 2025-08-12, updated 2026-11-09. https://www.conf42.com/blog/platform2025/securing-multi-tenant-platforms-in-finance

In short: Nageswara Rao Nelloru at Conf42 Platform Engineering 2025 on securing multi-tenant Kubernetes for finance with mTLS, admission control and policy as code.

A financial platform team has two jobs that pull in opposite directions: satisfy the regulator and let developers ship. At Conf42 Platform Engineering 2025, Nageswara Rao Nelloru of Marquee Technology Solutions, a technology lead with 20 years mostly in financial services, walked through the controls that let a multi-tenant cloud-native platform do both.

His abstract frames the stakes with results from platform teams securing financial operations across 530+ organisations, including incident detection cut from 21 days to 4 hours. The talk itself is a layered tour of the controls rather than a breakdown of those numbers.

## The threat list is long

Nageswara opens with the threats financial services face: increasingly AI-assisted attacks, phishing and social engineering, ransomware, insider threats, and third-party and supply chain risk. His goal is a multi-tenant platform that balances heavy security demands with rapid innovation as institutions move to cloud-native architectures. The platform evolves from managing infrastructure to running a self-service ecosystem with zero trust built in.

## Isolation and encryption by default

Multi-tenancy in finance means careful isolation boundaries, data segregation and access control, implemented as micro-segmentation for defence in depth at every layer. Service mesh does a lot of the work: fine-grained traffic control, mutual TLS for all service-to-service traffic, and security policies that travel with the workload so protection is consistent wherever it runs.

## Admission control is the gate

The Kubernetes section covers the container lifecycle: image scanning and vulnerability management, secure configuration, and runtime monitoring that flags anomalous behaviour. The piece he dwells on is admission controllers, the gatekeepers that check everything from resource limits to security context before a workload is admitted. Non-compliant workloads are rejected automatically, with clear feedback on how to fix them, and every decision is logged for compliance reporting and later investigation. A rejection with a fix-it hint beats a pentest finding six months later.

## GitOps and policy as code

GitOps treats infrastructure changes with the same review rigour as application code. Policy as code captures security requirements in a form machines can enforce and humans can read. Progressive security gates validate changes before they land, and vulnerability and compliance scanning run throughout the pipeline. Repeatable deployment patterns eliminate configuration drift.

Identity gets its own section: automated provisioning and de-provisioning from authoritative sources, attribute-based access that considers context beyond roles, and proper management of non-human identities such as service accounts, API keys and secrets. Observability ties it together with distributed tracing, SIEM correlation of platform events with security signals, automated response that contains threats while preserving evidence, and continuous compliance evidence collection instead of manual documentation.

## Secure has to be usable

His most important line of argument comes late: the most secure platform delivers no value if developers can't use it. Self-service with policy enforced automatically, templates and examples, and watching where developers hit friction are what keep teams on the paved road. He closes with chaos-style security experiments to find weaknesses before attackers do, and a reminder to design controls that can be updated as threats and regulations change.

## Who should watch

Platform and security engineers in regulated industries, especially anyone writing the admission and policy layer for a shared Kubernetes estate. The transcript is dense with terminology; the slides help.

## Related Conf42 talks

- [Ashish Dibouliya on Kube-native AI data governance for banking compliance](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance) covers the data side of the same problem.
- [Peter O'Neill on Terraform apply secured by Open Policy Agent](https://www.conf42.com/Site_Reliability_Engineering_2022_Peter_ONeill_terraform_apply_secured_open_policy_agent) is policy as code in practice.
- [Piotr Zaniewski on multi-tenant GPU sandboxes with vCluster](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) shows another approach to tenant isolation.

[Watch Nageswara Rao Nelloru's talk](https://www.conf42.com/Platform_Engineering_2025_Nageswara_Rao_Nelloru_tenant_services_multi)

[Watch the talk on YouTube](https://youtu.be/WooIVOPbYfQ).

## Watch the talk

[Platform Engineering Security: Building Resilient Multi-Tenant Infrastructure for Financial Services](https://www.conf42.com/Platform_Engineering_2025_Nageswara_Rao_Nelloru_tenant_services_multi) at Conf42 Platform Engineering 2025.
