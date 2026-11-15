# Machine learning as an intelligence layer across the payment lifecycle

Conf42 Blog, 2026-01-27, updated 2026-11-09. https://www.conf42.com/blog/ml2026/machine-learning-payment-ecosystem-layer

In short: Synchrony's Balakumaran Sugumar at Conf42 Machine Learning 2026 maps ML across merchant onboarding, authorisation, settlement and payment operations.

A card swipe gets roughly a hundred milliseconds to be scored, routed and approved, and static rules written by a committee can't keep up with fraudsters who probe them for weaknesses. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Balakumaran Sugumar, AVP and principal engineer for digital servicing at Synchrony, argued that machine learning in payments works best as a shared intelligence layer running through the whole lifecycle, not a feature bolted onto fraud detection.

He said up front that this is a systems talk, not an algorithms talk, built on more than 16 years of running large payment platforms.

## Rules versus models

The contrast is familiar but well drawn. Traditional systems decline a transaction over a fixed amount on a new card or flag high velocity, run batch reports overnight, treat every similar customer the same way, and need committee meetings and full test cycles to change a rule. Fraudsters get a window between rule updates. ML systems score every transaction in its own context, update from outcomes, and run on streams instead of batch windows.

## Where ML touches each stage

He walks the lifecycle:

- **Merchant acquisition:** risk scoring and KYC automation. Straightforward low-risk merchants are approved instantly, clear high risks declined with reasons, and the edge cases routed to an experienced underwriter with the model's key factors highlighted. He cites around a 90% cut in processing time for standard applications and 75% fewer manual reviews.
- **Authorisation:** real-time fraud scores from device, location, velocity, merchant category and history, returned as a probability rather than a yes or no. In his example, a score between 0.5 and 0.7 triggers step-up customer validation. Routing picks the payment network with the best historical approval rate.
- **Processing and settlement:** anomaly detection on transaction flows, capacity prediction, reconciliation and cash-flow forecasting.
- **Operations:** traffic forecasts that trigger autoscaling ahead of spikes, anomaly-based alerting, root-cause models and, in some systems, automated remediation.

He also reports manual intervention dropping from around half of cases to under 5% on an ML-enhanced platform.

## The challenges he doesn't skip

The challenges section is the most useful for builders. Data quality: missing fields, biased samples, duplicates. Explainability: regulators and stakeholders need to know why a merchant was declined. Latency: a two-minute ensemble is useless on a card swipe, so you trade sophistication for speed or precompute. Monitoring: fraud patterns shift daily, so retraining pipelines and alerts are part of the system. And integration with legacy platforms that were never designed for ML, including a fallback to the rule-based path when a model misbehaves. A bug in a fraud model, he notes, can cost millions.

## What's next, and a small demo

Looking ahead, he expects ML to underpin embedded finance, real-time personalisation, cross-border routing, alternative payment methods and more autonomous operations. Two concrete notes: shopping agents that must pick the customer's best-reward card on their behalf, and stablecoins entering cross-border transfers at the bank he works with.

The talk ends with a deliberately simple demo: Kafka running locally in Docker, a producer generating synthetic transactions, and a consumer scoring them with a pickled model trained on synthetic data where high amounts, low device trust, international origin and prior fraud push the score up. It's a teaching toy, not a production fraud system, and he presents it that way.

## Who should watch

Engineers and product owners new to payments who want a map of where ML fits end to end, and architects planning how to wire models into a legacy authorisation path. Fraud specialists will want the related talks below for depth.

## Related Conf42 talks

- [Python-powered fraud detection: high-performance ML systems with NumPy, PyTorch and Ray](https://www.conf42.com/Python_2025_Vinod_Upputuri_fraud_ml_numpy), Vinod Upputuri (Mastercard), Conf42 Python 2025
- [Real-time payments for database DevOps: scalable, secure systems](https://www.conf42.com/Database_DevOps_2026_Priyatham_Nagaiya_Seenu_Naidu_kafka_pipelines_clusters), Priyatham Nagaiya Seenu Naidu (Mastercard), Conf42 Database DevOps 2026
- [Advancing financial fraud detection with graph databases](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph), Venkateswarlu Boggavarapu (JPMorganChase), Conf42 Machine Learning 2025

[Watch Balakumaran Sugumar's talk](https://www.conf42.com/Machine_Learning_2026_Balakumaran_Sugumar_anomaly_detection_signals)

[Watch the talk on YouTube](https://youtu.be/-7tXg8Apc0Y).

## Watch the talk

[The Role of Machine Learning in Today’s Payment Ecosystems](https://www.conf42.com/Machine_Learning_2026_Balakumaran_Sugumar_anomaly_detection_signals) at Conf42 Machine Learning 2026.
