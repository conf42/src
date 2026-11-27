# More security tools, less clarity; a four-part health index fixes that

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/four-dimension-devsecops-health-index

In short: Sanjeevani Bhardwaj of Salesforce at Conf42 DevSecOps 2025 on a four-dimension DevSecOps health framework that tells you whether a pipeline is healthy.

Pipelines can pass every scan and still be brittle. At Conf42 DevSecOps 2025, Sanjeevani Bhardwaj, Director of Product Management at Salesforce, presented a four-dimension framework for DevSecOps health that answers the one question leadership keeps asking: is our pipeline actually healthy today? Her abstract reports 42% fewer incidents and 2.8 times faster secure development across 15 enterprise implementations.

## The DevSecOps health paradox

Organisations have more tools, more scans and more dashboards than ever, and somehow a less clear picture of their security posture. Security checks boxes, developers push code, operations keeps the lights on, and none of them share a language of health. When everything is measured separately, she says, nothing is understood collectively. Her bottom line: more tooling does not equal more clarity.

Her research found three gaps across industries: no standard way to turn raw scan output into health signals, inconsistent thresholds between teams (one group's acceptable build delay is another's emergency), and no remediation guidance once a problem is found. Is it a config fix, a redesign or a backlog item?

## Four dimensions instead of forty metrics

The framework distils health into four pillars:

- **Platform efficiency.** Pipeline performance, provisioning speed, resource utilisation and reliability. Her reasoning is behavioural: slow builds make developers bypass gates, and teams in permanent firefighting mode never get round to proactive security.
- **Customisation resilience.** How safely you diverge from vendor and community defaults. She calls it one of the most underestimated sources of incidents, with three maturity levels from everything customised and nothing tracked up to clear owners, lifecycle management, deliberate deprecation and real security reviews.
- **Observability.** Application instrumentation, infrastructure telemetry, security event aggregation and trace propagation across microservices, which buys earlier detection, faster investigation, empirical proof that controls work, and post-mortem learning.
- **Security guardrail adherence.** Preventative, detective and corrective controls, where the differentiator is operating them consistently with clear exceptions and feedback loops. When adherence is high, she argues, the secure path becomes the fastest one.

## Measure with layers and stable thresholds

Each dimension needs different data (monitoring tools, config repos, logging and tracing, scanners, policy engines), so collection is layered and automated, with data quality validation. Missing data often reveals infrastructure problems nobody knew about, which is a finding in itself.

Thresholds come in three tiers (baseline, target, excellence) rather than one magic number, and they must stay stable over time so you can tell real improvement from noise.

Industry adaptations get a short tour: healthcare guardrails tied to patient safety, retail's seasonal elasticity and strict payment thresholds, financial services' heavy customisation governance, and manufacturing's legacy systems and long deployment cycles.

## Start with the quick wins

Her rollout: a baseline assessment of all four dimensions, cross-functional health review forums, building skills such as root cause analysis plus DevSecOps health champions, then phased implementation. Platform efficiency and guardrails come first as quick wins; customisation resilience and observability follow because they need more instrumentation. Use the tools you already have, review regularly, and version the framework itself. Next on her list: AI-driven operations, confidential computing, third-party risk and supply chain security.

## Who should watch

Engineering and security leaders who have to report on pipeline health upward, and platform teams tired of arguing about whose dashboard is right. The talk is framework-level; the specific metrics behind each tier are left for you to define.

## Related talks

- [Automated DevSecOps maturity Assessment using Next-gen Technologies](https://www.conf42.com/DevOps_2023_Sandeep_Panghal_Juan_Antonio_Conde_automated_devsecops_maturity_assessment_nextgen) by Sandeep Panghal and Juan Antonio Conde.
- [Observability Maturity Model for AWS: From Reactive to Autonomous](https://www.conf42.com/Cloud_Native_2024_Indika_Wimalasuriya_observability_maturity_model) by Indika Wimalasuriya.

[Watch Sanjeevani Bhardwaj's talk](https://www.conf42.com/DevSecOps_2025_Sanjeevani_Bhardwaj_health_secure_cloud)

[Watch the talk on YouTube](https://youtu.be/7xz4n_dSKwM).

## Watch the talk

[DevSecOps Health Framework: 4-Dimension Assessment Cutting Incidents by 42%](https://www.conf42.com/DevSecOps_2025_Sanjeevani_Bhardwaj_health_secure_cloud) at Conf42 DevSecOps 2025.
