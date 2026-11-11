# Don't trust the agent. Trust the layers you build around it

Conf42 Blog, 2026-09-22, updated 2026-11-09. https://www.conf42.com/agents2026/trust-the-system-around-the-agent

In short: Morgan Willis (AWS) at Conf42 AI Agents 2026: layered guardrails, steering, MCP interceptors and deterministic policy for a customer service agent.

Trust is not something you give an AI agent; it's something you build into the system around it. That's the thesis Morgan Willis, Principal Cloud Technologist at AWS, works through at Conf42 AI Agents 2026, using a customer service agent for a fictional robot vacuum company and a set of very specific ways it misbehaved. Her toolkit is AWS (Amazon Bedrock, the Strands Agents SDK, Bedrock AgentCore), and she says up front that the patterns apply to any agent built anywhere.

## Model plus harness equals agent

She sorts failures into three buckets: the agent says something wrong (hallucinates, promises what it can't guarantee, leaks data), the agent does something wrong (wrong tool, wrong arguments, wrong account, deleted data), and someone deliberately tries to break it. The familiar headlines fit the buckets, from the dealership chatbot that sold a car for a dollar to the coding assistant that deleted a production database.

Her starting point: a system prompt is a suggestion. Models get better at following instructions, but you can't audit a prompt and promise the agent will never do the wrong thing. The opposite extreme, a rigid step-by-step graph, is controllable but brittle and breaks as soon as reality leaves the path. The goal is an open-ended, model-driven agent with enough layered controls that when one guardrail fails, another catches it.

## Five scenarios, five layers

**Off-task use.** A customer asks the vacuum bot to solve a LeetCode problem to save on a coding-assistant subscription, and the bot happily obliges. Amazon Bedrock Guardrails filter both directions: denied topics and injection patterns stopped before the model runs, and sensitive data such as card numbers masked on the way out.

**Not following directions.** Asked for a refund outside the return window, the agent says yes without checking eligibility or calling the refund tool. Long system prompts suffer from the lost-in-the-middle effect. Two fixes: hooks that run deterministic code at points in the agent loop (no refund call unless the eligibility tool ran first), and Strands' steering, where a second agent with its own context and rubric reviews tool calls and responses before they go out and sends them back with feedback when they're off policy.

**Wrong values in tool calls.** Asked about order 12345, the agent looked up 67890. She saw exactly this in her own testing. The problem is that the model controls the tool arguments. The fix is an MCP interceptor at AgentCore Gateway, one layer removed from the agent, which injects sensitive parameters like the customer ID from the authenticated user's token instead of trusting the model, and checks the order really belongs to that customer. The tools validate again, as the last line of defence, the same way a backend doesn't trust the frontend.

**High-stakes actions.** Policy says refunds over $500 need a human; the agent refunded $899 anyway, with the rule sitting right there in its prompt. A deterministic authorisation layer, AgentCore Policy with Cedar-family policies, permits the refund tool only under the threshold. As she puts it, no agent can think its way around that.

**Seeing what it does.** Auto-instrumented tracing, plus anomaly alerts on tool-call rates and token consumption, so a spike gets investigated before it gets expensive.

## The front door matters too

The reference architecture puts plenty in front of the agent: Cognito for OAuth (swap in any provider), AWS WAF for bot detection and IP rules, API Gateway for rate limiting. You are exposing a model to the internet, and people will try to abuse it, so you need places to shed load. Behind it, AgentCore Runtime hosts the agent in isolated sessions, tool calls pass policy and then the gateway interceptor before reaching Lambda, and IAM keeps both agent and tools on least privilege.

On shells: if you give an agent code execution, isolate it, for example in AgentCore Code Interpreter or with the open-source Strands Shell, which restricts the network addresses and files it can touch. Add egress and DNS controls, because a prompt-injected agent told to download a package is how attackers get onto your machine.

## Who should watch

Teams moving a customer-facing agent from demo to production, on AWS or not. It's an architecture talk; she ran out of time for the live demo, but the working agent with all the guardrails is in her repository. Her closing table, which labels each control as deterministic or probabilistic, is the slide worth screenshotting.

## Related talks

- [From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore) by Samuel Baruffi
- [Guardrails First: Designing Safe, Scalable, and Accountable AI Agents for Security Operations](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) by Neal Iyer
- [Who Is Calling Your Model? Identity and Authorization for AI Agents and ML Pipelines](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) by Bhavik Thakkar

[Watch Morgan Willis's talk](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust)

[Watch the talk on YouTube](https://youtu.be/feClaurFkbo).

## Watch the talk

[I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) at Conf42 AI Agents 2026.
