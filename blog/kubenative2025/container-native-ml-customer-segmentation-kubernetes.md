# Splitting a monolithic segmentation pipeline into Kubernetes services

Conf42 Blog, 2025-09-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/container-native-ml-customer-segmentation-kubernetes

In short: Ujjwala Modepalli (Wells Fargo) at Conf42 Kube Native 2025 on rebuilding segmentation ML as microservices with Helm, drift-triggered retraining and a feature store.

A monolithic analytics pipeline scales the way a single-lane bridge does: everything waits for the slowest truck. At Conf42 Kube Native 2025, Ujjwala Modepalli, Senior Credit Risk Specialist at Wells Fargo with around 14 years in analytics and predictive modelling, described how her team re-engineered a predictive customer segmentation system into a set of Kubernetes services, and why the biggest win was being able to scale each stage on its own.

The problem she started from is familiar to anyone who has run batch scoring in a bank. As data volumes grew, processing times stretched, insights arrived late, and adding servers did not help because the pipeline was one rigid unit. Data scientists, ML engineers and DevOps worked in separate silos on top of it.

## Four layers, each with its own scaling knob

The architecture splits into data ingestion, feature engineering, model training and inference. Ingestion services pull from CRM, digital interactions and transactions using event-driven ingestion. Feature engineering services clean and validate raw data into standard features. Training runs distributed across the cluster for gradient boosting, neural networks and clustering. Inference serves real-time segment predictions with Redis caching in front.

Her point is that the split matters more than any individual component. If training spikes, you scale training. If inference needs compute, you add inference pods. Different teams can ship changes to their stage without breaking the whole pipeline, which is the real productivity gain.

## Helm for consistency, CRDs for the ML-shaped parts

With dozens of services, every deploy needs to look the same. The team versions deployments as Helm charts with environment-specific overrides, so one chart goes to dev, staging and production and rolls back cleanly. For needs that plain Kubernetes does not model well, such as scheduling training jobs, managing GPU resources and automating retraining lifecycles, they extended the cluster with custom resource definitions.

## Let drift trigger the retrain

Customer behaviour shifts with promotions, seasons and product launches. Instead of retraining on a calendar, monitoring watches for data drift, and when behaviour no longer matches the model, Kubernetes kicks off a retraining pipeline. The new model is validated and deployed without manual steps or downtime.

A container-based feature store backs this up. Training and inference read the same versioned features, with Redis for fast retrieval, so A/B tests on new features and rollbacks to old ones stay traceable. Anyone who has debugged a training-serving skew will appreciate that line item.

## Sidecars, init containers and the GPU budget

She also walked through the Kubernetes patterns they leaned on: init containers that check data integrity and dependencies before the main container starts, sidecars that collect latency and drift metrics for Prometheus and Grafana, and multi-container pods for tightly coupled steps like preprocessing plus serving. GPU scheduling policies give deep learning jobs priority access, and tuned memory allocation stops large clustering jobs from crashing out of memory.

The reported outcomes: 85% GPU utilisation, roughly three times better memory efficiency, a 60% cost reduction, 99.9% uptime and 40% faster processing. The rollout ran in four phases (containerise, orchestrate, optimise, production), each iterated before going enterprise-wide.

## Who should watch

Data science and ML platform teams at enterprises still running segmentation or scoring as one large batch job. It is a case-study talk at the architecture level, with no code on screen, so it works best as a map of which pieces to break out first.

## Related Conf42 talks

- [MLOps at Scale: Operationalizing Machine Learning for Financial Risk and Fraud Detection in Cloud-Native Environments](https://www.conf42.com/MLOps_2025_Dileep_Kumar_Kanimetta_mlops_scale_operationalizing) by Dileep Kumar Kanimetta (Microsoft) covers a similar platform from the risk side.
- [AI-Powered Customer Insights for Financial Services](https://www.conf42.com/Machine_Learning_2025_Neha_Thakur_insights_financial_customer) by Neha Thakur (AWS) focuses on what the segments are used for.
- [Taming Data Skew in Production ML Pipelines](https://www.conf42.com/Machine_Learning_2026_Srihari_Godleti_fairness_bias_mitigation) by Srihari Godleti (Roku) tackles the Spark side of slow training pipelines.

[Watch Ujjwala Modepalli's talk](https://www.conf42.com/Kube_Native_2025_Ujjwala_Modepalli_ml_segmentation_customers)

[Watch the talk on YouTube](https://youtu.be/ykY4S6PjbHw).

## Watch the talk

[Container-Native ML: Scaling Predictive Customer Segmentation on Kubernetes](https://www.conf42.com/Kube_Native_2025_Ujjwala_Modepalli_ml_segmentation_customers) at Conf42 Kube Native 2025.
