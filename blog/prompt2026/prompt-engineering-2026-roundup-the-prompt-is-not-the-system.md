# Conf42 Prompt Engineering 2026 - the prompt is the smallest part

Conf42 Blog, 2026-10-30. https://www.conf42.com/blog/prompt2026/prompt-engineering-2026-roundup-the-prompt-is-not-the-system

In short: Conf42 Prompt Engineering 2026 in review, 18 talks on context contracts, prompt drift, injection defence, regulated workflows and agents in production.

[Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026) ran on October 29, 2026 with 18 talks, and almost none of them were about wording. The consensus across the day: a prompt is one input to a system, and the reliability lives in the contracts, context budgets, traces and rollout controls around it. Engineers from Adobe, Meta, eBay, Harness, Tech Mahindra and a handful of startups showed what that looks like when real users, regulators and attackers show up.

## Context is an engineering artefact with a budget

[Emerson Braun](https://www.conf42.com/Prompt_Engineering_2026_Emerson_Braun_contracts_context_agent) (Plan A Technologies) set the tone with "Prompting Is Not the System". He walks a realistic agent workflow and lists where it breaks: stale context, instructions that conflict with tool permissions, retries that repeat side effects, and prompts that grow until nobody knows what the agent may do. His fix treats context as a versioned input contract and moves tool schemas, permissions and failure behaviour out of the prompt.

[Nishant Kumar Thakur and Sonam Raj](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) (Adobe) brought the numbers. Pre-loading MCP tool schemas burned 150K tokens before the model read the user's question, and tool selection was right only 42% of the time. Code Mode, which swaps the schema dump for typed API stubs the model reads like library code, took that to 22K tokens and 80% accuracy. Same tools, different presentation.

[Ian Johnson](https://www.conf42.com/Prompt_Engineering_2026_Ian_Johnson_gate_whose_it) (Parento) asked the organisational version in "Whose gate is it?": every team running coding agents has a charter, a harness and a factory, and almost nobody has drawn the lines between them. He walks one rule down the rungs where a gate can sit and separates two boundaries, what a thing governs and who gets paged when it is wrong. [Kevin Brown](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) (Cloud World Model) pointed at a different gap: an agent can write Terraform but cannot feel what it breaks, so he simulates a proposed infrastructure change before merge and labels every number as modelled, estimated or a known gap.

## Prompts behave like software, so test them like software

[Sachin Gupta](https://www.conf42.com/Prompt_Engineering_2026_Sachin_Gupta_drift_prompts_stable) (eBay) proposed prompt contracts: required fields, banned claims, citation rules and token ceilings, enforced with JSON schema validation plus golden and fuzz tests in CI. His demo is a real regression caused by a harmless-looking prompt tweak, caught before users noticed. [Emmanuela Opurum](https://www.conf42.com/Prompt_Engineering_2026_Emmanuela_Opurum_workflows_production_reliable) (SoftNet Technologies) covered the same ground from the workflow side: prompt drift, weak evaluation and over-reliance on manual experimentation as the usual ways prompt-driven apps go wrong.

## You can't fix what you can't see fail

Observability got its own track. [Krishna Chaitanya Balusu](https://www.conf42.com/Prompt_Engineering_2026_Krishna_Chaitanya_Balusu_debugging_plan_fail) (Meta) authored the plan operation for agent planning spans in the OpenTelemetry GenAI semantic conventions, and showed how a first-class planning span lets you tell a planning failure from a tool failure, with a demo that catches a fault a final-answer check misses. [Indika Wimalasuriya](https://www.conf42.com/Prompt_Engineering_2026_Indika_Wimalasuriya_agentcore_datadog_observability) (Virtusa) traced a request through Amazon Bedrock AgentCore end to end in Datadog, correlating LLM signals with ordinary APM, logs and infrastructure.

Diamond sponsor Harness closed the loop. [Nicolas Zelaya](https://www.conf42.com/Prompt_Engineering_2026_Nicolas_Zelaya_prompt_survive_production) showed offline evals going green on a cheaper model, then a 20% canary in which every trace span stayed green while users got wrong answers and the cost per finished session went up. Rollback was a traffic edit, and the failed sessions became new eval cases.

## One guardrail is a demo, two are a design

[Manvitha Potluri](https://www.conf42.com/Prompt_Engineering_2026_Manvitha_Potluri_injection_guardrails_bedrock) (24x7 Systems) tested LLM guardrails on AWS Bedrock against 390 attack prompts in 15 categories: direct and indirect injection, role-play jailbreaks, encoding tricks, and attempts to fire destructive tool calls. Her case is for dual detection, a managed guardrail plus an independent second check, and for catching harmful actions before they execute rather than grading text after the fact. She also spends time on the cost of blocking too much, which security talks usually skip.

## When the output has to survive an auditor

Three talks took prompting into regulated work. [Mohit Upadhyay](https://www.conf42.com/Prompt_Engineering_2026_Mohit_Upadhyay_nepa_compliance_automation) (Tech Mahindra) built a permitting platform that automates NEPA Categorical Exclusion determinations for historically sensitive sites, combining RAG, computer vision and geospatial data while keeping traceability and human oversight. [Vraj Patel](https://www.conf42.com/Prompt_Engineering_2026_Vraj_Patel_safety_physical_assurance) (Apptronik) used bounded, human-supervised agents for safety assurance in physical AI, with the MBSE model as the single source of truth across ISO 26262, ISO 21448, UL 4600 and ASPICE. [Pratik Patel](https://www.conf42.com/Prompt_Engineering_2026_Pratik_Patel_aml_compliance_workflows) (Hexaware Technologies) applied the same discipline to anti-money-laundering workflows: grounded data products, factual extraction kept apart from interpretive reasoning, and no unsupported conclusions in a compliance decision.

## From pilot to product, with retrieval doing the heavy lifting

[Ahmed Gaber and Ahmed Morsi](https://www.conf42.com/Prompt_Engineering_2026_Ahmed_Gaber_Ahmed_Morsi_agent_front_facing) (Nowlun) took a customer-facing agent to production and found the single large system prompt broke under real traffic; intent detection, grounded tool calls and clear handoff rules to humans made it predictable, and real escalations became the eval set. [Aleem Khan](https://www.conf42.com/Prompt_Engineering_2026_Aleem_Khan_bias_news_llm) went the other way from the API: a real-time news pipeline that classifies around 70 types of bias started on frontier-model prompts, then used their outputs plus human review to train an in-house model that replaced most of the calls. [LaShawnda Rodgers](https://www.conf42.com/Prompt_Engineering_2026_LaShawnda_Rodgers_product_apps_launch) (RGLC) argued that a product starts long before the first prompt and showed her repeatable process for building and launching real apps.

On retrieval, [Santosh Muthyala](https://www.conf42.com/Prompt_Engineering_2026_Santosh_Muthyala_rag_personalizing_analytics) (Meta) personalised enterprise analytics RAG with a user profile store and five specialised indices, so a senior data engineer gets SQL-first answers and a product manager gets KPIs. [Ravi Ray](https://www.conf42.com/Prompt_Engineering_2026_Ravi_Ray_rag_context_enterprise) compared roughly 25 RAG implementations on a five-axis framework and made the case for ACL-aware retrieval, provenance and time-aware evaluation.

## Sponsors and where to watch

Thanks to [Harness](https://www.harness.io/) and [LLMday](https://llmday.com/), the Diamond sponsors, and to the [Prompt Engineering Conference](https://promptengineering.rocks/) at Gold. Every talk is on the [event page](https://www.conf42.com/prompt2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDzNtWZ0n1t5hBRAnvvhOpl).

The series is back with [Conf42 Prompt Engineering 2027](https://www.conf42.com/prompt2027). If this year is a guide, the talks will be even less about prompts.
