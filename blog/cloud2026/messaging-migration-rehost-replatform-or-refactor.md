# Moving RabbitMQ to the cloud? Choose rehost, replatform or refactor

Conf42 Blog, 2026-04-02, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/messaging-migration-rehost-replatform-or-refactor

In short: Ran Tao of AWS at Conf42 Cloud Native 2026 on migrating on-prem message brokers to EC2, Amazon MQ or SQS/SNS, and what changes in client code.

Lift-and-shift your message broker to a VM and you have moved the hardware, not the work: patching, broker monitoring and capacity planning still land on your team. At Conf42 Cloud Native 2026, Ran Tao, Cloud Support Engineer at AWS, gave an introductory walkthrough of the three paths for moving an on-prem messaging system to the cloud (rehost, replatform, refactor), with Python code comparing a RabbitMQ client to Amazon SQS.

Honest scope: Ran says up front it is an introductory session, and the cloud side is AWS throughout, covering EC2, Amazon MQ, SQS and SNS. The decision framework transfers to other clouds; the service names do not.

## Two kinds of messaging system

On one side sit traditional message brokers such as IBM MQ, ActiveMQ and RabbitMQ: dedicated infrastructure connecting upstream and downstream services. On the other sit serverless messaging services, in AWS terms SQS for queuing and SNS for broadcasting. Industries lean on them differently. Retail sees peaks on weekdays and quiet nights and weekends, so it cares about scaling. Financial and government customers care most about durability and recovery during incidents.

On-prem, you pay for both capacity and specialists: doubling throughput means buying hardware, and running the brokers needs engineers with specific skills.

## Three paths and who owns what

- **Rehost** onto EC2. Quickest, with full control over OS, broker engine and version, and application logic barely changes. But security, patching and broker monitoring stay with you, and metrics such as connected clients are not natively wired into CloudWatch or IAM.
- **Replatform** onto Amazon MQ. You choose single-node or cluster deployment and an instance size instead of tuning OS, memory and CPU. CloudWatch integration is on by default, TLS is enforced, KMS can encrypt data at rest, and patching runs in a weekly maintenance window you pick. Scaling up is an instance-size edit and a reboot, rather than reworking the RabbitMQ config file by hand.
- **Refactor** to SQS and SNS. Your team owns only the business logic; capacity and scaling belong to the provider, pricing follows API calls, and the retail-at-midnight problem disappears because nothing sits idle.

His single-node versus cluster advice is worth repeating: one instance in one availability zone is fine for proofs of concept and development, but for production, use the cluster deployment, which mirrors messages across three nodes in three availability zones so losing one zone loses no data.

## What the client code shows

The RabbitMQ side uses the Pika library: set connection parameters (TLS 1.2), open a connection and channel, declare a queue, publish, and close the connection when you are done or it keeps eating broker resources. Consumers must acknowledge each message with a basic ack, or the broker will eventually treat the consumer as inactive and close the connection.

The SQS side has no connection management at all. Create a queue with properties like retention period, get a handle by name, `send_message`, `receive_message`, and then delete the message using its receipt handle. Forget the delete and the message becomes visible again after the visibility timeout, which is SQS's version of the missing ack.

## The refactor checklist

When moving to serverless, Ran's list is practical:

- **Separate producers from consumers** so each scales on its own; a backlog means more consumers, not more producer connections.
- **Pick the delivery model.** One broker can do both point-to-point and publish-subscribe; in AWS those become two services, SQS for once-only processing and SNS for fan-out.
- **Protocols change** from connection-based AMQP, WebSockets or OpenWire to HTTPS API calls.
- **Ordering versus scale.** FIFO queues preserve order; standard queues give best-effort ordering and scale much further.
- **Payload size.** The default limit is 1 MB, but AWS's extended client libraries for Java and Python store the body in S3 and pass a pointer, allowing up to 2 GB.
- **Identity and audit.** IAM replaces the LDAP setup you might still need for RabbitMQ on Amazon MQ, and CloudTrail can log data requests per message.

## Who should watch

Teams sizing up a broker migration who want the trade-offs laid out plainly, and developers who know RabbitMQ and want to see how SQS semantics map onto it. Messaging veterans will find the first half familiar; the client-code comparison and the refactor checklist are the parts worth the time.

## Related Conf42 talks

- [Julien Jakubowski on choosing between RabbitMQ, Kafka and Pulsar](https://www.conf42.com/DevOps_2024_Julien_Jakubowski_right_messaging_platform_rabbitmq) at Conf42 DevOps 2024.
- [Natan Silnitsky on migrating to multi-cluster managed Kafka with zero downtime](https://www.conf42.com/Cloud_Native_2022_Natan_Silnitsky_migrating_multi_cluster_managed_kafka_0_downtime) at Conf42 Cloud Native 2022.
- [Srikar Kompella on serverless SaaS migration on AWS with Go](https://www.conf42.com/Golang_2025_Srikar_Kompella_serverless_migration_aws) at Conf42 Golang 2025.

[Watch Ran Tao's talk](https://www.conf42.com/Cloud_Native_2026_Ran_Tao_data_analytics_insights)

[Watch the talk on YouTube](https://youtu.be/20IWxo9vC6M).

## Watch the talk

[Migration from On-Prem Messaging System to The Cloud: What, How and Why](https://www.conf42.com/Cloud_Native_2026_Ran_Tao_data_analytics_insights) at Conf42 Cloud Native 2026.
