# In healthcare, an accurate model nobody trusts never ships

Conf42 Blog, 2025-08-20, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/healthcare-ai-needs-governed-mlops-pipelines

In short: Nikitha Edulakanti (Fresenius Medical Care) at Conf42 MLOps 2025 on governed MLOps pipelines that let healthcare AI scale past the pilot.

A model that predicts ICU admissions with 95% accuracy on paper is worthless if clinicians and regulators cannot see how it got there. That is the opening example from Nikitha Edulakanti, Manager of Data and AI Solutions at Fresenius Medical Care, at Conf42 MLOps 2025, and her whole talk follows from it: in healthcare, governance is the part of the pipeline that turns a clever model into a used one.

Her framing line, taken from her deck, is that healthcare AI does not just need to be powerful, it needs to be trusted. The rest of the talk is about how you build that trust into the plumbing instead of bolting it on at the audit.

## Pilots die on data formats, not accuracy

Nikitha's diagnosis of why healthcare AI stalls is practical. Fragmented pipelines, data silos and compliance risk mean a model that works brilliantly at one hospital cannot move to the next. Her example is a pneumonia detection model trained on chest X-rays that performs well and then fails to expand because data formats differ across sites and nobody can sign off on compliance. A readmission-risk model piloted in one hospital needs standards, automation and monitoring before it can run in fifty.

She groups the obstacles into four: data governance (HIPAA in the US, GDPR in Europe, PHI protection at every stage), model trust (bias, drift, explainability), integration into clinical workflows, and operational scale. The integration point is the one engineers underrate. A triage tool that makes doctors log into a separate portal tends to fail; the same tool inside the EHR, with no extra clicks, has a chance.

## Compliance belongs in every stage of the lifecycle

Her definition of healthcare MLOps is DevOps practice plus the ML lifecycle, with governance embedded at ingestion, preprocessing, training, deployment and monitoring rather than reviewed at the end. Everything flowing through the pipeline must be traceable and auditable.

Because she works at a dialysis company, her examples come from kidney care. A kidney disease progression model ingests EMR data, masks PHI in preprocessing, trains with bias checks, deploys behind secure APIs and is monitored for drift quarterly. In another, IoT devices on dialysis machines stream patient vitals into the pipeline, and a sudden drop in blood pressure alerts clinicians before the patient deteriorates.

Her reference architecture is easy to steal: ingestion from EMRs, IoT devices, imaging and claims; a governance layer with data catalogs, access controls and audit trails; training with validation and explainability checks; containerised deployment across hybrid or multi-cloud; and continuous monitoring with a human in the loop.

## Generative AI explains the score, governance keeps it honest

The generative AI section is grounded. Rather than handing a clinician a bare risk number, a GenAI layer can explain that a patient is at elevated risk because of abnormal creatinine levels, a history of hypertension and two prior admissions in six months. Nikitha also lists documentation, coding workflows and data curation as places GenAI helps, and she is clear that without governance it can hallucinate or amplify bias.

Her closing metaphor works: governance is the steering wheel rather than the brake, the same way seat belts and traffic lights are what let cars go fast safely.

## Who should watch

ML and data engineers in healthcare or life sciences, and anyone who has watched a promising pilot die in compliance review. It is a framework talk with concrete clinical examples rather than a code walkthrough, which makes it useful for aligning engineers, clinicians and compliance teams on one picture.

## Related Conf42 talks

- [Swapna Chimanchodkar on DevOps pipelines for real-time sepsis detection](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) at Conf42 DevOps 2026.
- [Tharun Nallamothu (Microsoft) on Dragon Copilot in clinical workflows](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows), the EHR-integration point in practice.
- [Nisheedh Raveendran (LinkedIn) on regulatory incidents under HIPAA, GDPR and DMA](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr) at Conf42 Incident Management 2025.

[Watch Nikitha Edulakanti's talk](https://www.conf42.com/MLOps_2025_Nikitha_Edulakanti_mlops_scale_designing) for the full governed pipeline architecture.

[Watch the talk on YouTube](https://youtu.be/V6iOKA7Mmck).

## Watch the talk

[MLOps at Scale: Designing Governed AI Pipelines for Healthcare Impact](https://www.conf42.com/MLOps_2025_Nikitha_Edulakanti_mlops_scale_designing) at Conf42 MLOps 2025.
