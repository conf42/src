# AI can take the toil out of platform teams if humans stay in the loop

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-ops-for-platform-teams-starts-with-human-loop

In short: Anbarasu Aladiyan of Compunnel maps AI-driven provisioning, scaling and self-service for platform teams at Conf42 Platform Engineering 2025, plus a phased rollout.

Platform teams are meant to make developers faster, and most of them spend their week answering tickets instead. At Conf42 Platform Engineering 2025, Anbarasu Aladiyan, Lead Java Full Stack Engineer at Compunnel, argues that AI-driven automation, in provisioning, scaling and self-service, is how platform teams climb out of reactive mode, and he lays out a four-phase plan for getting there without betting the cluster on it.

## The cost of the ticket queue

Aladiyan's problem statement is about time. Microservices multiply instances, every instance needs managing, and the platform team sits in the middle of thousands of developers and applications. He cites research figures that will feel familiar to anyone who has run an internal platform: developers losing several hours a week to infrastructure chores, a large share of feature delays traced back to platform bottlenecks, and platform engineers spending most of their time reacting and troubleshooting while the improvement backlog grows. Slow provisioning then shows up downstream as slower release cycles.

Treat the precise percentages as industry survey numbers rather than one team's measurement; the shape of the problem is the point.

## Three generations of scaling

The clearest part of the talk is a progression. Manual scaling means people adjust resources by anticipated need, so you get over-provisioning, performance issues and hours of response time. He adds a detail worth checking in your own cluster: instances idling at zero percent CPU and memory, and several low-utilisation copies of the same service, while other services wait for capacity.

Rule-based automation, with fixed thresholds and predetermined scaling rules, is where most teams live today. It helps, but it does not adapt and still needs frequent human intervention. The third stage is AI-powered orchestration that learns usage patterns, predicts needs and adjusts infrastructure in real time, turning scaling from an hours-long job into minutes.

## Where AI touches Kubernetes

For Kubernetes specifically he lists intelligent pod placement based on historical performance data, node scaling that anticipates workload changes, self-healing that shortens time to respond, and proactive detection of cluster-level problems. The headline claims are better utilisation, lower infrastructure cost and handling around three times the workload on the same hardware.

On the developer side, the vision is a self-service platform: infrastructure requested in natural language and translated into properly configured resources, configuration drift detected and corrected before it reaches production, developer portals that surface relevant docs based on project context, and continuous scanning of infrastructure as code with suggested fixes. His case study is a global financial services firm with roughly 2,800 developers and strict compliance needs, which rolled out self-service provisioning first, then anomaly detection, then automated compliance validation for every deployment, and reported a big drop in production incidents.

## Start with a human in the loop

The best section is on what goes wrong. Aladiyan lists poor-quality training data, skills gaps, resistance from operations teams, legacy integrations and worries about opaque AI decisions. His mitigations are practical: improve observability first and use synthetic data while real datasets build up, run education programmes and clear upskilling paths, put abstraction layers with well-defined APIs in front of legacy systems, keep comprehensive logs, use explainable approaches, and start with a human-in-the-loop model before letting automation act on its own.

The rollout runs in four phases: assess capabilities and pain points and define KPIs, build the foundation (observability, standardised IaC, API-first services), deploy targeted capabilities such as predictive scaling for critical workloads and a self-service portal, then scale across platform services and into CI/CD.

## Who should watch

Platform leads writing the case for AI-assisted operations, and teams still on rule-based autoscaling wondering what comes next. It is a strategy talk with survey numbers rather than a technical demo, so bring your own implementation details.

## Related Conf42 talks

- [Building the Internal Developer Platform (IDP) for Generative AI](https://www.conf42.com/Platform_Engineering_2026_Brindal_Patel_idp_generative_apis) by Brindal Patel, Conf42 Platform Engineering 2026
- [Proactive cluster autoscaling in Kubernetes](https://www.conf42.com/Cloud_Native_2023_Chris_NesbittSmith_proactive_cluster_autoscaling_kubernetes) by Chris Nesbitt-Smith, Conf42 Cloud Native 2023
- [Why should you bother about cluster autoscaling using Karpenter](https://www.conf42.com/Cloud_Native_2022_Raja_Ganesan_cluster_autoscaling_karpenter) by Raja Ganesan, Conf42 Cloud Native 2022

[Watch Anbarasu Aladiyan's talk](https://www.conf42.com/Platform_Engineering_2025_Anbarasu_Aladiyan_automating_enhanced_experience)

[Watch the talk on YouTube](https://youtu.be/rs3_kJ75xiE).

## Watch the talk

[AI-Driven Platform Engineering: Automating Infrastructure at Scale for Enhanced Developer Experience](https://www.conf42.com/Platform_Engineering_2025_Anbarasu_Aladiyan_automating_enhanced_experience) at Conf42 Platform Engineering 2025.
