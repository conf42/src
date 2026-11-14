# In regulated platforms, consent is a system event, not a checkbox

Conf42 Blog, 2026-05-15, updated 2026-11-09. https://www.conf42.com/blog/golang2026/evidence-centric-compliance-architecture

In short: Manasa Uppula at Conf42 Golang 2026 on evidence-centric compliance for financial onboarding, with versioned consent, assurance levels and sagas.

When a regulator asks what a customer agreed to three years ago, the answer should be a query, not a three-week dig through logs and old Confluence pages. At Conf42 Golang 2026, Manasa Uppula, an enterprise web architect at Virtusa, laid out an evidence-centric compliance architecture for customer-facing financial platforms, where the system produces its own proof as a normal output.

Manasa draws on nearly fourteen years building customer-facing platforms at US financial institutions, including Bank of America, Citigroup, Fidelity and BNY Mellon, and the talk has the specificity of someone who has sat in the audit room.

## Compliance is continuous, so evidence has to be too

Her opening point: oversight is not an annual checklist. A regulator, a customer dispute or an investigation can start any day, and the expectation is an immediate, complete answer. Digital onboarding is where it matters most, because that is where the legal relationship, consent boundaries and access to regulated services are created. In her framing, a misdisclosure is not a bug; it is a compliance event.

The anti-pattern she names is compliance as an afterthought, or as a surface layer of UI checkboxes and modals. A checkbox can be skipped, broken or shipped in a version that records nothing. She has seen exactly that: the UI looked right, and when the audit question came there was no reliable record of what the customer had agreed to.

## Every obligation gets an architectural counterpart

The core of the talk is a mapping exercise. Informed consent becomes a consent step embedded in the flow, which the system cannot proceed past without. Disclosure at the point of decision becomes an API that enforces the disclosure before the action can run, not merely before it should. Explanation becomes a decision trail generated at runtime. Record retention becomes an immutable, append-only event store per interaction.

She ties this together as interaction integrity, built on three pillars.

**Consent and disclosure as artifacts.** Each consent record carries the exact disclosure version shown, when it was presented, the user's explicit response, and the system state at that moment. Disclosures are versioned and addressable, never overwritten. The sequence is strict: disclose, acknowledge, act, never in parallel. Or, in her words, "Consent is not a checkbox. It is a system event." This is the difference she draws between a log, which records what happened, and evidence, which can prove it under scrutiny.

**Progressive identity assurance.** Identity is a risk level that builds up, not a pass-fail gate. The assurance level travels explicitly in the auth context on every service call, and verification events (an ID upload, say) update what downstream services allow. For Go developers she makes it concrete: pass it as a typed value in your context, validate it at each boundary, and never assume someone upstream checked it.

**Exception handling and continuity.** Networks drop and KYC providers time out. When services disagree about where a customer is in onboarding, you get a legally ambiguous state. Her fix is saga orchestration with compensating transactions: pause the session, preserve progress, notify the customer, and log the failure, the compensation and the resolution with the same rigour as the happy path.

## Auditability and traceability are different tests

Auditability means reconstructing key events on demand from structured, immutable, complete records that auditors can retrieve themselves. Her practical test: if your auditors need an engineer to extract the evidence, you have logs, not auditability. Traceability is the link from regulation to design control to observed behaviour, so you know which controls apply when you launch a product or region.

The reference stack is named per property: Kafka and S3 Object Lock for immutable consent records, OAuth, JWT claims and SPIFFE/SPIRE for identity, AWS Step Functions, Conductor or Temporal (which she notes has excellent Go support) for sagas, and OpenTelemetry, Elasticsearch and CloudTrail for audit logs. A savings-account walkthrough runs all three pillars end to end.

## Who should watch

Architects and backend engineers in fintech, insurance or any regulated onboarding flow. Her rollout advice is sensibly small: map obligations to interactions, translate them into constraints, instrument evidence, test auditability in CI like any feature, govern changes, and start with the single flow that would worry you most if a regulator asked about it tomorrow.

## Related Conf42 talks

- [Karishma Velisetty on governance and audit for AI assistants](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants) at Conf42 LLMs 2026
- [Pooja Ranjan on compliance and SaaS governance](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance) at Conf42 DevOps 2026
- [Pratik Patel on AML compliance workflows](https://www.conf42.com/Prompt_Engineering_2026_Pratik_Patel_aml_compliance_workflows) at Conf42 Prompt Engineering 2026

[Watch Manasa Uppula's talk](https://www.conf42.com/Golang_2026_Manasa_Uppula_designing_defensibility_evidence)

[Watch the talk on YouTube](https://youtu.be/2Tps70QDe2o).

## Watch the talk

[Designing for Defensibility: Evidence-Centric Compliance Architecture in Customer-Facing Financial Platforms](https://www.conf42.com/Golang_2026_Manasa_Uppula_designing_defensibility_evidence) at Conf42 Golang 2026.
