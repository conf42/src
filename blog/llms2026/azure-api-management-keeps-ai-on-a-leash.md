# Azure API Management as a leash for your AI endpoints

Conf42 Blog, 2026-06-11, updated 2026-11-09. https://www.conf42.com/blog/llms2026/azure-api-management-keeps-ai-on-a-leash

In short: Leo Visser of OGD at Conf42 LLMs 2026 demos token limits, content safety blocklists and semantic caching in Azure API Management in front of Foundry.

The cheapest LLM call is the one that never reaches the model. Leo Visser, a consultant at OGD ICT-diensten in the Netherlands and an Azure and PowerShell MVP, showed at Conf42 Large Language Models 2026 how putting Azure API Management in front of Azure AI Foundry gives you three practical controls: token-aware rate limits, content safety blocklists and semantic caching. It is a Microsoft-stack demo from start to finish, and a very hands-on one.

## A nature reserve that wanted less AI

The case behind the talk is unusual. A client, lightly disguised as a nature reserve management group, wanted an AI chatbot for staff and systems but also wanted to use it sparingly. They depend on donations, and supporters ask awkward questions about the energy and water that AI uses. They also wanted certain politically sensitive topics kept out of the chatbot entirely.

So the brief was a sustainable, restricted AI: useful, but on a leash. Visser says it was the first time a client asked him to limit topics, and that it made sense once he thought about it.

## The gateway in the middle

API Management, now also marketed as the AI gateway, sits between the application and the Foundry deployments. Visser walks through importing a Foundry endpoint as an API (there are dedicated options for Foundry, language model APIs and the newer A2A API), wiring the backend, and testing a gpt-5-mini chat completion from the portal. A small Power App drives the demos.

One detail worth noting from the demo: with gpt-5-mini he had to remove the max tokens parameter from the test body because that model does not support it.

## Limit tokens per consumer

The first control is the LLM token limit policy. Policies are XML, and in the demo he sets 60 tokens per minute, with optional quotas per hour, day, week, month or year, scoped per subscription key or IP address. Subscription keys are the useful unit: give each app, process or monitored area its own key and its own budget.

The demo also shows a gotcha. Three parallel requests all went through before the first response came back, because the gateway only knows the token count after the model answers. The fourth call was the one that got the limit-exceeded response.

## Block topics before the model sees them

The second control is AI content safety. You create an Azure Content Safety resource, then build a blocklist through its API, since the portal offers little to configure. Visser loops over a CSV of terms (for the demo, Azure service names such as App Service and Azure Functions), creates the list and adds each item. In API Management the content safety policy references the list by name.

The payoff is where the block happens. Asking about a blocked topic fails in the gateway, so the request never reaches the model, never burns reasoning tokens and never spends the energy. A system prompt telling the model to avoid a topic still runs the whole LLM.

## Cache answers that do not change

The third control is semantic caching. Before a prompt goes to the completion model, API Management embeds it with a small embedding model (text-embedding-ada-002 in the demo) and looks for a close enough vector in a Redis cache. A hit returns the stored answer; a miss calls the model and stores the result.

The settings are a similarity threshold and a cache duration, both tuned by trial and error. Static archives tolerate long durations; agents with RAG, tools or MCP servers need shorter ones. In the demo, the uncached version produces three slightly different answers slowly, while the cached version produces one slow answer and two instant, identical ones.

The setup notes are the kind you only get from someone who hit them: Azure Managed Redis needs the enterprise tier with RediSearch enabled, the connection string sometimes shows up without a port, only access keys work for the connection, and the AI gateway features need the Basic v2 tier. A confusing "role assignment already exists" error usually means the wrong tier.

## Who should watch

Azure teams putting Foundry models into production who need cost and content controls without writing them into every app, and platform teams that want one central gateway for many teams' models and MCP servers. If you are on another cloud, the patterns travel even if the clicks do not.

## Related Conf42 talks

- [AI-Driven Rate Limiting for Scalable, Secure, and Cost-Efficient APIs](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost) from Conf42 JavaScript 2025 looks at rate limiting from the other direction.
- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) from Conf42 DevOps 2026 is a good companion on gateway-level visibility and cost.
- [When AI Joins the Request Path: Securing API-Backed AI Systems](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) from Conf42 DevSecOps 2026 covers the security side of the same gateway.

[Watch Leo Visser's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Leo_Visser_governance_apis_control)

[Watch the talk on YouTube](https://youtu.be/eTT9MCGOKwU).

## Watch the talk

[Clean and Controlled AI with API Management](https://www.conf42.com/Large_Language_Models_LLMs_2026_Leo_Visser_governance_apis_control) at Conf42 Large Language Models (LLMs) 2026.
