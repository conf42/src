# Observability 2.0 trades firefighting for forecasting

Conf42 Blog, 2025-06-02, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observability-2-0-from-firefighting-to-forecasting

In short: Neel Shah of Middleware at Conf42 Observability 2025 on OpenTelemetry collectors, ML anomaly detection, smarter ingestion and AI-assisted root cause.

The 2 a.m. outage with terabytes of telemetry and no idea where to look is the scenario Neel Shah built his talk around. At Conf42 Observability 2025, Neel, a DevRel at Middleware and a DevOps community organiser, argued that observability is shifting from reactive troubleshooting to predictive operations, with OpenTelemetry as the foundation, ML and LLMs on top, and smarter ingestion to keep the bill sane.

It is a broad overview rather than a single technique, and it is a vendor-adjacent talk: Neel shows where Middleware's own features fit, which he flags openly.

## A short history of too much data

Neel sketches three eras. Around 2015, monoliths and classic tools like Grafana. Then the telemetry explosion, where microservices produced so much data from apps and infrastructure that teams had plenty of signals and little understanding. Then, from about 2023, AI arriving to make sense of it. The shift he wants: from manual troubleshooting to incidents that explain themselves, and from finding risk during the outage to having it flagged before.

## OpenTelemetry is the floor, the collector is the engine

The middle of the talk explains why OpenTelemetry matters. Before it, everyone collected data in different formats, so sharing between teams or tools was painful. OTel created a vendor-neutral, standard way to instrument, easier correlation between signals, and freedom to route data to multiple backends. Neel notes it is one of the largest CNCF projects after Kubernetes.

He walks through the collector's three parts: receivers that take data in, processors that transform it, and exporters that send it to a backend. If you have never looked inside a collector pipeline, this is a clean explanation.

## ML for patterns, LLMs for summaries

On the AI side, Neel separates two jobs. ML models detect anomalies and incident patterns that were previously invisible, and help prioritise incidents by severity and impact. LLMs summarise incidents in plain language and can predict likely issues from historical patterns. He also lists the data types he considers part of the 2.0 picture beyond the classic three: events, profiles, dependencies and eBPF, which reads from the kernel which ports are open and how packets move.

His example of where this goes is a little cheeky: an alert says CPU is above 80%, and the alert itself offers a button to double the capacity. Whether you want that button in production is a separate conversation with your change board.

## The cost problem has a pipeline answer

The section on cost is the most practical. Neel names the drivers: massive telemetry growth from microservices, storing every log, metric and trace even when much of it is irrelevant, high-cardinality metrics and oversampled traces. The results are higher infrastructure spend, slower queries and noise.

The answer is to filter before you store. He lists dynamic sampling, filtering, deduplication, aggregation and edge processing, and shows Middleware's ingestion control pipeline as one implementation that keeps unnecessary logs out of storage.

## Who should watch

Engineers and leads who want a quick map of where observability tooling is heading, and anyone new to the OpenTelemetry collector. If you already run sampling and ML-based alerting in production, the talk is mostly confirmation; the value is in the framing and the cost checklist.

## Related Conf42 talks

- Shahar Azulay's [True Kubernetes Observability with eBPF](https://www.conf42.com/Cloud_Native_2023_Shahar_Azulay_kubernetes_observability_ebpf) expands on the eBPF data type Neel lists.
- Michael Levan's [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) applies the cost discipline to AI agent traffic.

[Watch Neel Shah's talk](https://www.conf42.com/Observability_2025_Neel_Shah_logs_metrics_traces)

[Watch the talk on YouTube](https://youtu.be/FYfEZ9302P0).

## Watch the talk

[Observability 2.0 - Much more than just logs,metrics and traces](https://www.conf42.com/Observability_2025_Neel_Shah_logs_metrics_traces) at Conf42 Observability 2025.
