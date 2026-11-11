# Your SQL query has a debugger, it's called EXPLAIN ANALYZE

Conf42 Blog, 2023-06-07. https://www.conf42.com/obs2023/debug-sql-with-execution-plans

In short: Eyal Trabelsi (Bigabid) at Conf42 Observability 2023 on reading execution plans to find SQL bugs, empty joins and duplicates, not only slow queries.

A SQL query that returns the wrong answer rarely throws an error. It returns zero rows, or twice the rows, and the problem shows up three dashboards later. At Conf42 Observability 2023, Eyal Trabelsi, Architect at Bigabid, argued that databases already ship the closest thing they have to a debugger, the execution plan, and that we mostly use it for performance when we should also use it for correctness.

It's a short, practical talk: a tour of EXPLAIN in PostgreSQL, two worked bugs, and a prototype visualiser Eyal wrote himself and openly calls not ready.

## Why is SQL so hard to debug?

The bug list is familiar: missing records, too many records, duplicates, nulls, wrong business logic, wrong computations. Spotting them takes skill and experience, and most databases have no step-through debugger, because materialising every intermediate result would be expensive. What they do provide is an execution plan. "So we should democratize execution plan," Eyal Trabelsi said at Conf42 Observability 2023, after a self-aware buzzword alert.

## How do you read an execution plan?

A query goes from parsing (structure, basic validation) through analysis (semantic validation) and rewriting to planning, where the database picks a strategy using its statistics, and execution. Plain EXPLAIN shows what the planner intended. EXPLAIN ANALYZE actually runs the query and shows what happened, which is what you want for debugging. Options add cost, buffers, timing and output formats such as JSON or YAML.

Eyal's example counts users with a non-empty Twitter handle. The plan is longer than the query, but it carries real numbers: on the slides, execution took 1.27 seconds and planning 0.4 milliseconds. The plan is an inverted tree of nodes: scans, joins, aggregates. Each node reports estimated rows against actual rows, the average row width (8 bytes for the aggregate), planner costs in arbitrary units, and actual startup and total time in milliseconds.

The trap is loops. Actual time and rows are per-loop averages, so for a node executed many times you multiply by the loop count to get the totals. Eyal's two pro tips: read one full execution plan at least once in your career, since the format is similar across databases, and cheat on your homework by pasting the weird numbers into Google or ChatGPT once you know what to look for. Every database has its own quirks on top.

## What does a bug look like in a plan?

The first worked example is an empty result: the same count, filtered on a specific handle, returns zero. In the plan, both the aggregate and the sequential scan produce zero rows, and the scan reports how many rows its filter removed, so the problem is the filter, not a join. The stored handle was spelt differently. In a query with ten joins, the same reading tells you which step drops everything.

The second is duplication. Joining titles to genres to find kid-safe films, the row count after the join is far larger than the titles going in. If you expected one-to-one or many-to-one, that jump is your duplicate, and you've found it before someone papers over it with a DISTINCT at the end of the funnel, leaving every consumer in the middle with the bad rows.

## What would good tooling look like?

Most current tools focus on performance, Eyal says, while correctness gets little help outside heavily tested finance queries. His prototype, QueryFlow, parses execution plans per database into an engine-agnostic representation, enriches each node, and draws the plan with bar lengths proportional to a chosen metric and colour for suspicious operations: an operation that drops to zero rows, or a join that multiplies them. A movie query hunting for Rowan Atkinson's films that returns nothing shows the guilty filter in red. Because the rules run over a parsed intermediate representation, they could also run unattended and alert to Slack when a query starts returning nothing.

"But I think we should expect opinionated things that will help us make queries correct," Eyal said. His wish list: easy and intuitive tools, integrated in the IDE, proactive enough to monitor saved plans as the data changes.

## Who should watch

Analytics engineers and backend developers who write SQL that feeds dashboards, and anyone who has only used EXPLAIN to chase slow queries. If you already read plans daily, the first half is revision; the correctness framing is still worth your time.

Related Conf42 talks: [Adam Furmanek on database guardrails in CI](https://www.conf42.com/Observability_2023_Adam_Furmanek_missing_chapter_ci_playbook_database) from the same event, [Adam Furmanek on observability for PostgreSQL and MySQL](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql), and [Lukas Vileikis on lessons from MySQL records](https://www.conf42.com/Platform_Engineering_2024_Lukas_Vileikis_mysql_records_lessons).

[Watch Eyal Trabelsi's talk](https://www.conf42.com/Observability_2023_Eyal_Trabelsi_debug_sql_queries) from [Conf42 Observability 2023](https://www.conf42.com/obs2023).

## From Bigabid

Eyal spoke as an architect at Bigabid, which supported Conf42 Observability 2023. QueryFlow, the visualiser in the talk, is his own prototype.

- Bigabid: [bigabid.com](https://www.bigabid.com/)

[Watch the talk on YouTube](https://youtu.be/XvulxlK7EYE).

## Watch the talk

[Apparently, you can "debug" your SQL queries](https://www.conf42.com/Observability_2023_Eyal_Trabelsi_debug_sql_queries) at Conf42 Observability 2023.
