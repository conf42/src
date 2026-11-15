# Production ML needs HA, DR and Zero Trust designed in from day one

Conf42 Blog, 2026-02-12, updated 2026-11-09. https://www.conf42.com/blog/ml2026/production-ml-needs-ha-dr-zero-trust

In short: Srinivas Talasila (SAP) at Conf42 Machine Learning 2026 on the infrastructure pillars that keep ML training and serving available, secure and auditable.

A model that works in the lab still has to survive a zone outage, a traffic spike and an auditor. At Conf42 Machine Learning 2026, Srinivas Talasila, Director of Cloud Operations at SAP, argued that availability, recovery and security for ML platforms have to be settled in the planning phase, because bolting them on after launch is how you get both downtime and audit findings.

It is a high-level architecture talk from someone with nearly two decades in IT operations (AT&T, Adobe, HP, now SAP), aimed at the people who sign off on production readiness rather than the people tuning learning rates.

## The lab hides the hard parts

Talasila's starting contrast: in the lab the data is clean and the focus is benchmark metrics. In production you meet drift, use cases that keep changing, scalability and latency requirements, and availability targets. Each of those is an infrastructure decision, and each is harder to change once the architecture is locked.

He uses IBM Cloud SoftLayer as a worked example of what to look for in a provider (bare metal and virtual compute, global availability zones, a network backbone tuned for moving large datasets) while keeping the advice provider-neutral: benchmark throughput, IOPS and latency for your own use case before you commit.

## Resilience pillars, in plain terms

**High availability** means multi-zone deployments, load balancing across zones, stateless model servers so a failed instance takes no state with it, fault detection with automated failover, and a defined path back once the zone recovers. **Disaster recovery** means an off-site strategy with air-gapped or immutable backups and a recovery time you have actually checked against what the provider offers. **Rate limits** keep one tenant's unpredictable spike (or a DDoS) from taking down everyone else's real-time serving.

**Zero Trust segmentation** gets the most airtime. Training, QA and production environments are isolated, changes only flow upward after testing and security clearance, serving endpoints sit behind API authentication and rate limiting, and network rules or ACLs are defined up front. Drift management applies to infrastructure too: rate limits, allowed ports and software versions should not change quietly.

## Controls an auditor will ask about

The operational-controls section reads like a checklist for regulated ML: asset management for versions and releases, identity and privileged access management for model registries and pipelines (integrated with your existing directory where you have one), audit logging across training and serving so you can tell what ran where and why it failed, compliance validation for regulated workloads, and automated scanning of container images before they enter a repository.

## Ownership is the missing pillar

The closing argument is about people. Resilience stops being the infrastructure team's job alone and becomes shared across data scientists, ML engineers, MLOps practitioners and platform engineers, with a clear RACI, vendor and change management in the loop, and SLOs for availability, performance and security that you measure and iterate on. The point is that a vendor's maintenance window should never be the first time anyone checks whether a model endpoint is actually highly available.

## Who should watch

Platform and cloud operations leads planning where ML workloads will run, and anyone writing the production-readiness checklist for an ML platform. If you want benchmarks or reference configurations, this is a framework overview rather than a build log.

## Related Conf42 talks

- [Building Resilient ML Cloud Integrations: A Practical Guide to Secure, Scalable, and Cross-Platform Architectures](https://www.conf42.com/Machine_Learning_2025_Naga_Swetha_Kattula_integrations_resilient_cloud) by Naga Swetha Kattula (IEEE) works the same problem from the integration side.
- [Disaster Recovery preparedness using Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) by Kyle Shelton (AWS) shows how to test the DR plan instead of trusting it.
- [5 Levels of High Availability: from Multi-instance to Hybrid Cloud](https://www.conf42.com/Site_Reliability_Engineering_2021_Rafal_Leszko_high_availability_multiinstance_hybrid_cloud) by Rafal Leszko (Hazelcast) is a compact HA primer.

[Watch Srinivas Talasila's talk](https://www.conf42.com/Machine_Learning_2026_Srinivas_Talasila_compliance_governance_ai)

[Watch the talk on YouTube](https://youtu.be/rpNkCUPGb14).

## Watch the talk

[From Reliable Models to Resilient ML Platforms: Designing Secure, Highly Available Infrastructure for Production Machine Learning](https://www.conf42.com/Machine_Learning_2026_Srinivas_Talasila_compliance_governance_ai) at Conf42 Machine Learning 2026.
