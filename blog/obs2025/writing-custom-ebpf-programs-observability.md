# A first eBPF program for observability, in C and in Python

Conf42 Blog, 2025-05-22, updated 2026-11-09. https://www.conf42.com/blog/obs2025/writing-custom-ebpf-programs-observability

In short: Sooter Saalu of Draft.dev at Conf42 Observability 2025 introduces custom eBPF programs with two demos, packet counting in C and file tracing with BCC.

eBPF lets you run your own sandboxed code inside the Linux kernel without patching the kernel or loading a risky module, which is exactly why every observability vendor now ships something built on it. At Conf42 Observability 2025, Sooter Saalu, technical writer at Draft.dev, gave a compact introduction to writing custom eBPF programs, with two demos that show the round trip from kernel hook to a number you can graph.

## How a program gets into the kernel

Sooter starts with the pipeline every eBPF program goes through. You write the program, usually in C, compile it to bytecode, and hand it to the loader. Before it runs, the verifier checks it: no unbounded loops, no out-of-bounds memory access, nothing that could crash or compromise the kernel. Once accepted, it is compiled to machine code and attached to a hook, an event or a system call.

That path explains the three benefits he lists for observability: kernel-level visibility, often before any user-space application sees the event; no code changes to the applications you are watching; and low overhead, because what runs is native machine code next to the operations it observes.

## Demo one: counting packets in C

The first demo runs on a small AWS instance. A C program parses packet information from incoming traffic and writes it into BPF maps, one for packet counters and one for packet events, recording things like packet size. After compiling and loading it onto a network interface, Sooter sends traffic and shows the maps filling up.

The key concept is the map itself. It lives in kernel space but is readable from user space, so a user-space process can export its contents to Prometheus and Grafana. Kernel collects, user space ships.

## Demo two: tracing file access with BCC

The second demo trades C for Python using BCC. The Python script embeds the eBPF logic, and BCC compiles, loads and attaches it at runtime, with no manual load step. The target is an Nginx web server with a few HTML files; a load test sends a hundred requests across the pages and the program reports each file access as it happens.

What you do with those events is up to you: custom metrics, logs, or a direct feed into your analysis tools. Sooter's point is that eBPF gives you the access, and the logic is yours.

He is honest about the trade-off. Higher-level options, such as the Python, Go and Rust libraries, BCC and the Cilium libraries, make programs much easier to write but cost something in performance: slower execution and a larger footprint than native C.

## You probably do not have to write it all yourself

The last section maps the ecosystem built on eBPF: Pixie for Kubernetes observability without manual instrumentation, Parca and Pyroscope for continuous profiling, DeepFlow for automated tracing, Cilium for Kubernetes networking, plus eBPF-based tooling from OpenTelemetry, Prometheus and Grafana. There are also tools for managing and loading programs. Sooter points to write-ups of how companies such as Netflix and Apple use eBPF, and the demo code is on GitHub.

## Who should watch

This is an intro, and a good first talk on eBPF if you know what a syscall is but have never written a kernel program. It is short and demo-driven. If you already run Cilium or Pixie in production, skip to the related talks below for more depth.

## Related Conf42 talks

- [Anais Dotis-Georgiou on how kernel programming escaped the kernel](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) at Conf42 Observability 2026.
- [Yonatan Goldschmidt on low-overhead Python application profiling with eBPF](https://www.conf42.com/Python_2022_Yonatan_Goldschmidt_low_overhead_application_profiling_using_ebpf) at Conf42 Python 2022.
- [Pranshu Srivastava on the power of Cilium for eBPF](https://www.conf42.com/Golang_2025_Pranshu_Srivastava_cilium_ebpf_networking) at Conf42 Golang 2025.

[Watch Sooter Saalu's talk](https://www.conf42.com/Observability_2025_Sooter_Saalu_writing_programs_ebpf)

[Watch the talk on YouTube](https://youtu.be/2BphcNlG4XY).

## Watch the talk

[Writing Custom eBPF Programs for Observability: What You Need to Know](https://www.conf42.com/Observability_2025_Sooter_Saalu_writing_programs_ebpf) at Conf42 Observability 2025.
