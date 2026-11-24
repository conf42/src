# Kafka stalls quietly. Metrics, events, logs and traces catch it

Conf42 Blog, 2025-05-30, updated 2026-11-09. https://www.conf42.com/blog/obs2025/kafka-observability-melt-stack

In short: Abhishek Walia of Confluent at Conf42 Observability 2025 on the MELT stack for Kafka, with the broker metrics that matter, JMX, KIP-714, JSON logs and traces.

"Kafka doesn’t fail cleanly: it stalls, lags, and misfires beneath the surface." That is how Abhishek Walia, a staff customer success technical architect at Confluent, framed his talk at Conf42 Observability 2025. His answer is the MELT stack (metrics, events, logs, traces) applied to Kafka: which signals actually matter, how to collect them, and which ones you can postpone.

His opinionated short version: start with metrics and logs, then graduate to events and traces.

## The MELT pyramid, applied to Kafka

Abhishek stacks the signals as a pyramid:

- **Metrics** are the base: numerical measurements exposed by brokers, such as request counts, disk back pressure, network thread usage, replication lag and consumer lag.
- **Events** are discrete state changes: a broker crash, a rolling restart, a disk hitting 70%, a pod moving on Kubernetes. Kafka does not expose events directly, so you derive them from logs and metrics.
- **Logs** are not optional. Errors, stack traces, controller elections, client disconnections: root cause analysis cannot finish without them.
- **Traces** live at the client and business layer: a watermark in the Kafka message header that follows the message through every producer, broker and consumer.

His example of why events matter is a good one: during a rolling restart, producer latency spikes for no apparent reason in the metrics. Overlay the rollout event and the spike explains itself.

## Pick metrics carefully, because Kafka has thousands

He recalls counting about 3,500 MBeans on a small home-server cluster a few years ago. Most are noise. The ones he starts with are replication health, partition and leader distribution (no hot broker while others idle), error rates for fetch, produce and replication requests, and network utilisation, which he calls the most precious resource in a Kafka cluster. His sizing aside makes the point: produce at around 125 megabytes per second and a one-gigabit port is already close to full.

Collection is JMX on brokers and clients, a Prometheus JMX exporter to turn MBeans into a scrapable HTTP endpoint, Prometheus to store, and Grafana to graph. The newer piece is KIP-714 in Kafka 3.7 and later, which lets clients push their key metrics to the brokers, so you can collect client metrics centrally without instrumenting every producer and consumer with JMX.

## Logs: JSON, central, and kept longer than you think

The logging advice is concrete. Configure Log4j to emit structured JSON so machines can parse it without hand-built parsers; yes, the volume grows. Ship logs with Filebeat or an OpenTelemetry Collector to one central store, filterable by broker and cluster; he likes Grafana Loki. And do not set retention to seven days. He did, years ago, and regretted it. Size retention to how long application teams can come back with questions: if that is 30 days, keep around 45, tiering to warm and cold storage instead of deleting.

## Traces through message headers

For tracing, propagate context in Kafka headers so consumers continue the same trace, use OpenTelemetry auto-instrumentation, and store spans in Jaeger, Zipkin or similar. His example trace breaks a message's life into producer time, time waiting in the broker, consumer fetch and processing, which shows where the hot spot is when processing slows down.

He also points viewers at a JMX monitoring stack with tuned Kafka dashboards that he and friends maintain.

## Who should watch

Anyone running Kafka in production who has a Grafana dashboard full of panels and no idea which three to look at during an incident. The tool choices are his preferences and he says so; swap them for what your organisation already runs.

## Related Conf42 talks

- [Pranay Prateek on scaling OpenTelemetry Collectors using Kafka](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pranay_Prateek_scaling_opentelemetry_kafka) (SRE 2024), Kafka on the other side of the telemetry pipe.
- [Shalini Katyayani Koney on scaling Kafka on Kubernetes](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable) (Kube Native 2025).
- [Muralidhar Basani on simplifying Kafka governance for developers](https://www.conf42.com/DevSecOps_2023_Muralidhar_Basani_simplifying_kafka_governance) (DevSecOps 2023).

[Watch Abhishek Walia's talk](https://www.conf42.com/Observability_2025_Abhishek_Walia_kafka_visibility_scale)

[Watch the talk on YouTube](https://youtu.be/_EeN2_CWzio).

## Watch the talk

[Observability-First Kafka: Engineering Visibility at Scale](https://www.conf42.com/Observability_2025_Abhishek_Walia_kafka_visibility_scale) at Conf42 Observability 2025.
