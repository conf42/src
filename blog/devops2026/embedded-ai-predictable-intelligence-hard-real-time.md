# Embedded AI should aim for predictable, not maximum, intelligence

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/embedded-ai-predictable-intelligence-hard-real-time

In short: Rasmi Ranjan Nayak (ASML) at Conf42 DevOps 2026 presents a real-time embedded AI framework that keeps inference inside hard deadlines.

In a hard real-time system, an AI decision that arrives late is a wrong decision, however accurate it is. At Conf42 DevOps 2026, Rasmi Ranjan Nayak, a senior software engineer at ASML working on real-time embedded systems, argued that the supposed choice between deterministic behaviour and AI-driven intelligence is a false trade-off, and presented a framework for getting both on constrained hardware.

He sums up the design goal in one line: "The goal is not maximum intelligence. The goal is predictable intelligence." Everything else in the talk follows from that.

## The embedded AI paradox

Nayak's constraints will be familiar to anyone who has written firmware: limited compute because the device is built for one job, tight memory budgets because more RAM costs money and complexity, and millisecond latency requirements. Traditional AI optimises for accuracy and throughput; real-time systems optimise for predictability. That mismatch is the paradox.

He offers a handy distinction for the non-embedded audience. In a hard real-time system, a task due in two milliseconds must finish in two milliseconds. In a soft real-time system, a text message that arrives twenty minutes late is annoying but fine.

## Three layers on one control loop

The framework is hierarchical, with three layers running in a synchronised control loop:

- **Perception**: deterministic sensor acquisition and pre-processing, with sensor fusion making sure all data is time-aligned.
- **Cognition**: AI inference with models that are quantised and hardware-accelerated to keep latency bounded.
- **Execution**: every actuation is scheduled and verified.

The principle is that AI must adapt to the real-time constraints, never break them.

## C++ for the core, Python for the lab

The obvious question, why not Python everywhere, gets a straight answer. Python is excellent for rapid development, model training, pipelines and analytics, but not for hard real-time work. In his framework C++ forms the deterministic core: control loops, scheduling, sensor fusion, memory management and hardware access, with modern C++ standards making that safer to write. Optimised bindings connect the two worlds with minimal overhead.

## Every optimisation protects a deadline

The optimisation list is concrete. Quantised CNNs cut memory use by up to four times while preserving accuracy. Hardware acceleration on ARM NEON and GPUs brings up to ten times faster inference. Compile-time scheduling removes runtime uncertainty. Lock-free queues eliminate priority inversion and synchronisation bottlenecks.

He takes a moment to explain priority inversion: a low-priority task holds a resource that a high-priority task needs, and the usual fix is priority inheritance, temporarily lifting the low-priority task so it can finish and release the resource. As he puts it, every optimisation exists to protect the real-time guarantee.

Energy gets the same treatment: dynamic voltage scaling during low-demand periods, hibernating idle subsystems without hurting wake-up latency, and memory pooling to avoid fragmentation. A robot that hits every deadline but needs charging every hour has only solved half the problem.

## Where it runs

For manufacturing he cites vision-guided precision assembly at sub-millimetre accuracy with a 99.7% success rate, real-time inspection with 35% higher throughput and fewer false positives, and predictive maintenance cutting unplanned downtime by 60%. For defence, he describes autonomous navigation in GPS-denied environments via sensor fusion, and swarm coordination from distributed deterministic decisions, evaluated against dynamic obstacles and bandwidth limits. On implementation, he mentions sensor fusion loops at up to one kilohertz and inference under eight milliseconds.

Looking ahead, he points at federated learning, neuromorphic hardware, formal verification and smarter splitting of work between edge and cloud.

## Who should watch

Embedded and robotics engineers adding ML to control systems, and ML engineers about to deploy onto hardware that has never heard of garbage collection. The delivery is informal and wanders occasionally, but the architecture is clear. If your inference latency is reported as an average, this talk will make you want a worst case.

## Related Conf42 talks

- [Optimizing Real-Time AI Inference at the Edge](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge) by Murali Krishna Reddy Mandalapu (Renesas Electronics) looks at edge inference for vehicle safety.
- [At the Edge of Robotic Applications](https://www.conf42.com/Internet_of_Things_IoT_2024_Chiara_Civardi_Petr_Aubrecht_robotics_applications_edge) by Chiara Civardi and Petr Aubrecht (Payara Services) covers robotics at the edge.
- [Securing Embedded Systems in IoT: A Practical DevOps Approach](https://www.conf42.com/DevOps_2025_Victor_Oriakhi_iot_embedded_devops) by Victor Oriakhi (SONAE) brings DevOps practice to embedded devices.

[Watch Rasmi Ranjan Nayak's talk](https://www.conf42.com/DevOps_2026_Rasmi_Ranjan_Nayak_embedded_robotics_ai)

[Watch the talk on YouTube](https://youtu.be/cUCksn66J-k).

## Watch the talk

[Real-Time Embedded AI for Deterministic, Adaptive, and Sustainable Robotics](https://www.conf42.com/DevOps_2026_Rasmi_Ranjan_Nayak_embedded_robotics_ai) at Conf42 DevOps 2026.
