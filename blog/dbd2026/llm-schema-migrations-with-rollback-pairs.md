# LLM-generated schema migrations, shipped with their own rollback

Conf42 Blog, 2026-05-20, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/llm-schema-migrations-with-rollback-pairs

In short: Niraj Katkamwar (Intuit) at Conf42 Database DevOps 2026 on a prompt-driven pipeline that generates code, migrations and rollbacks together, gated by humans.

The scariest file in most repos is a hand-written down migration nobody has ever run. At Conf42 Database DevOps 2026, Niraj Katkamwar, Software Engineer at Intuit, presented independent research on a prompt-driven framework where an LLM turns a plain-English requirement into service code, API contracts, schema migrations and tests in one go, and where every forward migration is generated alongside its inverse.

It's a short, architecture-level talk. There's no live demo and no benchmark, so treat it as a design to borrow from rather than a product to install.

## Schema drift is a coordination bug

Niraj frames the problem as four failures that feed each other: application and database changes drift out of sync and break contracts between services; engineers still handcraft migrations, API updates and rollback scripts; business intent gets lost between stakeholders, developers and data engineers; and unvalidated schema changes pushed into distributed systems end in outages, data loss or rollbacks that don't work.

His answer moves the engineer's job from writing boilerplate to reviewing and approving generated artifacts.

## Three layers, and the first one is allowed to stop

The framework runs in sequence. Layer one interprets the prompt: the LLM extracts entities, relationships, constraints and the change type (add, modify or delete). The interesting part is ambiguity detection. Underspecified or conflicting requirements are flagged and the pipeline pauses for a human instead of guessing. Consistency checks then compare the change against the existing schema registry and cross-service contracts.

Layer two uses coding agents to generate the API contracts with versioning, data access code, scaffolded service logic and integration tests for happy paths and edge cases.

Layer three is where he spends the most care: database-aware schema transformation. Generated migrations must keep existing API contracts and consumer expectations working across service versions. Destructive operations such as column drops and type changes are blocked unless a human explicitly approves them.

## The rollback is written before you need it

The idea worth stealing even if you never let an LLM near your DDL: atomic artifact pairs. Each forward migration is generated together with its inverse, version-pinned and stored next to it, so rollback is a planned and tested action. Niraj notes that coding agents are particularly good at writing these compensation scripts, which is the part humans most often skip.

Two more mechanisms complete the safety story. The expand/contract pattern is enforced, so additive changes ship first and destructive ones only after consumers have adopted the new schema. And failed health checks after a deploy trigger the pre-generated rollback automatically, without someone hunting for a script during the incident.

## One pipeline for code and schema

He calls running application code and schema changes through separate, uncoordinated pipelines the most dangerous pattern in database DevOps. In his flow, a prompt produces all artifacts atomically. They then pass a four-layer validation pyramid: syntax parsing and linting, semantic checks against the schema registry, a dry run of the migration against a shadow database clone, and auto-generated integration tests in CI. Any failure halts the pipeline and returns structured feedback to the engineer.

Integration is meant to be incremental: a CLI and REST API to drop into Jenkins, GitHub Actions or GitLab, and compatibility with schema registries such as Confluent Schema Registry and AWS Glue. Approval gates sit at every layer. In his words, LLMs accelerate generation, but engineers still own the decision to promote to production.

## Who should watch

Platform and data engineers wondering where LLM code generation can safely touch the database. If your team already runs expand/contract migrations with tested rollbacks, the architecture will feel familiar, and the value is in seeing where the human gates go. If your rollback strategy is "restore from backup", the atomic pair idea alone justifies the time.

## Related Conf42 talks

- [Strategies for Reliable Database Schema Migrations](https://www.conf42.com/Kube_Native_2024_Rotem_Tamir_database_schema_reliable_migrations) by Rotem Tamir, the non-LLM foundations of safe migrations.
- [Ledger to Lake: Automating Database DevOps for ML in Finance with BigQuery, Liquibase, and Harness CI](https://www.conf42.com/MLOps_2026_Alejandro_Mercado_bigquery_liquibase_harness) by Alejandro Mercado, migrations as code in a regulated pipeline.
- [Automating Database Operations with Cortex Code](https://www.conf42.com/Large_Language_Models_LLMs_2026_Tim_Spann_sql_automation_operations) by Tim Spann, another angle on AI writing database work.

[Watch Niraj Katkamwar's talk](https://www.conf42.com/Database_DevOps_2026_Niraj_Katkamwar_llm_agents_delivery)

[Watch the talk on YouTube](https://youtu.be/n7xbZUjdKxw).

## Watch the talk

[Prompt-Driven Microservice & Database Evolution: Using LLMs for Automated Schema Migration and DevOps Delivery](https://www.conf42.com/Database_DevOps_2026_Niraj_Katkamwar_llm_agents_delivery) at Conf42 Database DevOps 2026.
