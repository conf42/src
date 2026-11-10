# In regulated finance, ML deploys wait on the database schema

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/ledger-to-lake-database-devops-for-ml

In short: Alejandro Mercado at Conf42 MLOps 2026 on tying every model deploy to a versioned BigQuery schema change with Liquibase and Harness CI.

In a regulated bank, the thing slowing your model deploys is often not the model. It is the database change ticket. At Conf42 MLOps 2026 on November 19, Alejandro Mercado, DevOps and Cloud Architect, tells a tale from the trenches about closing that gap: every model deployment linked to a versioned, verified schema change, using Google BigQuery, Liquibase and Harness CI.

## The Data DevOps gap

Alejandro's diagnosis is specific. In regulated financial institutions, ML deployment is bottlenecked by rigid database change management and audit requirements more than by algorithms. Traditional MLOps pipelines version code and models carefully, then treat the database underneath as somebody else's problem.

The result is a familiar set of failures: schema drift, failed deployments and compliance risk whenever model features depend on database structures that keep evolving. A feature pipeline that expects a column to exist is a contract with the schema, and in many shops nobody wrote that contract down.

## Schema as code, with the same rigour as models

The architecture puts Liquibase in charge of BigQuery schema versioning as code. Database migrations get treated with the same rigour as model artifacts: versioned, reviewed, and tied to the release that needs them.

That symmetry is the useful idea. If your model registry can tell you exactly which weights are in production but nobody can say which schema version those weights were trained against, you have half a lineage.

## Harness CI runs the handoff

Harness CI orchestrates the sequence between database migration and model deployment. The key piece is a set of automated verification gates that prevent schema-model mismatches, so a model cannot ship against a schema it was not built for, and a migration cannot quietly pull a column out from under a running model.

Worth noting for context: Harness is a Conf42 sponsor, but this is a practitioner talk about one team's pipeline, and Harness CI is one of three tools in the stack.

## The war story

The session includes a candid look at a critical failure in which a silent schema change threatened production model integrity, and how the new pipeline catches that class of error before it reaches production. Silent is the operative word. Schema changes that break things loudly get fixed fast. The ones that change meaning without changing shape are the ones that slowly poison a model.

## The outcome

Alejandro reports that the team cut deployment cycles from weeks to hours while reaching 100% audit compliance for database changes, in a highly regulated environment. Those are the talk's own numbers; the interesting part will be how the gates and approvals were designed so that speed and audit did not end up fighting each other.

## Who should watch

MLOps engineers, data platform leads and DevOps practitioners who sit between database operations and the ML lifecycle in an enterprise. Especially anyone in finance, insurance or another audited industry, where "just run the migration" is never the whole sentence. If your models only read from a feature store that someone else owns, you may still want to forward this to that someone.

## Related Conf42 talks

- [Schema Migrations in CI/CD: When AI Helps, When It Hurts, and How to Tell the Difference](https://www.conf42.com/Database_DevOps_2026_Ahmed_Tariq_postgres_mysql_scaling) by Ahmed Tariq, schema migrations in pipelines.
- [Database DevOps: CD for Stateful Applications](https://www.conf42.com/Database_DevOps_2026_Stephen_Atwell_cd_stateful_applications) by Stephen Atwell, continuous delivery when state is involved.
- [Prompt-Driven Microservice & Database Evolution: Using LLMs for Automated Schema Migration and DevOps Delivery](https://www.conf42.com/Database_DevOps_2026_Niraj_Katkamwar_llm_agents_delivery) by Niraj Katkamwar, the LLM-assisted angle on schema change.

[Watch Alejandro Mercado's talk](https://www.conf42.com/MLOps_2026_Alejandro_Mercado_bigquery_liquibase_harness) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Ledger to Lake: Automating Database DevOps for ML in Finance with BigQuery, Liquibase, and Harness CI](https://www.conf42.com/MLOps_2026_Alejandro_Mercado_bigquery_liquibase_harness) at Conf42 MLOps 2026.
