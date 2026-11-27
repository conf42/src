# Treat GPU performance like a failing test, not a production surprise

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/gpu-performance-gates-in-ci-cd

In short: Mohit Gupta of Intel at Conf42 DevOps 2026 on putting GPU performance gates into CI/CD, and why mixed compute and memory workloads must be tested together.

Most teams find their GPU performance regressions the expensive way: after deployment, on shared hardware, with several other teams' jobs running next to theirs. At Conf42 DevOps 2026, Mohit Gupta, a staff GPU performance verification engineer at Intel, argued for moving that discovery into the pipeline, with GPU counters as build artefacts and performance gates that fail a build the same way a broken unit test does.

It is a short talk, around ten minutes, and it reads like a checklist from someone who verifies GPU behaviour for a living. If you run a platform that hands out GPUs to AI teams, it is a cheap way to sanity-check your own approach.

## Why post-deployment testing breaks down on GPUs

Mohit's framing is simple. GPUs are expensive, shared and performance sensitive, so a regression burns money directly, and the feedback loop from production is slow. He gives three reasons the validation belongs in CI/CD: cost (a regression wastes compute you already paid for), reliability (training and inference need predictable performance) and early detection (catching it in the pipeline keeps it out of the incident queue).

The shared part matters most. When one GPU pool serves many workloads and teams, a post-deployment test tells you something got slower, but not whose change did it.

## Classify the workload with counters, not opinions

The core of the method is a split most GPU engineers will recognise: compute-bound workloads, dominated by math and expected to show high ALU utilisation with few memory stalls, and memory-bound workloads, limited by data movement, cache misses, bandwidth saturation and access patterns.

What Mohit adds is discipline about how you decide which is which. The framework classifies workloads from measurable GPU counters: ALU utilisation, cache hit rates, memory stall cycles, bandwidth use and coalescing efficiency. That replaces "it feels memory-bound" with numbers you can store per build and compare across builds.

The benchmark suite has three families:

- dense linear algebra for compute-heavy AI work
- irregular memory access, such as graph and sparse operations
- hybrid workloads that mix both, to look like real production systems

In his compute-bound results, sustained ALU utilisation sat around 85% with strong L1 locality and few memory stalls. On the memory-bound side, bandwidth utilisation reached about 75%, with a clear gap in coalescing efficiency between structured and irregular access patterns. That gap is where he points the optimisation effort.

## The regression your isolated benchmark never sees

The finding he calls critical is the mixed-workload one. When compute-bound and memory-bound workloads run at the same time, cache contention and resource interference cause slowdowns that testing each workload alone completely misses.

This is the GPU version of the noisy-neighbour problem, and it is why a green isolated benchmark proves less than it looks. If your production GPUs are shared, your validation has to share them too. His takeaway list ranks this as the most important item: test mixed workloads, not just isolated benchmarks.

## Performance becomes code

The implementation side is familiar CI/CD practice applied to a new signal: define performance gates in the pipeline, run benchmarks automatically in a controlled environment, and capture GPU metrics as part of every build. In Mohit's words, performance becomes "version, repeatable and enforceable."

The same metrics then feed observability. GPU utilisation trends, bandwidth saturation, cache degradation alerts and the workload mix give SRE teams data for capacity and reliability planning, so the numbers collected for gating do double duty.

## Who should watch

Platform and MLOps engineers who own shared GPU clusters, and anyone who has been asked why training got slower this week and had no good answer. There is no code or tool demo, so if you want a specific product walkthrough this is not it; if you want a clear model for what to measure and gate on, it is a quick, focused one.

## Related Conf42 talks

- [Which Workload Owns This GPU Metric?](https://www.conf42.com/MLOps_2026_Nishant_Modak_gpu_workload_metric) by Nishant Modak takes on attribution, the natural next question once you are collecting GPU counters.
- [Running vLLM Inference on Kubernetes Across Clouds: A Production-Ready GPU Blueprint](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) by Kosseila Haddalene covers the kind of inference platform these gates would protect.
- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) by Piotr Zaniewski looks at the sharing that makes mixed-workload testing necessary.

[Watch Mohit Gupta's talk](https://www.conf42.com/DevOps_2026_Mohit_Gupta_gpu_ci_validation)

[Watch the talk on YouTube](https://youtu.be/ASEXeHpSypM).

## Watch the talk

[Building Robust GPU Performance Validation into CI/CD Pipelines for AI Infrastructure](https://www.conf42.com/DevOps_2026_Mohit_Gupta_gpu_ci_validation) at Conf42 DevOps 2026.
