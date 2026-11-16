# Design for the crisis before it arrives, not during the outage

Conf42 Blog, 2025-09-24, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/design-for-crisis-before-the-crisis-arrives

In short: Dhruvesh Talati (Ally) at Conf42 Kube Native 2025 on cloud-native patterns that keep crisis-response systems up, scaled and talking to each other.

When a flood, a cyberattack or a pandemic hits, the systems people need most get their worst traffic day at the same moment the infrastructure underneath is least reliable. At Conf42 Kube Native 2025, Dhruvesh Talati, Senior Software Engineer at Ally with a background in cloud infrastructure and DevSecOps, argued that resilience for those systems has to be designed in from the first commit rather than bolted on after the first outage.

This is a strategy talk more than a hands-on one. Think of it as a checklist for an architecture review of anything that has to stay up when everything else is falling over.

## Three demands that legacy stacks fail at once

Dhruvesh frames crisis resilience as three pillars. Availability: emergency calls and medical services need near-perfect uptime, and he puts the target at 99.99%. Scalability: surges are unplanned, so the platform has to absorb something like ten times normal capacity within minutes. Interoperability: crisis response means public agencies, private companies and aid groups sharing data in real time, which only works if their systems can actually talk.

His point is that on-premise estates built for steady load struggle on all three together, and a weakness in one organisation spreads to everyone depending on it.

## The patterns are familiar; the stakes aren't

The building blocks will be known to any SRE: microservices so one failure stays local, Kubernetes for scheduling, scaling and self-healing, and infrastructure as code so a region can be rebuilt the same way twice. Then the four classic fault-tolerance patterns:

- Circuit breakers that isolate a failing dependency before it cascades.
- Timeouts that kill hung requests before they eat every thread.
- Retries with exponential backoff, so a flaky network does not become a self-inflicted load test.
- Bulkheads that partition resources so a noisy service cannot starve the critical one.

What the talk adds is the framing. In a normal product these are reliability hygiene. When the product is an emergency dispatch system, they decide whether the service survives the day it matters.

## Multi-region, edge and zero trust as one design

Beyond elastic scaling with real-time monitoring and smart traffic routing between zones, Dhruvesh pushes for active multi-region deployments with automated failover and strongly consistent replication, so disaster recovery stops being a scramble and becomes a property of the system.

Two less common points stood out. First, edge sites that keep working when the link to the central cloud drops, with local processing under 100 milliseconds for life-critical uses such as patient monitoring. Second, zero trust, because perimeter security tends to dissolve in exactly the chaos a crisis creates: continuous verification, strict least privilege and encryption in transit, at rest and in processing.

He also covers AI for predicting escalation and recommending resource allocation, though at a high level.

## Migrate in phases, start with what can break

The migration advice is pragmatic: assess and define resilience requirements, prove the architecture on non-critical systems, move core services using known patterns, then integrate and optimise with the legacy estate still in the picture. And treat resilience as an ongoing capability rather than a project with an end date.

## Who should watch

Architects and engineering leads in public-sector, healthcare, finance or utility platforms who need the vocabulary to argue for multi-region and failover budgets. If you want YAML and failure-injection demos, pair it with one of the talks below.

## Related Conf42 talks

- [Disaster Recovery preparedness using Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) by Kyle Shelton (AWS), to test the DR plan instead of trusting it.
- [Preparing for disaster: going Multi-Region](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region) by Ana Van Straaten (Globant), the multi-region part in practice.
- [Enhancing Business Resilience with Azure Site Recovery](https://www.conf42.com/Cloud_Native_2025_Somaning_Turwale_resilience_disaster_mitigation) by Somaning Turwale (Microsoft), one concrete failover tool.

[Watch Dhruvesh Talati's talk](https://www.conf42.com/Kube_Native_2025_Dhruvesh_Talati_resilience_design_recovery)

[Watch the talk on YouTube](https://youtu.be/plB_WOmLlNw).

## Watch the talk

[Resilient by Design: Cloud-Native Architectures for Crisis Response and Recovery](https://www.conf42.com/Kube_Native_2025_Dhruvesh_Talati_resilience_design_recovery) at Conf42 Kube Native 2025.
