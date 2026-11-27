# Amazon Bedrock AgentCore: the primitives between PoC and production

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/bedrock-agentcore-poc-to-production

In short: Samuel Baruffi (AWS) at Conf42 MLOps 2025 on AgentCore runtime, identity, gateway, memory and observability for shipping enterprise AI agents.

Most agent projects work fine on one developer's laptop. The trouble starts when they need auth, scale, memory and an audit trail. At Conf42 MLOps 2025, Samuel Baruffi, Principal Global Solutions Architect at AWS, toured Amazon Bedrock AgentCore, a set of pick-and-choose primitives for running agents in production, from serverless runtime and identity to an MCP gateway with semantic tool search.

This is an AWS product talk, and Samuel is upfront about it. It was recorded on September 5, 2025, while AgentCore was still in preview, so check current docs for what has changed since.

## Why PoCs stall

The pattern Samuel kept hearing from customers: an agent PoC runs locally, then hits four walls on the way to production. Performance, scalability, security and governance. AgentCore is AWS's answer, and the key design choice is that each piece can be used on its own. You do not have to buy the whole ecosystem; you can bring your own framework (Strands, LangGraph, LangChain, CrewAI or your own) and your own model, including non-Bedrock ones.

He also clarifies a common confusion: Bedrock Agents, which has existed for about two years, is the more opinionated option. AgentCore is the lower-level, more flexible set of building blocks.

## Runtime and identity

**AgentCore Runtime** is serverless compute for agents. You add a decorator, package a Docker image to ECR, and invoke the agent through an API. Sessions get true isolation, scale from zero, and can run for up to eight hours. Runtime can also host a remote MCP server, for example one built with FastMCP.

**AgentCore Identity** handles both directions of auth. Inbound: who may invoke this agent, using existing providers like Okta, Azure AD or Amazon Cognito over OAuth 2.0, without migrating users. Outbound: how the agent gets IAM permissions for AWS resources, or API keys and OAuth flows for third parties like Salesforce or Google Drive.

## The gateway and its tool search

**AgentCore Gateway** is a managed MCP server. Point it at an OpenAPI schema or a Lambda function, and those endpoints become MCP tools behind authenticated access. One gateway can have many targets, and each target many tools.

The feature Samuel clearly enjoys is semantic search over tools. If your gateway exposes 360 tools, a plain list-tools call returns all of them, which bloats context. Instead the agent can ask the gateway for tools relevant to a task (his example: creating a social media post) and get back four. His reasoning is the right one: "the more tools you provide, the less accuracy you have", plus more latency and more tokens billed. It is essentially a small RAG system over your tool catalogue.

## Memory, browser, code and traces

**AgentCore Memory** splits short-term memory (raw conversation turns, stored for a configurable period) from long-term memory, which is extracted asynchronously as semantic facts, user preferences or summaries. Storage is per-customer with namespaces and bring-your-own encryption.

**Browser** gives agents isolated, serverless headless browsers with live-view streaming and session replay. **Code Interpreter** runs model-generated code in isolated sandboxes with no root access. **Observability** ships prebuilt CloudWatch dashboards and traces of every model and tool call, and exports OpenTelemetry if you use another backend.

Samuel closes by pointing to the AgentCore samples repository on GitHub, the docs and the blog.

## Who should watch

Teams on AWS with an agent stuck at PoC, and anyone designing agent infrastructure who wants a checklist of the primitives production needs, whatever cloud you use. If you are not on AWS, the identity and tool-search sections still transfer.

## Related Conf42 talks

- [Beyond Chatbots: How Amazon Bedrock Agents Drive Enterprise AI](https://www.conf42.com/Machine_Learning_2025_Samuel_Baruffi_chatbots_bedrock_enterprise), Samuel's earlier talk on the more opinionated Bedrock Agents
- [Reduce AI Agents Costs and Mistakes with Semantic Tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost)
- [From PoC to Production: Deploying Agentic AI at Enterprise Scale](https://www.conf42.com/MLOps_2026_Meher_Bhaskar_Madiraju_agentic_poc_deploying)

[Watch Samuel Baruffi's talk](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore)

[Watch the talk on YouTube](https://youtu.be/ZAqZDBADoKY).

## Watch the talk

[From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore) at Conf42 MLOps 2025.
