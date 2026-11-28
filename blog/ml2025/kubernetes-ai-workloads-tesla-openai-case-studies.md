# What Tesla and OpenAI show about Kubernetes for AI workloads

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/kubernetes-ai-workloads-tesla-openai-case-studies

In short: Praneel Madabushini (NVIDIA) at Conf42 Machine Learning 2025 on GPU scheduling, self-healing and distributed training on Kubernetes, via Tesla and OpenAI.

A cluster sized for last year's models is underprovisioned today. At Conf42 Machine Learning 2025, Praneel Madabushini, Senior DevOps Engineer at NVIDIA with around ten years in DevOps, explained why Kubernetes became the default home for AI and ML workloads, then used Tesla and OpenAI as case studies of what the pattern looks like at extreme scale.

The case studies are drawn from public material about both companies, not inside knowledge, and the talk is upfront that it is about patterns you can copy.

## AI workloads break static clusters

Praneel's opening is a list of ways AI differs from a web service. Training is resource-hungry enough to eat a large share of a data centre's power budget. Data volumes and parameter counts keep compounding, so static infrastructure is always behind. Distributed pipelines spanning object stores, message queues and GPU nodes multiply failure modes, and without automated recovery the mean time to repair stretches into hours or days. Thousands of GPUs and no self-healing is how you lose a weekend of training.

## What Kubernetes brings to the table

The middle section maps each problem to a Kubernetes feature:

- **Declarative GPU provisioning.** Describe GPU type, driver and CUDA base image in YAML; the NVIDIA device plugin handles the rest.
- **Scaling.** The horizontal pod autoscaler fed by NVIDIA metrics, the vertical pod autoscaler for right-sizing, and KEDA for event-driven bursts.
- **Self-healing.** If a GPU node panics, the scheduler restarts the pod on healthy hardware and pod disruption budgets keep training jobs at quorum. Liveness and readiness probes catch hung processes.
- **Multi-tenancy.** Namespaces, quotas, taints and node selectors let you reserve one pool of A100s for a research team and a pool of H100s for production inference.
- **Monitoring.** Prometheus and Grafana dashboards for GPU temperature, power draw, PCIe throughput and network I/O.

He backs these with CNCF survey numbers and aggregated adoption statistics; the point is less any single figure than how normal running AI on Kubernetes has become.

## Tesla: hybrid cloud and over-the-air models

In Praneel's account, Tesla's autonomous driving pipeline processes video from eight cameras per car, roughly 1.5 TB of data per vehicle a year, with Kubernetes orchestrating thousands of containers for training. The stack he describes is PyTorch and TensorFlow for training, Triton Inference Server for inference, NVIDIA GPUs plus custom chips, data parallelism across GPUs, and a hybrid of on-prem and cloud capacity to balance cost and performance. The detail that stands out is deployment: model improvements ship over the air as new container images, so the fleet runs current weights.

## OpenAI: scheduling as the competitive edge

For OpenAI, the case is about scheduling at scale. Praneel describes Horovod on Kubeflow for distributed training, Spark on Kubernetes for petabyte-scale ETL, Triton plus custom operators for serving at sub-50 ms latency, priority-based preemption so critical research runs keep their SLAs, and pods moving between CPU-only preprocessing and GPU training stages as the pipeline progresses. Distributed tracing and GPU telemetry raise alerts in under a second.

## The ecosystem around it

He closes with the tooling: Kubeflow for pipelines, Katib for hyperparameter tuning, TensorFlow operators, KServe, Seldon Core and Triton for serving, and security from SPIFFE/SPIRE workload identity, mutual TLS and Kata Containers for hardware-virtualised isolation of high-value models.

## Who should watch

DevOps and platform engineers about to put GPUs into a cluster for the first time, or anyone who has to justify Kubernetes for ML to leadership. If you already run Kubeflow in production, the case studies are the main new material.

## Related Conf42 talks

- [Mohit Gupta on building GPU performance validation into CI/CD for AI infrastructure](https://www.conf42.com/DevOps_2026_Mohit_Gupta_gpu_ci_validation), so the GPU nodes you schedule onto are actually healthy.
- [Piotr Zaniewski (vCluster) on multi-tenant, multi-scheduler GPU sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant), the multi-tenancy point in practice.
- [Kosseila Haddalene (Cloudthrill) on running vLLM inference on Kubernetes across clouds](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu), a production GPU blueprint for LLM serving.

[Watch Praneel Madabushini's talk](https://www.conf42.com/Machine_Learning_2025_Praneel_Madabushini_tesla_openai)

[Watch the talk on YouTube](https://youtu.be/rlkwXaOww4E).

## Watch the talk

[Harnessing Kubernetes for Scalable AI/ML Workloads: Insights from Tesla and OpenAI](https://www.conf42.com/Machine_Learning_2025_Praneel_Madabushini_tesla_openai) at Conf42 Machine Learning 2025.
