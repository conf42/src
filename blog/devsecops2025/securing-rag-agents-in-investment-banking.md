# Bank-grade AI agents need consensus, not just guardrails

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/securing-rag-agents-in-investment-banking

In short: Swamy Biru of JPMorganChase at Conf42 DevSecOps 2025 on securing RAG pipelines and multi-agent systems in investment banking middle-office operations.

Traditional security controls assume the system makes the same decision twice. AI agents in a bank don't. At Conf42 DevSecOps 2025, [Swamy Biru](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai), a vice president at JPMorganChase & Co, walked through a security-first architecture for agentic AI and retrieval-augmented generation in investment banking middle-office operations, built on one rule: every component of the AI pipeline is a potential vulnerability, so design for that from day one.

## The problem: probabilistic decisions in a deterministic compliance world

Biru frames the challenge as two questions the industry hasn't fully answered. How do you secure a system where decisions come out of probabilistic models instead of deterministic code? And how do you stay compliant when agents autonomously pull and synthesise information from huge knowledge bases?

His answer is that security has to be embedded in the architecture, not bolted on afterwards. The rest of the talk is that idea broken into layers.

## Retrieval is a security boundary, not just a search call

The first layer is knowledge retrieval. The knowledge base is multi-tiered and segmented by domain, with encryption and a security posture that tightens with the sensitivity of the information. Every retrieval passes through validation before anything is released: verify the identity and credentials of the caller, sanitise the query to block injection, apply role-based access control to limit what can come back, log every interaction for compliance, and protect the response in transit.

If you have ever built a RAG prototype that happily returned whatever the vector store found, this is the list of things your prototype skipped.

## Agents get narrow scopes and have to agree with each other

The second layer is orchestration. Biru describes multiple specialised agents (validation, compliance, risk assessment, communication, exception handling, operations), each confined to a strictly defined scope under least privilege, talking over a zero-trust model with end-to-end encryption between agents.

The interesting bit is the consensus mechanism, which he calls blockchain-inspired. High-stakes decisions need agreement from several specialised agents: an execution agent proposes an action, and the compliance, risk and operations agents must approve it independently before anything runs. It's four-eyes review, automated, with the eyes being models that don't share a context.

The third layer is isolation of model processing: sandboxes with no direct access to production, multi-stage input sanitisation and output validation, and what he calls an air-gap approach so a compromised model can't reach the systems that matter.

## The DevSecOps plumbing around the models

Around those layers sits fairly familiar DevSecOps: automated security testing from the earliest stages, continuous automated penetration testing and fuzzing, infrastructure as code that carries security policies, access controls and encryption settings, and secure coding templates so the safe path is also the easiest one for engineers.

Model security gets its own lifecycle. Training data is curated, training runs in isolated environments without network access, models are benchmarked for consistency with previous versions, and deployment needs approval from security and compliance teams. After release, drift is monitored and regular back-testing checks the model still behaves under current conditions.

Threat detection combines statistical baselines, deep learning for attack signatures, graph neural networks for unusual relationships across systems, and reinforcement learning to adapt. Responses are tiered: low-severity events trigger automated defences such as extra authentication or rate limiting, while medium-severity ones keep operations running under closer monitoring and escalate to senior security staff.

## Lessons worth stealing

Biru's closing lessons are short. Retrofitting security into an AI architecture is far harder than building it in. Human oversight stays critical, with a clear line between what the AI handles alone and where it escalates when uncertain. And the defence has to keep learning, through regular red-team exercises.

He also covers the compliance side (transaction reporting, Dodd-Frank, GDPR, model risk management) and explainability tailored to auditors, engineers and business users. The abstract mentions efficiency gains; the talk itself is mostly architecture, so watch it for the design, not for benchmarks.

## Who should watch

Architects and security engineers putting RAG or agents near regulated data, especially in finance. The consensus pattern and the retrieval checklist travel well outside banking.

## Related Conf42 talks

- [RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) shows the attacks this architecture defends against.
- [I Don't Trust AI Agents (And Neither Should You)](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) builds production guardrails around agents.
- [Leveraging AI in Fintech](https://www.conf42.com/DevSecOps_2024_Sudeep_Meduri_ai_fintech_security) covers AI for security and compliance automation in financial DevSecOps.

[Watch Swamy Biru's talk](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai)

[Watch the talk on YouTube](https://youtu.be/dgmWPi6218A).

## Watch the talk

[Securing AI-Driven Financial Operations: RAG & Agentic Systems at Scale](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai) at Conf42 DevSecOps 2025.
