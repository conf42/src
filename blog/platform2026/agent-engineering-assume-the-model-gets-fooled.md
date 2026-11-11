# Agent engineering starts by assuming the model gets fooled

Conf42 Blog, 2026-10-07, updated 2026-11-09. https://www.conf42.com/blog/platform2026/agent-engineering-assume-the-model-gets-fooled

In short: Cynthia Akiotu of Accenture at Conf42 Platform Engineering 2026 on identity, MCP tools and authorization checks that hold when prompt injection works.

A customer asks a support agent about refunds, the agent retrieves the refund policy, and hidden in that document is an instruction to export every customer case to an outside address. At Conf42 Platform Engineering 2026, Cynthia Akiotu, AI security and data protection architect at Accenture and a Microsoft MVP in Security Copilot, used that one scenario to argue that once an LLM can act, every engineering decision becomes a security decision.

Her design goal is refreshingly modest: don't pretend the model can't be manipulated. Contain what happens when it is.

## Same model, new blast radius

Cynthia starts by putting prompt engineering and agent engineering side by side. The model is identical. What changed is everything around it: instructions, context, identity, tools, actions and governance. A chatbot that answers wrongly misleads someone. An agent that acts wrongly sends the email, updates the record or deletes it.

Each layer adds capability and widens the blast radius unless it's deliberately constrained. And these layers aren't one team's checklist; identity, data, security and operations teams all own a piece.

## Retrieved text can inform, never authorise

The refund scenario is indirect prompt injection. The attacker never talks to the agent; they plant instructions in a source the agent will read. Her design question is sharp and practical: who can write to the knowledge sources your agent retrieves from? Detection helps, she says, but you still need controls beyond the model, because the next question is whose authority the agent is running on.

She lays out three identity patterns: delegated access on behalf of a signed-in user (the agent inherits that user's reach), an agent with its own account like a digital worker, and app-only identities for background work. If any of these is broad, a fooled model gets broad reach.

## MCP is a protocol, not a trust decision

The Model Context Protocol section is the one platform teams will screenshot. MCP standardises how agents discover and call tools, which is convenient. It doesn't make a server trustworthy. Her example shows a ticket-search tool whose description quietly asks the model to send a report elsewhere, which is tool description poisoning. Review servers and tool definitions, restrict discovery, validate requests and enforce permissions at execution.

Then the line every agent builder should tape to the monitor: capability doesn't mean authorization. Writing "please don't delete data" in the system prompt is a suggestion. A policy check in the application that denies the delete because no approver exists, and logs the attempt, is a boundary.

## Follow the attack, then follow the trace

Cynthia connects the pieces into one path: the agent retrieves the poisoned policy, mistakes it for an instruction, tries the export, and the API rejects it. The model was fooled; the system held. Controls sit at several points (inputs, retrieved context, tool arguments, actions, outputs), and an AI gateway is a good shared front door for model traffic, but tool execution may take a different route to an enterprise API and still needs its own check.

Correlated traces let the security team see the denied export even when the customer sees a normal answer. Her case study uses the Microsoft stack she works in, including Entra Agent ID and Agent 365 for agent identity and life cycle, as one example of turning these principles into platform capabilities.

## Least agency

Her closing pattern is least agency: enough freedom to do the job and no more, narrow tool access, deny unapproved actions by default, humans in the loop for irreversible changes, and deterministic application logic validating whatever the model proposes. Before production, ask who owns the agent, which identity it uses, and whether you can trace, stop and recover its actions.

## Who should watch

Engineers moving from chatbots to agents with tools, and security architects reviewing them. It's a clear, structured talk rather than a code walkthrough, and the refund story makes it easy to retell in your own design review.

## Related Conf42 talks

- [RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) by Blaize Stewart at Conf42 AI Agents 2026.
- [Why Single-Layer LLM Guardrails Fail](https://www.conf42.com/Prompt_Engineering_2026_Manvitha_Potluri_injection_guardrails_bedrock) by Manvitha Potluri at Conf42 Prompt Engineering 2026.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026.

[Watch Cynthia Akiotu's talk](https://www.conf42.com/Platform_Engineering_2026_Cynthia_Akiotu_agent_llms_prompt) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/TWXwkFYsX4w).

## Watch the talk

[From Prompt Engineering to Agent Engineering: When LLMs Can Take Action](https://www.conf42.com/Platform_Engineering_2026_Cynthia_Akiotu_agent_llms_prompt) at Conf42 Platform Engineering 2026.
