# Six layers between an enterprise agent and a hallucination

Conf42 Blog, 2026-08-23. https://www.conf42.com/blog/obs2026/layered-guardrails-hitl-enterprise-agents-snowflake

In short: Arjun D Sureshbabu of Snowflake at Conf42 Observability 2026 on guardrails, hybrid RAG, validation and human review for trustworthy enterprise agents.

Ask an ungrounded employee assistant how to avoid tax and it will try to help, which is precisely the problem. At Conf42 Observability 2026, Arjun D Sureshbabu, who has spent three years building and productionising agents at Snowflake, walked through a layered reliability framework for enterprise AI: guardrails before generation, hybrid retrieval for grounding, validation after generation, structured human review and continuous benchmarking, rolled out in six phases.

## Why hallucinations are an enterprise problem

Sureshbabu's definition is practical. When an agent answers beyond what it is meant to answer, or answers without support, treat it as a hallucination. In a consumer chatbot that is embarrassing. In legal review, compliance, finance or HR it carries liability: an agent that explains ESPP or RSU rules from generic training data, with no citation, can create real legal exposure. Privacy is the other half. Ask an assistant for your work location and it needs to know who is asking, from a user profile loaded as context (title, manager, location), and must not answer Toronto when the right answer is San Francisco.

## Before generation: prompts as contracts

The first layer treats prompt templates as versioned, tested contracts that spell out task boundaries, permitted sources, output format and what to do when information is missing. Orchestration instructions matter more as agents gain tools: with ten tools and no routing hints, an agent will pick the wrong one or improvise. A simple rule such as sending payroll questions to the payroll search tool removes a whole class of wrong answers.

Role enforcement is the part data engineers will appreciate. Your payroll question must never return a colleague's payroll. Rather than trusting the model with that, Sureshbabu enforces it in the data layer with row-level security and row access policies, so a query resolves the current user at runtime and only ever sees that user's rows.

## Grounding with hybrid retrieval

The second layer is hybrid RAG. Sparse BM25 handles exact terms (ask about the ESPP enrollment window and it finds ESPP). Dense vector search handles meaning, so "my contribution" maps to the employee stock purchase plan. Reranking and multi-query orchestration break complex questions, such as comparing quarterly churn with customer support data, into sub-queries and combine the results.

The observability payoff is the paper trail. Every response is logged alongside the passages or SQL that supported it, which makes claims auditable and gives you data on what people actually ask. With an agent exposed to a large internal user base, the top questions by category tell you where to invest next.

## After generation: validate, then let experts score

Post-generation checks include citation enforcement, schema validation, showing the SQL for structured queries, and a second model acting as judge. Then comes human review, but not thumbs up and thumbs down. Experts score outputs on a structured rubric: factual correctness, contextual relevance (the current CEO, not one from five years ago), hallucination severity, and tone. Out-of-scope or malicious questions should get a graceful refusal, and an agent that is unsure should say it does not have enough data rather than invent an answer; he describes a confidence threshold below which the agent declines.

User feedback, including what the right answer should have been, is logged and fed back into instructions and tuning. Benchmarking then runs under stress, with adversarial prompts and missing-knowledge cases, and he describes a hybrid utility minimum Bayes risk approach that compares answers across multiple tools or sub-agents and picks the consensus. Groundedness thresholds gate releases.

## Who should watch

Teams building internal assistants over HR, finance or legal data, and data engineers asked to make those assistants safe. It is a framework overview rather than a code walkthrough, and the Snowflake features appear as one way to enforce access, not a sales pitch. The closing point is the one to keep: hallucination mitigation is not solved once at the model layer; you rerun the evals with every release.

[Watch Arjun D Sureshbabu's talk](https://www.conf42.com/Observability_2026_Arjun_D_Sureshbabu_llms_hallucinations_nlp) ([YouTube](https://youtu.be/vsYzDDZQcxE)).

## Related Conf42 talks

- [Secure Enterprise RAG: Building Trusted Vectorized Knowledge Systems for DevSecOps](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) by Ananda Kumar Dey (Quadrant Technologies), DevSecOps 2026.
- [RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) by Blaize Stewart (GBLI), AI Agents 2026: the attacker's view of the same pipeline.
- [Securing AI-Driven Financial Operations: RAG & Agentic Systems at Scale](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai) by Swamy Biru (JPMorganChase), DevSecOps 2025.

## Watch the talk

[Observability for Enterprise AI: Reducing NLP Hallucinations with HITL](https://www.conf42.com/Observability_2026_Arjun_D_Sureshbabu_llms_hallucinations_nlp) at Conf42 Observability 2026.
