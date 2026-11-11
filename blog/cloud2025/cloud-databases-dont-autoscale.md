# Everything in your stack autoscales except the database

Conf42 Blog, 2025-03-05. https://www.conf42.com/blog/cloud2025/cloud-databases-dont-autoscale

In short: Matan Nataf of Rapydo at Conf42 Cloud Native 2025 on why managing database fleets is broken, and a demo of throttling, blocking and caching queries.

In a cloud-native stack, the database is usually the one tier that doesn't scale out when a noisy neighbour shows up. At Conf42 Cloud Native 2025, [Matan Nataf](https://www.conf42.com/Cloud_Native_2025_Matan_Nataf_rapydo_databases_broken), co-founder of Rapydo, called databases "the stepson of every CloudOps organization" and argued that the way teams run fleets of RDS instances is broken: the people who write the queries aren't the people who get paged for them.

This is a vendor talk with a long live demo of the Rapydo console. The diagnosis in the first half is worth hearing even if you never install anything.

## Developers own the queries, CloudOps owns the consequences

Nataf's framing is organisational before it is technical. Managed services like RDS pushed database responsibility towards developers: they write the queries, pick the ORM, and often a single dev team owns a given database. Developers live in days and sprints, and their code has close to 100% of the impact on the database.

CloudOps and SRE teams live in minutes. They own the infrastructure bill, the database SLA, uptime and performance, and when queries run slow, the customer-facing team calls them. So one group causes the load and another absorbs it, usually without a DBA on the team. He calls that situation not healthy, which is a polite way to describe most on-call rotations that include a database.

## Observability alone leaves you reactive

The first problem with a fleet is visibility. Which instance has the slowest query? Where was the last CPU spike? Which databases are creeping towards the edge of their SLA? He acknowledges the existing observability tools for this, naming Datadog DBM, SolarWinds and New Relic, and argues that seeing the problem is only half the job. The other half is automation: caching queries, shielding the database from CPU spikes, accelerating slow queries and right-sizing the underlying instances.

His case for why it matters is the RDS scaling ladder. Hit a CPU spike, double the instance size, hit the ceiling again, double again. Scaling up is always a 100% step.

## The customer story: from emergency to shrinking instances

Nataf showed a CPU graph from a customer running a couple of hundred RDS instances that had climbed to 8xlarge one emergency at a time. After inserting Rapydo with a few rules, he said, the CPU baseline dropped from 60-100% to 20-30%, and the team then shrank instances step by step until they were 75% smaller than on day one, still below 50% CPU. He put the customer's compute savings at more than half a million dollars a month. Those are the vendor's numbers from a single customer, so treat them as a story, not a benchmark.

## The demo: from bird's-eye view to the offending query

The live part follows one workflow. A master dashboard ranks average query time across the fleet, MySQL and PostgreSQL side by side. Drill into the slowest instance and you find a `SELECT SQL_CALC_FOUND_ROWS` running for 333 seconds. A locks view groups by locking thread and points to a single `UPDATE` causing most of the locks across the fleet.

Then he switches to real time on a database pinned at 100% CPU, with a view that refreshes every three seconds and can scroll back to watch the problem compound, from a handful of concurrent executions to around fifty. Killing the query helps for a minute, then the application sends it again. That is the moment for rules.

## Rules: block, throttle, or cache

Rapydo's rule engine matches query patterns with wildcards and applies an action. You can block a pattern outright, restrict it to certain hours or weekdays so an analytics query only runs at night, or throttle it so only a couple of executions run in parallel. In the demo, the throttle brings the database back from the edge. A second rule caches a query with table-based invalidation: when someone writes to the underlying table, the cache entry is dropped so results stay coherent. Other rules cover database connections and limiting specific users or tenants, which is where the noisy-neighbour problem from the opening gets its answer.

## Who should watch

CloudOps and SRE teams responsible for many MySQL or PostgreSQL instances without a dedicated DBA, especially in multi-tenant SaaS. If your scaling strategy for RDS is "next instance size up", the rule-based throttling and caching ideas are worth knowing whatever tool you use.

## Related Conf42 talks

- [Effective Observability in PostgreSQL, MySQL, and Other SQL Databases](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql) by Adam Furmanek (Metis) at Conf42 DevOps 2024.
- [From Metrics Tsunami to Actionable Insights: Simplifying Database Troubleshooting](https://www.conf42.com/Observability_2024_Divine_Odazie_metrics_tsunami_troubleshooting) by Divine Odazie (Severalnines) at Conf42 Observability 2024.
- [Billions of Records in MySQL: Lessons Learned](https://www.conf42.com/Platform_Engineering_2024_Lukas_Vileikis_mysql_records_lessons) by Lukas Vileikis at Conf42 Platform Engineering 2024.

[Watch Matan Nataf's talk](https://www.conf42.com/Cloud_Native_2025_Matan_Nataf_rapydo_databases_broken) or the [YouTube recording](https://youtu.be/J5wbOyQwjVM).

## From Rapydo

Rapydo.io was a Gold sponsor of Conf42 Cloud Native 2025. The product in the talk is the Rapydo platform for observing and automating fleets of MySQL and PostgreSQL databases, including its rule engine for blocking, throttling and caching queries.

- [Rapydo.io](https://www.rapydo.io/): the database operations platform shown in the demo
- [All Conf42 Cloud Native 2025 talks](https://www.conf42.com/cloud2025)

## Watch the talk

[Managing Databases in the Cloud is BROKEN!](https://www.conf42.com/Cloud_Native_2025_Matan_Nataf_rapydo_databases_broken) at Conf42 Cloud Native 2025.
