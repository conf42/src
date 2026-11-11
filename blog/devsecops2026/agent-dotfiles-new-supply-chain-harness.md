# Your coding agent's dotfiles are the new software supply chain

Conf42 Blog, 2026-10-01. https://www.conf42.com/blog/devsecops2026/agent-dotfiles-new-supply-chain-harness

In short: Roshan Piyush of Harness at Conf42 DevSecOps 2026 on why hooks, skills, memory and MCP servers are where AI supply chain attacks now land.

Roshan Piyush, Head of Security Research at Harness, pointed a discovery script at his own laptop before giving his Conf42 DevSecOps 2026 talk. It found 1,103 agent-related artifacts, about half of which he didn't know were there, including 158 skills and around 830 instruction files like CLAUDE.md and AGENTS.md. His argument follows from that inventory: the software supply chain now runs through the configuration that tells AI agents how to behave, and almost nobody reviews it.

## Attackers follow the trust

The first third of the talk is a fast tour of supply chain incidents, and the point is the pattern, not the nostalgia. SolarWinds shipped a signed backdoor through a build pipeline. Codecov's compromised uploader script exfiltrated environment variables. Alex Birsan's dependency confusion research showed registries preferring the higher version number over the internal source. XZ Utils was a two-year trust-building operation, caught only because a developer was annoyed by a 500 millisecond SSH delay. Roshan's aside lands well: an AI agent would never have bothered about half a second.

Then the newer ones. The LiteLLM compromise came through an already-compromised Trivy action and dropped a Python `.pth` file, which runs every time the interpreter starts. Shai-Hulud tore through npm and used TruffleHog, a secret scanner, to find the secrets it stole. A later variant used AI to craft payloads and embedded a request about building a nuclear bomb, so that LLM-based malware scanners would refuse to look at it. Each step moved to wherever developers had put their trust: an update, a tool, a package manager, a contributor, a release channel. Roshan's claim is that trust is now moving to the agent.

## Committed config is committed behaviour

The sharpest line in the talk is about what lives in our repos now: "Not to commit dot ENV files, but now we commit an entire behavior." Teams check in CLAUDE.md, `.cursor` rules, `mcp.json` and `settings.json` so colleagues can share them. Anyone who clones the repo inherits instructions they've probably never read, which a colleague may have pasted from somewhere else.

Hooks get special treatment. In Roshan's words, "Hooks have become the dot bash RC problem for the agents at scale." They run on every prompt and every action, they can silently rewrite context, and his team's research found that hooks could edit other hooks without any approval prompt. A malicious instruction in an MCP server can install a hook that does the rest.

## Memory, hallucinated packages and blind spots between tools

Three more attack paths get a short treatment each:

- **Memory poisoning.** Tell an agent once to use a mock payment tool for testing and forget about it. Months later a vector store retrieves that note by relevance, not recency, and the agent authorises a payment through the mock. Roshan also cited research showing five malicious documents in a million can hijack an answer with a 90% success rate.
- **Hallucinated dependencies.** Agents rarely typo, but they do invent package names. An attacker only has to register the name the model keeps suggesting.
- **Cross-tool blindness.** Claude refused to tamper with its own hooks and settings, but Cursor or Windsurf would happily edit Claude's files, and the reverse holds too. Each agent guards itself and ignores its neighbours.

He also admitted that he, a head of security research, usually picks "always allow" on the permission prompt. Humans get tired of approving things, and he counts that fatigue as part of the threat model rather than a moral failing.

## What he wants teams and vendors to do

The recommendations split in two. Teams can act now: open your `.claude` and `.cursor` folders and look; review agent configuration as source code; replace static API keys with short-lived role credentials (his team uses 24-hour sessions for Bedrock); and red-team the models you rely on, as NIST AI 600-1 expects. Vendors and the ecosystem need to supply what nobody can build alone: a kill switch that hooks can't disable, signed models with provenance (CycloneDX ML-BOM and SPDX AI BOM are a start), signed MCP servers, provenance for hooks, and guardrails that work across agents. His blunt summary: "AI supply chain is completely broken right now."

## Who should watch

Platform and AppSec engineers rolling coding agents out to a whole organisation, and anyone who has approved a CLAUDE.md in code review without reading it. The talk is threat modelling and field notes rather than a product demo, and the attack history alone makes a good briefing for a team that hasn't been following the npm incidents.

[Watch Roshan Piyush's talk](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security) ([YouTube](https://youtu.be/9-n30eWZ8pY)).

## Related Conf42 talks

- Alex Shershebnev (Zencoder) on [wiring MCP into DevOps without opening a security hole](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure), DevSecOps 2025.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar (AuthZed), LLMs 2026.
- [LLM hacking is underrated](https://www.conf42.com/Large_Language_Models_LLMs_2025_Dmitriy_Volkov_hacking_underrated_security) by Dmitriy Volkov (Palisade), on fine-tuning poisoning, LLMs 2025.

## From Harness

Harness makes software delivery tooling, and in the talk Roshan describes it putting agents across the pipeline: dependency installs, PR review, deploys, production monitoring and rollbacks. The talk's abstract links to a demo of its runtime protection agent.

- [harness.io](https://www.harness.io/)
- [Runtime protection agent demo](https://www.harness.io/demo/runtime-protection-agent)

## Watch the talk

[Rethinking Supply Chain Security in the Age of Agentic AI](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security) at Conf42 DevSecOps 2026.
