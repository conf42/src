# Multicore avionics fail certification on timing, not features

Conf42 Blog, 2025-11-03, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/do-178c-multicore-avionics-certification

In short: Charles Antony Raj of Collins Aerospace at Conf42 Robotics 2025 on certifying multicore flight software under DO-178C and CAST-32A for electric aircraft.

Two cores sharing an L2 cache can make a flight control task late in ways no single-core analysis predicts, and that is what slows multicore avionics programs down. At Conf42 Robotics 2025, Charles Antony Raj, Senior Manager for Systems and Software Engineering at Collins Aerospace, explained how electric aircraft teams get multicore processors through DO-178C certification without losing determinism.

Charles brings about two decades in aerospace, and the talk reads like a certification plan you could hand to a new program lead.

## Why electric aircraft want more cores

The case for multicore is threefold: computing power for sensor fusion, flight management and onboard AI in real time; integration of several avionics functions onto fewer boxes, which cuts weight and wiring; and power efficiency, leaving more energy for propulsion. On an electric aircraft every kilogram and watt has a job.

## Shared hardware is the real adversary

The catch is that cores share caches, memory buses and IO. Charles lists the interference channels: shared L2 or L3 cache evictions, simultaneous memory access creating wait states, contention on IO controllers and DMA, and latency across the interconnect fabric. Each one makes worst-case execution time, WCET, much harder to bound. His first pitfall follows directly: never assume single-core WCET numbers carry over.

## DO-178C says what, CAST-32A says how

DO-178C remains the foundation: design assurance levels A to E, verification, configuration management, traceability. CAST-32A adds the multicore-specific objectives around interference mitigation, timing analysis and resource usage. Charles also notes that EASA's AMC 20-193 supersedes CAST-32A for applicants in its jurisdiction, and the FAA's AC 20-193 from 2024 aligns with it.

The objectives boil down to: plan and characterize the hardware early, budget and partition resources, demonstrate WCET bounds under interference, handle multicore-specific faults, and deliver a multicore accomplishment summary to the authority.

## Partition in space and in time

The engineering answer is partitioning. Spatial partitioning gives each function its own memory region. Temporal partitioning time-slices execution so every critical task gets guaranteed CPU access. Careful core and cache allocation cuts interference between partitions, and stress testing proves the boundaries hold.

For robotic control the rules get specific: put sensor fusion from IMUs, cameras and lidar on dedicated cores, keep path planning and other heavy autonomy away from low-level control loops, and run safety monitors and watchdogs on separate cores or partitions. As Charles puts it, "Even microsecond delays can affect stability."

The tooling list is concrete too: a partitioning RTOS such as Green Hills INTEGRITY-178 tuMP, timing tools from vendors like Rapita and LDRA, structured test harnesses, and ETM or PTM hardware tracing.

## Somebody already got to DAL A

The case study is CMC Electronics' PU-3000, which Charles describes as one of the first platforms to reach civil multicore certification to DO-178C DAL A, running INTEGRITY-178 tuMP and producing evidence against CAST-32A objectives. The lesson he draws: it's achievable, provided you pick the platform early, start interference characterization in parallel with development, bring in hardware-in-the-loop testing early and talk to the certification authority from the start.

## Who should watch

Avionics and safety-critical embedded engineers, anyone building drones or autonomous vehicles on multicore SoCs, and managers who need to explain to their own management why the timing analysis takes so long. If you have never met a DAL, it's a dense but readable first tour.

## Related Conf42 talks

- [Rasmi Ranjan Nayak: Real-Time Embedded AI for Deterministic Robotics](https://www.conf42.com/DevOps_2026_Rasmi_Ranjan_Nayak_embedded_robotics_ai) tackles determinism on the robot side.
- [Sumaiyya Fatima: Scalable HIL Architecture](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) covers hardware-in-the-loop validation for software-defined vehicles.
- [Marco Verleun: How to prove the safety of your software](https://www.conf42.com/Python_2024_Marco_Verleun_prove_safety_software) looks at safety evidence from a developer's chair.

[Watch Charles Antony Raj's talk](https://www.conf42.com/Robotics_2025_Charles_Antony_Raj_avionics_certify_flight)

[Watch the talk on YouTube](https://youtu.be/N-dEvazVukg).

## Watch the talk

[DO-178C in Multicore Avionics: Certification Paths for Electric Aircraft](https://www.conf42.com/Robotics_2025_Charles_Antony_Raj_avionics_certify_flight) at Conf42 Robotics 2025.
