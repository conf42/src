# An MCP server in Go should be narrow, gated and boring

Conf42 Blog, 2026-04-23, updated 2026-11-09. https://www.conf42.com/blog/golang2026/mcp-server-in-go-narrow-tools

In short: Shadi Elyafi at Conf42 Golang 2026 on a Go MCP server over AppSync GraphQL for 1M+ company profiles, with default-deny mutations and TDD.

Most MCP demos end the moment a model successfully calls a tool. [Shadi Elyafi](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow), Lead Golang Developer at METRO AG, starts his Conf42 Golang 2026 talk exactly there and asks what happens when the tool touches real business data: a company intelligence platform with more than one million company profiles, reached through GraphQL on AWS AppSync, with Claude as the client.

His answer is that the protocol is the easy part. The production question is how much power each tool gets and how precisely its behaviour is defined.

## The server is a contract-enforcing layer

The architecture is three boxes. Claude, or any MCP client, handles user intent and picks a tool. The Go MCP server sits in the middle, built on MCP Go, doing dispatch, schemas, validation, mutation gating and response shaping. AppSync stays the GraphQL boundary into the backend, and the platform stays the system of record. Claude never talks to GraphQL directly.

So a request like finding SaaS companies in Germany with 50 to 100 employees never travels as a sentence. The client selects a search tool, the server parses typed parameters, trims input, resolves "DE" to the backend's value for Germany, and caps limits: default 10 results, never more than 100, because a valid query over a million profiles can still be useless. On the way back, nested backend responses get flattened into one stable record shape (ID, name, country, employee range, domain, industry text) so the model isn't guessing which nested field matters.

Authentication stays inside that boundary too. With OIDC bearer tokens the client acts on behalf of a specific user, so backend authorisation, audit trails and data scoping behave as if that user called the API directly. The MCP layer inherits the access model rather than routing around it.

## Mutations are off until someone proves they're safe

Nine tools were implemented; eight ship. Six are read-only (search, lookups, AI-assisted search, collections), two can write (add to collection, request email discovery). Read-only tools are constructed without the mutation flag at all, so there is no write path to accidentally open. Write-capable tools receive an explicit allow-mutations flag and fail before any backend work without it.

Shadi is clear that this is not an authorisation model, which still belongs to the backend. It is an operational switch that flips the default question from why not let the client write to what evidence makes this write path safe.

## Test the request, not just the response

The mutation gate was built test-first. The test builds the tool with mutations disabled, calls it, and asserts an error, no result, and, most importantly, that the mock GraphQL client was never called. That last assertion fails the moment someone moves the backend call above the guard.

Mocks also capture the GraphQL variables each tool sends, so tests check limit capping and country resolution, not only whatever the mock returns. A Go interface with one small Execute method (context, query, variables, result pointer) makes that cheap.

Then the honest bit: the ninth tool, Create Collection, passed its mocked tests and then hit a Lambda null pointer failure in the backend when exercised against the real AppSync endpoint through MCP Inspector. The code stayed; the tool was simply not registered. Mocks and real-system validation answer different questions, and you need both.

Rate limits round it out, because conversational follow-ups turn into bursts: AI search at five requests per minute, email discovery at ten per hour.

## Who should watch

Anyone wiring an LLM client into a production API, especially Go teams. It is one of the more concrete MCP talks on the Conf42 shelf: real tool counts, real limits, a real failure. Teams already running per-tool telemetry and default-deny writes will find it confirms rather than surprises.

## Related Conf42 talks

- [From Prompt to Production Dashboard: Agentic AI with MCP Servers and Live Data](https://www.conf42.com/AI_Agents_2026_Rohit_Deshpande_Scott_Young_mcp_dashboards_live) by Rohit Deshpande and Scott Young, MCP tools pointed at live business data.
- [Less Theater, More Engineering: A Production Claude Code + MCP Agent Pipeline at 80% Accuracy](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) by Suneet Malhotra, another team measuring MCP in production.
- [Build a complex app with TDD](https://www.conf42.com/Golang_2023_Ivan_Pesenti_complex_app_tdd) by Ivan Pesenti, for the test-first habits that made the mutation gate trustworthy.

[Watch Shadi Elyafi's talk](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow)

[Watch the talk on YouTube](https://youtu.be/1d14_iIBcY0).

## Watch the talk

[Building an MCP Server in Go for a Real B2B Workflow](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) at Conf42 Golang 2026.
