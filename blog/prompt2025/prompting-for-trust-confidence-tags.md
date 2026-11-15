# Users act on AI answers they can check, so prompt for that

Conf42 Blog, 2025-10-29, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/prompting-for-trust-confidence-tags

In short: Raj Kommera at Conf42 Prompt Engineering 2025 on trust-building prompts with confidence tags, source attribution, clarifying questions and audit trails.

An accurate model that nobody acts on is a very expensive autocomplete. At Conf42 Prompt Engineering 2025, Raj Kommera, a Salesforce engineer and platform architect, argued that the enterprise AI adoption gap is about trust, and that trust is designed at the prompt layer: confidence tags, source attribution, clarifying questions and audit metadata built into every response.

## The trust gap

Raj's framing: LLMs already sit inside chatbots, copilots and decision tools, but if users cannot see how or why a model reached its answer, they will not act on it. You end up with systems that are technically capable and quietly unused. The challenge is human confidence, not model capability.

## Five principles for trustworthy prompts

The core of the talk is a short list:

1. **Confidence tagging:** have the model label outputs, for example as ready to act on, needs review, or needs an expert.
2. **Source attribution:** make the model cite the documents or reasoning behind each claim.
3. **Adaptive clarification:** let the model ask for more information when the request is ambiguous.
4. **Progressive disclosure:** high-level insight first, details on request.
5. **Audit trail integration:** embed metadata so every decision can be traced later.

His example of confidence tagging: rather than a raw number, the model reports a defect rate as moderate in confidence and recommends inspecting part of the batch. The user knows both how sure the system is and what to do next.

He adds context scaffolding: inject domain vocabulary (what counts as a qualified lead or a material risk), regulatory rules such as GDPR or SOC requirements, and thresholds for when to escalate or send to a human. Generic models do not know your organisation's words, and that mismatch is a common reason trust breaks.

## Same model, different prompts, different adoption

Raj walks through three cases. In a lead qualification assistant, sales reps ignored AI lead scores. The scores were fine; the explanation was missing. After redesigning prompts to include confidence tags, citations and visible reasoning, he reports 71% more follow-up actions and a 34% improvement in conversions, with no change to the model.

In a legal summarisation pipeline, teams refused summaries they could not trace to a clause. Section-level attribution and flags for clauses that deviate from standard templates cut review time sharply, and he reports user confidence rising to near 90%.

The third is a decision-support bot asked whether to approve a vendor contract. The old version answered at once. The new one first asked whether the vendor was new or a renewal and what the contract value was, then checked spend thresholds and compliance before recommending. Asking first turned out to be the trustworthy move, which anyone who has worked with a good senior colleague already knew.

## Making it scale

The techniques underneath are schema-driven outputs (JSON the system can validate automatically), chain-of-thought prompting so reasoning is visible, and conditional instructions for edge cases such as missing data. Feedback loops capture user corrections in the chat or orchestration layer, so prompts can be refined and failure modes found. His roadmap: audit current prompts for ambiguity, redesign for transparency, test with real users, and keep iterating.

## Who should watch

Product engineers and architects shipping LLM features to business users who are polite about the AI and then ignore it. If your team argues about model choice while adoption stalls, this talk points at the cheaper lever.

## Related Conf42 talks

- [Shradha Kohli on explainable AI and chatbot transparency](https://www.conf42.com/DevSecOps_2024_Shradha_Kohli_conversational_ai_trust) at Conf42 DevSecOps 2024.
- [Abhishek Vajpayee and Rathish Mohan on transparency for healthcare chatbots](https://www.conf42.com/DevSecOps_2024_Abhishek_Vajpayee_Rathish_Mohan_healthcare_chatbot_transparency), the same problem where the stakes are clinical.
- [Saideepak Kandibanda on the AI trust triad for DevOps in regulated systems](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) at Conf42 DevOps 2026.

[Watch Raj Kommera's talk](https://www.conf42.com/Prompt_Engineering_2025_Raj_Kommera_trust_llm_judgment), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/BGFIkq3LaJA).

## Watch the talk

[Prompting for Trust: Designing Transparent LLM Systems That Align With Human Judgment](https://www.conf42.com/Prompt_Engineering_2025_Raj_Kommera_trust_llm_judgment) at Conf42 Prompt Engineering 2025.
