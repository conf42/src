# Make identity the control plane of your cloud platform

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/identity-governance-as-platform-control-plane

In short: Sony Interactive Entertainment's Anjan Kaleru at Conf42 Platform Engineering 2025 on zero trust IAM, continuous compliance and self-service access for developers.

Developers want access quickly, security wants tight control, and auditors want evidence. Anjan Kaleru, Staff IAM Engineer at Sony Interactive Entertainment with more than ten years in identity and access management, opened his Conf42 Platform Engineering 2025 talk with that three-way tug of war, and his answer is to put identity at the centre of the platform so all three get what they need from the same automation.

His framing is borrowed from Gartner and repeated for good reason: identity is the new security boundary. Every login, every API call, every device check is an access decision.

## Why the old tools stopped fitting

VPNs and firewalls assumed a network you could draw a line around. Cloud platforms broke that, and the usual response, a patchwork of tools bolted on one at a time, adds confusion instead of fixing anything. Anjan traces identity through three phases: the centralised Active Directory and VPN era, the cloud disruption where hundreds of microservices brought their own rules, and the infrastructure-as-code era where access rules change as fast as the code. Most breaches, he notes, come down to weak or unmanaged identities, which is why the last phase needs zero trust and API-first identity platforms.

## What zero trust IAM looks like day to day

Zero trust here means every request is checked, every time. His examples are concrete. Contractors get temporary access with MFA and just-in-time provisioning through an access request system. If an application is connected to the identity platform, access is granted right away; if not, a service request is created automatically so it is still tracked. In multi-cloud setups, identity governance (IGA), privileged access management (PAM) and single sign-on work together as one control plane.

The patterns that produce results are automated access reviews, PAM vaulting for admin accounts, and SSO integrations. In Kubernetes environments, teams add namespace isolation and automated policy validation. The principle underneath is the same everywhere: enforce least privilege and validate access before it is granted, not after.

## Compliance that is always on

The section with the most practical value is about turning compliance from an annual event into a continuous property. Instead of big review cycles and spreadsheets, checklists live in workflows, reminders are automated and reports are audit-ready at any moment. Anjan reports zero audit flags thanks to automated reviews, and hundreds of hours saved per business cycle on reporting. Identity intelligence adds access recommendations so reviewers can make a sensible keep-or-revoke decision instead of rubber-stamping a long list of entitlements.

Self-service is the developer half of the deal. Service catalogues, automated key management and simple web-based account creation mean developers do not wait weeks for access, and security keeps control because the paths are pre-approved.

## A healthcare example and the next three trends

His case study is a healthcare organisation managing access to patient data under compliance rules. With zero trust, automated provisioning and self-service, provisioning time dropped from days to under 12 hours, incidents went down and audit preparation got much faster. (The abstract's headline is 48-hour requests becoming 12-minute flows; the talk itself reports the under-12-hours figure.)

Looking ahead, Anjan sees three trends: converged IAM where IGA and PAM merge into one platform covering human and machine identities; automation-first governance where reviews, evidence collection and policy checks run continuously; and identity for AI, where non-human identities and intelligent agents need governing just like people. As agents get spun up daily, that last one is coming for every platform team soon.

## Who should watch

Platform and security engineers who own access requests and audits, and anyone about to give AI agents credentials. It is a strategy-level talk with concrete patterns rather than a product demo, though Anjan's background is in Saviynt and SailPoint.

## Related Conf42 talks

- [Ahmed Tariq on tool and identity boundaries for AI agents in cloud operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud), the non-human identity trend in practice.
- [Gianluca Mardente (Cisco) on centralised access management across clusters and tenants](https://www.conf42.com/DevOps_2024_Gianluca_Mardente_centralised_access_management), the Kubernetes side of the same control plane.
- [Mahesh Vankayala (Oracle) on identity federation and single sign-on in DevSecOps](https://www.conf42.com/DevSecOps_2024_Mahesh_Vankayala_identity_federation_security), for the SSO building block.

[Watch Anjan Kaleru's talk](https://www.conf42.com/Platform_Engineering_2025_Anjan_Kaleru_governance_identity_secure)

[Watch the talk on YouTube](https://youtu.be/QLn-ir6KO0k).

## Watch the talk

[Engineering Secure Cloud Platforms: Data-Driven Identity Governance for Modern Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Anjan_Kaleru_governance_identity_secure) at Conf42 Platform Engineering 2025.
