# Route agent traffic through a gateway and the LLM bill gets a dashboard

Conf42 Blog, 2026-01-03, updated 2026-11-09. https://www.conf42.com/blog/devops2026/llm-cost-per-gateway-agentgateway-grafana

In short: Michael Levan (Solo.io) at Conf42 DevOps 2026 demos agentgateway on Kubernetes plus Prometheus and Grafana to track LLM tokens and cost per gateway.

Agents call LLMs, MCP servers and other agents, and the first question finance asks is who spent what. At Conf42 DevOps 2026, Michael Levan, AI architect and solutions engineer at Solo.io, answered it with a live terminal demo: route all that traffic through agentgateway on Kubernetes, scrape its metrics with Prometheus, and read token usage and cost per gateway off a Grafana dashboard.

This is a vendor-adjacent demo talk: Levan works at Solo.io and the demo uses agentgateway end to end, built step by step with kubectl, curl and Grafana.

## Three gateways, one model, on purpose

After installing agentgateway, Levan creates a Kubernetes secret holding an Anthropic API key. Any LLM provider would do; Anthropic is simply where he has a subscription.

He then creates three gateways. The number is arbitrary, chosen so the dashboard has something to break down. Each one is three objects:

- a **Gateway** from the Kubernetes Gateway API CRDs, using the agentgateway class, accepting routes from all namespaces for testing;
- an **agentgateway backend**, which tells the gateway where to send traffic, here a Claude model, though it could just as well be an MCP server;
- an **HTTPRoute** that references both and gives you an endpoint to hit.

A nice detail for anyone who has typed it too often: the route rewrites the OpenAI-style chat completions path to a short `/anthropic` prefix. Levan also heads off the obvious question about why a Claude backend uses the chat completions path at all: Claude supports the OpenAI API format, so it works as expected.

## Generate traffic, then make it visible

With the three gateways up, he exports their load balancer IPs into environment variables and curls each one. The point is partly to prove routing works and partly to generate metrics.

For observability he installs kube-prometheus, his usual choice because it ships Prometheus and Grafana with a set of Kubernetes dashboards already in place, instead of an empty Grafana. Then come pod monitors, one per gateway, each scraping the gateway's metrics endpoint every 30 seconds. There's a small live fix along the way: the gateways now deploy into the `agentgateway-system` namespace rather than the older `kgateway-system`, so the monitors needed updating. Demos that include the namespace rename are the honest kind.

## Cost per gateway, tokens per request

The payoff is a custom Grafana dashboard, published on Levan's GitHub, that shows cost per gateway and for all gateways combined. In his case the spend was small enough that he was still in budget.

Below the dashboard, the raw agentgateway metrics in Prometheus are where the useful slicing happens. Token usage can be broken down by which gateway received the request, which model served it and where it originated. That is the attribution a platform team needs before it can set budgets or rate limits per team.

## Why the gateway pattern matters

The demo is small, but the shape is the useful part. Put every agent-to-LLM, agent-to-MCP and agent-to-agent call through a gateway you control, and cost tracking becomes a metrics problem you already know how to solve, using the Prometheus and Grafana stack most Kubernetes teams run anyway. Splitting traffic across gateways (per team, per product, per environment) is what turns one big invoice into numbers someone can own.

## Who should watch

Platform engineers who have been asked to put guardrails on agent spend and want to see the moving parts in a terminal. If you already run the Kubernetes Gateway API, most of this will feel familiar, which is rather the point. If you were hoping for a deep comparison of AI gateways, this is a hands-on walkthrough of one.

## Related Conf42 talks

- [The Retry Storm That Ate My Budget](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty (AWS) digs into the hidden cost loops in agentic AI.
- [From 150K to 22K Tokens: Context Engineering for MCP Tool-Calling](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) by Nishant Kumar Thakur (Adobe) cuts the tokens before they reach the gateway.
- [Beyond Token Counts: Observability for AI Coding-Agent Trajectories](https://www.conf42.com/Observability_2026_Elliot_Gardiner_agents_codegeneration_tracing) by Elliot Gardiner (Code Telemetry) asks what to observe beyond tokens.

[Watch Michael Levan's talk](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs)

[Watch the talk on YouTube](https://youtu.be/OAwmnmY-IO0).

## Watch the talk

[Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) at Conf42 DevOps 2026.
