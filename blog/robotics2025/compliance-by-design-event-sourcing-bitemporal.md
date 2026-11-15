# Build compliance into the data model, not the audit week

Conf42 Blog, 2025-10-27, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/compliance-by-design-event-sourcing-bitemporal

In short: Sneha Nallapu of J.B. Hunt at Conf42 Robotics 2025 on compliance-by-design with event sourcing, bitemporal data, graph lineage, CQRS and ABAC.

Most compliance work arrives after the system is built, as a late patch with a deadline attached. At Conf42 Robotics 2025, Sneha Nallapu, Senior Software Engineer at J.B. Hunt Transport Services, argued for the opposite: pick architecture patterns that make a system auditable by construction, so regulation becomes a design input like security or scalability.

It's a compact pattern catalogue aimed at automated financial systems, and every pattern on it is something you can put on a whiteboard on Monday.

## Event sourcing is a diary you never edit

The first of three foundational patterns is event sourcing: every change captured as an event, never overwritten. Sneha's analogy lands: "It's like keeping a diary instead of editing yesterday's entry." Technically that means an append-only log with replayable history and cryptographic integrity. For a regulator it means full traceability and non-repudiation, because nothing gets quietly deleted.

## Two clocks beat one

The second pattern, bitemporal modelling, keeps two timelines for every fact: when something happened in the real world and when the system recorded it. With both, you can reconstruct what was true at any moment and what you believed at that moment, even after corrections. Anyone who has had to explain what a report showed before last month's backfill knows why this matters.

## Lineage as a graph, not a spreadsheet

The third is graph-based lineage. Nodes and edges map how data moves across microservices, so an auditor can trace a reported number back to its source and an engineer can see what a schema change will break before shipping it.

## Separate the writes, label the readers

On top of the foundation, Sneha adds three more patterns:

- **CQRS.** The command side validates transactions and enforces rules; the query side is tuned for audits, monitoring and reporting. Accuracy and read speed stop fighting over the same tables.
- **ABAC.** Attribute-based access control decides on user attributes, data sensitivity and context in real time. Her example: an analyst in Europe can see European data under GDPR while a contractor gets a narrower view. Policies are declarative, which also makes them auditable.
- **Adaptive exception handling.** Reinforcement learning watches compliance exceptions, picks responses and improves over time, so recurring issues shrink as rules change.

## Don't adopt all six at once

The most useful slide may be the effort map. Event sourcing and CQRS are heavy lifts; ABAC and bitemporal models are lighter. So the roadmap is phased: assess gaps and map current obligations, design around the core patterns, pilot one domain, then scale. Starting with the cheap patterns gets you evidence that the expensive ones are worth it.

## Who should watch

Engineers building ledgers, payment flows, trading or logistics systems under regulation, and architects who get asked to prove what happened more often than they'd like. It's an overview, so expect breadth across six patterns rather than code for any one of them.

## Related Conf42 talks

- [Joao Marques: Adding Tamper-Evident Audit Trails to AI Agents](https://www.conf42.com/MLOps_2026_Joao_Marques_audit_tamper_agents) applies the append-only idea to agents.
- [Manasa Uppula: Designing Compliant Digital Onboarding](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime) covers audit-ready architecture for financial services.
- [Arpita Sheth: Compliance as a Pipeline Stage](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline) moves governance checks into the ML pipeline.

[Watch Sneha Nallapu's talk](https://www.conf42.com/Robotics_2025_Sneha_Nallapu_compliance_design_finance)

[Watch the talk on YouTube](https://youtu.be/zJ216IULjYs).

## Watch the talk

[Demystifying Compliance-by-Design: Architecting Regulatory-Resilient Robotics and Financial Systems](https://www.conf42.com/Robotics_2025_Sneha_Nallapu_compliance_design_finance) at Conf42 Robotics 2025.
