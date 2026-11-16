# FHIR and Kubernetes microservices are closing healthcare access gaps

Conf42 Blog, 2025-10-05, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/fhir-and-microservices-widen-healthcare-access

In short: Geetha Sharanya Bolla (Apexon) at Conf42 Kube Native 2025 on data integration, FHIR and cloud-native microservices for rural and underserved care.

A diabetic patient visits a rural clinic, then a city hospital, then a specialist, and if those systems can't share data the tests get repeated and the history goes missing. At Conf42 Kube Native 2025, Geetha Sharanya Bolla, Lead Engineer at Apexon, made the case that fixing this is an integration problem, and that FHIR plus Kubernetes-based microservices is the combination that finally makes healthcare systems speak the same language.

The talk is an overview with a mission: the technology matters because of who it reaches, especially rural and underserved patients.

## Fragmented data means fragmented care

Geetha's opening statistic is that nearly 80% of critical patient data sits siloed across disconnected systems: records, lab results and prescriptions in separate databases that don't talk. Her framing is that this is a human problem as much as a technical one. When data is fragmented, care becomes fragmented, and every repeated test and delayed treatment follows from it.

The modernisation imperative she describes has three parts: infrastructure that handles large data volumes and many simultaneous users, interoperability so data moves securely between providers, payers and patients, and access for places where geography means weeks of waiting for a specialist.

## Lego bricks and a conductor

Her architecture metaphor is a friendly one. A monolithic hospital system is a giant rigid block; microservices turn it into Lego pieces for patient management, billing and scheduling that can be rearranged, reused and scaled independently. Kubernetes is the conductor that keeps them healthy and available. Standardised APIs, FHIR in particular, are how the pieces talk.

She tracks FHIR's rise as the quiet revolution behind it: adoption growing from 14.8% in 2017 to 58.3% by 2022, by the figures she cites. FHIR gives healthcare data a common grammar, so information flows between electronic health records, telehealth systems and mobile apps instead of staying locked in silos.

## What integration bought, in numbers she reports

The impact section collects figures from health information exchanges and implementations she reports on. Integrated HIEs, she says, cut preventable readmissions by 30% and duplicate lab tests by 52%. Moving to containerised, Kubernetes-native microservices brought, in her numbers, 62% higher transaction throughput, 47% faster responses at peak load, infrastructure costs down by up to 57% and deployment times improved by 74%.

COVID-19 was the stress test. Telehealth went from about 1% of visits before 2020 to 35.3%, and her argument is that systems already on cloud-native, API-based architectures were the ones that could absorb that overnight. The rural story is the one she clearly cares most about: a Kubernetes-based telehealth platform in rural India that, she reports, improved specialist access by 58% and cut urgent care delays by 43%.

## Four design principles

Her closing checklist is short enough to pin above a desk:

1. Cloud-native architecture: containerised microservices orchestrated by Kubernetes.
2. Standards compliance: FHIR and other interoperability standards from the start, not retrofitted.
3. Scalability: systems that expand elastically with demand.
4. Security and compliance across the whole development lifecycle.

## Who should watch

Engineers and architects new to healthcare who want the shape of the domain in one sitting, and healthcare IT teams making the case for interoperability work. Engineers already deep in FHIR will know the material; the value is the equity framing and the collected numbers.

## Related Conf42 talks

- [Platform Engineering for Healthcare Interoperability](https://www.conf42.com/Platform_Engineering_2025_Gunjan_Desai_Rajendrakumar_interoperability_exchange_fhir) builds FHIR data exchange as a platform.
- [API-Led Healthcare Transformation](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability) shows the API-led approach with MuleSoft.
- [Go Secure: Building Resilient Telemedicine Platforms](https://www.conf42.com/Golang_2025_Smita_Verma_telemedicine_security_resilience) covers the security side of telehealth.

[Watch Geetha Sharanya Bolla's talk](https://www.conf42.com/Kube_Native_2025_Geetha_Sharanya_Bolla_healthcare_integration_scalable)

[Watch the talk on YouTube](https://youtu.be/FnHdVzkEGKo).

## Watch the talk

[Reimagining Healthcare Access with Data Integration and Microservices at Scale](https://www.conf42.com/Kube_Native_2025_Geetha_Sharanya_Bolla_healthcare_integration_scalable) at Conf42 Kube Native 2025.
