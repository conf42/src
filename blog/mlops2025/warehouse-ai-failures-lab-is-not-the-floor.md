# Warehouse AI that aces the lab can still fail on the floor

Conf42 Blog, 2025-09-01, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/warehouse-ai-failures-lab-is-not-the-floor

In short: Shubham Beldar (Symbotic) at Conf42 MLOps 2025 on four warehouse automation failure patterns and the MLOps habits that prevent them.

A picking robot that scores above 90% in the lab can drop to the low 60s the first time it meets shrink wrap. At Conf42 MLOps 2025, Shubham Beldar, Solutions Engineer at Symbotic, walked through four ways AI fails in real warehouses and the MLOps practices that stop it: validate on the live floor, monitor across systems, deploy in phases, and never underestimate the people who have to use it.

Shubham has spent over six years designing automated distribution centres for large retailers across grocery, healthcare, apparel and food, and the talk is grounded in that floor-level experience.

## Failure one: the physical reality gap

The lab never had transparent shrink wrap on a robot-built pallet, irregularly shaped products, or dust on the vision sensors. Real warehouses have all three. Shubham describes accuracy falling from around 95% to the low 60s when systems hit those conditions.

His diagnosis is pure MLOps: training data lacked messy real-world cases, validation happened only in the lab, and no feedback loop pushed floor errors back into retraining. Teams optimised for benchmarks instead of reality.

## Failure two: forecasts that never noticed the market moved

Demand forecasting models worked until market volatility hit. Then came overstock of the wrong SKUs, empty shelves at peak demand and errors compounding unchecked. The root causes he lists are no drift detection, stale ground truth, no human verification points, and no fallback plan. His image: the model keeps steering even as it heads off the cliff.

## Failure three: seven middlewares and a schema mismatch

Many warehouses run seven or eight middleware systems. Each looks fine in isolation, but when traffic spikes, latency cascades across them, and a single schema mismatch becomes the single point of failure that brings the deployment down. The fixes: shared monitoring across teams, testing the full integrated system instead of components, and graceful degradation plans. Anyone who has debugged a distributed system will nod along; the warehouse just adds forklifts.

## Failure four: the people said no

The most striking story is about trust. One parts distributor invested about $7 million in an automated system, the workforce rejected it after early failures, and the whole thing was abandoned. Operators with 20 years of experience often believe they are more productive doing it their way, and some fear for their jobs. If they do not trust the system, they route around it.

## What actually works

Shubham's strategies map one-to-one onto the failures:

- **Phased deployment.** Start with controlled pilots in shadow mode next to existing operations, and scale when metrics hold. He cites a large US retailer rolling out one phase at a time, which he says reduced integration risk by nearly 40% compared with big-bang launches.
- **Comprehensive testing.** Adversarial tests, worst-case scenarios, chaos engineering, synthetic edge cases, and load tests timed for peaks like Christmas and Black Friday.
- **Hybrid human-AI operation.** Clear human-in-the-loop protocols, human corrections fed back into training, and AI designed to augment workers rather than replace them. The best results he has seen paired high inventory accuracy with better workforce morale.

His closing point is worth taping to a monitor: the most successful warehouse projects do not always have the most advanced algorithms. They follow ML operations practices.

## Who should watch

Robotics and supply chain engineers, and any MLOps team deploying models into the physical world where sensors get dirty and people have opinions. It is a lessons-learned talk, not an architecture deep-dive.

## Related Conf42 talks

- [SRE for Supply Chain: Building Reliable Human-AI Warehouse Operations at Scale](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses)
- [AI-Powered Incident Prevention: Supply Chain Monitoring and Automated Response](https://www.conf42.com/Incident_Management_2025_Krishna_Chaitanya_Yarlagadda_supplychain_automation_prevention)
- [Data-Driven Warehouse Design for Scalable, Risk-Resilient 3PL RFPs](https://www.conf42.com/Golang_2026_Vivek_Sander_data_driven_warehouse)

[Watch Shubham Beldar's talk](https://www.conf42.com/MLOps_2025_Shubham_Beldar_when_ai_automation)

[Watch the talk on YouTube](https://youtu.be/IzIwSGEHA3Y).

## Watch the talk

[When AI Automation Goes Wrong: Real-World MLOps Lessons from Warehouse Deployment Disasters](https://www.conf42.com/MLOps_2025_Shubham_Beldar_when_ai_automation) at Conf42 MLOps 2025.
