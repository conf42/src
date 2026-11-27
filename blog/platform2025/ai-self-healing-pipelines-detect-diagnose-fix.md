# Self-healing data pipelines detect, diagnose and fix with AI

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-self-healing-pipelines-detect-diagnose-fix

In short: Lakshmi Srinivasarao Kothamasu (Fidelity Investments) at Conf42 Platform Engineering 2025 on AI anomaly detection, LLM root cause and automated pipeline repair.

With enough interconnected jobs, at least one pipeline failure a day is close to guaranteed. At Conf42 Platform Engineering 2025, Lakshmi Srinivasarao Kothamasu, Principal Data Engineer at Fidelity Investments, made the case for pipelines that detect their own anomalies, diagnose the root cause with language models and apply the fix, turning data engineers from firefighters into supervisors of an autonomous system.

## Firefighting is the default, and it's expensive

Lakshmi draws on more than 20 years of building enterprise data lakes and analytics platforms, on-premises and in the cloud. His starting point: even with modern orchestrators and cloud-native platforms, pipeline failures remain a constant production pain. A small schema mismatch, a network blip or a configuration change breaks downstream workflows, and the cost lands as lost revenue, compliance violations and decisions made on stale data. He says around 60% of platform engineers' operational bandwidth goes on troubleshooting and recovery. Traditional monitoring tells you something failed; the remediation is still manual, and the logs you need are scattered across systems for an engineer to stitch together.

## Four capabilities, one loop

The self-healing pipeline he describes runs a detect, analyse, fix, learn loop:

- **Anomaly detection.** Transformer-based models watch metrics, logs and data quality checks for abnormal behaviour.
- **Root cause analysis.** Language models such as GPT-4 read logs, trace dependency graphs and propose the most probable cause.
- **Autonomous remediation.** Reinforcement learning agents or rule-based automation take the corrective action.
- **Continuous learning** from past failures, successful repairs and human feedback.

Architecturally, he offers three ways to deploy it: a centralised AI layer, decentralised agents embedded in pipelines, or a hybrid.

## Three domains, three flavours of failure

The case studies show how the same loop adapts. A global retailer ingesting around two terabytes of data kept hitting failures from schema changes and traffic spikes, delaying product availability online. With AI detection identifying schema mismatches and automated workflow recovery, Lakshmi reports recovery dropping from about two hours to five minutes.

In healthcare, an LLM parses logs to find authentication failures and misconfigured policies, the system isolates failing nodes and reroutes data, and higher-risk actions go to engineers for review. Recovery time fell by 70%, and because every AI-driven action was logged, compliance audits held up.

In a fintech running real-time fraud detection, where even short outages are dangerous, reinforcement learning agents shift compute to fraud models when volume spikes and fail over to backup pipelines without human intervention.

## Guardrails are part of the design

Lakshmi is clear that autonomy needs supervision. Every remediation is logged with an explanation, industry regulations shape what the system may do on its own, and engineers keep a supervisory role over high-impact fixes. Building trust takes transparency, continuous monitoring and cultural change, not just a better model.

## Who should watch

Data platform engineers who own on-call for pipelines and want a structure for automating the routine fixes without losing auditability. It's a short talk that stays at the architecture and case-study level; the domain comparisons are the most useful part.

## Related Conf42 talks

- [AI-Driven Self-Healing Infrastructure: The Next Evolution of SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Vijaybhasker_Pagidoju_selfhealing_infrastructure) by Vijaybhasker Pagidoju, the same idea one layer down.
- [Building Self-Healing Real-Time Streaming Pipelines with Go and AI](https://www.conf42.com/Golang_2026_Yogesh_Pugazhendhi_Duraisamy_Rajamani_building_self_healing) by Yogesh Pugazhendhi Duraisamy Rajamani (Ford Motor Company), with an RL control plane in Go.
- [Resilient Cross-Cloud Analytics Pipelines with Azure Databricks: A 10TB+ Scale Reliability Engineering Case Study](https://www.conf42.com/Incident_Management_2025_Sruthi_Erra_Hareram_databricks_analytics_reliability) by Sruthi Erra Hareram.

[Watch Lakshmi Srinivasarao Kothamasu's talk](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Srinivasarao_Kothamasu_firefighting_manual_pipelines)

[Watch the talk on YouTube](https://youtu.be/mjPreuYaUqU).

## Watch the talk

[Beyond Manual Firefighting: Building Self-Healing Data Pipelines with AI for Platform Engineering](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Srinivasarao_Kothamasu_firefighting_manual_pipelines) at Conf42 Platform Engineering 2025.
