# Self-healing AWS is a four-stage climb, not a switch

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/self-healing-aws-infrastructure-maturity-model

In short: Sreeja Reddy Challa at Conf42 Platform Engineering 2025 on building self-healing AWS infrastructure with DevOps Guru, GuardDuty, Lambda and Step Functions.

Nobody flips a flag and wakes up with autonomous operations. At Conf42 Platform Engineering 2025, Sreeja Reddy Challa, an AWS cloud engineer of seven years speaking as an independent researcher, laid out how platform teams move from reactive firefighting to self-healing AWS infrastructure, and why the human and cultural steps matter as much as the Lambda functions.

Her framing is clear from the start: AI does not replace engineers, it amplifies their judgement by learning from incidents, predicting failures and running the remediations people used to type by hand at 2am.

## Why manual ops stops scaling

The pressure comes from several directions at once: alert and telemetry volume beyond what humans can read, systems that move faster than human reaction time, evolving security threats, compliance overhead, and too few experienced platform engineers to go around. Teams that keep relying on manual processes, she argues, end up paying in operational cost, downtime and agility.

## The AWS building blocks

The architecture is pleasingly concrete. Detection comes from two ML-backed services: Amazon DevOps Guru, which builds baselines from metrics, logs and traces and flags anomalous behaviour, and Amazon GuardDuty, which analyses DNS logs, VPC Flow Logs and CloudTrail events for suspicious activity. AWS Config watches resource state against policy and, together with Systems Manager, runs playbooks that correct configuration drift.

Response is event-driven. Findings land in CloudWatch Events, which she calls the central nervous system, routing them to handlers. Lambda functions are the execution engine for individual remediations; Step Functions orchestrate the multi-step ones, with error handling, retries and rollback. Remediation outcomes are fed back so the system learns which fixes work. Severity matters too: critical issues trigger immediate action and escalation, while lower-priority ones queue for automated fixing later.

## Four stages of maturity

The heart of the talk is a maturity model you can hold your own platform against:

1. **Reactive automation.** Scripted remediation for well-understood problems: infrastructure as code, standard dashboards, automated runbooks.
2. **Predictive monitoring.** ML spots behaviour patterns before users feel them, with tools like DevOps Guru and smarter alerting.
3. **Intelligent remediation.** The system diagnoses and fixes most routine problems itself through event-driven, orchestrated workflows that learn from outcomes.
4. **Autonomous operations.** Most operational work runs with minimal oversight; humans handle strategy and the genuinely strange.

Most teams reading this are somewhere between one and two, and that is fine. Her implementation advice is to start in low-risk areas and take one risk at a time.

## Trust is the real migration

Sreeja spends real time on the organisational side, which is the part most self-healing pitches skip. Engineers' roles shift from troubleshooting to designing the systems that troubleshoot. Teams need skills in ML operations, event-driven design and serverless. Trust in automation comes from gradual rollout, monitoring and clear escalation rules, including when a human should step in and when they should not. She also suggests new performance metrics, such as autonomous remediation success rates, and a governance framework for automated decisions. Her timeline estimate is multi-year.

Looking ahead, she points at generative AI drafting remediations for novel failures, explainable AI so teams can see why an action fired, and digital twins of infrastructure for rehearsing cascading failures without touching production.

## Who should watch

AWS platform and SRE teams with a pile of runbooks and an appetite to automate them, and managers who need a maturity model to plan the next two years. It is an architecture and strategy talk with no live demo, so bring your own console.

## Related Conf42 talks

- [Madhu Chenna on a self-healing ops platform with telemetry, RAG and confidence-gated agents](https://www.conf42.com/Platform_Engineering_2026_Madhu_Chenna_healing_rag_telemetry) at Conf42 Platform Engineering 2026.
- [Amit Anand on cloud infrastructure for agentic AI and self-healing systems](https://www.conf42.com/MLOps_2026_Amit_Anand_agentic_cloud_healing) at Conf42 MLOps 2026.
- [Hareesh Iyer on practical chaos engineering for fault-tolerant systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Hareesh_Iyer_chaos_engineering_practical) at Conf42 SRE 2024.

[Watch Sreeja Reddy Challa's talk](https://www.conf42.com/Platform_Engineering_2025_Sreeja_Reddy_Challa_aws_healing_self), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/Dzk7inbmFdc).

## Watch the talk

[Platform Engineering with AI-Driven Self-Healing AWS Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Sreeja_Reddy_Challa_aws_healing_self) at Conf42 Platform Engineering 2025.
