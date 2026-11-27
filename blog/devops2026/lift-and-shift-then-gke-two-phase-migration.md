# Lift and shift first, then Kubernetes, so you change one thing at a time

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/lift-and-shift-then-gke-two-phase-migration

In short: Google staff SRE Harris Baskaran at Conf42 DevOps 2026 on moving a ticketing monolith from VMware and Oracle to GCE, then GKE and PostgreSQL.

Change your infrastructure, your runtime and your database in one go, and when latency jumps you will not know whether to blame the network, a pod limit or a rewritten stored procedure. At Conf42 DevOps 2026, Harris Baskaran, a staff SRE at Google, made the case for doing it in two phases, using the migration of a two-decade-old ticketing monolith that handles more than a hundred thousand tickets a day: first lift and shift onto Google Compute Engine, then rebuild cloud-native on GKE with PostgreSQL.

It is a grounded case study, including the parts they would do differently.

## Phase one buys a baseline

The starting point: a tightly coupled monolith on ageing VMware with a very large Oracle database, globally deployed, untouched for about a decade, where even patching was risky. Phase one moved it to GCE as is, to exit VMware quickly and, more importantly, to measure how the unchanged app behaves in the cloud before adding containers.

Four steps made that safe. Dependency mapping with discovery tools on the network, not just the code (he notes how many zombie services and undocumented API calls a ten-year-old monolith hides). A parallel cloud environment that mirrored production. Continuous replication with Oracle's native tooling, so the data was already there at cutover. And a cutover by DNS and load balancer redirects that took minutes, with an easy fallback.

The measured latency, throughput and resource utilisation then became the bar phase two had to meet or beat.

## The database was the real migration

Phase two moved the workload to GKE and the data from Oracle to Cloud SQL for PostgreSQL. Baskaran calls the database the hardest hurdle: rewriting custom PL/SQL packages, time zone conversions, character sets and data types, kept in sync with change data capture, and many rounds of performance tuning and load testing. Terraform made it cheap to spin up a full load-test environment and tear it down again.

## Zero trust replaces the perimeter

On-prem security was a hard perimeter. On GKE it became layers: Workload Identity instead of long-lived service account keys, so pods get short-lived rotated tokens; network policies across more than 200 distinct communication paths, started loose and tightened as traffic was observed, with default deny; image scanning and Binary Authorization in the build; and automated mTLS plus customer-managed encryption keys. The phase-one dependency map is what made those fine-grained policies possible.

## DR went from recovery to resilience

Legacy DR meant manual backups and recovery times measured in hours or days, rarely tested. Phase one brought automated persistent disk snapshots; phase two brought multi-region deployment and Backup for GKE. Before go-live, the team ran Google's "wheels of misfortune" exercises to test RTO and RPO for real. His line on untested DR plans: a system only theoretically ready for disaster is a liability.

## What they would change

Two honest regrets. Start the schema simplification for Postgres much earlier, even during phase one. And add distributed tracing to the monolith before the lift and shift, not after; it would have made latency jitter far easier to find.

## Who should watch

SREs and platform teams with a big, old, business-critical system and a mandate to modernise it. His four takeaways work as a checklist: map dependencies, measure baselines, plan for database complexity, test DR.

## Related Conf42 talks

- [Chris Engelbert on the dos and don'ts of PostgreSQL on Kubernetes](https://www.conf42.com/Internet_of_Things_IoT_2024_Chris_Engelbert_kubernetes_postgresql_cluster) at Conf42 IoT 2024.
- [Richard Lees and Jorge Alvarez on monolith-to-microservices modernisation with AWS App2Container](https://www.conf42.com/Cloud_Native_2024_Richard_Lees_Jorge_Alvarez_monolith_microservice_modernization) at Conf42 Cloud Native 2024, the same journey on another cloud.
- [Rajkumar Chindanuru on strategies for modernising legacy applications](https://www.conf42.com/Golang_2025_Rajkumar_Chindanuru_legacy_modernization_strategies) at Conf42 Golang 2025.

[Watch Harris Baskaran's talk](https://www.conf42.com/DevOps_2026_Harris_Baskaran_kubernetes_modernization_containers)

[Watch the talk on YouTube](https://youtu.be/NKsyUwfwtsI).

## Watch the talk

[From Lift-and-Shift to Kubernetes: A Two-Phase DevOps Modernization](https://www.conf42.com/DevOps_2026_Harris_Baskaran_kubernetes_modernization_containers) at Conf42 DevOps 2026.
