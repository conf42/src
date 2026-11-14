# Retina or Cilium? eBPF network observability, benchmarked on EKS

Conf42 Blog, 2026-04-12. https://www.conf42.com/blog/cloud2026/ebpf-retina-vs-cilium-network-observability

In short: Uudit Misra of Salesforce at Conf42 Cloud Native 2026 on why dashboards stay green during network failures, and Retina vs Cilium on a real EKS cluster.

Your dashboards are green, error rate is near zero, and users are getting 500s, because a network policy is dropping packets between two services without telling anyone. At Conf42 Cloud Native 2026, [Uudit Misra](https://www.conf42.com/Cloud_Native_2026_Uudit_Misra_distributed_systems_reliability), who works on the Kubernetes platform team at Salesforce, explained why that happens at the network layer and compared two open-source eBPF tools, Retina and Cilium, on a real AWS EKS cluster.

## Three failures your monitoring can't see

Misra lists three failure modes he has seen in production. Silent drops, where a policy blocks traffic and leaves no log, trace or alert. DNS timeouts in the few seconds while a pod starts up and lookups fail. And wrong backends, where a label change somewhere routes traffic to the wrong place. They share a cause: monitoring only watches what you told it to watch in advance.

His analogy is the car. Monitoring is the check-engine light someone wired to a threshold. Observability is the mechanic who can look under the hood for things nobody predicted. At the network layer that means flow-level records: source pod, destination pod, verdict, and the exact drop reason.

## Why iptables can't get you there

Traditional Kubernetes networking relies on iptables, a long linear list every packet walks. Misra gives four problems. It slows down as rules grow. It is shallow: layer 3 and 4 only, with no HTTP paths, DNS queries or gRPC service names. It has no identity, just IPs instead of pod names. And its drops are silent. None of the questions you ask mid-incident (why did traffic between these pods stop? which DNS query is timing out?) can be answered from iptables alone.

eBPF agents fix that from the kernel. They run as a DaemonSet, one per node, attach small programs to kernel hook points, and export flows to Hubble Relay, metrics to Prometheus and dashboards to Grafana, without sidecars, code changes or restarts.

## Retina sees the packet, Cilium knows who sent it

Retina, open-sourced by Microsoft in 2024, is observability only. It doesn't replace your CNI or enforce policy. It hooks TC for ingress and egress packets, kprobes for TCP, a socket filter for DNS and XDP for drops, and emits data in Hubble format, so an existing Hubble CLI works with it straight away. The catch is that it maps IPs to pods in user space, after the fact. In his screenshots, Retina flows show the destination as `world` with a raw IP instead of a pod name.

Cilium gives each pod a cryptographic identity derived from its labels when the pod starts, and the eBPF programs in the kernel carry that identity, so both ends of every flow are resolved. It also parses layer 7, giving you HTTP method, path and status, plus gRPC service names.

## The benchmark: identity costs CPU

Both tools ran one after the other on the same EKS cluster with around 500 QPS of sustained pod-to-pod traffic. Retina used 47% less memory per node and its CPU stayed flat. Cilium showed a 31% CPU spike under the same load, because it does per-flow identity work on every packet. The numbers come from `kubectl top`, not a simulator.

## A three-step blueprint

His recommendation is incremental. Install Retina with two Helm commands and have Prometheus scrape it, which gives you TCP flows and DNS in about five minutes. During an incident, run `hubble observe` filtered to your pod, and with a dropped-verdict filter to catch silent blocks. When you need pod identity on both sides or L7 detail, add Cilium in chaining mode. On EKS he set `cni.chainingMode=aws-cni`, so the VPC CNI keeps doing IP address management and Cilium adds identity-aware visibility on top.

## Who should watch

Platform engineers and on-call SREs running Kubernetes who have lost an evening to a packet that vanished without a log line. It's also a clear, well-measured comparison if you are choosing between the two tools.

## Related Conf42 talks

- [The Power of Cilium For eBPF](https://www.conf42.com/Golang_2025_Pranshu_Srivastava_cilium_ebpf_networking) by Pranshu Srivastava at Conf42 Golang 2025.
- [How Kernel Programming Escaped the Kernel](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) by Anais Dotis at Conf42 Observability 2026.
- [Zero-instrumentation observability based on eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) by Nikolay Sivko at Conf42 Site Reliability Engineering (SRE) 2024.

[Watch Uudit Misra's talk](https://www.conf42.com/Cloud_Native_2026_Uudit_Misra_distributed_systems_reliability) or the [YouTube recording](https://youtu.be/OUm8z83DKrE).

## Watch the talk

[Beyond Dashboards: Deep-Dive Network Observability with eBPF](https://www.conf42.com/Cloud_Native_2026_Uudit_Misra_distributed_systems_reliability) at Conf42 Cloud Native 2026.
