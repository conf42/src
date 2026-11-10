# Running vLLM Inference on Kubernetes Across Clouds: A Production-Ready GPU Blueprint

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Kosseila Haddalene](https://www.conf42.com/speaker_Kosseila_Haddalene) (Founder | AI infrastructure Lead @ Cloudthrill). Page: https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu

## Abstract

If you’ve tried vLLM locally, you’ve seen how fast it can generate tokens. The real challenges appear when serving production traffic: multiple models, 100s of concurrent requests, pod failures, and unpredictable tail latency. These are the same issues repeatedly raised by the community when running vLLM on Kubernetes.  In this talk, I’ll share an open-source, Terraform-driven vLLM production stack that runs consistently on EKS, AKS, GKE, and Nebius Mk8s. The talk is based on my upstream contributions to the official vLLM production stack. We’ll cover GPU-optimized Kubernetes deployments for vLLM workloads, tiered inference, and end-to-end automation, from cluster bootstrap to SSL-enabled, inference-ready endpoints, along with built-in observability using Grafana dashboards.  This session is aimed at platform engineers and MLOps teams building GPU-backed LLM inference w/o cloud lock-in.
