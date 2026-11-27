# Human-in-the-loop MLOps treats reviewer feedback as first-class data

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/human-in-the-loop-mlops-tiered-autonomy

In short: Tejasvi Nuthalapati of Amazon at Conf42 MLOps 2025 on tiered autonomy, observable models and feedback loops that put human judgment into retraining.

Most ML teams pick a side: automate everything and watch drift creep in, or put a human on every decision and watch throughput collapse. At Conf42 MLOps 2025, Tejasvi Nuthalapati, a software development engineer at Amazon, argued for a third design where the pipeline treats humans and models as first-class participants, and showed four patterns for building it.

This is a patterns talk, told through short case examples rather than code. The 40% in the title is his summary of the improvement in effective performance across organisations that adopted these patterns, and he was careful to say it came from architecture, not from a better algorithm.

## Both extremes fail the same way: trust evaporates

The full-automation pipeline looks clean until false positives pile up and nobody can say why the system decided what it did. The manual pipeline looks accurate but becomes slow and expensive, and reviewers burn out on repetitive cases. Tejasvi's opening story was a fintech fraud system drowning in false positives. Tuning the model barely helped. What worked was structured human review whose decisions were logged, versioned and tied into retraining cycles, and false positives fell by 40%.

## Autonomy is a dial, not a switch

The first pattern is tiered autonomy. Low-risk, high-confidence transactions get auto-approved. Medium-risk, uncertain ones go to an analyst who brings context. High-value cases go to full human review, with AI-generated insights attached so the reviewer starts with evidence. He listed several ways to implement the routing: a service mesh, CI/CD branches keyed on confidence thresholds, or Kubernetes operators that decide which requests need intervention. In one deployment this cut analyst workload by 60% because people stopped spending time on trivial cases.

## Models deserve the observability services get

Pattern two is the observable model. Nobody ships a service without logs, metrics and traces, yet models go to production as black boxes. Tejasvi's fix is structured decision logging, dashboards for confidence distributions, drift indicators and feature stability, and explanations layered for engineers, business stakeholders and end users. Imagine a recommender that quietly starts suggesting stale products: without confidence scores and drift signals you find out from the complaints.

## Corrections should reach retraining in days, not months

Pattern three is the one he cared about most. In many organisations a human spots a mistake, files a ticket, and the correction might reach a training set months later. He wants every correction logged against the model version that produced the error and fed automatically into retraining. In a content moderation system he observed, this loop lifted production F1 from 0.72 to 0.84 within three training cycles. His point that follows is the interesting one: as models improve, human input becomes more valuable, because what remains are the ambiguous, ethically loaded cases no model handles well.

## Oversight has to grow slower than the system

Pattern four is scalable oversight: stratify risk, sample intelligently, and design escalation paths. In a supply chain anomaly detection example, the team oversampled low-confidence cases for human review, caught 90% of novel anomalies and halved the human workload.

He closed with metrics for the whole human-plus-machine system: reduction in false positives, time to drift detection, how fast feedback reaches retraining, and operator confidence, because a system people trust is one they actually use.

## Who should watch

Anyone running fraud, moderation or anomaly detection with a review queue, and platform teams designing where humans plug into ML pipelines. Short on implementation detail, long on design patterns you can argue about with your team.

## Related Conf42 talks

- Vishal Shah (Visa) on [Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human).
- Vishnu Prasad (ERP Initiatives Group) on [Building Reliable Human-AI Warehouse Operations at Scale](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses).
- Morgan Willis (AWS) on why she doesn't trust AI agents, in [Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust).

[Watch Tejasvi Nuthalapati's talk](https://www.conf42.com/MLOps_2025_Tejasvi_Nuthalapati_human_loop_mlops)

[Watch the talk on YouTube](https://youtu.be/p4CVO3dLOPw).

## Watch the talk

[Human-in-the-Loop MLOps: Production Patterns That Boost Model Performance 40% While Maintaining Human Control](https://www.conf42.com/MLOps_2025_Tejasvi_Nuthalapati_human_loop_mlops) at Conf42 MLOps 2025.
