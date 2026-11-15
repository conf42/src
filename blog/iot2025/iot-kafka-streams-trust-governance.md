# Taming IoT streams on Kafka starts with trusting the data

Conf42 Blog, 2025-12-09, updated 2026-11-09. https://www.conf42.com/blog/iot2025/iot-kafka-streams-trust-governance

In short: Rehmat Kharal of Conduktor at Conf42 IoT 2025 on why IoT streaming data is hard to trust and how governance, quality gates and self-service tame Kafka.

The hard part of IoT streaming is not moving the bytes; it is knowing whether you can believe them. At Conf42 Internet of Things (IoT) 2025, Rehmat Kharal of Conduktor laid out three hidden challenges of IoT data pipelines, unreliable sensors, device heterogeneity and data provenance, and the governance controls a Kafka platform needs to keep them from turning into outages.

Honest scope: Rehmat works at Conduktor, which builds a control plane for Kafka, and the second half describes that kind of tooling. The talk does not do a product demo, though, and the problem framing applies whatever you run.

## Bad data rolls downhill

Sensors produce noisy, inaccurate or irrelevant readings because of temperature swings, vibration, hardware limits or plain malfunction. Because one device's data feeds many business applications, the damage multiplies.

Her manufacturing example sticks: robotic arms placing windows, painting and fitting tyres on cars. If the window count reported upstream is off by a factor of ten, the other robots, procurement, shipping and the exchange with the manufacturer all inherit the error. Calibration drift becomes a supply chain problem. Missing data and packet loss from flaky connectivity do the same thing, leaving an incomplete picture that can end in production halts or quality and safety issues. She poses the uncomfortable question for teams that moved off legacy ETL: which is worse, data that gets stuck, or data that flows fast and is wrong?

## Heterogeneity and provenance

The second challenge is making very different devices cooperate without the least capable one becoming the bottleneck. That means standard interfaces and protocols, assigning work to the right processor, and coping with uneven performance, power constraints and a larger attack surface. Integrating many sources also brings schema mismatches and inconsistent data.

The third is provenance. As companies spread across regions, languages, deployment types and entry points, it gets harder to establish a chain of custody: who gathered the data, when and where, which servers and systems touched it, who transformed it, and who touched it last. In regulated environments, that is what audits and liability hinge on.

## Guardrails at the source, not after the incident

The remedy is a single view across the whole streaming estate: topics, schemas, consumer groups and Kafka Connect in one place, with labels and metadata so resources are discoverable, and real-time cluster and broker monitoring. Developers get self-service tooling so they can build, test and debug against Kafka without being Kafka experts.

The security controls she lists are concrete: fine-grained role-based access integrated with SSO and LDAP or Active Directory, immutable exportable audit logs, end-to-end message encryption including field-level and schema-based encryption, and dynamic data masking so sensitive fields are visible only to authorized users.

Data quality is enforced before data lands: quality gates, mandatory schemas and validation rules, with non-compliant messages blocked at the producer. An enterprise catalog makes streams, topics and schemas searchable, supports sharing with partners and tracks usage for chargeback.

Cluster protection rounds it out. Topic creation and changes go through a governed approval workflow, and topics can be renamed without breaking producers or consumers. Producer policies require valid schemas and rate-limit runaway producers; consumer group policies limit membership, join rates and offset commits so one misbehaving consumer cannot destabilize the cluster. The aim is moving Kafka operations from firefighting to prevention.

## Who should watch

Platform engineers who run Kafka for teams ingesting device data, and data owners who have to vouch for that data in an audit. If your Kafka estate is one cluster and one team, the governance half may feel early; the sensor reliability half will not.

## More from Conf42

- [Muralidhar Basani on simplifying Kafka governance for developers](https://www.conf42.com/DevSecOps_2023_Muralidhar_Basani_simplifying_kafka_governance) at Conf42 DevSecOps 2023.
- [Abhishek Walia on observability-first Kafka at scale](https://www.conf42.com/Observability_2025_Abhishek_Walia_kafka_visibility_scale) at Conf42 Observability 2025.
- [Natan Silnitsky on migrating to multi-cluster managed Kafka with zero downtime](https://www.conf42.com/Cloud_Native_2022_Natan_Silnitsky_migrating_multi_cluster_managed_kafka_0_downtime) at Conf42 Cloud Native 2022.

[Watch Rehmat Kharal's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Rehmat_Kharal_streaming_scalability_governance) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/C1mQs9s88FA).

## Watch the talk

[Taming IoT Data Streams: Lessons in Managing Scale, Complexity, and Trust](https://www.conf42.com/Internet_of_Things_IoT_2025_Rehmat_Kharal_streaming_scalability_governance) at Conf42 Internet of Things (IoT) 2025.
