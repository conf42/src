# AI observability should tell you where the fire started

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-observability-turns-alerts-into-answers

In short: Ajay Averineni of IBM shows at Conf42 Platform Engineering 2025 how AI on metrics, logs and traces cuts alert noise and drives self-healing remediation.

It is 3 a.m., the dashboards say CPU and memory are fine, the logs run to millions of lines and the traces are missing half the context. At Conf42 Platform Engineering 2025, Ajay Averineni, Lead Application Developer at IBM, opens with that scene and spends the talk on how to make it rarer: use AI on observability data to find the one cause behind a thousand alerts, then let the platform fix the common failures itself.

His background is the useful part. Averineni has worked on enterprise hybrid cloud platforms at IBM and on telecom-scale services at AT&T, where millions of customers expect service around the clock and the alert volume grows with the microservice count.

## More data, less insight

The problem statement is one most SREs will nod at. Traditional observability works when you run tens of services. At thousands, metrics spike constantly, logs are mostly noise (he estimates 90% of them do not matter), traces are fragmented, and every service raises its own alarms, most of them false positives. He describes teams at AT&T drowning in alerts, to the point where observability became a distraction instead of a help.

## What AI changes on each signal

Averineni's breakdown is per signal, which keeps it concrete:

- **Metrics:** models look for subtle drift, seasonality and predicted spikes instead of crossing a fixed line.
- **Logs:** NLP models sift millions of lines for unusual error patterns.
- **Traces:** graph analysis connects transactions across services and points at causality rather than mere correlation.

The architecture behind it is a straightforward pipeline: streaming ingestion of API, network log and metric data; a processing layer built on tools like Kafka and Spark handling millions of events per second; models that detect anomalies, forecast demand and correlate incidents; and integration back into dashboards, incident management and CI/CD. The CI/CD hook is the clever bit. Running anomaly detection against new builds flagged regressions before deployment instead of after customers found them.

His telecom example shows why thresholds alone fall short: a signalling service might show a latency increase so small no human would notice it, but a model trained on historical outages can flag it as the precursor to a major incident.

## Root cause in minutes, not bridge calls

The section that will sell this to your manager is root cause analysis. The traditional version is hours on a bridge call with networking, database and application teams arguing over whose graph is red. Dependency mapping with AI highlights the one failing node that triggered the downstream alarms. Averineni says that at AT&T this cut RCA from hours to minutes, which he frames as the difference between a four-hour outage and a twenty-minute hiccup.

## Self-healing, with guardrails

Detection is half the loop. The self-healing cycle he describes is detect, diagnose, decide, remediate and learn, feeding results back into the model. The examples are deliberately unexotic: restart a failed container, scale APIs ahead of a peak event such as an Apple launch, isolate a misbehaving dependency before it takes the system down. He insists on guardrails, with thresholds, approvals and audit logs, because automation that can scale your fleet can also scale your mistakes.

The roadmap is incremental: assess observability gaps, pilot on one critical service, scale across services, then keep refining models from real incidents. Start where the pain is greatest; no big-bang transformation.

## Who should watch

SREs and platform engineers buried in alert noise, and anyone pitching AIOps internally who needs a sober framing with an RCA story attached. It is an architecture-level talk with no code, and the forward-looking part on reinforcement learning for operations is brief.

## Related Conf42 talks

- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz, Conf42 DevSecOps 2024
- [When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) by David McNerney and Daniel Raskin, Conf42 SRE 2026
- [Self Healing Systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) by Nick Hodges, Conf42 Chaos Engineering 2022

[Watch Ajay Averineni's talk](https://www.conf42.com/Platform_Engineering_2025_Ajay_Averineni_observability_healing_intelligent)

[Watch the talk on YouTube](https://youtu.be/s1Q9xbnEn1Q).

## Watch the talk

[Building Intelligent Platform Infrastructure: AI-Driven Observability and Self-Healing Systems at Scale](https://www.conf42.com/Platform_Engineering_2025_Ajay_Averineni_observability_healing_intelligent) at Conf42 Platform Engineering 2025.
