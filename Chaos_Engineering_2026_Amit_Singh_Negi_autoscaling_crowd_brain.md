# Surviving a 300% Flash Crowd: State-Safe Autoscaling With Zero Split-Brain Events

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Amit Singh Negi](https://www.conf42.com/speaker_Amit_Singh_Negi) (Software & Systems Architect @ T-Mobile). Page: https://www.conf42.com/Chaos_Engineering_2026_Amit_Singh_Negi_autoscaling_crowd_brain

## Abstract

Flash crowds expose a weak point in Kubernetes. The default autoscaler reacts only after thresholds break, and new pods take 30 to 90 seconds to become ready. During a simulated 300% surge on a stateful telemetry workload, P99 latency hit 4,200ms, and the baseline cluster recorded 14 split-brain events.  This talk walks through replacing the HPA loop with a Proximal Policy Optimization (PPO) reinforcement-learning agent. Its reward function penalizes state-synchronization faults alongside SLA violations. Before any pod is killed, it runs a four-step handoff: drain, flush, reassign, terminate. The system was tested in a one-month A/B experiment across 50 bare-metal nodes, with surges from 10,000 to 40,000 RPS in under 5 seconds.  Split-brain events fell from 14 to zero, P99 latency dropped to 1.2ms, and cold starts went from 45 seconds to zero.  Attendees will learn how surge experiments expose state-safety failures, plus a scaling pattern that stays consistent under stress.
