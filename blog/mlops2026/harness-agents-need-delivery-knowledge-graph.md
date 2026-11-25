# Agents need a map of your delivery system, not a longer tool list

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/harness-agents-need-delivery-knowledge-graph

In short: Sunil Gattupalle (Harness) at Conf42 MLOps 2026 on giving agents a typed knowledge graph of software delivery instead of raw API payloads and tool lists.

Give an agent your REST API spec and it knows what each endpoint does. It has no idea *when* to call it. At Conf42 MLOps 2026, Sunil Gattupalle, Engineering Architect at Harness, argued that this missing "when" is the context agents lack in software delivery, and showed how Harness models it as a knowledge graph of entities, events, metrics and relationships that agents query in one language.

It's a vendor talk about a vendor system, and Sunil says so by working in Harness's own terms throughout. But the modelling ideas travel well beyond Harness, and the half of the talk on *why* raw tool lists make agents worse is useful to anyone building MCP servers.

## Why does the API spec leave agents guessing?

Sunil starts with a short history of enterprise software: systems of record, then systems of engagement, then automation with CI/CD and Kubernetes. Reasoning is the next layer, where a system picks dynamic actions at run time instead of replaying behaviour someone coded in advance.

The catch sits in the contract. "The part that is not present in the API specification is when do you use it," Sunil said at Conf42 MLOps 2026. That reasoning used to live in documentation or in the developer's head. For agents it has to be codified and handed over as context.

Delivery makes it sharper. Generating code has become easy, and the rest of the pipeline has to absorb that pace of change while keeping its guardrails, which he calls non-negotiable in enterprise software. Coding can afford flexibility; the further right you move towards production, the more determinism you want, without switching off the agent's ability to reason.

## What goes into the graph?

Across every Harness module, the team sorted data into four buckets:

- **Entities**: the things you touch, such as pipelines, services, environments, artifacts, vulnerabilities and teams, each with a lifecycle.
- **Events**: immutable, point-in-time facts that happen to entities.
- **Metrics**: aggregations over events or lifecycles.
- **Relationships**: the edges, which Sunil describes as the part that makes the graph traversable.

The path he keeps returning to runs from pull request to commit to artifact, to artifact registry, to a pipeline, to an environment and finally to a running service. Because Harness runs those pipelines, it can see the whole path.

The incident question shows why that matters. Sunil's team asks the same thing every time: what changed? "Something must have changed, whether it is configuration that changed, whether it is code that has changed," he said. Answering it is a traversal: which service, how and when it was deployed, which artifact, which commit, which policy applied to the pipeline, which team owns it. The graph encodes that mental model as metadata so an agent can pick the relevant subgraph instead of rediscovering it.

## How does an agent query it?

Each entity type is declared with its dimensions, the operations allowed on them and a note on when to use the type. The graph is hydrated as you use the product: triggering a pipeline, scanning, creating commits and integrating Jira, GitHub and PagerDuty all land in a data lake, normalised and partitioned by tenant. Every query is scoped by the caller's RBAC permissions.

On top sits a SQL-like query language the talk calls HQL. The agent's loop is:

1. Discover which types exist in the account.
2. Pick the ones relevant to the question.
3. Drill into their dimensions, which is the equivalent of choosing projections, predicates and aggregations.
4. Validate the query it built.
5. Execute and return results.

The design point is the vocabulary. Sunil's team could have exposed all this through MCP as long tool lists with raw API payloads, and says that would have polluted the context window and made the agent reason worse. Typed, declared metadata gives the agent grounded data to work from, and "they just need to learn one language".

## What did the demo show?

On Harness's own environment, which Sunil calls "Harness on Harness", he asks the agent to explain the path from commit to artifact to deployment to environment. The thought process on screen goes breadth first (list the metadata), then narrows to a subgraph and goes depth first, validating each query before executing it. He then asks the AI to visualise the answer, which produces a dashboard whose query you can inspect in code mode, and shows a worker agent for pipeline failure analysis that takes a look-back window and an org and project filter and returns a report on the past thirty days of executions. Inference can go through your own LLM gateway via a connector.

Sunil also mentions that some models seem to prefer the Harness CLI over MCP for the same graph, and that delivery and runtime context in a coding agent adds blast radius and ownership to what the code alone can tell it.

## Who should watch

Platform and MLOps engineers wondering what context their agents are missing, and anyone designing an MCP server who suspects that more tools is not the answer. If you want a vendor-neutral benchmark of knowledge graphs against plain tool calling, this isn't it: there are no numbers comparing the two, and the product sections assume you use Harness.

Related Conf42 talks: [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg of Microsoft AI at the same event, [Your Agent Failed Mid-Run. Logs Won't Replay It.](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) by Reza Amini of Flashback, and Jimmy Caputo's [Agentic Engineering Platforms](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) from Harness at Platform Engineering 2026.

[Watch Sunil Gattupalle's talk](https://www.conf42.com/MLOps_2026_Sunil_Gattupalle_agents_software_delivery) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## From Harness

Sunil says the knowledge graph is available to Harness customers through Harness AI chat, the hosted or self-hosted Harness MCP server, the Harness CLI and custom dashboards. The graph is built as you use Harness; you don't have to ask for it.

- Harness: [harness.io](https://www.harness.io/)
- Free plan sign-up: [app.harness.io](https://app.harness.io/auth/#/signup?utm_source=webinar&utm_medium=webinar&utm_campaign=2026q4-conf42-mlops)

[Watch the talk on YouTube](https://youtu.be/xNfalEBNZZ4).

## Watch the talk

[What Your Agents Need to Know About Software Delivery](https://www.conf42.com/MLOps_2026_Sunil_Gattupalle_agents_software_delivery) at Conf42 MLOps 2026.
