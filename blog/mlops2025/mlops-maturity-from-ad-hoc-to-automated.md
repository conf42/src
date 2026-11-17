# An MLOps maturity model from ad hoc notebooks to full automation

Conf42 Blog, 2025-09-13, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/mlops-maturity-from-ad-hoc-to-automated

In short: Srikanth Vissarapu of Meta at Conf42 MLOps 2025 on maturity levels, validation layers, canary and A/B rollouts, and cost levers for ML pipelines.

Most ML projects never reach production, and many that do fail to deliver. At Conf42 MLOps 2025, Srikanth Vissarapu, a software engineer at Meta, laid out a maturity model for ML pipelines and the architecture patterns that move a team from ad hoc experiments to end-to-end automation. His argument: data quality and collaboration sink more ML initiatives than models do.

The talk is a broad blueprint rather than a Meta case study. Srikanth described several of his failure statistics as ballpark figures, which is a fair way to read them: directional evidence that most production ML trouble starts upstream of the model.

## Four levels of maturity

Level zero is ad hoc experimentation: manual work, no standard workflow, fragmented collaboration, no success metrics. Level one adds basic pipeline automation, maybe a few scheduled jobs, but governance is thin, teams are siloed and monitoring can't spot drift. Level two brings continuous integration with repeatable pipelines, version control for every model, automated testing and proactive monitoring. Level three is end-to-end automation with centralised pipelines, governance and compliance baked in, and metrics captured at every stage.

His reading of the obstacles puts data quality on top, which he linked to more than half of production ML failures, followed by lack of standardisation, insufficient monitoring and governance gaps. Garbage in, garbage out never retires.

## Four validation layers before a model ships

The validation framework is the most practical section. Data validation comes first: schema enforcement, distribution checks and drift detection on the data set. Then model accuracy measured against real production data and business KPIs, not just the training split. Then operational checks: a model that is accurate but slow still disappoints users, so latency, throughput and resource use get validated too. Last, ethical validation for bias and consistency.

His best practices: write clear pass/fail thresholds for each step, enforce them inside the CI/CD pipeline rather than by hand, and keep a history of validation results as a measure of how your MLOps practice is maturing.

## Canary, blue-green and A/B are different questions

On delivery, Srikanth separated the strategies cleanly. A canary exposes a small slice of traffic to the new model and promotes it as metrics hold up. Blue-green runs a parallel environment and switches over when it looks good. A/B testing exposes users to two versions and lets business and technical metrics decide. Around them sit model artifact versioning, dependency management, containerised model serving in Docker, and infrastructure as code.

## Cost is part of the architecture

The cost section is a welcome inclusion. Compute (GPUs above all), data storage and processing for pipelines and feature stores, tooling, and operational overhead are the main drivers. The levers he listed: autoscaling to match workload, model pruning, quantisation and distillation to shrink models with similar performance, end-to-end automation, and visibility into where the money goes. He finished with organisational advice: cross-functional MLOps teams, joint ownership of model performance and business outcomes, and a centre of excellence that offers self-service tooling.

## Who should watch

Teams trying to place themselves on a maturity curve, and leads writing an MLOps strategy document. The talk is long and general; engineers after a specific stack should treat it as a checklist to compare against.

## Related Conf42 talks

- Saiteja Jonnalagadda (CVS Health) on [Engineering Data Quality Into MLOps at Healthcare Scale](https://www.conf42.com/MLOps_2026_Saiteja_Jonnalagadda_healthcare_quality_data).
- Srihari Godleti (Roku) on [Taming Data Skew in Production ML Pipelines](https://www.conf42.com/Machine_Learning_2026_Srihari_Godleti_fairness_bias_mitigation).
- Alejandro Cantos (Barbara) with an [Introduction to MLOps at the Edge](https://www.conf42.com/Machine_Learning_2023_Alejandro_Cantos_introduction_mlops_edge).

[Watch Srikanth Vissarapu's talk](https://www.conf42.com/MLOps_2025_Srikanth_Vissarapu_lab_production_building)

[Watch the talk on YouTube](https://youtu.be/uP_yiHTPOL8).

## Watch the talk

[From Lab to Production: Building Scalable MLOps Pipelines That Actually Work - A Data-Driven Blueprint for ML Success](https://www.conf42.com/MLOps_2025_Srikanth_Vissarapu_lab_production_building) at Conf42 MLOps 2025.
