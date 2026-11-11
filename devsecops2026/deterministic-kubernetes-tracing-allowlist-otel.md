# Make Kubernetes debugging deterministic with mandatory trace context

Conf42 Blog, 2026-09-24, updated 2026-11-09. https://www.conf42.com/devsecops2026/deterministic-kubernetes-tracing-allowlist-otel

In short: At Conf42 DevSecOps 2026, Dell's Mridula Chilakamarri builds OpenTelemetry tracing that two engineers can't read two ways, with a nine-field allowlist.

Two engineers, one incident, two root causes. At Conf42 DevSecOps 2026, Mridula Chilakamarri, Product Manager at Dell Technologies building microservices platforms, called that non-deterministic debugging and showed the architecture that removes it: W3C Trace Context injected at ingress, propagation that is mandatory rather than polite, a deny-by-default list of nine trace fields, and telemetry that can never take a request down with it.

## Dashboards are not a shared identity

Her example app is the usual cast: authentication, cart, payment and inventory services, each owned by a different team and deployed on its own schedule. Logs sit in one system, metrics in another, traces are partial. The trace in her slide goes gateway, auth, cart, then a gap where the payment span should be. Whoever starts from cart data concludes one thing; whoever reads the scraps of payment data concludes another.

Teams think they have solved observability because they have lots of dashboards, she says, but logs, metrics and traces are collected as three silos with no common identifier. So you grep timestamps and hop. Per-service sampling quietly drops the exact failure you needed. And under SOC 2, HIPAA or PCI, not being able to reconstruct what happened is a compliance problem, not an inconvenience. The fix is not a fourth dashboard.

## Three decisions turn a standard into a guarantee

The foundation is the W3C traceparent header: version, a trace ID that stays constant for the whole request, a span ID per hop, and flags. She picks the standard over a home-grown correlation ID so that a service with the OpenTelemetry SDK, one behind a mesh and one with a vendor agent all speak the same header.

Then three choices. Trace identity is generated at the ingress gateway, so no request starts life untraceable. Context propagation is mandatory, the one she says she will defend hardest, because optional propagation creates gaps and gaps are where the worst incidents hide. And sampling, export targets and verbosity are configuration, not code, so you can tune telemetry during an incident without a redeploy.

## Telemetry off the request path

Each service records its span into a local buffer and the request moves on immediately. Spans are exported asynchronously to the OpenTelemetry Collector, which assembles traces for whatever backend you query by trace ID. If the collector is down or the vendor's network has a bad day, you drop spans and the request still returns 200.

She is pointed about why this must be structural rather than trusted to an SDK default or a timeout: the outage where your monitoring takes down your product, export calls blocking and threads piling up, is one of the most embarrassing kind there is. Observability that causes the incident it was meant to explain is the platform equivalent of the smoke alarm starting the fire.

## Deny by default for span attributes

Rich metadata is useful, and unrestricted metadata is how a trace store becomes a queryable copy of your most sensitive data. Nobody decides to leak; an engineer adds the request body or an auth header to debug something, it works, it stays, and that repeats across dozens of teams for years.

So the default is inverted to an allowlist of nine approved fields: trace ID, span ID, parent span ID, service name, operation name, timestamps, duration, status and HTTP response code. Everything else, payloads, headers, user data, never enters the pipeline. That one structural control is what lets the same design answer SOC 2 (reproducible records), HIPAA (no PHI in traces) and PCI DSS (no card numbers riding along in attributes).

## Seven checks you can run in CI

Her claims come as seven independently testable capabilities: a unique trace ID at ingress with existing IDs preserved; correct parent-child spans, with retries keeping the original trace ID; full trace-level capture; query by ID for the end-to-end path; config-only export with multiple backends and tenant routing; trace views, dependency graphs and per-span latency; and non-blocking, PII-free tracing. Because each is testable, "are we tracing-ready?" becomes a checklist rather than a judgement call.

Her worked scenario, checkout failing intermittently under load, shows the payoff: one engineer blames the database, another a downstream API, and a single failing trace shows the auth service exhausting its connection pool, with both earlier findings as symptoms.

## Who should watch

SREs and DevSecOps engineers who own both reliability and the audit, and platform teams rolling out OpenTelemetry across services they do not control. Practical, vendor-neutral, with lessons from production; the allowlist alone is worth the time.

## Related Conf42 talks

- [Narendra Reddy Sanikommu on OpenTelemetry's messy problems](https://www.conf42.com/Observability_2025_Narendra_Reddy_Sanikommu_opentelemetry_messy_problems), the candid counterpoint.
- [Bruno Ferreira on budget-friendly observability with the OpenTelemetry Collector](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector).
- [Zameer Fouzan's OpenTelemetry 101](https://www.conf42.com/Observability_2024_Zameer_Fouzan_opentelemetry_beginners_tracing), if traceparent is new to you.

[Watch Mridula Chilakamarri's talk](https://www.conf42.com/DevSecOps_2026_Mridula_Chilakamarri_kubernetes_opentelemetry_diagnostics)

[Watch the talk on YouTube](https://youtu.be/1_dgNKe-Vss).

## Watch the talk

[Deterministic Kubernetes Diagnostics with OpenTelemetry for Secure DevSecOps Operations](https://www.conf42.com/DevSecOps_2026_Mridula_Chilakamarri_kubernetes_opentelemetry_diagnostics) at Conf42 DevSecOps 2026.
