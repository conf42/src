# Most of your logs are never read, and you pay for them twice

Conf42 Blog, 2025-05-25, updated 2026-11-09. https://www.conf42.com/blog/obs2025/logging-bills-sampling-filtering-tiered-storage

In short: Venkata Madhu Prateek Reddy Kambala of Synapsis at Conf42 Observability 2025 on cutting logging bills with sampling, filtering, tiered storage and compression.

Cloud vendors charge you once to ingest a log line and again to keep it, and most of those lines are never queried. At Conf42 Observability 2025, Venkata Madhu Prateek Reddy Kambala, a senior DevOps engineer at Synapsis, laid out four ways to shrink a logging bill without losing the logs you need at 3am: sampling, filtering, tiered storage and cheaper tooling.

The talk leans on public engineering write-ups from Uber, Slack, Shopify and Razorpay, so it reads as a field guide to what other teams already tried.

## Why the bill keeps growing

Venkata names the usual suspects. Microservices multiplied the number of log streams. Pricing hits both ingestion and storage, so every line is charged twice. Debug logging gets left on in production, where it generates huge volume that almost nobody reads. And without governance, nobody decides what should be collected in the first place. He cites research that only about 30% of generated logs are ever used for queries or monitoring; the rest just sits in storage.

## Sample debug, never sample errors

The first strategy is sampling. He describes Uber keeping only 5% of its debug logs, and walks through three approaches: head-based (decide at the source), tail-based (decide after the trace completes) and level-based (different rates per log level). The rule he repeats is the one worth remembering: never sample error or fatal logs. Start debug and info sampling around 10% and tune from there, and keep the sampling consistent across service boundaries.

To avoid sampling bias hiding a rare event, he suggests trace-aware sampling and a safety switch: when an alert fires, stop sampling so the incident gets full fidelity.

## Drop the noise at ingestion

Filtering removes logs that carry no value at all. His example is Slack dropping health check logs with Fluent Bit. The common noise list is familiar: health and ping endpoints, repeated non-critical connection timeouts, every successful authentication, chatty service-to-service calls. Filtering at the ingestion layer saves twice, because the line is never ingested and never stored.

## Hot, warm, cold

Storage tiering matches retention to how often data is read: roughly the last seven days in Elasticsearch for fast queries, seven to 30 days in standard S3, and anything older in Glacier for compliance. He flags the catch honestly: querying cold storage is slow and painful, so design queries to stay on hot and warm data, and build rehydration workflows for the rare deep look back.

## Tooling and compression

The fourth lever is moving to open-source stacks such as Grafana Loki, with the trade-off spelled out: you swap a vendor bill for the cost of people who can run the system. The case study that gets the most airtime is Uber's CLP (Compressed Log Processor), which compressed huge volumes of Spark job logs while still allowing queries without decompressing them.

Structured JSON logging runs through all of it. It makes filtering precise, compresses better and makes queries faster, so it is the cheapest change on the list.

## A roadmap, with baselines first

Venkata closes with a plan: audit volumes, find the five to ten streams that generate most of the data, put cost dashboards in place, then roll out filtering and sampling, then tiering, then longer-term moves like compression and log-based metrics. Track financial, operational and volume metrics, and set the baseline before you change anything, or you will never know what worked.

## Who should watch

Platform and SRE teams who just got the observability invoice and need a structured list of options to bring to a FinOps review. If you already sample and tier, the case studies are still useful ammunition.

## Related Conf42 talks

- [Pradeep Gaddamidi on cost-effective cloud monitoring and logging](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) (DevOps 2025).
- [Phil Wilkins on making logs work for you with Fluentd](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd) (Cloud Native 2021), for the pipeline where filtering happens.
- [Shyamkumar Kalariya on getting the most out of your logs at 3 AM](https://www.conf42.com/Observability_2024_Shyamkumar_Kalariya_logs_3AM) (Observability 2024), the other side of the trade-off.

[Watch Venkata Madhu Prateek Reddy Kambala's talk](https://www.conf42.com/Observability_2025_Venkata_Madhu_Prateek_Reddy_Kambala_logging_cost_cutting)

[Watch the talk on YouTube](https://youtu.be/IVC8lfsO244).

## Watch the talk

[Logging in the Age of Cost-Cutting: Smart Strategies to Reduce Bills](https://www.conf42.com/Observability_2025_Venkata_Madhu_Prateek_Reddy_Kambala_logging_cost_cutting) at Conf42 Observability 2025.
