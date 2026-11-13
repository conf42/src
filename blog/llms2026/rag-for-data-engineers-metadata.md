# Data engineers already own the metadata RAG needs

Conf42 Blog, 2026-05-23, updated 2026-11-09. https://www.conf42.com/blog/llms2026/rag-for-data-engineers-metadata

In short: Varun Joshi (AWS) at Conf42 LLMs 2026 on four RAG uses for data teams, from schema Q&A to on-call, and why your metadata is the missing piece.

LLMs know SQL. What they don't know is your warehouse: which `orders` table is real, what grain a fact table has, why two columns with the same name mean different things. At Conf42 Large Language Models (LLMs) 2026, Varun Joshi, Senior Data Engineer at AWS, argues that data engineers are better placed than anyone to fix that with retrieval-augmented generation, because they already produce the context RAG needs as a side effect of their day job.

It's a practical introduction, aimed at data engineers rather than ML teams, and it ends with a four-week plan.

## RAG is prompt engineering at scale

Varun keeps the fundamentals short. A question is embedded, a similarity search runs against a vector store of your docs, schemas and incident threads, the top chunks go into the prompt, and the model answers with that context. The model's weights never change.

That gives you three properties he cares about: it's cheap to update (re-index the docs), fast to deploy (no fine-tuning), and auditable, because you can see exactly what was retrieved and why.

## Your metadata is already machine-readable

His case for data teams rests on four assets most of them already have: schemas (DDL, column descriptions, catalogs), lineage graphs, query history (a corpus of what stakeholders actually ask), and documentation, however patchy. Lineage alone answers questions like which reports break if you deprecate a dimension table, which is otherwise a tour through hundreds of jobs.

## Four places it fits

**Schema Q&A.** New engineers spend months learning a handful of entities. Index the DDL, dbt YAML descriptions and catalog exports and they can ask what a table contains and get the current answer instead of a Confluence page last edited in 2021. His recipe: export the dbt manifest, parse DDL, chunk by table, embed, store. He sizes it as a two or three day project.

**Grounded SQL agents.** The difference between a SQL agent that invents column names and one that doesn't is usually whether it was given the real DDL. With schema retrieval, the agent finds relevant tables semantically, even ones without "customer" in the name, and can use primary key and nullability information to pick join keys.

**Incident response.** When a pipeline breaks at 2 a.m., the on-call engineer needs to know whether this happened before and what fixed it. The postmortem usually exists; nobody searches Confluence at 2 a.m. Index postmortems, runbooks and Slack threads, and his team, which already runs this, gets the earlier incident and its root cause back in seconds.

**Tribal knowledge.** His favourite example: an orders pipeline runs at 6 a.m., not midnight, because years ago someone scheduled it around a billing system window. When that person leaves, the reason leaves too. Architecture decision records and PR descriptions are underrated sources, and he recommends recorded Q&A sessions with tenured engineers on what a new hire should know when the system breaks.

## An integration problem, not a content problem

The core thesis: if your team has done data engineering for more than six months, you almost certainly have most of this content already, scattered across a catalog, Git, Confluence and Airflow logs. Building RAG looks less like an AI project and more like a new data pipeline, which is home turf.

His month plan: week one, audit your metadata without writing code. Week two, a minimal schema Q&A over the dbt manifest in Chroma. Week three, one agent use case, SQL or incident response, whichever hurts more. Week four, measure and share. He puts the first month at roughly 15 to 20 engineering days.

## Who should watch

Data engineers who keep hearing about RAG from the ML side and want to know where it lands in their own workflow. If you already run RAG in production, the use cases will feel familiar, but the point that you already own the corpus makes a good pitch to take to your manager.

## Related Conf42 talks

- [Agentic Text-to-SQL in Production: What 500+ Data Marts and 30M Users Taught Us](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) by Vladimir Beskorovainyi, the grounded SQL agent at much larger scale.
- [How to use generative AI to finally fix out-dated runbooks](https://www.conf42.com/Incident_Management_2023_Anurag_Gupta_generative_ai_fix_runbooks) by Anurag Gupta, the incident-response use case from the SRE side.
- [Vector Embeddings and RAG Demystified](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) by Veliswa Boya, if you want the retrieval mechanics in more detail.

[Watch Varun Joshi's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varun_Joshi_rag_metadata)

[Watch the talk on YouTube](https://youtu.be/g4tV8ESA2g0).

## Watch the talk

[RAG for Data Engineers: What It Is, Where It Fits, and Why Your Metadata Is the Missing Piece](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varun_Joshi_rag_metadata) at Conf42 Large Language Models (LLMs) 2026.
