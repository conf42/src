# Moving a message broker to AWS: rehost, replatform or refactor

Conf42 Blog, 2026-03-05, updated 2026-11-09. https://www.conf42.com/blog/sre2026/moving-rabbitmq-to-aws-rehost-replatform-refactor

In short: Ran Tao (AWS) at Conf42 SRE 2026 compares lifting RabbitMQ to EC2, Amazon MQ, and refactoring clients for SQS and SNS, with Python code.

Lift-and-shift is the fastest way to move a message broker to the cloud and the one that keeps the most work on your team. At Conf42 Site Reliability Engineering (SRE) 2026, Ran Tao, Cloud Support Engineer at Amazon Web Services, compared three migration paths for on-prem messaging (rehost on EC2, replatform onto Amazon MQ, refactor for SQS and SNS) and showed Python client code for RabbitMQ and SQS side by side.

He calls it an introductory session, and it is: a structured map of the options on AWS, from an AWS engineer, useful if you're about to make this decision.

## Two kinds of messaging

On one side sit traditional message brokers such as IBM MQ or RabbitMQ, dedicated infrastructure connecting producers and consumers. On the other sit cloud-native serverless services: on AWS, SQS for queueing and SNS for broadcasting. Ran notes how requirements differ by industry: retail needs elasticity for peaks and quiet nights, while financial and government customers care most about durability and recovery during incidents.

Running brokers on-prem means paying for capacity up front, provisioning more to scale, and keeping engineers with specialist skills to run and monitor them.

## Three paths and who owns what

**Rehost.** Mirror the OS, broker engine and configs on EC2. Few application changes and full control, but you still own patching, broker monitoring and security configuration, and native integration with IAM or CloudWatch is limited.

**Replatform.** Move to Amazon MQ, a managed broker. Configuration shrinks to deployment mode and instance size; CloudWatch metrics (connections, channels, memory, per-queue message counts) and broker logs come enabled. Scaling up is a bigger instance size and a reboot instead of editing RabbitMQ config files. TLS is enforced, data at rest can be encrypted with a KMS key, and patching happens in a weekly maintenance window you pick, for example midnight for a retailer. Single-node brokers live in one Availability Zone and suit proofs of concept; for production Ran recommends cluster mode, which mirrors messages across three nodes in three AZs so losing one doesn't lose data.

**Refactor.** Rewrite clients for SQS and SNS. Scaling and capacity become the provider's problem and pricing is per API call, so a retailer isn't paying for an idle broker fleet at night. Your team's responsibility shrinks to business logic.

## What the code actually changes

The RabbitMQ example uses Pika: set TLS 1.2 connection parameters, open a connection and channel, declare a queue, publish, then close the connection. Ran stresses closing connections, because leaked ones show up as broker memory and CPU creeping up over time. Consumers must call `basic_ack`, or the broker eventually treats them as inactive.

The SQS version has no connection management at all. Create the queue, get its URL, send and receive messages through API calls, and delete each message after processing using its receipt handle; skip that and the message reappears after the visibility timeout.

## The refactor checklist

- **Separate producers from consumers** so they scale independently; draining a backlog shouldn't require more producers.
- **Know your delivery model.** A broker does point-to-point and publish-subscribe in one place. On AWS they split: SQS is point-to-point, SNS is publish-subscribe.
- **Protocols change.** AMQP and other persistent-connection protocols become HTTPS API calls.
- **Ordering versus scale.** SQS FIFO queues keep strict order; standard queues give best-effort ordering and scale much further.
- **Payload limits.** Messages are capped at one megabyte by default; AWS extended client libraries for Java and Python store the body in S3 and send a pointer, up to two gigabytes.
- **Auth and audit.** SQS and SNS use IAM and can log requests in CloudTrail, whereas RabbitMQ, even on Amazon MQ, may need something like an LDAP server.
- **Lost knobs.** Managed services remove some settings; you can't turn TLS off on an Amazon MQ RabbitMQ broker.

## Who should watch

Teams running RabbitMQ or ActiveMQ on-prem with a cloud migration on the roadmap, and SREs who want to know what they will still own after each option. If you already run SQS in production, you can skip it.

## Related Conf42 talks

- [Choosing the Right Messaging Platform for Your Event-Driven Application: RabbitMQ, Kafka, or Pulsar?](https://www.conf42.com/DevOps_2024_Julien_Jakubowski_right_messaging_platform_rabbitmq) by Julien Jakubowski (StreamNative).
- [Migrating to Multi Cluster Managed Kafka with 0 Downtime](https://www.conf42.com/Cloud_Native_2022_Natan_Silnitsky_migrating_multi_cluster_managed_kafka_0_downtime) by Natan Silnitsky (Wix), a messaging migration story at scale.
- [Transforming SaaS with Serverless Architectures](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Srikar_Kompella_transforming_saas_serverless) by Srikar Kompella (Prime Video & Amazon Studios).

[Watch Ran Tao's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ran_Tao_migration_prem_messaging)

[Watch the talk on YouTube](https://youtu.be/H5903XfJR4I).

## Watch the talk

[Migration from On-Prem Messaging System to The Cloud: What, How and Why](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ran_Tao_migration_prem_messaging) at Conf42 Site Reliability Engineering (SRE) 2026.
