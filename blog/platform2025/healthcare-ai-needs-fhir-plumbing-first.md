# Healthcare AI only pays off once the FHIR plumbing is in place

Conf42 Blog, 2025-08-14, updated 2026-11-09. https://www.conf42.com/blog/platform2025/healthcare-ai-needs-fhir-plumbing-first

In short: Srimurali Krishna Chillara of Boston Children's Hospital shows at Conf42 Platform Engineering 2025 how FHIR, NLP and BI turn clinical data into outcomes.

The flashy part of healthcare AI is a model beating a dermatologist. The part that decides whether it ever helps a patient is an integration layer nobody puts on a slide. At Conf42 Platform Engineering 2025, Srimurali Krishna Chillara, Senior MicroStrategy Architect at Boston Children's Hospital, made that case: BI and AI only deliver outcomes in hospitals once platform engineers have unified the data underneath them.

## Sixteen platforms and no common language

Chillara opens with the mess. By his figures the average health system runs more than 16 platforms, most with incompatible data models; over 80% of healthcare data is unstructured (physician notes, imaging, scanned PDFs); and only about 30% of hospitals have achieved meaningful integration despite regulatory mandates. Add HIPAA, GDPR and newer AI rules on top, and "let's add some AI" becomes a multi-year project before the first prediction.

His proposed shape is a three-layer platform:

1. **Data integration:** FHIR-based APIs, real-time streaming and ETL/ELT pipelines pulling structured and unstructured data together.
2. **Analytics processing:** NLP over clinical text, dashboards for operations, machine learning for patient risk and resource needs.
3. **Delivery:** role-based access, integration into clinical workflows, and explainable AI so clinicians actually trust what they see.

## FHIR is the boring hero

The most engineering-heavy section is about FHIR (Fast Healthcare Interoperability Resources). Its pitch to developers is that it is plain RESTful APIs instead of the rigid message formats of older standards. Chillara cited integration projects finishing 63% faster on FHIR than on HL7 v2, and roughly three times the return on investment because data moves between systems instead of being re-keyed. If you have ever parsed a pipe-delimited HL7 message by hand, that speedup will not surprise you.

## Models matter less than where they land

He walks through the clinical numbers that usually headline these talks, from AI diagnostic accuracy in dermatology to fewer missed lung nodules in radiology and faster pathology. The point he draws from them is a platform one: none of it helps unless the model is embedded in the clinician's workflow, showing decision support inside the systems they already use rather than in a separate research tool.

Two case studies make it concrete. An emergency department fighting overcrowding combined real-time capacity management, predictive analytics and ML triage on one platform; he reported boarding times for admitted patients down 32%, triage 41% faster and about $4.2 million a year saved. On the money side, NLP pulling billing-critical details out of clinical notes, plus models that flag claims likely to be denied before submission, cut denied claims by 67% and lifted revenue by 12% in his example.

## NLP turns notes into FHIR resources

The unstructured-data section is the bridge between the two worlds. Named entity recognition and medical concept detection turn discharge summaries and referral letters into structured, FHIR-compliant resources, which can then feed population health analytics, quality reporting or decision support. In other words, the notes stop being a write-only database.

## Match ambition to readiness

The adoption advice is refreshingly modest. Low-readiness organisations should start with small pilots and simpler tools while fixing data quality and culture; high-readiness ones can go for enterprise-wide ML. The pitfalls he names are the classic ones: leading with technology instead of the problem, underestimating data quality, and building tools that sit outside clinical workflows. He closes on what comes next: federated learning across institutions without sharing raw data, ambient documentation, multimodal models, and AI regulation that demands every system be explainable and auditable.

## Who should watch

Data and platform engineers moving into healthcare, or BI teams being asked to "add AI", will get a sensible architecture and a vocabulary for the conversation with clinicians. It is an overview talk: expect the reasoning and the reported results, not code or FHIR resource walkthroughs.

## Related Conf42 talks

- Venugopal Reddy Depa on [API-led healthcare interoperability with MuleSoft](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability) at Cloud Native 2025.
- Satya Manesh Veerapaneni on [AI-powered healthcare BI built in Go](https://www.conf42.com/Golang_2025_Satya_Manesh_Veerapaneni_healthcare_bi_analytics) at Golang 2025.
- Tharun Nallamothu on [Dragon Copilot, an AI assistant inside clinical workflows](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows) at Kube Native 2025.

[Watch Srimurali Krishna Chillara's talk](https://www.conf42.com/Platform_Engineering_2025_Srimurali_Krishna_Chillara_outcomes_intelligence_transforming)

[Watch the talk on YouTube](https://youtu.be/VZEh4sbiDLE).

## Watch the talk

[Engineering Intelligence: Transforming Healthcare with BI & AI from Data to Outcomes](https://www.conf42.com/Platform_Engineering_2025_Srimurali_Krishna_Chillara_outcomes_intelligence_transforming) at Conf42 Platform Engineering 2025.
