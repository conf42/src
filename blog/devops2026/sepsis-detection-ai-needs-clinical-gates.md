# Sepsis detection AI needs clinical gates, not just a good model

Conf42 Blog, 2026-01-04, updated 2026-11-09. https://www.conf42.com/blog/devops2026/sepsis-detection-ai-needs-clinical-gates

In short: Swapna Chimanchodkar at Conf42 DevOps 2026 on DevOps for clinical AI - streaming vitals, EHR integration, shadow and canary rollouts, SRE for sepsis alerts.

With sepsis, every hour of delay raises the chance of death by roughly 8%, so a prediction model that is down or late is a clinical failure. At Conf42 DevOps 2026, Swapna Chimanchodkar, an IEEE Senior Member and Osmania University alumna who works as a senior consultant and manager at Cognizant Business Consulting, walked through the DevOps and SRE practices that get real-time sepsis detection from a trained model into hospital workflows safely.

The talk frames sepsis as the case study, but she says explicitly at the end that the same approach applies to any mission-critical domain: fraud detection, predictive maintenance, autonomous vehicles.

## Why this is a platform problem

Chimanchodkar opens with the scale: sepsis claims approximately 11 million lives, around 20% of all mortality by her figures. AI can improve outcomes, she argues, but only when it is embedded into redesigned care workflows and backed by an always-on platform.

The complexity is familiar to anyone who has integrated enterprise systems, with higher stakes. Data comes from distributed hospital systems, vendor systems such as labs, and legacy electronic health records. It must stream in real time, feed a validated model, stay compliant and keep an audit trail. And a correct alert that no clinical process acts on is useless, so the workflow has to be designed alongside the pipeline.

## The pipeline, from monitor to alert

Her reference architecture processes patient vitals (heart rate, blood pressure, lab values) through cloud-native, event-driven microservices aiming for sub-second latency. Apache Kafka and cloud streaming services ingest data from monitors, lab systems and nursing platforms, and do feature engineering, aggregation and EHR enrichment before the model sees anything.

Two details stand out. Back-pressure management protects downstream services during peak demand. And EHR integration is a real engineering job: extract via HL7 FHIR APIs or custom interfaces, normalise heterogeneous data and terminology, handle missing values, and validate quality. Her example of an outlier blood pressure reading is a good reminder that normalising is not the same as averaging away the signal.

## Shadow mode before a clinician ever sees it

The rollout sequence is the most transferable part of the talk:

1. Algorithm development on retrospective data.
2. Retrospective validation on held-out data across patient demographics.
3. Shadow deployment, generating predictions without acting on them.
4. Clinical review of those results.
5. Canary release to small cohorts with continuous adverse-event monitoring.
6. Full production with ongoing performance and drift detection.

She calls these CI/CD with clinical gates: validation, performance and bias checks run continuously, alongside Kubernetes orchestration with autoscaling and health checks, and infrastructure as code for reproducible, recoverable environments.

## Observability is clinical, not just technical

Uptime is not enough. Her observability list covers prediction performance (sensitivity, specificity, alert rates), dashboards segmented by demographic and clinical unit to catch uneven drift, end-to-end latency from ingestion to alert delivery with thresholds tied to intervention windows, and automated data-quality alerts for missing values.

Drift is expected: patient populations change, practice changes, seasons shift. Statistical tests compare live prediction distributions against training baselines, and a breach triggers automated retraining or a data-science investigation, with actual clinical outcomes feeding back into supervised updates.

## SRE with patients in the loop

The SRE section translates directly: error budgets aligned with clinical impact (she cites a 99.95% uptime target for sepsis detection with strict latency percentiles), structured on-call with escalation paths to DevOps engineers, data scientists and clinical informatics, runbooks for common failures, and blameless postmortems. A pager rotation that includes a clinical informatics team is one most SREs have never had to design.

## Who should watch

Platform and ML engineers in healthcare, and anyone running models where a late answer is a wrong answer. It is a well-structured overview rather than a system tour from a specific hospital, so expect patterns, not war stories.

## Related Conf42 talks

- [Reliable AI for Clinical Handoffs: SRE Lessons for Safer Care Transitions](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhiram_Potharaju_reliable_clinical_handoffs) by Abhiram Potharaju (Wells Fargo) applies SRE thinking to another clinical workflow.
- [MLOps at Scale: Designing Governed AI Pipelines for Healthcare Impact](https://www.conf42.com/MLOps_2025_Nikitha_Edulakanti_mlops_scale_designing) by Nikitha Edulakanti (Fresenius Medical Care) covers governance for healthcare ML.
- [Clinical troubleshooting: diagnose production issues with scientific precision](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Dan_Slimmon_clinical_troubleshooting_diagnose) by Dan Slimmon borrows from medicine in the other direction.

[Watch Swapna Chimanchodkar's talk](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai)

[Watch the talk on YouTube](https://youtu.be/bk-cddFdoSI).

## Watch the talk

[DevOps Pipelines for Clinical AI: Deploying Real-Time Sepsis Detection at Scale](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) at Conf42 DevOps 2026.
