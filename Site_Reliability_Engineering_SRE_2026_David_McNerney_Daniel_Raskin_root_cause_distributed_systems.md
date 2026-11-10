# When the Stack Lies: Finding Root Cause in Distributed Systems

A talk at [Conf42 Site Reliability Engineering (SRE) 2026](https://www.conf42.com/sre2026) by [David McNerney](https://www.conf42.com/speaker_David_McNerney) (Director of Product Management @ Virtana) and [Daniel Raskin](https://www.conf42.com/speaker_Daniel_Raskin) (Chief Marketing Officer @ Virtana). Page: https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems

Video: https://www.youtube.com/watch?v=z9mjbWbV8eo

## Abstract

SRE teams know the pattern. A service slows down, dashboards light up, and every tool points to a different culprit. Application metrics say one thing, infrastructure metrics say another, and the real cause is buried somewhere in the interactions between them.

Modern incidents rarely originate in a single component. A storage queue spike can throttle Kubernetes pods. Network contention can cascade into application latency. GPU pipelines can stall because of upstream data bottlenecks. These failures emerge from system behavior, not isolated services, which makes them difficult to diagnose with traditional APM and fragmented telemetry.

In this session, we explore a system-aware approach to operations. We will demonstrate how to automatically construct a System Dependency Graph that continuously discovers and maps relationships across services, Kubernetes, infrastructure, networks, and storage, exposing how the system actually behaves in production. The demo will also show how autonomous agents can use this graph as operational context to investigate incidents, trace cascading failures, and surface root cause faster.

Attendees will leave with a clearer understanding of why modern outages are system problems, not application problems, and how SRE teams can use relationship-aware observability and agentic intelligence to diagnose them.
