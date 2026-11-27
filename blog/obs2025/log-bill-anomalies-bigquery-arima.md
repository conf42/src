# Catch the log bill spike with ARIMA in BigQuery ML

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/log-bill-anomalies-bigquery-arima

In short: Yury Nino of Google shows at Conf42 Observability 2025 how time series anomaly detection on Cloud Logging data flags cost spikes before the invoice.

Turning on every log you can find during an incident feels responsible right up until the bill arrives. At Conf42 Observability 2025, Yury Nino, Cloud Applications Modernization Engineer at Google, told exactly that story: an incident with too little logging, a decision to enable all the available audit logs, and a 700% jump in billing from one month to the next. Her fix is to point time series analysis at the logs themselves, so the next spike shows up as an anomaly before it shows up as an invoice.

The premise is neat and a little ironic. If logs are part of the cost problem, they also carry the signal you need to see it coming.

## The reactive tax is bigger than the bill

Nino frames the cost of doing nothing in four buckets: downtime (lost revenue, churn, reputation), inefficient resource use, security breaches, and wasted engineering time spent firefighting. The billing spike is just the most visible symptom. Proactive cost management, in her definition, means continuous monitoring and optimisation, predictive analytics for right-sizing, elasticity, picking the right pricing models, and above all visibility. The talk focuses on that last one.

Cloud logs are harder to reason about than on-prem logs because the infrastructure is distributed, dynamic and often ephemeral. That makes simple thresholds brittle. You need something that knows what normal looks like for your workload.

## A fast tour of the anomaly detection toolbox

Before the demo, Nino gives a compact map of the machine learning options SRE teams use for anomaly detection:

- **Unsupervised** methods such as clustering and autoencoders, which fit cloud data well because nobody has labelled your logs.
- **Supervised** classifiers such as support vector machines and random forests, which need historical labelled anomalies.
- **Semi-supervised** approaches trained on normal data only, plus isolation forest.
- **Time series** techniques like seasonal decomposition into trend, season and residual.

Because most cost and log signals have a time component and are rarely stationary, she lands on ARIMA (autoregressive, integrated, moving average). It's an introduction to the ideas, and she says as much, but it's enough to understand why the model choice isn't arbitrary.

## The pipeline is three clicks and two queries

The architecture is pleasingly boring. A Cloud Logging log router sink sends logs to a BigQuery dataset (the sink can also target a Cloud Logging bucket, Cloud Storage, Pub/Sub or another project). In BigQuery ML, a SQL query builds the training set from a subset of fields: timestamps truncated to the minute, grouped so each time unit has a count. A second query runs the ARIMA-based anomaly detection over that series.

For charts, Nino exports the results to CSV and opens them in Google Sheets, which is a refreshingly honest choice for a demo. The flagged days line up with the extra logs being generated, and those match the behaviour in Cloud Billing. Once the pattern is known, you can forecast the next jump in log volume, and with it the next jump in cost.

## Who should watch

Platform and SRE folks on Google Cloud who own the logging budget, or who have been asked why it doubled. The demo is short enough to reproduce in an afternoon, and the SQL-only approach means nobody has to stand up a separate ML stack. If you already run anomaly detection on billing exports, the interesting part is applying it one step earlier, to log volume. Your finance team will not thank you, because they will never find out there was a problem. That's the point.

## Related Conf42 talks

- Pradeep Gaddamidi on [Mastering the Chaos: A DevOps Engineer's Journey to Cost-Effective Cloud Monitoring and Logging](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring), the same bill from the other side.
- Santosh Kumar Sana on [AI-Powered Anomaly Detection in Cloud Data Pipelines](https://www.conf42.com/Machine_Learning_2025_Santosh_Kumar_Sana_pipelines_quality_anomaly), anomaly detection pointed at data quality.
- Manoj Kalakoti on [Autonomous FinOps for Cloud-Native Financial Services](https://www.conf42.com/Kube_Native_2025_Manoj_Kalakoti_finops_costgovernance_autonomous), cost governance at fleet scale.

[Watch Yury Nino's talk](https://www.conf42.com/Observability_2025_Yury_Nino_series_cost_anomalies)

[Watch the talk on YouTube](https://youtu.be/NBMen0k6N6k).

## Watch the talk

[Proactive Cost Management: Detecting Anomalies in Logs with Time Series Analysis](https://www.conf42.com/Observability_2025_Yury_Nino_series_cost_anomalies) at Conf42 Observability 2025.
