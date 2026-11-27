# The LLM era needs more MLOps, not less

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/llm-era-needs-more-mlops-not-less

In short: Naveen Edapurath Vijayan of AWS at Conf42 MLOps 2025 on automation, CI/CD, governance and monitoring for classic models and LLMs alike.

A model in a Jupyter notebook is an experiment; a model in production, monitored and governed at scale, is a business solution. That was the starting line for Naveen Edapurath Vijayan, Head of Engineering for AWS Central Economics, at Conf42 MLOps 2025, and his answer to whether large language models make MLOps obsolete was an emphatic no: they make it more necessary.

Naveen has 15-plus years in data analytics and ML, building petabyte-scale warehouses and models for finance and HR, and more recently agentic AI. He opened with a disclaimer that the views were his own, not Amazon's or AWS's. The talk is a crisp conceptual overview that maps each MLOps pillar onto its LLM equivalent, which is its most useful feature.

## Models fail silently when nobody watches

His cautionary tale was a credit risk model trained on pre-2020 data. When COVID changed consumer behaviour overnight (job losses, defaults, relief cheques), the model kept running unmonitored and misclassified risk for months, with heavy financial losses. Add the other usual suspects: brittle pipelines where a renamed column breaks the feature store, manual deployments where someone copies a model file and hopes, and models in production that haven't been retrained in months or years. LLMs then add cost explosions, hallucinations and compliance gaps on top.

## MLOps is DevOps plus data and models

Naveen's definition is tidy: MLOps applies continuous integration, delivery and infrastructure automation to machine learning, but where DevOps deals with code, MLOps deals with code, data and models. The lifecycle is a loop: ingest and validate data, train and fine-tune (tracked in MLflow or SageMaker), validate for accuracy, fairness, robustness and interpretability, deploy, then monitor and retrain automatically when metrics drift out of bounds. His retail example retrains recommendation models daily, validates them on test sets and rolls them out through shadow deployments.

## Every pillar has an LLM twin

This is the part worth bookmarking. Feature pipelines become prompt pipelines, with prompts and prompt chains version-controlled and tested. Automation that reruns preprocessing with Airflow or Kubeflow also refreshes a retrieval index when new documents are published and triggers evaluations, with nobody intervening by hand. CI/CD tools like DVC and MLflow run regression, bias and feature unit tests; for LLMs, each new prompt template is tested against historical customer interactions and shadow-deployed beside the old one. Fine-tuning is expensive, so automated evaluation pipelines keep you from retraining when you don't need to.

Monitoring widens from accuracy, latency, drift and infrastructure cost to hallucination rate, toxicity, bias and grounding, meaning whether answers tie back to real sources. He described enterprises running red teaming in production and flagging unsafe outputs for human review, and gave the example of a healthcare chatbot drifting into advice not grounded in medical sources, which guardrails need to catch instantly.

## Governance is the price of doing business

Enterprises need to answer which model made a decision, what data trained it and whether it was biased; a financial regulator may ask why a loan was denied. MLOps governance lets you produce the data set, the model version and the code. For LLMs, add provenance for fine-tuning data, red-teaming results, and the transparency obligations of GDPR and the EU AI Act. His best practices: infrastructure as code, feature stores and the emerging prompt stores, bias and safety evaluation inside CI/CD, and cross-functional teams that include compliance and business owners.

## Who should watch

Teams adding LLM features on top of an existing ML platform, and leaders deciding whether "LLMOps" needs a separate org chart. Practitioners after tooling depth will find a framework here, not a tutorial.

## Related Conf42 talks

- Artem Zamarajev (Amazon) on [Shipping LLM-Powered Features Reliably at E-commerce Scale](https://www.conf42.com/MLOps_2026_Artem_Zamarajev_llm_commerce_renders).
- Deepak Karunanidhi (Novartis) on the [Future of LLMs and Machine Learning Productionization](https://www.conf42.com/Large_Language_Models_LLMs_2024_Deepak_Karunanidhi_future_llms_productionization).
- Ofer Mendelevitch (Vectara) on [Measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations).

[Watch Naveen Edapurath Vijayan's talk](https://www.conf42.com/MLOps_2025_Naveen_Edapurath_Vijayan_mlops_scale)

[Watch the talk on YouTube](https://youtu.be/xo8usJEjcIQ).

## Watch the talk

[MLOps at Scale](https://www.conf42.com/MLOps_2025_Naveen_Edapurath_Vijayan_mlops_scale) at Conf42 MLOps 2025.
