# Hardware-in-the-loop for software-defined cars needs observability built in

Conf42 Blog, 2026-09-08, updated 2026-11-09. https://www.conf42.com/blog/obs2026/hil-testing-with-observability-built-in

In short: Sumaiyya Fatima of General Motors at Conf42 Observability 2026 on a five-layer HIL platform with embedded diagnostics and closed-loop validation.

A pass/fail result tells a vehicle validation engineer almost nothing when the failing feature spans a dozen controllers. At Conf42 Observability 2026, Sumaiyya Fatima, Senior Software Engineer at General Motors, proposed treating hardware-in-the-loop (HIL) testing as shared infrastructure with observability designed in, so every test run records the signals, timings and diagnostics needed to explain a failure, not just report it.

It's an architecture talk rather than a tooling demo, and an unusual one for an observability conference: the system under observation is the test rig and the car's software, not a web service.

## One kick, many systems

Her example is a hands-free power liftgate. The customer kicks under the bumper and expects the tailgate to open. Behind that, the vehicle detects the motion, validates sensors, confirms a key fob is present, checks operating state and security conditions, passes messages across modules, and finally commands an actuator. When it doesn't open, the question is which of those broke: sensor, network, software service, configuration, or a diagnostic state blocking the action.

Fatima names three pressures on validation teams in software-defined vehicles: cross-domain dependencies like the liftgate, runtime variability from CI/CD and over-the-air updates changing behaviour after release, and scale, where more scripts and benches stop keeping up. She was careful to credit traditional HIL as a big reason embedded quality improved; it was built for single-controller architectures.

## Intermittent bugs need context, not a red cross

The motivating failure is the classic intermittent one: a ten-millisecond delay between two services that's harmless most of the time but causes a timeout under one startup condition. A traditional test reports that an expected output didn't arrive. What engineers need is what messages were exchanged, which services were active, the timing relationships and the diagnostics present at the moment.

## Five layers, observability at the centre

Her framework replaces per-program test benches with a shared validation platform, closer to how companies run cloud infrastructure than how they build one-off rigs. The five layers:

1. **Hardware abstraction.** Tests say send the lock command; the framework works out how that reaches whichever controller this program uses.
2. **Real-time simulation.** Deterministic recreation of rare conditions, such as low battery plus heavy network load at startup.
3. **Signal governance.** One standard name, scaling, owner and version per signal, ending the vehicle-speed-versus-speed-value arguments.
4. **Embedded diagnostics.** Every run records signal transitions, diagnostic trouble codes, network and service-to-service traffic, so the context exists before anyone asks.
5. **Automation orchestration.** The framework controls timing and collection, removing operator variability. Three engineers waiting five versus six seconds between steps can disagree about whether a timing bug is real.

None of the layers is new on its own, she noted. The integration is the contribution.

## Closed-loop validation asks how it passed

The part most transferable to other domains: tests that watch behaviour while running and react. An overnight software drop triggers regression tests; a service responds slower than baseline but still passes; the framework flags it, stores the telemetry and can launch extra scenarios. Her question for it: "How did the system behave while it passed?"

She closed with where this heads: using months of run data to prioritise risky test areas and spot latency trends drifting towards a failure threshold, with machine learning helping engineers find patterns. Her point was that none of that works without observability collecting the right data first.

## Who should watch

Automotive and embedded validation engineers, obviously. Backend engineers who own flaky integration suites will recognise the closed-loop and signal-governance ideas too. Expect concepts and examples, not code or benchmarks.

## Related Conf42 talks

- [Rajesh Reddy's introduction to ADAS and autonomous driving](https://www.conf42.com/DevOps_2024_Rajesh_Reddy_computing_software_vehicles) (Conf42 DevOps 2024).
- [Ravinder Katla on power moding in vehicle software](https://www.conf42.com/Machine_Learning_2025_Ravinder_Katla_sustainability_vehicle_software) (Conf42 Machine Learning 2025).
- [Victor Oriakhi on securing embedded IoT systems with DevOps](https://www.conf42.com/DevOps_2025_Victor_Oriakhi_iot_embedded_devops) (Conf42 DevOps 2025).

[Watch Sumaiyya Fatima's talk](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation)

[Watch the talk on YouTube](https://youtu.be/t99cbVdhtYM).

## Watch the talk

[Scalable HIL Architecture: Observability-Driven Validation in Software-Defined Vehicles](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) at Conf42 Observability 2026.
