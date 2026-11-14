# A consent checkbox stored as a boolean won't survive an audit

Conf42 Blog, 2026-04-10. https://www.conf42.com/blog/cloud2026/consent-is-a-record-not-a-checkbox

In short: Manasa Uppula at Conf42 Cloud Native 2026 on designing financial onboarding as evidence: append-only consent, propagated identity assurance, audited sagas.

Most onboarding flows store consent as a boolean and call it done. At Conf42 Cloud Native 2026, [Manasa Uppula](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime), an enterprise web architect with nearly 14 years on large financial platforms, argued that this is exactly where regulated systems fail: the record exists, but it can't prove what the customer saw, when, and in what system state.

It's a compact talk, about 15 minutes, built around one framework and a worked example.

## Storing data versus proving what happened

Onboarding is where the legal relationship starts. You set consent boundaries, grant access to regulated services, and create a record a regulator might read years later. Uppula's point is that regulators have moved on from whether you collected the data to how a disclosure was presented, which version the customer saw, and what the system state was at that exact moment. KYC, AML, GDPR, CCPA and E-SIGN each turn into a specific architectural obligation. Her line: "The system must be able to prove what happened, not just store data."

The common failure she describes is compliance as surface: checkboxes and form validation on top of mutable database state, with exception paths as an afterthought. Every service ends up with its own version of what happened, and audits turn into manual reconstruction under pressure.

## Interaction integrity in three pillars

Her approach, which she calls interaction integrity, makes every material interaction produce verifiable evidence as a first-class output:

- **Consent and disclosure as artifacts.** Each disclosure event carries the disclosure version, a timestamp, the user's explicit response and the system state. Events go into append-only logs (she names Apache Kafka) backed by immutable storage. Nothing is updated; everything is appended.
- **Progressive identity assurance.** Verification is gradual: email, then document upload, maybe biometrics. Low-risk access comes early and higher capabilities open as confidence grows. In microservices, the trap is stale identity state in some services. Her fix is to carry the assurance level as a JWT claim and emit an event when verification succeeds, so downstream services update their enforcement instead of guessing.
- **Exception handling as compliance.** Session timeouts and a third-party KYC provider going down are not edge cases; they happen every Tuesday. A half-finished flow leaves legal ambiguity about whether the customer is onboarded at all. So she uses saga patterns with compensating transactions, orchestrated by AWS Step Functions or Temporal, and logs every failure path with the same rigour as the happy path.

## The savings account walkthrough

The example ties it together. A customer reads the terms and GDPR disclosure, and each view is an immutable event. Email verification grants low-risk access. An ID upload raises the assurance level in the JWT claims, which enables funds transfer. Then the KYC provider times out: the saga fires a compensating transaction, partial state is preserved, the customer gets a clear notification, and both the cause and the resolution are logged. No gap for an auditor to fall into.

## Governance has to change with the system

Her last point is the one platform teams tend to skip. Cloud-native systems change constantly, and every service update or migration is a chance for compliance to erode quietly. Treat compliance as an explicit, versioned architectural input, not something each team is assumed to preserve.

## Who should watch

Architects and backend engineers building onboarding, KYC or any consent-heavy flow in a distributed system. If your consent table has an `UPDATE` statement anywhere near it, this is worth 15 minutes.

## Related Conf42 talks

- [An Introduction to Saga Pattern for Distributed Transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) by Dmitry Khorev at Conf42 Cloud Native 2023.
- [Cloud-Native Insurance: Real-Time Underwriting & Enrollment at Kubernetes Scale](https://www.conf42.com/Kube_Native_2025_Gurucharann_Visagamurthy_insurance_enrollment_realtime) by Gurucharann Visagamurthy at Conf42 Kube Native 2025.
- [Kube-Native AI Data Governance for Scalable Compliance in Modern Banking](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance) by Ashish Dibouliya at Conf42 Kube Native 2025.

[Watch Manasa Uppula's talk](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime) or the [YouTube recording](https://youtu.be/cUGDWydSqEw).

## Watch the talk

[Designing Compliant Digital Onboarding: Cloud-Native Architectures for Trustworthy, Audit-Ready Financial Services](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime) at Conf42 Cloud Native 2026.
