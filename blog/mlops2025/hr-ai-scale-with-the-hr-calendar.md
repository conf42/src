# HR AI at 10 million interactions a month scales with the HR calendar

Conf42 Blog, 2025-09-10, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/hr-ai-scale-with-the-hr-calendar

In short: Ramprasad Reddy Mittana of NSF at Conf42 MLOps 2025 on running production ML for HR shared services, from privacy pipelines to blue-green deploys.

HR traffic has a calendar: onboarding spikes in January, performance reviews in December, benefits enrollment in the fall. At Conf42 MLOps 2025, Ramprasad Reddy Mittana, Senior Manager HRIS at NSF (NSF International), laid out the MLOps architecture behind AI in an HR shared services centre handling over 10 million interactions a month for about 50,000 employees, and his one line to remember was to align your scaling with the HR calendar.

Ramprasad brings 20-plus years across NSF International, the Abu Dhabi Investment Authority and Oracle. The talk is an architecture walkthrough with the speaker's reported results attached, aimed at people who run ML where the data is personal and the audit trail is mandatory.

## HR is a hard place to run models

He listed why standard MLOps falls short here. The data is sensitive and crosses national and legal jurisdictions. Volume swings with mass hiring, review cycles and open enrollment. The models have to answer a wide spread of query types consistently. Compliance is non-negotiable. And all of it runs at the 10-million-a-month scale, so manual babysitting is off the table.

## Containers, canaries and retraining on a schedule

The production setup is containerised models on Kubernetes, with GPU acceleration where training or inference needs it. New models roll out through automated A/B testing and canary deployments to a small slice of users first, gated by statistical significance tests. Scheduled retraining pipelines keep accuracy at or above 92% as query mix and data distributions drift.

Monitoring is HR-specific: real-time dashboards for chatbot response accuracy, resolution time and satisfaction, plus drift detection that he said spots degradation 73% faster than before. Every interaction, response and satisfaction rating feeds a supervised retraining loop, which he credited with a 28% accuracy gain overall.

## Privacy and the feature store do the heavy lifting

The data engineering section is the strongest. Automated PII detection and tokenisation built for GDPR and CCPA, schema enforcement and anomaly detection for data quality, and streaming feature engineering to keep inference fast. At the centre sits an HR feature store serving the same features to training and real-time inference, with point-in-time correctness to prevent leakage in time-series HR data, sub-10ms serving, and versioning and lineage tracked with Spark and Flink. He tied it to a 65% latency reduction and 40% lower compute cost.

Point-in-time correctness is the detail to steal. HR features like tenure or internal mobility change over time, and training on today's value for last year's label is a quiet way to build a model that looks brilliant offline and disappoints in production.

## Multi-tenant, blue-green, and spot instances

For scale, a multi-tenant architecture isolates business units on shared infrastructure. Blue-green deployments give zero-downtime updates and instant rollback. Autoscaling absorbs traffic spikes up to ten times normal during busy seasons, and spot instances plus right-sizing cut infrastructure spend by 40%.

Governance closes the talk: end-to-end audit trails for every AI decision, multi-jurisdiction compliance monitoring, HR-tailored explainability, and bias checks on both training data and every retraining cycle. He reported an 89% drop in discriminatory outcomes and made the point that bias is a continuing responsibility, not a one-off fix.

## Who should watch

HRIS and people-tech engineers putting chatbots or classifiers in front of employees, and anyone building a feature store for time-dependent personal data. If you need the Kubernetes specifics, this stays at the architecture level.

## Related Conf42 talks

- Swetha Priya Sathiyam (ADP) on [Leveraging Global HCM Systems for HR Digital Transformation](https://www.conf42.com/Machine_Learning_2025_Swetha_Priya_Sathiyam_hcm_transformation_implementation).
- Marina Goplacheva (Sberbank) on [building intelligent conversational AI experiences for HR tech](https://www.conf42.com/Prompt_Engineering_2024_Marina_Goplacheva_hrtech_conversationalai_intelligent).
- Reshma Vemula (Loma Linda University Health) on [Protecting PHI in Machine Learning Development Environments](https://www.conf42.com/Machine_Learning_2026_Reshma_Vemula_pipelines_orchestration_mlops), another take on sensitive data in ML.

[Watch Ramprasad Reddy Mittana's talk](https://www.conf42.com/MLOps_2025_Ramprasad_Reddy_Mittana_mlops_scale_production)

[Watch the talk on YouTube](https://youtu.be/u7lk2zrXZhs).

## Watch the talk

[MLOps at Scale: Production-Ready AI Systems for HR Transformation in Enterprise Shared Service Centers](https://www.conf42.com/MLOps_2025_Ramprasad_Reddy_Mittana_mlops_scale_production) at Conf42 MLOps 2025.
