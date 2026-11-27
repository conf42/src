# An MLOps primer for fraud and risk models in banking

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/mlops-fraud-risk-intro-microsoft

In short: Dileep Kumar Kanimetta (Microsoft) at Conf42 MLOps 2025 gives an intro to MLOps for bank fraud and risk models, from IaC and CI/CD to drift and governance.

If your fraud model takes weeks to reach production because someone sets up servers by hand, the fraudsters are iterating faster than you are. At Conf42 MLOps 2025, Dileep Kumar Kanimetta, Advanced Cloud and Customer Experience Engineer at Microsoft, gave an introductory tour of how MLOps helps financial institutions run fraud detection and risk models reliably, with infrastructure as code, CI/CD, drift-triggered retraining and governance as the four load-bearing pieces.

This is a first talk on the subject rather than a deep technical one, and that is how to approach it.

## What breaks without MLOps

Dileep draws on more than 19 years in IT, including work on SWIFT integration onto Azure, which gave him a view of how ML can help with fraud and risk in payment processing. The problems he describes are the classic ones. Deployment is manual, so a team spends weeks standing up systems and installing code instead of improving models. Models are poorly tracked, so they drift and lose accuracy without anyone noticing. And governance gaps create compliance problems in an industry where regulators are watching.

His one-line definition: MLOps is to machine learning what DevOps is to software development, with the promise that deployment can happen in hours instead of the old, slow way.

## Four building blocks

The core of the talk is a blueprint of four components:

- **Infrastructure automation**, with the whole environment defined as code. He names Terraform and stresses isolated development environments so new projects cannot disturb current ones, and a separate, secured production environment.
- **CI/CD pipelines**, which he describes as an assembly line for AI: automated testing, pre-deployment checks and post-deployment validation.
- **Monitoring and alerting**, watching data accuracy, model metrics and feature importance, so drift is caught early.
- **A governance framework**, starting with documentation of models, data and process steps so compliance becomes part of the flow rather than an audit scramble.

## Retraining on a trigger, not a calendar

The retraining section is the most actionable. Drift detection watches for changes in incoming data; when a shift is detected, the training pipeline updates the model and it goes back through validation before serving. Dileep's claim is that with this automated, leading firms deploy models in hours rather than days.

He adds A/B testing to validate each change before full launch, automated bias detection so the system treats customers fairly across backgrounds and ages, and auto-scaling serving infrastructure because fraud attacks do not wait for business hours. In finance, as he puts it, every second matters and 24/7 availability is the expectation.

## Cloud choice and team shape

On platforms, Dileep is pragmatic: Azure, Google Cloud or AWS can all host an ML platform, and the choice comes down to your needs. On people, he argues for cross-functional MLOps teams where data scientists, engineers and operations actually talk to each other, because the pipeline crosses all their boundaries.

His closing advice is to start by measuring where you are and what needs to improve before building anything.

## Who should watch

Engineers and managers in financial services who are new to MLOps and want the vocabulary and the main components in one sitting. If you already run drift-triggered retraining in production, pick one of the more detailed finance talks below.

## Related Conf42 talks

- [AI-Enhanced Fraud Detection: Transforming Financial Services with Real-Time Analytics and Machine Learning](https://www.conf42.com/Machine_Learning_2025_Sudhakar_Kandhikonda_fraud_detection)
- [AI-Powered Fraud Detection in Cloud-Native Digital Payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security)
- [AI-Powered Fraud Detection with Advanced Machine Learning Techniques](https://www.conf42.com/DevOps_2025_Vinod_Upputuri_ai_fraud_machine)

[Watch Dileep Kumar Kanimetta's talk](https://www.conf42.com/MLOps_2025_Dileep_Kumar_Kanimetta_mlops_scale_operationalizing)

[Watch the talk on YouTube](https://youtu.be/8YEdJeF9Y48).

## Watch the talk

[MLOps at Scale: Operationalizing Machine Learning for Financial Risk and Fraud Detection in Cloud-Native Environments](https://www.conf42.com/MLOps_2025_Dileep_Kumar_Kanimetta_mlops_scale_operationalizing) at Conf42 MLOps 2025.
