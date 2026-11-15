# In production the system is the star, not the model

Conf42 Blog, 2026-02-08, updated 2026-11-09. https://www.conf42.com/blog/ml2026/in-production-the-system-is-the-star

In short: Ancilia Dmello of Ford at Conf42 Machine Learning 2026 on an observable MLOps framework on Google Cloud, told through an oil-change prognostics model.

Shipping a model is harder than training one, and Ford's oil-change prognostics showed why: one region's "change oil soon" flags nearly doubled while every infrastructure dashboard stayed green. At Conf42 Machine Learning 2026, Ancilia Dmello, Software Engineer Technical Lead at Ford Motor Company, presented the MLOps framework on Google Cloud that caught that drift, and the deployment and governance patterns around it.

Her framing: in the lab the model is the star; in production the system is.

## Four barriers, one composed stack

Ancilia named the four things that keep ML stuck in notebooks: infrastructure complexity (bespoke clusters and snowflake deployments), fragmented tooling with weak integration, silent model degradation from data drift, concept drift and feature skew, and governance requirements that keep getting stricter.

Her answer is to compose managed services rather than build platforms: Vertex AI for training, pipelines and experiment tracking; Dataflow for streaming and batch feature computation; Cloud Run for containerised serving that scales with load; Cloud Monitoring for metrics, logs and model health; BigQuery for features, training data and prediction logs. The value is the opinionated path: teams know where data, training, serving and monitoring go.

## Pick the deployment pattern from the constraint

Real-time inference serves sub-second decisions such as fraud or pricing; batch serves nightly risk scores and weekly churn; streaming sits between them. The oil-change model uses all three. Instead of a fixed mileage or six-month rule, vehicles stream engine temperature, RPM patterns, trip duration and load; Dataflow aggregates, BigQuery holds trip and maintenance history, Vertex AI trains a remaining-oil-life model, Cloud Run answers when a driver starts a trip, and batch retraining folds in new service outcomes.

## Two layers of observability

Model monitoring covers data drift against a training baseline, training/serving feature skew (the transformation applied offline but not online), prediction drift in output distributions, and performance against ground truth when labels arrive, here when the car reaches the shop. Infrastructure monitoring covers availability, error rates, latency percentiles and autoscaling. Having both lets the on-call tell "the model is wrong" from "the system is slow".

That is how the regional incident resolved. Infrastructure was healthy, the daily evaluation join showed the model had become over-conservative without improving engine outcomes, and drift plots traced it to a wave of short urban trips underrepresented in training. The team retrained, rolled out through CI/CD, and watched the flag rate fall back to normal.

## Ship like software, gate like a regulator

Deployments follow a progressive rollout: validation and automated tests, a canary of around 5% of traffic, then 25, 50 and 100% while health checks stay green, with automated or on-call rollback. Retraining is scheduled and automated, but only low-risk updates auto-approve; high-risk models, such as those affecting credit or safety, go to domain experts who review performance and fairness first. Immutable, semantically versioned artifacts linked to data, code and hyperparameters, plus audit logs, make every decision reproducible.

## Who should watch

ML platform engineers on GCP, and anyone whose models are live but whose monitoring stops at uptime. The oil-change example makes it worth watching even on another cloud.

## Related Conf42 talks

- [MLOps: From Jupyter to Production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production) by Tomas Fernandez.
- [Bridging the MLOps Gap: From AI Research to Production-Ready Systems](https://www.conf42.com/MLOps_2025_Bharath_Reddy_Baddam_bridging_mlops_gap) by Bharath Reddy Baddam.
- [MLOps in Healthcare: Scaling AI Model Deployment Through Strategic Automation and Monitoring Frameworks](https://www.conf42.com/MLOps_2025_Aishwarya_Pai_mlops_healthcare_scaling) by Aishwarya Pai, the same governance questions in another regulated industry.

[Watch Ancilia Dmello's talk](https://www.conf42.com/Machine_Learning_2026_Ancilia_Dmello_forecasting_inventory_retail) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/F6Okuh3Eqtg).

## Watch the talk

[From Experiment to Enterprise: Building Scalable, Observable MLOps Systems on Google Cloud](https://www.conf42.com/Machine_Learning_2026_Ancilia_Dmello_forecasting_inventory_retail) at Conf42 Machine Learning 2026.
