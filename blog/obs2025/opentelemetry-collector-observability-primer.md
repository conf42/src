# Monitoring says it broke; OpenTelemetry helps you find out why

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/opentelemetry-collector-observability-primer

In short: Naga Murali Krishna Koneru of Hexaware at Conf42 Observability 2025 explains observability basics and the OpenTelemetry Collector with Loki, Mimir and Grafana.

"Monitoring shows you're broken - observability tells you why." That line from the abstract is the thesis of Naga Murali Krishna Koneru's talk at Conf42 Observability 2025. Naga, a technical architect at Hexaware Technologies working on AWS, DevOps and DevSecOps, walked from the vocabulary of observability to a working OpenTelemetry Collector setup that hides Loki, Mimir and Grafana behind a single endpoint.

It is a primer, and a well-organised one: if you are the person on your team who has to explain OpenTelemetry to everyone else, this is a good script.

## The methods you measure with

Naga grounds everything in two outcomes: mean time to detection and mean time to resolution. Then he lines up the standard measurement methods side by side:

- **RED:** rate, errors and duration, for request-driven services.
- **USE:** utilisation, saturation and errors, for resources such as CPU, disk and network queues.
- **Google's four golden signals:** latency, traffic, errors and saturation.
- **Core Web Vitals:** LCP, FID and CLS, for what the user's browser experiences.

His distinction between monitoring and observability is practical: monitoring tracks known issues and suits small or monolithic systems; observability uncovers unknown unknowns in complex systems and tells you where, when and why.

## Four signal types, two ways to collect

He covers the signal types with a one-line job for each: metrics say what is happening, logs say what happened and when, traces show where in the request path the bottleneck is, and profiles explain why at the resource level (CPU, garbage collection).

Push versus scrape gets a decision rule. Scrape, as Prometheus does, when running on Kubernetes or other dynamic environments and apps can expose an HTTP endpoint. Push, as with StatsD to Graphite, when apps are short-lived, need real-time metrics, or sit in restricted networks where nothing can scrape them.

## The Collector is the part to understand

The OpenTelemetry section explains the project (a CNCF project, vendor-neutral, multi-language) and then focuses on the Collector: receivers as entry points, processors that filter, enrich or sample, exporters that ship to back ends, plus connectors that link pipelines and extensions that add capabilities. A pipeline can have several of each.

He lists where telemetry comes from in a typical Kubernetes setup: SDK-instrumented apps, service meshes such as Istio, node and pod metrics, cluster events, Fluentd and Fluent Bit for container logs, cloud provider metrics, liveness and readiness probes, and container runtime data. On instrumentation, auto-instrumentation gets you visibility quickly with little effort, while manual instrumentation gives precise control over business-specific signals.

## One endpoint, many back ends

The closing architecture is the takeaway. Two VMs run Fluent Bit for logs and node exporter for metrics. Both talk only to the OpenTelemetry Collector, which routes logs to Loki and metrics to Mimir, with Grafana on top (Tempo is the tracing piece of the same stack). The applications never need to know which back ends exist, so swapping one later does not touch application code. The full stack, from bottom to top, is instrumentation, collection, storage and visualisation.

## Who should watch

Engineers new to OpenTelemetry, and leads who need a structured overview to onboard a team. Experienced Collector operators will find it introductory.

## Related Conf42 talks

- [Zameer Fouzan's OpenTelemetry 101 on tracing, metrics and logs](https://www.conf42.com/Observability_2024_Zameer_Fouzan_opentelemetry_beginners_tracing) (Observability 2024).
- [Prathamesh Sonpatki's complete handbook to OpenTelemetry metrics](https://www.conf42.com/DevOps_2024_Prathamesh_Sonpatki_handbook_opentelemetry_metrics) (DevOps 2024).
- [Nicolas Frankel's practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) (DevOps 2023).

[Watch Naga Murali Krishna Koneru's talk](https://www.conf42.com/Observability_2025_Naga_Murali_Krishna_Koneru_chaos_modern_systems)

[Watch the talk on YouTube](https://youtu.be/yFUfDdD46OY).

## Watch the talk

[Observability: Seeing Through the Chaos of Modern Systems](https://www.conf42.com/Observability_2025_Naga_Murali_Krishna_Koneru_chaos_modern_systems) at Conf42 Observability 2025.
