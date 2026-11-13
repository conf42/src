# Compliance by construction for co-branded credit card platforms

Conf42 Blog, 2026-06-05, updated 2026-11-09. https://www.conf42.com/blog/llms2026/compliance-by-construction-co-branded-credit-cards

In short: Ravindra Rajasekhar Kavuru (Expedia Group) at Conf42 LLMs 2026 on building PCI, privacy and audit controls into credit platforms by design.

Retrofitting compliance onto a production system costs far more than designing it in, so make non-compliance architecturally hard. That is the thesis Ravindra Rajasekhar Kavuru, a software engineering manager at Expedia Group, puts forward at Conf42 Large Language Models (LLMs) 2026 for co-branded credit card platforms, where regulated banking infrastructure meets high-volume consumer traffic.

He opens with a disclaimer that the views are his own and based on general industry knowledge, not his employer's systems. Read it as a reference architecture, not a case study.

## Two worlds, one transaction

A co-branded card sits between a consumer platform that cares about throughput and a bank that cares about regulation, and every transaction has to satisfy both. Ravindra's framing of compliance by construction has four phases: regulatory constraints become system invariants at design time, enforcement is woven into service contracts and data flows at build time, policy is evaluated continuously against live telemetry at runtime, and audit evidence falls out of normal operation instead of being assembled once a year.

## Spend where the expected loss is

Security budgets should follow math, not fear. The talk proposes estimating breach probability per component and integration point from incident history, threat intelligence and system topology, then funding controls where the reduction in expected breach cost exceeds what the control costs, and spotting diminishing returns before over-investing in low-risk areas.

Technical controls alone aren't enough either. Drawing on behavioral compliance research, he lists what makes people actually follow policy: believing violations will be detected, security as a shared norm, compliant paths that are the easiest ones, and fast feedback on near misses.

## The stack, bottom to top

The architecture is presented as a pyramid:

- **Networking** built for very low latency and high throughput, with active-active regional deployment.
- **Distributed transactions** via sagas with compensating steps and outbox-based publishing, since two-phase commit is too slow at scale. A payment that succeeds but fails to record its compliance event is a regulatory liability, so the compliance record captures both the attempt and any compensation.
- **Event-driven services** on a bus such as Kafka, with schema-enforced, tamper-evident audit logs written to append-only sinks and enriched in-stream with risk scores and regulatory tags.
- **Security controls**: PCI DSS-aligned microsegmentation into cardholder-data, connected and out-of-scope zones, mTLS on every service call, network policy as code checked in CI, and tokenization using format-preserving encryption so tokens look like card numbers and downstream schemas don't change. ML predicts which tokens will be hot and keeps them in fast memory.
- **Real-time intelligence**: underwriting on precomputed features with no synchronous bureau calls on the critical path, streaming fraud scoring, and partner data checked at the ingestion boundary so partners can't inject non-compliant state.
- **Observability and governance** at the top.

## Where the LLMs come in

The LLM layer sits at the peak. Models learn normal behaviour from streaming telemetry and flag deviations with a plain-language explanation for analysts, aimed at novel fraud and violations that signature rules miss. Policy engines check operational behaviour against declared policy, and LLM components parse regulatory updates into proposed policy diffs. Every one of those proposals goes to a human, and Ravindra's last takeaway is to design the human-in-the-loop explicitly rather than as an afterthought.

## Who should watch

Architects and engineers on payments, cards or lending platforms, especially anyone preparing for a PCI DSS scope review. It is a dense architecture overview; LLMs are one layer, not the subject.

## Related Conf42 talks

- [AI-Powered Fraud Detection in Cloud-Native Digital Payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) by Sandeep Katuri, on the fraud-scoring layer.
- [IoT Payment Systems: Microservices Architecture for Connected Devices](https://www.conf42.com/Remix_2026_Silpa_Potluri_payments_microservices_architecture) by Silpa Potluri (GoodLeap), on payment gateways moving to microservices.
- [AI-Driven Sensitive Data Discovery for Secure DevSecOps and Privacy Compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) by Mary Sirisha Duggimpudi (T-Mobile USA), on finding regulated data before you can protect it.

[Watch Ravindra Rajasekhar Kavuru's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Ravindra_Rajasekhar_Kavuru_privacy_compliance_credit)

[Watch the talk on YouTube](https://youtu.be/lccAwOE5HG4).

## Watch the talk

[Compliance-by-Construction for Scalable, Privacy-Resilient Credit Apps](https://www.conf42.com/Large_Language_Models_LLMs_2026_Ravindra_Rajasekhar_Kavuru_privacy_compliance_credit) at Conf42 Large Language Models (LLMs) 2026.
