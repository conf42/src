# How a CNN-LSTM pipeline cut VoIP fault detection to minutes

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/voip-monitoring-mlops-cnn-lstm-oracle

In short: Krishna Munnaluru (Oracle) at Conf42 MLOps 2025 on a Kafka, Kubeflow and MLflow pipeline that monitors carrier-grade VoIP with neural networks.

In telecom, a 15-to-30-minute delay in spotting a problem means thousands of dropped calls. At Conf42 MLOps 2025, Krishna Munnaluru, Senior Principal Architect at Oracle, walked through a production MLOps pipeline for voice-over-IP monitoring: Kafka for streaming, Kubeflow for training, MLflow for the registry, and a CNN-LSTM model that he says reached 88% prediction accuracy and brought fault detection down to two to five minutes.

This is one of the more concrete talks of the event: real components, real numbers, and a clear view of where each piece sits.

## Traditional monitoring sees less than half the network

Krishna's starting point is the state of conventional VoIP monitoring. By his figures, traditional tools give about 40% visibility into the network, react in 15 to 30 minutes, and statistical models for call-quality prediction reach around 65% accuracy. Blind spots plus slow reaction plus mediocre prediction is a bad combination when every minute is customer-visible.

## The model reads packets like a sequence

The neural network combines CNN layers that extract features from packet sequences with LSTM layers that pick up temporal patterns across sessions. On top of that sit a custom embedding layer for protocol-specific features, an attention mechanism that focuses on anomalies, and a hierarchical feature extractor that works across timescales. Krishna reports a 23-point improvement over the traditional statistical approach.

Features come from edge collectors capturing SIP, RTP and QoS metrics. Apache Beam processes more than 10,000 events per second and extracts 45-plus features, recursive feature elimination handles selection, and Feast serves as the feature store so training and inference see the same values. That last detail is the one that saves you from the classic training-serving skew bug.

## Every piece is wired to the next

The architecture point Krishna keeps returning to is that the components are tied together, so models are not just trained but continuously deployed, observed and improved. Kafka ingests events at sub-100-millisecond latency. Kubeflow pipelines run TensorFlow Data Validation for schema checks and drift detection, then distributed GPU training with hyperparameter tuning. MLflow tracks every experiment's parameters, metrics and artifacts, and versioned models go through approval workflows so teams can roll forward or back.

Serving uses TensorFlow Serving in containers on Kubernetes with horizontal autoscaling, blue-green deployments for zero downtime and instant rollback, and edge inference nodes across regions answering in under 50 milliseconds. In production he cites 96% anomaly detection accuracy and 99.99% availability.

## Monitoring that retrains itself

Monitoring covers model metrics (precision, recall), data quality (feature drift, missing values) and system health (latency, throughput). When drift is detected, retraining triggers automatically. The team also runs A/B tests in production and self-healing mechanisms for infrastructure faults.

Because operators have to trust the output, explainability is built in: SHAP values for feature importance, counterfactual explanations, dashboards tracking feature attribution over time, and automated model cards and audit logs, so an engineer can trace a prediction back to its cause.

The rollout went in four phases: foundation (data collection, features, first model), automation (CI/CD, testing, registry, dashboards), scale (distributed training, geographic deployment), then ongoing optimisation with ensembles and tuning. He also notes reduced licensing costs from using open-source tooling.

## Who should watch

Telecom and network engineers thinking about ML for service assurance, and any MLOps engineer who wants a reference architecture with named tools at each stage. The talk stays at architecture level, so do not expect code.

## Related Conf42 talks

- [AI-Powered Anomaly Detection for Telecom Service Reliability](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability)
- [Go-Powered Telecom BSS: Scaling Enterprise Solutions with Microservices, AI, and Cloud-Native Architecture](https://www.conf42.com/Golang_2025_Bhaskara_Beeraka_telecom_microservices_scaling)
- [The AI-Driven Future of Network Engineering](https://www.conf42.com/Prompt_Engineering_2025_Vamsi_Gadireddy_network_protocols_reliability)

[Watch Krishna Munnaluru's talk](https://www.conf42.com/MLOps_2025_Krishna_Munnaluru_production_ready_mlops)

[Watch the talk on YouTube](https://youtu.be/ljqZgxPzwtA).

## Watch the talk

[Production-Ready MLOps for Telecommunications: Neural Network-Based VoIP Monitoring with 88% Accuracy and Automated Deployment Pipelines](https://www.conf42.com/MLOps_2025_Krishna_Munnaluru_production_ready_mlops) at Conf42 MLOps 2025.
