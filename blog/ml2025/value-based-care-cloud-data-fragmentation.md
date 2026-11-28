# Value-based care is a data integration problem first

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/value-based-care-cloud-data-fragmentation

In short: Bandanawaz Mulla (Health Care Service Corporation) at Conf42 Machine Learning 2025 on how cloud platforms tackle the data and reporting work behind value-based care.

If you get paid for patient outcomes instead of procedures, you have to be able to measure outcomes, and most healthcare data is not ready for that. At Conf42 Machine Learning 2025, Bandanawaz Mulla, Senior Manager Platform Strategy at Health Care Service Corporation with more than 19 years in IT, walked through the challenges of value-based care (VBC) and the cloud patterns that address each one, ending with a system his team built on AWS.

It is a payer-side view of the problem, which makes it a useful counterweight to the many provider-side healthcare AI talks.

## From fee-for-service to quality metrics

Bandanawaz frames VBC as the move from fee-for-service, where more services equal more revenue, to reimbursement tied to benchmarks, cost and patient satisfaction. That means preventive care, chronic disease management and coordinated care across providers. It also means tracking a lot of quality metrics: HEDIS measures, STAR ratings, ACO performance. The model promises better care at lower cost, but it demands changes in workflows, infrastructure and culture.

## Fragmentation is the root problem

Patient data lives in separate EHRs, lab systems, pharmacy databases, billing platforms and specialty records. Each silo creates a blind spot for clinical decisions and makes quality reporting close to impossible. His fix is the familiar but correct one: a cloud data lake that pulls disparate sources into one repository, FHIR APIs and HL7 integration engines for two-way data sharing, and normalisation services so the data is usable for analytics.

Reporting follows from there. He names AWS HealthLake, Microsoft Azure for Health and the Google Cloud Healthcare API as platforms that automate extraction, normalisation and metric calculation, with dashboards that find care gaps while there is still time to act, rather than in a retrospective review months later.

## Coordination, engagement and risk

The middle of the talk maps the remaining challenges to cloud capabilities:

- **Care coordination**: role-based shared care plans that specialists, primary care, nurses and social workers update at the same time, plus alerts for missed appointments or care plan deviations.
- **Patient engagement**: automated SMS, email and app reminders, secure messaging, wearables for remote monitoring, and patient portals tailored to language and literacy.
- **Risk stratification**: machine learning on clinical data, claims history and social determinants of health, using cloud compute to find high-risk patients early.
- **Compliance**: HIPAA, HITRUST and SOC 2 frameworks available from the cloud provider, with automated audit logging.

## The engine his team built

The most concrete part is a value-based care data enablement engine Bandanawaz's team implemented on AWS. It aggregates data into a unified view of contract performance against key metrics. He reports that it cut provider onboarding and implementation costs by 25% or more, reduced reporting time by 75% and improved accuracy by 30%. That is the bit of the talk you can take to a planning meeting.

His best-practice advice is incremental: assess current systems, define specific VBC goals, start with the highest-impact use case, involve stakeholders early, and use FHIR APIs to standardise exchange. Nobody migrates a payer's data estate in one quarter.

## Who should watch

Data and platform engineers at payers, ACOs or health systems moving into value-based contracts, and anyone who needs to explain to a non-technical sponsor why the data lake comes before the AI. It is a strategy talk with one real system in it, not a hands-on tutorial.

## Related Conf42 talks

- [Venugopal Reddy Depa on API-led healthcare interoperability with MuleSoft](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability), the integration layer in more detail.
- [Santhosh Kumar Rai on cloud-native data engineering in healthcare](https://www.conf42.com/Cloud_Native_2025_Santhosh_Kumar_Rai_data_engineering_healthcare_precision), for the pipelines underneath.
- [Sulabh Jain on cloud-native core systems for insurance](https://www.conf42.com/Database_DevOps_2026_Sulabh_Jain_kafka_streams_k8s), the insurer's view of modernising the core.

[Watch Bandanawaz Mulla's talk](https://www.conf42.com/Machine_Learning_2025_Bandanawaz_Mulla_value_based_care)

[Watch the talk on YouTube](https://youtu.be/96iCOppiWTk).

## Watch the talk

[Overcoming Key Challenges in Value-Based Care through Cloud Solutions](https://www.conf42.com/Machine_Learning_2025_Bandanawaz_Mulla_value_based_care) at Conf42 Machine Learning 2025.
