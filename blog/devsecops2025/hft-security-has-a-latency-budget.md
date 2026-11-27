# In high-frequency trading, every security control has a latency bill

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/hft-security-has-a-latency-budget

In short: Janardhan Chejarla of Calypso Technology at Conf42 DevSecOps 2025 on securing event-driven trading systems without paying the sidecar latency tax.

A service mesh sidecar is a reasonable price for security in most microservices. In high-frequency trading it is the whole budget. At Conf42 DevSecOps 2025, [Janardhan Chejarla](https://www.conf42.com/DevSecOps_2025_Janardhan_Chejarla_trading_cloud_scale), senior technical consultant at Calypso Technology, made the case that trading platforms have to move security into the application and eventually into the hardware, because every check added on the hot path is measured in microseconds and money.

It's a short, high-level talk, closer to an architecture sketch than a demo. The value is in how cleanly it lays out the trade-offs.

## The latency tax

Chejarla starts with three goals that pull against each other: speed, scale (millions of orders per second) and security. Focus on one and you usually sacrifice another. He calls the cost of security checks the latency tax. His illustrative example: if a traditional firewall adds something like 50 microseconds, you are losing money.

His comparison chart makes the point sharper. A sidecar, the default security pattern in modern microservices, adds about 150 microseconds, which he calls too much for HFT. The alternative is to bake security into the application through an in-process library and keep the overhead to around five microseconds or less. The lesson isn't that sidecars are bad. It's that the security architecture should follow the latency tier of the component it protects.

## Bypassing the kernel means bypassing its protections

The fastest trading paths skip the operating system entirely. Chejarla describes kernel-bypass networking with DPDK or RDMA so the application talks directly to the network card. The catch, which he states plainly, is that this also skips security measures the OS would normally give you. So the controls have to move closer to the hardware.

For the order matching core he uses Aeron, which he describes as reliable, encrypted, near-instant messaging for machines, with Raft consensus so all trading nodes agree on the order of trades even if one fails. Slower, high-volume work such as market data analysis and trade settlement goes over Kafka, kept separate so record-keeping never slows the matching engine. Two tiers, two latency budgets, two security designs.

## Observe with eBPF, prove with event sourcing

You still need to see what happens, and standard agents cost too much. Chejarla's answer is eBPF: hook into the kernel to observe packets and system actions for compliance without adding latency to the trading path.

The second half of his compliance story is determinism. Every action in the system is captured as an immutable event, so you can replay a trading sequence after something goes wrong and reconstruct exactly what happened in a given window. That matters for post-mortems and for regulators, who increasingly ask for proof of best execution. His rule of thumb: if you can't replay it, you can't prove it. He folds this into what he calls compliance as code, and points to the London Stock Exchange as an example of speed and reliability improving together.

On resilience he offers one memorable principle for HFT: a system that cannot recover in milliseconds has already failed.

## The next step is the wire itself

The forward-looking part goes below software. Chejarla wants firewalls, risk checks and encryption implemented in FPGA gates as bump-in-the-wire devices, so bad packets are dropped before they ever reach a CPU, giving zero CPU overhead for those checks. He also wants these patterns to work on public clouds, not only private infrastructure, which is the harder half of the problem.

## Who should watch

Engineers on trading, market data or other microsecond-sensitive systems, and anyone who has been told to add a sidecar to a hot path and suspected it was the wrong tool. It's an overview, so expect pointers (Aeron, DPDK, eBPF, FPGA) rather than implementation detail.

## Related Conf42 talks

- [Observability in Modern Treasury Trading Platforms](https://www.conf42.com/Observability_2025_Ganesh_Marimuthu_trading_treasury_platforms) covers monitoring high-frequency systems at scale.
- [True Kubernetes Observability with eBPF](https://www.conf42.com/Cloud_Native_2023_Shahar_Azulay_kubernetes_observability_ebpf) goes deeper on the kernel-level observation Chejarla relies on.
- [Ambient Mesh: the sidecar-less Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) is another answer to the sidecar overhead question.

[Watch Janardhan Chejarla's talk](https://www.conf42.com/DevSecOps_2025_Janardhan_Chejarla_trading_cloud_scale)

[Watch the talk on YouTube](https://youtu.be/5Kt9ZEZfcHU?si=CehCngf5bXj5y7w5).

## Watch the talk

[Securing High-Frequency Trading at Scale: Event-Driven, Cloud-Native Order Management Systems](https://www.conf42.com/DevSecOps_2025_Janardhan_Chejarla_trading_cloud_scale) at Conf42 DevSecOps 2025.
