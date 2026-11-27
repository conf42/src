# Privacy observability means answering who touched this data, and why

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observability-for-privacy-infrastructure-meta

In short: Krishna Ganeriwal of Meta at Conf42 Observability 2025 on lineage, consent propagation and audit trails for privacy infrastructure at hyperscale.

In most systems observability answers "is it up and is it fast?". In privacy infrastructure it has to answer something harder: who touched this user's data, why, and were they allowed to? At Conf42 Observability 2025, Krishna Ganeriwal, an engineer on Meta's ads privacy infrastructure team, explained why that question makes observability foundational to privacy-aware systems at hyperscale, and which architectural patterns make it answerable.

## A black box recorder for every interaction

Krishna defines privacy observability as the ability to reconstruct a privacy black box recording for every interaction with user data. The stakes are regulatory, with GDPR, CCPA and India's DPDP in play and fines that can reach 4% of global revenue, but he argues trust matters more than fines. Users stop using services that cannot tell them what happened to their data.

## Five questions you need to answer daily

The use cases he walks through are the heart of the talk:

- **Data lineage**: where user data was generated, who processed it, whether it was shared externally.
- **Consent propagation**: when a user revokes consent in one UI, every system must respond, in real time. His example: a user who allowed location for personalised ads and later turns it off. Wherever that location data fed models or training, it has to be wiped. One lagging cache is enough for a compliance failure.
- **Purpose limitation**: data collected for personalisation must not quietly feed targeting or model training without explicit consent.
- **Anomaly detection**: a login from a new location or a sudden access to full history; is that expected, or a policy mismatch?
- **Policy drift**: over time, does enforcement silently bypass updated constraints?

None of these can be answered from uptime dashboards.

## Speed, scale and secrecy at once

The design challenges stack up. Volume means billions of log events a day and petabytes of data. Speed means sub-second processing, because the services behind it are real-time. Granularity means tracking per user, sometimes per impression, since every user's privacy settings differ. And security: the observability data itself describes how users interacted with the system, so it must never leak personally identifiable information. Krishna's summary is that you have to design for speed, scale and security simultaneously.

## Four patterns from production

The architecture section names patterns he says privacy teams across big tech run in production:

1. **Event-driven lineage**: Kafka or another pub-sub system tracks data flows as they happen.
2. **Consent-aware tagging**: each payload is tagged with the purposes and scopes allowed to consume it, so location data can be marked as off limits to ads systems but usable elsewhere.
3. **Embedded policy engines**: runtime guards check that every access matches consent.
4. **Cryptographic audit trails**: Merkle trees or blockchain-style structures for immutable, verifiable logs.

At Meta, lineage systems track data across thousands of internal sources, consent status travels with the data, and policy engines enforce compliance along the way. Auditors, legal and engineering use the same real-time views of how data moves. Krishna reports a 40 to 50% reduction in audit prep time across several internal teams where this was applied well.

## What it buys and what is still open

Beyond faster audits and lower fine risk, he lists two benefits engineers will appreciate: developers can finally see how their own systems handle data, and only compliant data reaches downstream ML models. The open problems are just as interesting. Can ML detect privacy anomalies in real time? Can a system be observed and enforce policy at once? And should policy observability get a standard, the way OpenTelemetry standardised traces? Right now there is none. His closing line works as a slogan: "If you can't see it, you can't enforce it."

## Who should watch

Engineers building data platforms that touch personal data, and anyone who has had to answer a data subject access request by hand. It is an architecture talk without code, but the use-case list makes a good checklist for your own system.

## Related Conf42 talks

- [Natalia Grybovska on building privacy-aware infrastructure](https://www.conf42.com/Platform_Engineering_2024_Natalia_Grybovska_privacy_aware_infrastructure) at Conf42 Platform Engineering 2024.
- [Mary Sirisha Duggimpudi on AI-driven sensitive data discovery for privacy compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) at Conf42 DevSecOps 2026.
- [Arun Vivek Supramanian on ethical data engineering, privacy and fairness](https://www.conf42.com/Machine_Learning_2025_Arun_Vivek_Supramanian_privacy_engineering_ethical) at Conf42 Machine Learning 2025.

[Watch Krishna Ganeriwal's talk](https://www.conf42.com/Observability_2025_Krishna_Ganeriwal_privacy_infrastructure)

[Watch the talk on YouTube](https://youtu.be/VtyToTO8cRM).

## Watch the talk

[Observability in Privacy Infrastructure: Building Trustworthy and Compliant Software Systems at Scale](https://www.conf42.com/Observability_2025_Krishna_Ganeriwal_privacy_infrastructure) at Conf42 Observability 2025.
