# CloudNativePG fails over in 11 seconds, but misses replication lag

Conf42 Blog, 2026-05-18, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/kubernetes-operator-vs-dba-cloudnativepg

In short: Amarachi Iheanacho of Sidero Labs at Conf42 Database DevOps 2026 broke a CloudNativePG Postgres cluster six ways to test whether an operator can replace a DBA.

Kill the primary Postgres pod and CloudNativePG promotes a replica and rebuilds the cluster in about eleven seconds. Pause replication on a replica and it reports the cluster healthy while the replica falls more than 100 MB behind. At Conf42 Database DevOps 2026, Amarachi Iheanacho, technical writer and developer advocate at Sidero Labs, ran six failure scenarios against an operator-managed Postgres cluster to answer one question: can a Kubernetes operator replace a DBA?

Her answer is the useful kind of nuanced: it replaces the routine execution, not the judgement. And because every scenario is shown with real `kubectl` output, you can see exactly where the line falls.

## No SSH allowed

The setup makes the test honest. Four nodes on AWS (one control plane, three workers) running Talos Linux, an immutable OS managed by Omni, so there is no SSH into nodes and no sneaky human fix. Kubernetes 1.35, CloudNativePG, Postgres 16 with three instances. The plan was 30 days; AWS bills shortened it to roughly 16 to 20, a constraint every homelab reader will sympathize with.

## What the operator did well

**Primary pod deleted.** CloudNativePG detected it almost immediately, promoted the most up-to-date replica, repointed the service so writes went to the new primary, and created a fresh pod. Eleven seconds, back to three of three healthy, no human. That is exactly what a DBA would do by hand (check WAL replay positions, promote, fix routing, provision a standby), only faster.

**Major version upgrade.** Patching the image from Postgres 16.13 to 17.6 triggered a coordinated shutdown, an upgrade job, the primary back on 17 in about 47 seconds, and two fresh replicas cloned from it. Amarachi notes a DBA would still plan a window, rehearse on staging and take a full backup first.

## Where it needed a human

**Node drain.** Failover worked, but the evicted replica sat in Pending for about 26 minutes. Its PersistentVolumeClaim was bound to local storage on the cordoned node, so no other node could take it. Uncordoning brought it back within the minute. A DBA would have checked storage topology and switched over deliberately before draining. Verdict: partial.

**Disk filling up.** She wrote 8.4 GB of junk to the primary (64% utilization), then about 4 GB more toward 90%. Between those points the operator said nothing. At 90% the primary crashed, failover kicked in, Kubernetes tainted the node with DiskPressure, and the replacement pod stayed Pending, with no SSH to clean up. A DBA would have had alerts at 70, 80 and 90% and a runbook. Point to the human.

**Replication lag.** With WAL replay paused on one replica and a million rows written to the primary, the replica fell about 102 MB behind while the cluster status stayed healthy, with no event or alert. Resuming replay caught it up immediately. The lesson is the clearest in the talk: the operator sees pod health, not Postgres-level replication state.

**Backup and point-in-time recovery.** A base backup to S3 via Barman finished in eight seconds. Recovery failed: WAL archiving had not been configured at cluster creation, nothing enforced it, and the recovery pod restart-looped for about an hour looking for WAL segments that were never archived. A DBA configures WAL archiving on day one and tests recovery before trusting it.

## The DBA's job moves, it doesn't vanish

The scorecard is honest: pod failover, upgrades, replica cloning and self-healing after pod failures are automated well. Storage topology, replication lag monitoring, disk-full recovery on an immutable OS, and backup architecture still need a person, or at least monitoring that a person configured. Amarachi calls it the beta of the experiment, with more to come.

## Who should watch

Platform teams deciding whether to run Postgres on Kubernetes with an operator, and DBAs asked to hand theirs over. Even if you have run CloudNativePG for years, the drain and PITR scenarios are a good checklist for your own setup. Bring your own Prometheus alerts for lag and disk.

## Related Conf42 talks

- [Chris Engelbert on running a PostgreSQL cluster on Kubernetes](https://www.conf42.com/Internet_of_Things_IoT_2024_Chris_Engelbert_kubernetes_postgresql_cluster) at Conf42 Internet of Things 2024.
- [Jan Karremans on databases on Kubernetes](https://www.conf42.com/Cloud_Native_2024_Jan_Karremans_databases_kubernetes) at Conf42 Cloud Native 2024.
- [Natalie Pistunovich on a Kubernetes operator for a distributed database](https://www.conf42.com/Cloud_Native_2021_Natalie_Pistunovich_k8s_operator_distributed_database) at Conf42 Cloud Native 2021.

[Watch Amarachi Iheanacho's talk](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning)

[Watch the talk on YouTube](https://youtu.be/8IkNVlfrt9I).

## Watch the talk

[Can a Kubernetes Operator Replace a DBA? A 30-Day Experiment](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning) at Conf42 Database DevOps 2026.
