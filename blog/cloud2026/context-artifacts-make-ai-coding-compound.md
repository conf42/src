# Stateless AI coding tools need a team memory you version

Conf42 Blog, 2026-03-30, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/context-artifacts-make-ai-coding-compound

In short: Gaurav Kumar of Amazon at Conf42 Cloud Native 2026 on context loss in AI development: living context artifacts, shared prompt templates, session handoffs.

Every new session with an AI coding assistant starts with you explaining, again, the architecture, the conventions and why that weird retry exists. At Conf42 Cloud Native 2026, Gaurav Kumar, Software Development Manager at Amazon with 15 years at the company, called context loss the critical bottleneck in AI-assisted development and proposed a three-pillar fix: living context artifacts, standardized prompt templates and structured session handoffs.

It is a practice-and-process talk from an engineering manager, not a tool demo, and it is aimed as much at team leads as at individual developers.

## The bottleneck is continuity, not capability

Gaurav's diagnosis is that most AI development happens in stateless environments. The tool has no memory of the project's architecture, trade-offs, standards or business use cases, so developers rebuild the same mental model before the tool is useful. The same thing happens without AI when a teammate picks up work after a few weeks: the decisions live in spreadsheets, documents or someone's head.

He names three costs. Repeated re-establishment of structure and conventions at the start of every interaction. Lost architectural memory, so earlier design decisions are invisible and suggestions drift. And shallow collaboration in larger teams, where the assistant cannot reason about how the project evolved or enforce team conventions. His summary: until AI can retain project context over time, it stays strong at isolated tasks and weak at sustained engineering work.

## Pillar one: living context artifacts

Keep continuously updated documents that act as the project's persistent memory for AI: architecture decision records kept current, a domain glossary, and a prompt catalogue, all reviewed and version-controlled alongside the code. The key move is treating them as first-class engineering assets rather than optional docs. Do that, he argues, and the AI can answer the way a senior teammate would, which cuts meetings with senior engineers and shortens onboarding.

## Pillar two: prompts as a team practice

Replace ad hoc prompting with structured templates that embed architecture and domain knowledge, shared and versioned across the team. His examples are the repetitive jobs: on-call tickets, digging through logs, working out why threads are eating a service's resources. A template also solves the blank-page problem; as he puts it, once you have a way to start, the work is rarely the hard part.

## Pillar three: deliberate session handoffs

At the end of a session, write a summary of the decisions made. At the start of the next, reload context in a standard sequence. Store the handoff artifacts in the team repository so anyone can pick up where someone else left off. This is the piece that makes progress carry across sessions and people.

## Compound interest, and what is coming

Gaurav's metaphor is simple versus compound interest: plain AI use gives linear gains, while context carried across coding, testing, documentation and review compounds. He points at emerging stateful AI environments, with agents that retain memory, tool-use state and decision history across sessions, and argues that teams with good context habits now will adopt those fastest.

His starter kit is pleasantly small: audit where people keep re-explaining project context, build templates for the three most common AI tasks on your team, create the living artifacts (ADRs and glossary, co-located with code, reviewed every sprint) and agree a lightweight end-of-session summary format.

## Who should watch

Team leads rolling out AI coding assistants across more than a handful of developers, and anyone whose CLAUDE.md or rules file has grown by accident rather than design. Engineers looking for tool-specific configuration will need to translate the patterns themselves.

## Related Conf42 talks

- [Emerson Braun on engineering context, contracts and reliable agent behaviour](https://www.conf42.com/Prompt_Engineering_2026_Emerson_Braun_contracts_context_agent) at Conf42 Prompt Engineering 2026.
- [Suneet Malhotra on a production Claude Code and MCP agent pipeline](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) at Conf42 AI Agents 2026.
- [Kabir Ibraheem on riding the AI wave as a fullstack engineer](https://www.conf42.com/AI_Agents_2026_Kabir_Ibraheem_fullstack_tooling_productivity) at Conf42 AI Agents 2026.

[Watch Gaurav Kumar's talk](https://www.conf42.com/Cloud_Native_2026_Gaurav_Kumar_cloudarchitecture_microservices_backend)

[Watch the talk on YouTube](https://youtu.be/1ep_FtCWUpc).

## Watch the talk

[Context-Aware AI Development: Unlocking the Next Wave of Engineering Productivity](https://www.conf42.com/Cloud_Native_2026_Gaurav_Kumar_cloudarchitecture_microservices_backend) at Conf42 Cloud Native 2026.
