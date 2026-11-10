# Conf42 AI Agents 2026: less LLM, more harness

Conf42 Blog, 2026-09-25. https://www.conf42.com/agents2026/conf42-ai-agents-2026-roundup

In short: Conf42 AI Agents 2026 roundup - planning without model calls, AI coding harnesses, LLM-as-judge testing, runaway token bills and agent security, in 22 talks.

Conf42 AI Agents 2026 ran online on September 24, 2026, with 22 talks, and the loudest message was a sceptical one: the model is rarely the problem. Speaker after speaker argued that what makes an agent shippable is the system around it, meaning deterministic planning, typed tools, review harnesses, evals, budgets, and identity boundaries. There were plenty of demos, but the best talks were about what happens after the demo.

The full lineup is on the [Conf42 AI Agents 2026 event page](https://www.conf42.com/agents2026), and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCZ8u5VHJAm9eOB9KJTCZT8).

## Stop asking the model what to do next

[Maureese Williams](https://www.conf42.com/AI_Agents_2026_Maureese_Williams_planning_search_graph), an AI Engineer at Disney, started from a mundane observation: at every step, an agent asks the language model what to do next, so a twenty-step task costs twenty model calls and gives a different plan each run. The GATS approach (Graph-Augmented Tree Search) runs UCB1 tree search over a state-transition graph the agent builds as it works. The LLM never picks an action; it is the last rung of an escalation ladder, after symbolic rules and learned statistics, and its answers are cached.

[Michael Haim](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism), founder and CEO of Zindell Technologies, tackled the same non-determinism from the language side: you cannot orchestrate agents with a plain if or switch when their output is fuzzy, so use pattern matching to turn it into structured, auditable control flow. And [Elizabeth Fuentes Leone](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) of AWS showed semantic tool selection: every call serialises every tool description into the context, so filter tools with vector search before they reach the LLM, cutting both wrong picks and token cost.

## The harness decides what ships

AI coding got its own track, and almost none of it was about prompts.

- [Ruben Marcus Luz Paschoarelli](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) of MultiVM Labs argued that AI coding fails because the system around the model trusts the wrong evidence, and showed his harness: short specs, isolated git worktrees, model routing by role, browser verification, screenshot gates, and cost controls.
- [Guido Scheffler](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) of CGI told the story of scaling AI code reviews across more than 70 projects, moving from brittle prompts to a deterministic review harness with an agent runner, an MCP server, managed checklists, and enforced completeness.
- [Suneet Malhotra](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy), Senior Manager of Test Engineering at Motorola Solutions, presented a Claude Code and MCP pipeline whose three MCP servers turn product requirements into Jira stories, test cases, and Appium code at about 80% accuracy; the talk is about the other 20%, and why the human PR gate is mandatory.
- [Kemet Dugue](https://www.conf42.com/AI_Agents_2026_Kemet_Dugue_workflows_productivity_onboarding) walked through how Uber's driver onboarding team turned script-heavy manual processes into agentic workflows, and [Peter De Tender](https://www.conf42.com/AI_Agents_2026_Peter_De_Tender_azure_deployment_automation) of Microsoft showed how his open-source library of Azure demo scenarios became an agentic deployment system. [Kabir Ibraheem](https://www.conf42.com/AI_Agents_2026_Kabir_Ibraheem_fullstack_tooling_productivity) of Meltwater offered a practical tour of AI tools for full-stack engineers.

## Who judges the agent

Testing non-deterministic systems came up again and again. [Liran Yushinsky](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen), who leads automation at JFrog, asked how you test an AI that never gives you the same answer twice when it generates executable code through a chain of tool calls, and answered with LLM-as-judge alongside conventional checks.

Diamond sponsor Harness made the enterprise case: [Shubham Jindal](https://www.conf42.com/AI_Agents_2026_Shubham_Jindal_ai_demo_enterprise), Director of AI at Harness, laid out four pillars (context engineering, evals, memory, and governance) and argued that an eval suite should never pass at 100%, because then it cannot measure progress. [Shubham Sharma](https://www.conf42.com/AI_Agents_2026_Shubham_Sharma_readiness_platform_enterprise) of Microsoft proposed a unified readiness framework, so models, retrieval, orchestration, and human-in-the-loop workflows are assessed together rather than team by team.

## The bill comes at 2 AM

[Yamini Rathamsetty and Karthik Akula](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) of AWS opened with the scene every agent operator dreads: 2 AM, no customers, no deploys, every dashboard green, and the bill climbing by multiples because their own agents were working hard all night on nothing. The talk dissects retry storms, runaway tool calls, context bloat, and multi-agent overhead.

[Vladimir Beskorovainyi](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) of Besk Tech brought the most production-scarred talk of the day: an on-prem text-to-SQL platform with open-weight models across 500+ data marts and 30M+ users. The opener says it all: "Very few people have to answer for the number it gives at 9:00 in the morning."

## Don't give the agent a shell

The trust track was about boundaries. [Ahmed Tariq](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) of Simplify9 argued for a small set of typed tools, a deliberately limited identity, and enforcement outside the model, instead of a shell and a broad credential. [Blaize Stewart](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) of GBLI broke a RAG application live with prompt injection, poisoned documents, and broken document-level authorisation. [Morgan Willis](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) of AWS summed it up: don't trust the agent, trust the system you build around it, with Amazon Bedrock AgentCore and the Strands Agents SDK as the toolkit.

## Agents meet enterprise data

Agents are only as good as the data they act on. [Rohit Deshpande and Scott Young](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) of SAP showed a ReAct agent that turns a request like AR aging by customer into a deployed dashboard over live data via MCP. [Vishwak Thatikonda](https://www.conf42.com/AI_Agents_2026_Vishwak_Thatikonda_mdm_data_retail) of Starbucks explained why master data management built for reporting breaks when agents make decisions on it. [Pon Murugesh Devendren](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events) of Deloitte built event-driven agents for proactive SAP incident management, [Nick Rezaee](https://www.conf42.com/AI_Agents_2026_Nick_Rezaee_health_wearables_intervene) of Harvard showed agents that turn wearable data into timely interventions, and [Dmytro Hlotenko](https://www.conf42.com/AI_Agents_2026_Dmytro_Hlotenko_serverless_photos_aws) of Sage confessed that his Step Functions DAG for judging 8,000 photos was a lie, and went agentic.

## Sponsors and what's next

Thanks to diamond sponsors [Harness](https://www.harness.io/) and [LLMday](https://llmday.com/), gold sponsor the [Prompt Engineering Conference](https://promptengineering.rocks/), the [HockeyStick](https://www.hockeystick.show/) podcast, and all the media partners on the event page.

The series returns with [Conf42 AI Agents 2027](https://www.conf42.com/agents2027) on September 23, 2027. Until then, the playlist holds enough harness engineering to keep your agents honest.
