# Self-tuning databases have to earn trust before they act

Conf42 Blog, 2026-05-08, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/self-tuning-databases-earn-trust-first

In short: Naga Bellamkonda of Gartner at Conf42 Database DevOps 2026 on AI-driven database tuning in finance, e-commerce and healthcare, and the failures that shaped it.

A bad deployment starts degrading a database within minutes; a human tuning it works on a timescale of hours or days. At Conf42 Database DevOps 2026, Naga Bellamkonda, Senior Database Administrator at Gartner with 15 to 16 years across Oracle, Postgres, Aurora, Redshift and MySQL, made the case for AI-driven tuning, and spent most of the talk on how to roll it out without the automation becoming the incident.

That second part is why the talk is worth your time. Plenty of people pitch self-optimizing databases; fewer describe the three ways theirs went wrong.

## Monitoring alerts, self-tuning acts

Naga's definition is simple: a self-tuning system does more than alert, it changes things. The scope covers continuous workload analysis, automatic index creation and removal from observed access patterns, execution plan selection refined from historical workloads, dynamic memory and compute allocation, and automated patching with audit trails. The engine runs a loop of observe, recommend, adopt and test, and that feedback loop is what he says separates real self-optimization from sophisticated alerting.

## Three sectors, three different entry points

The talk draws on deployments in three industries, and each started somewhere different:

- **Finance**: execution plan regressions after releases caused intermittent transaction failures that were found only after users were hit. The fix was AI-driven query plan monitoring inside the CI/CD pipeline, catching regressions within seconds of deployment and rolling back to the stable configuration.
- **E-commerce**: static overprovisioning was expensive and reactive scaling too slow for promotional spikes. Models trained on past promotions, fed by the marketing events pipeline, allocated resources before the traffic arrived.
- **Healthcare**: every configuration change needed an auditable approval trail, so automation started as recommendations in a review dashboard. Only low-risk, reversible changes were automated later, with full audit logging.

## The failures are the best part

Naga names three that reshaped the approach. Model staleness: a large application refactor shifted query patterns faster than the model adapted, and degraded recommendations went unnoticed for nearly two weeks. Transfer limits: a model trained in one environment did not port cleanly to a similar client and needed weeks of fine-tuning. And integration: wiring the AI engine into existing CI/CD and change management consistently took longer than building the models. Sophistication without operational integration, he concludes, delivers nothing.

## If you can't roll it back, don't automate it

Automated indexing is high value and high risk, so the guardrails matter more than the model. Recommendations are first tested in shadow against replayed production traffic. Every change is tagged with the model version and workload context that produced it. One-click rollback is in the pipeline from day one. Write performance and lock contention are watched right after each index change. Everything lands in the same dashboards teams already use for deployments, with the rationale, model version, shadow results, timestamp and observed impact, which then feeds back into training.

His rollout plan has four stages: instrument and baseline with no automated action; recommendations with humans approving everything; automation of a bounded set of reversible actions; then gradual expansion, with schema changes and irreversible actions still needing a human. The DBA instinct shows through: take a Data Pump export or physical copy on Oracle, a snapshot on AWS, before any data change.

## Who should watch

DBAs and platform teams being asked to "add AI" to database operations, and anyone who has to sell automation to a change advisory board. It is a lessons-learned talk rather than a demo of the open-source toolkit the abstract mentions, so come for the rollout discipline, not the code.

## Related Conf42 talks

- [Stefano Doni on ML-driven automated performance tuning](https://www.conf42.com/Site_Reliability_Engineering_2021_Stefano_Doni_MLdriven_automated_performance_tuning) at Conf42 Site Reliability Engineering 2021.
- [Adam Furmanek on database guardrails](https://www.conf42.com/JavaScript_2023_Adam_Furmanek_database_guardrails) at Conf42 JavaScript 2023.
- [Eyal Trabelsi on debugging SQL queries](https://www.conf42.com/Observability_2023_Eyal_Trabelsi_debug_sql_queries) at Conf42 Observability 2023.

[Watch Naga Bellamkonda's talk](https://www.conf42.com/Database_DevOps_2026_Naga_Bellamkonda_alerts_incident_platform)

[Watch the talk on YouTube](https://youtu.be/ru5AFziYRrg).

## Watch the talk

[AI-Driven Database Tuning in DevOps: Real-World Lessons from Self-Optimizing Systems](https://www.conf42.com/Database_DevOps_2026_Naga_Bellamkonda_alerts_incident_platform) at Conf42 Database DevOps 2026.
