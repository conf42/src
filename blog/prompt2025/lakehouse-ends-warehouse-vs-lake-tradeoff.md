# A lakehouse ends the choice between governed and cheap data

Conf42 Blog, 2025-10-18, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/lakehouse-ends-warehouse-vs-lake-tradeoff

In short: Richa Solanki (Ally Bank) at Conf42 Prompt Engineering 2025 on lakehouse zones, Data Vault, ELT, open table formats and automated governance at scale.

For years the data team's choice was a governed, expensive warehouse or a cheap lake that slowly turned into a swamp. At Conf42 Prompt Engineering 2025, Richa Solanki, Manager of Data Management at Ally Bank, explained how lakehouse architecture removes that trade-off, and walked through the patterns that make it work at enterprise scale: raw, refined and curated zones, Data Vault modelling, ELT in place, and governance that runs itself.

It's a compact architecture primer from someone running enterprise data management in banking, with a sensible implementation checklist at the end.

## Two flawed options

Richa frames the problem first. Data now arrives structured, semi-structured and unstructured from many systems, and fragmented environments make governance, security and efficiency harder. Warehouses give reliability, consistency and strong governance, but they're expensive and rigid. Lakes are cheap and scalable, but drift into swamps with unclear ownership and no transactional consistency. Enterprises have been forced to pick structure or flexibility.

The lakehouse, in her telling, combines warehouse governance with lake economics, and runs batch analytics, streaming and machine learning on one platform: build once, govern centrally, serve many use cases.

## Four capabilities that make it a lakehouse

She lists four pillars. ACID transactions keep integrity as you scale to billions of records. Schema enforcement supports both schema-on-read and schema-on-write as business data evolves. Real-time analytics query batch and streaming data together without complex ETL. Unified governance gives one place for metadata, lineage and compliance, which is what enterprise adoption hinges on.

## Zones and vaults

The structural pattern is three zones. Raw stores data exactly as it arrives, for auditability. Refined is where cleansing, validation, standardisation and business rules happen. Curated holds analytics-ready datasets for reporting and machine learning. The layering is what lets people trust a number: you can always trace it back to what arrived.

Inside, she recommends Data Vault modelling for flexibility and history. Hubs hold core business entities and their identifiers, links capture relationships between them, and satellites store descriptive attributes with full history. Schemas can evolve without breaking downstream systems, and you can see how data changed over time, which auditors in a bank tend to ask about.

## Performance and ELT

Scale is pointless if queries crawl, so she covers the performance trio: columnar formats like Parquet and ORC that compress well and read only needed columns; intelligent caching for frequently accessed data; and dynamic partitioning by time, geography or other dimensions for pruning and parallelism.

The pipeline shift is from ETL to ELT. Instead of extracting, transforming and loading across several systems, with latency and failure points at each hop, you extract and load first, then transform in place. Fewer copies, less maintenance, and more time analysing data instead of fixing pipelines.

## Governance can't be manual

At scale, governance has to be automated: data quality checks that flag anomalies before they reach analytics, complete lineage and audit trails, role-based access control and encryption. Richa cited results from lakehouse implementations of around 60% less maintenance effort, ETL workflows about 45% faster and total cost of ownership down roughly 40%, and says the bigger gain is agility.

Her implementation advice: choose platforms that support open table formats such as Delta Lake, Apache Iceberg or Apache Hudi to avoid lock-in; migrate in phases, starting with non-critical workloads; and train engineers and analysts in both warehouse and lake thinking, because it's as much about people and process as technology.

## Who should watch

Data engineers and architects planning a move off a separate lake and warehouse, and data managers in regulated industries who need the governance story to hold up. If you already run Iceberg with Data Vault, it's a refresher; the related talks go into DataOps and ingestion.

## Related Conf42 talks

- [Bring your DataOps to the Data Lakehouse: What are the benefits and how to navigate the common challenges](https://www.conf42.com/DevOps_2025_Jorge_LoaicigaRodriguez_dataops_lakehouse_challenges) by Jorge Loaiciga-Rodriguez at Conf42 DevOps 2025.
- [AI-Governed Lakehouse Ingestion with Flink on Kubernetes for Reliable DataOps](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Jyothish_Sreedharan_governed_lakehouse_ingestion) by Jyothish Sreedharan at Conf42 Site Reliability Engineering 2026.
- [IoT Data Lakehouse: Scalable Architectures for Connected Device Analytics](https://www.conf42.com/Internet_of_Things_IoT_2025_Bhanudeepti_Chinta_lakehouse_analytics_scalable) by Bhanudeepti Chinta at Conf42 Internet of Things 2025.

[Watch Richa Solanki's talk](https://www.conf42.com/Prompt_Engineering_2025_Richa_Solanki_data_lakehouse_enterprise) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/EpC1PDiZ7mM).

## Watch the talk

[Transforming Enterprise Data with Lakehouse Architecture at Scale](https://www.conf42.com/Prompt_Engineering_2025_Richa_Solanki_data_lakehouse_enterprise) at Conf42 Prompt Engineering 2025.
