# Fraud ML has to decide before the customer leaves checkout

Conf42 Blog, 2025-09-08, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/fraud-ml-at-checkout-speed-intuit

In short: Naresh Karri (Intuit) at Conf42 MLOps 2025 on running fraud, credit and ledger ML at transaction scale, with drift handled by shadow deployments.

A card authorisation has to finish while the customer is still standing at the checkout, and in that fraction of a second the system also has to run KYC, KYB and sanctions screening. At Conf42 MLOps 2025, Naresh Karri, Group Product Manager for the Money Platform at Intuit, used that moment to explain what production MLOps looks like in finance: pipelines built for latency, compliance in every layer, and drift handled with shadow deployments and gradual traffic ramps.

## Every dropped checkout is lost revenue

Naresh's framing is the product manager's view of ML infrastructure. Financial institutions process enormous transaction volumes with tight response budgets, under GDPR, CCPA and FCRA, while keeping critical systems at 99.99% uptime. If the decision is slow or wrong, checkout conversion drops, and a lost sale is lost revenue. That turns latency and false positives from engineering metrics into business ones.

He groups the work into three applications: real-time fraud detection, credit assessment (where a loan or card decision takes seconds but covers prospecting and underwriting behind the scenes) and automated financial management, from portfolio optimisation to personalised guidance.

## Fraud detection is a pipeline, not a model

The fraud architecture starts with channels: point of sale, online and mobile, each with its own stream. Those feed pipelines and a feature store, then low-latency inference, decision engines with rules, and finally monitoring and audit with telemetry and retraining. His key line is that fraud detection "isn't just about a model", it is a pipeline that has to handle massive scale.

The hard parts he lists: sub-10-millisecond latency while processing more than 100,000 transactions per second at peak, feature freshness as fraud tactics evolve, rapid adaptation to new patterns, and false positives. Flag too many legitimate transactions and you lose good customers, so the balancing act has to be precise.

## Debits and credits still have to match

The financial management section has the most memorable engineering point. Money cannot be created or destroyed in a ledger; debits and credits must always reconcile. Naresh describes streaming each transaction to a Kafka topic, with consumers recording it in the ledger and driving reconciliation, settlement and clearing. Without that automation, tracking transactions becomes, in his words, super tricky. ML or not, the accounting identity always wins.

## The layered architecture

His reference stack goes bottom to top: data infrastructure with separate governance policies for structured and unstructured data; a training and validation pipeline that automates compliance checks and testing; a feature layer serving both batch and real-time features; a model registry with versioning, A/B tests and controlled rollouts; and a high-performance serving API on top for time-sensitive flows like checkout and loan applications.

Deployment runs on Kubernetes with separate clusters for training and inference, GPU nodes for deep learning, demand-based autoscaling, dedicated or isolated nodes for compliance-critical models, hot standby replicas and geo-distributed deployments. Monitoring spans latency, throughput, resource use and error rates, plus model accuracy and drift, plus business KPIs like approval rate, false positives and revenue impact.

## Drift is unavoidable, so plan the response

Naresh treats drift as a given in high-stakes systems. Detect it with statistical tests and segment-based analysis. Respond with shadow deployment comparisons, gradual traffic ramps up or down, and a human-in-the-loop approval fallback when in doubt, with an audit trail through every transition. A/B testing gets the same discipline: a clear hypothesis tied to a business metric, statistical rigour, controls for adverse effects, segment-level analysis and progressive rollout.

His takeaways: design for scale from day one, integrate compliance throughout, automate everything but keep fallbacks and humans in the loop, and invest in monitoring and response.

## Who should watch

Payments and lending engineers, and product managers who own ML-backed decisions with a latency budget. It is an architecture-level talk with a strong product lens.

## Related Conf42 talks

- [Building Financial Fortresses: Scaling Cloud-Native AI for Real-Time Fraud Detection](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Prakash_Vanga_building_financial_fortresses)
- [Cloud-Native Observability for Financial Systems: Graph-Based Monitoring and Behavioral Analytics](https://www.conf42.com/Observability_2025_Siva_Prakash_financial_anomaly_graph)
- [AI-Driven Financial Reconciliation: Enhancing Accuracy, Speed, and Compliance Through Human-AI Synergy](https://www.conf42.com/Large_Language_Models_LLMs_2025_Naveen_Gowda_financial_reconciliation_compliance)

[Watch Naresh Karri's talk](https://www.conf42.com/MLOps_2025_Naresh_Karri_production_mlops_finance)

[Watch the talk on YouTube](https://youtu.be/FxFGlyEdHeo).

## Watch the talk

[Production MLOps in Finance: Scaling AI Systems for High-Volume Transaction Processing](https://www.conf42.com/MLOps_2025_Naresh_Karri_production_mlops_finance) at Conf42 MLOps 2025.
