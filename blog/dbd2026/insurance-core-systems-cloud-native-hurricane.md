# Insurance cores have to survive the claims spike after a hurricane

Conf42 Blog, 2026-05-16, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/insurance-core-systems-cloud-native-hurricane

In short: Sulabh Jain at Conf42 Database DevOps 2026 on decoupling insurance core systems with per-domain data, Kubernetes, IaC, events and a four-phase roadmap.

A hurricane or wildfire turns a quiet claims system into a queue overnight, and a monolith on bigger servers cannot stretch to meet it. At Conf42 Database DevOps 2026, Sulabh Jain, a Business Applications Supervisor working on insurance platforms, laid out how to move insurance core systems to cloud-native architecture, with the database decisions front and centre.

It is a broad, well-structured modernization talk: domain decomposition, Kubernetes, infrastructure as code, CI/CD, events, APIs, observability and data consistency, finished with a phased roadmap. None of the patterns are new, but seeing them mapped onto policy, claims and billing makes the case unusually concrete.

## Three pressures at once

Sulabh frames the urgency as compounding forces. Regulation: audit trails must be precise and available on demand, and change windows are shrinking, so a platform that is slow to change becomes a legal liability as well as a technical one. Competition: insurtechs built cloud-native from day one ship in days, not quarters. And catastrophe scale: a claims spike that the monolith cannot absorb becomes a backlog at the worst possible moment for customers.

All three trace back to tight coupling. A small fix to claims adjudication triggers a full regression cycle; a new underwriting rule needs a coordinated release across application, database and integration layers.

## Each service owns its data, or none of this works

The core move is data ownership. A policy service owns the policy lifecycle; a claims service owns everything from first notice of loss to settlement and scales out during a catastrophe without touching billing or underwriting; a billing service handles premiums and reconciliation, so a billing outage blocks neither policies nor claims. Share a database instead and one slow query degrades everything, one schema change breaks someone else. His warning lands well: a shared database is how a microservice migration quietly becomes a distributed monolith.

On Kubernetes he picks the capabilities that matter for insurance: horizontal pod autoscaling for claims spikes, pod disruption budgets for zero-downtime maintenance, namespaces as hard boundaries between regulated and non-regulated workloads, rolling deploys with automatic rollback, plus multi-zone clusters and StatefulSets with persistent volume claims for database pods.

## Make the audit trail a side effect

Infrastructure as code gets four stages: define networks, clusters, databases and IAM in Terraform, Pulumi or CloudFormation next to the app; review through pull requests with policy-as-code checks from OPA or Checkov; apply through CI/CD with drift tracking and rollback as a code revert; audit through Git history, so a regulator's request for the full change history is already answered. Disaster recovery becomes a drill, not a crisis.

The CI/CD pipeline adds functional tests of underwriting rules and premium calculations on every commit, synthetic load tests that simulate catastrophe-level claims volume, SAST, DAST and image scanning, and progressive delivery with automatic rollback.

## Synchronous fraud checks are the outage waiting to happen

The best example in the talk: claims intake calls fraud detection synchronously, fraud detection slows under catastrophe load, every claim waits, mobile apps time out, and one slow service takes the platform down. With events, intake publishes "claim received" and fraud scoring, adjuster assignment and notifications consume it at their own pace. Kafka suits ordered, durable claims event sourcing; EventBridge fits serverless partner routing. Event sourcing, CQRS, dead letter queues, sagas and circuit breakers round out the toolkit, with the outbox pattern bridging database writes and the event stream.

Schema changes follow expand and contract, consumer-driven contract tests, blue-green migrations for large tables, and a schema registry on Kafka topics. Partner APIs are designed spec-first in OpenAPI with versioning and deprecation timelines, secured at a gateway with OAuth 2.0 or mutual TLS.

## Foundation before decomposition

The roadmap is a strangler fig in four phases: containerize, build CI/CD, IaC and observability with no refactoring; extract high-pain domains such as claims and billing and introduce event streaming; add a service mesh, GitOps and API contracts; then tune autoscaling for catastrophes and implement SLOs. Each phase ships working software, and the whole thing is a multi-year program. His closing point is that upskilling and team ownership are prerequisites, not soft extras.

## Who should watch

Architects and engineering leads planning an insurance (or any regulated, spiky-load) core modernization who need a sequence they can defend to the business. Engineers already running event-sourced microservices will mostly find confirmation.

## Related Conf42 talks

- [Pravesh Nikhare on insurance rules processing](https://www.conf42.com/Cloud_Native_2025_Pravesh_Nikhare_insurance_rules_processing) at Conf42 Cloud Native 2025.
- [Dmitry Khorev on the saga pattern for distributed transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) at Conf42 Cloud Native 2023.
- [JJ Asghar on the stumbling blocks of migrating a monolith to cloud native](https://www.conf42.com/Site_Reliability_Engineering_2021_JJ_Asghar_migrating_monolith_cloudnative_stumbling_blocks) at Conf42 Site Reliability Engineering 2021.

[Watch Sulabh Jain's talk](https://www.conf42.com/Database_DevOps_2026_Sulabh_Jain_kafka_streams_k8s)

[Watch the talk on YouTube](https://youtu.be/ICxBDSlkd3M).

## Watch the talk

[Cloud-Native Core Systems: Database & DevOps for Insurance](https://www.conf42.com/Database_DevOps_2026_Sulabh_Jain_kafka_streams_k8s) at Conf42 Database DevOps 2026.
