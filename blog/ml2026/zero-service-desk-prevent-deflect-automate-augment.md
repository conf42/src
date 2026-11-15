# Zero Service Desk: prevent, deflect, automate, then augment

Conf42 Blog, 2026-02-04, updated 2026-11-09. https://www.conf42.com/blog/ml2026/zero-service-desk-prevent-deflect-automate-augment

In short: Anu Arora of ServiceNow at Conf42 Machine Learning 2026 on how ServiceNow IT used ML and its own platform to keep support staff flat while headcount grew.

Every growing company eventually does the same maths: more employees, more tickets, more support staff. At Conf42 Machine Learning 2026, Anu Arora, Director of Enterprise Systems at ServiceNow, explained how her team broke that line by aiming for a "Zero Service Desk": level-one support delivered by ML, workflows and self-service rather than human agents, while the support team stayed flat for years.

Honest scope: this is ServiceNow running on ServiceNow. Anu's team acts as customer zero for the company's own products, so the platform in the middle of every diagram is theirs. The framework travels anyway.

## Zero does not mean nobody

Anu was careful about the name. Zero Service Desk does not mean there is no service desk. It means users get help in seconds or minutes through self-service instead of waiting hours for an agent. ServiceNow's own bar is 90% self-service; she expects other companies to set a different number for their size and goals.

The people did not vanish either. Freed from level-one tickets, they moved to level-two work, other teams, or premium support for the cases that will never automate.

## Three ML jobs underneath

She named three machine-learning capabilities the approach depends on:

- **Classification**: what kind of issue is this, and has it been solved before? If an HR leave-policy question has a known answer, apply it.
- **Intent detection**: from what a user types into the virtual agent, work out whether they need information, access or a fix.
- **Anomaly detection**: the predictive piece, such as a laptop whose CPU spikes at the same time every day, flagged to the user before it becomes a ticket.

## Four pillars, in order of preference

The operating model is four pillars, and the order matters.

**Prevent** with observability across laptops, network, servers and applications: notice the outdated Zoom client and schedule the upgrade before anything breaks.

**Deflect** what you cannot prevent. A question about parental leave policy in California does not need a ticket and an agent who pastes a knowledge article; search should surface the article. A "my laptop is slow" request can trigger a health check that suggests a restart after a month of uptime.

**Automate** requests that cannot be deflected. A new hire needing access gets intent detection, a role check against their profile, approval if required, and provisioning, with no human agent in the loop.

**Augment** whatever is left. When a ticket still gets created, AI helps the agent resolve it. Anu said work that used to take 30 minutes now takes five to ten.

## The human change came first

The step she stressed most was not technical. Help used to arrive through phone calls, chats and emails, and you cannot automate a funnel with five entrances. Consolidating everyone onto one standard path, the virtual agent, was a behaviour change for employees as much as an architecture change, and it came before the rest worked.

## Who should watch

IT and enterprise-systems leaders sizing a self-service programme, and SREs who want the prevent-first framing applied to internal support. Expect a strategy talk with examples, not model details.

## Related Conf42 talks

- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz, the same deflect-before-humans idea for alerts.
- [Mastering Automation and Monitoring for Optimized IT Operations](https://www.conf42.com/Golang_2025_Jugnu_Misal_automation_monitoring_operations) by Jugnu Misal.
- [How AI is redefining SRE and Customer Experience](https://www.conf42.com/DevOps_2026_Spiros_Economakis_sre_experience_ai) by Spiros Economakis.

[Watch Anu Arora's talk](https://www.conf42.com/Machine_Learning_2026_Anu_Arora_personalization_recommendation_platforms) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/Y-HCcRIr8Vg).

## Watch the talk

[Zero Service Desk: Applying Machine Learning for Autonomous IT Support](https://www.conf42.com/Machine_Learning_2026_Anu_Arora_personalization_recommendation_platforms) at Conf42 Machine Learning 2026.
