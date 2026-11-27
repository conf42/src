# A four-floor security map for the AI stack, and the floor teams skip

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/four-layer-security-map-for-ai-stack

In short: Kriti Faujdar (Yelp) at Conf42 MLOps 2026 on a four-layer defense-in-depth map for AI systems: model, agents, tools and MCP, infrastructure.

An AI demo takes an afternoon, and the launch stalls for months on everything the demo skipped. At Conf42 MLOps 2026, Kriti Faujdar, Lead Product Manager at Yelp, where she works on agentic systems after leading security foundation model work at Microsoft Security, hands teams a map of where production AI gets attacked: four layers (model, agents, tools and MCP, infrastructure), the threats on each, and the fixes. Her pick for the layer most teams overlook is the third one.

Her picture is a building. Each floor has its own doors to lock, and a great lock on the front door does nothing about the ground floor window. "an attacker only needs one layer to fail", Kriti Faujdar said at Conf42 MLOps 2026, so the job is to make every floor annoying to get through.

## The model cannot tell instructions from data

Layer one is the model itself: direct prompt injection, indirect prompt injection, jailbreaks and output hijacking. Direct injection is the user typing an override into the input. Indirect injection is the one she says people worry about most, because the user does nothing wrong. The attack sits in an email, a shared document, a web page or a calendar invite, the app pulls it into the prompt as relevant context, and input validation never sees it. Her real-world case is published research in which instructions hidden in a Google Calendar invite or an email hijacked Gemini-powered assistants, which in the demos leaked data and controlled smart home devices.

Output hijacking is the shortest path to a bad day: ask the model for a shell command, run it with os.system, and a manipulated answer becomes remote code execution.

The five defenses are deliberately unglamorous. Keep instructions and data apart with the structured messages API instead of string concatenation. Validate every output before it drives an action, the way normal software validates anything from outside. Run a content classifier on responses. Harden the system prompt with explicit scope and refusals. Constrain output to a schema, so injected free text has a harder time riding along. The rule under all five: nothing the model says reaches an action without a check in between, and a failed check is blocked and logged.

## An agent's blast radius equals its permissions

Layer two is where a wrong answer stops being a user experience problem and becomes an incident: the wrong email sent, the wrong file deleted, the wrong customer charged. She names three threats. The confused deputy, where an agent acting for user A reads or changes user B's data, usually because memory or a vector store has no per-user namespace. Excessive permissions, such as a search-and-summarize agent that can also delete files. And multi-agent trust chains, where sub-agents trust whatever comes from upstream.

Her line on permissions is worth pinning above a desk: "the blast radius of any failure actually equals the permissions you have granted".

The fixes: a tool allowlist with least privilege, human review for actions you cannot undo, context isolated per user, every action logged before it happens, and agent-to-agent messages checked like user input. She recommends a two-phase design, plan then execute. The agent lists the tool calls and arguments it wants, a human or automated reviewer approves them, and only then does anything run. You get an audit trail for free and a natural place to start an investigation.

## MCP servers deserve the npm treatment

Layer three is tools and the Model Context Protocol, and it is the floor she flags. "Teams adopt MCP and new tools quickly without threat modeling them", she said. The threats are tool poisoning (a malicious tool description changes agent behaviour with no code change, because the instruction lives in metadata nobody validates), schema abuse through loose free-form inputs, and unvetted third-party servers, which she compares directly to pulling in any npm package.

So treat them like dependencies. Allowlist tools in production with no dynamic discovery. Validate tool inputs and outputs against a strict JSON schema with additional properties set to false. Log every call. Read the source, check for telemetry, audit network calls, pin versions and review updates.

## The infrastructure floor is old advice with higher stakes

Layer four has nothing new in it, and she says so. Secrets still end up in prompts, and prompts land in provider logs and traces, so use a vault and managed identity. Restrict egress at two levels, an application URL filter and network firewall rules, so an injected instruction to ship data elsewhere has nowhere to go. Scan weights and packages in CI/CD with tools like pip-audit, Safety and ModelScan, and prefer safetensors over pickle-based formats that can run code on load. Run agents in minimal containers with dropped capabilities and a read-only root file system.

Stacked together, a prompt injection that gets through layer one still meets permission controls, then the tool allowlist, then egress rules.

## Who should watch

ML engineers and platform teams taking an LLM feature from notebook to customers, and product managers who need a shared vocabulary with security. It is a lightning-format survey, so security specialists will know most of the individual controls. The value is the map and the closing checklist: sixteen questions, four per layer. Her advice is to find the weakest layer and ship one fix this sprint: "Small improvements that ship are worth more than a complete plan."

## Related Conf42 talks

- [Prompt Injection Attacks: Understanding and Mitigating Risks in LLM-Powered Web Apps](https://www.conf42.com/Large_Language_Models_LLMs_2025_Jorrik_Kiijnsma_attacks_risks_security) by Jorrik Kiijnsma of Sopra Steria at Conf42 Large Language Models 2025.
- [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal of ArmorCode at Conf42 DevSecOps 2026.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026.

[Watch Kriti Faujdar's talk](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Securing the AI Stack: From Models to Agents to Infrastructure](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) at Conf42 MLOps 2026.
