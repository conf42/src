# Signed receipts, not logs, as evidence for high-risk AI pipelines

Conf42 Blog, 2026-06-17, updated 2026-11-09. https://www.conf42.com/blog/llms2026/signed-receipts-for-high-risk-ai-pipelines

In short: Neeraj Kumar Singh Beshane of Meta at Conf42 LLMs 2026 on RuntimeGuard-AI, which uses hash-chained signed records and zero-knowledge proofs for AI compliance.

If the team that built the AI system also controls the logs that describe what it did, an auditor can only trust them, not verify them. Neeraj Kumar Singh Beshane, Staff Software Engineer at Meta, built his Conf42 Large Language Models 2026 talk around that gap and presented RuntimeGuard-AI, a design that turns each consequential decision in an AI pipeline into a signed, hash-chained receipt, with zero-knowledge proofs for when the details cannot be disclosed. The abstract frames it as provable EU AI Act compliance for high-risk systems.

His line for the whole talk: "immutable log is a testimony, a verifiable receipt is an evidence."

## The threats are old, the speed is new

Beshane refuses to treat AI as a brand-new risk category. The losses he sees are still credential abuse, phishing, misconfiguration, ransomware and data in the wrong place. What changes is autonomy (agents act without confirmation), velocity (thousands of actions before anyone notices) and tool access (systems humans cannot reach through normal channels). A compromised or prompt-injected agent fails faster and wider than a human would.

So the goal is not more logging. It is verifiable evidence at the moment delegated authority is used.

## It records controls, it does not replace them

He is explicit about scope. RuntimeGuard-AI does not replace IAM, patching, network isolation, prompt defenses, sandboxing or human oversight. If those are weak, the cryptography will faithfully record a badly secured system behaving badly. It runs as a vertical rail through three layers (cyber hygiene, AI and application security, governance) and asks one question at each: when a control made a consequential decision, did that decision become a structured, signed, verifiable event?

## Identity and delegation, signed at every hop

For agents, the unit of governance is the acting machine identity and its delegated authority, not the prompt. Running agents under shared accounts is fast and a dead end after an incident. His model gives each meaningful agent a distinct identity tied to an accountable human owner, a scoped delegation token tied to a purpose, risk tier, data class and expiry, and a runtime authorization check.

In multi-agent pipelines, "trust is not transitive". Identity and authorization context travel with the request, but each downstream component revalidates them, the same way microservices each authenticate a call. Every handover emits a record.

Governance documents get the same treatment. The decision-rights matrix becomes a delegation digest inside the execution token; the constraint catalog becomes a versioned policy. Asked whether a constraint was enforced on a transaction, the answer is a receipt with policy version, verdict, signer and chain pointer, not a wiki screenshot.

## Keep cryptography off the hot path

The obvious objection is latency. The design splits paths. Inline, a Rust policy engine in the gateway issues a verdict (approve, deny, escalate for human review, block); he reports a prototype latency overhead in the range of 2.3 to 4.1 percent. Then a non-blocking dispatch hands a compact record to a background attester that hash-chains it, builds the Merkle tree, signs checkpoints and generates Groth16 proofs. The roughly 1.4 seconds of prover time he quotes is compute cost in the background, not inference latency.

Receipts carry digests rather than raw prompts, customer data or model configuration. Private details sit in Merkle leaves; the root is a compact fingerprint that can be anchored externally. Edit one record and the digests stop matching: tamper-evident, which he is careful to distinguish from tamper-proof. He adds a caveat worth repeating: a zero-knowledge proof shows the encoded policy ran, not that the policy is good, fair or legally sufficient.

## Tiers, and a verifier you actually run

Not every workflow deserves the full stack. Low-risk internal assistants get distinct agent identity and a basic audit trail. Customer-facing workflows get verified actions, sandboxed tools and reviewable records. Money movement, identity changes and regulated data get mandatory human gates, signed approvals and external anchoring.

His rollout order is boring on purpose: record inference-time facts as structured evidence, sign and chain every event, anchor checkpoints outside the admin domain (WORM storage, a transparency log or a notarization service), and build and exercise the verifier before an incident forces you to.

## Who should watch

Security and platform engineers working on AI in regulated domains, anyone preparing for EU AI Act audits, and teams whose agent audit trail is currently an application log. The cryptography is explained at architecture level, so you do not need to know Groth16 going in.

## Related Conf42 talks

- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) from Conf42 DevOps 2026 is Beshane's own take on governance earlier in the lifecycle.
- [Adding Tamper-Evident Audit Trails to AI Agents in Production](https://www.conf42.com/MLOps_2026_Joao_Marques_audit_tamper_agents) from Conf42 MLOps 2026 tackles the same receipts problem from another angle.
- [The AI Trust Triad for DevOps: Shipping Reinforcement Learning, Federated Learning, and Explainable AI Safely in Regulated Systems](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) from Conf42 DevOps 2026 widens the view to regulated ML in general.

[Watch Neeraj Kumar Singh Beshane's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Neeraj_Kumar_Singh_Beshane_cryptography_compliance_pipelines)

[Watch the talk on YouTube](https://youtu.be/EelEvPhQLDk).

## Watch the talk

[RuntimeGuard-AI: Cryptographic Compliance for High-Risk AI Pipelines](https://www.conf42.com/Large_Language_Models_LLMs_2026_Neeraj_Kumar_Singh_Beshane_cryptography_compliance_pipelines) at Conf42 Large Language Models (LLMs) 2026.
