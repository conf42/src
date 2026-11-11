# Sensitive data discovery has to run as often as your schema changes

Conf42 Blog, 2026-09-16, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/sensitive-data-discovery-continuous-not-audits

In short: At Conf42 DevSecOps 2026, T-Mobile's Mary Sirisha Duggimpudi layers metadata, ML and runtime telemetry into continuous PII discovery.

A compliance inventory is a photograph of a system that keeps moving. At Conf42 DevSecOps 2026, Mary Sirisha Duggimpudi, Senior Software Engineer at T-Mobile USA, laid out a layered design for finding sensitive data continuously, and for turning each finding into a ticket, a policy check or a blocked promotion instead of a line in next year's audit.

## The audit snapshot is already stale

Her starting point is familiar to anyone who has owned a data platform. Regulated data does not sit in one control database. It leaks into object storage, analytics platforms, SaaS APIs, temporary tables created during a migration, and, most often forgotten, logs. One careless debug line and a customer identifier is now flowing into the observability stack.

She names two gaps. The visibility gap: an audit captures one moment, while containers, datasets and schemas change in hours. The ownership gap: the security team spots the risk, but only the application team knows what the field means for the business. Discovery that ignores either one produces findings nobody can act on.

## Read the metadata before you read the rows

The design stacks independent signals rather than trusting one scanner. Layer one is metadata intelligence, and her phrase for it is "signal before sampling". A column called customer SSN tells you plenty without reading a million rows. Schema fingerprints match structures that resemble previously classified ones. Lineage flags derived tables that probably inherited their parent's sensitivity. Access patterns reveal stores that suddenly receive sensitive traffic.

The point is cost. Metadata is cheap, so it decides where the expensive deep scans go first.

Layer two is classification, and she is firm that it is not a choice between AI and rules. Regex and validation algorithms catch Social Security numbers, card numbers and IBANs with high precision. ML classifiers add context when values are masked or encoded oddly. NLP entity detection covers the free text in support tickets, comments and JSON blobs. Confidence scores then route work: a 99% finding and a 65% finding should not land in the same queue.

Layer three is runtime telemetry: API traces showing sensitive fields crossing service boundaries, query logs exposing shadow access paths, and continuous checks on application logs. Her example is the classic regression: masking works today, a dependency bump disables it tomorrow, and only runtime validation notices.

## Explainability is an adoption requirement

The sharpest part of the talk is about trust. A platform that raises hundreds of alerts a day, half of them wrong, trains engineers to ignore it. So every finding should carry its evidence: which pattern matched, which metadata contributed, the model's confidence, what was sampled. High-confidence findings can be remediated automatically, medium ones go to a human, and the human's verdict feeds back into the classifier.

She also walks through schema drift as a four-step loop: detect the change from DDL logs or catalog events, classify the new columns, assign the finding to an owner from metadata, and govern it with policy as code. A developer adding a date-of-birth field ships working code and a changed privacy risk profile in the same commit. The architecture catches the second part near the moment it happens.

## Findings that do something

Discovery only matters when it drives action. Findings open Jira or GitHub issues with evidence and a remediation SLA. OPA or Sentinel enforce requirements before deployment, Vault or KMS integrations validate encryption, and the same pipeline assembles evidence packages for auditors. She maps four control points onto delivery: pre-commit hooks, pull request schema diffs, deployment gates that demand classification, encryption attestation and a retention label, and post-deployment drift detection.

Her trade-offs are honest. Full content scanning costs more than metadata triage. In regulated environments she would rather favour recall and spend human review on the ambiguous cases. And she is careful to say automation does not make an organisation compliant; it gives continuous visibility and evidence that support compliance.

## Who should watch

Platform and data engineers being asked for a PII inventory, and security teams whose discovery tool has become an alert firehose. It is an architecture talk with no product pitch, so expect patterns rather than a demo.

## Related Conf42 talks

- [Vivek Chittireddy on privacy by design for DevOps](https://www.conf42.com/DevOps_2026_Vivek_Chittireddy_privacy_regulation_security), the build-time side of the same problem.
- [Natalia Grybovska on building privacy-aware infrastructure](https://www.conf42.com/Platform_Engineering_2024_Natalia_Grybovska_privacy_aware_infrastructure).
- [Pooja Ranjan on automating continuous compliance for SaaS delivery](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance), for the evidence half of the story.

[Watch Mary Sirisha Duggimpudi's talk](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance)

[Watch the talk on YouTube](https://youtu.be/b11L3jcL0Fk).

## Watch the talk

[AI-Driven Sensitive Data Discovery for Secure DevSecOps and Privacy Compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) at Conf42 DevSecOps 2026.
