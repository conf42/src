# agentctl treats AI agents and MCP servers like pods

Conf42 Blog, 2026-03-24, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/agentctl-manage-ai-agents-like-infrastructure

In short: Andrew Espira of Kustode at Conf42 Cloud Native 2026 on agentctl, a Go CLI that registers, health-checks and discovers AI agents and MCP servers.

You have `kubectl` for pods and `docker` for containers, but the Ollama instance, the three MCP servers wired into your editor and the agent somebody left running in a terminal tab have no common control plane at all. At Conf42 Cloud Native 2026, Andrew Espira, Founding Engineer at Kustode, showed agentctl, a zero-dependency Go CLI his team built to register, start, stop, health-check and discover AI agents and MCP servers as if they were ordinary infrastructure.

It is a short, demo-led talk about a tool the speaker's own team wrote, so treat it as a working pattern rather than a survey of the field.

## The agent layer is load-bearing and nobody is paging on it

The abstract paints a familiar mess: Ollama locally, MCP servers spread across Cursor and Claude Desktop, a LiteLLM proxy, a couple of custom agents. Some run in Docker, some as Node processes, some only exist because a terminal tab is still open. There is no unified view, health checks are manual, and when one dies overnight you find out the hard way.

In the talk Andrew frames the operational question more broadly. Once agents fan out across environments and make parallel tool calls, the people running them need to see which tools each agent calls, which data it touches, which services it hits, and why it chose operation X over operation Y. That last part, auditing the reasoning, is what separates this from a process manager.

## Registration, lifecycle and a state file you can read

agentctl keeps everything in a single JSON state file: no database, no daemon. You register agents and MCP servers with typed metadata (transport such as stdio, SSE or HTTP, endpoints, commands, tags), and `agentctl agent start` launches the process, records the PID and streams logs to `~/.agentctl/logs/`. `agentctl mcp health` probes HTTP endpoints, or checks PIDs for stdio servers that have no endpoint to probe.

The demo walks through `agentctl agent list`, a health check across everything registered locally, and pulling logs for a single agent with a line limit. Nothing exotic, which is the point: the verbs are the ones you already type for every other service you run.

## Discovery beats remembering what you installed

The part worth stealing is `agentctl discover`. Per the abstract, it scans three sources in parallel: running processes against roughly 30 known signatures (Ollama, LM Studio, CrewAI, LangServe, and any `node` process with "mcp" in its name), well-known ports such as 11434 and 1234, and the MCP config files of Claude Desktop, Cursor and VS Code. New services get registered automatically and re-runs are idempotent. If you have ever grepped three different JSON configs to remember which MCP servers your laptop is running, you can see why.

`agentctl dashboard` then renders a live terminal UI refreshing every few seconds: agents, MCP servers, recent calls, health and confidence scores. Andrew compares it to running `htop` on a Linux box, only pointed at the agent layer instead of RAM and disk.

## Confidence scores as a gate, SRE practice as the frame

Each agent carries a confidence score from 0 to 1, mapped to tiers in the abstract: green at 0.85 and above proceeds automatically, yellow between 0.60 and 0.85 notifies and proceeds, red below 0.60 escalates to a human. In the talk Andrew ties this to guardrails: validating that the data an agent used and the decision it made fit the context, and alerting on hallucinations at the stage where they appear in the reasoning chain.

The wider argument is that agent workflows deserve the same SRE treatment as any service. Kustode pushes the telemetry into its monitoring tools and Slack, and Andrew points at Grafana dashboards, SLOs and SLIs, token usage and hallucination rates as the things to track.

## Who should watch

Platform and SRE engineers whose developers are quietly accumulating local models, MCP servers and agents, and anyone who wants a concrete shape for "agent observability" before buying a product for it. If you want deep internals of the reasoning-trace pipeline, the talk only sketches it; the abstract and the repo carry more detail than the recording.

## Related Conf42 talks

- [Alex Shershebnev on adding MCP to DevOps without opening a security hole](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure) at Conf42 DevSecOps 2025.
- [Shadi Elyafi on building an MCP server in Go for a real B2B workflow](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) at Conf42 Golang 2026.
- [Girish Konda on guardrails for confidently wrong agents](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) at Conf42 Feature Flags 2026.

[Watch Andrew Espira's talk](https://www.conf42.com/Cloud_Native_2026_Andrew_Espira_ai_agents_automation)

[Watch the talk on YouTube](https://youtu.be/FmXbubd43P4).

## Watch the talk

[agentctl: A CLI for Managing AI Agents and MCP Servers Like Infrastructure](https://www.conf42.com/Cloud_Native_2026_Andrew_Espira_ai_agents_automation) at Conf42 Cloud Native 2026.
