# An ML inference platform succeeds when deploying a model is boring

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ml-inference-platforms-built-for-developers

In short: Gangadharan Venkataraman of Starbucks covers Kubernetes ML inference at Conf42 Platform Engineering 2025, from CRDs and canaries to feature stores and caches.

A model that works in a notebook needs one pod. The same model serving a marketing use case in production might need a thousand, depending on latency targets and the features it pulls. At Conf42 Platform Engineering 2025, Gangadharan Venkataraman, Technical Lead for the AI/ML Platform at Starbucks, walks through how to build a Kubernetes-based ML inference platform that scales to that kind of load while keeping the developer experience simple enough that shipping a model feels routine.

It is a long, practitioner-flavoured talk, full of examples from retail and e-commerce, and it covers the whole path from orchestration to team structure.

## Three layers that have to agree

Venkataraman's architecture has three pillars. The orchestration layer is Kubernetes doing scheduling, resource allocation, container lifecycle, service discovery and GPU scheduling. The model serving layer loads and routes models, batches where it helps, and reformats responses into whatever the calling application expects. The data pipeline layer supplies features at three speeds: offline historical data, near-real-time features from Kafka streams, and true real-time checks just before a response goes out. His example: a model may pick ten items for a customer, but something has to confirm they are still in stock before the customer sees them.

## Teach Kubernetes what a model is

The orchestration detail is custom resource definitions. CRDs let teams talk in ML terms (a model deployment, a feature pipeline, an experiment run) instead of raw Deployments and Services, and custom operators handle the lifecycle: deployment workflows, autoscaling on inference load, and integration with feature stores and model registries. He points to Databricks as an example of the end-to-end pattern, with training, a feature store and connectors to managed Kubernetes on Azure and AWS.

The developer experience goal follows from that. Check code into a branch and it deploys to a dev namespace automatically. Merge to main and CI/CD tests, validates and deploys to production. No hunting through consoles.

## Rollouts in percentages, rollbacks without a meeting

The CI/CD section is where the platform pays for itself. Automated regression, integration, sanity and smoke tests run on every model change, and if they fail, the deployment never happens. After deployment, monitoring triggers automatic rollback when failures cross a threshold, which only works if artifact management keeps the last few stable versions ready. Canary deployment means one pod gets the new model first; gradual traffic shifting moves through 1%, 5%, 10% and then all traffic. He adds the pragmatic exception: for a hotfix, you need the option to go straight to 100%.

## Cold starts and caches

Serving gets three topics. Container images for ML need multi-stage builds to keep large artifacts and GPU dependencies out of the runtime image. Autoscaling keeps a minimum pod count warm and scales up with request rate. Cold-start optimisation covers model preloading, lazy initialisation and shared model caches; when a pod restarts its local cache is gone, so a persistent shared cache tier keeps latency in milliseconds instead of falling back to the database. He comes back to caching later for model chaining, where each cache hit saves a call to another model.

Monitoring rounds it out: accuracy metrics, prediction distribution and feature drift detection, so retraining happens when the data moves rather than on a fixed schedule.

## The people part

Unusually for an infrastructure talk, Venkataraman spends real time on organisation: a platform team that owns the infrastructure, scientists who build on it, domain teams that consume model output, and the business that defines the problem. His Starbucks example is a store where coffee wait times run long and a model helps rebalance baristas. Governance means design reviews, pull-request reviews and security scans that block merges, plus communicating platform migrations early so consuming teams are not surprised. Security for sensitive data, audit trails and data lineage get their own section.

## Who should watch

Engineers building or inheriting an internal ML serving platform on Kubernetes, especially the ones fielding complaints from data scientists that deployment takes too long. If you already run KServe or Seldon in production, the organisational and caching sections are the fresh material.

## Related Conf42 talks

- [Running vLLM Inference on Kubernetes Across Clouds](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) by Kosseila Haddalene, Conf42 MLOps 2026
- [Horizontal Autoscaling with Kubernetes](https://www.conf42.com/Kube_Native_2022_Rob_Richardson_horizontal_autoscaling) by Rob Richardson, Conf42 Kube Native 2022
- [MLOps in Healthcare: Scaling AI Model Deployment Through Strategic Automation and Monitoring Frameworks](https://www.conf42.com/MLOps_2025_Aishwarya_Pai_mlops_healthcare_scaling) by Aishwarya Pai, Conf42 MLOps 2025

[Watch Gangadharan Venkataraman's talk](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes)

[Watch the talk on YouTube](https://youtu.be/JHxK3LhKCvo).

## Watch the talk

[Building Developer-Centric ML Inference Platforms: From Kubernetes Orchestration to Production Excellence](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes) at Conf42 Platform Engineering 2025.
