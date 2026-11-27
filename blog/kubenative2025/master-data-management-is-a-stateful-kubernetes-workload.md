# Master data management is a stateful Kubernetes workload

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/master-data-management-is-a-stateful-kubernetes-workload

In short: Rahul Ameria (Meta Platforms) at Conf42 Kube Native 2025 on rebuilding MDM as Kubernetes microservices with StatefulSets, Helm, GitOps and Kafka.

The fastest way to lose master data on Kubernetes is to treat it like a stateless web app. At Conf42 Kube Native 2025, Rahul Ameria, Data Analyst at Meta Platforms, walked through what cloud-native master data management (MDM) looks like when matching, merging, validation and governance each become their own containerised service, and which Kubernetes primitives keep the single source of truth from quietly forking.

It is an architecture overview, broad rather than deep, and useful as a map of the moving parts.

## Why MDM had to change

Traditional MDM systems, in Rahul's description, are heavyweight, stateful and slow to scale. That was tolerable when everything lived in one data centre. With hybrid and multi-cloud deployments and microservices that need customer, product, supplier and account data in real time, the old shape doesn't fit.

His key distinction: cloud-native MDM is a redesign of how data mastering works in distributed, elastic infrastructure, and containerising the legacy MDM product isn't the same thing. Each capability becomes a service with clear boundaries, declared in Kubernetes manifests, deployed through Helm and GitOps, and scaled by the Horizontal Pod Autoscaler when ingestion spikes.

## State is the whole game

The section on stateful workloads is the core of the talk. StatefulSets give the core MDM stores stable network identities and ordered deployment. Persistent volumes on cloud block storage (AWS EBS, Azure Disk, GCP persistent disk) mean data survives pod restarts. Consensus stores such as etcd or CockroachDB keep state consistent across nodes.

His pitfalls list makes the same point from the other direction. Stateless assumptions lead to data loss on restarts. Ignoring storage latency slows matching and merging under load. Underestimating service mesh overhead turns into a configuration nightmare later. Skipping observability makes debugging impossible while data quality degrades unnoticed. His advice on databases and consensus strategy: choose them up front, because changing them later is expensive refactoring.

## Governance rules belong in Git

The governance argument is the one regulated industries will like most. Match rules, survivorship rules and validation policies all go into version control, so every change has a history. CI/CD applies the manifests, cutting human error. If a governance update causes trouble, you roll back to a known good configuration.

Observability gets a specific treatment too. Prometheus exporters publish data-quality metrics such as validation throughput, matching latency and merge accuracy; Grafana dashboards show MDM health at a glance; Jaeger or OpenTelemetry trace a record across microservices. That turns MDM from a black box into something an on-call engineer can reason about.

## Integration and a retailer story

Rahul positions MDM as a hub: API gateways such as Kong or NGINX expose master data with rate limits and auth, Kafka or Pulsar stream raw data in and master updates out, adapters bridge mainframe and ERP systems, and dbt and Airflow feed warehouses. Security is zero trust with mutual TLS through the mesh, HashiCorp Vault for secrets, encryption in transit and at rest, and RBAC with audit logs for GDPR and CCPA.

He illustrates it with a global retailer whose legacy MDM downtime during seasonal peaks hurt order fulfilment. After moving to microservices on StatefulSets backed by block storage, with Kafka for ingestion, the talk reports 99.9% uptime through Black Friday, a 30% cost reduction from elastic scaling off-peak, and governance rule changes deployed via GitOps in minutes.

## Who should watch

Data platform and data governance teams weighing a move of MDM onto Kubernetes, and platform engineers who are about to be asked to host it. His first best practice is the right one: start with one domain, such as customer data, before expanding.

## Related Conf42 talks

- [From Analytics to Action: Re-Architecting MDM for Agentic Enterprise AI](https://www.conf42.com/AI_Agents_2026_Vishwak_Thatikonda_mdm_data_retail) asks what MDM must become when agents consume it.
- [AI-Driven Data Quality Management](https://www.conf42.com/Python_2025_Shashank_Reddy_Beeravelly_data_quality_management) covers automated quality checks in Python.
- [Breaking Data Silos](https://www.conf42.com/Cloud_Native_2025_Siddhartha_Parimi_data_silos_unification) takes the lakehouse route to a single source of truth.

[Watch Rahul Ameria's talk](https://www.conf42.com/Kube_Native_2025_Rahul_Ameria_mdm_quality_orchestration)

[Watch the talk on YouTube](https://youtu.be/l7N532UDDck).

## Watch the talk

[Cloud-Native MDM: Kubernetes Orchestration for Enterprise Data Quality at Scale](https://www.conf42.com/Kube_Native_2025_Rahul_Ameria_mdm_quality_orchestration) at Conf42 Kube Native 2025.
