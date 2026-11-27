# Your MCP server is safe. The web page it fetched isn't

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/mcp-for-devops-without-a-security-hole

In short: Alex Shershebnev of Zencoder at Conf42 DevSecOps 2025 on wiring MCP into DevOps workflows and a live prompt-injection demo that wrote a file to disk.

The scary part of giving an LLM tools isn't the tool. It's whatever text the tool brings back. At Conf42 DevSecOps 2025, [Alex Shershebnev](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure), ML/DevOps lead and developer advocate at Zencoder, showed how the Model Context Protocol lets an assistant solve Jira tickets, open pull requests and inspect Kubernetes from your IDE, then hijacked his own agent with a web page that looked harmless to a human.

The demos run inside Zencoder, his company's AI coding assistant, so expect some product on screen. The MCP concepts and the attack apply to any client.

## LLMs need context, so we gave them hands

Shershebnev starts from why MCP exists. Models predict probable tokens and live somewhere in the cloud, with no access to your servers, your logs or your in-house frameworks. Ask a chatbot for Google's response time and it suggests running ping; it can't run it. Tools fix that by letting the model gather extra context.

MCP, introduced by Anthropic around December 2024 and since adopted by OpenAI too, is the common way to do it. It's based on JSON-RPC 2.0 and has two main roles: the host (your IDE or LLM client) and the server, which advertises a list of tools and executes them. He shows the GitHub MCP server's create-branch tool, whose short description and parameter list are exactly what ends up in the prompt so the model can decide which tool to call.

Writing your own server is cheap. In Python with FastMCP he circles three lines: import the library, instantiate the server, decorate a function. His example turns a function that runs bash commands into a tool any MCP-compatible model can call, which is also a nice preview of the security half of the talk.

## The useful part: tickets to pull requests, pods to answers

The first demo chains Jira, Git and GitHub servers. He tags a ticket, asks the agent to solve it, create a branch, push and open a pull request. The agent explores the repository, edits files, runs commands to regenerate an OpenAPI schema and opens a PR under his token, touching 110 files with a tidy description. He jokes that a well-documented PR is now a sign it was written by AI.

The second gives the agent the Kubernetes MCP server and asks whether any pods in a namespace are unhealthy. He also runs through the servers he finds most useful day to day: Postgres for databases, Grafana and Sentry for monitoring, Slack, Context7 for up-to-date library docs, and Playwright MCP to drive a browser.

## The attack lives in the context, not the protocol

Then the security part. Shershebnev serves pages that look identical to a human reader but carry hidden instructions, fetched through the fetch MCP server. The first page is a clean control. The second hides an injection, and Anthropic's prompt injection detection catches it. The third, more elaborate one asks the model to list every function it can access, then introduces a fake function and asks it to test that function and simulate the output. The model said hi as instructed, listed 17 functions and, instead of simulating, actually called its write-file tool and created a file on his machine.

His point is precise: the MCP fetch server did exactly what it was built to do. The attack came through the page content. He ties it to the publicised GitHub MCP exploit, where an issue in a public repository asked the agent to collect information from private repositories and post it publicly, and the agent, holding a token that allowed both, obliged.

## What to lock down

His recommendations are practical:

- Allowlist which MCP servers developers and agents may use, and manage configs organisation-wide.
- Store the tokens servers need, such as GitHub personal access tokens, in a proper secrets system.
- Keep agents away from sensitive systems like production databases, or at least make access read-only.
- Use server permission flags where they exist. The Kubernetes MCP server, he notes, has one to enable read-only tools and another to disable destructive ones.
- Put an intermediary in front of untrusted content: a search or summarising proxy instead of piping raw web pages into the model.

## Who should watch

Anyone who has added an MCP server to their IDE this year, and platform or security teams deciding what agents may touch. The injection demo is worth the time on its own.

## Related Conf42 talks

- [Don't Give the Agent a Shell](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) draws tool and identity boundaries for agents in cloud operations.
- [Building an MCP Server in Go for a Real B2B Workflow](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) is the build-your-own side in more depth.
- [A Production Claude Code + MCP Agent Pipeline at 80% Accuracy](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) shows MCP agents running for real.

[Watch Alex Shershebnev's talk](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure)

[Watch the talk on YouTube](https://youtu.be/rYIeY6yPgeI).

## Watch the talk

[Supercharging DevOps with MCP (Without Opening a Security Hole)](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure) at Conf42 DevSecOps 2025.
