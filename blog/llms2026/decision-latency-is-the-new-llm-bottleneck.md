# Decision latency is the new bottleneck in LLM delivery

Conf42 Blog, 2026-06-13, updated 2026-11-09. https://www.conf42.com/blog/llms2026/decision-latency-is-the-new-llm-bottleneck

In short: Senior engineering manager Lakshmi Priya Gopalsamy at Conf42 LLMs 2026 on SLOs for human approvals, policy as code and golden paths for LLM teams.

LLMs made writing code, tests and docs take minutes, but the approvals around them still take days. Lakshmi Priya Gopalsamy, a senior engineering manager with over 20 years of building large distributed systems, argued at Conf42 Large Language Models 2026 that the bottleneck in enterprise AI has moved from the machine to the human, and that decision latency and cognitive load deserve the same treatment as throughput and error rate.

Her reframing of the classic SRE question: "What happens when system succeeds faster than human can govern it?"

## The checkpoints never got the memo

Every AI output that touches production still crosses human gates: model approvals, prompt reviews, data governance, security and safety checks, incident response. Gopalsamy's opening scenario will be familiar: the model is ready, testing looks great, and the launch stalls because nobody knows who signs off.

She defines two properties. Decision latency is the time between an AI output being ready and a human making a call on it. Cognitive load is the stack of choices engineers juggle at once: model and provider selection, evaluation frameworks, hallucination mitigation, prompt versioning, prompt injection, data leakage and audit trails. Each is manageable alone. All at once, at LLM speed, they lead to burnout, and burnt-out engineers build fragile systems.

## Put SLOs on human loops

The useful move is borrowing SRE vocabulary for people. Do you know the p95 for a model approval? Is there a runbook when a safety validation fails, or does it go to a Slack channel and hope? Manual AI governance is toil in the strict sense, because it grows linearly with every new model, prompt and use case. Your team's capacity for manual governance decisions per sprint works like an error budget.

## Three tiers instead of one queue

The first pattern replaces the default of sending everything to a human review queue with three tiers borrowed from access control:

- **Pre-authorized** for low-stakes, reversible changes such as well-tested prompt templates or internal tooling suggestions. No human gate.
- **Async review** for medium-stakes changes such as new prompt patterns within an approved model family, reviewed within a clear SLO (she suggests something like four hours).
- **Explicit approval** for high-risk, irreversible moves: new model families, data classification changes, public APIs with regulatory exposure.

She compares it to a circuit breaker: the response to overload is built in, not remembered from a meeting two years ago.

## Owners, not committees

AI initiatives often launch with a cross-functional committee and no team owning production reliability, so incidents go to everyone, meaning nobody. Her fix is plain engineering management: one team owns each production LLM, carries the pager and the SLO, and has the authority to decide. For every model in production you should be able to say who owns it, what the SLO is, who gets paged and how architecture decisions are made.

## Governance you can unit test

The pattern she knows best comes from building a generative AI support system for a data platform with thousands of internal users and over a hundred thousand Spark jobs a day. Any governance decision that could be a rule lived in the pipeline, not in Slack. Prompt boundary checks, data classification and output safety thresholds ran in milliseconds and wrote an audit log with model version, timestamp and policy version.

"You cannot unit test a Slack approval, but you can absolutely unit test a policy engine." When an auditor asks how a decision was made, you point at a versioned policy and a log.

## Golden paths, including model choice

The last pattern is the opinionated golden path: an approved model catalog with version pinning, a standard evaluation framework, prompt templates with safety checks and observability hooks built in. Adoption is maths, not culture, because the paved road is faster. She singles out model selection: pick by task profile, risk profile and operational constraints, not by public benchmark score, and treat every model version bump as a governance event rather than a routine dependency upgrade.

Her homework for next week: map and time your decision loops, name an owning team for every production LLM, automate one governance decision this sprint, and write a one-page golden path.

## Who should watch

Engineering managers, platform leads and SREs who own the path from prototype to production for LLM features. Hands-on engineers will find it light on code but heavy on arguments to bring to the next governance meeting.

## Related Conf42 talks

- [The Paved Road Had a Compliance Gate](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved) from Conf42 Platform Engineering 2026 puts a gate on a golden path.
- [Building AI-Native DevSecOps Platforms with Governed Platform Engineering](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai) from Conf42 DevSecOps 2026 covers governance built into the platform.
- [A Policy-as-Code Approach to RBAC Authorization](https://www.conf42.com/DevSecOps_2024_Graziano_Casto_policy_rbac_authorization) from Conf42 DevSecOps 2024 is a concrete policy-as-code example.

[Watch Lakshmi Priya Gopalsamy's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lakshmi_Priya_Gopalsamy_latency_reasoning_reliability)

[Watch the talk on YouTube](https://youtu.be/BL81rkI3oKQ).

## Watch the talk

[Building Reliable LLM Systems: Managing Decision Latency and Cognitive Load in the AI Era](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lakshmi_Priya_Gopalsamy_latency_reasoning_reliability) at Conf42 Large Language Models (LLMs) 2026.
