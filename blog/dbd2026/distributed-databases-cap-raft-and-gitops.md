# Distributed databases, from CAP trade-offs to GitOps rollouts

Conf42 Blog, 2026-06-01, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/distributed-databases-cap-raft-and-gitops

In short: Srikanth Uddanti (Charles Schwab) at Conf42 Database DevOps 2026 on replication, sharding, Raft vs Paxos, automation and zero trust for database clusters.

Picking a distributed database starts with deciding what you're willing to lose when the network splits. At Conf42 Database DevOps 2026, Srikanth Uddanti, Senior Manager of Software Development and Engineering at Charles Schwab, where he runs multi-terabyte database clusters, walks through the fundamentals behind modern distributed databases and the DevOps and security practices that keep them running.

This is a good first talk on the subject: a structured tour from the CAP theorem to mutual TLS, with MongoDB as the recurring example. Engineers who already operate Cassandra or CockroachDB in anger will know most of it.

## Why monoliths run out of road

Srikanth frames three limits of the monolithic database. It scales vertically but not horizontally, which makes it a single point of failure. Global distribution brings latency and consistency problems across regions. And applications handling millions of transactions a day hit a throughput ceiling on a vertically scaled box.

## CAP, as a design decision

He uses the CAP theorem as the base for everything else: consistency, availability and partition tolerance, pick two. Traditional relational databases sit on consistency and availability; the horizontally scaled NoSQL systems he names, MongoDB, DynamoDB and Cassandra, are built to tolerate partitions. His practical framing of consistency: with a replication factor of two, a write isn't acknowledged to the user until it has been written twice.

## Three replication models, three sharding schemes

The replication section compares single leader, multi-leader and leaderless designs. Single leader, which MongoDB uses, sends all writes to a primary. It's simple, but it's a bottleneck, and writes not yet replicated when the primary dies are lost; you have to handle that edge case. Multi-leader enables geo-distributed writes at the price of conflict resolution. Leaderless accepts reads and writes on any node with quorums, maximising availability but needing careful quorum tuning.

For sharding: range-based keeps contiguous keys together (his example is querying people aged one to twenty), hash-based spreads load evenly (Amazon order IDs looked up from anywhere), and directory-based uses a lookup table, which is flexible but turns the table into a critical dependency.

## Raft is the one you can explain to on-call

On consensus, he walks through Raft leader election using MongoDB, where operators can set election priority and geography, followed by oplog replication to secondaries in the same or different zones, then commit and apply. Paxos, used in multi-master designs, is mathematically proven and flexible but harder to implement, and needs Multi-Paxos for practical log replication.

## Automate the cluster like any other infrastructure

The DevOps section treats database infrastructure as versioned, declarative code: Terraform or Pulumi to provision, Ansible and Helm charts to configure and enforce tuning parameters, and GitOps pipelines for schema migrations, rolling upgrades and canary rollouts with automated rollback gates. His deployment pattern is zone isolation: do maintenance one zone per region at a time, prove it works, and touch the other zones on a different day. Automated runbooks, he argues, shorten MTTR compared to manual response and remove the toil.

## Zero trust inside the cluster

Security comes in three parts: mutual TLS between clients and the database and between nodes; identity-based, least-privilege access so an application can read or write only the tables it needs; and audit logging of every admin action and schema change for root cause analysis. Certificates need lifecycle management (he mentions Venafi), and keys belong in a key management system or secrets manager.

His closing advice is to start from the use case: work out whether you need strong consistency or high availability, align it with your business SLAs, then automate and secure everything around that choice.

## Who should watch

Engineers new to running distributed databases, or DBAs moving from a single relational primary to a sharded cluster, who want the vocabulary in one sitting.

## Related Conf42 talks

- [Modern Database Architectures: From SQL to NoSQL and Distributed SQL](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Andrei_Manakov_tradeoffs_distributed_nosql) by Andrei Manakov, the same trade-offs with distributed SQL in the mix.
- [Building a K8s Operator for a Distributed Database](https://www.conf42.com/Cloud_Native_2021_Natalie_Pistunovich_k8s_operator_distributed_database) by Natalie Pistunovich, for automating cluster operations on Kubernetes.
- [Building Highly Available Databases with Cloud Native Reliability Practices](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Rajesh_Kumar_Balusu_building_highly_available) by Rajesh Kumar Balusu, the availability side in more depth.

[Watch Srikanth Uddanti's talk](https://www.conf42.com/Database_DevOps_2026_Srikanth_Uddanti_distributed_systems_delivery)

[Watch the talk on YouTube](https://youtu.be/fc3KjkIWdD4).

## Watch the talk

[Modern Distributed Databases: Architecture, DevOps, and Operational Trade-offs](https://www.conf42.com/Database_DevOps_2026_Srikanth_Uddanti_distributed_systems_delivery) at Conf42 Database DevOps 2026.
