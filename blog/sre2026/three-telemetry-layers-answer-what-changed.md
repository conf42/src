# Three telemetry layers that answer "what changed?" in an incident

Conf42 Blog, 2026-03-07, updated 2026-11-09. https://www.conf42.com/blog/sre2026/three-telemetry-layers-answer-what-changed

In short: Khushboo Nigam (Oracle) at Conf42 SRE 2026 on organizing traces, Kubernetes signals and CI/CD telemetry so incident triage follows evidence.

The alert already tells you something is wrong; the question you actually ask next is "what changed?" At Conf42 Site Reliability Engineering (SRE) 2026, Khushboo Nigam, Principal Cloud Architect at Oracle, presented a layered observability framework that sorts telemetry by the investigation question it answers, so an engineer can move from user impact to platform health to the deployment that caused it without becoming the manual integration layer.

Her one-line thesis is the talk's title: correlation over collection.

## A clarity problem, not a data problem

Khushboo's diagnosis is that most teams already collect plenty: infrastructure metrics, logs, traces, deployment events, a pile of alerts. Each signal has value, but on its own it doesn't tell a story. During an incident they all compete for attention at once, and the on-call engineer ends up stitching them together by hand under pressure.

She draws the usual line between monitoring and observability, and it's a useful refresher. Monitoring catches known failure conditions: CPU above 90%, latency above 500 milliseconds, the known knowns. Observability is for the unknown unknowns, the failures nobody wrote an alert for. Neither helps if the telemetry has no shared context linking a latency spike, a timeout in the logs, a slow span and last night's release.

## Organize signals by the question they answer

The framework has three layers, each tied to one question:

1. **Application traces: where is it failing?** Follow the request across services and find the slow or failing span.
2. **Kubernetes metrics and events: is the platform healthy?** Node resource pressure, pod restarts, crash loops, scheduling problems.
3. **CI/CD telemetry: what changed?** Deployments, version bumps, configuration changes, pipeline results.

The order matters. You narrow from the whole system to one component, then decide whether the platform or the application is at fault, then look for the change.

## Enrich spans so you can pivot

The demo uses a retail microservices app on managed Kubernetes: a load balancer, a web frontend, an API backend with a payment operation, and an external database. Telemetry flows through the OpenTelemetry Collector plus cloud-native services into separate backends for application monitoring, logs and metrics.

The key move is in the collector: it enriches application spans with Kubernetes metadata, so the payment span that shows the error and high latency also carries the node name, pod name and pod IP. That's the pivot from layer one to layer two; you jump straight to that node's resource usage and that pod's events. Further down the same span sits the service version and the error message from the application's instrumentation. If the platform looks healthy and errors began right after a deploy, the version in the span tells you which release to look at.

Put together, telemetry becomes what she calls a structured hierarchy of evidence, with each layer narrowing the search rather than adding more noise.

## Know what your provider owns

One aside is easy to skip and shouldn't be. On managed Kubernetes, the control plane (API server, etcd) is usually the cloud provider's responsibility, while nodes and workloads are yours. Khushboo's advice: read your provider's policy, find out which metrics and logs they expose for the parts they manage, and know in advance when to escalate rather than debug.

## Who should watch

SREs whose incident response still starts with opening five dashboards, and platform teams setting up OpenTelemetry who want a reason to enrich spans with Kubernetes and deployment metadata. The framework is platform-agnostic and clearly explained; it's not a vendor pitch.

## Related Conf42 talks

- [Practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) by Nicolas Frankel (Apache APISIX), if layer one needs work first.
- [Deterministic Kubernetes Diagnostics with OpenTelemetry](https://www.conf42.com/DevSecOps_2026_Mridula_Chilakamarri_kubernetes_opentelemetry_diagnostics) by Mridula Chilakamarri (Dell Technologies), on the layer two side.
- [Optimizing Observability with OpenTelemetry Collector for Budget-Friendly Insights](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) by Bruno Ferreira (TheyDo), for the collector doing the enrichment.

[Watch Khushboo Nigam's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Khushboo_Nigam_correlation_over_collection)

[Watch the talk on YouTube](https://youtu.be/0VC_JuqimbY).

## Watch the talk

[Correlation Over Collection: A Layered Observability Framework for SREs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Khushboo_Nigam_correlation_over_collection) at Conf42 Site Reliability Engineering (SRE) 2026.
