# In banking, make the compliant path the fastest path to production

Conf42 Blog, 2025-09-25, updated 2026-11-09. https://www.conf42.com/blog/im2025/compliance-built-into-the-paved-path

In short: Nirup Baer (Wells Fargo) at Conf42 Incident Management 2025 on building compliance into cloud platforms so incidents are rarer and leave their own audit trail.

Think of compliance as seat belts in a performance car: designed in from the start, not strapped on before the inspection. That is the image Nirup Baer, Program Manager at Wells Fargo, built his talk around at Conf42 Incident Management 2025, and the practical claim behind it is that when the safe path is also the fast path, teams stop negotiating with controls and incidents leave their own evidence behind.

## An incident in a bank is three incidents

Nirup starts with the stakes. Financial services move enormous sums every day, customers touch real balances, and when a system pauses the cost shows up in money and reputation at once. So an incident is technical, business and regulatory simultaneously, and the response has to respect all three. That is why, in his framing, incident management sits where reliability, regulation and brand meet.

His answer is modernisation as a way to set better defaults: repeatable patterns for network, identity, storage and compute; rules in the build and release steps so risky changes never reach customers; and unchangeable logs so the system can tell its own story afterwards.

He gives a quick field example. A fragile service was moved into a landing zone with strong guardrails, with the same team and the same code. The next incident felt like a drill they had already practised: they knew what changed, when, and the safe way back.

## Blast radius is an architecture decision

The architecture section stays at the level of principles, which suits a mixed audience. Manage policy and visibility centrally while keeping sensitive customer data in the region where it belongs. Design for small blast radius: clear service boundaries, sensible timeouts and retries, and fast ways to switch off risky features. Practise failovers until they are boring. Run the most critical systems in more than one place and keep a warm backup for the rest.

His highway analogy works: each service has its own lane with dividers and a shoulder, so a blown tyre in one lane does not close the road.

## Three stories where the audit trail came for free

The case studies are where the idea earns its keep. In regulatory reporting, overnight batches became real-time streams, so delays showed up in minutes instead of the next day, and every step wrote an unchangeable record. Reports that took days ran in minutes, and audit prep that took weeks took days.

In fraud detection, the turning point was managing the whole model lifecycle rather than just the score. Changes needed approval, a misbehaving version could be rolled back with one decision, and the team could explain what changed and why. False alarms and losses both dropped.

In trading, surveillance moved from after the fact to real time, with limits enforced as orders flowed and check records travelling alongside the trades. When the market surged, the system followed a safe playbook rather than calling a meeting.

## Policy in the pipeline, not in the quarterly review

The repeatable part is infrastructure as code plus rules in the delivery pipeline. If a setting would expose data or open a risky path, it does not pass, and the system says which rule failed and shows the approved pattern. Long review meetings become fast feedback while the work is still in progress, and the platform keeps a timestamped record of what fired, who changed what and how it was fixed.

His incident routine follows from that: confirm the signal, start a clean log immediately, pause risky change paths, use pre-approved moves (switch off a feature, limit traffic, fail over), communicate in plain language, let the system collect the facts, and do not call it fixed until the service holds steady for a meaningful window. Then promote the fix into the shared template so the next team never meets the same problem.

## Who should watch

Platform and SRE leads in banks, insurers and trading firms, and anyone whose change process is a quarterly checklist. The closing advice is small enough to start on next sprint: pick one painful control, automate it end to end inside a golden path, and measure recovery time and audit hours saved.

## Related Conf42 talks

- [Compliance-Aware Platform Engineering: Scaling Hybrid Cloud Automation in Regulated Financial Environments](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) by Satish Manchana, the platform-engineering version of the same argument.
- [Go-Powered Banking: Modernizing iSeries Systems for the FinTech Era](https://www.conf42.com/Golang_2025_Srinivas_Allam_banking_modernization_fintech) by Srinivas Allam, on what modernisation looks like at the legacy end.
- [Kubernetes-Native AI Microservices: Scaling Compliant ML Workloads in Regulated Industries](https://www.conf42.com/Kube_Native_2025_Manisha_Ponugoti_microservices_regulated_scalable) by Manisha Ponugoti, for the model-lifecycle angle.

[Watch Nirup Baer's talk](https://www.conf42.com/Incident_Management_2025_Nirup_Baer_finance_modernization_resilience)

[Watch the talk on YouTube](https://youtu.be/oMwkZBbiL7E).

## Watch the talk

[Cloud Modernization Meets Compliance: Resilience and Speed in Financial Services](https://www.conf42.com/Incident_Management_2025_Nirup_Baer_finance_modernization_resilience) at Conf42 Incident Management 2025.
