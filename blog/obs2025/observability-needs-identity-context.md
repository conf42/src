# Your dashboards show what broke, not who broke it

Conf42 Blog, 2025-05-06, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observability-needs-identity-context

In short: Cynthia Akiotu of Tesco Bank argues at Conf42 Observability 2025 that identity belongs inside observability, from privilege misuse to ghost access.

Most observability stacks can tell you the API spiked at 14:02. Very few can tell you which identity was holding elevated permissions at 14:01. At Conf42 Observability 2025, Cynthia Akiotu, Cyber Risk Analyst at Tesco Bank, made the case that this gap is where modern breaches live, and that identity has to be a first-class signal next to logs, metrics and traces. Her opening line sets the tone: observability without identity is like a map without landmarks.

It's a security talk aimed at observability people, which is exactly the audience that needs it.

## Attackers log in, they don't break in

Akiotu's core claim is that identity is now the perimeter. The firewall-and-perimeter era assumed attackers had to force their way through; today they sign in with valid credentials and move laterally without tripping anything. And "identity" no longer means a person: managed identities, service principals, bots acting on behalf of users and, increasingly, AI agents all hold credentials.

She lists the usual identity-shaped incidents: insider threats (employees, vendors, third parties, malicious or careless), unauthorised access, audit violations and privilege misuse, the last one being an admin quietly raising their own rights. The Tesla insider leak of 2023, where former employees handed staff data to the media, is her example of people with legitimate access doing illegitimate things.

## Four quadrants of not knowing

The most memorable part of the talk is a quadrant that crosses identity visibility with risk awareness. The interesting cells are the uncomfortable ones:

- **Unsanctioned SaaS**: an employee finds a free tool online and signs in with office credentials, unseen.
- **Ghost access** (the unknown known): unused roles, misconfigurations and policy gaps. Akiotu describes it as a dashboard on fire without knowing who lit the match, and points to the third-party route into Marks & Spencer's ransomware incident.
- **Invisible identities** (the unknown unknown): the CISO's worst case, like the abandoned legacy system behind the Legal Aid Agency breach, or the NHS trusts exposed through a third-party mobile device management tool.

She also names the reasons teams don't fix this: hybrid estates where on-prem Active Directory isn't synced with Entra ID, tools that don't talk to each other, and licensing costs that keep growing until a breach makes the budget appear.

## Correlate first, buy tools second

The practical section is a short checklist. Correlate identity with system events, so your SIEM (she mentions Microsoft Sentinel) and identity platform (Entra ID) actually share data. Audit permissions in real time using signals like location and device compliance, instead of static role-based rules checked once a quarter. Detect insider threats and shadow AI, add data loss prevention, align with Zero Trust (assume breach, verify every identity), and enforce least privilege under whatever regime applies to you: GDPR, HIPAA, NIST and friends.

Her sharpest point is that the tooling list matters less than whether the tools are wired together. Microsoft Defender for Cloud Apps, Sentinel and Purview get a mention, but the warning is about silos, not products. And because some breaches are unavoidable, she closes on incident response: mature security is also measured by how fast you contain and recover.

## Who should watch

SREs and platform engineers who own the logging pipeline but have never been asked to join identity data to it, and security analysts who want vocabulary to pitch that work to them. It's conceptual rather than hands-on, so don't expect queries or a demo. Start with her opening question, which is when your organisation last ran an access review, and whether anyone would admit the answer.

## Related Conf42 talks

- Naveen Kumar Birru on [Beyond Perimeters: Implementing Zero Trust at Enterprise Scale](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust).
- Karan Bansal on [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks), for when the identity is an agent.
- Mahesh Vankayala on [identity federation and single sign-on in DevSecOps](https://www.conf42.com/DevSecOps_2024_Mahesh_Vankayala_identity_federation_security).

[Watch Cynthia Akiotu's talk](https://www.conf42.com/Observability_2025_Cynthia_Akiotu_identity_access_breach)

[Watch the talk on YouTube](https://youtu.be/_CbvYGGESjM).

## Watch the talk

[Access is the New Breach: Why Observability Must Start with Identity](https://www.conf42.com/Observability_2025_Cynthia_Akiotu_identity_access_breach) at Conf42 Observability 2025.
