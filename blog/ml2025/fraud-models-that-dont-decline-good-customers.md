# Fraud detection's other job is not declining good customers

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/fraud-models-that-dont-decline-good-customers

In short: Amazon engineer Surendra Lakkaraju laid out ML fraud detection at Conf42 Machine Learning 2025: supervised and unsupervised models, features, scale.

A falsely declined card doesn't just lose one sale; that customer may never come back. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Surendra Lakkaraju, Senior Software Development Engineer at Amazon, explained why rule-based fraud systems now hurt both sides of the ledger, and how machine learning systems catch more fraud while turning away fewer real shoppers.

It's a short, dense overview of a modern fraud stack, with industry figures rather than Amazon internals.

## The rule that blocks a thousand dollars from a new device

Lakkaraju opens with the classic rule: block every transaction over a thousand dollars from a new device. It worked when fraud was simple. Today's fraud is faster and more coordinated, rules can't adapt, and the false-positive rate he cites for rule-based systems is above 28%. His figure for the cost of false declines is over $3.6 billion a year in lost transactions. Meanwhile fraud keeps growing by more than 20% a year.

ML systems, by the abstract's numbers, process hundreds of thousands of transactions per second against thousands of features each, with detection accuracy above 96% and false positives down by 81%.

## Pick the model by what you need to explain

The supervised section is a practical guide to choosing:

- **Random forests** are interpretable, which matters when you have to explain a decision to a regulator.
- **Gradient boosting** handles imbalanced data well, and fraud is the textbook imbalanced problem.
- **Neural networks** find complex patterns humans can't articulate.

All of them need to answer in real time; the abstract cites sub-70 millisecond inference across more than 100,000 concurrent sessions. In practice you pick by fraud pattern, data volume and explainability requirements, or combine them.

For fraud you've never seen, there are no labels, so unsupervised methods take over: isolation forests separate odd behaviour, autoencoders flag anything they can't reconstruct as normal, and clustering finds groups such as fraud rings. He credits these with catching over 26% of novel fraud patterns that traditional filters would have missed.

## Features are where fraudsters get caught

The feature engineering section is the most transferable part. Temporal features catch timing anomalies, like 500 gift cards bought in five seconds. Network features link users, devices and IPs. Behavioural features such as cursor movement and typing speed separate bots from humans. The best signals combine domains, so a fraudster can't fake all of them at once, and they have to keep evolving because static feature sets become targets.

Scale is its own problem. Black Friday means millions of transactions in minutes, decisions in under 150 milliseconds, and a system that can't go down: distributed, fault-tolerant microservices with failover infrastructure.

## Rules and humans stay in the loop

Lakkaraju doesn't argue for ripping out rules. Hybrid systems use rules as guardrails that encode business expertise, with ML finding the subtle patterns, like a pilot on autopilot who can still take the controls. He puts hybrid detection accuracy above 97%, with the bonus of explainability for regulators. For the cases automation can't settle, ML prioritises and routes them to the right analyst, highlights the suspicious signals, and learns from the analyst's decision.

Looking ahead, he points to explainable AI for auditable decisions, federated learning so companies can fight fraud together without sharing sensitive data, and models that update within seconds of a new attack pattern.

## Who should watch

Engineers building or inheriting a payments risk system, and product people who need to argue that false declines are a revenue problem. It's an architecture-and-concepts talk without code.

## Related Conf42 talks

- [Real-Time Fraud Prevention at Scale: SRE + Advanced ML for MCCA Reimbursement Protection](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sasidhar_Reddy_Somula_real_time_fraud) by Sasidhar Reddy Somula adds the reliability angle.
- [Building Resilient AI Platforms: Engineering Financial Fraud Detection at Scale](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial) by Rahul Ganti looks at the platform underneath.
- [AI-Powered Payment Systems: Balancing Security and Experience Through Intelligent Fraud Prevention](https://www.conf42.com/Large_Language_Models_LLMs_2025_Arpit_Mittal_payment_security_fraud) by Arpit Mittal shares the same false-decline worry.

[Watch Surendra Lakkaraju's talk](https://www.conf42.com/Machine_Learning_2025_Surendra_Lakkaraju_ecommerce_fraud)

[Watch the talk on YouTube](https://youtu.be/q95G2WkwEv4).

## Watch the talk

[Harnessing Machine Learning to Combat E-commerce Fraud: Real-time Detection, Advanced Feature Engineering, and Scalable Systems](https://www.conf42.com/Machine_Learning_2025_Surendra_Lakkaraju_ecommerce_fraud) at Conf42 Machine Learning 2025.
