# Four signals, one backend - why Gigapipe stores everything in ClickHouse

Conf42 Blog, 2026-09-05, updated 2026-11-09. https://www.conf42.com/blog/obs2026/gigapipe-four-signals-one-backend

In short: Rita Lopes, founder of Gigapipe, at Conf42 Observability 2026 on unifying logs, metrics, traces and profiles in one open source backend.

Putting Prometheus, Loki, Tempo and Pyroscope behind one Grafana doesn't give you one system; it gives you four backends and one browser tab. At Conf42 Observability 2026, Rita Lopes, founder and CEO of Gigapipe, made that argument and presented her company's answer: an open source, AGPLv3 observability stack that ingests all four signals through their existing protocols and stores them together in ClickHouse.

This is a founder talking about her own product, and she says so from the first sentence. It's still worth the time for the architecture reasoning, which applies whichever tool you end up running.

## The 3 AM tab shuffle

The opening is an incident walk-through. Metrics show the spike but not the cause. Logs show a flood of errors but not which request. Traces need timestamps you line up by hand. Fifteen minutes in, you know what broke and haven't started fixing it.

Lopes's sharper point is aimed at teams who think Grafana solved this. Open the data source config and there's a separate backend per signal, so the log panel doesn't know about the metrics spike and nobody hands you the trace ID from the log line. One UI, same manual correlation.

## The trade-off triangle

She frames the market as a triangle: complete coverage, affordable, operationally simple, pick two. Coverage plus cheap means self-hosting four systems and a part-time job as an observability engineer. Coverage plus simple means a vendor bill. Cheap plus simple means cutting signals, longer scrape intervals and shorter retention, until the one incident that needed the data. She added that AI workloads generate far more telemetry, which makes per-event pricing hurt more.

## The architecture: polyglot in, columnar underneath

Gigapipe's claims, as presented:

- **Polyglot writes.** OTLP, Prometheus remote write, Loki push, Tempo, Pyroscope, plus InfluxDB, Datadog and Elastic agents, so you can point an existing proprietary agent at a staging install and compare.
- **Polyglot reads.** PromQL, LogQL, TraceQL and FlameQL, plus InfluxDB and SQL, so Grafana and Perses dashboards work unchanged.
- **Clean-room code.** In her words, "Not a fork, not a wrapper", with no translation layer on the hot path.
- **Single binary.** Runs on Kubernetes, VMs or bare metal; your data stays where you put it.

ClickHouse is the deliberate choice underneath. Observability data is write-heavy, read in time ranges and rarely updated, and a columnar engine reads only the columns a query needs. Labels become columns rather than in-memory series, which she argued sidesteps the high-cardinality limits Prometheus hits. Cold data tiers to any S3-compatible store by TTL or space rules, without downsampling. She also said the next version is moving to a self-contained, Parquet-based data-lake design with no external database.

## Migration as a config change

The adoption path is incremental: start with one signal, usually logs, check data lands within seconds, repoint the data source, confirm dashboards still work, then move the next signal. The layers are independently replaceable, so you can adopt only the storage or only the query layer. She said teams report doing the full move in a single sprint.

Her performance and savings figures (billions of points a day on a single standalone deployment, sub-second historical queries, a 50 to 90 percent cost reduction) are customer-reported claims from the talk; benchmark them on your own data before quoting them to finance.

## Who should watch

SREs running the full Grafana LGTM-plus-profiling stack who are tired of operating four storage systems, and anyone evaluating ClickHouse-backed observability. If you want a neutral comparison of options, this isn't it; it's one team's case for its design.

## Related Conf42 talks

- [Sivasubramanian Bagavathiappan on unified observability as a single source of truth](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sivasubramanian_Bagavathiappan_unified_observability_single) (Conf42 SRE 2025).
- [Michael Levan on observing agentic and MCP traffic while keeping costs low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) (Conf42 DevOps 2026): the AI telemetry pressure Lopes mentions.
- [Neel Shah on Observability 2.0, beyond logs, metrics and traces](https://www.conf42.com/Observability_2025_Neel_Shah_logs_metrics_traces) (Conf42 Observability 2025).

[Watch Rita Lopes's talk](https://www.conf42.com/Observability_2026_Rita_Lopes_metrics_logging_tracing)

[Watch the talk on YouTube](https://youtu.be/MzPk4IqL54A).

## Watch the talk

[404: Observability Without Trade-offs Not Found - Until We Built Gigapipe](https://www.conf42.com/Observability_2026_Rita_Lopes_metrics_logging_tracing) at Conf42 Observability 2026.
