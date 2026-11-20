# Healthcare AI where the ledger holds receipts, not patient data

Conf42 Blog, 2025-08-22, updated 2026-11-09. https://www.conf42.com/blog/platform2025/healthcare-ai-ledger-holds-receipts-not-patients

In short: Kedar Mohile at Conf42 Platform Engineering 2025 on federated learning plus a permissioned ledger for privacy-first healthcare AI platforms.

The best training data in healthcare is the data nobody is allowed to move. At Conf42 Platform Engineering 2025, Kedar Mohile, a data protection strategist in healthcare at Amazon, presenting his own views and research rather than his employer's, laid out a platform design that moves the model to the data and puts only the proof of what happened on a permissioned ledger. No patient record ever touches the chain.

## The privacy paradox, stated plainly

Kedar opens with the bind every healthcare ML team knows. Models get better with richer data, and the richest datasets sit behind HIPAA, GDPR and competitive walls. Anonymisation is weaker than people hope: he points to cases where supposedly anonymised DICOM scans and clinical notes could be linked back to patients through auxiliary data. Centralising everything creates one big breach target. His answer is to stop moving data at all and bring computation and proofs to where the data lives.

The data itself is fragmented too: EHRs in Epic or Cerner, imaging in PACS, genomics in research silos, trial data with pharma. Rather than building giant central extractors, he argues for thin, standardised adapters running inside each institution. They translate local formats into the minimal features training needs, enforce local policy and emit cryptographic proofs. Tolerating heterogeneity, in his framing, makes the system more resilient to schema drift than trying to erase it.

## Blockchain as an audit log with opinions

When Kedar says blockchain he means a permissioned ledger shared between institutions, not a public chain or a token. What goes on it are trust events: which site trained, when, under which consent policy, with which differential privacy budget and which model lineage. When an auditor asks you to prove a model never saw a disallowed cohort, the ledger is the tamper-evident answer.

The design rules are strict: store only hashes and references, rotate keys with hardware-backed identities, and let smart contracts encode regulatory gates. One example he gives is a contract that rejects a model update if the site's privacy budget is exhausted. With tens of participants rather than millions, he suggests PBFT-style consensus fits better than anything proof-of-work shaped. It also has to survive hospital reality: firewalls, intermittent links and strict change control.

## Naive federated learning leaks

Federated learning flips the usual flow, since hospitals train locally and send updates back. Kedar is blunt that the naive version is a false sense of security: raw gradients can reveal training examples and malicious clients can poison the model. The fix is a stack, not a single tool. Secure aggregation so the server never sees individual updates, differential privacy at the edge, robust aggregation on the server, and attestation that every site runs the approved training binary. Zero-knowledge proofs, homomorphic encryption and secure multi-party computation come in where the risk warrants their cost. His default starting point is differential privacy plus secure aggregation, layering heavier tools only where regulators or the data class demand it.

## Compliance as a build artefact

The platform-engineering part of the talk is the CI/CD story. Every code change and training run gets checked automatically; the pipeline enforces privacy budgets, generates model cards and lineage, and fails the build when a run violates policy. By audit time the evidence package already exists. Monitoring follows the same rule: privacy-preserving telemetry, update-magnitude checks to catch poisoning, and automated quarantine of a misbehaving site rather than a human triaging it at 2am.

He closes with a four-phase rollout: ledger and adapters first, then a low-risk pilot such as readmission prediction, then more sites, and only then high-stakes clinical workloads. Smaller hospitals need turnkey edge nodes, or they drop out.

## Who should watch

Platform and security engineers building ML infrastructure across organisational boundaries, in healthcare or anywhere data cannot leave its owner. It's an architecture talk rather than a demo, so bring your own whiteboard.

## Related Conf42 talks

- [Ethical AI in Healthcare: Bias, Privacy, and Trust in Kube-Native Systems](https://www.conf42.com/Kube_Native_2025_Venus_Garg_ethical_ai_trust) by Venus Garg (Boston University), the bias side of the same trust problem.
- [API-Led Healthcare Transformation: Enhancing Interoperability, Diagnostics & Personalized Medicine with MuleSoft](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability) by Venugopal Reddy Depa (CRH Americas Materials), on the integration layer Kedar's local adapters have to plug into.

[Watch Kedar Mohile's talk](https://www.conf42.com/Platform_Engineering_2025_Kedar_Mohile_enabled_privacy_blockchain)

[Watch the talk on YouTube](https://youtu.be/_4aEWfnbKwA).

## Watch the talk

[Building Privacy-First Healthcare AI Platforms: A Blockchain-Enabled Architecture](https://www.conf42.com/Platform_Engineering_2025_Kedar_Mohile_enabled_privacy_blockchain) at Conf42 Platform Engineering 2025.
