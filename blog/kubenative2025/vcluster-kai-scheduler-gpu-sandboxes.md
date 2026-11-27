# Run a GPU scheduler per team by putting it in a virtual cluster

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/vcluster-kai-scheduler-gpu-sandboxes

In short: Piotr Zaniewski (vCluster) at Conf42 Kube Native 2025 demos NVIDIA's KAI Scheduler inside vCluster for fractional GPUs and per-team scheduler versions.

Upgrading the one scheduler every GPU team depends on is the kind of change that gets scheduled for a Friday and regretted by Saturday. At Conf42 Kube Native 2025, Piotr Zaniewski, Head of Engineering Enablement at vCluster, showed a way out: run NVIDIA's open-source KAI Scheduler inside a virtual cluster, so each team gets its own scheduler version and an upgrade's blast radius shrinks to one disposable pod.

This is a vendor talk in the honest sense. vCluster Labs makes vCluster, and the session is a live demo of it, run on a local kind cluster with an older NVIDIA consumer card passed through to Docker. The setup is published with the video so you can reproduce it on your own GPU.

## Kubernetes inside a pod, with a syncer in the middle

vCluster runs a full, certified Kubernetes control plane inside a pod on a host cluster: an API server, a controller manager, a data store (SQLite in the demo, with etcd or an external backend for high availability) and optionally its own scheduler. The key component is the syncer, which runs a reconciliation loop that copies resources between the virtual cluster and the host, handling name collisions along the way and configurable down to which resource types cross over.

The result is cheap. Zaniewski pointed out the virtual cluster pod in the demo using roughly 370 MB of memory, which is why spinning one up per team, per test or per CI run is realistic where a new EKS cluster is not.

## KAI Scheduler slices the GPU

NVIDIA open sourced the Kubernetes AI scheduler in 2025. It adds fractional GPU allocation, queue-based scheduling and topology awareness. In the demo, two pods asked for 20% and 10% of the same GPU through annotations, with the KAI scheduler name and the NVIDIA runtime class set, and both landed on the one card exactly as configured. The abstract cites utilisation going from 40% to 90% with fractional GPUs. There was also a small GPU-backed web app that wrote SRE horror-story haiku on request, which is the most on-brand demo app a Kubernetes conference has seen.

## Upgrades without a shared blast radius

The real argument is about risk. With one scheduler on a big shared cluster, a buggy release leaves every dependent pod pending, a bad CRD upgrade can corrupt namespaces, and teams wait on each other for features. He cited a New Relic 2024 figure of enterprise downtime costing up to a million dollars per hour.

Inside a virtual cluster, the scheduler is one more workload. The vCluster config enables a virtual scheduler, syncs nodes, node labels and runtime classes from the host so pods can target GPU nodes, and uses a setting that stops vCluster from taking ownership of pods when you want the host scheduler instead. He then created two virtual clusters, team stable and team beta, installed different KAI Scheduler versions in each, and ran the same fractional GPU pods in both, while a third team kept using the host cluster's default scheduler.

## Rollback is a delete

Testing a scheduler upgrade without a new host cluster takes minutes instead of hours. Rolling back took about 39 seconds in the demo: delete the virtual cluster, and nothing else on the host notices. That turns A/B testing of scheduler versions into something you can do in production, team by team.

## Who should watch

Platform engineers and SREs running shared GPU clusters for ML, research and inference teams with different version needs. You will get the most out of it if you already know Kubernetes scheduling basics; it moves quickly through vCluster internals into the demo.

## Related Conf42 talks

- [Cell-Based Isolation for Multi-Tenant Platforms on Kubernetes](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) by Lahiru De Silva (WSO2) looks at isolation beyond namespaces.
- [Running vLLM Inference on Kubernetes Across Clouds](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) by Kosseila Haddalene (Cloudthrill) covers what runs on those GPUs.
- [The Art of Complex Deployments in Kubernetes Using Argo Rollouts](https://www.conf42.com/Cloud_Native_2024_Karan_Jagtiani_complex_deployments_kubernetes) by Karan Jagtiani (Storylane) is the progressive-delivery side of safe upgrades.

[Watch Piotr Zaniewski's talk](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant)

[Watch the talk on YouTube](https://youtu.be/FGLb4xDZ2VY).

## Watch the talk

[Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) at Conf42 Kube Native 2025.
