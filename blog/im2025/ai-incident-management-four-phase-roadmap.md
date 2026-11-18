# A four-phase roadmap from threshold alerts to AI remediation

Conf42 Blog, 2025-09-06, updated 2026-11-09. https://www.conf42.com/blog/im2025/ai-incident-management-four-phase-roadmap

In short: Mallikarjun Ramasani (Barclays) at Conf42 Incident Management 2025 maps the AI/ML incident stack, from anomaly detection to RL-driven auto-remediation.

Threshold alerts tell you the CPU crossed 90%. They don't tell you the database will saturate in twenty minutes. At Conf42 Incident Management 2025, Mallikarjun Ramasani, Software Engineer at Barclays, gave an overview of how AI and machine learning move incident management from reacting to outages toward predicting and auto-remediating them, and offered a phased plan for getting there without betting the platform on day one.

This is a survey talk: broad, well-structured and short, aimed at teams deciding where to start rather than teams already running models in production.

## Reactive, responsive, predictive

Ramasani frames the history in three stages. First came threshold monitoring, where an alarm fires on CPU or memory and a human digs through logs. Then came the responsive era of correlation engines, automated runbooks and structured postmortems. The leap he cares about is the third: models that forecast failures before users feel them. He name-checks LSTM networks for time-series forecasting, causal inference to pin down dependencies, and reinforcement learning agents to handle remediation.

The motivation is the familiar one. Downtime in distributed systems cascades across dozens of services, human error and alert fatigue still cause a large share of incidents, and manual triage doesn't scale with microservice counts.

## Four capabilities, one pipeline

The core of the talk is four capabilities:

- **Predictive alerting**, with models trained on baselines that catch early warning signals before static thresholds trip.
- **Automated root cause analysis**, using graph-based models of service dependencies to isolate where a fault started.
- **Autonomous remediation**, where RL agents restart services, reroute traffic or scale clusters.
- **Intelligent escalation**, routing incidents to the right engineer by expertise, context and availability.

He then sketches the architecture that carries them: telemetry collected with OpenTelemetry or native agents, a unified observability layer such as Elastic or Datadog, an AI processing layer on Spark ML or TensorFlow Serving, orchestration into ServiceNow or PagerDuty to trigger runbooks, and a feedback loop that retrains continuously. Each major cloud has its own version of the loop: SageMaker with CloudWatch and Lambda on AWS, Azure ML with Log Analytics and Logic Apps, and Vertex AI with Cloud Operations and Cloud Functions.

## Garbage telemetry in, false positives out

The section worth slowing down for is about training data. Metrics give latency, throughput and saturation; logs can be parsed with NLP to pull out error codes and correlation IDs; past postmortems become labelled training sets for root cause models. His warning is blunt: a model trained on noisy, inconsistent telemetry produces false positives, and false positives are how you lose the on-call team's trust. Clean and normalise the pipeline before you train anything.

His one concrete example comes from financial services: a predictive model spotted database saturation about twenty minutes ahead of failure and scaled the cluster automatically, avoiding the outage.

## Phase it, and keep humans in charge

The roadmap runs in four phases: data readiness (centralised telemetry, normalised logs, baseline anomaly detection), augmentation (AI alert correlation and runbooks), proactive intelligence (graph-based RCA and RL remediation), then optimisation (predictive capacity planning, expanding across regions and teams). Start with one service, prove value, then scale. Explainability matters because engineers won't adopt recommendations they can't follow, and the end state he describes has engineers moving from firefighting to design and governance rather than disappearing.

## Who should watch

Engineering managers and SREs building a business case for AIOps, or looking for a sequence that doesn't start with "train an RL agent". If you already run anomaly detection in production, the later phases are where the value is.

## Related Conf42 talks

- [AIOps in AWS: Choosing the Best Approach for Predictive Maintenance](https://www.conf42.com/Incident_Management_2024_Indika_Wimalasuriya_17_aiops_aws_maintenance) by Indika Wimalasuriya gets specific about the AWS options.
- [How to use generative AI to finally fix out-dated runbooks](https://www.conf42.com/Incident_Management_2023_Anurag_Gupta_generative_ai_fix_runbooks) by Anurag Gupta tackles the runbook half of auto-remediation.
- [Chaos Experiments under the lens of AIOps](https://www.conf42.com/Chaos_Engineering_2022_Michele_Dodic_chaos_experiments_under_the_lens_of_aiops) by Michele Dodic shows how to test whether the models actually catch failures.

[Watch Mallikarjun Ramasani's talk](https://www.conf42.com/Incident_Management_2025_Mallikarjun_Ramasani_intelligence_cloud_future)

[Watch the talk on YouTube](https://youtu.be/10wvHoa_32s).

## Watch the talk

[Intelligent Incident Management: AI, ML, and the Future of Resilient Cloud Operations](https://www.conf42.com/Incident_Management_2025_Mallikarjun_Ramasani_intelligence_cloud_future) at Conf42 Incident Management 2025.
