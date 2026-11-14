# Put a rule engine on both sides of the LLM in grocery retail

Conf42 Blog, 2026-02-18, updated 2026-11-09. https://www.conf42.com/blog/sre2026/llms-in-grocery-need-a-rule-engine-around-them

In short: Sanjay Basu of TCS at Conf42 SRE 2026 on running LLMs in grocery retail with new SLOs, hybrid rule-plus-LLM decisions and a five-stage AI incident playbook.

When an LLM recommends a substitute for an out-of-stock item, a wrong answer costs a sale and maybe a customer. At Conf42 Site Reliability Engineering 2026, Sanjay Basu, Global Head for AI / GenAI Products at TCS, laid out a framework for running LLMs in grocery retail: redefine the SLOs for probabilistic systems, wrap the model in deterministic rules, and give AI failures their own incident playbook.

## Why LLMs break the usual SRE assumptions

He starts with the three properties that make LLM services awkward to run. Outputs are non-deterministic, so the same prompt can give different results across calls, which undermines traditional notions of correctness. Latency varies at the token level and grows with output length. And the dependencies keep moving: prompts, embeddings and context windows change continuously.

Retail raises the stakes. Traffic spikes around flash sales such as Cyber Monday, substitutions have to be the right substitution, personalization runs at an audience of one, and inventory accuracy has to be predicted rather than assumed.

## SLOs for a system that is allowed to be a little wrong

His answer is to extend the SLO set rather than abandon it. Alongside the usual availability, he proposes semantic accuracy (the share of responses that pass automated semantic evaluation against ground truth or intent), time to first token, a hallucination rate budget treated like an error budget, and cost per inference as a first-class reliability signal. The last one is the quiet troublemaker: tokens behave like infrastructure spend, so scaling decisions have a bill attached.

## The rule engine goes before and after the model

The architectural centrepiece is a hybrid decision layer. A rule engine enforces the hard business constraints, which are deterministic. The LLM works as a reasoning layer inside that decision space. Then a post-inference validation step checks the output against the rule engine again before it reaches a customer or a downstream system. The point is to keep hallucinations from surfacing, and to make sure every call has a deterministic fallback so the customer experience does not degrade when the model does. Resilience, he insists, is designed in, not bolted on after the first production incident.

## AI incidents get their own five stages

For AI-induced failures he outlines a five-stage response:

1. Detection, via the semantic evaluation pipeline alerting on hallucinations and quality drops.
2. Containment, by shifting traffic automatically to the rule-based fallback layer and throttling model traffic.
3. Diagnosis, by replaying prompt telemetry to isolate the offending template version or embedding refresh.
4. Remediation, by rolling back the prompt version or restoring traffic through a shadow model.
5. Post-incident hardening, by reviewing the SLO breach and the evaluation pipeline itself.

That only works if you log every prompt and template version, which is why observability features so heavily: prompt telemetry, embedding-based similarity checks between output and retrieval context, and drift monitoring on semantic distributions.

Guardrails round it out: pattern classifiers for prompt injection before the model is invoked, named entity recognition to strip personal data from the context window, toxicity and bias screening, and regulatory filters that hard-block things like alcohol, pharmacy and age-restricted products in recommendations.

## Agents get budgets, not blank cheques

The last section covers agentic LLMs in logistics, fulfilment and last-mile delivery, where models plan, call tools and act. His constraint is that this autonomy is bounded at the orchestration layer: action budgets, rollback triggers and human evaluation ratios for every agent workflow.

## Who should watch

This is a short, dense framework talk rather than a war story, so expect a checklist more than a postmortem. It suits SREs and platform leads who have been handed an LLM feature in a high-traffic commerce system and need a vocabulary for SLOs, fallbacks and incidents. If you already run semantic evals in production, the hybrid rule-engine pattern and the incident stages are the parts to compare against your own setup.

## Related Conf42 talks

- [Building Reliable LLM Systems: Managing Decision Latency and Cognitive Load in the AI Era](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lakshmi_Priya_Gopalsamy_latency_reasoning_reliability) by Lakshmi Priya Gopalsamy.
- [Observability for Enterprise AI: Reducing NLP Hallucinations with HITL](https://www.conf42.com/Observability_2026_Arjun_D_Sureshbabu_llms_hallucinations_nlp) by Arjun D Sureshbabu.
- [Platform Engineering for Resilient Retail Supply Chains with Event-Driven Design](https://www.conf42.com/Platform_Engineering_2026_Nidhin_Jose_retail_supply_event) by Nidhin Jose.

[Watch Sanjay Basu's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sanjay_Basu_operationalizing_llms_scale) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/7RCZKCfk1qc).

## Watch the talk

[Operationalizing LLMs at Scale: Reliability, Resilience, and Cognitive Commerce in Grocery Retail](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sanjay_Basu_operationalizing_llms_scale) at Conf42 Site Reliability Engineering (SRE) 2026.
