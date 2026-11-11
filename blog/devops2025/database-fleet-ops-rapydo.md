# Your app autoscales a thousandfold, your database does not

Conf42 Blog, 2025-01-23, updated 2026-11-09. https://www.conf42.com/blog/devops2025/database-fleet-ops-rapydo

In short: Matan Nataf of Rapydo at Conf42 DevOps 2025 on managing fleets of MySQL and Postgres databases, with a live demo of throttling a runaway query.

Kubernetes and autoscaling groups let your application scale out on demand, but the relational database behind it is still one shared-everything box. At Conf42 DevOps 2025, Matan Nataf, co-founder and CEO of Rapydo, argued that the tooling for running relational databases in the cloud has not kept up with microservices and multi-tenant architectures, and demoed how Rapydo tackles it.

Rapydo was a gold sponsor of the event, and this is a product talk: roughly half framing, half live demo of the Rapydo console. The framing is useful for anyone running more than a handful of MySQL or Postgres instances.

## From a few databases to thousands

Matan's history lesson is short. On-prem, a company ran a small fleet of databases for a few monolithic apps, with a full DBA team watching them. Load changed by modest percentages, so sizing for the peak was neither hard nor expensive.

Microservices changed that. Teams ship features daily, often on open-source MySQL and Postgres, and the fleet can grow to thousands of instances. Per-instance tools such as Amazon RDS Performance Insights show one database at a time, and with a fleet of 5,000 databases, he points out, looking at one instance at a time makes you reactive by definition.

He also names the uncomfortable part of the ops job: even when you find the bad query, the fix usually lives in legacy code owned by a development team, so all you can do is file it with them and wait.

## Three pillars: observability, resiliency, sane costs

Matan's spec for a modern database management tool has three legs, and he says missing any one of them fails:

- **Fleet-wide observability.** The slowest queries, top CPU and IO consumers, connection shortages, and locks and deadlocks across all instances in one view, with alerts on thresholds.
- **Resiliency without code changes.** Guardrails that protect the database from CPU spikes, runaway queries, repeated identical queries from buggy code, and idle connections eating the pool.
- **Sane costs.** Capacity planning that does not have to assume the worst spike, since he notes managed databases are often the second or third line on a cloud bill.

Rapydo maps onto that with two parts deployed in your own VPC: Scout for observability across Postgres and MySQL, and Cortex, an automation layer that works through a proxy and managed connections to apply caching, throttling, and query rewrites.

## The demo: a query that keeps coming back

The live demo is the best part. The master dashboard shows a 48-hour view of slow queries, top CPU consumers, and locks across the fleet. Grouping the lock view shows the single Postgres instance suffering most, and that two statements, one update and one select, generate most of the locks.

Then the real-time view: a MySQL 8 demo database at 100% CPU with all 250 of its 250 connections in use. Going back 15 minutes shows the same `SQL_CALC_FOUND_ROWS` query running four times in parallel, then 112, then 230, and 237 when he returns to the live view.

Matan kills the query, and the application immediately sends it again, which is the honest moment of the talk: killing queries is a fire extinguisher, not a fix. He considers a cache rule with table-based invalidation, which keeps cached data consistent with the table, then rejects it because the query uses the current date. Instead he applies a throttling rule, with a wildcard on the `LIMIT` clause, that lets that query run only two at a time. The parallel count falls from 75 to 46 to 2, and the database recovers while the app keeps sending the query.

## Who should watch

DevOps and SRE teams who own a large fleet of MySQL or Postgres databases but not the application code hitting them. The framing helps you argue for fleet-level tooling; the demo shows what intervening at the proxy layer looks like. If you run three databases and a DBA, it will feel like someone else's problem, for now.

More database talks from Conf42:

- [Adam Furmanek on observability for PostgreSQL and MySQL](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql) at Conf42 DevOps 2024.
- [Lukas Vileikis on lessons from MySQL records](https://www.conf42.com/Platform_Engineering_2024_Lukas_Vileikis_mysql_records_lessons) at Conf42 Platform Engineering 2024.

[Watch Matan Nataf's talk](https://www.conf42.com/DevOps_2025_Matan_Nataf_db_ops_rapydo), part of [Conf42 DevOps 2025](https://www.conf42.com/devops2025).

## From Rapydo

Rapydo offers database observability and automation for fleets of MySQL and PostgreSQL databases, deployed in the customer's VPC, with Scout for visibility and Cortex for caching, throttling, and query rewrite rules.

- [Rapydo website](https://www.rapydo.io/)

[Watch the talk on YouTube](https://youtu.be/xvFDiSRfGBY).

## Watch the talk

[Revolutionizing DB OPS with Rapydo](https://www.conf42.com/DevOps_2025_Matan_Nataf_db_ops_rapydo) at Conf42 DevOps 2025.
