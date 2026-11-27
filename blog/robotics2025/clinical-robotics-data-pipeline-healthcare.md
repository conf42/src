# Surgical robots need a data pipeline before they need a smarter arm

Conf42 Blog, 2025-11-20, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/clinical-robotics-data-pipeline-healthcare

In short: Srinivasa SKN Ambati of Anthem at Conf42 Robotics 2025 on a five-layer analytics architecture that feeds clinical robots real-time patient data.

A surgical robot is only as good as the data reaching it, and hospital data lives in systems that rarely talk to each other. At Conf42 Robotics 2025, Srinivasa SKN Ambati, Engineer Lead at Anthem, laid out an architecture that connects EHRs, IoT devices and robotic telemetry into one pipeline, so clinical robots and the clinicians beside them act on the same near-real-time picture.

The talk is a wide overview, from history to ethics, with a clear technical spine in the middle.

## From reactive care to closed loops

Srinivasa frames the shift as moving from treating illness to predicting and preventing it, powered by a mix of imaging, genomics, wearables, IoT and electronic health records. He sketches the robotics timeline too: PUMA 560 and later the da Vinci surgical system for minimally invasive surgery, robotic rehabilitation in the 2010s, AI-assisted robotics across surgery, pharmacy and hospital logistics by 2020. What comes next, he argues, is an integration era where robotic data feeds patient analytics and the loop closes.

Analytics follows the same arc: descriptive (what happened), predictive (what will happen), and now prescriptive (what to do next).

## Five layers between a sensor and a surgeon

The core of the talk is a five-layer framework:

1. **Acquisition** from robots, EHRs, IoT sensors and medical devices.
2. **Processing** that turns raw feeds into structured, usable records.
3. **AI and analytics**, where statistical and ML models produce insight.
4. **Integration** through APIs and middleware, so the pieces combine.
5. **Presentation**: dashboards, alerts and decision support at the point of care.

In motion, that is Apache Kafka streaming robotic telemetry and patient vitals, Apache Spark processing across a cluster, Hadoop HDFS storing structured and unstructured data, SAS Viya for modelling and forecasting, and HL7 and FHIR for talking to hospital EHR systems. Srinivasa calls the result the digital nervous system of modern healthcare, which is a fair description of a Kafka cluster nobody is allowed to restart.

## The model zoo has a job for everyone

The ML infrastructure runs on an automated lifecycle, a hybrid cloud that keeps sensitive PHI under tighter on-prem control while bursting to the cloud for scale, GPU clusters for imaging and containerized deployment. Models are monitored for drift, fairness and performance, with retraining triggered on drift. The algorithm map is tidy: CNNs for images, RNNs for patient time series, transformers for clinical text and reinforcement learning for robotic control.

Governance is non-negotiable here: HIPAA controls with role-based access, AES-256 encryption and audit logging, GDPR-style consent tracking, MFA, network segmentation and lineage. His one-liner: "trust is the ultimate currency".

## Before, during and after the incision

The clinical walkthrough covers preoperative 3D maps for planning, intraoperative tissue classification and postoperative models that flag complications early. The talk cites a 23% cut in operating times, roughly a third fewer complications, and predictive maintenance on robotic components at over 90% accuracy with downtime down nearly 40%; it doesn't name the studies behind them, so treat them as the speaker's figures.

Srinivasa is candid about the limits: inconsistent data quality, interoperability gaps, compute cost, clinician resistance, algorithmic bias and the need for real-world validation. His advice is to pilot small, adopt HL7 and FHIR, monitor for bias, set up ethics committees, and keep clinicians, engineers and patients in the same conversation.

## Who should watch

Data engineers moving into healthcare, architects designing PHI-heavy pipelines, and robotics teams who need to know what clinical data integration really involves. Expect breadth over depth; it's a map rather than a build guide.

## Related Conf42 talks

- [Swapna Chimanchodkar: DevOps Pipelines for Clinical AI](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) deploys real-time sepsis detection at scale.
- [Rajarshi Tarafdar: Human-AI Symbiotic Robotics](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Rajarshi_Tarafdar_human_ai_symbiotic) looks at precision in collaborative robots.
- [Aishwarya Pai: MLOps in Healthcare](https://www.conf42.com/MLOps_2025_Aishwarya_Pai_mlops_healthcare_scaling) covers deploying and monitoring clinical models.

[Watch Srinivasa SKN Ambati's talk](https://www.conf42.com/Robotics_2025_Srinivasa_SKN_Ambati_healthcare_analytics_ai)

[Watch the talk on YouTube](https://youtu.be/iC1E6RKvQK0).

## Watch the talk

[Harnessing Advanced Analytics and AI to Transform Clinical Robotics and Healthcare](https://www.conf42.com/Robotics_2025_Srinivasa_SKN_Ambati_healthcare_analytics_ai) at Conf42 Robotics 2025.
