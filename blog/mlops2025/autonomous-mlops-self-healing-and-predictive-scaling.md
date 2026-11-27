# Autonomous MLOps is a four-phase climb, not a switch

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/autonomous-mlops-self-healing-and-predictive-scaling

In short: Mohan Singh (Amazon) at Conf42 MLOps 2025 on self-healing infrastructure, predictive scaling and AI-driven code modernization as the path to autonomous ops.

The 2 a.m. pipeline page is the thing every ML platform team wants to retire, and Mohan Singh, a software development manager at Amazon Web Services, spends his Conf42 MLOps 2025 talk on how you get there. His model is three pillars (self-healing infrastructure, intelligent scaling and AI-driven code evolution) climbed in four phases over 18 to 36 months, with each phase paying for itself before full autonomy arrives.

It is a short, high-level talk with a clear structure, more strategy map than implementation guide.

## From firefighting to systems that fix themselves

Mohan's history of MLOps has three stages. First it was manual: engineers on call in the middle of the night patching broken pipelines. Then automation made workflows faster and cut errors, but still needed constant supervision. The next stage is systems that learn, adapt and repair themselves. His analogy is the human immune system: detect, respond, adapt to new threats.

## Self-healing is a loop with four parts

A self-healing system, in his breakdown, has monitoring that uses ML to spot anomalies, diagnosis that pinpoints root causes across logs and signals, resolution through automated playbooks, and a feedback loop that makes the system smarter after every incident. He compares it to an aircraft autopilot that stabilises the plane rather than just alerting the pilot.

The implementation pieces are observability-driven AI that catches small deviations before they become incidents, cross-service intelligence that understands dependencies so failures are diagnosed in context, and automated patching that finds and fixes vulnerabilities without waiting for a human.

## Scale before the spike, not after

Traditional autoscaling reacts once demand has already arrived, which Mohan likens to braking after you have run the red light. Predictive resource management flips that: forecast demand hours or days out and provision ahead, then scale back down when the load passes.

His five-step loop is worth noting: collect telemetry beyond CPU and memory (request patterns and business metrics), analyse it with time-series models to find cycles and seasonality, forecast demand from minutes to days ahead, turn forecasts into allocation plans, then automate execution through infrastructure as code with feedback to correct in real time.

## Code that maintains itself

The third pillar treats the codebase as a living system. Mohan describes three approaches powered by LLMs, code analysis and reinforcement learning: performance optimisation that detects bottlenecks and validates fixes with A/B tests, dependency management that assesses library risk and performs safe upgrades, and architecture evolution where ML tools recommend structural changes. He says his own team at AWS used to spend around 30% of its time on cleanup and migration work of this kind.

He quotes large improvements in recovery time, operational overhead and infrastructure cost for organisations adopting these systems. The talk does not show the methodology behind those figures, so read them as the speaker's reported results rather than benchmarks.

## The roadmap is the takeaway

The four phases are the most reusable part. Foundation: observability and standardised infrastructure as code, because nothing autonomous works without good telemetry. Augmentation: AI-assisted monitoring, anomaly detection and early predictive scaling with humans in the loop. Autonomy: remediation and predictive scaling with minimal intervention, plus early code optimisation. Evolution: self-improving systems that adapt architecture through reinforcement learning.

He closes on what comes next: multi-agent systems sharing infrastructure decisions, explainable AI operations for accountability, cross-platform optimisation over hybrid and multi-cloud, and infrastructure that learns from patterns across industries.

## Who should watch

Platform leads and engineering managers building a case for investing in AIOps, and SREs who want a staged plan to point at. If you want config files and code, pair it with one of the talks below.

## Related Conf42 talks

- [Vijaybhasker Pagidoju on AI-driven self-healing infrastructure as the next step for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Vijaybhasker_Pagidoju_selfhealing_infrastructure) at Conf42 SRE 2025.
- [Leonid Belkind (StackPulse) on chaos engineering and generic mitigations](https://www.conf42.com/Chaos_Engineering_2021_Leonid_Belkind_generic_mitigations_self_healing_systems), an earlier take on the same goal.
- [Sudhakar Pallaprolu on building self-healing cloud infrastructure in Go](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure) at Conf42 Golang 2026.

[Watch Mohan Singh's talk](https://www.conf42.com/MLOps_2025_Mohan_Singh_building_autonomous_mlops) for the full three-pillar model.

[Watch the talk on YouTube](https://youtu.be/Fostk7boNTA).

## Watch the talk

[Building Autonomous MLOps: Self-Healing Infrastructure and AI-Driven Code Evolution](https://www.conf42.com/MLOps_2025_Mohan_Singh_building_autonomous_mlops) at Conf42 MLOps 2025.
