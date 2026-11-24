# Cut the Kubernetes observability bill by collecting better signals

Conf42 Blog, 2025-05-28, updated 2026-11-09. https://www.conf42.com/blog/obs2025/kubernetes-observability-bill-signals-budget

In short: Aritra Ghosh of Microsoft at Conf42 Observability 2025 on trimming Kubernetes monitoring costs layer by layer, from control plane to network, with budgets.

Observability can eat up to 40% of a cloud bill, and in Kubernetes a lot of that data shows up whether you asked for it or not. At Conf42 Observability 2025, Aritra Ghosh, a senior product manager at Microsoft working on cloud-native monitoring, walked through where that money goes and how to cut it layer by layer without going blind.

His closing mantra sums up the talk: better signals mean lower cost and happier engineers.

## Where the money actually goes

Aritra names four spending sinks he sees in enterprises:

- **High-cardinality custom metrics**, priced separately by most tools and inflated by labels like user ID.
- **Long log retention and verbose logging**, with debug logs left on and kept for 30 or 90 days.
- **The same data shipped to several destinations**, paying storage more than once.
- **Cross-region and cross-network traffic**, which adds egress on top of storage.

Cloud-native makes this worse because pods spin up and down constantly and some telemetry is generated outside your direct control.

## Start from SLOs, then rank the signals

The framework is: collect what matters, choose the right signal, tune retention and aggregation, and consolidate or offload the rest. Start with service level objectives, because that is what users feel. Then rank by value: metrics first (they drive alerting), traces second (they show the path between services), logs last (they explain what went wrong inside one service). That ranking is a useful corrective for teams whose bill is 80% logs.

## Four layers, four diets

The Kubernetes-specific part splits monitoring into four components:

- **Control plane:** ingest managed-service metrics such as API server latency and health checks instead of full logs, and alert on deviation from expected behaviour rather than static thresholds.
- **Nodes:** track CPU, memory and disk IO, watch heartbeats and node-ready transitions, and skip per-process metrics unless you are actively debugging.
- **Pods:** filter health checks and static endpoints at the source, and use labels and OpenTelemetry auto-tagging to tie telemetry to services.
- **Network:** focus on connection failures and DNS resolution problems, sample flow records such as NetFlow or IPFIX, and prefer eBPF-based tooling.

On OpenTelemetry he recommends explicit aggregation temporality, dropping labels to cut cardinality, and limiting custom metrics to business-critical paths.

## A budget, not just a dashboard

The organisational advice is the part many cost talks skip. Build a cost-aware dashboard showing spend per telemetry type, then attribute it to teams with tags so chargebacks are at least visible. Then set an observability budget: a monthly cap per cluster, with quotas on log volume and custom metrics enforced through tools like Fluent Bit and Loki.

His checklist runs drop, shorten retention, filter at source, consolidate tools, tune alerts. On cardinality: keep user IDs and UUIDs out of metric labels and use tier, region or status code. On alerts: funnel raw data to filtered to routed to actionable, and page only on SLO violations or customer impact.

He illustrates the result with an explicitly fictional customer that reached a 40% saving by dropping health check logs, lowering verbosity, replacing raw latency logs with Prometheus histograms and moving cold data to object storage. It is labelled as an illustration, not a benchmark, and the trade-off curve that follows makes the real point: past a certain volume, more telemetry adds cost but not insight.

## Who should watch

Kubernetes platform teams and engineering managers who own the monitoring line item. The tool list at the end (Prometheus with Thanos or Cortex, Fluent Bit, the OpenTelemetry Collector, Grafana, Cilium) is a sensible open-source baseline.

## Related Conf42 talks

- [Bruno Ferreira on budget-friendly insights with the OpenTelemetry Collector](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) (DevOps 2024).
- [Michael Levan on cost and resource optimization in Kubernetes](https://www.conf42.com/Kube_Native_2023_Michael_Levan_cost_resource_optimization) (Kube Native 2023).
- [Roman Khavronenko on measuring PromQL and MetricsQL expression complexity](https://www.conf42.com/Observability_2024_Roman_Khavronenko_measure_promql_metricsql) (Observability 2024), for what cardinality does to your queries.

[Watch Aritra Ghosh's talk](https://www.conf42.com/Observability_2025_Aritra_Ghosh_shrinking_kubernetes_cost)

[Watch the talk on YouTube](https://youtu.be/X--SntuCCTg).

## Watch the talk

[Shrinking the Observability Bill: Smart Strategies for Cost-Effective Kubernetes Monitoring](https://www.conf42.com/Observability_2025_Aritra_Ghosh_shrinking_kubernetes_cost) at Conf42 Observability 2025.
