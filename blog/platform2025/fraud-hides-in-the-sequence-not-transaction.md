# Fraud Hides in the Sequence of Events, So Build a Platform

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/fraud-hides-in-the-sequence-not-transaction

In short: Rahul Ganti at Conf42 Platform Engineering 2025 on a real-time fraud platform with Kafka, Flink, a feature store and graph features.

The fraud in Rahul Ganti's case study wasn't in any single transaction. It was in six days of behaviour: small test payments, new payees with names close to existing ones, then a new device and an odd login location. At Conf42 Platform Engineering 2025, Rahul, who builds fraud detection at a financial institution he doesn't name, walked through the end-to-end platform that caught it, and argued that beating modern fraud is about engineering platforms, not writing better rules.

## Why rule engines lose

Rules were the long game of cat and mouse played in slow motion: a pattern emerges, analysts write a rule, criminals move on. Rigid thresholds generate false positives that block legitimate customers, a cost his team put at nearly $5 million a year. Rules see one transaction at a time, not the pattern around it, and they didn't scale with digital payments. Rahul also cites FTC data showing that while fraud report counts held steady, the share of people who actually lost money rose from 27% to 38% in a year: attackers are getting better per attempt.

## Five layers that decide in milliseconds

- **Ingestion** of transactions, customer profiles, device data and external threat feeds.
- **Stream processing** with Apache Kafka as the durable log and Apache Flink computing on the streams, so analysis happens in flight.
- **A feature store** with offline and online sides, so training and serving use the same feature logic. This is the guard against training-serving skew, the bug that quietly degrades models without throwing an error.
- **A model registry** as the control plane: multiple live models, A/B tests, gradual rollouts and instant rollbacks.
- **A decision engine** that combines model scores with configurable business rules, so analysts can trigger step-up authentication or flag an account without writing code.

Kafka between all of them keeps the components decoupled.

## Graphs find the network behind the account

The feature engineering is where the case study gets interesting. Streaming aggregations capture behaviour over windows (transaction count in five minutes, average amount over 24 hours). Graph features model customers, accounts and devices as nodes and transactions as edges. In the case study, the payees led to a network of 47 accounts across 12 institutions created in the same two-week window, with circular money flows and shared device fingerprints. Meanwhile login velocity was up 400% against the six-month baseline and behavioural biometrics showed an 85% deviation in mouse patterns. Rahul estimates the response prevented $2.3 million in losses across the affected institutions.

## The rest of the platform

Multi-cloud is deliberate: portability through containers and Kubernetes, failover between providers for a 99.99% availability target, and data residency per jurisdiction. The ML side has a sandbox, distributed GPU training, automated retraining pipelines and serving replicas across zones. Security is defence in depth: zero trust and microsegmentation, encryption, least privilege and full audit logs. Event sourcing gives regulators an append-only history, and sagas keep cross-service transactions consistent without two-phase commits. Federated learning lets institutions train a shared model without exchanging raw customer data, and Rahul is clear it's a big undertaking.

He reports p50 latency of 47 ms and p99 of 89 ms against a 100 ms SLA, and, for a mid-sized bank processing close to $50 billion a year, $27.2 million in prevented annual losses and 52,000 fewer legitimate transactions blocked each day.

## Who should watch

ML and platform engineers in payments or banking, and anyone building real-time decisioning where latency budgets and audit both bite. The feature store and decision engine sections apply well beyond fraud.

## Related Conf42 talks

- [Sandeep Katuri on AI-powered fraud detection in cloud-native digital payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security).
- [Arpit Mittal on balancing security and experience in payment fraud prevention](https://www.conf42.com/Large_Language_Models_LLMs_2025_Arpit_Mittal_payment_security_fraud).
- [Sridhar Muthineni on fraud detection in scalable Go fintech systems](https://www.conf42.com/Golang_2026_Sridhar_Muthineni_driven_fraud_detection).

[Watch Rahul Ganti's talk](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial)

[Watch the talk on YouTube](https://youtu.be/bC_CVJOvmpE).

## Watch the talk

[Building Resilient AI Platforms: Engineering Financial Fraud Detection at Scale](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial) at Conf42 Platform Engineering 2025.
