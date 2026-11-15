# In healthcare ML, PHI leaks from dev environments, not production

Conf42 Blog, 2026-02-13, updated 2026-11-09. https://www.conf42.com/blog/ml2026/phi-leaks-from-ml-dev-environments

In short: Reshma Vemula (Loma Linda University Health) at Conf42 Machine Learning 2026 on why ML dev copies leak PHI and a five-step plan built on synthetic data.

Every healthcare ML project starts the same way: someone copies production data into a dev environment so the model has something to learn from. At Conf42 Machine Learning 2026, Reshma Vemula, a Visualization Developer at Loma Linda University Health who specialises in EHR data security and compliance, argued that those copies are where protected health information actually escapes.

It is a short, focused talk: the risk, the numbers she presents, and a roadmap. Good for a lunch break.

## Your production data has several unmonitored twins

The core observation is multiplication. Production data gets copied into development, testing, training, validation and UAT, and Vemula says most healthcare organisations keep at least three to five copies of production data in non-production workflows, each carrying dozens of PHI elements per patient record. Every copy is another place to secure, and the non-production ones rarely get production-grade monitoring.

Her slides put the share of breaches occurring in development environments at 51.3%, and she reports that organisations relying on real PHI in dev and test face remediation costs roughly three times higher than those using synthetic data, once regulatory penalties, legal costs, disruption and reputational damage are counted.

## Mask it, or better, never copy it

The controls come in layers. Advanced data masking and encryption reduce unauthorised access while keeping data useful for testing, and deterministic masking matters for ML specifically: the same input always maps to the same masked value, so validation and model performance tests stay consistent across runs.

The stronger move is synthetic data generation. It preserves the statistical properties a model needs, keeps patients out of the training set entirely, and in her framing is the foundation of the whole roadmap. You cannot leak a record that was never real.

## Shift the security work left

The second half covers process. DevSecOps puts scanning into code writing, testing and deployment rather than after release, and she cites teams on this approach fixing over 95% of vulnerabilities during development. AI-driven monitoring watches activity across ML pipelines for anomalies to shorten response time. Across the pipeline she wants automated PHI detection at ingestion, isolated and encrypted training environments, secure validation, controlled deployment, and logging at every phase.

## The five-step roadmap

Her plan is incremental by design: start with synthetic data generation, then encryption and access controls, then secure training pipelines, then DevSecOps integration, and finally automated compliance. Each step can land without stopping the data science team, which is usually the objection that keeps real PHI in dev in the first place.

## Who should watch

Healthcare data engineers, ML platform owners and security or compliance leads in organisations bound by HIPAA. It is an overview rather than a tooling walkthrough, so pair it with something hands-on if you need to pick a masking or synthesis tool next week.

## Related Conf42 talks

- [Securing Healthcare at Scale: DevSecOps for Critical Patient Platforms](https://www.conf42.com/DevSecOps_2025_Mahendar_Ramidi_health_cloud_scale) by Mahendar Ramidi (Maryland Health Benefits Exchange) covers the DevSecOps half in a patient-facing system.
- [AI-Driven Sensitive Data Discovery for Secure DevSecOps and Privacy Compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) by Mary Sirisha Duggimpudi (T-Mobile USA) is about finding the sensitive data before it gets copied.
- [SRE and Healthcare Data Compliance: Balancing Security and Reliability](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sidhartha_Velishala_sre_healthcare_data) by Sidhartha Velishala (Humana) adds the reliability angle.

[Watch Reshma Vemula's talk](https://www.conf42.com/Machine_Learning_2026_Reshma_Vemula_pipelines_orchestration_mlops)

[Watch the talk on YouTube](https://youtu.be/qennWGFvRtA).

## Watch the talk

[Protecting PHI in Machine Learning Development Environments](https://www.conf42.com/Machine_Learning_2026_Reshma_Vemula_pipelines_orchestration_mlops) at Conf42 Machine Learning 2026.
