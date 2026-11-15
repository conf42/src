# AI can run the network, but you still need to know BGP

Conf42 Blog, 2025-10-27, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/ai-network-engineering-still-needs-bgp

In short: Vamsi Gadireddy of Microsoft Azure at Conf42 Prompt Engineering 2025 on AI-driven network engineering, self-healing networks and the skills that still matter.

The 2 AM router failure used to mean a phone call. At Conf42 Prompt Engineering 2025, Vamsi Gadireddy, Senior Network Engineer on Microsoft Azure, described how AI is moving network operations from monitor-and-react to anticipate-and-adapt, and argued that this makes protocol fundamentals more important, not less.

It is a career-and-strategy talk for network engineers rather than a prompt engineering deep cut. Expect a roadmap and a skills list, with real examples sprinkled in.

## Three kinds of network, one engineer

Vamsi says the modern network engineer has to be fluent in three worlds. Enterprises care about compliance, uptime and security (think a bank keeping trading live around the clock, or a healthcare company keeping HIPAA intact across clouds without slowing doctors down). Cloud providers care about automation and elasticity at continental scale. Telecom operators carry enormous traffic and billions of IoT connections. His image for enterprise work is renovating an old house while keeping the lights on, because the legacy systems never expected to talk to cloud services.

## The fundamentals are your compass

The part worth underlining: AI can optimise configurations, but it cannot replace understanding of BGP, OSPF and MPLS. When a model recommends a route change, someone has to tell whether it really improves latency or hides a topology problem. IPv6, security and observability join that core list as IoT pushes past what IPv4 can address.

On top of that, he wants programming fluency, AI literacy and data interpretation. If a model suggests reallocating bandwidth based on telemetry, you should know what it learned from and what biases it may carry. The new command line, in his telling, is Python, YAML, JSON and Git, driving Ansible, Terraform, Netmiko-style libraries, NAPALM and SDN controllers. You push a commit, and validated changes roll across hundreds of devices.

## Where AI already pays

Vamsi lists anomaly detection (traffic spikes that might be an attack), predictive maintenance (ports and links likely to fail) and root cause analysis that correlates thousands of logs in seconds. His example is a global telco that used AI to detect Wi-Fi degradation across regions before customers noticed.

Self-optimising networks are the next step: systems that diagnose themselves and reroute around failures, such as shifting traffic from a failed Singapore link through Tokyo without anyone touching a console. He is clear that autonomy needs guardrails, with engineers defining what the AI is allowed to change.

## Humans keep the context

His best example of why: an AI might flag a huge data transfer as a security threat, while a human knows it is the sanctioned quarterly backup. AI speeds up analysis; people supply business context, regulation and judgment.

He closes with design principles (API-first, microservices, declarative configuration, observability by default, horizontal scaling, stateless design, graceful degradation, chaos engineering in the spirit of Netflix's Chaos Monkey) and a five-step roadmap: assess, automate and collect telemetry, pilot AI in low-risk areas such as anomaly detection, scale what works, and keep learning.

## Who should watch

Network engineers wondering which skills to invest in next, and engineering managers planning a NetDevOps or AIOps programme. If you already run intent-based networking in production, the material will be review; the framing is still handy for explaining it to leadership.

## Related Conf42 talks

- [Jason Belk's introduction to Ansible for network engineers](https://www.conf42.com/Cloud_Native_2022_Jason_Belk_ansible_network_engineers) at Conf42 Cloud Native 2022, the automation baseline Vamsi assumes.
- [Akshat Kapoor on predictive network maintenance](https://www.conf42.com/Prompt_Engineering_2024_Akshat_Kapoor_predictive_network_failures) at Conf42 Prompt Engineering 2024.
- [Sunil Govindankutty on testing network resilience in Amazon ECS](https://www.conf42.com/Chaos_Engineering_2025_Sunil_Govindankutty_network_resilience_experiments), chaos engineering applied to the network layer.

[Watch Vamsi Gadireddy's talk](https://www.conf42.com/Prompt_Engineering_2025_Vamsi_Gadireddy_network_protocols_reliability), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/Q55GIEy-p4g).

## Watch the talk

[The AI-Driven Future of Network Engineering: Scaling Protocols, Reliability, and Intelligence](https://www.conf42.com/Prompt_Engineering_2025_Vamsi_Gadireddy_network_protocols_reliability) at Conf42 Prompt Engineering 2025.
