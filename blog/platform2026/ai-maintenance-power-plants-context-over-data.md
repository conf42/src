# Power plant AI maintenance runs on context, not more sensor data

Conf42 Blog, 2026-11-02, updated 2026-11-09. https://www.conf42.com/blog/platform2026/ai-maintenance-power-plants-context-over-data

In short: Mohan Kumar Dalai of GE Vernova at Conf42 Platform Engineering 2026 on AI maintenance platforms that read context, cut alarm floods and keep humans in charge.

A power plant already has more data than it can read. At Conf42 Platform Engineering 2026, Mohan Kumar Dalai, staff software engineer at GE Vernova, argued that the job of AI in maintenance is to turn that pile into decisions an engineer will trust, and that the hard part is context and adoption, not the model.

It's a short, clear talk aimed at people who build platforms for operational technology rather than at data scientists. If your users wear hard hats, it's worth the time.

## Failures are slow; schedules are blind

Mohan starts with the two maintenance styles every plant knows. Reactive maintenance fixes things after they break. Time-based maintenance inspects or replaces on a calendar. Both have value, and both miss the point that most failures develop gradually. A turbine bearing doesn't die overnight, and a transformer fault starts inside long before anyone can see it.

So the question shifts from when the asset was last serviced to what the equipment is saying right now. That is condition-based thinking, and it's the foundation the rest of the talk builds on.

## A vibration spike is a question, not an answer

The sharpest section is about context. A rise in vibration on a rotating asset could mean degradation. It could also mean a recent startup, a load change, a hot afternoon or a drifting sensor. Without context, all of those look the same on a chart.

Mohan's case for AI here is specific: models are useful because they evaluate relationships between operating conditions instead of single data points. Instead of fixed thresholds, the system learns what normal looks like for each machine at each load. The payoff he stressed is alert quality. Fewer false alarms means operators keep listening, which anyone who has muted a noisy Slack channel will recognise.

He walks the same idea across three asset families:

- **Rotating machinery** (turbines, generators, pumps, bearings): earlier detection of lubrication problems, misalignment, imbalance and wear.
- **Boilers and heat systems**: spotting drift in relationships, like fuel use rising without more output, that never crosses a classic alarm threshold.
- **Transformers**: dissolved gas analysis, where trend direction and persistence matter more than any single reading, and explainability is non-negotiable.

## AI should organise alarms, not hide them

Control rooms rarely lack information; they drown in it. During abnormal events operators can get hundreds of notifications. Mohan's line is that AI's job is to group related alarms, point at likely causes and add context, while decision authority stays with the human operator.

That ties into the platform half of the talk. He lists the reasons AI maintenance projects stall, and none of them is the algorithm: data quality, integration with legacy systems, explainability requirements and cybersecurity. His five-step path is plain on purpose: define the problem, build reliable data foundations, develop and validate models, deploy under governance with continuous feedback, and judge the result by operational outcomes rather than by how many graphs it produces.

## Trust is the real deployment target

The adoption advice reads like it came from someone who has watched a good model get ignored. Show the signal, the reasoning and the evidence. Fit existing workflows instead of adding steps. Let users challenge a recommendation. Mohan frames the goal as partnership, not dependency, and closes with the claim that AI strengthens maintenance engineering rather than replacing it.

The forward-looking part covers digital twins, inspection robots for hazardous areas and fleet analytics, where a lesson learned at one plant reaches dozens of others.

## Who should watch

Platform and reliability engineers working with industrial or energy customers, and anyone building an internal AI service that operators must trust before they act on it. If you want model architectures, benchmarks or code, this isn't that talk; it's an overview of the operating model around the models.

## Related Conf42 talks

- [AI Driven Vectorized Motor Health Monitoring for Reliable Industrial Operations](https://www.conf42.com/DevOps_2026_Avinash_Sista_maintenance_industrial_ai) by Avinash Sista at Conf42 DevOps 2026.
- [Generative AI for Predictive Maintenance in Kubernetes-Native Manufacturing Ops](https://www.conf42.com/Kube_Native_2025_Abhijit_Joshi_maintenance_predictive_manufacturing) by Abhijit Joshi at Conf42 Kube Native 2025.
- [Building Scalable AI/ML Platforms for Industrial IoT](https://www.conf42.com/Platform_Engineering_2025_Muruga_Angamuthu_industrial_iot_maintenance) by Muruga Angamuthu at Conf42 Platform Engineering 2025.

[Watch Mohan Kumar Dalai's talk](https://www.conf42.com/Platform_Engineering_2026_Mohan_Kumar_Dalai_maintenance_power_plant) or find it in the [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026) lineup.

[Watch the talk on YouTube](https://youtu.be/lX1GI6cLX2k).

## Watch the talk

[AI Maintenance Platforms for Reliable Power Plant Operations](https://www.conf42.com/Platform_Engineering_2026_Mohan_Kumar_Dalai_maintenance_power_plant) at Conf42 Platform Engineering 2026.
