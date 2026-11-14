# Let AI review your schema migration, never approve it

Conf42 Blog, 2026-05-17, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/schema-migrations-ci-cd-ai-advises

In short: Ahmed Tariq at Conf42 Database DevOps 2026 on safe schema migrations in CI/CD, expand-migrate-contract, and a framework for where AI belongs.

The pipeline was green, the health checks passed, and production fell over anyway, because the migration behind the release locked a hot table. At Conf42 Database DevOps 2026, Ahmed Tariq, Cloud DevOps Engineer, gave a field guide to shipping schema changes safely through CI/CD and a simple rule for AI in that pipeline: it advises, a named engineer decides.

The talk is practical rather than flashy, and Ahmed says as much: the boring part is what you want for a production database. It also includes a worked example and a two-axis matrix you can take to your next architecture review.

## Code rolls back, data doesn't

Stateless deploys are built around reversibility: immutable artifacts, blue-green, canaries, feature flags. Migrations break that, because they mutate shared persistent state. Ahmed's one line to remember: "You can roll back the code, you cannot always roll back the customer data being wrong". Point-in-time recovery and spare replicas help, but cost money and can still miss things.

His failure modes will look familiar to anyone who has been paged for one: locking DDL on a hot table that fills the connection pool, rollbacks that cannot restore a dropped column or undo a destructive backfill, environment drift (ten thousand rows in staging, four hundred million in production), big-bang changes that couple new code to the new schema, and the worst one, silent data loss from a type conversion that truncates values while the migration reports success.

## Six stages, and only one of them is a human

A good migration pipeline in Ahmed's version: lint the SQL for unsafe type changes, missing indexes and destructive operations; dry run against a production-sized clone to measure duration and locking; test the application against the new schema with both old and new code paths; approval gate with a human reviewer; deploy in a controlled way, not a manual command from someone's terminal at 11pm; then post-deploy checks of data and flows. Flyway, Liquibase or GitHub Actions all work, because the operating model matters more than the tool. Automate the mechanical checks; save the human for judgement.

## Expand, migrate, contract, in that order

The worked example adds a `customer_status` column to a table with hundreds of millions of rows and several dependent services. The unsafe version adds the column, backfills everything at once, ships dependent code and drops the old field quickly to look tidy. The safe version: add a nullable column with no default and check lock behaviour for your engine (Postgres, MySQL and SQL Server differ); dual-write old and new fields; backfill in rate-limited batches while watching replication lag; switch reads behind a feature flag, so rollback is a flag flip rather than a data revert; verify with observability; and only then drop the old field. A safe migration is a safe sequence, not a safe statement.

Observability is part of the release plan: baseline latency, replication lag, error rate, CPU and connections before, watch lock waits and p95 and p99 latency during (averages hide the pain), and let it cool down before declaring victory.

## Where AI helps and where it hurts

AI earns its keep on review prep: flagging risky type changes, likely locks and unclear rollbacks, summarizing a dense pull request into a plain risk brief, generating edge-case tests for nulls and historical rows, drafting runbooks, and summarizing timelines after an incident. The abstract's example of the failure side is a good one: hallucinated syntax such as "Postgres flags that are actually MySQL flags". The model also cannot see your traffic, data volume or which table is billing, and it can confidently suggest a rollback that makes things worse. Confident but wrong, Ahmed says, is worse than silence. The hard line: no auto-approve or auto-apply in production, because accountability cannot be delegated to a tool.

## Score every migration on two axes

The decision framework asks about blast radius, reversibility and whether business context is needed. Low risk and easy to reverse: automation with AI assistance is fine. High risk but reversible: staged rollout plus human approval. Low risk but hard to reverse: AI drafts or reviews, an engineer owns it. High risk and hard to reverse: human-led, rehearsed, explicitly approved, heavily observed. His first step for teams starting out: add a migration linter and dry-run risky migrations on production-like data.

## Who should watch

Backend and platform engineers who ship migrations through CI/CD and are being handed AI review tools. It is a good primer for less experienced engineers, and a useful checklist for the senior ones writing the team's migration policy.

## Related Conf42 talks

- [Rotem Tamir on reliable database schema migrations](https://www.conf42.com/Kube_Native_2024_Rotem_Tamir_database_schema_reliable_migrations) at Conf42 Kube Native 2024.
- [Saikrishna Ala's playbook for zero-downtime migrations](https://www.conf42.com/Platform_Engineering_2026_Saikrishna_Ala_migrations_downtime_playbook) at Conf42 Platform Engineering 2026.
- [Adam Furmanek on the missing database chapter of the CI playbook](https://www.conf42.com/Observability_2023_Adam_Furmanek_missing_chapter_ci_playbook_database) at Conf42 Observability 2023.

[Watch Ahmed Tariq's talk](https://www.conf42.com/Database_DevOps_2026_Ahmed_Tariq_postgres_mysql_scaling)

[Watch the talk on YouTube](https://youtu.be/dFUmB4zZnp4).

## Watch the talk

[Schema Migrations in CI/CD: When AI Helps, When It Hurts, and How to Tell the Difference](https://www.conf42.com/Database_DevOps_2026_Ahmed_Tariq_postgres_mysql_scaling) at Conf42 Database DevOps 2026.
