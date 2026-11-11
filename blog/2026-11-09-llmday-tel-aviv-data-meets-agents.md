# LLMday Tel Aviv brings data engineering and AI agents to one room

Conf42 Blog, 2026-11-09. https://www.conf42.com/blog/2026-11-09-llmday-tel-aviv-data-meets-agents

In short: LLMday Tel Aviv, November 17 at Microsoft Reactor - free talks from FalkorDB, groundcover, Komodor, Snyk and TeraSky on agents, graphs and data.

LLMday lands in Tel Aviv for the first time on November 17, 2026, at the Microsoft Reactor, with a one-track day where LLM talks sit right next to hard data engineering. Speakers come from FalkorDB, groundcover, Komodor, Cato Networks, Neradot, Snyk and TeraSky, and the event is free to attend (registration is with approval).

The edition is run with Microsoft and TeraSky, and the angle is the overlap: what happens to your agents when the data under them is huge, messy or impossible to summarise.

## The lineup reads like a postmortem collection, in the good way

Several talks are about things that broke and what the team did next.

- **Avital Tamir (groundcover)**, *The Ninth Rewrite Might Be a Delete: Building Production AI Agents on Shifting Ground*. The abstract counts eight full rewrites of a production agent, some forced by mistakes, some by model and platform releases that turned the team's own infrastructure into somebody else's feature.
- **Nir Adler (Komodor)**, *Bye Bye Timestream - A Tale of Migrating 5.9 Billion Metrics a Day to ClickHouse*. When AWS announced end of life for Amazon Timestream, Komodor had to move the metrics behind customer dashboards without taking queries offline.
- **Liran Tal (Snyk)**, *From Second Brain to AI Chief-of-Staff: Engineering an Assistant That Runs Your Workweek*. A markdown second brain wired into email, chat, calendar and a work tracker, which looked tidy for six weeks while it was quietly failing.

## Agents need a map, and sometimes the raw numbers

**Roi Lipman (FalkorDB)** takes on a familiar pain in *From grep to graph: giving AI agents a map of your code*: coding agents handle a single function fine, then fall back to grep when you ask what breaks if a shared type changes across many repos. His approach turns the codebase into a graph the agent can query.

**Liza Katz (Neradot)** goes the other way in *Just Roll Up and Die: When Your Agent Needs Data You Can't Aggregate*. In construction and manufacturing, averaging lies: 99% progress is meaningless if the missing 1% is a structural beam. The talk is an anonymised case study of building an LLM system on data you are not allowed to compress.

**Noa Baron (Cato Networks)** brings *From Data Pipelines to Humans: Advantages of Mechanical Sympathy*, on context switching as a cost for CPUs and for people alike. **Yev Berman (TeraSky)** opens the technical part with *Talk to Your Cluster. It Talks Back!*

## Workshop and panel

**Haggai Zohar (TeraSky)** runs *Company Brain with Fabric and Claude*, connecting Claude to a Microsoft Fabric semantic layer over the Model Context Protocol so business users can ask questions without writing DAX or SQL. A panel with **Adaya Tal (ReasonLabs)** and **Einat Borohovich (Rambam Health Care Campus)**, moderated by **Sharone Revah Zitzman**, closes on where data and AI go next.

## Why a Conf42 viewer should go

If you watched [Conf42 Large Language Models 2026](https://www.conf42.com/llms2026) and wanted the follow-up conversation in person, this is it, with a heavier dose of storage and pipelines than most LLM days. Bring the migration war story you never got to tell; someone from the ClickHouse talk will want to hear it.

## Register

The day starts at 09:00 at the Microsoft Reactor in Midtown Tel Aviv. Tickets are free and handled through in10t, linked from the [LLMday Tel Aviv page](https://llmday.com/2026-tel-aviv-q4), together with the full agenda. Seats are approved by the organisers, so apply early.
