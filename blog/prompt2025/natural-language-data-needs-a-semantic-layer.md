# Natural-language data access only works on top of a semantic layer

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/natural-language-data-needs-a-semantic-layer

In short: Jimish Kadakia (Snowflake) at Conf42 Prompt Engineering 2025 on LLMs for SQL generation, conversational pipelines and the governance that keeps them honest.

Asking for customer retention rates by region for quarter four is a lovely prompt, right up until the model guesses what your company means by retention. At Conf42 Prompt Engineering 2025, Jimish Kadakia, a solutions architect at Snowflake with around 12 years in data and analytics, argued that LLMs can open cloud data to business users, but only when context, validation, governance and feedback loops are built in first.

It's a practitioner's overview rather than a product demo. He mentions Snowflake's Cortex Analyst and Snowflake Intelligence, and dbt's use of LLMs, as examples, but the advice applies to any warehouse.

## From SQL tickets to plain questions

Jimish starts with the traditional setup: data engineers write complex SQL views and stored procedures, script and babysit pipelines, and handle monitoring, security and governance. Business users file a ticket and wait. LLMs, he argues, go well beyond chatbots and content generation here; they can bridge the gap between business users and technical data infrastructure.

His three applications: query generation (natural language to optimised SQL), pipeline orchestration through conversation (rerun last night's job after a source fix), and real-time analytics (where are sales high, which region is hurting).

## Four components, and context comes first

The core of the talk is four components that make this work.

**Context optimisation.** Give the model business information and data relationships. His concrete recommendation is a semantic layer: semantic views or models that capture business terms, calculation logic and how entities relate. The more useful context the model has, the more accurate the query.

**Prompt design patterns.** The way a question is written shapes the answer, so build reusable templates that guide business users to consistent results.

**Validation.** Safeguards that check data integrity and output quality, with rigorous testing before anything reaches business users in production.

**Feedback loops.** Humans refine prompts based on real usage and model performance, so accuracy improves over time.

## Three things you can actually build

His examples make it concrete. Ad hoc querying: a user asks for retention by region; the system generates SQL that a technical user can review before it runs, or, for non-technical users, returns a table or chart directly. Pipeline management for developers and admins: run the nightly customer aggregation pipeline by asking for it, instead of hunting through a scheduler. Data exploration embedded in BI tools, with a natural-language search bar that reshapes existing views.

The review-before-run option is the quiet good idea here. You get the speed without letting an LLM fire unchecked SQL at production.

## The hard parts

He doesn't skip them. Accuracy and hallucination need validation frameworks and guardrails, because a model that starts down a wrong path can keep confidently producing wrong answers. Governance and security are independent of LLMs but more urgent with them: privacy regulations, reviewed permissions, and keeping PII and policy-restricted company data out of what the model sees. Fine-tuning on domain schemas and business terminology helps. Performance at scale needs enough compute without wasting it. His governance checklist: access control, automatic column masking, role-based access, complete audit trails of LLM-generated queries, and human approval before execution where required.

His rollout mantra: start small with one domain or process, collaborate across business, engineering, security and compliance, test rigorously, scale incrementally.

## Who should watch

Data engineers and analytics leads being asked to put a chat box on the warehouse, and platform owners who need a checklist for doing it without leaking data or trust. If you've already shipped text-to-SQL in production, the related talks go deeper into orchestration and semantic consistency.

## Related Conf42 talks

- [Agentic Text-to-SQL in Production: What 500+ Data Marts and 30M Users Taught Us About LLM Orchestration](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) by Vladimir Beskorovainyi at Conf42 AI Agents 2026.
- [Closing the Semantic Gap with Feedback-Driven Ontology Learning](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) by Ravi Chandra at Conf42 Observability 2026.
- [Operationalizing Semantic Consistency: A DevOps Framework for Reliable Cross-Engine Analytics](https://www.conf42.com/Database_DevOps_2026_Muthupalaniappan_Ramanathan_queries_monitoring_sql) by Muthupalaniappan Ramanathan at Conf42 Database DevOps 2026.

[Watch Jimish Kadakia's talk](https://www.conf42.com/Prompt_Engineering_2025_Jimish_Kadakia_data_cloud_access) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/CgZVZ7Jhmn0).

## Watch the talk

[Prompt Engineering for Data Engineering Unlocking Natural Language Access to Cloud Data](https://www.conf42.com/Prompt_Engineering_2025_Jimish_Kadakia_data_cloud_access) at Conf42 Prompt Engineering 2025.
