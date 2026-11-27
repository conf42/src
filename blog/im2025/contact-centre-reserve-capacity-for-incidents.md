# An incident-ready contact centre keeps humans in reserve for the outage

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/contact-centre-reserve-capacity-for-incidents

In short: Sujit Kumar (Copart) at Conf42 Incident Management 2025 on designing AI-assisted contact centres that stay calm when the CRM is down and call volume spikes.

When the CRM goes down, your agents cannot see order history, customers repeat themselves, hold times grow and somebody posts about it. At Conf42 Incident Management 2025, Sujit Kumar, Vice President of Technology at Copart, described how to design customer support so it absorbs exactly that kind of incident, and the core idea is capacity: let automation handle the routine so humans are free when things get emotional.

Sujit's position is that incidents are inevitable, but how the support operation responds decides whether customers stay. The talk is an architecture and strategy overview, not a product demo.

## Resilience by design, not by chance

The foundation is cloud-native support architecture. Microservices isolate faults so one failing component does not take the whole platform down. Event-driven processing reacts to sudden change in real time. Auto-scaling adjusts resources when traffic spikes. Underneath sit the usual guards: circuit breakers to stop degraded components cascading, intelligent load distribution across available resources, and redundant systems so there is always an alternative path.

None of that is unique to contact centres, which is the point. A support platform is a production system with an unusually loud failure mode.

## Route by intent, and by mood

On top of the foundation, AI does triage. Intent detection with natural language processing and historical data works out what the caller wants from the first interaction; during an incident, misrouted calls only add friction. Sujit adds two refinements: detecting multiple intents in one conversation, and reading emotional state. His example: a customer who says they cannot log in and are really frustrated has both a login issue and an urgency signal, and the system should treat it accordingly.

Risk-based escalation scores cases using patterns, account history and behaviour to flag potential fraud or security concerns, so high-risk cases jump the queue and routine ones follow the standard path. AI-driven decision trees, unlike static flowcharts, adjust in real time; if one system is degraded, they reroute customers to an alternative resolution.

## Never make the customer start over

The handoff section is the one most support teams will recognise as their weak spot. Conversational AI handles routine requests (account updates, password resets, basic troubleshooting), which creates reserve capacity for agents. When a case does need a human, the context travels with it: interaction history, intent and emotional state, delivered as a briefing so the agent can pick up without asking the customer to repeat everything. During an outage, when patience is already thin, that continuity matters most.

Agents also get real-time assistance: suggested responses, compliance guidance and knowledge articles, with speech analytics flagging potential compliance violations before they become costly.

## The ticket queue is a monitoring signal

The idea SREs may steal: support data as early warning. Predictive models look at historical patterns, system metrics and external factors, and an unusual rise in password-reset tickets can be the first sign of a broader outage. Spot it early and you can communicate proactively, sometimes before the incident is formally an incident. Multimodal support helps resolution speed too, with customers sharing a photo of an error or a video of a malfunction.

Sujit ties it together as a four-phase roadmap: a cloud-native foundation, AI for intent and routing, predictive analytics and multimodal processing, then resilience optimisation with tuned load balancing, failover and incident procedures. He presents it as a roadmap, not a one-off project.

## Who should watch

Engineering leaders who own customer support platforms, and SREs who have never looked at their company's ticket volume as telemetry. If you want hard numbers from Copart's own rollout, the talk stays at the level of patterns.

## Related Conf42 talks

- [Dmitry Kindrya on whether LLMs save customer support or ring its death knell](https://www.conf42.com/Large_Language_Models_LLMs_2024_Dmitry_Kindrya_customer_support_revolutionizing), the sceptic's view on automating support.
- [How To Use Voice AI For Incident Reporting, Monitoring and Alerts](https://www.conf42.com/Site_Reliability_Engineering_2021_Arthur_Grishkevich_voice_AI_Incident_reporting_monitoring_alerts) by Arthur Grishkevich, voice interfaces pointed at the incident itself.

[Watch Sujit Kumar's talk](https://www.conf42.com/Incident_Management_2025_Sujit_Kumar_contactcenters_automation_scale)

[Watch the talk on YouTube](https://youtu.be/69XSds6sN0s).

## Watch the talk

[Incident-Ready Contact Centers: AI, Automation, and Resilience at Scale](https://www.conf42.com/Incident_Management_2025_Sujit_Kumar_contactcenters_automation_scale) at Conf42 Incident Management 2025.
