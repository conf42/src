# Pick AWS observability tools by function, not by familiarity

Conf42 Blog, 2025-05-16. https://www.conf42.com/blog/obs2025/aws-observability-tools-function-or-friction

In short: Prudhvi Raj Atluri of Quantiphi at Conf42 Observability 2025 maps CloudWatch, X-Ray, Managed Grafana, QuickSight and OpenTelemetry to the jobs they fit.

Using QuickSight as a real-time monitoring tool is a good way to learn what "periodic refresh" means during an outage. At Conf42 Observability 2025, Prudhvi Raj Atluri, Associate Architect for Data at Quantiphi with more than ten years building analytics platforms on AWS, built his talk around that kind of mismatch: managed services picked for the wrong job create blind spots, alert fatigue and ballooning costs.

His lens is simple and reusable. A tool adds function when it speeds up insight and integrates at scale. It adds friction when it brings noise, lag and complexity.

## The AWS toolbox, sorted by job

Atluri walks through the core services and what each is for. CloudWatch is the general-purpose foundation: log collection, metric aggregation, dashboards, alarms and automated actions. X-Ray traces requests end to end through distributed applications, the tool for finding which microservice is slow. Amazon Managed Grafana is for rich, real-time visualisation across AWS services and open source data sources. QuickSight is BI: interactive dashboards and natural language queries, with periodic data refresh, explicitly not real time. And AWS Distro for OpenTelemetry gives vendor-neutral, standardised instrumentation across stacks.

He then widens the list to the governance and optimisation side: CloudTrail for auditing every API action, AWS Config for continuous resource configuration checks, DevOps Guru for ML-based anomaly detection with suggested root causes, Trusted Advisor for best-practice checks, Compute Optimizer for right-sizing, and Inspector for automated security scans on EC2, Lambda and containers.

## Function, by example

The function examples are the recommended defaults. CloudWatch alarms for real-time alerts on EC2, Lambda metrics and Container Insights. X-Ray to pinpoint bottlenecks across API Gateway and Lambda flows using service maps. Grafana, his favourite, for live dashboards over CloudWatch, Prometheus and other sources, including SLO tracking. And OpenTelemetry for unified instrumentation across ECS, EKS or hybrid environments, sending data to CloudWatch or third-party tools.

## Friction, by example

The friction examples are the ones worth remembering. QuickSight for real-time monitoring, where batch refresh guarantees lag. CloudWatch Logs at scale without structured queries, which turns unstructured log data into reduced visibility. And overlapping tools without integration, which fragments data and slows collaboration. Tool sprawl rarely looks like a decision; it looks like five teams each making a reasonable one.

## Architecture patterns and where AI fits

For architecture he describes four patterns: a centralised telemetry pipeline using S3 and OpenSearch; real-time monitoring with Grafana and CloudWatch plus SNS or SES notifications; AI/ML integration through SageMaker and Bedrock for predictive analysis and anomaly detection; and automated response with Lambda and EventBridge for remediation and scaling. His view of GenAI in observability is measured: predictive analytics, automated root cause suggestions, natural language questions about system behaviour, and smarter alert filtering to cut noise.

## Best practices

The closing advice is short. Build observability in at design time rather than bolting it on. Align SLOs and SLIs with business KPIs. Automate alert generation and root cause analysis where you can. And keep reviewing the pipeline and tool choices so they stay relevant as the system changes.

## Who should watch

Teams designing or cleaning up an AWS observability stack, and architects who need a quick map of which native service does what. It stays high level by design, so experienced CloudWatch and X-Ray users will mostly get the framework, not new tricks.

## Related Conf42 talks

- [AWS: Your Ally Against Observability Anti-Patterns](https://www.conf42.com/Observability_2024_Indika_Wimalasuriya_ally_antipatterns_aws) by Indika Wimalasuriya at Conf42 Observability 2024.
- [OpenTelemetry 101: A Beginner's Guide to Tracing, Metrics, and Logs on Observability](https://www.conf42.com/Observability_2024_Zameer_Fouzan_opentelemetry_beginners_tracing) by Zameer Fouzan at Conf42 Observability 2024.
- [Network X-Ray Vision: Harnessing eBPF for Cloud-Native Observability](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sai_KR_Pentaparthi_xray_ebpf_o11y) by Sai KR Pentaparthi at Conf42 Site Reliability Engineering 2025.

[Watch Prudhvi Raj Atluri's talk](https://www.conf42.com/Observability_2025_Prudhvi_Raj_Atluri_stack_observability_aws) or the [YouTube recording](https://youtu.be/DlRaIo86zq8).

## Watch the talk

[Function vs. Friction: Designing the Right Observability Stack in AWS Cloud](https://www.conf42.com/Observability_2025_Prudhvi_Raj_Atluri_stack_observability_aws) at Conf42 Observability 2025.
