# One feature pipeline for six teams, not six for one

Conf42 Blog, 2025-12-15, updated 2026-11-09. https://www.conf42.com/blog/iot2025/snowflake-feature-store-iot-cost

In short: Manmohan Alla of Apple at Conf42 IoT 2025 on cutting IoT ML costs with a Snowflake feature store, incremental processing, dbt tests and right-sized compute.

The same rolling average, computed three different ways by three teams, is how IoT machine learning gets expensive and untrustworthy at the same time. At Conf42 Internet of Things (IoT) 2025, Manmohan Alla, a member of technical staff at Apple, showed how a structured feature store on Snowflake brings IoT telemetry under control, and where the cost savings in his title actually come from.

The talk draws on deployments in manufacturing, utilities, energy grids and smart monitoring. It is an architecture and practices talk, built around Snowflake.

## Temporal context is the feature

Manmohan's first point is that a single sensor reading means almost nothing. A vibration value is only interesting compared with the last hour, last week or the seasonal pattern. So useful IoT features are rolling windows, lags, trend acceleration and seasonal behaviour, and he says that in many real deployments over 70% of model accuracy comes from that temporal context.

Doing that consistently across thousands of sensors and dozens of models is where ad hoc scripts collapse. Sample rates differ, smart meters report every few seconds while vehicles send irregular bursts, and the resulting temporal misalignment breaks simple SQL analytics.

## Fragmentation is the real cost

IoT data quality problems such as null values, network gaps and calibration drift are unavoidable. The danger, in his telling, is inconsistent handling: data engineers clean at ingestion one way, scientists write their own transforms, ops builds BI aggregates, and the same metric ends up computed three different ways. He has seen three to six copies of the same logic in real pipelines because there was no central feature store.

A feature store fixes that with canonical, versioned, reusable feature definitions and optimized serving. He reports feature reuse cutting engineering effort by 60 to 80%, and frames it neatly: instead of six teams building six pipelines, one pipeline serves six teams.

## Where Snowflake earns its place

He highlights three Snowflake capabilities. VARIANT ingests semi-structured sensor JSON without schema gymnastics. Time Travel keeps historical training data reproducible even if it changes. Streams with materialized views give incremental change capture, so only new sensor data is processed; he says this routinely cuts compute by 40 to 60% because nobody reprocesses history that has not changed.

The layering is raw (truth, timestamps, device metadata), transform (windowing, smoothing, health metrics) and a denormalized serving layer for fast lookups. dbt turns the transforms into software, with dependency graphs, reusable macros for rolling statistics and automated tests that catch bad upstream sensor data before it reaches dashboards or models. SQL handles about 80% of the work; Python running inside Snowflake, with libraries such as pandas and SciPy, covers the remaining spectral analysis and anomaly scoring inside Snowflake, so data never leaves its governance boundary.

## Right-size everything

The cost section is the most directly reusable. Match warehouse size to the job: small for simple aggregations, medium for wide joins, large only for parallel work, which he says commonly saves over 50% of compute in production. Tier storage from granular recent data to downsampled older data to a cold compliance archive. Lean on caching for repeated inference lookups. Denormalized serving tables trade a little storage for two to five times better serving latency in many deployments, and he notes that predictable latency matters more than raw speed for IoT ML.

Operations close it out: monitor data quality, pipeline health and feature drift (he has seen unnoticed drift cost 20 to 30% of model accuracy within a month), use RBAC with row-level security, run multiple feature versions side by side, and tag cost per model and team.

## Who should watch

Data and ML engineers feeding models from device telemetry, especially teams already on Snowflake or arguing over who owns feature logic. If you are not on Snowflake, the principles transfer; the specific features do not.

## Pair it with

- [Akshat Kapoor on real-time analytics in IIoT](https://www.conf42.com/Internet_of_Things_IoT_2024_Akshat_Kapoor_analytics_iiot) at Conf42 IoT 2024.
- [Sunil Kumar Mudusu on data quality and validation in ML pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) at Conf42 Machine Learning 2025.
- [Bhanudeepti Chinta on lakehouse architectures for IoT analytics](https://www.conf42.com/Internet_of_Things_IoT_2025_Bhanudeepti_Chinta_lakehouse_analytics_scalable), also at Conf42 IoT 2025.

[Watch Manmohan Alla's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Manmohan_Alla_warehousing_featurestores_optimization) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/lPkXf4MKRL0).

## Watch the talk

[IoT Data Warehousing with Snowflake Feature Stores: 40% Cost Reduction Strategy](https://www.conf42.com/Internet_of_Things_IoT_2025_Manmohan_Alla_warehousing_featurestores_optimization) at Conf42 Internet of Things (IoT) 2025.
