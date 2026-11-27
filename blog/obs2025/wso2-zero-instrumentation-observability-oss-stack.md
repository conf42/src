# How WSO2 rebuilt Choreo observability on open source for 70% less

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/wso2-zero-instrumentation-observability-oss-stack

In short: Isala Piyarisi and Nilushan Costa of WSO2 at Conf42 Observability 2025 on Fluent Bit, OpenSearch, Prometheus and eBPF zero-instrumentation metrics.

WSO2 moved the observability behind its Choreo internal developer platform off Azure-native services and onto Fluent Bit, OpenSearch and Prometheus, and the abstract claims log latency under five seconds with roughly 70% lower cost. At Conf42 Observability 2025, Nilushan Costa, associate technical lead, and Isala Piyarisi, senior software engineer, both on the Choreo observability team, explained the migration, the eBPF-based zero-instrumentation metrics, and the lessons they paid for along the way.

This is one of the more detailed architecture talks of the event, with real component names, failure stories and a cost breakdown.

## Why they left an Azure-only setup

Choreo started on Azure, with logs going through Azure agents into Log Analytics, and traces and metrics through an OpenTelemetry Collector into Azure Data Explorer. Three things pushed them off it. Cost: publishing and querying telemetry in a cloud platform is expensive. Portability: customers wanted Choreo data planes on AWS, on Vultr and on-premises, and each cloud has its own query language and APIs. Control: owning the stack meant they could build features on top of it.

## Logs: Fluent Bit, OpenSearch, and an operator

Fluent Bit runs as a DaemonSet collecting container logs into OpenSearch, which they had already used as a short-lived cache alongside Log Analytics and liked. The new setup runs OpenSearch as a distributed deployment with separate master and data nodes, managed by the OpenSearch operator, because Choreo also runs private data planes per customer and manual upgrades across many clusters would be slow and error-prone. Primary and replica shards are spread across availability zones, so a lost pod or deleted volume recovers from its peers.

## Metrics without asking anyone to instrument

The zero-instrumentation side is the part many teams will want to copy. Prometheus, managed by the Prometheus operator and backed by Thanos for retention and high availability, scrapes three sources: kube-state-metrics for Kubernetes context like labels and resource requests, cAdvisor in the kubelet for per-container CPU and memory, and Hubble from Cilium for HTTP-level and layer 3/4 metrics such as status codes and latencies, with no code changes from users. They described routing traffic through an Envoy proxy on the node with eBPF to extract RED metrics without the overhead of a full service mesh. All of it feeds a dynamically generated service diagram showing error rates and latency between components, and clicking a spike pulls the related logs.

## The lessons they learned the hard way

The war stories are the best part:

- **Prometheus counts are estimates.** Send 15 requests and the diagram might show 13.8. Their older event-based system showed exact counts; Prometheus gives aggregated data, so use something else if you need exact numbers, for billing for example.
- **Order of operations matters.** Taking a rate over a recording rule that had already summed data produced wrong results.
- **Storage is part of observability.** An AWS deployment on EFS underperformed; switching to EBS fixed it, and Fluent Bit's metrics alone would not have told you why.
- **Config details bite.** The inotify watcher in Fluent Bit's tail plugin stopped collecting logs after a while; switching to the stat-based watcher fixed it. They also wrote a Lua script for log throttling so Fluent Bit cannot overwhelm OpenSearch.

## The cost numbers

Per data plane, the old setup cost around $1,200 a month for Azure Data Explorer and about $1,000 for Log Analytics. The open-source stack costs roughly $250 for compute and $100 for storage, which they put at about 70% overall savings, plus more control and better performance.

## Who should watch

Platform teams running Kubernetes across several clouds or on-premises, and anyone with an expensive managed observability bill wondering what self-hosting really involves. You will leave with a component list and a short catalogue of traps.

## Related Conf42 talks

- Nikolay Sivko's [Zero-instrumentation observability based on eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) on the same idea from another angle.
- Pranshu Srivastava's [The Power of Cilium For eBPF](https://www.conf42.com/Golang_2025_Pranshu_Srivastava_cilium_ebpf_networking) for the Cilium side that Hubble comes from.
- Alejandro Mercado's [Observability in Kubernetes with eBPF](https://www.conf42.com/Kube_Native_2025_Alejandro_Mercado_observability_kubernetes_ebpf).

[Watch Isala Piyarisi and Nilushan Costa's talk](https://www.conf42.com/Observability_2025_Isala_Piyarisi_Nilushan_Costa_fluent_opensearch_zero)

[Watch the talk on YouTube](https://youtu.be/DswnTMsGk1E).

## Watch the talk

[Faster, Cheaper, Smarter: Lessons from Building Zero-Instrumentation Observability with Fluent Bit OpenSearch & Prometheus](https://www.conf42.com/Observability_2025_Isala_Piyarisi_Nilushan_Costa_fluent_opensearch_zero) at Conf42 Observability 2025.
