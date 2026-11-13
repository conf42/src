# The Kubernetes platform decides how reliable your LLM service is

Conf42 Blog, 2026-06-12, updated 2026-11-09. https://www.conf42.com/blog/llms2026/kubernetes-platform-decides-llm-reliability

In short: Sergey Speranskiy at Conf42 LLMs 2026 on BGP anycast control planes, routable pod networks, GPU scheduling and canary rollouts for LLM workloads.

An LLM service is only as reliable as the cluster under it. Sergey Speranskiy, a senior infrastructure platform engineer, made that case at Conf42 Large Language Models 2026 in a compact talk on what breaks first when LLM workloads move from one experimental node to production Kubernetes, especially on-prem.

His closing line sums it up: "The model is important, but the platform decides how the model behaves under failure."

## LLM workloads expose weak platforms faster

A typical web service is CPU-bound, has short requests and scales by adding replicas. LLM services need scarce GPUs and lots of memory, run long requests, and have latency that depends on model size, prompt length, generated tokens, batching and queue time. So bad scheduling, flaky networking or an unexpected restart turns into a user-visible problem quickly.

The experiment phase hides all this. One node, manual deploys and SSH debugging are fine until production asks for redundancy across failure domains. Losing one node, switch or rack can take a big share of your GPU capacity with it.

## Anycast the API server, run BGP on the host

The control plane is not on the request path, but scheduling, rollouts and autoscaling all depend on it. Speranskiy's preferred design gives the Kubernetes API a virtual IP announced by BGP anycast from every healthy control plane node. Each node checks its local API server and withdraws the route if it is unhealthy, so failover happens at the network level. etcd members go in separate physical failure domains to keep quorum.

He runs BGP routing (BIRD) on the host rather than in a pod, for a reason that is obvious once said: Kubernetes needs networking to start pods, so basic networking must not depend on pods.

## Make the packet path boring

Default overlay and NAT designs work, but during an incident you end up staring at translated addresses instead of real pod-to-pod flows. In his routable design, each node peers with two top-of-rack switches over BGP and advertises its pod CIDR into the data center fabric. No overlay, no NAT, and iproute, traceroute and tcpdump show what actually happens.

ECMP uses both uplinks at once, so redundancy also means active-active capacity, and BFD pulls a failed path quickly instead of waiting on long BGP timers.

## Treat GPUs as explicit, scheduled capacity

GPU nodes need the right NVIDIA driver, container runtime integration, device plugin, labels, monitoring and a safe upgrade process; many teams use the NVIDIA GPU operator for this. Kubernetes never assigns a GPU on its own: the device plugin exposes it and the pod has to request it.

From there it is scheduling discipline. Requests declare CPU, memory and GPU. Node selectors or affinity target the GPU pool. Anti-affinity and topology spread keep replicas out of a single failure domain. Taints and tolerations stop ordinary workloads from squatting on expensive GPU servers. Deployments suit simple serving, while training, fine-tuning and batch work fit jobs or queues with controlled concurrency.

## Roll out by traffic weight

A new model version, prompt template, runtime image or config can change latency, cost and error rate. Gateway API HTTPRoutes let you split traffic, for example 90 percent stable and 10 percent new, then shift it forward if metrics hold or back if they do not.

Observability has to cover more than application errors: GPU utilization and memory, scheduling problems, network behaviour, API server latency and etcd health.

## Who should watch

Platform and infrastructure engineers running or about to run model serving on their own Kubernetes, particularly on-prem or in tightly controlled environments. It is short and dense; cloud-managed-cluster users can skip the BGP section but should keep the scheduling checklist.

## Related Conf42 talks

- [Building Developer-Centric ML Inference Platforms: From Kubernetes Orchestration to Production Excellence](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes) from Conf42 Platform Engineering 2025 picks up the inference orchestration story.
- [Bye Kubernetes Ingress, Long Life to Gateway API](https://www.conf42.com/DevOps_2024_Yuri_Bacciarini_kubernetes_ingress_gateway_api) from Conf42 DevOps 2024 is a good primer on the rollout tool he relies on.
- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) from Conf42 Kube Native 2025 tackles sharing that scarce GPU capacity.

[Watch Sergey Speranskiy's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sergey_Speranskiy_kubernetes_infrastructure_llms)

[Watch the talk on YouTube](https://youtu.be/2P4GUP3lS7Q).

## Watch the talk

[Building Reliable Infrastructure for LLM Workloads on Kubernetes](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sergey_Speranskiy_kubernetes_infrastructure_llms) at Conf42 Large Language Models (LLMs) 2026.
