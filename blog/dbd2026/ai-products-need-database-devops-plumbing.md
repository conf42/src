# Enterprise AI fails in the plumbing, not the model

Conf42 Blog, 2026-05-07, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/ai-products-need-database-devops-plumbing

In short: Bharat Kumar Reddy Karumuri of General Motors at Conf42 Database DevOps 2026 on the data, MLOps and governance layer that turns AI demos into products.

Most enterprises can build an AI proof of concept; far fewer can run one that a business process trusts. At Conf42 Database DevOps 2026, Bharat Kumar Reddy Karumuri, Senior Data Scientist at General Motors, argued that the gap is the engineering layer between data and models, and that Database DevOps practices are what fill it.

It is an architecture talk at the level of principles, drawn from his twelve-plus years across healthcare, marketing and technology, and pitched, in his words, as lessons shared "over coffee, just with better slides". There is no code or demo; the value is in the checklist and the framing.

## The model is the easy part

Bharat's opening line of argument: the difference between an interesting AI demo and a reliable AI product usually comes down to the system behind it. Isolated analytics, unreliable pipelines and a governance gap between them make AI feel brittle. His joke for it is that enterprise AI looks amazing in PowerPoint and a little nervous in production, and the nervousness comes from weak plumbing.

If schemas drift silently and data contracts are fuzzy, model quality is compromised before anyone touches a hyperparameter. So before asking how good the model is, ask how trustworthy the system feeding it is.

## Three pillars of Database DevOps for AI

He splits the data layer discipline into three:

- **Continuous integration for data**: automated validation, schema contract tests and data quality gates on every pipeline change.
- **Schema evolution management**: versioned, backward-compatible schemas, so an upstream change is not a small heart attack for every downstream feature.
- **Pipeline observability**: end-to-end lineage, SLA monitoring and alerting at every transformation step.

On top of that sit the classic pipeline properties: idempotency so reruns are safe, modular stages you can deploy and test alone, fault tolerance, and versioned datasets so you can answer "why did the model behave differently last Tuesday?" by checking out the old version and comparing.

## Models are deployable assets, not research artifacts

MLOps closes the loop with model versioning, CI/CD, and canary or shadow deployments, turning a once-a-quarter release drama into a repeatable process. A model in a notebook is a science project; with testing, monitoring and rollback it becomes a product.

For generative AI he makes the case for retrieval-augmented generation over fine-tuning alone on four counts: freshness without retraining, answers traceable to source documents, lower cost than tuning every domain variant, and access controls on the data layer that carry through to the AI response.

## Silent failure is the enemy

The observability section is the strongest. AI systems rarely fail with an explosion; they fail quietly, as a feature goes stale, a distribution shifts or accuracy slips, and business trust erodes. Bharat layers monitoring accordingly: pipeline SLAs, schema drift and quality scores at the data layer; distribution shift, freshness and missing values at the feature layer; drift, latency, accuracy and business KPIs at the model layer. A visible outage hurts, but a confidently wrong answer at scale is usually worse. Governance bolted on after launch, he says, "becomes archeology".

For real-time decision platforms the stack adds online feature stores, streaming pipelines, autoscaling model serving with latency budgets, and HTAP-style integration so decisions run inside the operational workflow. Every component must scale and be observed on its own, because one slow dependency breaks the whole real-time contract.

## Who should watch

Data and platform leads making the case for investing in data CI, lineage and model monitoring before the next GenAI launch. It is a well-organised overview rather than a how-to, so engineers already running feature stores and drift monitoring will recognise most of it.

## Related Conf42 talks

- [Tim Markin on feature stores and their management](https://www.conf42.com/Machine_Learning_2026_Tim_Markin_feature_stores_management) at Conf42 Machine Learning 2026.
- [Sunil Kumar Mudusu on data quality validation](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) at Conf42 Machine Learning 2025.
- [Tomas Fernandez on taking MLOps from Jupyter to production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production) at Conf42 Machine Learning 2024.

[Watch Bharat Kumar Reddy Karumuri's talk](https://www.conf42.com/Database_DevOps_2026_Bharat_Kumar_Reddy_Karumuri_models_training_telemetry)

[Watch the talk on YouTube](https://youtu.be/TWKRIcrJTN0).

## Watch the talk

[From Data Pipelines to AI Products: Operationalizing Machine Learning and Generative AI in Enterprise Decision Platforms](https://www.conf42.com/Database_DevOps_2026_Bharat_Kumar_Reddy_Karumuri_models_training_telemetry) at Conf42 Database DevOps 2026.
