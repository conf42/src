# Correlate first, automate second, and let Copilot write the summary

Conf42 Blog, 2026-01-14, updated 2026-11-09. https://www.conf42.com/blog/devops2026/defender-xdr-alert-storms-to-mttr

In short: Nikolay Milyaev of Microsoft at Conf42 DevOps 2026 on taming SOC alert storms with Defender XDR correlation, safe playbooks, Security Copilot and metrics.

A SOC drowning in alerts usually has plenty of tools and too little attention to spend on them. That is how Nikolay Milyaev, a senior consultant at Microsoft, framed his Conf42 DevOps 2026 talk, and his answer is a four-stage pipeline built only from Microsoft-native pieces: correlate alerts into incidents, automate the safe first-mile steps, use Security Copilot to compress analysis, and measure MTTR so the programme keeps its funding. He notes up front that the views are his own, not Microsoft's.

This is a Microsoft-stack talk through and through (Sentinel, Defender XDR, Azure Monitor, Logic Apps, Security Copilot), but the four-stage shape applies to any SOC or on-call rotation.

## Why the storm inflates MTTR

Nikolay quotes a commonly cited survey figure of 3,832 alerts a day on average, with about 62% going unattended. Once that happens, the system feeds itself: responders burn out, start ignoring alerts, and the organisation slows down. MTTR is the sum of detection, triage, analysis, coordination and remediation, so if the first three are noisy and manual, everything after them waits.

He makes the SRE parallel explicit. One root cause produces dozens of symptom alerts on CPU, latency, error rates and gateway health; one attack shows up separately in email, identity and endpoint. Same beast, different clothes.

## Correlation is the front door

If the system shows 40 alerts that are really one event, the team does 40 micro-investigations and opens 40 tickets. Correlation trades volume for fidelity, so people work an incident with shared entities and a timeline. On the Microsoft stack that happens in three places:

- **Microsoft Sentinel**, with Fusion, an ML correlation engine for multi-stage attacks, plus simple alert grouping at the analytics rule level, which can turn a hundred failed logons into one incident.
- **Defender XDR**, which decides whether a new alert joins an existing incident, starts a new one, or merges incidents into one campaign across endpoint, email, identity and cloud apps.
- **Azure Monitor smart groups** for SRE, which cluster related alerts by similarity and co-occurrence, alongside dynamic thresholds.

Sentinel moving into the Defender portal gives one queue for both, which cuts tool switching.

## First-mile automation, safe by design

Once an incident exists, a Logic Apps playbook should do the checklist you wish ran itself: enrich indicators with threat intelligence, attach user and device context, flag entities seen recently, suppress obvious duplicates while keeping the evidence trail, set severity and owner, open the ITSM ticket and notify in Teams. His guardrails are to start read-only, log every action, and make any containment step reversible or gated on approval.

## Copilot as analysis accelerator, not autopilot

The pattern he recommends chains the two: a playbook triggers on a new Sentinel incident, loops over entities such as IPs, accounts, hosts and processes for deterministic enrichment (reputation lookups, device compliance from Intune), then calls Security Copilot through its Logic Apps connector for an incident overview, entity analysis and mitigation steps, and posts the result back as a comment. The analyst starts from a narrative instead of raw logs.

Interactively, Copilot answers questions, drafts executive reports and turns plain language into KQL, which helps less experienced responders most. The governance point is clear: Copilot advises; it does not change your environment.

## The scorecard keeps the programme alive

Without numbers the work stalls. Start with metrics that are easy to compute and hard to argue with, such as MTTA, MTTR, incident count by severity and time saved by automation; build them from Sentinel incident data exported through its REST API into a custom Log Analytics table and a workbook. Read the scorecard as a control loop: the categories that keep taking hours show you which playbook to build next.

The walk-through scenario ties it together. A phishing email, a suspicious process on the same user's device and an identity anomaly become one incident instead of three, playbooks enrich and route it, and Copilot attaches a summary. Together that collapses the first 15 minutes, which is often where MTTR is decided.

## Who should watch

SOC leads and security engineers on Microsoft Defender and Sentinel, and SREs who want a template for the same correlate-automate-measure loop. Roll-out advice is incremental: one painful incident category, one enrichment playbook, one Copilot summary, measure, repeat.

## Related Conf42 talks

- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) by Mandi Walls attacks the same storm from the reliability side.
- [AI Agents for DevSecOps: Automating Secure Infrastructure, Delivery, and Incident Response](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) by Deepanshu Kukreja goes further on automated response.
- [Incident Response, for Developers](https://www.conf42.com/Incident_Management_2023_Tanya_Janca_incident_response_developers) by Tanya Janca covers the human process behind the tooling.

[Watch Nikolay Milyaev's talk](https://www.conf42.com/DevOps_2026_Nikolay_Milyaev_xdr_security_analytics)

[Watch the talk on YouTube](https://youtu.be/NtpVnWCAVVk).

## Watch the talk

[Defender XDR in the Real World: From Alert Fatigue to Measurable Risk Reduction](https://www.conf42.com/DevOps_2026_Nikolay_Milyaev_xdr_security_analytics) at Conf42 DevOps 2026.
