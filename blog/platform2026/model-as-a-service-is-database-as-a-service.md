# Model-as-a-service on Kubernetes is database-as-a-service again

Conf42 Blog, 2026-10-27, updated 2026-11-09. https://www.conf42.com/blog/platform2026/model-as-a-service-is-database-as-a-service

In short: Sergey Pronin (Solanica, OpenEverest) at Conf42 Platform Engineering 2026 on serving LLMs with KServe, vLLM, an AI gateway and per-key token limits.

If someone filed a ticket saying "we need to run LLMs on our cluster" with no further detail, Sergey Pronin built his talk for you. At Conf42 Platform Engineering 2026, the founder of Solanica and maintainer of OpenEverest, a CNCF project for running databases on Kubernetes, walked through adding model-as-a-service to OpenEverest, and his recurring punchline is that platform engineers have solved this before: it's database-as-a-service with different nouns.

The talk is framed as a bar joke. The platform engineer wants reproducibility, the LLM wants a big GPU nobody else is using, Kubernetes wants everything to be an object with a reconciler. The rest is how each gets served.

## Parameters times two

Why self-host at all? Sergey hears three reasons: data that can't leave (banks, healthcare, government, plenty of Europe), cost once token volume is steady and high, and GPUs that companies already bought and left idle.

Then the one piece of maths for the whole talk. A model is a folder of files full of weights, which he likens to a database's read-only data files. All of them must sit in GPU memory at two bytes each, so parameters times two is roughly gigabytes. A 4B model needs about 8 GB; a 70B Llama needs about 141 GB and won't fit even an 80 GB H100. And weights aren't the only tenant: the key-value cache holds every in-flight conversation, like a buffer pool. When it fills, requests queue. A model that fits isn't the same as a model that serves.

## From one command to an operator

Day one is easy: `vllm serve <model>` on a GPU box gives you an OpenAI-compatible endpoint. Day one on Kubernetes is a Deployment with `nvidia.com/gpu: 1`. Day two is the familiar mess: every restart re-downloads the weights, upgrades are manual, per-model flags live in someone's head, and the next team copies your YAML and changes three lines.

Sergey has seen this film. Ten years ago it was Postgres as a StatefulSet plus a pile of YAML, and the answer was operators. For models the operator is KServe: one LLM inference service object (which model, how many GPUs, how many replicas) and a reconciler that keeps a vLLM pod running on a GPU and rolls out changes.

## A gateway, a key per app, a token budget

One model for one team isn't a platform. With four models you'd have four URLs, so an Envoy AI Gateway sits in front and routes by the `model` field in the request body; clients only change their base URL. Sergey compares it to PgBouncer or ProxySQL.

Then the questions every DBA has asked. A shared API key is a shared superuser password, so every app gets its own key, rotated or revoked without touching anyone else. Limits are in tokens rather than requests, because one request can be ten tokens or ten thousand. In his example each key gets 3,000 tokens an hour; the batch job that burns through its budget gets a too-many-requests error while the chat app carries on. Counters live in Redis or Valkey. And because every token is tagged with a key, asking who used all the GPUs becomes one Prometheus query instead of a meeting.

## When it doesn't fit, split it; when it's busy, scale on the queue

On his 20 GB test cards, a 14B Qwen model dies with out-of-memory. No amount of YAML fixes physics. A model is also a stack of layers, so vLLM's pipeline parallelism spreads them across nodes, run by KServe with the Kubernetes LeaderWorkerSet project: one head pod serves the API, workers hold the rest, and every request visits each in turn, like sharding where every query hits every shard. The catch: the group lives and dies together, and two replicas means two whole groups.

For autoscaling, CPU is the wrong signal; models leave it idle. KServe's workload variant autoscaler scales on the KV-cache queue. And scaling up takes minutes rather than seconds, since a new pod pulls a multi-gigabyte image and then the weights, so keep weights on a cluster volume instead of fetching from Hugging Face, and keep a warm replica if you can afford it. Time to first token and requests waiting are the two health metrics he watches first.

## Who should watch

Platform engineers who just inherited the LLM ticket, especially anyone who has run databases on Kubernetes. Sergey is a maintainer, and the last part shows how OpenEverest wraps all of this as just another instance next to Postgres and ClickHouse, but the architecture is open source building blocks you can assemble yourself.

## Related Conf42 talks

- [Running vLLM Inference on Kubernetes Across Clouds: A Production-Ready GPU Blueprint](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) by Kosseila Haddalene (Cloudthrill)
- [Building Developer-Centric ML Inference Platforms: From Kubernetes Orchestration to Production Excellence](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes) by Gangadharan Venkataraman (Starbucks)
- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) by Piotr Zaniewski (vCluster)

[Watch Sergey's talk](https://www.conf42.com/Platform_Engineering_2026_Sergey_Pronin_kubernetes_llm_engineer)

[Watch the talk on YouTube](https://youtu.be/Ncaxm6AESt4).

## Watch the talk

[Kubernetes, LLM and Platform Engineer walk into a bar](https://www.conf42.com/Platform_Engineering_2026_Sergey_Pronin_kubernetes_llm_engineer) at Conf42 Platform Engineering 2026.
