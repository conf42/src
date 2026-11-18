# Getting patients to appointments by wiring Epic to Uber and Lyft

Conf42 Blog, 2025-09-02, updated 2026-11-09. https://www.conf42.com/blog/platform2025/epic-ehr-rideshare-integration-for-patients

In short: Sai Sharan Reddy Mittapelly at Conf42 Platform Engineering 2025 on a HIPAA-compliant link from Epic EHR to rideshare APIs, with provider failover.

One in five patients in the United States misses or delays care because they have no reliable way to get there, and for a dialysis or chemotherapy patient a missed appointment is not a scheduling nuisance. Sai Sharan Reddy Mittapelly, a healthcare integration engineer with ten-plus years in the field (he mentioned Henry Ford Health as his current employer), spent his Conf42 Platform Engineering 2025 talk on the platform that connects Epic EHR scheduling to Uber and Lyft so the ride is booked with the appointment.

It is a nice change from yet another generic microservices talk: the domain constraints are unusual, the failure mode is a patient not getting treatment, and the architecture decisions follow directly from that.

## Two APIs that were never meant to meet

On one side sits Epic, speaking SMART on FHIR: REST APIs carrying patient data as JSON or XML resources, replacing the older HL7 v2 and v3 messages. On the other side, rideshare APIs designed for consumers: quick pickups, arrival estimates, and no built-in compliance for medical data. The integration layer between them is, in Sai's description, a translator and a security guard combined.

## The three hard problems

**Bidirectional flow.** Epic shares appointment details; the rideshare side sends back driver location, ETA and drop-off confirmation. Both systems, and the patient's app, need to stay in sync throughout.

**Provider failover.** If Lyft goes down, the system switches to Uber without the patient noticing, the way a GPS reroutes you around a closed road. Care does not wait for a vendor's status page to turn green.

**HIPAA in every request.** Each ride request carries more than 47 sensitive fields: patient name, appointment type, pickup address, notes and mobility needs. Every one must be encrypted, logged and auditable.

## The architecture that follows

The platform splits into microservices (Epic integration, transport orchestration, a provider gateway, patient profiles and compliance) around a Kafka event bus. Kafka carries transport requests and their state changes, appointment updates from Epic, driver location and ETA updates, and compliance audit events. PostgreSQL handles the transactional side: the ride registry, billing reconciliation, compliance documentation and configuration. A cache holds patient transport profiles, so details like wheelchair access are on hand instantly.

Sai's hospital analogy works: separate wings for emergency, lab and radiology, each with its own team, connected by secure hallways. During flu season the ride-matching service scales up without dragging the rest of the system along.

It runs on Kubernetes across multiple AWS regions with predictive autoscaling driven by historical clinic load, active-active clusters, and canary deployments. Security is zero trust: rotating tokens, AES-256 encryption, OAuth 2 with PKCE, TLS and a web application firewall.

## Monitor the clinic, not just the cluster

The most transferable idea is the split in observability. If an API slows down, that is an IT problem. If a dialysis ride is late, that is a clinical problem that could harm a patient, and it should page a different team. So they define custom SLOs tied to medical schedules, not just latency percentiles.

There is an ML layer too: a pipeline from data collection through feature engineering to monitored deployment, with the healthcare caveats of incomplete data and the need for clinicians to understand recommendations. His example is a model that learns a patient often cancels Monday-morning rides and schedules a backup plus a reminder. He credits AI with cutting no-shows by 42%, and describes a Chicago hospital where dialysis patients had been missing appointments because of transport: after the integration, no-shows fell, patients were happier, and clinicians got back about 20 hours a month of manual transport coordination. The transcript is a bit tangled on the exact percentages for that case, so watch the slides for the figures.

## Who should watch

Engineers working on healthcare integrations, and anyone building a platform where an outage has a human cost and SLOs need a domain meaning. His closing line sums up the stance: in healthcare, uptime is a lifeline.

## Related Conf42 talks

- [Venugopal Reddy Depa on API-led healthcare interoperability with MuleSoft](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability), the integration layer from the API-management side.
- [Geetha Sharanya Bolla (Apexon) on healthcare access with data integration and microservices](https://www.conf42.com/Kube_Native_2025_Geetha_Sharanya_Bolla_healthcare_integration_scalable), a sibling architecture.
- [Akshay Pratinav (Intuit) on predictable failover across the stack](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads), for the failover mechanics in depth.

[Watch Sai Sharan Reddy Mittapelly's talk](https://www.conf42.com/Platform_Engineering_2025_Sai_Sharan_Reddy_Mittapelly_mobility_rideshare_epic)

[Watch the talk on YouTube](https://youtu.be/G4UG39WMxqc).

## Watch the talk

[Building Resilient Healthcare-Mobility Platforms: Engineering Epic-Rideshare Integration at Scale](https://www.conf42.com/Platform_Engineering_2025_Sai_Sharan_Reddy_Mittapelly_mobility_rideshare_epic) at Conf42 Platform Engineering 2025.
