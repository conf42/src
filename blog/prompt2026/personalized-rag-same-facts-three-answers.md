# Personalised RAG should change the answer's shape, never its numbers

Conf42 Blog, 2026-10-25, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/personalized-rag-same-facts-three-answers

In short: Santosh Muthyala (Meta) at Conf42 Prompt Engineering 2026 on RAG for analytics that adapts to engineers, analysts and PMs while facts stay fixed.

A data engineer, a business analyst and a product manager ask the same question: why did checkout conversion drop last week? At Conf42 Prompt Engineering 2026, Santosh Muthyala, Data Engineering Manager at Meta, argued that a RAG system should give them three different answers built on one set of facts. Personalise the evidence emphasis and the presentation; never the metric definition, the numbers, the uncertainty or the access rights.

## Grounded isn't the same as useful

RAG grounds an analytics answer in metric definitions, schemas, documentation and queries. That settles whether the answer is supported. It doesn't settle whether it helps the reader: several paragraphs of SQL detail don't help a PM, and a tidy business summary leaves an engineer unable to reproduce the result. Personalisation is aimed at that second question while keeping the first intact.

His hypothetical e-commerce example runs through the whole talk. Conversion is completed checkouts over eligible checkout starts, comparing two full weeks. Overall it falls from 5% to 4.5%; mobile drops from 6% to 5% while desktop holds at 4%, with 10,000 checkout starts per device each week.

## Three work products from one set of evidence

The engineer gets the query, the metric definition, session-level counts, lineage and assumptions, plus a flag when validation checks haven't actually run. The system doesn't pretend they passed.

The analyst gets the headline drop, the device breakdown pointing at mobile, and a lead: the mobile payment error rate rose from 2% to 3.5%, marked as not yet validated. A hypothesis to investigate, not a root cause.

The product manager gets the impact framed as a 10% relative drop and 100 fewer completed sessions, suggested next steps, likely owners in checkout and payments, and links to the dashboards. Nobody gets a different number because a simpler summary would read better, and nobody gets a cause presented as confirmed when it isn't.

## Profiles hold hints, not rules

The architecture has three components with explicit contracts: a user profile store that supplies hints, a retrieval system that supplies permitted evidence with enough context to interpret it, and a personalised generation layer that produces the answer in the right format.

Santosh's profile rules are the most transferable part. Keep it minimal: preferred tools, familiar domains, role, preferred depth. Record where each attribute came from: declared by the user, supplied by an application, or inferred. The current request wins over history, so a summary-lover who asks for SQL gets SQL. Users can inspect, correct and reset their preferences. And familiarity with a dataset never grants access to it; authorisation stays a separate decision.

## Eligible first, then useful

Retrieval draws on five logical indices that can live in one store: schemas, documentation, metric definitions, past queries and curated SQL examples. Before ranking, an eligibility stage drops sources that are similar but inappropriate (another business unit, another environment, outside the user's permissions) and weighs authority: a canonical definition and an informal investigation note aren't equals. When sources conflict, the system should surface the conflict instead of quietly picking one.

Ranking then orders the eligible evidence by relevance, task fit and freshness. His line on it is a good one to tape to a monitor: usefulness doesn't override authority. A popular query blaming payment errors can't replace the canonical conversion definition.

## Roll it out in phases, and prove it helps

His rollout order is foundation first (sources, metadata, access controls), then a RAG system that serves the current task before inferring anything about the user, then editable preferences. Evaluation covers retrieval, answers, drift (an old profile shouldn't keep steering someone whose job changed) and safety (prompt injection, query-history exposure, cross-tenant leakage). Keep a non-personalised baseline so you can tell whether personalisation is helping at all, and keep humans in the loop for consequential actions: suggesting an investigation differs from executing a rollback.

## Who should watch

Data platform teams building natural-language analytics, and anyone whose RAG assistant serves very different roles from one index. The example data is hypothetical, so treat it as a design pattern with clear contracts rather than a production results talk.

## Related Conf42 talks

- [RAG for Data Engineers: What It Is, Where It Fits, and Why Your Metadata Is the Missing Piece](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varun_Joshi_rag_metadata) by Varun Joshi (AWS) at Conf42 Large Language Models 2026.
- [Agentic Text-to-SQL in Production: What 500+ Data Marts and 30M Users Taught Us About LLM Orchestration](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) by Vladimir Beskorovainyi (Besk Tech) at Conf42 AI Agents 2026.
- [Operationalizing Semantic Consistency: A DevOps Framework for Reliable Cross-Engine Analytics](https://www.conf42.com/Database_DevOps_2026_Muthupalaniappan_Ramanathan_queries_monitoring_sql) by Muthupalaniappan Ramanathan (DoorDash) at Conf42 Database DevOps 2026.

[Watch Santosh Muthyala's talk](https://www.conf42.com/Prompt_Engineering_2026_Santosh_Muthyala_rag_personalizing_analytics) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/OKUWBc0-blw).

## Watch the talk

[Personalizing RAG for Prompt-Driven Enterprise Analytics](https://www.conf42.com/Prompt_Engineering_2026_Santosh_Muthyala_rag_personalizing_analytics) at Conf42 Prompt Engineering 2026.
