# Cloud-native AI patterns, from containers to drift detection

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/cloud-native-ai-patterns-separate-training-inference

In short: Bhaskar Goyal (Google) at Conf42 Machine Learning 2025 on the cloud-native patterns behind enterprise AI, from IaC and layered stacks to split training and inference.

Getting a model to work in a notebook is a weekend. Getting it to production reliably, many times a week, is an architecture. At Conf42 Machine Learning 2025, Bhaskar Goyal, Software Engineer at Google, walked through the cloud-native patterns that make that second part repeatable: containers, infrastructure as code, a layered stack, separate training and inference environments, feature stores, ML-aware Kubernetes, accelerator scheduling, CI/CD for models and automated monitoring.

It is a well-organised tour of the whole stack in about twenty minutes, so think of it as a checklist you can hold your own platform against.

## Containers and IaC kill "works on my machine"

Bhaskar starts with the contrast everyone in ML has lived: manual steps, handoffs between data science and ops, and deployment cycles measured in weeks. The first two fixes are old DevOps ideas applied to ML. Containers bundle code, libraries and dependencies so the environment is identical from development to production, and minimal inference images cut both latency and attack surface. Infrastructure as code, with Terraform or Pulumi, makes clusters and networks declarative, version-controlled and easy to roll back. He cites industry and project figures like a 90% reduction in configuration drift and 65% faster disaster recovery, presented as typical outcomes rather than a single case study.

## Training and inference want opposite things

The idea most worth stealing is the split. Training wants massive GPU clusters, batch optimisation and cheap interruptible spot instances, and can be ephemeral: spin up, train, tear down. Inference wants low latency, autoscaling, right-sized compute and high availability. Running both on one environment means one of them is always configured wrong. Bhaskar connects the split to 99.9% or higher inference uptime as a common SLA target, and to lower cloud costs from using spot capacity only where restarts are acceptable.

## Feature stores fix training-serving skew

His feature store section is a clean explanation of why the component exists: standard feature definitions, versioned storage with metadata, point-in-time correct retrieval for reproducible training, and low-latency serving for real-time predictions. The headline benefit is the notorious training-serving skew, when the feature computed in training differs from the one computed in production. Anyone who has chased a model that was great offline and mediocre online will nod here.

## Kubernetes needs ML-shaped extensions

On orchestration he lists the patterns that make Kubernetes ML-aware: custom resources like TFJob and PyTorchJob for distributed training, operators that encode the ML lifecycle, horizontal pod autoscaling on request volume or GPU utilisation, and a service mesh such as Istio for canary releases, A/B testing models and mutual TLS. For accelerators: device plugins, multi-tenant GPU sharing, NUMA-aware scheduling, mixed-precision inference, and hibernating idle GPUs and TPUs, which matters given what they cost per hour.

## Deployment is not the end

The last stretch covers MLOps pipelines (continuous integration with data and model validation gates, continuous delivery that packages models with Helm charts, continuous deployment with blue-green or canary rollouts and automated rollback) and monitoring. Models degrade as data drifts, so monitoring has to watch inputs and predictions, trigger retraining, and tie ML metrics to business KPIs so the value of the model stays visible.

## Who should watch

Platform engineers inheriting an ML workload and ML engineers who want the ops vocabulary. It is a broad, vendor-neutral overview, not a Google product talk and not a hands-on demo; the numbers are industry-reported ranges, so benchmark your own.

## Related Conf42 talks

- [Jim Dowling (Hopsworks) on why the ML pipeline is a myth and feature/training/inference pipelines are the answer](https://www.conf42.com/Python_2023_Jim_Dowling_pipeline_myth_production_ml_systems_feature_training_inference_pipelines), the feature store argument from first principles.
- [Gangadharan Venkataraman (Starbucks) on developer-centric ML inference platforms on Kubernetes](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes), the inference half built out.
- [Tomas Fernandez (Semaphore) on MLOps from Jupyter to production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production), for the CI/CD part done hands-on.

[Watch Bhaskar Goyal's talk](https://www.conf42.com/Machine_Learning_2025_Bhaskar_Goyal_enterprise_cloud_patterns)

[Watch the talk on YouTube](https://youtu.be/kK_Bh2hDEoo).

## Watch the talk

[Cloud-Native AI at Scale: Architectural Patterns for Enterprise Success](https://www.conf42.com/Machine_Learning_2025_Bhaskar_Goyal_enterprise_cloud_patterns) at Conf42 Machine Learning 2025.
