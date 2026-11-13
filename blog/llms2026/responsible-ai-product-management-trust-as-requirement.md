# For LLM products, trust is a functional requirement

Conf42 Blog, 2026-06-06, updated 2026-11-09. https://www.conf42.com/blog/llms2026/responsible-ai-product-management-trust-as-requirement

In short: Vijayalakshmi Narasimhan at Conf42 LLMs 2026 on product management for production LLMs, from trust-aware requirements to monitoring trust signals.

For web products the thing to manage was scalability, for mobile it was user experience, and for AI products it is trust. That's how independent researcher Vijayalakshmi Narasimhan closes her talk at Conf42 Large Language Models (LLMs) 2026, and the half hour before it argues that the product development lifecycle most teams use was built for deterministic software and needs rework once an LLM ships.

This is a product management talk, not an engineering one. It is aimed at the people who write requirements and own outcomes, which is exactly why engineers on LLM teams may want to see it.

## The demo-to-production cliff

Her description of the typical enterprise journey will sound familiar: build a chatbot proof of concept, impress stakeholders, then hit the wall of deploying it safely at scale. A hallucinated answer in a demo is a funny slide. In production it can be a compliance, financial or reputational problem.

Traditional software gives the same output for the same input, so "does the feature work?" was most of the question. With an LLM you also have to ask whether it is fair, safe, explainable and auditable, and whether you can still answer that after launch. Prompts, context, data sources and model settings all move the output.

## Write trust into the requirements

Vijayalakshmi's main move is reclassification. Trust, compliance and security are usually filed as non-functional requirements and deprioritized. For LLM products she argues they are functional, because what the user experiences is the model's behaviour. A strong requirement says the system must give explainable responses, cite sources where appropriate and protect sensitive data, and it says so in measurable terms.

Compliance by design follows: identify regulatory, privacy, security and ethical constraints early and turn them into acceptance criteria and evaluation gates. Her example is a financial advisory assistant that needs transaction context, domain context, audit logs and decision traceability from day one, because retrofitting end-to-end audit into a mixed human and AI workflow is hard.

Governance artifacts make it visible: model cards for intended use, limitations and known risks, and datasheets for datasets covering origin, purpose and what the AI may do with the data.

## Test how it fails, not whether it fails

Classic QA isn't enough. She pushes scenario-based and behaviour-based validation, bias testing, ambiguous prompts (different users describe the same problem very differently) and adversarial cases. The aim isn't identical wording on every run; it is the same outcome for the same scenario. The useful question, in her framing, is how the model will fail and why.

## Monitor trust, not just latency

Models get updated, prompts evolve, data and policy change, so a passing validation result says little about next month. Monitoring has to cover technical metrics (latency, cost, error rate, hallucination rate, retrieval quality) and product metrics (task completion, satisfaction, adoption, business impact). The ones teams skip are trust signals, which are hard to quantify and often come from feedback sessions and dogfooding: ask users whether they trust the answers and, if not, whether the cause is the data, the response or the experience.

For structure she points PMs to the OECD AI Principles for what trustworthy AI looks like and the NIST AI Risk Management Framework (govern, map, measure, manage) to put it into practice. Human oversight should scale with the stakes: light for low-risk tasks, verification checkpoints and override paths for healthcare, finance or hiring decisions.

## Who should watch

Product managers taking an LLM feature from pilot to production, and engineering leads who need a shared vocabulary with them for requirements, evaluation gates and post-launch monitoring. Engineers looking for implementation detail should pair it with something more hands-on.

## Related Conf42 talks

- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) by Neeraj Kumar Singh Beshane (Meta), governance from the delivery pipeline side.
- [Responsible AI with Amazon Bedrock Guardrails](https://www.conf42.com/Machine_Learning_2025_Mohamed_Najaaf_guardrails_responsible_bedrock) by Mohamed Najaaf (AWS), on enforcing some of these controls in code.
- [A Product Manager's Take on the "AI-fication" in the World of Fintech](https://www.conf42.com/Machine_Learning_2024_Adhikar_Babu_product_manager_aification) by Adhikar Babu (Worldpay), another PM's view from a regulated industry.

[Watch Vijayalakshmi Narasimhan's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vijayalakshmi_Narasimhan_governance_lifecycle_products)

[Watch the talk on YouTube](https://youtu.be/ULJkX-0Vo9I).

## Watch the talk

[Responsible AI Product Management for Production LLM Lifecycles](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vijayalakshmi_Narasimhan_governance_lifecycle_products) at Conf42 Large Language Models (LLMs) 2026.
