# Informatica filters telemetry at the source and lets AI run the pipes

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/informatica-telemetry-pipeline-ai

In short: Kirti Ranjan Parida and Sarav Jagadeesan show at Conf42 Observability 2025 how Informatica cut telemetry noise with OpenTelemetry filters and AI agents.

Sixty terabytes of logs a day is the point where every unnecessary log line has a network bill attached. At Conf42 Observability 2025, Sarav Jagadeesan, Director of Platform Engineering and Infrastructure, and Kirti Ranjan Parida, DevOps Architect, both at Informatica, described how they rebuilt the company's telemetry pipeline: filter at the agent, shape data centrally, and use AI agents (with a human approving) to build and maintain the pipelines themselves. The payoff they describe is lower cost, faster dashboards and lower MTTR.

## The scale that forced the rethink

Jagadeesan opens with Informatica's footprint: four hyperscalers (AWS, Azure, Google Cloud and Oracle), around 20 regions, more than 600 Kubernetes clusters and thousands of nodes and VMs. That produces about 60 TB of logs every day and 3.8 trillion documents ingested a month, with roughly 15 PB stored on S3.

The old design shipped logs from every region and availability zone into a central Kafka queue, then into the data store, visualised in Kibana, Grafana and a homegrown analytics tool. At that volume it meant rising cost, operational overhead and slow dashboards.

## The expensive part is the collector, not the backend

Parida's key finding: after adding a central telemetry pipeline, they realised most of the cost came from the agents collecting logs and shipping them across the network, where NAT gateway and transfer fees pile up. So the fix moved left. They standardised on an OpenTelemetry-based agent with filters (and ML models) at the source to drop noise before it ever crosses the network; the talk credits that step with about a 20% reduction.

The central pipeline then reshapes what's left:

- **Logs that are really metrics** get converted and stored in the metrics system, which is far cheaper than storing them as logs.
- **High-volume, low-value data** such as health checks gets downsampled to a summary.
- **PII** gets masked in one central place before long-term storage.

Less data means lower cardinality, faster search and dashboards, and lower storage and backup costs. A single agent covers all telemetry signals and is managed by fleet management, so config changes don't mean touching every host.

## AI agents build the pipelines, humans approve them

The catch with all this control was the human effort to create pipelines, maintain them and keep up with new data patterns. Informatica's answer is an AI agent that takes a natural language request, knows the pipeline transforms and query languages, and can create or modify pipelines and recommend optimisations based on the shape of the data. It doesn't deploy on its own: a human reviews and approves, then the agent rolls it out. That human-in-the-loop design is the detail worth stealing.

A second AI assistant faces the people investigating incidents. Ask in plain language, and it translates to the observability system's query language, correlates traces, metrics and logs, draws a basic visualisation, and can run routine runbooks. Combined with APM context propagation, service maps and ML anomaly detection on response times and error rates, it means you don't need the one expert who knows which dashboard to open on every incident call. That's where the MTTR improvement comes from.

## Who should watch

Platform and observability teams paying for telemetry at multi-cloud scale, especially anyone who has only optimised the backend. The talk is architectural rather than a code walkthrough, but the sequence (filter at source, convert logs to metrics, downsample, mask, then automate with a human gate) is directly reusable.

## Related Conf42 talks

- Pranay Prateek on [Scaling Opentelemetry Collectors using Kafka](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pranay_Prateek_scaling_opentelemetry_kafka).
- Nishanth Vepachedu on [Scaling Microservices Observability with Agentic LLMs](https://www.conf42.com/MLOps_2026_Nishanth_Vepachedu_microservices_observability_llms).
- Prathamesh Sonpatki on [The Complete Handbook to OpenTelemetry Metrics](https://www.conf42.com/DevOps_2024_Prathamesh_Sonpatki_handbook_opentelemetry_metrics), handy once your logs become metrics.

[Watch the talk by Kirti Ranjan Parida and Sarav Jagadeesan](https://www.conf42.com/Observability_2025_Kirti_Ranjan_Parida_Sarav_Jagadeesan_mttr_pipelines_reduce)

[Watch the talk on YouTube](https://youtu.be/y4hSuAEs5uo).

## Watch the talk

[Next-Gen Observability: Leveraging AI and Data Pipelines to reduce Cost and MTTR](https://www.conf42.com/Observability_2025_Kirti_Ranjan_Parida_Sarav_Jagadeesan_mttr_pipelines_reduce) at Conf42 Observability 2025.
