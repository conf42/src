# In ML compliance monitoring, an anomaly score is not a verdict

Conf42 Blog, 2026-09-15, updated 2026-11-09. https://www.conf42.com/devsecops2026/anomaly-score-is-not-a-verdict

In short: Vinay Puri of Amazon at Conf42 DevSecOps 2026 builds a working-hours alert system where ML flags unusual patterns and human investigators decide.

The hard part of ML-based compliance monitoring isn't the model. It's building a system that spots unusual behaviour at enterprise scale, explains why it looks unusual, and still leaves the decision with a human. At Conf42 DevSecOps 2026, Vinay Puri, Systems Development Manager at Amazon, used a Working Hours Alert System (WHAS) as the case study: rules for known policy violations, anomaly detection for patterns nobody wrote a rule for, and a firm line that a score measures unusualness, not guilt.

The domain is workforce time and attendance, but Vinay is clear the same architecture fits security events, access behaviour and transaction monitoring.

## Rules catch what you can describe

Traditional compliance monitoring asks deterministic questions: did someone exceed a set number of hours, did they miss a required break? Those rules stay. What they miss are patterns where every single event is technically valid, yet over several weeks you see odd start times, abnormal durations, repeated gaps or a sharp change from that person's own history. Anomaly detection asks a different question, whether this behaviour looks unusual compared with what we'd expect, and the design combines both.

## Four stages, separate jobs

WHAS is a four-stage pipeline: ingest operational data, validate and clean it, turn raw events into behavioural features, then score them. The separation is the point. Model code shouldn't compensate for bad timestamp parsing, and policy logic shouldn't hide inside feature engineering.

Data quality gets the most airtime, deservedly. Attendance, schedules, approved leave and HR records live in different systems with different time zones, duplicates, late updates and conflicting states. Feed that straight in and, in Vinay's words, "The model will happily detect your data pipeline problems as employee anomalies." Normalise and validate relationships between records before anything reaches features.

## Compare people with themselves

Features fall into four groups: duration and timing, recurrence (one odd day is noise, the same pattern for a week is interesting), a historical baseline per individual rather than one global definition of normal, and context such as leave, travel, shift changes or operational incidents. Normal looks different across job functions, shifts and geographies, so the per-person baseline does a lot of work.

On algorithms, Vinay steers away from treating this as classification. There's a mountain of ordinary behaviour and very few confirmed violations, often too few reliable labels to train on. Anomaly detection learns what expected looks like instead. The ladder runs from interpretable statistical baselines through clustering and tree-based methods to representation learning, with interpretability dropping as you climb. In compliance, the most accurate model isn't automatically the best one, because investigators stop trusting alerts they can't understand.

## An alert must say why

A high score can mean a legitimate schedule change, an emergency, missing data, an integration failure or something worth investigating. So an alert carries the observed pattern, the contributing signals, the comparison with history and the available context, not just "0.87". Prioritise by anomaly strength, recurrence, how many independent signals agree, and whether context already explains it. Ten thousand alerts every morning is technically anomaly detection and operationally useless.

Reviewer feedback improves thresholds and features, but through validation, versioning and controlled deployment, never by retraining production straight from investigator clicks.

## Degrade gracefully, monitor the monitor

Production reliability means watching data freshness, feature validity, source distributions and model behaviour, not just CPU. His graceful-degradation example is a good one: if the scheduling feed fails while attendance keeps flowing, the system must mark the analysis incomplete rather than read missing schedules as unusual employee behaviour. Every transformation, model version and threshold change goes in an audit trail so an alert can be reconstructed months later.

Because this is workforce data, privacy and governance cover the platform itself: data minimisation, and clear answers on who can change a threshold, deploy a model or read an alert. When drift appears, diagnose before retraining, since a source system changing its timestamp format looks a lot like behaviour change.

## Who should watch

Engineers building any detection system that points at people, whether insider risk, fraud or access anomalies, and teams arguing about how much to automate. The closing principle is the one to keep: appropriate automation, not maximum automation.

## Related Conf42 talks

- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu of Church Mutual Insurance Company at Conf42 Machine Learning 2025.
- [The AI Trust Triad for DevOps: Shipping Reinforcement Learning, Federated Learning, and Explainable AI Safely in Regulated Systems](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) by Saideepak Kandibanda of DISH Network at Conf42 DevOps 2026.
- [LLM Enabled Multi Document Correlation for Financial Compliance and Fraud Detection](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varsha_Shah_correlation_fraud_compliance) by Varsha Shah at Conf42 Large Language Models 2026.

[Watch Vinay Puri's talk](https://www.conf42.com/DevSecOps_2026_Vinay_Puri_ml_compliance_monitoring) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/SIdz64ciQ6M).

## Watch the talk

[Building ML-Based Compliance Monitoring for Automated Risk Detection](https://www.conf42.com/DevSecOps_2026_Vinay_Puri_ml_compliance_monitoring) at Conf42 DevSecOps 2026.
