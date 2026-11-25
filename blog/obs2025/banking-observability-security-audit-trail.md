# In cloud banking, the trace is the security control

Conf42 Blog, 2025-05-19, updated 2026-11-09. https://www.conf42.com/blog/obs2025/banking-observability-security-audit-trail

In short: Subrahmanyam Mamidi at Conf42 Observability 2025 on using metrics, logs and traces to catch breaches early and keep cloud banking audit-ready.

A payment breach that sits undetected for 72 hours is the scenario Subrahmanyam Mamidi builds his Conf42 Observability 2025 talk around. His argument: once a bank runs on microservices across several clouds, observability stops being an operations nicety and becomes a security and compliance control. The same traces that explain a slow payment also show where an attacker went.

## Why banks lose sight of their own systems

Subrahmanyam starts with the migration path most banks are somewhere along: fully on-premises data centres with total control, then hybrid setups where selected workloads move to cloud providers, then cloud-native banking built on distributed microservices and serverless. Each step buys agility and gives up a bit of visibility.

He lists the pressures that make that trade painful in finance:

- Regulation that does not care about your architecture: Basel III, GDPR and regional banking authorities.
- Distributed dependencies that traditional monitoring was never built to follow.
- An attack surface that grows with every new provider and region.
- Data sovereignty: a bank must know exactly where customer financial data flows.

## Three signals, two jobs

The framework is the classic trio. Metrics track system performance, resource use and transaction volumes. Logs give a chronological record of events, incidents and financial transactions, which doubles as the audit trail. Traces follow a transaction end to end across microservices, capturing the dependencies and latencies in payment processing.

What makes the talk worth a listen is how he maps those signals onto security work. Suspicious patterns surface before they become a breach. Traces let you find the source and scope of an incident across distributed systems quickly. A live dependency map doubles as an attack surface map. And after the incident, a complete audit trail makes forensics a query instead of a scavenger hunt.

On the compliance side the same data supports continuous, automated validation against Basel III and GDPR, plus immutable audit artefacts that examiners can actually use.

## Four steps to build it

His implementation recipe is short:

1. **Instrumentation**: put telemetry into the critical banking services so the code reports on itself.
2. **Collection**: a fault-tolerant pipeline that gathers and normalises metrics, logs and traces from very different systems.
3. **Storage**: regulatory-compliant, secure repositories with granular retention policies that satisfy both operations and compliance.
4. **Analysis**: machine learning to correlate the streams and flag security anomalies.

Storage is the step people underestimate. In a bank, telemetry is itself sensitive data with its own retention rules.

## The case study and the numbers

The anchor example is a retail bank whose payment processing breach went undetected for 72 hours under traditional monitoring. After adding distributed tracing across its cloud microservices with anomaly detection, Subrahmanyam says the bank detected incidents in under five minutes and prevented about $4.2 million in fraud losses while staying compliant. He also cites a 62% reduction in incidents, 78% faster response and a 41% cut in compliance documentation effort after observability programmes like this one. No bank or data source is named for those figures, so read them as illustrations of the shape of the payoff.

## Practical advice that survives the slides

The best practices are sensible and specific to the domain: design observability into the architecture from the start, map technical metrics to banking outcomes and customer experience, use ML for anomaly detection in complex transaction flows, and control cost with sampling, because full-fidelity telemetry on every transaction gets expensive fast. The rollout he suggests starts with an assessment focused on high-risk transaction paths, then a pilot in one critical service, then enterprise scale, then continuous tuning as threats change.

## Who should watch

Engineers and architects in financial services who need to explain to a security or compliance team why tracing deserves budget. It is an overview rather than a hands-on session, so you get a framework and a vocabulary, not a reference implementation.

## Related Conf42 talks

- [Narendra Bhargav Boggarapu on cloud-powered open banking and its security model](https://www.conf42.com/DevOps_2025_Narendra_Bhargav_Boggarapu_cloud_banking_security) at Conf42 DevOps 2025.
- [Sandeep Katuri on real-time fraud detection in cloud-native digital payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) at Conf42 Cloud Native 2025.
- [Vijaya Kumar Guntumadugu on cloud-based anti-money laundering with AI](https://www.conf42.com/Large_Language_Models_LLMs_2025_Vijaya_Kumar_Guntumadugu_banking_compliance_money) at Conf42 LLMs 2025.

[Watch Subrahmanyam Mamidi's talk](https://www.conf42.com/Observability_2025_Subrahmanyam_Mamidi_security_trust_banking)

[Watch the talk on YouTube](https://youtu.be/Lunp9X4FIJI).

## Watch the talk

[Observability in the Cloud: Enhancing Security and Trust in Modern Banking](https://www.conf42.com/Observability_2025_Subrahmanyam_Mamidi_security_trust_banking) at Conf42 Observability 2025.
