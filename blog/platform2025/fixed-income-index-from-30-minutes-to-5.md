# A fixed-income index system goes from 30-minute runs to under 5

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/fixed-income-index-from-30-minutes-to-5

In short: Tarun Chataraju (JPMorganChase) at Conf42 Platform Engineering 2025 on moving a monolithic index system to Kubernetes, Airflow and Kafka.

Monthly index rebalancing used to mean a maintenance window during which clients couldn't see their data. At Conf42 Platform Engineering 2025, Tarun Chataraju, Senior Lead Software Engineer at JPMorganChase, described how his team moved a legacy fixed-income index system to Kubernetes, Apache Airflow and Kafka, cutting calculation time by 88% (from 30 minutes or more to under five) and removing scheduled downtime altogether.

## The monolith was failing on three fronts

The legacy system was one code base, deployed by hand, scaled by buying bigger boxes and run as nightly batches. Rebalancing needed ever longer windows, which hurt SLAs. Data volumes grew five times in three years. Index calculations took 30 minutes or more at peak, when clients wanted near real-time numbers, and quarter-end reporting or a volatile market day could swamp it. Tarun's point is that this was a business problem, touching client satisfaction and revenue, not just an IT one.

## Kubernetes is the engine, Airflow the conductor

The new architecture splits responsibilities cleanly. "Think of Kubernetes as the engine and airflow as the conductor, making sure the orchestra plays in the right order."

Airflow runs the index workflow as a DAG: pull issuer and bond metadata from providers such as Bloomberg through stateless, containerised adapters; collect real-time and end-of-day prices with data quality checks before anything proceeds; trigger calculation pods; generate reports and validations; publish to APIs and downstream consumers. Every step is visible, retriable and auditable, and if pricing data fails, calculations pause until it's corrected. At month-end the calculation engine scales out to around 30 pods, then back down overnight.

Around that sit domain-driven services (pricing logic decoupled from reporting), time-series databases tuned for financial tick data, REST and GraphQL APIs with compliance masking of restricted securities at the API layer, and a service mesh for traffic control, encryption and tracing.

## Kafka and Redis absorb the spikes

Kafka decouples processing so spikes queue gracefully and state survives a node failure; in one stress test it handled three times the expected peak without dropping a message. Redis cut database reads by 90%, with cross-region replication. StatefulSets, network policies for regulatory boundaries and horizontal pod autoscaling let the system handle 20 times more concurrent calculations on volatile days.

## The migration was strangled, not switched

The part worth stealing is the migration plan. Phase one built cloud infrastructure with compliance, IaC, CI/CD and monitoring baked in. Phase two moved historical data with dual writes and a validation framework that checked every bond reference record and price across old and new systems. Phase three peeled services off the monolith with the strangler pattern, with Airflow orchestrating across both worlds while reference data still lived in the legacy database and calculations had moved to Kubernetes. Phase four cut over with blue-green deployments and ran both systems in parallel until the team trusted the new one. Clients never saw a disruption; the system just got faster.

Tarun also credits the organisational side: a platform team acting as an internal service provider, a self-service portal for databases and dev environments, internal tech talks and runbooks. Custom product time to market dropped by 70%.

## Who should watch

Anyone modernising a batch-heavy system in a regulated industry, especially if Airflow is already on your shortlist. The next steps he lists (ML anomaly detection on market data, streaming DAGs for intraday triggers) show where the design goes next.

## Related Conf42 talks

- [Orchestrating data and ML workflows with Apache Airflow](https://www.conf42.com/Machine_Learning_2023_Tamara_Janina_Fingerlin_orchestrating_workflows_apache_airflow) by Tamara Janina Fingerlin (Astronomer), an Airflow primer from the people who build it.
- [Kube-Native ETL at Scale: Optimizing PySpark + Airflow Workflows in Cloud-Native Environments](https://www.conf42.com/Kube_Native_2025_Sruthi_Erra_Hareram_etl_airflow_optimization) by Sruthi Erra Hareram (TELUS Digital), the same pairing tuned for data workloads.

[Watch Tarun Chataraju's talk](https://www.conf42.com/Platform_Engineering_2025_Tarun_Chataraju_modernizing_fixed_index)

[Watch the talk on YouTube](https://youtu.be/7snFR5YT5aM).

## Watch the talk

[Cloud-Native Platform Engineering: Modernizing Fixed-Income Index Systems](https://www.conf42.com/Platform_Engineering_2025_Tarun_Chataraju_modernizing_fixed_index) at Conf42 Platform Engineering 2025.
