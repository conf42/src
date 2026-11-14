# AI's best job in enterprise teams is carrying the mental model

Conf42 Blog, 2026-03-29, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/ai-for-the-invisible-complexity-of-enterprise-systems

In short: Dreema Patel of Adobe at Conf42 Cloud Native 2026 on three ways AI eases invisible complexity: RAG over internal knowledge, assisted coding, and failure-led tests.

In a platform with hundreds of services, nobody holds the whole map, and the gaps only show up when a deployment fails at 2 a.m. At Conf42 Cloud Native 2026, Dreema Patel, Software Engineer at Adobe, argued that the real bottleneck in cloud-native enterprises is human cognition rather than infrastructure, and laid out three places where AI helps carry that load: knowledge retrieval, assisted development and data-driven testing and onboarding.

It is an overview talk aimed at engineering teams rather than a product walkthrough, and it works best as a framing for where to point AI first.

## Invisible complexity

Dreema's term for the problem is invisible complexity. Microservices, micro-frontends and real-time distributed systems let teams scale and deploy continuously, but they replaced one system with hundreds of interconnected parts. Each engineer knows their own services and a few dependencies; past that it gets fuzzy. That complexity does not go away because nobody looks at it. It builds up, and it becomes visible exactly when something times out or a dependency breaks. When system complexity grows faster than team understanding, she says, you get slower cycles, longer debugging and more incidents.

## Pillar one: make institutional knowledge queryable

Every organization piles up API contracts, design docs, PRDs and tickets. The answers usually exist somewhere; finding them costs time and focus, because every hop between docs, code, old tickets and a colleague's calendar is a context switch. Teams end up re-solving problems that were already solved.

Her answer is retrieval-based systems over your actual internal sources. Generic answers are useless inside an enterprise; you need ones that know your architecture and dependencies. RAG bridges static documentation and live context, so engineers start from accumulated experience instead of a blank page.

## Pillar two: move engineers up a level

Much development time goes to boilerplate, test plans, small fixes and repeated validation. AI can generate service scaffolding, complete complex logic, write unit tests and validate patterns while you code, which keeps engineers in flow. Dreema is careful about the limit: AI can generate code, but it does not grasp long-term system behaviour, business context or architectural trade-offs. The shift she wants is from asking how to write this code to asking what the right design is, which trade-offs to make, and how it will scale.

## Pillar three: test what actually broke before

The testing argument is the most concrete. Traditional tests are predictive: we test what we imagine might fail, while production fails in ways we did not imagine. AI can turn that around by mining history. Which combinations of services have failed together? Which files change constantly and are therefore likely unstable? She breaks it into three steps: analyse historical defects, generate scenarios aimed at failure-prone logic and service interactions, and validate over time which tests earn their keep and which are redundant.

Onboarding gets the same treatment. Instead of a new engineer spending weeks working out which services exist and who owns what, they ask how authentication works and get a walkthrough of the services, dependencies and key pieces, without waiting for a senior engineer to free up.

## The summary in one line

Knowledge becomes queryable, development becomes higher-level, testing follows real failures, and onboarding speeds up because context is always available. AI here is an intelligent layer across the platform, with engineers as the decision makers.

## Who should watch

Engineering managers and platform leads deciding where AI investment pays off first, and engineers new to applying RAG inside a company. If you are looking for benchmarks or a specific implementation, the talk stays conceptual.

## Related Conf42 talks

- [Kemet Dugue on agentic workflows for Uber's driver onboarding team](https://www.conf42.com/AI_Agents_2026_Kemet_Dugue_workflows_productivity_onboarding) at Conf42 AI Agents 2026.
- [Srinivas Chennupati on production-ready RAG for enterprise knowledge](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) at Conf42 Platform Engineering 2025.
- [Christian Denich and Robert Hoffmann on thinking developer productivity before developer platforms](https://www.conf42.com/Cloud_Native_2024_Christian_Denich_Robert_Hoffmann_developer_productivity_platforms) at Conf42 Cloud Native 2024.

[Watch Dreema Patel's talk](https://www.conf42.com/Cloud_Native_2026_Dreema_Patel_ai_llm_inference)

[Watch the talk on YouTube](https://youtu.be/sOgppF3gxIQ).

## Watch the talk

[AI as a Force Multiplier for Cloud Native Enterprise Development](https://www.conf42.com/Cloud_Native_2026_Dreema_Patel_ai_llm_inference) at Conf42 Cloud Native 2026.
