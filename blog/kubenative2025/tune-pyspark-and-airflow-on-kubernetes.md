# Tuning PySpark and Airflow on Kubernetes, one variable at a time

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/tune-pyspark-and-airflow-on-kubernetes

In short: Sruthi Erra Hareram (TELUS Digital) at Conf42 Kube Native 2025 on executor sizing, joins, skew and Airflow patterns for Kubernetes-native ETL.

A 60 MB dimension table, switched to a broadcast join, took one Spark stage from 19 minutes to three. That story sits in the middle of Sruthi Erra Hareram's talk at Conf42 Kube Native 2025, and it sums up her approach: most ETL speed comes from a few boring, measurable changes. Sruthi, a Data Engineer at TELUS Digital, covers the architecture, the Spark tuning, the Airflow patterns and a four-week rollout plan for running PySpark and Airflow on Kubernetes.

She promised zero fluff and mostly delivered. This is a practitioner's checklist, not a product pitch.

## Why ETL breaks at scale

Sruthi names four recurring failures. Clusters sized by guesswork, either over-provisioned and expensive or under-provisioned and flaky. Poor visibility, so a job failing at 2 AM means manual recovery because nobody can see lineage or timing. Brittle monolithic scripts where a new column ripples through everything. And growing data volume that inflates shuffle cost, storage cost and the blast radius of bad input.

Her foundation has three pillars: containers so each pipeline declares its own dependencies, CPU, memory and JVM; Kubernetes as the compute fabric, with namespaces isolating teams and quotas keeping noisy neighbours in check; and infrastructure as code, with Terraform and Helm reviewed through pull requests and promoted via GitOps.

## Spark tuning lives in memory, joins and skew

The tuning section is the densest and most reusable. Her starting points:

- executors of roughly 4 to 8 GB as a pragmatic range
- persist only where reuse pays off
- memory fractions around 0.6 for execution and 0.2 for storage as a baseline, adjusted with real metrics
- broadcast hash joins for small dimensions, sort-merge for large fact-to-fact joins
- salting or pre-aggregation for hot keys

The skew story is the other memorable one: a single customer accounted for 40% of the rows in one pipeline, and salting into 16 buckets levelled the partitions and removed the straggler.

Her diagnostic trick is worth stealing. If median task time is low but p95 is awful, suspect skew. If both are high, you are under-resourced or over-shuffling. And the discipline around it: take a baseline, change one variable at a time, and when a change wins, bake it into project templates so the next pipeline inherits it.

## Airflow on Kubernetes needs a few patterns, not more people

Running Airflow on Kubernetes aligns the control plane with the data plane: pod-level isolation per task, workload identity and managed secrets. Her practical tip is to define a small set of pod templates (small, heavy joins, machine learning) and let tasks pick by convention.

The four patterns she recommends:

1. Dynamic DAG generation from configs kept in S3 or GCS, so hundreds of similar pipelines don't mean hundreds of copy-pasted files.
2. Branching with BranchPythonOperator to route around known bad data or choose a light or heavy path by input size.
3. Backfills driven by logical run dates, with every step idempotent.
4. SLA monitoring through custom callbacks into Datadog or Prometheus, alerting on leading indicators like rising retries instead of only failures.

Her micro-example ties it together: if today's volume is more than 1.5 times the seven-day median, the DAG branches to a wider executor profile and adds a checkpoint.

## Observability and the rollout

Prometheus for executor and shuffle metrics, structured JSON logs with correlation IDs, OpenTelemetry tracing across Airflow tasks and Spark jobs, Great Expectations for data quality, and per-app cost tracking. Then a migration that keeps risk low: one medium-impact pipeline per sprint, compare against the baseline, publish the result, repeat. Her pitfalls list includes the cheap win most teams still miss: move large datasets from CSV or JSON to Parquet or ORC.

## Who should watch

Data engineers running Spark and Airflow who are moving onto Kubernetes, or who already have and are paying for it. Platform engineers supporting data teams will get a clear picture of what those teams need from the cluster.

## Related Conf42 talks

- [Optimising Apache Spark and SQL for improved performance](https://www.conf42.com/Machine_Learning_2024_Marcin_Szymaniuk_apache_spark_sql) goes further into Spark internals.
- [How to use common Python frameworks to test Apache Airflow data pipelines](https://www.conf42.com/Python_2024_Tamara_Janina_Fingerlin_frameworks_apache_airflow_pipelines) covers the testing side of the DAGs Sruthi generates.
- [Building Resilient Apache Spark Clusters on Kubernetes for AI Workloads](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters) looks at the cluster layer underneath.

[Watch Sruthi Erra Hareram's talk](https://www.conf42.com/Kube_Native_2025_Sruthi_Erra_Hareram_etl_airflow_optimization)

[Watch the talk on YouTube](https://youtu.be/3cAgChisXXw).

## Watch the talk

[Kube-Native ETL at Scale: Optimizing PySpark + Airflow Workflows in Cloud-Native Environments](https://www.conf42.com/Kube_Native_2025_Sruthi_Erra_Hareram_etl_airflow_optimization) at Conf42 Kube Native 2025.
