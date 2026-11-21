# Log anomaly detection needs context, not more thresholds

Conf42 Blog, 2025-08-07, updated 2026-11-09. https://www.conf42.com/blog/platform2025/log-anomaly-detection-embedded-context-agents

In short: Konstantin Berezin of Rapyd at Conf42 Platform Engineering 2025 on embedded context agents that enrich logs, score anomalies with ML and alert only on what matters.

A timeout in your logs means nothing until you know it happened during checkout on Black Friday. At Conf42 Platform Engineering 2025, Konstantin Berezin, back-end developer at Rapyd, proposed embedded context agents: small components inside the observability pipeline that enrich every log with business and system context, score it with ML models, and page a human only when an outlier really matters.

## Why the classic approaches drown you

Konstantin lays out the problem in three parts. Volume: microservices across staging, QA and production in several regions produce millions of lines a day, mostly connection-opened and cache-hit chatter. Heterogeneity: one team logs structured JSON, another logs free-form strings. And missing context: the same error can be routine or a crisis depending on what else is happening.

The usual tools each fall short. Threshold rules (more than a hundred errors a minute, ping Slack) are easy and noisy, and they still miss subtle drift. Statistical methods like moving averages and z-scores work for latency and throughput but do not understand what a log line means. Basic ML such as isolation forests and clustering promises more, but breaks on new log types, which is exactly when you need it. The net effect: false positives until engineers stop reading the pages.

## A guard, not a camera

His analogy is a shopping mall. Cameras record everything, but someone has to interpret it: a person walking around a closed mall at night is suspicious, the same person on Black Friday is a customer. In his words, logs without agents are just raw video. The agents are embedded (they live inside your system), contextual (they attach service, deployment, user and region metadata) and autonomous (they alert, correlate and can trigger small fixes).

## The pipeline, end to end

The reference architecture is concrete. Sources are application logs, infrastructure logs from containers and cloud resources, and security events such as access attempts, audit trails and firewall logs. A collector like Fluentd, Logstash or OpenTelemetry normalises them. Kafka sits in the middle as the message bus, for durable high-throughput streaming, replay and backpressure. The agent layer does context enrichment, runs the models and makes a decision about severity and response. Results fan out to Grafana or Kibana, Slack, storage in Postgres, Redis or Elasticsearch, and automated actions such as Kubernetes scaling or blocking an IP.

For the detection core he combines autoencoders, isolation forests, LogBERT for semantic understanding, and DeepLog's LSTM approach to modelling log sequences, plus Microsoft's open-source LogAI library. Agents specialise by domain (network, authentication, performance) and share findings over the bus.

## Three scenarios worth stealing

- A 500 on an order request that matches no known error cluster gets flagged before it disappears into thousands of lines.
- A spike of failed logins from an unusual region, from the same IP range within the same time window, is reframed from technical error to likely attack.
- Every dashboard is green, but slow-query warnings keep rising; individually harmless, the trend triggers an early performance alert before an outage.

## Where LLMs fit

Konstantin is clear-eyed about LLMs. They explain patterns well in human language, but they are not real-time, do not watch streams continuously, get expensive at millions of lines per minute, and raise privacy questions for logs full of sensitive data. His recommended setup is hybrid: ML agents scan and alert in real time, and an LLM helps engineers summarise the incident and suggest root causes afterwards. He also names the open problems: keeping context up to date as services change, explainability of anomaly verdicts, and agents that overlap or conflict.

## Who should watch

Observability and platform engineers designing log pipelines, and teams whose alert channel has become wallpaper. Note the talk starts slightly mid-thought, so give it a minute.

## Related Conf42 talks

- [Chloe Caron on how well LLMs detect anomalies in your data](https://www.conf42.com/Large_Language_Models_LLMs_2024_Chloe_Caron_llms_detect_anomalies) at Conf42 LLMs 2024.
- [Birol Yildiz on AIOps approaches to reduce alert noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) at Conf42 DevSecOps 2024.
- [Clay Langston on GPT for monitoring and logging systems](https://www.conf42.com/Site_Reliability_Engineering_2023_Clay_Langston_gpt_monitoring_logging_systems) at Conf42 SRE 2023.

[Watch Konstantin Berezin's talk](https://www.conf42.com/Platform_Engineering_2025_Konstantin_Berezin_context_agents), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/MdqBaSDsA7Q).

## Watch the talk

[Anomaly Detection for Platform Logs using Embedded Context Agents](https://www.conf42.com/Platform_Engineering_2025_Konstantin_Berezin_context_agents) at Conf42 Platform Engineering 2025.
