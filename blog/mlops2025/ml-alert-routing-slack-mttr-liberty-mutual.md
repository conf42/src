# ML that ranks errors by business impact cut MTTR at Liberty Mutual

Conf42 Blog, 2025-09-02, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/ml-alert-routing-slack-mttr-liberty-mutual

In short: Sreelatha Pasuparthi (Liberty Mutual) at Conf42 MLOps 2025 on ML-driven alert triage and Slack routing across 17 enterprise systems.

When customers find two thirds of your critical issues before you do, the alerting is not working. At Conf42 MLOps 2025, Sreelatha Pasuparthi, Principal Software Engineer at Liberty Mutual Insurance, described how her team built an ML system that classifies errors by business impact and routes them to the right person over Slack, Teams or email, and she reports mean time to resolution falling from 162 to 18.6 minutes across 17 enterprise systems.

## The cost of noise at scale

The starting numbers are the kind that make an on-call engineer wince. Seventeen production systems supporting about 230,000 daily active users and 3.7 million daily transactions produced over 12,000 error events a day. Average detection took 162 minutes, 68.2% of critical issues were first discovered by customers, and SLA compliance sat at 62.3%. Engineers spent 23% of their time triaging alerts instead of building.

Alert fatigue is usually described as a morale problem. Here it is a measurable tax on delivery.

## Capture everything, cheaply

The first layer is middleware that captures exceptions across all systems. Sreelatha cites a 99.7% capture rate with only 3.2 milliseconds of overhead per transaction, distributed tracing to preserve context, an event-driven architecture on a Kafka backbone, and containerised ML inference endpoints. If the capture layer is expensive, someone turns it off; keeping it cheap is what makes everything after it possible.

## An ensemble that asks "does this matter?"

The classifier is an ensemble: random forest for categorical features, LSTM for stack-trace analysis and gradient boosting for time-series patterns, with continuous retraining fed by human feedback. She reports 93.8% accuracy at prioritising errors by business impact.

The features are the interesting part, grouped into four families:

- **Exception characteristics**: stack-trace patterns, exception type, message semantics, code-path frequency.
- **Business context**: estimated affected users, transaction financial value, process criticality, data integrity impact.
- **Temporal patterns**: time-of-day correlation, error frequency trends, business-hour weighting, seasonality.
- **Historical response**: prior resolution times, SLA breach prediction, escalation rates, developer response patterns.

The models were trained on 18 months of history covering 12,387 resolved incidents with full resolution workflows.

## Right alert, right channel, fewer storms

Routing evaluates each alert across 14 parameters, including severity, system impact, time of day and team workload, then picks the channel and urgency: a Slack DM, Microsoft Teams or email. Intelligent rate limiting clusters related errors and suppresses predicted cascades, which she says cut alert volume during major incidents by 68.2% while still catching 99.8% of unique issues.

Reported outcomes: an 88.5% reduction in MTTR, $2.3 million in annual savings from reduced downtime, a 23.5% gain in developer productivity and a 73.4% drop in overall alert volume.

## The MLOps lessons

Sreelatha's practices are refreshingly unglamorous. Start with one high-volume system and expand as models mature. Build explicit human feedback loops. Measure business outcomes like MTTR and cost, not just model accuracy. And build for transparency, so engineers understand why an alert fired and how it was routed. A classifier nobody trusts is just a new source of noise.

## Who should watch

SRE and platform teams drowning in alerts, and ML engineers looking for an applied problem with a clear success metric. It is a results-focused talk; the slides describe the architecture rather than show code.

## Related Conf42 talks

- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue)
- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise)
- [Mastering Monitoring and Alerting](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Rishabh_Srivastava_mastering_monitoring_alerting)

[Watch Sreelatha Pasuparthi's talk](https://www.conf42.com/MLOps_2025_Sreelatha_Pasuparthi_intelligent_error_response)

[Watch the talk on YouTube](https://youtu.be/Kxp3Ebhhhd8).

## Watch the talk

[Intelligent Error Response: How ML-Driven Slack Integration Cut MTTR by 88.5% Across 17 Enterprise Systems](https://www.conf42.com/MLOps_2025_Sreelatha_Pasuparthi_intelligent_error_response) at Conf42 MLOps 2025.
