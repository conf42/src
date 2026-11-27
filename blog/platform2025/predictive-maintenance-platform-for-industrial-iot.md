# Predictive maintenance is a platform problem before it's a model

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/predictive-maintenance-platform-for-industrial-iot

In short: Muruga Angamuthu of Techtonic Industries at Conf42 Platform Engineering 2025 on cloud-native platforms for industrial IoT predictive maintenance.

A model that predicts a bearing failure is worthless if the sensor data never reaches it. At Conf42 Platform Engineering 2025, Muruga Angamuthu, BI manager and data and analytics architect at Techtonic Industries, laid out the cloud-native platform that sits under AI-driven predictive maintenance for factories, drawing on 23 years in data engineering, BI and manufacturing.

His thesis: data scientists should focus on the model, not the plumbing, and platform engineers are the ones who build the plumbing.

## From fix-it-when-it-breaks to eight days' notice

Muruga walks the maintenance ladder: reactive (fix after failure, pay for unplanned downtime), scheduled (often too early or too late), condition-based (better, still no foresight), and AI-driven predictive maintenance. The figures he cites for the last rung are 8 to 12 days of advance warning with around 90% prediction accuracy, and implementations reporting roughly half the downtime they had before.

Getting there, he notes, takes infrastructure plus organisational change, technical and cultural.

## Four architecture choices that decide the rest

The patterns are sensible and battle-worn:

- **Multi-tier processing**: edge devices for fast local decisions, cloud for heavy analysis, hybrid where you need both.
- **Event-driven architecture**: handle data as events happen so sudden surges from many sensors don't queue up.
- **Kubernetes auto-scaling** for peak loads.
- **Tiered storage**: hot storage for real-time access, cold storage for history used in training.

Then the layers: ingestion over industrial protocols such as OPC UA, MQTT and Modbus, streamed through Kafka or Pulsar; time-series databases and data lakes such as Snowflake and Databricks; ML orchestration with Kubeflow or MLflow and a feature store; and GraphQL and REST APIs feeding dashboards and alerts. Loose coupling is the rule, so each layer can change without dragging the others along.

## The edge needs its own checklist

The edge computing section is the most practical. Handling critical alerts locally is much faster, sending only important data saves bandwidth, and the plant keeps working when connectivity drops. The platform engineer's list: deploy models onto devices with little memory, update them remotely without a truck roll, use mutual authentication, and keep data consistent between edge and cloud over unreliable links. Anyone who has tried to OTA-update a gateway on a factory floor will nod along.

## Case study and roadmap

His case study is a global manufacturer with 37 facilities and 12 equipment vendors. The platform used a hybrid AWS and Azure architecture, Snowflake analytics, Kubeflow pipelines and custom adapters for the vendor mix. Reported results: 42% less downtime, $4.3 million in annual savings, a 93% model deployment success rate and a 2.5x productivity gain for the data science team.

The roadmap is phased: foundations (connectivity, basic pipelines, governance) over three to four months, ML deployment over two to three, scale and optimise with edge integration over four to six, then ongoing expansion as an internal platform service. Start with one high-ROI use case and grow from there.

## Who should watch

Platform and data engineers in manufacturing, energy or any asset-heavy business, and MLOps folks who have only ever deployed models to clean cloud APIs. It is an architecture overview with a full ML lifecycle (collect, process, train, validate against real failures, deploy, monitor for drift), not a code walkthrough.

## Related Conf42 talks

- [Akshat Kapoor on real-time analytics in IIoT](https://www.conf42.com/Internet_of_Things_IoT_2024_Akshat_Kapoor_analytics_iiot) covers the decision layer on the same data.
- [Indika Wimalasuriya on AIOps in AWS for predictive maintenance](https://www.conf42.com/Incident_Management_2024_Indika_Wimalasuriya_17_aiops_aws_maintenance) compares managed options.
- [Mohan Kumar Dalai on AI maintenance platforms for power plants](https://www.conf42.com/Platform_Engineering_2026_Mohan_Kumar_Dalai_maintenance_power_plant) applies the idea to energy.

[Watch Muruga Angamuthu's talk](https://www.conf42.com/Platform_Engineering_2025_Muruga_Angamuthu_industrial_iot_maintenance)

[Watch the talk on YouTube](https://youtu.be/VvaDixj9MYU).

## Watch the talk

[Building Scalable AI/ML Platforms for Industrial IoT: A Cloud-Native Approach to Predictive Maintenance Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Muruga_Angamuthu_industrial_iot_maintenance) at Conf42 Platform Engineering 2025.
