# Self-service ETL platforms generate the DAGs so developers don't

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/self-service-etl-platforms-from-metadata

In short: Batchu Krishna (Fidelity Investments) at Conf42 Platform Engineering 2025 on metadata-driven ETL, generated Airflow DAGs and GitOps for data platforms.

Most developers who need a data pipeline don't want to write an Airflow DAG by hand, and a good platform shouldn't make them. At Conf42 Platform Engineering 2025, Batchu Krishna, a Software Engineer at Fidelity Investments with around two decades of data migration and ETL work behind him (banking projects included), described how to turn traditional ETL operations into a self-service data platform: metadata-driven pipelines, generated DAGs, infrastructure as code and the guardrails enterprises need.

## ETL as a product, not a ticket queue

Batchu frames platform engineering as a shift from managing infrastructure to building internal products. A data platform should feel natural to application developers: it plugs into the CI/CD they already use and follows patterns they already know. It also has to handle enterprise-scale processing, large legacy migrations and live transaction volumes while staying simple enough for general-purpose developers. Done well, that removes the handoffs where one team waits for the next to finish its stage.

## Declare the pipeline, let the platform write it

The central idea is metadata-driven ETL. Instead of imperative code per pipeline, pipelines are defined as structured metadata describing the transformations, the data quality requirements and operational parameters such as how to handle bulk loads or real-time feeds. At runtime the platform interprets that metadata and generates the workflows.

He grounds it in a familiar Azure layout from earlier projects: data moves from sources into a landing zone, then integration, then curated, with a pipeline and transformation step at each hop. In a metadata-driven platform those hops are described rather than hand-built, and Airflow DAGs are generated from the definitions so users never write Python DAG code directly. The payoff is maintainability: the definitions focus on business requirements, not implementation details, which removes a whole class of implementation errors.

The architecture underneath is microservices on Kubernetes with Apache Airflow as the orchestration backbone. The hard part, in his words, is hiding Kubernetes complexity from users while still giving them access to its scheduling and resource management, without handing permissions to people who shouldn't have them.

## The rest of the stack is software engineering applied to data

The supporting practices will look familiar:

- **CI/CD for pipelines:** version control, automated tests on pre-loaded test data, staged deployments with approvals, and rollback to the previous version when a release misbehaves.
- **Cloud integration:** templates over Azure Data Factory, careful cluster, notebook and job management for Databricks, and REST or GraphQL APIs with consistent error handling.
- **Infrastructure as code:** Terraform modules and Helm charts, with GitOps through Argo CD or Flux giving an audit trail and approval workflow.
- **Data testing at four levels:** generated test data, integration tests in containers, schema compatibility checks and performance regression against a baseline.
- **Observability:** distributed tracing with Jaeger or Zipkin, metrics in InfluxDB, logs in Elasticsearch or Splunk, and ML-based anomaly alerting.

Governance closes the list: automatic lineage capture, RBAC tied to enterprise identity, audit logs of every action, and privacy controls for GDPR and CCPA such as classification and deletion.

## Who should watch

Engineers moving an ETL team from hand-built jobs to a platform model, especially on Azure and Airflow. The delivery is conversational and wide-ranging rather than tightly scripted; the metadata-to-DAG section is the part to watch closely.

## Related Conf42 talks

- [Demystifying Modern Data Pipeline Architecture: From Legacy ETL to Cloud-Native Streaming at Scale](https://www.conf42.com/Kube_Native_2025_Vamsi_Pulusu_datapipeline_streaming_modern) by Vamsi Pulusu (Ford Motor Company), the streaming end of the same migration.
- [4 Tricks That Help You Leverage Your Airflow Pipelines](https://www.conf42.com/DevOps_2024_Aliaksandr_Sheliutsin_leverage_airflow_pipelines) by Aliaksandr Sheliutsin, practical Airflow habits.
- [How to use common Python frameworks to test Apache Airflow data pipelines](https://www.conf42.com/Python_2024_Tamara_Janina_Fingerlin_frameworks_apache_airflow_pipelines) by Tamara Janina Fingerlin (Astronomer), for the testing layer.

[Watch Batchu Krishna's talk](https://www.conf42.com/Platform_Engineering_2025_Batchu_Krishna_etl_service_experience)

[Watch the talk on YouTube](https://youtu.be/F0qacyTSkYs).

## Watch the talk

[Building Self-Service Data Platforms: Engineering Scalable ETL Infrastructure for Developer Experience](https://www.conf42.com/Platform_Engineering_2025_Batchu_Krishna_etl_service_experience) at Conf42 Platform Engineering 2025.
