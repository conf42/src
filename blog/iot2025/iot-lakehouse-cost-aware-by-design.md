# IoT data platforms fail on cost, not on collection

Conf42 Blog, 2025-12-06, updated 2026-11-09. https://www.conf42.com/blog/iot2025/iot-lakehouse-cost-aware-by-design

In short: Bhanudeepti Chinta of Dave at Conf42 IoT 2025 on lakehouse architectures for sensor telemetry, from Iceberg and Delta Lake to medallion layers.

Collecting sensor data is the easy part; paying for it a year later is where IoT platforms come apart. At Conf42 Internet of Things (IoT) 2025, Bhanudeepti Chinta, Engineering Manager for Data at Dave, with 14 years on high-volume data platforms, argued that the lakehouse is as much a cost containment strategy as an architecture for connected device analytics.

Her opening observation sets the tone: organizations rarely fail at IoT because they cannot collect data, but because the cost and complexity of managing it grow faster than the value they get out.

## Three audiences, one firehose

IoT telemetry arrives at millisecond intervals and can reach petabyte scale within months. The same data then has to serve operations teams who want real-time dashboards, data scientists who need history for modeling, and business users who want aggregates. On top of that, schemas keep moving: firmware updates add fields and vendors produce consistently inconsistent formats. Any architecture has to ingest continuously, absorb schema changes gracefully, and keep years of history without rewriting it.

## Why the lakehouse wins the middle ground

Warehouses give performance and consistency but get expensive and rigid with semi-structured telemetry. Data lakes are cheap but weak on reliability, governance and transactions. The lakehouse puts warehouse-grade guarantees on cheap cloud object storage.

The enabling layer is the open table format: Delta Lake, Apache Iceberg and Apache Hudi add transactional semantics, schema evolution and efficient metadata management to object storage. Without them, she warns, IoT platforms quietly pile up hidden operational and storage costs. Physically, storage, table formats and compute are separated, with engines like Spark or Trino scaling only when there is work, instead of paying for fixed infrastructure around the clock.

## The decisions that decide the bill

Bhanudeepti points at where IoT cost overruns usually start: architectural choices made early.

- **Streaming at the core.** Data flows through Kafka, Kinesis or Event Hubs and is processed in real time with Spark or Flink.
- **Time-based partitioning** that matches the temporal nature of telemetry.
- **Lifecycle management** across hot, warm and cold tiers.
- **Schema evolution** without rewriting historical data.

The medallion layout organizes the rest. Bronze keeps raw sensor data exactly as received, for audit and replay. Silver validates, normalizes and standardizes. Gold exposes business-ready datasets for reporting and dashboards. The cost argument is that expensive compute only runs where business value sits, and nothing gets reprocessed twice for no reason.

For real-time versus batch, she favours a Kappa-style approach where one streaming pipeline feeds both, with incremental processing and materialized views lowering long-term cost. On the ML side, feature engineering tends to get duplicated across teams; a governed feature store such as Snowflake's keeps features consistent between training and inference and cuts the repeated compute.

## Use cases, briefly

The case studies are short sketches rather than deep dives: predictive maintenance in manufacturing from early failure signals in telemetry, connected vehicle fleets doing route optimization, driver scoring and vehicle health, smart city traffic and environmental monitoring with open data, and utility smart meter analytics for theft detection, peak demand forecasting and grid optimization across millions of households. Looking ahead, she expects lower-latency streaming, better time series performance, stronger governance and more analytics pushed to the edge.

Her closing line is the one to keep: the platforms that last will be cost aware by design, not merely data aware.

## Who should watch

Data engineers and platform owners sizing an IoT analytics stack, or inheriting one whose storage bill grows faster than its users. It is an architecture overview rather than a hands-on build; pair it with a talk that goes deep on a single table format if you want the mechanics.

## Next up

- [Satish Mane and Rajeev Jaiiswal on building a cloud-native open format data lakehouse](https://www.conf42.com/Cloud_Native_2023_Satish_Mane_Rajeev_Jaiiswal_build_open_format_data_lakehouse) at Conf42 Cloud Native 2023.
- [Jorge Loaiciga Rodriguez on bringing DataOps to the data lakehouse](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) at Conf42 DevOps 2025.
- [Manmohan Alla on IoT data warehousing with Snowflake feature stores](https://www.conf42.com/Internet_of_Things_IoT_2025_Manmohan_Alla_warehousing_featurestores_optimization), from the same Conf42 IoT 2025 lineup.

[Watch Bhanudeepti Chinta's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Bhanudeepti_Chinta_lakehouse_analytics_scalable) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/b34tpd-0uSk).

## Watch the talk

[IoT Data Lakehouse: Scalable Architectures for Connected Device Analytics](https://www.conf42.com/Internet_of_Things_IoT_2025_Bhanudeepti_Chinta_lakehouse_analytics_scalable) at Conf42 Internet of Things (IoT) 2025.
