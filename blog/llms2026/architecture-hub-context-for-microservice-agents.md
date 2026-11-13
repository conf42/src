# An AI-maintained architecture hub so agents can reason across services

Conf42 Blog, 2026-05-24, updated 2026-11-09. https://www.conf42.com/blog/llms2026/architecture-hub-context-for-microservice-agents

In short: Lior Schejter at Conf42 LLMs 2026 on a Git repo of AI-written markdown facets that gives agents system-wide context across many microservices.

Drop a coding agent into one repository and it feels like magic. Ask it to fix a bug spanning six microservices and it's flying blind. At Conf42 Large Language Models (LLMs) 2026, Lior Schejter, Lead R&D Architect, shows how he fixed that with an Application Architecture Hub: a plain Git repo of markdown files that AI agents write, keep current on every merge, and read when they need the system-level picture.

The best part is how little infrastructure it needs. No graph database, no wiki platform, no servers.

## The same AI that's hungry for context can write it

The underlying problem predates AI. In a large microservice system, tracing a flow across services, or finding where data is used and changed, is possible but slow and doesn't scale. Humans are notoriously bad at keeping documentation current. Agents raise the stakes because they need that documentation to work well, and they also happen to be good at producing it: reading code, matching semantics, doing it tirelessly.

## Flat files beat the graph database

Lior's team did prototype graph databases first, because modelling a system as a graph feels natural. Flat markdown won. Agents read it natively, Git provides versioning, diffs and pull requests for free, and there is nothing to operate. He calls the robust architecture a temptation the team decided was premature optimisation.

The unit of ingestion is one repo, but documentation is split into facets: domain models, exposed APIs, events, dependencies and more. Questions to the hub tend to cut across services along one facet. Tracing a bug wants events and APIs for a set of services; assessing blast radius wants dependencies. Facets also make ingestion parallel and retries cheap.

A strict naming convention maps a repo and a facet to exactly one file path. If you know what you're looking for, you know the file name, with no search or lookup in between.

## Agents write it, scripts check it, citations keep it honest

An orchestrator agent dispatches one sub-agent per facet. Each reads the same repo, extracts its slice, and writes its own file, so they run concurrently without polluting each other's context, and a failure retries only that facet.

Early on, the ingestion agent was asked to lint its own output. That was unreliable, and since every check was mechanical (file locations, broken links, front matter), it moved into a script. His summary is an old lesson: don't use AI where you don't need it.

A GitHub Actions workflow triggers updates on merges to main for relevant repos, and opens a pull request for human review. Those reviews caught real gaps, like a non-standard Kafka publishing pattern in some repos that left events undocumented; the skill was updated to recognise it. With confidence built up, updates can merge automatically.

The single most effective measure against hallucination and run-to-run drift: requiring every claim to cite a file name and line numbers. Structured templates helped too, and repos built on consistent frameworks such as NestJS produced noticeably better documentation than older, looser code. To control cost, an update skill diffs the code against the hub and rewrites only what changed.

## Querying is where the value is

Query skills, distributed as a plugin to the team's Cursor installations, tell agents how to navigate the hub and connect files. An incident troubleshooting agent uses the hub alongside its log, Jira and Slack tools. Ready-made reports turn common questions into one prompt: a dependency map for a repo (including implicit dependencies through a shared database), flow descriptions with a plain-English variant for product managers, and architecture overviews for onboarding.

The latest step maps business terms to the repos that own or consume them. Because those mappings can't be anchored in code, low-confidence ones go to a human audit, and confirmed mappings survive future updates.

He says the initial prototype took one or two weeks, built mostly by one person.

## Who should watch

Teams with dozens or hundreds of services who want agents to help beyond a single repo. It's also a good reference for anyone tempted to build a knowledge platform before trying a folder of markdown.

## Related Conf42 talks

- [Context Engineering for DevOps: Turning Your Infrastructure into a Reasoning Graph](https://www.conf42.com/DevOps_2026_Roxane_Fischer_context_reasoning_infrastructure) by Roxane Fischer, the graph approach Lior decided against, applied to infrastructure.
- [Prompting Is Not the System: Engineering Context, Contracts and Reliable Agent Behavior](https://www.conf42.com/Prompt_Engineering_2026_Emerson_Braun_contracts_context_agent) by Emerson Braun, on context as an engineered artifact.
- [Scaling Microservices Observability with Agentic LLMs](https://www.conf42.com/MLOps_2026_Nishanth_Vepachedu_microservices_observability_llms) by Nishanth Vepachedu, for the troubleshooting-agent side of a large service estate.

[Watch Lior Schejter's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lior_Schejter_context_agents_reasoning)

[Watch the talk on YouTube](https://youtu.be/xUtMaen3D3Y).

## Watch the talk

[Beyond the Context Window: Building a "Mental Model" for Your AI Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lior_Schejter_context_agents_reasoning) at Conf42 Large Language Models (LLMs) 2026.
