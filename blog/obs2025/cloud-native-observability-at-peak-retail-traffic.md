# Cloud-native observability, from API gateway to capacity planning

Conf42 Blog, 2025-06-05. https://www.conf42.com/blog/obs2025/cloud-native-observability-at-peak-retail-traffic

In short: Vamsi Krishna Munnangi of Walmart at Conf42 Observability 2025 on pillars, stateless vs stateful signals, API gateway telemetry and HA pipelines for peak traffic.

Monitoring tells you something is wrong; observability tells you why and how to fix it. That is the line Vamsi Krishna Munnangi, a senior software engineer in infrastructure engineering at Walmart, builds his Conf42 Observability 2025 talk on, using lessons from systems that have to survive Thanksgiving, Black Friday and holiday peaks.

It is a structured survey that covers a lot of ground in 30 minutes. The best sections are the practical ones on API gateways and on keeping the observability pipeline itself highly available.

## Stateless and stateful services need different signals

Munnangi makes a distinction many overviews skip. For stateless services such as load-balanced APIs, watch throughput, latency and resource use with horizontal scaling in mind, and lean on tracing individual requests and analysing errors. For stateful services such as databases, track persistence signals: replication health, consistency and storage performance. His example is Google Cloud Spanner and keeping data durable across regions. Health probes and anomaly detection are the shared patterns across both.

## Tracing done with intent

His tracing recipe has four steps. Instrument code and propagate trace context with OpenTelemetry. Configure intelligent sampling: keep 100% of critical paths, sample the rest (he suggests something like one in a thousand) and make sure both normal and exceptional patterns are represented. Centralise the pipeline on scalable transport such as Kafka or GCP Pub/Sub. Then visualise traces in Jaeger to find bottlenecks. For the three pillars he names Prometheus for metrics, the ELK stack for logs and Jaeger for traces.

## The API gateway is an observability hub

The gateway section is the one to watch. As the point where external traffic enters the internal world, the gateway sees request volumes, service dependencies, rate-limiting effectiveness, authentication events and attack patterns worth handing to the security team. He mentions traffic ranging from a few hundred to tens of thousands of requests per second at peak, and tooling combinations such as Azure API Management with Application Insights, Apigee with Stackdriver, and Kong or NGINX with Prometheus and Grafana.

The best practices are a usable checklist: structured access logs with correlation IDs, rate limiting and circuit breakers that expose metrics, tracing headers instrumented at the gateway, and latency percentiles (p50, p95, p99) for SLO enforcement.

## Keep the observability pipeline highly available

A pipeline that goes down with the system it watches is not much use. Munnangi's four-stage pipeline (collection, processing and filtering, tiered hot and cold storage, visualisation) is backed by HA practices: collectors and storage across multiple availability zones, monitoring at node, zone and region level, tracking failover events and MTTR, correlating signals across clouds and auditing cross-cloud failover and data sync. Local buffering keeps metrics when a connection drops, and multi-channel alerting through Slack, email and PagerDuty means one dead channel does not silence a page.

## Capacity planning from the same data

Finally, the telemetry feeds capacity planning: aggregate months of utilisation data, forecast seasonal spikes with machine learning, autoscale to balance cost and performance, and compare forecasts with actual consumption to refine the models. His roadmap ends where most good ones do: Prometheus and centralised logging first, SLIs and SLOs for core services, then tracing and team dashboards, then automated detection and remediation. Start with one service and scale.

## Who should watch

Platform and SRE engineers designing observability for high-traffic microservices, especially anyone who owns an API gateway. Parts of the talk cite percentage improvements from studies and production systems without much detail, so value it for the patterns more than the numbers.

## Related Conf42 talks

- [Observe your API with API Gateway Plugins](https://www.conf42.com/Observability_2023_Bobur_Umurzokov_api_gateway_plugins) by Bobur Umurzokov at Conf42 Observability 2023.
- [Modern API Gateways: Data-Driven Reliability for Microservices & Serverless](https://www.conf42.com/Incident_Management_2025_Vijaykumar_Pasunoori_apigateways_microservices_serverless) by Vijaykumar Pasunoori at Conf42 Incident Management 2025.
- [Automating peak readiness: turning observability signals into workload engineering insights](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning) by Vasuki Uday Kiran Vudathala at Conf42 Observability 2026.

[Watch Vamsi Krishna Munnangi's talk](https://www.conf42.com/Observability_2025_Vamsi_Krishna_Munnangi_visible_resilient_scalable) or the [YouTube recording](https://youtu.be/xSYwSeMXOvA).

## Watch the talk

[Cloud-Native Observability: Building Visible, Resilient, and Scalable Enterprise Systems](https://www.conf42.com/Observability_2025_Vamsi_Krishna_Munnangi_visible_resilient_scalable) at Conf42 Observability 2025.
