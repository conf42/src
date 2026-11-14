# Let agents think freely, but make every action pass a gate

Conf42 Blog, 2026-02-20, updated 2026-11-09. https://www.conf42.com/blog/sre2026/agents-reason-freely-but-act-through-gates

In short: Ajay Athitya Ramanathan of FourthSquare at Conf42 SRE 2026 maps the guardrail stack for AI agents in high-risk production, from Pydantic to OPA and Temporal.

A model that suggests something wrong is usually harmless; a model that executes something wrong touches real systems, data and users. At Conf42 Site Reliability Engineering 2026, Ajay Athitya Ramanathan, Data & AI Engineer at FourthSquare, turned that gap into a design rule for agentic automation: "maximum reasoning freedom, but with strict execution boundaries." Then he spent most of the talk naming the actual tools that enforce it.

## Old automation assumes you know every step

Ramanathan's diagnosis is that existing automation was built for deterministic software. ETL pipelines, batch jobs and rule-based workflow engines follow predefined decision trees, static scripts and fixed actions. Agents do the opposite: they plan dynamically, reason probabilistically and discover which tools to call. Plug an agent into infrastructure built for predictable workflows and you inherit the risks without the controls: hallucinated actions, prompt injection, unauthorized data access, cascading automation failures and, in regulated industries, compliance violations.

His answer is not to remove the autonomy, since reasoning is what makes agents useful. It is to make sure an agent never talks to production directly. Requests flow from a user or workflow into the agent framework, then through guardrails and policy engines, and only then into enterprise systems via secure tool APIs, with monitoring across the whole path.

## Five pillars, each with tools you can install

The second half is a practical catalogue, organised in five groups.

**Programmable safety.** Prompt injection defence (think SQL injection, but for prompts) with tools such as Guardrails Hub and NVIDIA NeMo Guardrails. Structured output so the agent always returns typed, machine-readable data, with Pydantic validating on the receiving end. Business-rule validations, with an example anyone in finance will recognise: check that the invoice line items plus tax and charges add up to the grand total. And LLM-as-a-judge, using a second model to evaluate the first, made measurable with tools like LangSmith.

**Identity and access.** Agents need identities like employees do, starting from least privilege. Open Policy Agent for fine-grained access control, cloud managed identities such as Azure managed identity, session-bound JWT or OAuth 2.0 tokens, and time-bound credentials that expire with the session. If the agent only needs to read, it should not hold write access to the database.

**Privacy.** Microsoft Presidio for detecting and redacting PII, AWS Comprehend as a managed alternative, Faker for masking with realistic values, Ollama for running models entirely on-prem, and synthetic data tools such as Mostly AI.

**Human in the loop**, which he calls the most underrated pillar. LangGraph supports interrupt-and-resume so execution pauses until a human approves, Temporal handles longer, durable approval flows, OPA allow lists define which actions are permitted at all, and irreversible actions get explicit checkpoints that require confirmation.

**Observability and evals.** Per-step traces with LangSmith or Weights & Biases, logging of prompts, responses, latency and token counts with Azure Monitor or Datadog, OpenTelemetry for vendor-neutral instrumentation, LLM Guard for real-time input and output checks, DeepEval and RAGAS for offline evals that catch drift, and Grafana or Elastic to pull it all into one audit timeline. If you can't observe it, you can't trust it.

## Who should watch

This is a survey talk, wide rather than deep: no single tool gets a long demo, but you leave with a shopping list sorted by the risk it addresses. It suits platform and SRE teams about to give an agent write access to anything that matters, and anyone who needs to explain to a compliance team what stands between the model and the database. His closing claim is the one to test against your own stack: safety and autonomy are not opposites if the guardrails are real.

## Related Conf42 talks

- [Your Agent Works. Will It Survive Tomorrow? Operating LangGraph.js with skein-js](https://www.conf42.com/MLOps_2026_Maina_Wycliffe_langgraph_skein_agent) by Maina Wycliffe.
- [Guardrails First: Designing Safe, Scalable, and Accountable AI Agents for Security Operations](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) by Neal Iyer.
- [Running 50+ AI agents in production: the patterns that held up](https://www.conf42.com/MLOps_2026_Muhammad_Haris_Farooq_agents_patterns_production) by Muhammad Haris Farooq.

[Watch Ajay Athitya Ramanathan's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/iUXbQsRt5SQ).

## Watch the talk

[Autonomy with Guardrails: Operating Agentic Automation in High-Risk Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) at Conf42 Site Reliability Engineering (SRE) 2026.
