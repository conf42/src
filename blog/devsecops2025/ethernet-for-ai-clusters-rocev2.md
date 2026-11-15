# Your GPUs are only as fast as the Ethernet between them

Conf42 Blog, 2025-11-25, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/ethernet-for-ai-clusters-rocev2

In short: Nazim Khan of Cisco at Conf42 DevSecOps 2025 on building lossless Ethernet fabrics for AI clusters with RoCEv2, ECN, PFC and Ultra Ethernet, plus how to secure them.

The expensive part of an AI cluster is the GPU, and the most common way to waste it is a network that makes it wait. At Conf42 DevSecOps 2025, [Nazim Khan](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra), technical solutions architect on Cisco's data center and AI infrastructure team, explained how plain Ethernet becomes a lossless, GPU-to-GPU fabric with RoCEv2 and congestion control, and where security fits as the clusters grow.

Khan brings 23 years in networking and a dual CCIE, and it shows: this is a clear, well-paced primer, with the occasional joke. His line about buying the fastest GPU and putting it on a congested network is that you are driving a Ferrari in a traffic jam.

## The network is part of the computer

He starts with the silicon. The CPU orchestrates, the GPU does the heavy parallel maths, and the DPU takes over what he calls the infrastructure tax: at 400G and 800G, packet processing, encryption and inspection eat CPU cycles, so the DPU offloads them and leaves the CPU and GPU to their workloads.

An AI cluster, in his framing, is a group of GPUs acting as one supercomputer, which makes the network part of the compute fabric rather than plumbing. During training every GPU computes a gradient and they all have to exchange results together, using topology-aware patterns such as rings and trees. If that collective communication lags, training time explodes.

Training and inference need different networks. Training wants high node-to-node bandwidth and is measured in time to train; inference cares about latency and reliability and can run on smaller, more distributed clusters that look much like a regular data center network.

## Lossless Ethernet is the trick

Training uses RDMA, remote direct memory access, so the NIC writes straight into GPU memory and skips the CPU. His joke: with human RDMA you could sit in the room and have his networking knowledge copied into your head by the end of the session.

RDMA assumes no packet loss. If a packet drops, the collective operation stalls or restarts. So AI designs split into a front-end network (storage, management, user access, ordinary data center traffic) and a dedicated back-end network for GPU-to-GPU traffic only.

For that back end you choose InfiniBand or Ethernet. InfiniBand runs RDMA natively and has better latency, but it's proprietary and expensive. Ethernet is standard, widely understood and cheaper, but best effort. RoCE closes the gap by carrying RDMA inside Ethernet frames. RoCE v1 was limited to layer 2; RoCEv2 adds UDP/IP headers so RDMA can route across layer 3, which is what lets clusters span racks, rows and whole halls.

Two mechanisms keep it lossless. ECN, explicit congestion notification, marks packets instead of dropping them when queues build, so endpoints slow down. PFC, priority flow control, pauses specific traffic classes under congestion. Khan stresses that tuning PFC headroom, pause thresholds and queues is critical to a successful RoCEv2 deployment. Get it wrong and you've built a very fast way to stall.

Looking ahead, the Ultra Ethernet Consortium is standardising better congestion control and lower latency for AI back ends, aiming to replace proprietary approaches.

## Security for the fabric

The security section is shorter and higher level. Khan lists the AI-specific risks (data poisoning, model extraction, privacy violations, insider threats) and the core strategies: encryption in transit and at rest, secure design, continuous monitoring for anomalies in traffic flows and user behaviour, and access control. DPUs enforce encryption and isolation at the server edge so the GPU can stay fully on training.

## Who should watch

Platform, SRE and security engineers who are suddenly responsible for GPU clusters and want the networking vocabulary fast. Network veterans will know the material; everyone else gets a clean mental model in one sitting. Don't expect a deep security architecture; the talk is mainly about the fabric.

## Related Conf42 talks

- [How Ultra Ethernet and UALink Accelerate Token-to-Token Performance](https://www.conf42.com/Prompt_Engineering_2025_Rajesh_Arsid_ethernet_performance_scaling) picks up where Khan's Ultra Ethernet section ends.
- [Instant KAI Sandboxes with vCluster: Multi-Tenant GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) covers the scheduling side of shared GPU infrastructure.
- [AI in the Machine Room](https://www.conf42.com/DevOps_2025_Ashok_Jonnalagadda_ai_datacenter_operations) looks at running the data center itself.

[Watch Nazim Khan's talk](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra)

[Watch the talk on YouTube](https://youtu.be/J09-1CSmOns).

## Watch the talk

[AI Infrastructure over Ethernet: Secure, Scalable, High-Performance Design](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra) at Conf42 DevSecOps 2025.
