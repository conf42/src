# SiriusXM cut model deployments from 45 days to four hours

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/siriusxm-mlops-deploys-45-days-to-4-hours

In short: Jimmy Katiyar of SiriusXM at Conf42 MLOps 2025 on validation gates, CI/CD, monitoring and Kubernetes behind a jump from MLOps level one to three.

Machine learning projects rarely fail because the model is bad; they fail when someone tries to run it in production at scale. At Conf42 MLOps 2025, Jimmy Katiyar, Senior Product Manager at SiriusXM, showed how his organisation went from MLOps maturity level one to level three in 18 months, bringing model deployments down from 45 days to four hours while serving millions of daily transactions.

It is a product manager's view of an ML platform, which is a feature: the talk spends as much time on shared KPIs and team habits as on pipelines, and the numbers come with the organisational changes that produced them.

## Months to production is a business problem

Jimmy started with the familiar enterprise picture: deployments done by hand, environments that don't match between development and production, teams in silos, frequent incidents and painful compliance. When a model takes 60 to 90 days to reach production, competitors who iterate faster win. He framed maturity in four levels, from fully manual and ad hoc (level zero) through partial automation and continuous delivery to level three, where everything is automated and systems heal themselves.

## Four pillars, and the gate that mattered most

SiriusXM's architecture rests on four pillars: automated model validation, CI/CD pipelines, monitoring, and scalable infrastructure. The validation framework is the part worth copying. Every model passes three gates before going live: statistical performance (accuracy, precision, recall, F1 and business KPIs), operational readiness (latency, scalability, throughput) and compliance (explainability, bias detection, regulatory alignment). Jimmy credited those gates with a 94% reduction in production issues.

The CI/CD pipeline versions data sets, configurations and artifacts alongside code. Build and test covers containerisation, performance benchmarks and security scanning. Staging runs shadow deployments and A/B tests under load, and production relies on canary releases, automated rollbacks and audit logs. That pipeline is where 45 days became four hours.

## Monitoring that pays for itself early

Monitoring spans four dimensions: model performance, data quality, system operations and business impact, the last measured in revenue or conversion. In its first year the system caught 28 critical drift incidents before customers felt them. On the infrastructure side, Kubernetes handles orchestration and autoscaling, Apache Spark does distributed data processing, and load-balanced inference services sit behind strict access controls, encryption and audit logging. He reported 3.5 million inference requests a day at 99.99% uptime and under 50 ms latency.

## The hardest pillar is the one without a diagram

Jimmy was candid that technology doesn't solve mismatched skills, fragmented tools and inconsistent success metrics. Data scientists and engineers often don't speak the same language. SiriusXM unified development environments, standardised workflows and created shared KPIs, and he relayed that their VP of AI engineering considered getting both sides speaking one language the biggest win.

His roadmap has four phases: foundation (standard environments, version control, basic pipelines), automation (CI/CD, validation dashboards, model registry, metadata tracking), scale (Kubernetes orchestration, drift detection, automated rollback), and optimisation (feature stores, self-healing infrastructure, governance). The pitfalls are the ones every platform team has hit at least once: tool obsession, underestimating culture change, and over-complicating the first step. Start with one high-value use case.

## Who should watch

Product and engineering managers building an internal ML platform, and teams stuck at level one wondering what level three looks like in practice. Engineers wanting pipeline code will find the outline here and the details elsewhere.

## Related Conf42 talks

- Chinmay Naik (One2N) on [From DevOps to MLOps: Scaling Machine Learning Models to 2 Million+ Requests per Day](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Chinmay_Naik_devops_mlops_scaling).
- Ancilia Dmello (Ford Motor Company) on [Building Scalable, Observable MLOps Systems on Google Cloud](https://www.conf42.com/Machine_Learning_2026_Ancilia_Dmello_forecasting_inventory_retail).
- Anant Kumar (Salesforce) on [Building Resilient Apache Spark Clusters on Kubernetes for AI Workloads](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters).

[Watch Jimmy Katiyar's talk](https://www.conf42.com/MLOps_2025_Jimmy_Katiyar_model_production_building)

[Watch the talk on YouTube](https://youtu.be/WLolfgNUN-c).

## Watch the talk

[From Model to Production: Building Scalable MLOps Pipelines for Enterprise Systems](https://www.conf42.com/MLOps_2025_Jimmy_Katiyar_model_production_building) at Conf42 MLOps 2025.
