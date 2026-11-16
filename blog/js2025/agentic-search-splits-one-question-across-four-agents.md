# Agentic search splits one question across four kinds of agents

Conf42 Blog, 2025-10-15, updated 2026-11-09. https://www.conf42.com/blog/js2025/agentic-search-splits-one-question-across-four-agents

In short: At Conf42 JavaScript 2025, Ajitha Buvanachandran showed how research, analysis, domain and QA agents in Node.js turn search into answers.

Search engines hand you a pile of documents and wish you luck. At Conf42 JavaScript 2025, Ajitha Buvanachandran, a principal machine learning and generative AI engineer at an investment firm (listed on the talk page with Anna University), argued that the fix is to stop retrieving and start investigating: split the question across specialised agents, and let Node.js do the coordinating.

The talk is an architecture overview with one worked example, which makes it a good map before you start wiring agents together yourself.

## The question nobody's keyword index can answer

Her running example is a financial company whose leadership asks why mobile banking satisfaction went down and what to do about it. A keyword search matches every document that contains "mobile", "banking", "satisfaction" and "decline", including hardware specs for mobile phones. Someone then spends days reading.

Semantic search does better: it understands that the question is about customer experience and returns survey results, NPS scores and feedback analysis. But a human still has to put the story together.

The third generation, agentic search, aims to hand back the story itself. In her example the agents pull metrics from CRM data, app store reviews, support tickets and social media monitoring, notice that the satisfaction drop lines up with a mobile app release, tie user complaints to navigation complexity from a UI redesign, and check the finding against seasonal effects and sampling bias before anyone sees a report.

## Four roles, four phases

The architecture has four agent types:

- **Research agents** break the query into parts and fetch data from databases, documents and external sources.
- **Analysis agents** look for patterns and correlations using statistics and ML.
- **Domain expert agents** add industry context, such as how similar dips played out at other banks.
- **Quality checking agents** look for bias, accuracy problems and gaps.

They work in four phases: query interpretation, distributed execution (research and early analysis run in parallel), collaborative synthesis, and quality validation before delivery. The validation step is the part most hand-rolled agent demos skip, and here it has its own agent.

## Why JavaScript gets the coordinator job

Her case for JavaScript is about the event loop, not about raw model performance. Coordinating agents mostly means waiting: on LLM calls, vector lookups and other services. Node.js's non-blocking I/O handles many concurrent agent requests without stalling, and Express or NestJS give you the microservice scaffolding. The building blocks she lists are LangChain.js for chains, agents and streaming; a vector database for retrieval-augmented generation over private data; message queues and event buses for passing messages between agents; and a validation pipeline at the end.

The rollout path is practical: define agent personas and protocols, build an event-driven orchestration layer, connect vector stores, semantic search and LLM APIs, then add quality pipelines before production.

## The bill comes in latency and tokens

She doesn't pretend multi-agent setups are free. Coordination adds overhead, which she suggests fighting with caching, parallel execution and streaming partial results. LLM costs pile up fast, so batch calls, cache results and pick the model per task. Debugging a distributed agent pipeline needs logging and tracing across the whole orchestration path, and the QA agents have to catch bias in the data as well as in the model output. Her framing is that these are engineering problems with known fixes, not reasons to stay away.

## Who should watch

JavaScript and Node.js developers asked to "add AI search" to an internal data platform, and architects deciding whether agent orchestration belongs in their existing Node services. If you want code walkthroughs, this one stays at diagram level; pair it with something hands-on.

## Related talks

- [Implementing Agentic AI Solutions in Python from scratch](https://www.conf42.com/Python_2025_Craig_West_agentic_ai_django) builds the agent loop by hand, the hands-on follow-up to this architecture.
- [Beyond Text Generation: The Rise of Agentic AI and Its Transformative Potential](https://www.conf42.com/Machine_Learning_2025_Naman_Goyal_generation_text_agentic) steps back to what makes a system agentic at all.
- [Langchain with Golang](https://www.conf42.com/Golang_2024_Alexandre_Evangelista_de_Souza_langchain) shows the same chain-and-agent ideas outside JavaScript.

[Watch Ajitha Buvanachandran's talk](https://www.conf42.com/JavaScript_2025_Ajitha_Buvanachandran_agentic_search_multi)

[Watch the talk on YouTube](https://youtu.be/9maZ9zMCM9E).

## Watch the talk

[Agentic Search with JavaScript: Multi-Agent Intelligence for Next-Gen Insights](https://www.conf42.com/JavaScript_2025_Ajitha_Buvanachandran_agentic_search_multi) at Conf42 JavaScript 2025.
