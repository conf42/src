# Real-time payments leave no 2 a.m. maintenance window

Conf42 Blog, 2026-05-30, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/real-time-payments-have-no-maintenance-window

In short: Priyatham Nagaiya Seenu Naidu (Mastercard) at Conf42 Database DevOps 2026 on Kafka, consistency choices and zero-downtime schemas for 24/7 payment rails.

Batch settlement had one quiet luxury: a maintenance window at 2 or 3 in the morning. Real-time payment rails took it away. At Conf42 Database DevOps 2026, Priyatham Nagaiya Seenu Naidu, Lead Software Engineer at Mastercard, walks through what that means for databases and DevOps when RTP, FedNow, UPI, Pix and SEPA Instant all run 24/7/365 with sub-second expectations and no off-peak hours.

It's a broad survey of the architecture, from streaming to compliance, rather than a single war story. Useful as a map of the moving parts and the decisions each one forces.

## Every transaction is an event now

The shift is from processing data on a schedule to processing each transaction the moment it happens. Priyatham puts event streaming at the centre: Apache Kafka for durable, distributed event logs with exactly-once semantics, and NATS or RabbitMQ for lightweight low-latency messaging. Kafka's partition model matters most to him because it scales horizontally while preserving per-account ordering. You can't process a debit before the credit it depends on, and you can't reorder events. Ingestion, validation, fraud scoring, settlement and notification all hang off the stream.

## Pick your consistency model on purpose

The database section is the core of the talk, with three rules:

- **Consistency is a deliberate choice.** Ledger updates and transactional flows need strong consistency; downstream analytics and notifications can often live with eventual consistency. His line: don't let the database choose for you.
- **Schema evolution happens with traffic flowing.** You can't take the system offline for migrations, so you rely on backward compatibility, strict schema change rules, feature flags, schema registries and rolling deployments.
- **High write pressure needs idempotency.** Write-optimised storage and connection pooling help, but in a distributed system retries are inevitable, so idempotency keys and retry-safe operations make sure a transaction is processed once even if the request arrives several times.

He also covers ISO 20022, which he describes as more than a message format: a schema-driven data model for rich remittance data, straight-through processing and real-time validation, adopted by FedNow and RTP among others.

## Always-on infrastructure, in three patterns

Microservices isolate failure domains, so a fraud service outage doesn't take settlement down with it. Kubernetes supplies auto-recovery, rolling deployments and horizontal pod scaling. And multi-region active-active databases accept writes in more than one region with consensus-based conflict resolution, so a regional outage doesn't stop payments. He contrasts Raft, with its leader-follower model that is easier to reason about operationally, and Paxos, which underpins systems like Spanner.

## Observability, fraud and security

"You cannot secure what you cannot see" runs through the last third. OpenTelemetry tracing follows a payment across dozens of microservices; latency percentiles, throughput and error rates become the primary SLAs; every log line carries a correlation ID, and adding region, country and city to log records shortens diagnosis from hours to seconds. Fraud detection gets its own constraint: the model has to run inside the transaction's latency budget, which pushes you to streaming feature engineering and lightweight models. Security is zero trust (network location is not a trust boundary), PCI DSS encryption and tokenisation, and PSD2 strong customer authentication, all treated as architectural constraints from day one rather than later additions.

## Who should watch

Engineers moving a payments or ledger platform from batch to streaming, and database teams asked to support one. If you've already built real-time rails, it's a good checklist; if you're new to the domain, it shows where the hard decisions are.

## Related Conf42 talks

- [Choosing the Right Messaging Platform for Your Event-Driven Application: RabbitMQ, Kafka, or Pulsar?](https://www.conf42.com/DevOps_2024_Julien_Jakubowski_right_messaging_platform_rabbitmq) by Julien Jakubowski, for the streaming choice.
- [Feature Flags as a Migration Engine: De-risking Domain-Driven Decomposition of Monolithic Payment Platforms](https://www.conf42.com/Feature_Flags_2026_Jaya_Chand_Bandi_migration_payment_platforms) by Jaya Chand Bandi, getting a payment monolith there safely.
- [AI-Powered Fraud Detection in Cloud-Native Digital Payments: Real-Time Security and Future Innovations](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) by Sandeep Katuri, the fraud scoring stage in more depth.

[Watch Priyatham Nagaiya Seenu Naidu's talk](https://www.conf42.com/Database_DevOps_2026_Priyatham_Nagaiya_Seenu_Naidu_kafka_pipelines_clusters)

[Watch the talk on YouTube](https://youtu.be/d02Iz4nQV8s).

## Watch the talk

[Real-Time Payments for Database DevOps: Scalable, Secure Systems](https://www.conf42.com/Database_DevOps_2026_Priyatham_Nagaiya_Seenu_Naidu_kafka_pipelines_clusters) at Conf42 Database DevOps 2026.
