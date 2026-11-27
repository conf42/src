# At trillion-parameter scale, cost is a training metric

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/mlops-for-trillion-parameter-llm-training

In short: Anjan Dash (Meta) at Conf42 MLOps 2025 on operating trillion-parameter LLM training runs, from parallelism and checkpoints to early warnings and cost.

When a training run lasts weeks on thousands of synchronised GPUs, every idle hour is money you will not get back, and you only learn whether the model is any good at the end. At Conf42 MLOps 2025, Anjan Dash, a technical leader at Meta who works on ads ranking systems, walks through what it takes to operate trillion-parameter LLM training, and his conclusion is that MLOps here is the foundation that makes training possible at all.

It is an overview talk that covers the whole stack: infrastructure, orchestration, failure recovery, monitoring and cost. Good if you need the map before you go deep on any one piece.

## The scale problem in five lines

Anjan lists the challenges plainly. Training cycles are so long that feedback arrives weeks late. Thousands of GPUs must stay in sync or nothing trains. Hardware, power and specialist people all cost a lot. The models are data hungry, so the data pipeline has to keep up. And checkpoints of a trillion-parameter model are huge, so even saving a snapshot is an engineering problem.

The financial framing matters: weekly training cost, the cost of every failed hour while GPUs sit idle, waste when data or power is not arriving, and the total duration of the run. Each one is a lever MLOps can pull.

## Parallelism is a stack, not a choice

His infrastructure section covers distributed training clusters, high-bandwidth interconnects between GPUs and clusters, custom kernels that exploit hardware-specific acceleration, a data pipeline system to feed the cluster, GPU-aware orchestration, and monitoring.

He compares two frameworks. NVIDIA's Megatron brings tensor parallelism to split layers efficiently and sequence parallelism to chunk long input sequences across GPUs to manage memory footprint. Microsoft's DeepSpeed brings the ZeRO optimizer for memory, pipeline parallelism, and offloading to CPU and NVMe. Real trillion-parameter training, he notes, combines tensor, pipeline, data and sequence parallelism at once.

## Recovery has to be automatic

The failure-recovery section is the most operationally useful. Detection watches for hardware failures, gradient explosions and data corruption. Checkpoint management decides how often to save and how far back you can fall. Resource reallocation reconfigures the cluster around failed hardware. Training should resume on its own; a human fixing things by hand during a multi-week run is not a plan.

Monitoring runs at two levels. System metrics cover GPU utilisation, network bandwidth, disk IO and power. Training metrics cover loss, gradients, learning rate and parameter norms. Alerting needs anomaly detection, multiple channels (phone, Slack, email) and automated escalation if nobody answers.

## Watch the gradients before they bite

Anjan's early-warning list is the part to copy into a runbook: gradient spikes, shifts in activation distributions across layers, a widening gap between training and validation, and unexpected loss behaviour when the learning rate changes. Each is a signal that lets you intervene before a catastrophic failure wastes days of compute.

His takeaways close the loop: invest in distributed systems and the people who understand them, automate everything, monitor at multiple levels, and treat cost as a first-class metric tracked as seriously as model quality. The GPU bill, after all, does not care how elegant the loss curve looks.

## Who should watch

ML platform and infrastructure engineers moving from single-node or modest multi-node training toward large distributed runs, and engineering managers who need to explain where the money goes. Researchers already living inside Megatron or DeepSpeed configs will find it a summary rather than new detail.

## Related Conf42 talks

- [Murali Krishna Reddy Mandalapu (Renesas) on interconnect bottlenecks in GPU-accelerated HPC clusters](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Murali_Krishna_Reddy_Mandalapu_overcoming_interconnect_bottlen) at Conf42 SRE 2025.
- [Piotr Zaniewski (vCluster) on multi-tenant GPU sharing with KAI sandboxes](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) at Conf42 Kube Native 2025.
- [Nicolo Brandizzi (Fraunhofer IAIS) on turning 173 billion documents into LLM training data](https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents), the data side of the same pipeline.

[Watch Anjan Dash's talk](https://www.conf42.com/MLOps_2025_Anjan_Dash_mlops_trillion_parameter) for the full pipeline and monitoring breakdown.

[Watch the talk on YouTube](https://youtu.be/OlnfHi9EBSE).

## Watch the talk

[MLOps at Trillion-Parameter Scale: Operationalizing Large Language Model Training Pipelines](https://www.conf42.com/MLOps_2025_Anjan_Dash_mlops_trillion_parameter) at Conf42 MLOps 2025.
