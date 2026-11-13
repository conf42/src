# How eBPF turned the frozen Linux kernel into something you script

Conf42 Blog, 2026-09-02, updated 2026-11-09. https://www.conf42.com/blog/obs2026/how-ebpf-escaped-the-kernel

In short: Anais Dotis-Georgiou of groundcover at Conf42 Observability 2026 tells eBPF's origin story, explains the verifier and JIT, and demos bpftrace.

For years, changing the Linux kernel meant either waiting two to four years for an upstream patch to reach your distro or shipping a kernel module that could panic the whole machine. At Conf42 Observability 2026, Anais Dotis-Georgiou, Developer Advocate at groundcover, explained how eBPF broke that deadlock by turning "trust this code" into "trust this proof", and then showed what you can do with it from a shell prompt.

She credits groundcover founding engineer Ori Shuchman as the author of the talk and its examples. groundcover is an observability platform built on eBPF, and it gets a mention, but this is an explainer, not a product demo. Think of it as a good first talk on eBPF that goes one level deeper than most.

## JavaScript for the kernel

The framing comparison, which she credits to Brendan Gregg: "eBPF is to the kernel what JavaScript is to HTML." A button in HTML is static until an event listener gives it behaviour. An eBPF program is an event listener on a kernel function, such as one that fires every time a TCP packet arrives and prints the process ID that received it.

## The history: networking pressure and a verifier

The origin story starts around 2011, when virtualisation turned servers into packet routers between fleets of VMs and the kernel became load-bearing for networking. Alexei Starovoitov, known as the father of eBPF, proposed running packet logic inside the kernel via a new virtual instruction set. Daniel Borkmann joined, and they extended the old BPF used by tcpdump. She recommends the eBPF documentary for the full story.

The trick is the verifier. Before loading, the kernel walks every path through the program, proving it terminates and only touches memory it was given. Fail the proof and it doesn't load. The first big proof of scale she cited was Facebook's Katran load balancer, open sourced. Early eBPF still meant writing bytecode and arguing with a verifier you didn't understand; tools like bcc and bpftrace, led by Brendan Gregg's work on observability at Netflix, made it approachable.

## Under the hood: helpers, trampolines, JIT

The technical section follows a probe on `do_nanosleep` that logs which process went to sleep. It compiles to BPF bytecode, where a call to helper number 14 (`bpf_get_current_pid_tgid`) is just a byte sequence. The verifier checks it. The kernel patches the target function at runtime with a call to a trampoline that jumps into your code and back. Then a JIT compiler translates each BPF instruction to native x86, so it runs as if it had been native from the start.

She also covered the timeline: classic BPF for packet capture, a full in-kernel virtual machine by 2014, loops, a million-instruction limit and CO-RE (compile once, run everywhere) by 2019, and more recently hooks into the scheduler itself.

## Three bpftrace demos

The demos are the part to steal:

1. A one-liner on the `openat` tracepoint printing every file opened on the machine, live.
2. Reading TLS traffic in plaintext by attaching a uprobe to `SSL_write` in libssl, after tcpdump showed only ciphertext.
3. Tracking writes to one specific file with three cooperating probes and two kernel maps, because the write syscall only knows a file descriptor, not a name.

She was fair about the trade-off: eBPF gives full coverage without code changes or restarts, but you lose application context. Reading a variable from your own code at write time is possible, just harder. And she positioned it as complementary to OpenTelemetry, not a replacement.

## Who should watch

Engineers who've heard eBPF mentioned in every observability pitch and want to know what's actually happening. If you already write eBPF in C, skip to the demos for teaching material.

## Related Conf42 talks

- [Nikolay Sivko on zero-instrumentation observability with eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) (Conf42 SRE 2024).
- [Thomas Labarussias on Falco and eBPF for runtime security](https://www.conf42.com/Observability_2023_Thomas_Labarussias_falco_ebpf_protect_applications) (Conf42 Observability 2023): the security use case in practice.
- [Yonatan Goldschmidt on low-overhead Python profiling with eBPF](https://www.conf42.com/Python_2022_Yonatan_Goldschmidt_low_overhead_application_profiling_using_ebpf) (Conf42 Python 2022).

[Watch Anais Dotis-Georgiou's talk](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking)

[Watch the talk on YouTube](https://youtu.be/0EwUeOLz3DY).

## Watch the talk

[How Kernel Programming Escaped the Kernel](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) at Conf42 Observability 2026.
