# Set RTO, RPO and SLOs before you migrate a single database

Conf42 Blog, 2026-02-23, updated 2026-11-09. https://www.conf42.com/blog/sre2026/database-ha-starts-with-rto-and-rpo

In short: Rajesh Kumar Balusu of AGAP Technologies at Conf42 SRE 2026 on database high availability via SLO-first planning, Kubernetes self-healing and the 6 Rs of migration.

Databases are often the last mile of availability: the application tier can be redundant three times over and a single standalone database node still decides your uptime. At Conf42 Site Reliability Engineering 2026, Rajesh Kumar Balusu, Database Architect at AGAP Technologies, laid out a three-phase approach to highly available databases, and his first rule is simple: define the reliability targets before touching the architecture.

Balusu brings 20 years of database engineering and cloud architecture across Oracle Cloud Infrastructure, AWS and Google Cloud, much of it spent on migrations from on-premises data centres for public sector, university, retail and pharmaceutical customers. The talk is a structured checklist built from that experience.

## Targets come from the business, not from hope

Phase one is assessment and planning. Before any change, an SRE team should pin down four numbers: an uptime SLO (five nines leaves roughly five minutes of downtime a year), a recovery time objective for how long a restore may take, a recovery point objective for how much data you can afford to lose, and P99 query latency targets for reads and writes. His point is that every later decision, from replication mode to backup frequency, should trace back to these.

Then comes the infrastructure review, which is where the hidden single points of failure live: standalone database nodes, single-region deployments, storage nobody meters. He adds aging components (end-of-support software and hardware), workload saturation (CPU spikes, memory pressure, IOPS ceilings) and security gaps such as unencrypted connections, overprivileged service accounts and missing audit logs. Most of these surface only during an incident, which is an expensive way to do an audit.

Capacity planning should be driven by metrics rather than instinct: utilisation trends, peak transaction rates and concurrency, storage growth and IOPS headroom, connection pool saturation. The goal is reliability headroom without paying for idle capacity. Traffic control uses battle-tested tools: NGINX for layer 7 load balancing, health checks and read-replica routing, HAProxy for TCP-level proxying and active-passive failover.

## Kubernetes as an SRE tool, not a developer convenience

Phase two maps cloud native practices onto reliability outcomes. Immutable container images remove environment drift between development, QA and production. Kubernetes liveness probes detect pod failures and restart automatically, cutting MTTR. HPA and KEDA scale replicas on CPU, memory or custom signals such as queue depth. CI/CD pipelines carry quality gates and rollback triggers tied to error-rate breaches. He measures it all against the DORA metrics: deployment frequency, mean time to recovery and change failure rate.

## The 6 Rs stop you refactoring everything

Phase three is migration, using the 6 Rs: rehost (lift and shift), replatform (for example moving to managed RDS or Aurora), repurchase (move to a SaaS database), refactor (microservices, event sourcing, CQRS), retain (stay on-premises where latency, compliance or cost justify it) and retire (decommission databases nobody uses, which also shrinks the attack surface). His takeaway: not every database needs refactoring, and picking the right path protects stability.

Execution means mapping every upstream and downstream consumer before touching a schema or a connection string, costing compute, storage, egress, licensing and operations rather than just instance prices, and tuning and right-sizing after the move.

## HA you haven't tested is a rumour

The high availability principles are the classics, stated plainly: multi-zone or multi-region replicas, health-check-driven automatic failover, synchronous replication where you need zero RPO and asynchronous for distribution and scale, and regular chaos experiments and failover drills. His final takeaway is the one to tape to the runbook: HA must be tested, not assumed.

## Who should watch

This is a broad, methodical overview rather than a close look at one engine. It suits teams planning a database migration to the cloud, SREs inheriting database ownership, and anyone who needs a checklist to run an infrastructure review. Experienced DBAs will recognise most of it, and may still find the 6 Rs framing handy for the next "should we rewrite it?" meeting.

## Related Conf42 talks

- [Can a Kubernetes Operator Replace a DBA? A 30-Day Experiment](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning) by Amarachi Iheanacho.
- [Recovery Without Reintroducing Risk: A Security-First Approach to RTO/RPO in Event-Driven Systems](https://www.conf42.com/DevSecOps_2026_Sanjay_Iyer_recovery_eventdriven_rto) by Sanjay Iyer.
- [Just don't do it - Databases in Kubernetes](https://www.conf42.com/Cloud_Native_2024_Jan_Karremans_databases_kubernetes) by Jan Karremans.

[Watch Rajesh Kumar Balusu's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Rajesh_Kumar_Balusu_building_highly_available) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/9Z-WcRFPA2Y).

## Watch the talk

[Building Highly Available Databases with Cloud Native Reliability Practices](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Rajesh_Kumar_Balusu_building_highly_available) at Conf42 Site Reliability Engineering (SRE) 2026.
