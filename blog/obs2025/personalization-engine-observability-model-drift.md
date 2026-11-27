# Your recommender did not crash. It quietly served default content

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/personalization-engine-observability-model-drift

In short: Sai Kumar Bitra of AT&T at Conf42 Observability 2025 on observing real-time personalization engines, with model metrics, traces and a silent drift story.

The worst personalization incident is the one where nothing crashes. At Conf42 Observability 2025, Sai Kumar Bitra, a principal software engineer at AT&T, walked through how to observe a real-time personalization engine, and illustrated it with a scenario where engagement slid for a week while every service stayed green.

The answer to that scenario turned out to be a missing profile attribute upstream, and finding it took metrics, traces and logs together.

## Why personalization is hard to observe

Sai lists the challenges. Personalization runs on distributed pipelines of services, data pipelines and ML models, so end-to-end tracking is a must. Event volume is high, and telemetry must be captured without adding latency to responses that users expect in milliseconds. Model decisions are a black box: when recommendations get worse, is it the model, the rules or the source data? And users hop between web, mobile and store, so their journey has to be stitched across channels.

## The architecture and the metrics that matter

His reference architecture is a request entering through APIs, a decision engine calling a model service that executes models and rules, a data layer holding profiles and content, and event ingestion (for example through Kafka) feeding the model. Everything ships telemetry to one centralised observability pipeline, instrumented once with the OpenTelemetry SDK.

The metrics he cares about go beyond latency:

- **Latency and throughput** per API, model call and data call.
- **Error rates and timeouts**, including how often the system falls back to default recommendations.
- **Engagement metrics** such as click-through, conversion and dwell time, tied to observability so a drop shows up as a signal.
- **Model indicators**: confidence score distribution, frequency of each model variant, and drift between live inputs and training data.
- **Resources**, including Kafka topic throughput and consumer lag.

## Traces and logs for the black box

Tracing follows each personalization request through API, decision engine, model and database, with a span per segment, so you can see which layer is eating the milliseconds. Tracing every request is not feasible, so sample normal traffic and keep a representative slice. Logs should be structured and rich: user segment, relevant features, perhaps a reason or explanation score, plus trace IDs for correlation. And anonymise: GDPR concerns mean engineers get enough to troubleshoot without logging sensitive customer data.

On scale, he warns against metric overload from per-user labels (aggregate by category or percentile instead), recommends batching and buffering telemetry exports so applications are not blocked, tiered storage, and monitoring the observability pipeline itself, because a lagging log forwarder during an incident is its own outage.

## The silent drift incident

The case study is the memorable part. Engagement on a personalized component dropped gradually over a week. Nothing crashed. An alert on click-through rate falling below baseline fired, and the model drift metric showed live inputs had shifted from the training data. Traces showed normal latency, but many sessions were getting default content: the model was unsure and falling back. Logs, which recorded whether each response was personalized or default, showed users not landing in any segment. The cause was upstream: the ETL had stopped collecting an age attribute that segment rules depended on. Fix the ETL, and the recommendations come back.

The lesson: monitoring isn't just an ops concern when the product is the model's output.

## Who should watch

Engineers running recommendation or ranking systems in production, and ML teams whose models are monitored only for uptime. It is a broad overview with one strong story; the tool stack at the end (OpenTelemetry, Prometheus, Grafana, Jaeger, the ELK stack, plus commercial APM) is standard.

## Related Conf42 talks

- [Lakshmi Narayana Gupta Koralla on hyper-personalization with AI and analytics](https://www.conf42.com/Machine_Learning_2025_Lakshmi_Narayana_Gupta_Koralla_hyper_personalization) (Machine Learning 2025).
- [Leonid Yankulin on actionable alerts that fix problems quickly](https://www.conf42.com/Observability_2024_Leonid_Yankulin_actionable_alerts_fix) (Observability 2024), for alerting on business signals like click-through.
- [Emmanuela Opurum on building observability into modern cloud architectures](https://www.conf42.com/Observability_2026_Emmanuela_Opurum_cloudnative_architecture_tracing) (Observability 2026).

[Watch Sai Kumar Bitra's talk](https://www.conf42.com/Observability_2025_Sai_Kumar_Bitra_scaling_engines_personalization)

[Watch the talk on YouTube](https://youtu.be/kwgnuGUnzrg).

## Watch the talk

[Scaling Observability for Real-Time Personalization Engines](https://www.conf42.com/Observability_2025_Sai_Kumar_Bitra_scaling_engines_personalization) at Conf42 Observability 2025.
