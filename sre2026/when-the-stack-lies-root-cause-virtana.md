# When every dashboard blames someone else, map the dependencies

Conf42 Blog, 2026-03-19. https://www.conf42.com/sre2026/when-the-stack-lies-root-cause-virtana

In short: David McNerney and Daniel Raskin of Virtana at Conf42 SRE 2026 on finding root cause with a live system dependency graph and investigating agents.

Modern outages are system problems, not application problems. That is the thesis David McNerney, Director of Product Management at Virtana, and Daniel Raskin, Virtana's Chief Marketing Officer, brought to Conf42 Site Reliability Engineering 2026. Their answer to the familiar incident where every tool points at a different culprit is a system dependency graph, discovered automatically and kept current, which both humans and AI agents can use as context while they hunt for root cause.

## The incident where every tool is right and nobody is

Every SRE has been on this call. A service slows down, the dashboards light up, application metrics say one thing and infrastructure metrics say another. Each team's view is accurate for its own layer, and none of them explains the outage, because the cause lives in the interaction between layers.

The examples in the talk are the kind that cost hours. A spike in a storage queue throttles Kubernetes pods, and the pods look like the problem. Network contention shows up as application latency, so the application team starts profiling code. A GPU pipeline stalls, but the real bottleneck is the upstream data feeding it. In each case the symptom appears in one place and the cause in another, and traditional APM, built around services, plus telemetry split across tools, makes the jump between them hard.

## A graph of how the system actually behaves

The approach Virtana presents in the talk is a System Dependency Graph: a continuously updated map of the relationships between services, Kubernetes objects, infrastructure, networks and storage, discovered from production rather than drawn from an architecture diagram. The difference matters. The diagram in your wiki shows how the system was meant to work. A discovered graph shows how it is wired today, including the dependency someone added during last quarter's migration and never documented.

Once you have that map, the question during an incident stops being which dashboard is right. It becomes what this slow service depends on, and which of those dependencies changed. Following edges from symptom to cause is what an experienced SRE does in their head. The graph makes that path explicit and gives everyone on the call the same picture.

## Agents that use the graph as context

The second half of the talk, per the abstract, is a demo of autonomous agents using the dependency graph as operational context: investigating incidents, tracing cascading failures across layers and surfacing root cause faster. This is the same pattern several Conf42 speakers arrived at in 2026. An LLM agent with access to metrics alone tends to produce plausible stories. An agent that can walk a relationship graph has a structure to reason over, so its conclusions can be checked against real dependencies instead of taken on trust.

If you are evaluating any tool in this space, the talk suggests some good questions to ask: how the graph is discovered and how fresh it stays, whether it reaches below Kubernetes into network and storage, and whether the agent's investigation can be traced edge by edge so an engineer can verify it.

## Who should watch

SREs and platform engineers who run Kubernetes on shared infrastructure and keep losing the first hour of incidents to blame between layers. It is a vendor talk: the graph and the agents shown are Virtana's. The framing of outages as system behaviour, and the habit of following dependencies rather than dashboards, are useful whatever you run.

[Watch David McNerney and Daniel Raskin's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) ([YouTube](https://youtu.be/z9mjbWbV8eo)).

## Related Conf42 talks

- [Shipping with Context: Knowledge Graphs as the Backbone of AI-First Software Delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) by Prateek Mittal (Harness), LLMs 2026: the same graph-as-context idea, applied to delivery pipelines.
- [Feature Flags as Incident Evidence: Safer AI-Assisted RCA Workflows](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) by Ishan Shah (PayPal), Feature Flags 2026.
- [Mastering Observability in Distributed Systems: Tools, Techniques, and Lessons Learned](https://www.conf42.com/Observability_2025_Raghavender_Puchhakayala_tools_mastering_techniques) by Raghavender Puchhakayala (JPMorgan Chase), Observability 2025.

## From Virtana

Virtana builds what the talk calls relationship-aware observability; the session shows its System Dependency Graph and agent-driven root cause analysis.

- [virtana.com](https://www.virtana.com/)

## Watch the talk

[When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) at Conf42 Site Reliability Engineering (SRE) 2026.
