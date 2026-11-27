# Why most ML models never ship, and the MLOps pillars that fix it

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/ml-models-are-products-not-projects

In short: Bharath Reddy Baddam of New York Life at Conf42 MLOps 2025 on orchestration, infrastructure, monitoring and CI/CD that move models from lab to production.

Only about one in five ML models makes it to production, according to the research Bharath Reddy Baddam opened with, and his takeaway at Conf42 MLOps 2025 was to treat machine learning as a product, not a project. Bharath, a Senior Salesforce Developer at New York Life Insurance Company with nine years in Salesforce cloud and AI work across finance, healthcare and real estate, organised the talk around five pillars that close the gap between a notebook and a service.

This is an introductory-to-intermediate roadmap. If you are new to MLOps or need a structure to explain it to a team, it is a tidy one; if you already run Kubeflow in anger, skim to the testing section.

## Proofs of concept die of the same causes

Bharath's list of barriers will be familiar: reproducibility, a gap between research and engineering, no standard deployment process, weak monitoring and maintenance, testing methods that don't fit ML, and poor integration with enterprise systems. He then walked the maturity curve from isolated notebooks and one-off deployments, through basic training automation, to CI/CD for ML and finally full maturity with monitoring, drift detection, retraining and rollback. Mature organisations, he said, cut deployment time by 80% and sustain 95% accuracy in production, and he stressed that the shift is cultural as much as technical.

## Pick orchestration tools for the team you have

The orchestration section compares three tools fairly. Kubeflow is Kubernetes-native with strong model serving, a fit if you already live on Kubernetes. MLflow is lightweight for experiment tracking and a model registry. Apache Airflow is a general workflow engine that handles complex, data-heavy processes without being ML-specific. Many organisations mix them, for example MLflow for tracking with Kubeflow for deployment. His test for any tool: does it fit our workflow and skills, or are we adding complexity for its own sake?

## Real-time inference is an infrastructure problem

Infrastructure as code with Terraform, Docker to kill the works-on-my-machine bug, CI/CD across dev, test and prod, and Kubernetes autoscaling form the base. For real-time use cases like fraud detection, chatbots and recommenders, he added horizontal scaling, load balancing with health checks, Redis caching for frequent queries, and GPUs where they earn their keep. His example: a healthcare client's real-time insurance eligibility checks went from minutes to milliseconds on an optimised autoscaling setup.

## Monitoring and testing keep the model honest

Monitoring covers three layers: data drift (statistical checks such as divergence measures and the population stability index), model performance (accuracy, F1, AUC against benchmarks) and operational metrics (latency, throughput, resource use). When drift shows up, retraining can trigger on a performance threshold, a schedule, or a significant distribution shift. New models then go out as shadow deployments running silently in parallel, canaries starting at 5% of traffic, A/B tests that measure business impact, and automated rollback when the newcomer underperforms.

The CI/CD-for-ML test suite is the most reusable slide: data validation (schema checks, missing values), model performance tests that block regressions, integration tests over the whole pipeline, load and performance tests, and security and compliance checks for GDPR and HIPAA.

## Who should watch

Engineers moving from application development into ML platforms, and leads who need a shared vocabulary for an MLOps roadmap. It is a map, not a deep implementation guide.

## Related Conf42 talks

- Tomas Fernandez (Semaphore) on [MLOps: From Jupyter to Production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production).
- Ryan Dawson (Seldon) with an early classic, [Machine Learning in Production: An Intro to MLOps](https://www.conf42.com/Site_Reliability_Engineering_2020_Ryan_Dawson_machine_learning_in_production).
- Noa Goldman (DagsHub) on [A Hitchhiker's Guide to the MLOps Experience](https://www.conf42.com/Machine_Learning_2023_Noa_Goldman_hitchhiker_guide_mlops_experience).

[Watch Bharath Reddy Baddam's talk](https://www.conf42.com/MLOps_2025_Bharath_Reddy_Baddam_bridging_mlops_gap)

[Watch the talk on YouTube](https://youtu.be/gAltdyeaI1U).

## Watch the talk

[Bridging the MLOps Gap: From AI Research to Production-Ready Systems](https://www.conf42.com/MLOps_2025_Bharath_Reddy_Baddam_bridging_mlops_gap) at Conf42 MLOps 2025.
