# UALink scales GPUs up, Ultra Ethernet scales them out

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/ualink-ultra-ethernet-scale-up-scale-out

In short: Rajesh Arsid of Synopsys at Conf42 Prompt Engineering 2025 with a short primer on UALink and Ultra Ethernet, the interconnects behind fast token exchange.

Every clever prompt ends up as tokens moving between GPUs, and the wires decide how fast. At Conf42 Prompt Engineering 2025, Rajesh Arsid, ASIC Physical Design Principal Engineer at Synopsys, gave a compact primer on the two open interconnect standards aimed at AI clusters: UALink for scaling accelerators up inside a pod, and Ultra Ethernet for scaling clusters out.

Set expectations before you click: this is a brief talk, a few slides long, and it is about hardware. Prompt engineering appears in the title and the framing, not in the content. As a two-term vocabulary lesson for software people who keep hearing these names, it does the job quickly.

## Compute grew faster than the plumbing

Rajesh opens with the bottleneck. Compute demand is growing exponentially, and despite parallelisation, training times have stretched from weeks to months. His slide shows model parameter counts doubling every three to four months. The strain lands on every dimension at once: network bandwidth and latency, memory bandwidth and capacity, and compute. He points to the memory and interconnect standards (DDR, HBM, PCIe and others) racing to keep up.

He ties this back to the ML lifecycle: prepare data, build, train, test, fine-tune, repeat. Through that loop, data is split and fed to many GPUs, often across many machines, so GPU-to-GPU performance shapes the whole timeline.

## Scale up: make many GPUs look like one

UALink is an open interconnect for scaling up accelerators. Picture a pod of racks, each with GPUs, wired together so they behave like one giant GPU. The goal is memory sharing and synchronisation between accelerators, with direct load, store and atomic operations across them. Rajesh says UALink can connect from hundreds up to thousands of GPUs.

For inference, this is the layer that matters when one model is split across several accelerators: the faster they share memory, the faster tokens pass between them.

## Scale out: connect the pods

Ultra Ethernet, developed by the Ultra Ethernet Consortium, is the open, high-performance networking answer for AI and HPC at the next level up: linking clusters to each other. Rajesh describes it as high bandwidth, multipath, open and highly configurable, with a new transport layer that brings better congestion control and stronger RDMA. The scale he cites is millions of GPUs.

The split is the takeaway. UALink is the inside-the-pod fabric, Ultra Ethernet is the between-pods network, and both are open standards rather than a single vendor's fabric.

## Why a prompt engineer might care

Rajesh's conclusion links both to token-to-token performance. UALink's memory synchronisation suits the rapid token passing inside a sharded model; Ultra Ethernet's low latency and high throughput handle token exchange at cluster scale. If you own inference latency budgets, the interconnect is one more term in the equation, and it helps to know which layer a vendor is talking about.

## Who should watch

Software and platform engineers who want a quick orientation on AI cluster networking before a capacity planning meeting or a hardware vendor pitch. If you design interconnects for a living, it is too short to teach you anything new; if you came for prompt techniques, look elsewhere in the event.

## Related Conf42 talks

- [Murali Krishna Reddy Mandalapu on interconnect bottlenecks in GPU-accelerated HPC clusters](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Murali_Krishna_Reddy_Mandalapu_overcoming_interconnect_bottlen) at Conf42 SRE 2025, a longer look at the same problem.
- [Nazim Khan on AI infrastructure over Ethernet](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra), covering secure, scalable design.
- [Kosseila Haddalene on running vLLM inference on Kubernetes across clouds](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu), where the interconnect meets the serving stack.

[Watch Rajesh Arsid's talk](https://www.conf42.com/Prompt_Engineering_2025_Rajesh_Arsid_ethernet_performance_scaling), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/XVwTw5oj94g).

## Watch the talk

[Scaling Prompt Engineering: How Ultra Ethernet and UALink Accelerate Token-to-Token Performance](https://www.conf42.com/Prompt_Engineering_2025_Rajesh_Arsid_ethernet_performance_scaling) at Conf42 Prompt Engineering 2025.
