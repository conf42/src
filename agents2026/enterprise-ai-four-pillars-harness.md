# Enterprise AI in four pillars: context, evals, memory, governance

Conf42 Blog, 2026-09-24, updated 2026-11-09. https://www.conf42.com/agents2026/enterprise-ai-four-pillars-harness

In short: Shubham Jindal of Harness at Conf42 AI Agents 2026 on why AI demos stall before production, and the four pillars that get agents there.

An AI demo takes days to build and wows the room; the production version can take months and still embarrass you in front of a customer. At Conf42 AI Agents 2026, Shubham Jindal, Director of AI at Harness, laid out the blueprint his team uses to close that gap: four pillars called context, evals, memory, and governance, each with concrete habits you can copy.

This is a sponsor keynote, and Shubham says up front that Harness has built all four pillars into its own AI for the software delivery pipeline. But the talk is a framework, not a product tour. Almost everything in it applies to any team shipping agents to paying users.

## Demos run on prompts, production runs on context

Shubham's opening claim is that the mindset has to shift from prompt engineering to context engineering. In a demo you are not throwing large data at the model, so a clever prompt carries the day. In production the model meets your siloed systems, your company jargon, and your sensitive data, and that is where it starts to make things up with great confidence.

His line for it: "Context is the new code." His team's case is personal. Harness has separate CI, CD, and code products, and an LLM trained on the whole internet does not know that CI means something specific inside Harness.

He gave four practical tricks for keeping the context window healthy:

- **Compaction.** Summarise the conversation as it nears the limit and keep only the decisions. He compares it to a garbage collector.
- **Large outputs go to files.** A Jira or GitHub MCP call can return a giant JSON blob. Write it to a file and let the agent read the slice it needs, instead of flooding the window.
- **Context editing.** Proactively drop dead ends, like the five wrong Gradle commands the agent tried before finding the right one.
- **Semantic augmentation.** Load skills and reference material when they become relevant, not all at once in the system prompt.

## A knowledge graph is the compiler for your context

The most useful example in the talk is a question that sounds simple: which of my PRs caused an incident last week? The answer crosses the PR, the CI run, the CD deployment, the version that shipped, and the on-call page. Ask an agent to stitch that from three raw data sources and it will guess at relationships it does not understand.

Shubham's fix is to extract the entities you care about (services, users, incidents, releases), enrich them with metadata such as owners, link them into a graph, and expose that graph through an API the agent can query and walk. If context is the new code, he says, the knowledge graph is its compiler.

## Evals should fail on purpose

The second most important pillar, in his ranking, is evals. Unit tests assume deterministic code; agents are probabilistic, so many teams skip testing entirely because they cannot define what good looks like. His example is model switching: an agent tuned on Opus burns too many tokens, so you want to try Sonnet. Without evals you are changing a model name and hoping.

The framework he described:

- LLM-as-a-judge checks, ideally with a different model than the one being judged.
- Regression evals as a quality gate in CI/CD before any prompt, temperature, or model change ships.
- Evals on production traces. Harness runs a simple user temperament check that asks whether the user seems frustrated, types in caps, or repeats the same question.
- Every production failure becomes a new eval case.

The idea worth stealing is that an eval suite should not pass at 100%. Treat it like a benchmark: if 80 of 100 cases pass today, a change that moves you to 85 is progress and one that drops you to 75 is a regression. A suite that always passes can only tell you about the cases you already solved.

## Memory makes an assistant, governance makes it shippable

On memory, Shubham separates short-term memory (the current session) from long-term memory that bubbles up patterns, such as which repos a team works in or what a user keeps asking about. His summary: chatbots forget, assistants remember. He also traces the arc from chatbot to in-app assistant to autonomous agent, with examples like an agent that watches a PR's CI, fixes failures, and pushes until it is green.

Governance he calls the boring pillar enterprises care about most. He splits it into scoped access (do not hand an agent every tool in the GitHub MCP when it only needs a few), guardrails such as PII redaction and EU data residency, real-time content filters, and full audit trails of tool calls and model versions. Governance, in his words, is the new runtime, because it only exists while the agent is running.

## Who should watch

Engineers and leads who have a working agent prototype and a nervous security team. The context-window tricks and the "evals as benchmarks" framing are worth the time on their own. If you are still deciding whether to build an agent at all, start elsewhere.

Related talks from other Conf42 events:

- [Hilik Paz on how to evaluate your evals](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) at Conf42 LLMs 2025.
- [Srikanth Devarakonda on LLM evals and benchmarks](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) at Conf42 Observability 2026.
- [Prateek Mittal on knowledge graphs in software delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) at Conf42 LLMs 2026.

[Watch Shubham Jindal's talk](https://www.conf42.com/AI_Agents_2026_Shubham_Jindal_ai_demo_enterprise) or see the whole [Conf42 AI Agents 2026 lineup](https://www.conf42.com/agents2026).

## From Harness

Harness covers the delivery side of software, from CI and CD pipelines to testing and security, with an AI layer aimed at speeding up the path from merged code to production.

- [Harness website](https://www.harness.io/)
- [Create a free Harness AI account](https://app.harness.io/auth/#/signup?utm_campaign=conf42&utm_source=youtube)

[Watch the talk on YouTube](https://youtu.be/sYmfZfIvFbM).

## Watch the talk

[AI Demos Are Easy. Enterprise AI Is Not](https://www.conf42.com/AI_Agents_2026_Shubham_Jindal_ai_demo_enterprise) at Conf42 AI Agents 2026.
