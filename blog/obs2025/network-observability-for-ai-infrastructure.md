# AI clusters need networks that observe and heal themselves

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/network-observability-for-ai-infrastructure

In short: Bhaskararao Vakamullu at Conf42 Observability 2025 traces network observability from ARPANET to streaming telemetry and self-healing AI networks.

When a single switch moves 51.2 Tbps and ports run at 800G, polling SNMP every few minutes is like checking a Formula 1 car with a sundial. At Conf42 Observability 2025, Bhaskararao Vakamullu, an Anna University graduate who has worked at networking and observability companies, made the case that AI workloads have turned the network into the critical path, and that the network now has to observe and repair itself in real time.

## Sixty years of watching packets

The first section is a history lesson, and a good one for anyone who started with Datadog. In the 1960s ARPANET, the packet-switching research network that became the internet, had rudimentary tools: interface message processor consoles, a network control centre, ping-like utilities. From the 1980s to 2000, SNMP became the standard for performance and health metrics. Then came agent-based monitoring on VMs and containers, SaaS dashboards from New Relic, Datadog and Stackdriver, threshold and anomaly alerts in CloudWatch, and integrations with PagerDuty, Slack and CI/CD. Today's stack adds Grafana, Prometheus and Loki, OpenTelemetry as the open standard, Dynatrace, ML monitoring tools for drift and explainability, and native tooling from AWS, GCP and Azure.

## Why AI raises the stakes

Bhaskararao lists four reasons network observability matters more for AI: performance guarantees that hold under real workloads, failure domain isolation so a fault in ingestion, training or inference does not cascade, resource optimisation across expensive compute, and security, since AI systems are attractive targets for data breaches and model theft.

The hardware numbers explain the urgency. Ports that were a revolution at 100G are now built at 800G; a single networking box processes 51.2 Tbps. Training and inference need ultra-low latency to stay synchronised and near-perfect availability, because an interrupted training run is expensive.

## Streaming telemetry replaces polling

The shift he calls the programmable telemetry revolution is the practical core. Traditional monitoring collects predefined metrics such as CPU, memory, disk and traffic, mostly through periodic checks and thresholds. That works for basic health but lacks the context distributed AI systems need. Modern telemetry, with gRPC streaming as his example, continuously pushes high-resolution metrics, logs, events and traces from every layer, and feeds analytics and ML that can predict problems before users see them.

## Detect, analyse, decide, execute

The self-healing architecture is a closed loop. Real-time telemetry detects faults, degradations and threats. Analysis correlates metrics, logs and traces across components with ML to find the root cause. The decide phase weighs policy rules and historical incidents to pick a remediation: isolate a component, fail over, change a configuration. Execution then runs it automatically through playbooks and orchestration tools: reroute traffic, restart services, scale resources. The goal is a network that does not wait for a human at 3 AM.

## Still hard: opaque hardware and sheer scale

He is honest that visibility gaps remain. GPUs, TPUs and accelerators from different vendors follow different protocols, so hardware is often a black box. Correlating user behaviour, system logs and network metrics across domains is difficult. And AI systems generate so much telemetry that collecting and processing it without adding latency requires sampling and aggregation.

The future section points at chip-level telemetry (power, temperature, clock speed, cache misses), AI-powered analysis, digital twin networks for testing changes safely, and intent-based observability. His example of intent is the best line in the talk: instead of asking how the CPU is doing, ask whether important users in the EU region are getting 4K quality, and act on that.

## Who should watch

Network and infrastructure engineers moving into AI clusters, and SREs who want the history of their tools in one place. This is a broad survey, heavy on definitions and history, with no demos; watch it for the big picture and the intent-based framing.

## Related Conf42 talks

- [Siri Varma Vegiraju on building a network telemetry platform to minimise security threats](https://www.conf42.com/Platform_Engineering_2024_Siri_Varma_Vegiraju_network_telemetry_security) at Conf42 Platform Engineering 2024.
- [Dumlu Timuralp on the life of a packet in Amazon EKS](https://www.conf42.com/Cloud_Native_2025_Dumlu_Timuralp_networking_performance_optimization) at Conf42 Cloud Native 2025.
- [Sunil Govindankutty on testing network resilience with fault injection on Amazon ECS](https://www.conf42.com/Chaos_Engineering_2025_Sunil_Govindankutty_network_resilience_experiments) at Conf42 Chaos Engineering 2025.

[Watch Bhaskararao Vakamullu's talk](https://www.conf42.com/Observability_2025_Bhaskararao_Vakamullu_networking_era_highways)

[Watch the talk on YouTube](https://youtu.be/aMZWGhzzrZ0).

## Watch the talk

[Invisible Highways: Observability in the Evolution of AI-Era Networking Infrastructure](https://www.conf42.com/Observability_2025_Bhaskararao_Vakamullu_networking_era_highways) at Conf42 Observability 2025.
