# Sample synthetic tests at 100% and aggregate the traces

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/synthetic-traces-critical-user-journeys-salesforce

In short: Sudeep Kumar of Salesforce at Conf42 Observability 2025 on turning fully sampled synthetic traces into aggregated views of critical user journeys.

Synthetic tests tell you a user journey failed; traces tell you which of the many services in that journey did it. At Conf42 Observability 2025, Sudeep Kumar, a principal engineer in Salesforce's Monitoring Cloud organisation, showed how his team traces every synthetic test run at full sampling and then aggregates those traces into views that point straight at the slow or failing service.

The scale is the first thing he puts on the table: observability for over a million hosts and containers, more than 2,000 teams and 13,000 developers, and more than 300 billion spans a day.

## Critical user journeys are hero flows

Sudeep defines critical user journeys (CUJs) as "hero flows": high-value, customer-facing, business-critical request paths, often revenue-impacting. In a microservices estate those paths cross many services, so when an incident hits, finding the guilty hop is the slow part. Distributed tracing answers the key questions: which services sit on the critical path, how healthy those transactions are, and where the bottleneck is. Because journeys change as features ship, tracing also exposes new and unwanted access patterns.

His advice on instrumentation is unglamorous and correct: on CUJ paths, add spans manually, one at a time, where they add value. Those spans become your best signals.

## A refresher that sets up the trick

He walks through the semantics: each service emits spans with a start time, duration and operation, all tied to one trace ID and assembled into a waterfall. Context propagates through transport headers (Salesforce uses B3 headers for legacy reasons; OpenTelemetry headers work too). The detail that matters later is the sampling flag: if it is zero, downstream services propagate context but do not emit spans, which is how most platforms keep trace volume affordable.

## Synthetic tests get 100% sampling

That is the core idea. Ordinary traffic is sampled; synthetic tests that emulate a CUJ are always sampled at 100%, so every run is captured end to end. Each test is a set of templated steps, each step emitting its own trace tied to the test ID, and variables let the same definition run from Europe, Japan or the US. The result is an outside-in view of performance and availability: browser, APM and DNS monitoring included.

Drilling into one failed run, linking to its trace IDs and opening the waterfall works. But looking at runs one by one does not scale.

## Aggregation is where the gold is

The payoff is aggregation across similar traces:

- **Latency contributors:** a "create account" transaction takes around 85 milliseconds, and the metric alone does not say where. Aggregating similar traces into a time series shows which operation (here, authentication) dominates.
- **Slice and compare:** the same view for errors, per step, per region variable, against a baseline for week-over-week trends.
- **Directed graphs:** an aggregated graph of the request flow with per-edge health, such as 72 runs of a test with 12 failing on the call to one app. Since synthetic traces are fully sampled, nothing is missing from that picture.

He finishes with three on-demand options for when synthetic coverage is not enough: tracing for one specific user, long-running tracing to catch sporadic issues, and per-instance tracing for a single tenant's instance.

## Who should watch

SREs and observability platform engineers who run synthetic checks and tracing as separate tools and suspect they should talk to each other. You need a tracing back end you control to build the aggregation views; the design ideas transfer anyway.

## Related Conf42 talks

- [Justin Scherer and Justin Snyder on RESTifying OpenTelemetry traces](https://www.conf42.com/Observability_2024_Justin_Scherer_Justin_Snyder_restifying_traces_tracing) (Observability 2024).
- [Siddhartha Khare on tracing in CI/CD](https://www.conf42.com/Cloud_Native_2024_Siddhartha_Khare_tracing_triumph_o11y) (Cloud Native 2024), another place to trace synthetic work.
- [Eleftheria Batsou on why your app can be up while your business is down](https://www.conf42.com/Observability_2026_Eleftheria_Batsou_healthchecks_outages_dependencies) (Observability 2026), the case for outside-in checks.

[Watch Sudeep Kumar's talk](https://www.conf42.com/Observability_2025_Sudeep_Kumar_traces_user_synthetic)

[Watch the talk on YouTube](https://youtu.be/1aGN1I3x0aE).

## Watch the talk

[Turning Synthetic Traces into Gold: Scalable Monitoring for Critical User Journeys](https://www.conf42.com/Observability_2025_Sudeep_Kumar_traces_user_synthetic) at Conf42 Observability 2025.
