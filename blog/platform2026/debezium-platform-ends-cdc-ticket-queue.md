# Debezium Platform turns CDC from a ticket queue into self-service

Conf42 Blog, 2026-10-15, updated 2026-11-09. https://www.conf42.com/blog/platform2026/debezium-platform-ends-cdc-ticket-queue

In short: Vincenzo Santonastaso (IBM, Debezium maintainer) at Conf42 Platform Engineering 2026 on scaling change data capture across teams with Debezium Platform.

The first change data capture pipeline is a win. The twentieth is a queue of tickets in front of the platform team. At Conf42 Platform Engineering 2026, Vincenzo Santonastaso, Senior Software Engineer at IBM and a core maintainer of Debezium, argued that once CDC is popular, the hard part stops being CDC and becomes everything around it, and showed how Debezium Platform moves that work to self-service.

Honest scope up front: this is a talk by a Debezium maintainer about Debezium's own platform, with a live demo. It's open source, and the pitch is about operating model as much as tooling.

## Why one team ends up owning everyone's pipelines

Vincenzo starts with a quick baseline (batch vs streaming, Lambda architecture, the streamhouse) and lands on log-based CDC: read the database's transaction log (binlog, WAL, redo log) instead of re-scanning tables, so you ship only the rows that changed with little load on the source. Debezium does this across MySQL, Postgres, Oracle, SQL Server, MongoDB, Db2, Cassandra and more, with one event format and offsets that let a restart resume exactly where it left off.

Then the catch. Shipping even one pipeline means knowing snapshots, offsets, schema changes, replication slots, permissions, dozens of connector properties, converters and SMTs, plus deployment, monitoring and upgrades. Nobody wants every product team to learn that, so the knowledge concentrates in the platform team. That works, until every team that wants a pipeline routes through the same few people who review configs, deploy connectors and answer tickets. The people waiting get slower; the platform team gets tired.

## Raise the abstraction, keep the knobs

Debezium Platform's answer is to stop passing around raw connector JSON. The platform team defines reusable building blocks: sources, destinations and transformations. A pipeline is a combination of those, with room left for tuning. In Vincenzo's words, that is what turns a pile of configuration into a product.

The roles shift with it. Platform engineers own the building blocks and the guardrails. Data engineers create and manage their own pipelines from the UI or the CLI. The platform deploys and runs them and shows health, status, logs and metrics for every pipeline in one console, rather than everybody grepping logs across clusters.

## The demo: one database, three very different consumers

The demo is the bit worth the watch. One Postgres inventory database, three teams:

- Analytics wants clean rows upserted into a separate warehouse database via JDBC.
- Integration wants row-change events pushed to an external HTTP endpoint as webhooks.
- A third team wants current product and stock state in Redis.

Each pipeline gets its own replication slot, so they're independent. Under the hood: Debezium Platform installed with Helm on a local Kind cluster, a UI called Stage, a control plane and REST API called Conductor, and the Debezium operator, which deploys a dedicated Debezium Server pod per pipeline. There's no Kafka or Kafka Connect anywhere in the demo, which will surprise anyone who thinks of Debezium as a Kafka Connect plugin. Metrics flow through an OpenTelemetry Collector into Prometheus and back into the UI's dashboards.

Vincenzo builds the three pipelines in a few clicks, shows that every connector property in the forms carries its documentation inline, and then checks the webhook receiver, Redis and the warehouse tables. All three got their data. Demo gods appeased.

## Who should watch

Platform teams already running Debezium on Kafka Connect who have become the CDC help desk, and data platform leads deciding how to offer CDC to many teams without a ticket per pipeline. If you've never touched CDC, the first third is a decent primer. If you want deep internals on snapshotting or schema evolution, this stays at the operating-model level.

## Related Conf42 talks

- [Event-Driven Change Data Capture pattern using Apache Pulsar](https://www.conf42.com/Cloud_Native_2023_Mary_Grygleski_eventdriven_data_capture_pattern_apache_pulsar) by Mary Grygleski (DataStax)
- [Building Self-Service Data Platforms: Engineering Scalable ETL Infrastructure for Developer Experience](https://www.conf42.com/Platform_Engineering_2025_Batchu_Krishna_etl_service_experience) by Batchu Krishna (Fidelity Investments)
- [Event-driven applications: Apache Kafka and Python](https://www.conf42.com/Python_2021_Francesco_Tisiot_Apache_Kafka_event_driven_applications_streaming_platform_data_streamin) by Francesco Tisiot (Aiven)

[Watch Vincenzo's talk](https://www.conf42.com/Platform_Engineering_2026_Vincenzo_Santonastaso_pipelines_data_teams)

[Watch the talk on YouTube](https://youtu.be/99KHmdg2Kgc).

## Watch the talk

[Beyond the First Pipeline: Scaling Data Pipelines Across Teams](https://www.conf42.com/Platform_Engineering_2026_Vincenzo_Santonastaso_pipelines_data_teams) at Conf42 Platform Engineering 2026.
