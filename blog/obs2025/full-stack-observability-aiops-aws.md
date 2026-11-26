# From MELT data to AIOps, one AWS service at a time

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/obs2025/full-stack-observability-aiops-aws

In short: Manik Kashikar of Thoughtworks maps full-stack observability and AIOps onto CloudWatch, X-Ray and DevOps Guru at Conf42 Observability 2025.

A checkout spike is rarely a frontend problem; it's often a database lock timeout or a flaky third-party payment API that nobody connected to the user's spinning button. At Conf42 Observability 2025, Manik Kashikar of Thoughtworks walked through how to get from siloed monitoring to full-stack observability and then to AIOps, with the AWS services that cover each step. It's a strategy-level talk with an AWS reference stack, not a hands-on demo.

## Visibility is the thing most teams don't have

Kashikar opens with a figure from a state of observability report: 89% of organisations say they still lack complete visibility into their systems, despite running several tools. Tool sprawl, long MTTR and exploding telemetry volume all push costs up. His ask is to treat observability as a first-class citizen, which means understanding why the system behaves as it does in real time, and ideally what it will do next.

The foundation is the MELT stack (metrics, events, logs, traces), but the value appears when you correlate those across application, infrastructure, business and user experience domains.

## The maturity curve ends at business context

His maturity model goes from siloed monitoring (logs and metrics without context) to telemetry tied to business KPIs like uptime, revenue impact and churn, and finally to full-stack observability, where infrastructure, applications, digital experience and business context are stitched together. The illustrative example: a 40 millisecond rise in response time that costs 2% in conversions is a business problem, not a graph.

To get there, he argues for two lenses at once. Outside-in captures what users experience: slow pages, failed transactions, latency. Inside-out surfaces backend response times, slow database queries, memory spikes and API gateway bottlenecks. Real observability joins the two, so the checkout spike points straight at the lock timeout.

## The AWS kit, layer by layer

For the observability layer, the talk maps the pieces: CloudWatch for native metrics and logs, X-Ray for distributed tracing across microservices, CloudWatch Synthetics to mimic user journeys and catch issues before customers do, and CloudWatch RUM for frontend latency and Core Web Vitals. The value, he says, is in composite dashboards that correlate them, for instance CloudWatch alarms with X-Ray traces to isolate bottlenecks.

## AIOps is observe, learn, act

Once telemetry is flowing in volume, AIOps is the natural next step. Kashikar breaks it into three pillars: observe (ingest clean, structured MELT data), learn (ML models for outliers, seasonality and failure prediction) and act (alert suppression, ticketing, dynamic scaling, even rollbacks). The example: if CPU spikes are always followed by database timeouts, the system learns the relationship, suppresses the noise and highlights the root cause.

On AWS, that means DevOps Guru for ML-powered operational insights, CloudWatch anomaly detection on time series metrics, and X-Ray Insights to tie traces to error rates. Chained together, DevOps Guru can spot a performance anomaly, link it to the failing X-Ray segment and fire an SNS alert into your incident management system.

He's candid about what slows teams down (data quality, integration complexity, resistance to change) and frames the outcome as fewer tickets and faster root cause, with every incident becoming training data.

## Who should watch

Engineering managers and architects on AWS who need a maturity model and a service map to justify the next observability investment. If you already run DevOps Guru in anger, you'll know most of this; if you're still on per-team dashboards, it's a solid roadmap. Other clouds have equivalents, and he says so.

## Related Conf42 talks

- Indika Wimalasuriya on [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws).
- Birol Yildiz on [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise).
- Mandi Walls on [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue), the non-ML way to cut noise.

[Watch Manik Kashikar's talk](https://www.conf42.com/Observability_2025_Manik_Kashikar_landscape_full_intelligent)

[Watch the talk on YouTube](https://youtu.be/3sA4EzjJdT0).

## Watch the talk

[Navigating the Digital Landscape with Intelligent Full Stack Observability](https://www.conf42.com/Observability_2025_Manik_Kashikar_landscape_full_intelligent) at Conf42 Observability 2025.
