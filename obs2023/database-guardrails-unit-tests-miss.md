# The database bugs your unit tests are built not to see

Conf42 Blog, 2023-06-08. https://www.conf42.com/obs2023/database-guardrails-unit-tests-miss

In short: Adam Furmanek (Metis) at Conf42 Observability 2023 on database guardrails in CI, using execution plans and OpenTelemetry to catch bad SQL before production.

A query that reads 300,000 rows to build a single user object passes every unit test you'll ever write, because your test database has 100 rows in it. At Conf42 Observability 2023, Adam Furmanek, DevRel at Metis, catalogued the database failures that slip through CI/CD and argued for database guardrails: checks that read execution plans and query traces during development, long before a load test or a Friday deploy.

The first two-thirds are a vendor-neutral tour of what goes wrong between application code and the SQL engine. The last part shows Metis, the product Adam works on.

## Why doesn't CI/CD catch this?

Adam splits deployment risk into three: getting the deployment itself wrong (missing IAM roles, connection strings, platform quirks such as line endings or Docker networking), code that fails in a new environment, and production data that looks nothing like test data in volume, distribution or encoding. Unit and integration tests check logic. "Your unit test will test your code and assume how it's going to work in your database," Adam Furmanek said at Conf42 Observability 2023. They know nothing about the indexes, statistics, configuration or extensions of the production database.

## What actually breaks?

The examples are the strongest part of the talk.

**The aggregate that ate the network.** An ORM loads a user aggregate root with its details eagerly, joining several tables. In a production system Adam debugged, the cross product meant about 300,000 rows came back, and the ORM spent around 25 seconds deduplicating them into one object. The fix was to split it into several queries and join in application code: more round trips, each one fast.

**Equivalent queries, different speeds.** On a boarding passes table of about 8 million rows, a query that hashes ticket numbers in a common table expression and joins it three times gives the same result as one that reads the table directly three times. The CTE version took 13 seconds, the other 8. Tests compare results, so they treat both as correct.

**Innocent schema changes.** Adding a column or changing its type can rewrite a large table, which takes minutes, not milliseconds. Dropping a column across a big fleet creates a split brain where half the machines still expect it. Several applications in different languages sharing one database all need updating together.

**Indexes, both ways.** A missing index makes reads slow; telling developers to index everything slows every write, since each modification updates every index.

**Engine semantics.** Adam recalls the Halloween problem, where an update raising salaries below 10,000 by 10% kept re-matching the same rows until everyone crossed the threshold, and notes that under read committed, often the default, a query may legally read a row twice or skip one.

**ORMs hide the rest.** N+1 selects (one query for all aircraft, then one per aircraft for its seats), where the lazy-versus-eager choice sits in configuration far from the code. Impedance mismatch: inheritance mapping, spatial types, string collation configured per database while the application has one string type, decimal precision squeezed into floats. Transaction scope, connection pooling and migrations that may fix schema drift on their own.

## So what's a database guardrail?

Context, captured early. Ask the database how it would execute the query your ORM generated: EXPLAIN gives a tree of nodes, each with a type and a cost, and shows which indexes it chose. Capture the queries themselves with OpenTelemetry, whose traces and spans follow a request from the web tier down to the SQL. Put the two together and you can judge a query's real behaviour while the developer is still writing it.

The alternative, load testing, gets short shrift. It costs time and money (GPUs, if the app is ML), needs realistic, anonymised, GDPR-compliant data, and runs at the end of the pipeline, hours or days after the code was written. "So load tests are expensive, are slow, and are way too late in our pipeline," Adam said.

## What did the Metis demo show?

An application with one OpenTelemetry-based dependency added: recent REST calls with their status codes, the SQL each generated behind the scenes, the execution plan (visualised or raw), and a direct verdict on whether it will hold up in production. In GitHub Actions, Metis comments on pull requests with analysis of queries and schema migrations. After deployment, a container running next to the database watches slow queries, anomalies, missing and unused indexes, dead rows and autovacuum, extensions and configuration.

## Who should watch

Backend developers who trust their ORM a little too much, and platform teams deciding where database checks belong in the pipeline. If you know the N+1 problem by heart, skip ahead to the schema and isolation-level sections.

Related talks: [Eyal Trabelsi on debugging SQL with execution plans](https://www.conf42.com/Observability_2023_Eyal_Trabelsi_debug_sql_queries) from the same event, [Rotem Tamir on reliable database schema migrations](https://www.conf42.com/Kube_Native_2024_Rotem_Tamir_database_schema_reliable_migrations), and [Hari Krishnan on shift-left performance testing](https://www.conf42.com/Site_Reliability_Engineering_2021_Hari_Krishnan_shift_left_performance_testing).

[Watch Adam Furmanek's talk](https://www.conf42.com/Observability_2023_Adam_Furmanek_missing_chapter_ci_playbook_database) from [Conf42 Observability 2023](https://www.conf42.com/obs2023).

## From Metis

In the talk, Metis covers three stages: query and execution-plan insight during development through an OpenTelemetry-based SDK, pull request analysis of queries and schema migrations in CI, and database monitoring in production through a container beside the database.

- Metis: [metisdata.io](https://www.metisdata.io/)

[Watch the talk on YouTube](https://youtu.be/LUmTXMGIkp0).

## Watch the talk

[The missing chapter in your CI playbook: database guardrails](https://www.conf42.com/Observability_2023_Adam_Furmanek_missing_chapter_ci_playbook_database) at Conf42 Observability 2023.
