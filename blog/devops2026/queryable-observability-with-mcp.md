# Observability has a context problem, so fix it where telemetry is born

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/queryable-observability-with-mcp

In short: Pronnoy Goswami of Workday at Conf42 DevOps 2026 on context-enriched telemetry, query APIs and an MCP layer that lets LLMs analyse metrics, logs and traces.

At 2am you do not lack data. You have terabytes of logs, millions of metrics and traces, and no thread tying them together. At Conf42 DevOps 2026, Pronnoy Goswami, a software engineer and tech lead at Workday, argued that observability has a context problem rather than a data shortage, and that the fix belongs at generation time: stamp the same context onto every signal, wrap the store in query APIs, and put a Model Context Protocol server in front so LLMs can do the cross-signal correlation humans currently do by hand.

His closing line sums it up: the observability problem is a data problem and should be solved at the data layer, not the inference layer.

## Why metrics, logs and traces do not add up

Metrics tell you what happened, logs why, traces where. Without a consistent thread of context, joining them is manual work under pressure. Pronnoy cites New Relic's 2023 Observability Forecast: half of organisations report siloed telemetry, and only a third have unified views across the three signal types.

## Layer one: enrich every signal with the same context

The architecture is three layers, illustrated with a payments checkout service. In the first, the service generates correlation IDs and builds a context dictionary (user ID, order ID, request ID, cart item count, payment method, service name and version) that goes onto every span, log line and metric.

His before-and-after debugging example is the convincing bit. Without context, an alert says payment failed and someone starts grepping. With context, the same error arrives carrying request, order, user and service, so you can follow the request ID straight to the failing hop, whether that is payment, fulfilment or the warehouse service.

## Layer two and three: query APIs, then an MCP server

The second layer is an MCP server acting as a structured query interface over the telemetry store (InfluxDB or Prometheus in his example). It indexes spans by context fields, filters by time window and other dimensions, and aggregates.

The third is the analysis engine. Given a time window, it pulls the relevant metrics, traces and logs by context, then computes statistical properties, using z-scores against the standard deviation, to flag anomalies and suggest a starting root cause. It is exposed through an API, so it can sit behind a Grafana panel or any other dashboard. Dashboards become a question box rather than a wall of charts.

Pronnoy points out that some vendors offer similar enrichment inside their own stack; the appeal of this design is that it stays vendor-agnostic.

## The results, and the obvious objection

In his team's implementation, which he describes as still fairly early, average time to resolution fell from about 45 minutes to about 8, an 82% reduction, with 65% less alert fatigue. He takes on the obvious objection, that this is a lot of overhead, by pointing at the costs teams already pay: on-call time, mostly unactionable alerts, constant context switching and dependence on a few people who know where things are. He estimates two to four weeks to set up one service and a break-even within roughly six to ten weeks.

His key insight line is worth keeping: complexity added at generation time removes far more complexity at analysis time.

## Start with one service

The takeaways are deliberately small:

- start with context enrichment on one high-traffic service, without the AI layer
- add a minimum viable context, such as owner team and service ID
- wrap existing tools with simple query APIs so data is AI-ready
- let real incidents shape the schema: add the fields engineers reach for, remove the ones nobody uses, and do not design the perfect schema up front

He has published sample code on his GitHub, linked from the talk.

## Who should watch

Teams already on OpenTelemetry who want LLM-assisted debugging without handing everything to one vendor. Even if you never build the MCP layer, the context-enrichment advice is a quick win on its own.

## Related Conf42 talks

- [Practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) by Nicolas Frankel covers the propagation basics layer one builds on.
- [From Prompt to Production Dashboard: Agentic AI with MCP Servers and Live Data](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) by Rohit Deshpande and Scott Young takes MCP over live data in a dashboard direction.
- [When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) by David McNerney and Daniel Raskin is a good reality check on what correlation can and cannot tell you.

[Watch Pronnoy Goswami's talk](https://www.conf42.com/DevOps_2026_Pronnoy_Goswami_observability_queries_context)

[Watch the talk on YouTube](https://youtu.be/a97Sa5nonZ8).

## Watch the talk

[From Signal to Insight: Building Queryable Observability with the Model Context Protocol](https://www.conf42.com/DevOps_2026_Pronnoy_Goswami_observability_queries_context) at Conf42 DevOps 2026.
