# A graph neural network that tunes Step Functions fan-outs live

Conf42 Blog, 2025-06-05. https://www.conf42.com/blog/obs2025/step-functions-fan-outs-that-tune-themselves

In short: Vamsi Praveen Karanam of Amazon at Conf42 Observability 2025 on OpenTelemetry plus a small GNN that resizes Step Functions map chunks mid-run, with guardrails.

When an AWS Step Functions map state fans out into thousands of Lambda invocations, one slow branch can hold up the whole workflow. At Conf42 Observability 2025, Vamsi Praveen Karanam, Software Development Engineer at Amazon, presented Adaptive Parallelism Insights (APIX): OpenTelemetry spans on every branch, a compact graph neural network that reads them, and a controller that changes chunk sizes on a running workflow without touching business code.

It is one of the more concrete AI-for-observability talks of the event: a named architecture, a model size, explicit guardrails and a results table.

## Three pains of big fan-outs

Karanam lists the failure modes anyone who has run large map states will recognise. Latency cliffs, where a few slow branches delay the entire execution. Tracing gaps, because high-level dashboards average away branch-specific anomalies and the native execution history only shows coarse events. And cost spikes from hidden retries and cold starts. Those turn into three questions: how to capture per-branch telemetry cheaply, whether a small model can digest it fast enough, and how to act on its advice mid-run without blowing through limits.

## The pipeline, top to bottom

Every task gets an OpenTelemetry span; map and parallel branch spans carry a chunk ID. The same wrapper writes counters such as payload size, retry count and cold start time through CloudWatch Embedded Metric Format, so no agent is needed inside Lambda. Spans travel over OTLP to a collector on AWS Fargate, then into Kinesis Data Firehose, which feeds live heat maps in Amazon Managed Grafana and lands raw records as Parquet in S3.

SageMaker Serverless hosts a two-layer GNN of about 1.2 million parameters. Every 60 seconds it reads the latest window of branch metrics and predicts an ideal chunk size, with a confidence score and projected cost and latency impact. EventBridge passes the inference to a Lambda callback that checks guardrails and patches the running map state. Each decision is hashed, stored in Systems Manager Parameter Store and written into later spans, so auditors can follow a change from inference to outcome.

Span emission adds about two milliseconds per invocation, which he calls negligible for tasks that run for seconds.

## Guardrails make the automation shippable

The part to steal even if you never train a GNN is the controller's three boundaries. Chunk size can change by at most 25% within five minutes, which prevents oscillation. A concurrency cap keeps total Lambda concurrency below the account quota minus a safety buffer. And a rollback trigger reverts to the previous chunk size if p95 latency and errors both rise for two consecutive windows.

## The numbers he showed

The evaluation compared static batching at 1,000 items and dynamic S3 partitioning against adaptive chunking on three workloads: a uniform 10 TB synthetic set, a skewed 10 TB set with larger records mixed in, and 3 TB of anonymised production data. Adaptive chunking had the lowest latency and cost on every workload. On the skewed set, throttle errors fell from 47 under static batching to five; on the live data, from 24 to three.

He is upfront about the limits: cold start jitter can exaggerate latency gains, synthetic workloads may miss extreme patterns, and model drift means weekly retraining plus drift alerts.

## Who should watch

Teams running data enrichment, ETL or compliance jobs on Step Functions distributed maps, and anyone who wants a worked example of putting a model in a control loop safely. The five lessons at the end (sample generously during peaks, keep guardrails, publish dollar deltas next to trace IDs, watch retry patterns, retrain weekly) apply well beyond AWS.

## Related Conf42 talks

- [One Step Ahead: Modern Application Architecture with AWS Step Functions](https://www.conf42.com/Cloud_Native_2023_Oskar_Neumann_modern_application_architecture_aws_step_functions) by Oskar Neumann at Conf42 Cloud Native 2023.
- [Patterns for efficient serverless development](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless) by Yan Cui at Conf42 Cloud Native 2024.
- [Serverless Workflow Orchestration on AWS](https://www.conf42.com/DevOps_2025_Bharat_Vishal_Tiwary_aws_serverless_workflow) by Bharat Vishal Tiwary at Conf42 DevOps 2025.

[Watch Vamsi Praveen Karanam's talk](https://www.conf42.com/Observability_2025_Vamsi_Praveen_Karanam_aws_serverless_workflows) or the [YouTube recording](https://youtu.be/7wmZsEkiYII).

## Watch the talk

[AI-Driven Observability for Massive AWS Serverless Workflows](https://www.conf42.com/Observability_2025_Vamsi_Praveen_Karanam_aws_serverless_workflows) at Conf42 Observability 2025.
