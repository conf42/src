# Rust for edge AI, from no_std operators to Candle and Burn

Conf42 Blog, 2025-08-04, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-edge-ai-no-std-inference

In short: Anushree Nagvekar of AEye at Conf42 Rustlang 2025 on Rust for edge AI, with no_std neural operators, portable SIMD, ARM and RISC-V targets, and the crates to use.

On an edge device every byte and every CPU cycle counts, and the latency budget for perception is measured in milliseconds the cloud cannot reliably deliver. At Conf42 Rustlang 2025, Anushree Nagvekar, a software engineering manager at AEye, made the case for Rust as the language of edge AI and showed the implementation patterns that make it work on constrained hardware.

AEye builds lidar for autonomous vehicles, so the examples lean towards perception and safety-critical inference. The second half of the talk, on custom operators and target-specific builds, is where the useful detail lives.

## Why edge AI needs a different language

Anushree's framing: the holy grail for edge AI is latency under 50 ms, which means computing on the device rather than round-tripping to the cloud. On-device means tight memory, small CPUs and real-time deadlines.

Rust's fit, in her telling, is threefold: memory safety without a garbage collector, zero-cost abstractions for clean code with no performance tax, and fine-grained system control. She highlighted safe concurrency across multi-core ARM chips, portable SIMD for vectorized maths without hand-written assembly, and good integration with NPUs and DSPs, even in `no_std` environments.

## Two case studies, two kinds of edge

The first is autonomous vehicles: a tight obstacle-detection budget, high detection success and very high uptime requirements, where Rust's compile-time guarantees remove runtime errors that have long plagued C++ in these systems. The second is industrial IoT security: threat detection on modest hardware with long battery life, where predictable performance is what makes low-power devices viable.

The performance and memory figures she presented are production numbers in her account, without the benchmark detail, so read them as reported results.

## Writing neural operators that fit on a chip

The implementation patterns for custom neural network operators are the part to rewatch:

- **No heap allocations**, which gives `no_std` compatibility for the most constrained embedded targets and keeps latency deterministic.
- **Cache-friendly memory access patterns** to cut memory latency, often the real bottleneck on small devices.
- **Manual loop unrolling** to help the CPU pipeline and make execution times predictable.
- **Direct slice manipulation** written so bounds checks are optimized away in release builds, keeping Rust's safety without paying for checks in the hot loop.

## Compile for the chip you actually have

For ARM and RISC-V processors, Anushree showed using Cargo features and `cfg` attributes to enable instruction sets specific to the target CPU, so the compiler emits architecture-specific binaries that use what the hardware offers. One codebase, several tuned builds. She also mentioned memory-mapped hardware accelerators accessed through safe Rust, giving direct hardware control without dropping into C.

## The ecosystem to start with

Her crate list is short and practical:

- **Candle**, for inference with minimal dependencies.
- **Burn**, a deep learning framework with a strong type system and modular backends, for training.
- **SmartCore**, classic machine learning algorithms, `no_std` compatible.

Her closing advice: add them with Cargo and start experimenting on your own system.

## Who should watch

Embedded and robotics engineers bringing ML onto devices, and Rust developers who want concrete patterns for `no_std` numeric code. ML researchers who live in Python will get a good sense of what deployment on the edge actually demands.

## Related Conf42 talks

- [Optimizing Real-Time AI Inference at the Edge for Autonomous Vehicles](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge) by Murali Krishna Reddy Mandalapu: the same vehicle problem, from another stack.
- [Edge Computing and TinyML for Autonomous IoT](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai) by Pradeep Kumar Vattumilli: ML at the smallest scale.
- [Get maximum benefit from zero-cost abstractions](https://www.conf42.com/Rustlang_2022_Tim_McNamara_maximum_benefit_zerocost_abstractions) by Tim McNamara: the language feature this talk leans on hardest.

[Watch Anushree Nagvekar's talk](https://www.conf42.com/Rustlang_2025_Anushree_Nagvekar_edge_memory_safety)

[Watch the talk on YouTube](https://youtu.be/2DiY2pVybmo).

## Watch the talk

[Building the Edge AI Revolution with Rust: Zero-Cost Abstractions Meet Real-World Performance](https://www.conf42.com/Rustlang_2025_Anushree_Nagvekar_edge_memory_safety) at Conf42 Rustlang 2025.
