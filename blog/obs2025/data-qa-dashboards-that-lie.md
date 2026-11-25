# Your dashboards are lying, and your pipeline tests are why

Conf42 Blog, 2025-05-21, updated 2026-11-09. https://www.conf42.com/blog/obs2025/data-qa-dashboards-that-lie

In short: Chaitanya Reddy Krishnama of MoneyGram at Conf42 Observability 2025 on fixing silent pipeline failures and schema drift with data observability.

The worst dashboard is not the broken one; it is the one that looks polished and is quietly wrong. At Conf42 Observability 2025, Chaitanya Reddy Krishnama of MoneyGram told the story of how silent pipeline failures and schema drift corrupted his team's analytics, and how they fixed it by treating data pipelines like production software: instrumented, tested continuously and on call.

## How a dashboard learns to lie

The failure modes will be familiar to anyone who has owned a warehouse:

- **Silent pipeline failures**: jobs that failed or only partly succeeded without loud errors, so some records simply never loaded.
- **Schema drift**: an upstream column renamed or a format changed, pipelines kept running, and key fields misaligned without a single alert.
- **Brittle validations**: the few quality rules that existed broke whenever volume spiked or new fields appeared.
- **Thin coverage**: a couple of critical tables tested, hundreds not.

Detection came from stakeholders, typically the Monday 8 AM Slack message about broken data. Chaitanya sums up the cost in one line: "Once a dashboard tells a lie, every report becomes a suspect." Team morale went with it, as more time went into firefighting than delivering.

## Why the old QA could not keep up

Traditionally, data QA was a checkbox at development time: if the pipeline ran without errors, the data was assumed fine. Tests were static while the data changed every month, and writing even five checks for each of a thousand tables by hand meant thousands of tests to maintain. QA lived before deployment with no feedback loop from production, and the rest was people eyeballing reports.

## The pivot: telemetry on every stage

The turning point was asking why they ran data systems in the dark when nobody would deploy an app without monitoring. The team added logging at each ETL stage, measured row counts and processing times, and traced data flows from source to dashboard. A few principles came with it:

- **Fail fast**: some tests are marked critical, and when they fail the pipeline stops and alerts instead of pushing bad data downstream.
- **Lineage**: a map from source to target, so a bad data set points to its likely upstream cause and to the reports it will affect.
- **Checks as code**: expectations such as no nulls in critical columns or transaction amounts within a sane range, run on every update.
- **Data health monitoring**: freshness, volume, distribution and schema changes, watched around the clock.

The alert example is the kind you can copy straight away: a daily sales table that normally has around 100K rows and today has zero should page someone, and so should an ETL job that has not run by its scheduled time.

## The toolchain

The stack is open source and ordinary in the best sense. Great Expectations runs checkpoints after loads to verify row counts, ranges and null percentages. dbt handles transformations and SQL tests, with tests code-reviewed and versioned like the models. OpenTelemetry instruments custom pipeline code, propagating a trace ID so every event in a pipeline run is linked. Prometheus stores pipeline metrics and Grafana became their pipeline control centre. In BigQuery, the information schema tables help detect schema changes and track bytes processed.

At the end of the chain, dashboards carry an implicit trust score: if it is live, every upstream check passed. If upstream data is stale or under investigation, the report gets an annotation saying so.

## The cultural half

The lessons are as much about people as tools. Trust but verify, at every step. Make observability a team sport across data engineers, QA and analysts. Start with your worst pain point, such as the dashboard that breaks every quarter, and win there first. Treat data incidents like software incidents, with on-call rotations, root cause analysis and a new test after every miss. And celebrate catches, because a prevented bad dashboard is invisible unless someone points at it.

## Who should watch

Analytics engineers, data platform teams and anyone whose stakeholders have stopped trusting the numbers. The talk is practical and tool-specific enough to act on; you could set up a freshness alert and a first Great Expectations suite the same afternoon.

## Related Conf42 talks

- [Shashank Reddy Beeravelly on AI-driven data quality management with Python](https://www.conf42.com/Python_2025_Shashank_Reddy_Beeravelly_data_quality_management) at Conf42 Python 2025.
- [Sunil Kumar Mudusu on data quality and validation in ML pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) at Conf42 Machine Learning 2025.
- [Aliaksandr Sheliutsin's four tricks for getting more out of Airflow pipelines](https://www.conf42.com/DevOps_2024_Aliaksandr_Sheliutsin_leverage_airflow_pipelines) at Conf42 DevOps 2024.

[Watch Chaitanya Reddy Krishnama's talk](https://www.conf42.com/Observability_2025_Chaitanya_Reddy_Krishnama_dashboards_qa_nightmares)

[Watch the talk on YouTube](https://youtu.be/HN7PtUCR23c).

## Watch the talk

[Data QA Nightmares: A Journey from Broken Dashboards to Observability Maturity](https://www.conf42.com/Observability_2025_Chaitanya_Reddy_Krishnama_dashboards_qa_nightmares) at Conf42 Observability 2025.
