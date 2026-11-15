# Predict a two-hour Prefect flow will fail in its first minutes

Conf42 Blog, 2026-02-07, updated 2026-11-09. https://www.conf42.com/blog/ml2026/predict-prefect-flow-failures-in-minute-one

In short: Pavel Solikov of J.P. Morgan at Conf42 Machine Learning 2026 on a CatBoost model that scores Prefect flow runs for SLA breaches before the heavy step.

The worst failure is the one that waits until minute 118 of a two-hour run. At Conf42 Machine Learning 2026, Pavel Solikov, Software Engineer at J.P. Morgan, showed how to predict that a Prefect flow will breach its SLA after only the first task, explain why, and stop or reroute the run before the expensive step burns compute.

The title's "Perfect Flows" is a Prefect pun, and the talk ends with a live demo in the Prefect UI.

## Prefect already knows enough at the start

Pavel's insight is about where to put the model. At flow start, the orchestrator already holds the parameters, the environment and metadata such as the code version. After the first cheap task it can also compute data-quality fingerprints and early runtime signals. That is enough to score risk before the costly stage begins, and Prefect has the hooks to act on the score.

To keep things concrete he defined failure as an SLA breach: the runtime exceeding a threshold.

## A synthetic risk flow with 11 features

The example is a portfolio risk computation (deliberately synthetic, and he says so). Step one generates a returns matrix and injects missing values and outliers; step two computes statistics; step three is the heavy covariance estimation and simulation work, with a runtime that depends non-linearly on the inputs.

The feature vector has 11 fields: the number of assets, days and simulations, data-quality measures, the code version, return statistics and how long step one took. Nothing from after the heavy step leaks in.

## CatBoost wins, SHAP explains

He generated 5,000 runs with balanced success and failure classes and benchmarked logistic regression, random forest, XGBoost, histogram gradient boosting and a single-feature threshold rule as a sanity check. CatBoost came out on top at about 0.87 ROC AUC, a natural fit for tabular data with a categorical code-version feature and little preprocessing. The other boosting models were close, and even logistic regression cleared 0.80.

A score alone does not help a developer, so each run gets a SHAP explanation. In his example, a run scored about 95% risk because returns had more extreme spikes than usual and many values had been filled in during step one, both of which make the simulation unstable. The explanation itself suggests the fix.

In the demo, a run in report-only mode logs a high risk score and its top drivers and keeps going; flip the stop flag and the same run fails immediately with the reason in the logs.

## From demo to production

Pavel's production checklist: add code-change features from Git, possibly via AST diff tools such as ChangeDistiller, because the same inputs can pass on one version and fail on the next; start in shadow mode and alert before gating; log predictions and outcomes to monitor drift; retrain on a sliding window.

The pattern generalises to any long-running job where late failure is expensive: ETL, batch scoring, model training, CI pipelines that die after hours. The action can be rerouting to a different worker pool, not just aborting, and another useful label is the probability that a retry will succeed.

## Who should watch

Data and ML platform engineers running Prefect, Airflow or anything with slow, costly jobs. The approach is cheap to try and the demo makes it concrete.

## Related Conf42 talks

- [Beyond SLOs: Proactive Failure Prediction Through Anomaly Detection](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Gaurav_Mittal_slos_failute_prediction) by Gaurav Mittal.
- [Orchestrating data and ML workflows with Apache Airflow](https://www.conf42.com/Machine_Learning_2023_Tamara_Janina_Fingerlin_orchestrating_workflows_apache_airflow) by Tamara Janina Fingerlin, for the orchestrator on the other side of the fence.
- [4 Tricks That Help You Leverage Your Airflow Pipelines](https://www.conf42.com/DevOps_2024_Aliaksandr_Sheliutsin_leverage_airflow_pipelines) by Aliaksandr Sheliutsin.

[Watch Pavel Solikov's talk](https://www.conf42.com/Machine_Learning_2026_Pavel_Solikov_security_adversarial_attacks) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/rEBi0oQSLWE).

## Watch the talk

[Stop Failures Before They Happen: Gradient Boosting for Perfect Flows](https://www.conf42.com/Machine_Learning_2026_Pavel_Solikov_security_adversarial_attacks) at Conf42 Machine Learning 2026.
