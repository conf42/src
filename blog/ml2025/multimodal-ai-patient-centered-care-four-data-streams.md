# Multimodal AI in patient care means four data streams, not one

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/multimodal-ai-patient-centered-care-four-data-streams

In short: Hari Suresh Babu Gummadi (Frontier Internet) at Conf42 Machine Learning 2025 on fusing EHRs, patient-reported outcomes, genomics and wearables for care.

A clinical model that only reads the EHR sees the patient on the days they visit the clinic. At Conf42 Machine Learning 2025, Hari Suresh Babu Gummadi, an IT solutions architect at Frontier Internet with a background in enterprise workflow automation across telecom, finance and insurance, argued that patient-centred AI needs four streams at once: electronic health records, patient-reported outcomes, genomic profiles and wearable sensor data.

The talk is a framework overview, not a code walkthrough. Its value is in how it puts the pieces together and which clinical problems each stream is supposed to solve.

## Each stream covers a different blind spot

Hari's framing is that every data source fills a gap the others leave open. The EHR is the backbone: medical history, clinical notes, diagnostics. Patient-reported outcomes capture what the chart misses, such as pain levels and emotional wellbeing, the things a lab panel never shows. Genomic profiles bring in individual variants and biomarkers, so therapy choice can be targeted rather than averaged. Wearables fill the time between visits with heart rate, sleep and activity.

Put together, the model gets a continuous picture instead of a series of snapshots. Anyone who has debugged a system from hourly metrics alone, and then got per-second data and saw what was actually happening, will recognise the argument.

## The first payoff is clinician time

Before outcomes, Hari puts the clinician's workload. Automating routine analysis and surfacing the most relevant clinical information is pitched as reducing documentation time by 42%, giving clinicians about 3.5 extra hours a week with patients, and he reports 89% provider satisfaction with clinicians citing better work-life balance. On the patient side, he describes higher engagement, with patients more involved in treatment planning and more willing to trust their providers when AI-driven insights are shared and explained openly.

The point worth keeping: a model that adds clicks to a clinician's day will be ignored, however accurate it is. Workload comes first.

## Prediction is where multimodal earns its keep

The sharpest section is on early deterioration. Hari describes a prediction system that looks for subtle physiological changes across several parameters at once and flags critical deterioration up to 48 hours before conventional monitoring would. His examples are the kind of slow drift a single threshold alarm misses, like small but consistent changes in respiration or sleep quality preceding something like sepsis.

The same data feeds the shift from reactive to proactive care: personalised risk profiles built from genetics, lifestyle and environment; alerts when the expected pattern breaks, for example when refill activity drops; and treatment pathways tailored in oncology to reduce adverse effects. He closes with results from a five-year study across 27 healthcare systems, reporting a 34% increase in clinical efficiency and a 41% reduction in adverse events. The talk gives the headline figures rather than the study design, so treat them as the speaker's summary.

## The communication layer is underrated

One part that often gets skipped in AI healthcare talks is communication. Hari spends time on how the framework gives specialists and primary care the same consistent data, and turns complex results into clear recommendations a patient can follow. Prediction is useless if the referring GP never sees it.

## Who should watch

Engineers and architects starting on healthcare data platforms who want a map of which data sources matter and why. If you need model architectures, fusion techniques or validation methods, this talk stays at the framework level. One data note: the abstract on the talk page describes a different session on population health BI, so go by the video.

## Related Conf42 talks

- [Nick Rezaee (Harvard University) on AI agents that observe, reason and intervene on health data](https://www.conf42.com/AI_Agents_2026_Nick_Rezaee_health_wearables_intervene), the wearables stream taken to action.
- [Swapna Chimanchodkar on DevOps pipelines for real-time sepsis detection](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai), the deterioration use case shipped to production.
- [Tharun Nallamothu (Microsoft) on Dragon Copilot in clinical workflows](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows), for the documentation-burden side.

[Watch Hari Suresh Babu Gummadi's talk](https://www.conf42.com/Machine_Learning_2025_Hari_Suresh_Babu_Gummadi_healthcare_decision_patient)

[Watch the talk on YouTube](https://youtu.be/Eg0IWneE4jc).

## Watch the talk

[From Data to Decision: How Multimodal AI Is Transforming Patient-Centered Healthcare](https://www.conf42.com/Machine_Learning_2025_Hari_Suresh_Babu_Gummadi_healthcare_decision_patient) at Conf42 Machine Learning 2025.
