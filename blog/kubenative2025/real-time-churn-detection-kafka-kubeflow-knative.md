# Catch churn while it happens with Kafka, Kubeflow and Knative

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/real-time-churn-detection-kafka-kubeflow-knative

In short: Gaurav Sunkar (Google) at Conf42 Kube Native 2025 on real-time churn detection using LSTMs and ensembles served via Kafka, Kubeflow and Knative on Kubernetes.

By the time a monthly churn report flags a customer, that customer has usually already left. At Conf42 Kube Native 2025, Gaurav Sunkar of Google Cloud, who previously worked on digital marketplaces including eBay, Walmart and StockX, proposed a real-time retention engine on Kubernetes: Kafka to stream every interaction, Kubeflow to train and retrain the models, and Knative to score customers the moment behaviour changes.

Why bother? His four reasons are revenue tied to customer lifetime value, acquisition costing more than retention, targeted campaigns instead of broad ones, and freeing teams from manually spotting at-risk customers.

## Traditional churn models are late by design

Sunkar listed why the classic approach falls short. It is reactive: by the time patterns are processed, the customer is gone. It segments customers into homogeneous cohorts and misses individual trajectories. It mostly uses transactional data and ignores support tickets, communications, payment issues and product usage. And it runs on fixed rules and static thresholds that cannot follow seasonality or shifting expectations.

What AI adds, in his framing, is response time (act when the behaviour happens), continuous learning from new data streams, and multi-source inputs for a fuller risk picture.

## Pick the model by the memory you need

The model section is a useful quick comparison. Recurrent neural networks handle sequences of customer behaviour, like a drop in login frequency, but lean on recent history. LSTMs keep both immediate and distant signals, so they can catch gradual disengagement over weeks or months. Ensembles such as random forests and gradient boosting combine with deep learning for a fuller assessment. On features, he stressed micro-interactions like click-through rates and navigation patterns, which can precede visible churn by weeks and give you the intervention window.

## An orchestra with a stage manager

Sunkar explained the stack with an orchestra analogy that actually holds up. Kubernetes is the conductor. Kafka collects every event from mobile apps, web apps and backend services into a unified log, and Kafka Streams handles real-time feature extraction and aggregation. Kubeflow is the brain: training pipelines that retrain as data arrives, experiment tracking, hyperparameter tuning and model versioning, so data scientists iterate while DevOps manages deploys. Knative is the stage manager, scaling inference functions up for Black Friday and down on quiet days, triggered directly by Kafka events.

Production needs a unified data platform for batch and streaming, REST and GraphQL APIs for CRM integration so interventions carry full customer context, and autoscaling compute. Prometheus and Grafana watch accuracy, latency and drift, and new model versions are validated against production traffic before they take over.

## Retention means keeping trust too

The ethics section is more than a box tick. Audit predictions across segments so infrequent users are not systematically written off, use SHAP and LIME so customer success teams know why someone is flagged, and log model decisions and intervention triggers. Privacy by design under GDPR and CCPA means feature selection must adapt to each customer's consent, with consent checks and retention policies automated in the Kubeflow pipeline.

His roadmap has four steps: foundation (Kubernetes, Kubeflow, Kafka), model development on historical data, production on Knative with CRM integration, then A/B testing and scaling.

## Who should watch

ML and data platform engineers at marketplaces, subscription businesses or anyone with a churn dashboard that only explains the past. It is a blueprint talk without code, and a good overview of how the three CNCF-adjacent tools fit together.

## Related Conf42 talks

- [Beyond Traditional DevOps: A Dive into Serverless with Kubernetes using Knative](https://www.conf42.com/Kube_Native_2023_Karan_Jagtiani_devops_serverless_knative) by Karan Jagtiani (HackerRank) explains the Knative layer.
- [Leveraging AI-Driven Insights for Incident Management: Enhancing Customer Retention](https://www.conf42.com/Incident_Management_2024_Anandakumar_Kumaravelu_4_ai_retention_personalization) by Anandakumar Kumaravelu (SADA) ties retention to personalisation.
- [Supply and demand in social marketplaces](https://www.conf42.com/Cloud_Native_2024_Igor_Sedachev_supply_demand_marketplaces) by Igor Sedachev (Avito) covers the other end of marketplace dynamics, the cold start.

[Watch Gaurav Sunkar's talk](https://www.conf42.com/Kube_Native_2025_Gaurav_Sunkar_retention_churn_ai)

[Watch the talk on YouTube](https://youtu.be/_IjcboEsOn4).

## Watch the talk

[Building Intelligent Retention Engines: Real-Time Churn Detection with AI on Kubernetes](https://www.conf42.com/Kube_Native_2025_Gaurav_Sunkar_retention_churn_ai) at Conf42 Kube Native 2025.
