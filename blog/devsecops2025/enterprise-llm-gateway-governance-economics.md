# Enterprise LLMs stall between the pilot and the AI gateway

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/enterprise-llm-gateway-governance-economics

In short: Murali Koney of Cox Automotive at Conf42 DevSecOps 2025 on why enterprise LLM projects stall and a framework of deployment models, TCO and an AI API gateway.

The gap between an LLM demo and an LLM in production is mostly governance, security and an invoice nobody can forecast. At Conf42 DevSecOps 2025, [Murali Koney](https://www.conf42.com/DevSecOps_2025_Murali_Koney_ai_risk_llm), technical team lead at Cox Automotive, laid out why enterprise AI projects stall before production and a three-pillar framework for getting past that: pick the right deployment model, do the economics honestly, and put an AI API gateway between your users and the model.

It's a structured, slide-led talk aimed at DevSecOps and platform leads who have been handed an AI roadmap. No demos, a lot of checklists, most of them useful.

## Why pilots don't graduate

Koney lists four reasons initiatives fail. Infrastructure gaps: traditional systems struggle with AI compute and storage needs. A governance vacuum: no clear policies on model selection, data handling or decision accountability, with compliance frameworks lagging behind. Security teams unprepared for AI-specific threats such as prompt injection, model poisoning and data exfiltration through model outputs. And cost uncertainty, because token usage is hard to predict and that makes return on investment hard to argue beyond the pilot.

## Pick a deployment model on purpose

The first pillar is choosing between infrastructure, platform and software as a service. IaaS gives full control over model selection, fine-tuning and infrastructure, which suits highly regulated environments, at the price of a heavy operational burden, slower time to market and deep ML expertise. PaaS runs on managed infrastructure while you keep model development and tuning, trading some vendor lock-in for much less operational complexity. SaaS, with Amazon Bedrock as his example, is the fastest path for standard use cases but gives the least control over model behaviour and raises compliance questions because you depend on a third party.

## Do the five-year maths before the launch

The economics pillar is a five-year total cost of ownership: infrastructure (compute, storage, networking, scaling), licensing and API costs, operational overhead (monitoring, maintenance, security, compliance), talent and training, and ongoing optimisation. He ties investment to three performance metrics: time to first token, which shapes user experience in chat-style apps; tokens per second, which decides how many concurrent users you can serve; and utilisation, which he calls the fastest path to better return on infrastructure spend.

## The AI gateway is the control plane

The part most teams can lift directly is the AI API gateway, which Koney treats as the security control plane. It does five jobs:

- Authentication and authorisation with role-based access.
- Token-based rate limiting and quotas, so neither abuse nor a runaway loop blows the budget.
- Input sanitisation to detect and block prompt injection.
- Output filtering to scan responses and redact sensitive data before it reaches the user.
- Semantic caching, so similar queries are answered from cache instead of paying for a fresh completion.

That list maps neatly onto his four operational risks: prompt injection, data exfiltration, hallucination (mitigated with confidence scoring and human-in-the-loop review where the stakes are high) and cost overruns, which he wants handled with token limits and budget alerts so the bill is never a surprise.

## LLMOps habits for production

His LLMOps lifecycle runs from prompt engineering, model selection and fine-tuning, through adversarial, bias and performance testing (essential because the models are non-deterministic), to controlled rollouts with A/B testing, then monitoring of quality and cost. Production best practices include version-controlling prompts, configuration and policies as code so you can roll back instead of hot-fixing; fallback models for graceful degradation when the preferred one is down; and decision logs for compliance and debugging. For regulated industries he points to domain-specific models, naming BloombergGPT and Med-PaLM.

He closes on where it's heading, from text-only models to multimodal and agentic systems, and on embedding AI into the DevOps toolchain itself: code review in CI/CD, incident triage, anomaly detection and root cause analysis, and knowledge base generation.

## Who should watch

Platform and DevSecOps leads writing the business case or the guardrails for an internal LLM platform. Practitioners who already run a gateway will find it a checklist to compare against.

## Related Conf42 talks

- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) takes the governance pillar into pipelines.
- [Reduce AI Agents Costs and Mistakes with Semantic Tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) attacks the cost problem from the agent side.
- [Transforming Cybersecurity Governance with GenAI](https://www.conf42.com/Platform_Engineering_2024_Akshay_Sekar_Chandrasekaran_cybersecurity_governance_genai) covers risk and compliance from the security team's seat.

[Watch Murali Koney's talk](https://www.conf42.com/DevSecOps_2025_Murali_Koney_ai_risk_llm)

[Watch the talk on YouTube](https://youtu.be/Z2BM2KeumGo).

## Watch the talk

[Securing Enterprise AI: Governance, Risk, and Economics of LLM Adoption](https://www.conf42.com/DevSecOps_2025_Murali_Koney_ai_risk_llm) at Conf42 DevSecOps 2025.
