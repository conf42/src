# Database DevOps with Cortex Code starts with a role that can't drop

Conf42 Blog, 2026-05-29, updated 2026-11-09. https://www.conf42.com/blog/llms2026/cortex-code-database-devops-least-privilege-role

In short: Tim Spann (Snowflake) at Conf42 LLMs 2026 runs database operations from the Cortex Code CLI and starts by locking down what the agent may touch.

Before you type a single prompt into a database agent, decide what it is not allowed to do. That is the first piece of advice Tim Spann, Senior Solution Engineer at Snowflake, gives at Conf42 Large Language Models (LLMs) 2026, in a demo-heavy tour of Cortex Code, Snowflake's coding agent, doing day-to-day database operations from natural language.

This is a vendor talk and says so: it shows Snowflake's own tool, on Tim's own demo account, with his cat making a cameo. What makes it useful beyond Snowflake shops is how he sets the agent up and what he trusts it with.

## Permissions first, prompts second

Tim's rule is blunt. If you don't want the agent dropping objects, give it a role that cannot drop objects. If it should only see one database or one schema, scope it to that. Read-only is an option. Don't hand it your own credentials and don't give it full access.

In the demo the agent runs under a dedicated key-pair user that can only reach demo data, on a warehouse assigned just to it, so its compute cost shows up on its own line. He also runs Cortex Code on a Raspberry Pi 500 on an isolated network with no root access, which is the hardware version of the same idea. Only inside that kind of fenced-off environment does he switch to the mode where it stops asking for confirmation on every step.

## Give the agent house rules, not just a chat box

Consistency matters more to data teams than cleverness, so Tim leans on the standard pieces: an agents markdown file that records his preferences (users, directories, what he likes), MCP connections to the other systems he uses, and skills. His install listed 102 skills, from data quality to Iceberg table management, and there's a skill for writing your own skills. The point of skills, as he puts it, is that they carry the best practices so each session doesn't reinvent them.

There are two versions of the tool. One lives inside Snowsight and pops up when a query fails or a typo breaks something; Tim compares it to Clippy, but one that actually works. The one he spends the talk in is the command line, which can also run one-off commands so you can wire it into other systems the way you would the Snow CLI.

## What the demos actually did

The live part is a run of small, real admin chores against his transit and traffic data:

- Find the five largest tables in a schema (the New York MTA bus tracking table came out on top at about 22 million rows), then pull the ten most recent rows, with the agent working out which column is the timestamp.
- Run a "know your data" skill that profiled tables for quality and freshness, with the agent planning six tasks and fixing its own failed queries along the way.
- List running queries, agents, services, dynamic tables, tasks and pipelines, which turned up objects that last ran a year ago and were worth dropping.
- Write those findings to a markdown report, because session memory is handy but a document survives.

He also shows SQL the agent wrote to send a video sitting in a Snowflake stage to a Gemini model and get structured JSON back; it counted 25 vehicles on a busy New York street.

The wider claim is about pace. Tim describes handing the agent a source and having it build tables, tests, a semantic view, Cortex Search, agents and a dashboard in about an hour, while he validates and says yes or no. Treat that as one practitioner's workflow, not a benchmark.

## Who should watch

Data engineers and part-time database admins on Snowflake who want to see what an agent can do with their schema, and anyone outside Snowflake who needs a concrete checklist for giving a database agent a safe sandbox. If you want a vendor-neutral architecture talk, this isn't it.

## Related Conf42 talks

- [Prompt-Driven Microservice & Database Evolution: Using LLMs for Automated Schema Migration and DevOps Delivery](https://www.conf42.com/Database_DevOps_2026_Niraj_Katkamwar_llm_agents_delivery) by Niraj Katkamwar (Intuit), on LLM-written schema migrations.
- [Agentic Text-to-SQL in Production](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) by Vladimir Beskorovainyi (Besk Tech), on what breaks when SQL agents meet many data marts.
- [Database DevOps: CD for Stateful Applications](https://www.conf42.com/Database_DevOps_2026_Stephen_Atwell_cd_stateful_applications) by Stephen Atwell (Harness), for the delivery side of database change.

[Watch Tim Spann's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Tim_Spann_sql_automation_operations)

[Watch the talk on YouTube](https://youtu.be/pWt1_bmnPZ8).

## Watch the talk

[Automating Database Operations with Cortex Code](https://www.conf42.com/Large_Language_Models_LLMs_2026_Tim_Spann_sql_automation_operations) at Conf42 Large Language Models (LLMs) 2026.
