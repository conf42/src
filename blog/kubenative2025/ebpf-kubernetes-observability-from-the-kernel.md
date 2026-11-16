# eBPF gives Kubernetes observability from inside the kernel

Conf42 Blog, 2025-10-10, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/ebpf-kubernetes-observability-from-the-kernel

In short: Alejandro Mercado, DevOps Lead at Michael Page, explains at Conf42 Kube Native 2025 why eBPF sits under Kubernetes networking, security and observability.

Kubernetes hides the Linux kernel from you on purpose, which is great right up until the problem lives in the kernel. At Conf42 Kube Native 2025, Alejandro Mercado, DevOps Lead at Michael Page, made the case that eBPF is how you get that visibility back: small sandboxed programs attached to kernel events, reporting what really happens to your pods.

This is an introduction, and a good one. If you've heard "eBPF" in every other CNCF talk and nodded along, this is the half hour that explains why.

## Observability is a data problem first

Mercado opens with a line he picked up at another conference: observability is a data problem. Getting the data, cleaning it and acting on it in real time is the hard part, and the closer you collect it to the source, the less you have to guess. For Kubernetes, the source is the kernel, because everything the orchestrator does rests on Linux primitives underneath.

## User space pays a toll on every syscall

The middle of the talk is a clear tour of kernel space versus user space. Applications can't touch hardware; they ask the kernel through system calls, and each call costs hundreds to thousands of CPU cycles because of the mode switch. So when an application needs a new kernel-level capability (a protocol, a load-balancing algorithm, traffic redirection for sidecars) there are two bad options: ship all the data up to user space and pay for it, or get the feature into the kernel itself.

Mercado's slides include a cartoon about the second path: the kernel is run by committee, a change can take a year, and by the time it ships your application may no longer need it. eBPF is the third option. You write a constrained program, usually in C (Rust is possible), load it into the kernel's virtual machine, and attach it to kprobes, tracepoints, network events or cgroups. A feature can arrive in days instead of a release cycle.

## Is it dangerous? Only as dangerous as you are

He takes the obvious question head on. eBPF runs in a privileged context, and loading programs needs admin rights by default, which keeps casual misuse out. You still could attach a program to every kernel function or drop all network traffic, he notes, but the sandbox and verifier make the kernel harder to crash by accident, not easier. The responsibility sits with whoever writes the program.

## Where you are already using it

The tools list is the useful bit for anyone mapping their own stack: Cilium for networking and its service mesh, Kuma, Falco, Tetragon and Tracee for runtime security, Pixie for application visibility, Weave Scope tracking TCP connections between containers. He also walks through concrete use cases: per-pod and per-container network statistics via cgroup-attached programs, Landlock LSM letting unprivileged apps sandbox themselves, and auditing `kubectl exec` sessions down to the exact commands typed.

His closing pitch pairs eBPF with OpenTelemetry. OpenTelemetry sees the application layers, eBPF sees the low layers, and correlating the two gives you both sides of the same incident.

## Who should watch

Platform and SRE folks who run Cilium or Falco without quite knowing what's under them, and anyone deciding whether eBPF-based tooling belongs in their cluster. Kernel hackers already writing BPF programs can skip it. Mercado ends with a reading list: the BCC tools, Brendan Gregg's talks, the Cilium project and the eBPF Foundation.

## Related talks

- Pranshu Srivastava goes deeper on the networking side in [The Power of Cilium For eBPF](https://www.conf42.com/Golang_2025_Pranshu_Srivastava_cilium_ebpf_networking).
- Shahar Azulay's [True Kubernetes Observability with eBPF](https://www.conf42.com/Cloud_Native_2023_Shahar_Azulay_kubernetes_observability_ebpf) applies the same idea to tracing applications without code changes.
- For the security tools Mercado lists, Thomas Labarussias shows [Use Falco and eBPF to protect your applications](https://www.conf42.com/Observability_2023_Thomas_Labarussias_falco_ebpf_protect_applications).

[Watch Alejandro Mercado's talk](https://www.conf42.com/Kube_Native_2025_Alejandro_Mercado_observability_kubernetes_ebpf)

[Watch the talk on YouTube](https://youtu.be/zdB4sQ21x1w).

## Watch the talk

[Observability in Kubernetes: Unlocking the Power of eBPF](https://www.conf42.com/Kube_Native_2025_Alejandro_Mercado_observability_kubernetes_ebpf) at Conf42 Kube Native 2025.
