# Green dashboards, failing checkout. An observability primer

Conf42 Blog, 2026-08-22. https://www.conf42.com/blog/obs2026/green-dashboards-failing-checkout-observability-101

In short: Emmanuela Opurum of SoftNet Technologies at Conf42 Observability 2026 explains, from zero, why dashboards miss customer pain and how to design for it.

Every dashboard is green, and customers still cannot pay. At Conf42 Observability 2026, Emmanuela Opurum, Solutions Architect at SoftNet Technologies, built a long, patient beginner's session around that scenario, and the answer she keeps returning to: a dashboard only answers the questions someone chose in advance, so observability has to start from the customer journey and be designed into the architecture, not bolted on later.

This is explicitly a first talk on observability. If you have never heard the word, Opurum promises you will not need to be an expert, and she means it. Experienced SREs will know most of the material; it is the talk to send to a new team member, a product owner, or an architect who has only ever seen monitoring from the outside.

## The dashboard is not lying, it is incomplete

The running example is an online shop. Servers up, errors low, CPU normal, and a stream of complaints from customers who cannot complete a payment. Opurum's point is that the dashboard is not wrong. It shows exactly what it was configured to show, and nobody configured it to show the customer's experience.

Her follow-up example makes it concrete: payments fail for customers in one availability zone while customers elsewhere pay fine, and the aggregate view stays green because whoever built it did not break it out by zone. The business does not care that the CPU looks healthy. It cares that people can pay and complete an order, so the signals have to line up with that.

## Logs, metrics and traces as clues

The middle of the talk explains the three signal types in plain terms. Logs are the system's diary, a record of events such as a payment starting and a payment service failing. Metrics are the numbers that show change over time. Traces show the journey of one request across services, which is where the most useful information about a checkout lives. Together they are telemetry, which she is at pains to say is less scary than it sounds.

She makes two points that beginners often miss. Collecting more telemetry does not automatically give you better observability; millions of log lines without a service name, version or ID will not answer a simple question during an incident. And good telemetry should never carry sensitive customer data. For cost, she suggests keeping errors and important journeys, sampling repetitive successful requests, and keeping some data, such as close monitoring of a new release, only for a short time.

She also introduces the four golden signals (latency, traffic, errors, saturation), SLIs and SLOs, and a rule worth repeating to any new on-call: not every change on a chart is an emergency. A CPU bump while customers keep paying is not a page. Too many unimportant alerts teach people to ignore all of them.

## Design it in, then test it on purpose

The architecture section follows the data: services emit logs, metrics and traces; instrumentation adds service name, version, IDs and timing; a collector receives and routes the data to the team's tools. OpenTelemetry gets a mention for giving teams a common way to collect telemetry without being tied to one vendor. But collection is not the goal; using it to find and fix problems before customers notice is.

Her lifecycle advice is the most practical part. During planning, pick the important customer journeys. During development, add the logs, metrics and traces they need. During testing, create a small, harmless problem on purpose and check that the metric shows it, the trace locates it and the logs explain it. After launch, alert on what affects customers. And after every incident, the system should be easier to understand next time.

## Who should watch

Newcomers to observability, students and cloud architects who want the reasoning before the tooling. It is long and deliberately repetitive, closer to a guided lesson than a conference sprint, so experienced engineers may prefer to skim. The closing advice works at any level, though: start with one critical journey, decide what success means, test the setup, then repeat for the next one.

[Watch Emmanuela Opurum's talk](https://www.conf42.com/Observability_2026_Emmanuela_Opurum_cloudnative_architecture_tracing) ([YouTube](https://youtu.be/Sy84i7OdVLM)).

## Related Conf42 talks

- [OpenTelemetry 101: A Beginner's Guide to Tracing, Metrics, and Logs on Observability](https://www.conf42.com/Observability_2024_Zameer_Fouzan_opentelemetry_beginners_tracing) by Zameer Fouzan (New Relic), Observability 2024: the hands-on next step.
- [The Failures You Don't See on Dashboards](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) by Abhimanyu Narwal (Bloomberg LP), SRE 2026.
- [Observability 2.0 - Much more than just logs, metrics and traces](https://www.conf42.com/Observability_2025_Neel_Shah_logs_metrics_traces) by Neel Shah (Middleware), Observability 2025.

## Watch the talk

[Beyond Dashboards: Building Observability into Modern Cloud Architectures](https://www.conf42.com/Observability_2026_Emmanuela_Opurum_cloudnative_architecture_tracing) at Conf42 Observability 2026.
