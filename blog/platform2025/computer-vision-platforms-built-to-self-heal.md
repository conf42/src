# Real-time computer vision needs a platform that heals itself

Conf42 Blog, 2025-08-19, updated 2026-11-09. https://www.conf42.com/blog/platform2025/computer-vision-platforms-built-to-self-heal

In short: Manoj Sai Jayakannan of George Mason University lays out a containerised, observable, self-healing platform for computer vision at Conf42 Platform Engineering 2025.

Computer vision is where ML platforms stop being forgiving. Video frames do not wait for a slow model, and a GPU node falling over mid-stream is a gap in the footage, not a retry. At Conf42 Platform Engineering 2025, Manoj Sai Jayakannan of George Mason University presents a playbook for AI platforms that serve real-time vision workloads: containerised pipelines, careful model rollout, three layers of observability and infrastructure that recovers without a human.

The talk is a compact reference architecture. It reads like the design doc you wish you had before your first GPU cluster went into production.

## Split the pipeline into pods with one job each

Jayakannan starts from three principles: infrastructure as code (Terraform or CloudFormation, so GPU-enabled environments can be replicated and versioned), GitOps with Git as the single source of truth and automated rollbacks, and testing that covers data validation and model validation, not only code.

The pipeline itself is modular. Ingestion pods pull video streams from IoT sensors. Preprocessing pods normalise and augment. Training pods use distributed GPUs. Inference pods serve predictions over REST or gRPC. GPU access comes through the NVIDIA container runtime and Kubernetes device plugins, builds are tied to Git commits so they are deterministic, and node pools are tuned for each stage. Horizontal autoscaling applies to inference, where load actually varies.

## Ship models like risky code, because they are

Model rollout gets three patterns, each for a different appetite for risk. Blue-green runs the new version beside the old and switches traffic. Canary releases expose a slice of users first. Shadow deployments run the new model on production traffic without showing its output to anyone, which is the cheapest way to find out that your new detector thinks every shopping trolley is a person.

Serving performance comes from three optimisations: request batching to keep GPUs busy, keeping hot models in memory to avoid cold starts, and accelerated serving frameworks such as TensorRT, Triton Inference Server and TorchServe. Jayakannan says these typically give a three- to five-fold throughput gain and quotes latency dropping from 200 ms to 15 ms.

## Watch the model, not only the machine

Observability spans three layers: infrastructure (CPU, GPU, memory, network), pipeline (success rates, queue latency, data integrity checks) and model (prediction drift, latency, error rates, fairness metrics). The tooling is mostly what you would expect: Prometheus and Grafana for infrastructure, OpenTelemetry for tracing through ML pipelines, and ML-specific monitoring tools for drift and bias detection. Tie those signals to alert thresholds and the system can respond to GPU saturation or falling accuracy before users see it.

## Recovery is a feature you test

Self-healing comes from ordinary Kubernetes mechanics used deliberately: liveness and readiness probes restart failing containers, cluster autoscaling adjusts compute, and chaos engineering with Chaos Mesh injects failures to prove the recovery actually works. To remove single points of failure he adds distributed processing across nodes and regions, geo-redundant clusters for disaster recovery and lower latency, and event-driven rerouting when a node dies.

The outcomes he reports from organisations doing this are 99.9% uptime, model updates in hours instead of weeks, and 20 to 40% lower cost from better GPU scheduling. He notes the same practices carry over to NLP, recommendation and generative AI.

## Who should watch

ML platform engineers moving vision models from notebooks to production, and SREs who have just been handed a GPU cluster. It is a checklist talk rather than a single case study, but nearly every item on it is concrete and nameable.

## Related Conf42 talks

- [Edge AI for Smart Camera IoT Devices](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing) by Madhu Niranjan Reddy Puduru, Conf42 IoT 2025
- [Cascade models in computer vision to boost accuracy and performance](https://www.conf42.com/Machine_Learning_2023_Argo_Saakyan_cascade_models_computer_vision_accuracy_performance) by Argo Saakyan, Conf42 Machine Learning 2023
- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) by Piotr Zaniewski, Conf42 Kube Native 2025

[Watch Manoj Sai Jayakannan's talk](https://www.conf42.com/Platform_Engineering_2025_Manoj_Sai_Jayakannan_vision_computer_deployments)

[Watch the talk on YouTube](https://youtu.be/s35rksKHhyI).

## Watch the talk

[Building Resilient AI Platforms at Scale: Engineering Infrastructure for Real-Time Computer Vision Deployments](https://www.conf42.com/Platform_Engineering_2025_Manoj_Sai_Jayakannan_vision_computer_deployments) at Conf42 Platform Engineering 2025.
