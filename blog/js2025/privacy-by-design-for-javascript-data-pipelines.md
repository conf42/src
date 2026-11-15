# Privacy by design for JavaScript data pipelines, layer by layer

Conf42 Blog, 2025-10-24, updated 2026-11-09. https://www.conf42.com/blog/js2025/privacy-by-design-for-javascript-data-pipelines

In short: Meta data engineer Vivekananda Chittireddy showed at Conf42 JavaScript 2025 how k-anonymity, differential privacy and tokenisation fit JS stacks.

Three attributes, zip code, date of birth and gender, are enough to identify most people in the US, which is why "we removed the names" isn't anonymisation. At Conf42 JavaScript 2025, Vivekananda Chittireddy, a data engineer at Meta, showed how to build privacy into JavaScript data systems from the browser to the analytics layer, with the techniques that actually hold up: k-anonymity, differential privacy, tokenisation and a five-layer architecture.

He's clear that this is his own experience building privacy-aware systems, not a description of how Meta does it.

## The four principles, applied to code

He frames privacy by design with four principles: be proactive, not reactive; make maximum privacy the default without waiting for users to opt in; build privacy into the design from day one instead of bolting it on; and keep full functionality, because a private product nobody can use helps no one. For JavaScript developers that means controls at every stage, from client-side collection through Node.js backends to processing and analytics.

## Techniques that survive contact with an attacker

- **K-anonymity**: every record looks identical to at least k-1 others on identifying fields. With k of 5, any individual blends in with four others.
- **L-diversity**: each of those groups also needs varied sensitive values. If every patient in a group has the same diagnosis, being hidden in the group protects nothing.
- **Differential privacy**: add calibrated noise to query results so that any one person's presence barely changes the output. He suggested epsilon values between 0.1 and 1.0 as the practical range, and pointed to Node.js libraries that can apply local differential privacy in the browser.
- **Pseudonymisation and tokenisation**: replace identifiers like social security numbers with internal IDs that keep joins working, or with random tokens mapped in a separate vault, so the analytics pipeline never touches real PII.

For the ambitious, he covered homomorphic encryption (computing on data without decrypting it) and secure multi-party computation, where several organisations compute over combined data without seeing each other's records.

## Two case studies

In healthcare, a consortium wanted medical research across institutions without exposing patient data. Using JavaScript-based federated learning with differential privacy, records stayed on hospital servers, models trained locally, and only differentially private updates were shared, keeping the setup within HIPAA and GDPR.

In financial services, card details were tokenised at the point of collection, so real-time fraud detection ran on streaming pipelines without seeing card numbers, while behaviour analytics used k-anonymous cohorts of 25 to 50 people.

## A five-layer blueprint

1. **Collection**: consent management, minimal scope, pseudonymise immediately using browser APIs.
2. **Storage**: encrypt at rest, keep identifying data in separate databases from transactional data, strict access controls between them.
3. **Processing**: differential privacy on queries, secure enclaves for sensitive operations, aggregate instead of working per user.
4. **Analytics**: insights only from de-identified data, with full audit trails for breach investigations and certifications.
5. **Access**: role-based access, purpose limitation and least privilege.

Tools: Node.js's built-in `crypto` module, JSON Web Tokens for token handling, and the browser's SubtleCrypto API for client-side encryption.

## The pitfalls list is the part to print

PII in plain-text logs (one stack trace with user data undoes the rest). Treating MD5 hashes or sequential IDs as anonymisation, when they're trivially reversible. Collecting everything just in case. Privacy controls only on the client, where any developer with devtools can bypass them. And keeping data forever, which conflicts with GDPR and California privacy law and makes any breach more expensive.

## Who should watch

Node.js and data engineers handling user data in regulated sectors, and anyone who has to argue for privacy work in a design review. It's a broad overview with real techniques; you'll still need the library docs to implement them.

## Related talks

- [Privacy by Design for DevOps: Building Scalable, Secure, Regulation-Ready Data Systems](https://www.conf42.com/DevOps_2026_Vivek_Chittireddy_privacy_regulation_security) brings the same principles to DevOps pipelines.
- [Building Privacy Aware Infrastructure](https://www.conf42.com/Platform_Engineering_2024_Natalia_Grybovska_privacy_aware_infrastructure) looks at the platform layer.
- [Advanced Security Strategies for Protecting PII in Cloud Environments](https://www.conf42.com/Golang_2025_Sharath_Chandra_Adupa_security_pii_cloud) covers PII protection from a Go backend's view.

[Watch Vivekananda Chittireddy's talk](https://www.conf42.com/JavaScript_2025_Vivekananda_Chittireddy_privacy_design_building)

[Watch the talk on YouTube](https://youtu.be/-Y3ZT7KfZyk).

## Watch the talk

[Privacy by Design for JavaScript Data Systems: Building Secure and Compliant Architectures](https://www.conf42.com/JavaScript_2025_Vivekananda_Chittireddy_privacy_design_building) at Conf42 JavaScript 2025.
