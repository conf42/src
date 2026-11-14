# A cloud MCP server is privileged infrastructure, not a connector

Conf42 Blog, 2026-04-16. https://www.conf42.com/blog/cloud2026/treat-cloud-mcp-servers-as-privileged-infra

In short: Aleksandr Pinaev of Swordfish Security at Conf42 Cloud Native 2026 on where MCP security risk comes from, a classification of MCP flaws, and defenses.

The moment an MCP server advertises tools to an AI client, it joins your trust boundary. At Conf42 Cloud Native 2026, [Aleksandr Pinaev](https://www.conf42.com/Cloud_Native_2026_Aleksandr_Pinaev_security_vulnerabilities_compliance), founder of Swordfish Security, argued that cloud-hosted MCP servers concentrate access, execution and privilege behind one interface, and that the worst MCP bugs are design choices, not coding mistakes.

It's a focused 15-minute threat-modeling talk: where the risk comes from, a classification you can use in reviews, and a list of defenses.

## A capability container is also a risk container

Pinaev's model of an MCP server is a capability container. It tells the client what it can do (scan code, validate policies, read resources, trigger actions) and offers one protocol to discover and invoke all of it. That is elegant for interoperability. It also means trust, permissions, execution logic and external reach now sit behind a single boundary, which centralises risk very efficiently if you draw that boundary badly.

So he treats MCP as a control layer between models, tools and cloud services. It doesn't just move data; it shapes what a simple request can eventually turn into.

## Intent has to be constrained across the whole chain

Classic cloud security reasons about one API calling another. MCP chains are more fluid: a user talks to a model, the model uses an agent, the agent uses an MCP client, the client calls an MCP server, and the server reaches a tool or API. At every hop parameters can change, scope can widen and privileges can quietly expand. The question is less whether one endpoint is secure and more whether intent stays constrained end to end.

That's why he says a system can be unsafe even when the code is fine, authentication exists and the connectors are tested. Too much power in the wrong place, or trust mixed between the wrong components, produces systemic risk anyway.

## Six classes of MCP weakness

His classification gives security teams something to assess and prioritise:

1. Identity and access: weak authentication, token misuse, confused identity, broad scopes.
2. Trust boundary failures and unsafe delegation: hidden privilege changes, implicit trust between model, client, server and tools.
3. Tool and connector exposure: too many callable actions, overly powerful connectors, weak control over what gets registered.
4. Isolation failures: cross-tenant leakage, drift between environments, shared context abuse.
5. Validation and execution flaws: prompt injection, context injection, unsafe parameter handling, dangerous writes.
6. Visibility and control gaps: weak auditability, weak approval logic, weak monitoring.

Real attacks chain these. Injected context steers the model, the model picks a tool, and the MCP server performs a risky read that leaks data. Each step looks small; together they are high impact. Cloud hosting makes it worse: public reachability, harder forensics on ephemeral infrastructure, tokens spread across agents and automation, and trust that drifts between dev and prod.

## Defenses: split reads from writes, gate the dangerous ones

On design, he recommends treating MCP as a privileged execution path, separating read paths from write paths with much stronger controls on writes, constraining tool choices, scopes and allowed parameters, validating execution intent and not only input shape, adding explicit confirmation gates for dangerous or irreversible operations, and isolating tenants, agents, services and environments by default.

Operationally: strong authentication with short-lived credentials, scoped authorisation per tool and connector, allowlists for actions and resource classes where realistic, audit trails covering both MCP calls and their downstream effects, and monitoring tuned to AI-enabled abuse rather than ordinary API errors. His parting advice: "Do not ask only can the model call the tool." Also ask what authority that connection creates and how tightly it is controlled.

## Who should watch

Security engineers, cloud architects and AI platform teams about to put MCP servers in front of production systems. The classification alone is worth stealing for your next design review.

## Related Conf42 talks

- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026.
- [RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) by Blaize Stewart at Conf42 AI Agents 2026.
- [Securing the AI Stack: From Models to Agents to Infrastructure](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) by Kriti Faujdar at Conf42 MLOps 2026.

[Watch Aleksandr Pinaev's talk](https://www.conf42.com/Cloud_Native_2026_Aleksandr_Pinaev_security_vulnerabilities_compliance) or the [YouTube recording](https://youtu.be/wqsypIAys7A).

## Watch the talk

[Cloud MCP Servers Under Fire: Security Risks, Vulnerability Patterns, and Practical Defenses](https://www.conf42.com/Cloud_Native_2026_Aleksandr_Pinaev_security_vulnerabilities_compliance) at Conf42 Cloud Native 2026.
