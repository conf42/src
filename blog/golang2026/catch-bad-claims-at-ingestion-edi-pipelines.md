# Catch the bad claim at ingestion, not at adjudication

Conf42 Blog, 2026-05-12, updated 2026-11-09. https://www.conf42.com/blog/golang2026/catch-bad-claims-at-ingestion-edi-pipelines

In short: Devi Manoharan of ASTA CRS at Conf42 Golang 2026 on healthcare claims systems that pair ML scoring with staged EDI pipelines on Go and Kafka.

Healthcare claims get expensive the later a problem is found. At Conf42 Golang 2026, Devi Manoharan, Senior SDET at ASTA CRS who works in healthcare quality engineering, made the case for moving intelligence earlier in the claims workflow: score claims with machine learning as they arrive and treat EDI processing as a staged, concurrent pipeline.

It is a short, high-level talk, closer to an architecture briefing than a build log, and a useful one if you are new to how payer systems move claims around.

## Rules engines stop scaling before the claims do

Devi starts with the pressure on payers: growing claim volumes, coding standards, payer rules and compliance requirements. Rule-based validation handles the basics, but large organisations end up maintaining thousands of business rules, and a small change can ripple through several systems. Rules also cannot spot patterns they were not written for.

Machine learning fills that gap with claim classification, anomaly detection, risk scoring and intelligent routing. Her examples are duplicate claims, unusual billing patterns and high-risk claims flagged before they reach adjudication. High-confidence claims flow straight through automation, and only the complex ones go to analysts. As she points out, even small efficiency gains add up when a system processes millions of claims.

## EDI is a pipeline, so build it like one

The EDI section is the most concrete. X12 transactions, 837 claims (dental, professional, institutional) and 835 remittance files, are the backbone of claims processing. Devi breaks the workflow into stages: segment parsing, enrichment (eligibility and provider details added before the claim moves on), schema mapping and HIPAA compliance validation in line with CMS guidelines. Smaller stages scale and fail more gracefully than one big batch job.

Her reason for caring about validation up front is money. A claim that goes through wrong and is later denied or voided can leave the payer dealing with overpayments and adjustments. Catching it at the parsing and enrichment stage is cheaper than unwinding a payment. It is the claims version of the oldest rule in testing, which makes sense coming from an SDET.

## The stack behind it

The reference architecture is modular: independent services talking through Kafka topics, each scaling on its own workload and isolating faults from its neighbours. Go runs the backend services, Python and TensorFlow handle the models, and PostgreSQL with Redis covers storage and caching. Models run inside the pipeline as real-time scoring services, so claims are evaluated during processing rather than after, and Devi flags model versioning and feature consistency as requirements for trustworthy predictions.

Reliability features round it out: circuit breakers, retries, distributed tracing and audit logging, which in a regulated environment serve stability and compliance at the same time.

## Who should watch

Engineers and testers joining a payer or health-tech team who want the map of 837/835 flows, enrichment and validation in one sitting. If you already run an EDI platform at scale, expect a summary rather than new techniques; the talk does not go into model details or metrics. Her four takeaways make a decent checklist anyway: move intelligence earlier, treat EDI as a scalable pipeline, design for concurrency, and build reliability into every layer.

## Related Conf42 talks

- [Suman Neela on payer claims integration](https://www.conf42.com/Golang_2025_Suman_Neela_payor_claims_integration) at Conf42 Golang 2025
- [Uday Bag on AI-driven claims](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Uday_Bag_ai_driven_claims) at Conf42 SRE 2025
- [Pravesh Nikhare on dental claims fraud](https://www.conf42.com/Large_Language_Models_LLMs_2025_Pravesh_Nikhare_dental_claims_fraud) at Conf42 LLMs 2025

[Watch Devi Manoharan's talk](https://www.conf42.com/Golang_2026_Devi_Manoharan_building_high_performance)

[Watch the talk on YouTube](https://youtu.be/YMtSrnLA9XU).

## Watch the talk

[Building High-Performance Claims Systems with AI and EDI Pipelines](https://www.conf42.com/Golang_2026_Devi_Manoharan_building_high_performance) at Conf42 Golang 2026.
