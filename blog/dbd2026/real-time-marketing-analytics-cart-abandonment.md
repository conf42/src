# The abandoned cart won't wait for your overnight batch job

Conf42 Blog, 2026-05-13, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/real-time-marketing-analytics-cart-abandonment

In short: Kamini Murugaboopathy of Wonderbow Analytics at Conf42 Database DevOps 2026 on Kafka, lakehouses, bitmap indexes and DataOps for real-time marketing analytics.

A customer adds shoes to a cart and leaves; a batch pipeline finds out tomorrow morning, after they have bought the shoes elsewhere. At Conf42 Database DevOps 2026, Kamini Murugaboopathy, Director at Wonderbow Analytics, walked through the architecture that lets marketing act on that event within seconds, and argued that it is as much a database and DataOps problem as a data engineering one.

The talk is a well-paced architecture tour aimed at engineers who know batch ETL and want the map of what changes when everything streams. Expect clear explanations of the building blocks rather than a single system's war story.

## Freshness, not volume, is the advantage

Kamini's starting point: almost every company collects website visits, app activity, email clicks, ad impressions, CRM and purchase data. The edge goes to the one that can use it while it is fresh. Batch systems fail on three counts: latency (a 10am cart abandonment seen the next day is a lost sale), fragmentation (web, apps, Google Ads, Meta Ads, CRM, email and support tools each with their own formats and timing), and scalability (a flash sale or influencer post turns normal traffic into thousands of simultaneous shoppers).

The answer is event-driven: every page view, click, add-to-cart and purchase is an event that can update a dashboard, a profile, a recommendation model or trigger a recovery email.

## Warehouse to report, lake to store, lakehouse to do both

Her storage explanation is a clean one to borrow. A warehouse such as Snowflake, BigQuery or Redshift is the tidy filing cabinet for structured questions like yesterday's revenue by campaign. A data lake holds the messy, semi-structured clickstream logs, raw app events and creative assets. A lakehouse combines both, so raw events stay around for machine learning while clean campaign data answers dashboards quickly.

Apache Kafka is the "live message highway" in the middle, letting segmentation, recommendations and campaign triggers consume the same events independently, with Apache Flink, Spark Streaming or AWS Kinesis processing them in flight.

## Segmentation needs the right index

The most database-flavoured part of the talk covers real-time audience segmentation. With profile updates arriving by the thousand every second, you cannot scan every customer for everyone who viewed shoes but did not buy. Kamini covers three tools: inverted indexes that keep ready-made lists (everyone interested in shoes, everyone who clicked the discount ad) and intersect them; bitmap indexes that store yes-or-no flags like clicked, added to cart, purchased, which CPUs compare extremely fast; and materialized views that precompute the questions marketing asks every hour, such as cart abandonments today.

## No maintenance window, so ship changes like code

Streaming systems never stop for a midnight change, so DataOps applies DevOps habits to data: version control for schemas and pipeline definitions, automated data quality and regression tests, CI/CD for database migrations, and monitoring of freshness, schema failures and consumer lag. Schema changes follow expand, migrate, contract, with a schema registry stopping one team from publishing a format that breaks another's pipeline. Models get the same treatment: retrained in parallel, then shifted over with blue-green or canary traffic while performance is watched.

Scaling should be proactive: a surge in event ingestion is a leading indicator of the query load about to hit the warehouse, so scale that layer first. Observability should watch the leading signals too: consumer lag, schema failure rates, p99 dashboard latency, model drift. Consistency should be selective: strong for purchases, attribution and deduplication; eventual for click tracking and audience scores; causal where order matters, such as session stitching.

Her production lessons close it out: infrastructure as code from day one, data quality before models (bad data propagates instantly), schema registries with compatibility checks, and stress tests well beyond expected peak, because many streaming failure modes only show up under pressure.

## Who should watch

Data engineers and architects moving marketing or product analytics from nightly batch to streaming, and DBAs who want to know why the analytics team keeps asking about bitmap indexes. If you already run Kafka with a schema registry in production, the value is in the consistency and scaling sections.

## Related Conf42 talks

- [Mark Needham on a real-time analytics dashboard with Apache Pinot and Kafka](https://www.conf42.com/Python_2022_Mark_Needham_realtime_analytics_dashboard_streamlit_apache_pinot_apache_kafka) at Conf42 Python 2022.
- [Satish Mane and Rajeev Jaiiswal on building an open-format data lakehouse](https://www.conf42.com/Cloud_Native_2023_Satish_Mane_Rajeev_Jaiiswal_build_open_format_data_lakehouse) at Conf42 Cloud Native 2023.
- [Jorge Loaiciga Rodriguez on DataOps and lakehouse challenges](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) at Conf42 DevOps 2025.

[Watch Kamini Murugaboopathy's talk](https://www.conf42.com/Database_DevOps_2026_Kamini_Murugaboopathy_agents_pipelines_o11y)

[Watch the talk on YouTube](https://youtu.be/_ilGTMTK56o).

## Watch the talk

[Cloud-Native Data Architectures for Real-Time Marketing Analytics in Database DevOps](https://www.conf42.com/Database_DevOps_2026_Kamini_Murugaboopathy_agents_pipelines_o11y) at Conf42 Database DevOps 2026.
