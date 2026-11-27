# ML Network Routing Should Start in Shadow Mode

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ml-routing-rollout-shadow-mode-first

In short: Rahul Tavva of Kairos Technologies at Conf42 Platform Engineering 2025 on a phased rollout of ML-based routing with BGP and OSPF as the fallback.

Nobody sane hands their network to a model overnight. At Conf42 Platform Engineering 2025, Rahul Tavva, a senior network delivery lead at Kairos Technologies in Dallas, laid out how to bring ML-based routing into production the careful way: telemetry first, then shadow mode, then advisory mode, then automation for low-risk traffic, with classic protocols kept as the safety net throughout.

The talk is short and high level. Its value is the rollout plan and the operational questions, which apply to putting any model in a control loop.

## Why BGP and OSPF aren't enough on their own

Rahul's framing: BGP and OSPF have been reliable for decades, but they run on fixed rules, react only after something breaks, take a while to converge and lean on manual tuning. Cloud, microservices and real-time apps want routing that adapts. ML systems learn from network data, spot patterns, predict trouble and reroute before it happens, balancing speed, cost and reliability, and they can flag unusual patterns that hint at a failure or a security problem.

## The pipeline

The architecture has four parts: telemetry collection (latency, packet loss, throughput, link usage, application patterns, even time of day and scheduled maintenance), a data pipeline that cleans it, a training system that builds, tests and stores models, and an inference system that makes routing decisions in real time. Fallbacks and safety switches sit around all of it.

Training options include supervised learning on past good decisions, reinforcement learning from feedback, and a hybrid that mixes ML with traditional routing, which he recommends as the best fit today.

## Four phases, and the first one changes nothing

1. **Shadow mode**: the model makes decisions on paper only.
2. **Advisory mode**: the model suggests routes and engineers approve them.
3. **Selective automation**: the model takes over certain traffic classes or low-criticality regions.
4. **Full automation**: the model runs routing, with the classic protocols as backup.

If you've done progressive delivery for application code, this is the same idea pointed at the control plane. The difference is that the blast radius is the network.

## The operational questions are the real content

Monitoring an ML router means watching the model, not just the links: accuracy, drift, confidence per decision. Dashboards should show ML and traditional routes side by side and explain why a path was chosen, which is how operators come to trust it.

Security gets its own section: poisoned telemetry can steer routes, and a reverse-engineered model can be exploited, so encrypt telemetry, validate inputs, run anomaly detection and always keep a human override. Runbooks need new entries for what to do when the model makes strange choices, when confidence drops or when telemetry breaks: how to roll back, shift traffic gradually and retrain after an incident.

He cites examples from financial services (latency spikes cut by almost 70%) and e-commerce (page load times down 30% at peak, far fewer manual interventions), alongside the challenges they hit: compliance concerns, false alarms and models degrading during unusual events.

## Who should watch

Network engineers being asked about AIOps, and platform teams that will end up hosting the models. It needs network engineers, data scientists, platform and ops people working together, with cross-training, which is perhaps the most realistic slide in the deck.

## Related Conf42 talks

- [Tammy Bryant Butow: Chaos Engineering, When The Network Breaks](https://www.conf42.com/Chaos_Engineering_2021_Tammy_Bryant_Butow_breaking_network), for testing the fallbacks.
- [Dumlu Timuralp: Life of a packet in Amazon EKS](https://www.conf42.com/Cloud_Native_2025_Dumlu_Timuralp_networking_performance_optimization).
- [Sunil Govindankutty on network fault injection in Amazon ECS](https://www.conf42.com/Chaos_Engineering_2025_Sunil_Govindankutty_network_resilience_experiments).

[Watch Rahul Tavva's talk](https://www.conf42.com/Platform_Engineering_2025_Rahul_Tavva_routing_world_deployments)

[Watch the talk on YouTube](https://youtu.be/vgpLrhLnMZ8).

## Watch the talk

[Building Production-Ready ML-Based Network Routing: Lessons from Real-World Platform Engineering Deployments](https://www.conf42.com/Platform_Engineering_2025_Rahul_Tavva_routing_world_deployments) at Conf42 Platform Engineering 2025.
