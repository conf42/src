# A dashboard agent that profiles its MCP data before you ask

Conf42 Blog, 2026-09-01, updated 2026-11-09. https://www.conf42.com/blog/agents2026/mcp-dashboard-agent-profiles-data-first

In short: Rohit Deshpande and Scott Young of SAP at Conf42 AI Agents 2026 demo a LangGraph agent that turns prompts into live, editable dashboards over MCP servers.

Connecting an agent to an MCP server is the easy part; knowing what the data behind it actually looks like is what decides whether the chart is true. At Conf42 AI Agents 2026, Rohit Deshpande, Senior Staff Engineer at SAP, and his colleague Scott Young demoed a system that turns a typed question into a live dashboard, and the trick is that the agent studies each new data source and writes its own manual before anyone asks a question.

The talk is almost entirely a live demo, run as a conversation: Scott asks the product-manager questions, Rohit drives.

## Profile first, query later

When you register an MCP server (base URL, transport type), a profiling workflow kicks in. It discovers the tools, records each one's inputs and outputs, makes real sample calls, clusters related tools (sales with sales, customers with customers) and writes a usage guide that gets fed to the agent on later queries. The point is to save latency and tokens on every call that follows. In the demo the server exposes six tools, and the generated guide shows the clusters and the actual calls made.

With the server selected, asking what data it is connected to returns sales orders, customers and a product catalog. A question about which region had the lowest sales growth last quarter gets a plain answer (APAC) and, correctly, no dashboard.

## Seven small nodes, one with real reasoning

The backend is Python on LangGraph with seven nodes: router, conversation agent, clarifier, planner, fetcher, builder and saver. Simple questions route to the conversation agent. "Visualize this sales data as a dashboard" routes to the planner, the one node doing heavy reasoning, which picks bar and line charts and renders them progressively as data arrives.

The planner keeps a small tool belt on purpose. Tool discovery is delegated to the fetcher, which has two sub-agents: a discoverer and an executor. Tool schemas live as JSON files in a virtual file system backed by Redis, and the discoverer navigates them with four tools: `tree`, `grep`, `cat` and `select`. Tools as files is a neat answer to the context bloat you get from connecting several MCP servers with hundreds of tools between them. Builder converts raw tool responses into the JSON the front end understands; saver persists it. Single responsibility, applied to agents.

Edits are deltas. Ask to add a US West chart by product category and the agent, which already has the canvas in context, fetches only that slice instead of regenerating everything. Deletes work the same way, so dashboards get CRUD by conversation. The abstract adds the plumbing behind this: append-only versioning in Cassandra, and every step streamed to the front end over GraphQL subscriptions.

## How the numbers stay honest

Scott's best question is whether the LLM could hallucinate the values in a chart. Rohit's answer is four tiers:

1. **Profiling.** Real sample calls, distinct-value counts, cardinality and patterns per field, with identifier-like columns flagged. It reads data, not column names.
2. **Value-overlap ontology.** To join two sources, it checks whether the actual key values overlap (does customer 001 from source A appear in source B?) and rejects columns that merely look joinable by name.
3. **Recipe binding.** Domain templates written and verified by experts. The agent can apply business logic; it can't invent it.
4. **Execution.** The executor runs the SQL or API calls and returns real responses.

On top sits an explainability feature: select a chart and ask how it was generated, and you get the tool call, the data queried, why a bar chart, and a short insight, all saved at generation time. A cross-source request for customers with high revenue but low margin shows the tiers working together.

## Who should watch

Teams building natural-language analytics over enterprise systems, and anyone fighting tool overload with several MCP servers attached. The demo is short and dense, so watch it for the architecture pattern rather than the UI. Everything shown is built on open source pieces (LangGraph, Deep Agents, Cassandra, Postgres, GraphQL), so the design transfers.

## Related Conf42 talks

- [From 150K to 22K Tokens: Context Engineering for MCP Tool-Calling](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) by Nishant Kumar Thakur and Sonam Raj at Conf42 Prompt Engineering 2026.
- [Closing the Semantic Gap with Feedback-Driven Ontology Learning](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) by Ravi Chandra at Conf42 Observability 2026.
- [Building an MCP Server in Go for a Real B2B Workflow](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) by Shadi Elyafi at Conf42 Golang 2026.

[Watch Rohit Deshpande and Scott Young's talk](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/eYYo9EIJT-A).

## Watch the talk

[From Prompt to Production Dashboard: Agentic AI with MCP Servers and Live Data](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) at Conf42 AI Agents 2026.
