# Solution architects are what make a Kubernetes CRM resilient

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/solution-architects-make-kubernetes-crm-resilient

In short: Chakra Gadige (Splunk) at Conf42 Kube Native 2025 on how Technical Solution Architects steer CRM platforms onto Kubernetes without new bottlenecks.

Moving a CRM onto Kubernetes is mostly an organisational problem with a YAML-shaped tail. At Conf42 Kube Native 2025, Chakra Gadige, Technical Lead for Salesforce at Splunk, argued that the role holding that move together is the Technical Solution Architect (TSA): the person who translates business goals into a cluster design and keeps today's shortcut from becoming next year's outage.

This is a short, high-level talk. There is no demo and no code; it is a framework for how to think about CRM modernisation and who should own it. If you lead a platform or CRM team and need a checklist to argue with, it is worth the time.

## The CRM stopped being a monolith, so the architect stopped being a diagrammer

Chakra's starting point is the shift he sees in CRM platforms: away from monolithic suites and towards containerised services, with Kubernetes as the default orchestration layer. That shift changes the job. In his framing, the TSA is a "business translator" who makes sure technical design lines up with what the organisation wants, and a manager of technical debt who designs systems that scale before they have to.

His most useful line is that TSAs are simplifiers. They reduce complexity by finding where technical debt comes from, designing a streamlined architecture, using a modular approach to scaling, and putting observability in early so problems surface before customers notice them. Anyone who has inherited a CRM integration layer with eleven point-to-point connectors knows exactly why that matters.

## Resilience comes from a short list of principles

The architecture section is a compact list of principles for a Kubernetes-native CRM:

- microservices for flexibility, so one team's change doesn't redeploy the world
- declarative configuration for consistency across environments
- deliberate stateful service management, because CRM data has to persist
- API-first design and integration
- a zero trust security model, end to end

None of these is new on its own. The value is in seeing them applied to CRM, where stateful data, multi-tenancy and integrations with every other system make shortcuts expensive.

## Before and after is the honest way to sell it

Chakra frames the change as a before-and-after. Before the TSA gets involved: monolithic CRMs, manual deployments, inconsistent environments and security gaps. After: a microservice-based CRM on Kubernetes, automated CI/CD pipelines, security built in by design, and full observability.

He also says how to know whether it worked. The metrics he lists are the DORA family: change failure rate, mean time to recovery, deployment frequency and lead time for changes. That's the right answer, because calling an architecture resilient is a claim and those four numbers are the evidence.

## The hard parts get named, briefly

The challenges slide covers the problems that bite in practice: stateful workload management, integration latency, database performance and multi-tenant complexity. The mitigations he pairs with them are the standard Kubernetes toolkit: StatefulSets, caching, service mesh adoption and namespace isolation. Security gets its own list: identity and access management, secret management, network policies between microservices, and continuous container scanning.

The roadmap is five stages: assessment, design of a Kubernetes-native blueprint, a pilot that proves core functionality, progressive migration, and continuous optimisation. A pilot before migration sounds obvious. Plenty of CRM programmes skip it anyway.

## Who should watch

Architects and engineering managers planning a CRM or Salesforce-adjacent modernisation, and anyone who has to explain to leadership why a Kubernetes migration needs an owner and not just a ticket. Engineers looking for StatefulSet tuning or mesh configuration should look elsewhere; this talk stays at the level of principles and roles.

## Related Conf42 talks

- [De-Risking a Legacy CRM Migration in Life Sciences](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) shows the rollout side: feature flags guarding a governed Salesforce migration.
- [Salesforce Platform & AI Agentforce as a CloudNative App](https://www.conf42.com/Cloud_Native_2025_Pradeep_Reddy_Guttha_salesforce_ecosystem_development) looks at Salesforce itself through a cloud-native lens.
- [Modernize without the madness](https://www.conf42.com/Cloud_Native_2024_Hareesh_Iyer_modernize_monoliths_microservices) covers the phased monolith-to-microservices path in general terms.

[Watch Chakra Gadige's talk](https://www.conf42.com/Kube_Native_2025_Chakra_Gadige_crm_resilience_secure)

[Watch the talk on YouTube](https://youtu.be/fxayyGcwqe8).

## Watch the talk

[Architecting CRM Resilience: How TSAs Enable Scalable, Secure K8s-Native Systems](https://www.conf42.com/Kube_Native_2025_Chakra_Gadige_crm_resilience_secure) at Conf42 Kube Native 2025.
