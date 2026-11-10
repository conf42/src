# A looping agent keeps every dashboard green

Conf42 Blog, 2026-10-18, updated 2026-11-09. https://www.conf42.com/prompt2026/agentcore-datadog-loops-burn-tokens-silently

In short: Indika Wimalasuriya (Virtusa) at Conf42 Prompt Engineering 2026 traces a Bedrock AgentCore agent end to end in Datadog, kill switch included.

It's 3am, p95 latency is fine, the error rate is 0.2% and CPU sits at 34%, while the agent underneath calls the same tool over and over with hallucinated arguments. At Conf42 Prompt Engineering 2026, Indika Wimalasuriya, Director of SRE and Observability at Virtusa, showed how to see that kind of failure by wiring an Amazon Bedrock AgentCore agent into Datadog, and how to stop it with a kill switch built before go-live.

The talk is a vendor-specific build (AWS plus Datadog) with a working demo and the configuration traps he hit along the way, which is the most reusable part.

## Healthy infrastructure, unhealthy agent

Indika's starting point: the old question "is it running?" barely matters for an agent that reasons, picks tools, reads results and acts, and might take two steps today and seven tomorrow. Loops, wrong arguments, conversations drifting away from what the user asked, token burn and actions that succeed while doing the wrong thing raise no traditional alert at all.

So on top of metrics, logs and traces he wants six more signals: the decision trace, tool invocation spans, token cost per step, model behaviour (stop reasons, errors, throttles), session and memory state, and guardrail evaluations.

## The reference architecture

The demo is an insurance assistant built with the Strands Agents SDK on AgentCore Runtime, using a Claude model on Bedrock and six in-process Python tools: policy lookup, claim status, filing a claim, policyholder lookup, weather risk and a repair cost estimator. The browser carries Datadog Real User Monitoring and calls API Gateway plus a small Lambda proxy that holds the IAM permission to invoke the agent. The agent sends OpenTelemetry traces and logs straight to Datadog's intake with no collector in the path; the Lambda uses the Datadog extension, and the web host runs a normal Datadog agent.

## Three steps and the hours they cost

Keep AgentCore's built-in instrumentation (the AWS Distro for OpenTelemetry) on, register a Datadog OTLP exporter in code next to it, and opt spans into LLM Observability while emitting the GenAI semantic conventions (version 1.37 or later). The heads-up box is where he lost a few hours: setting the standard OTLP exporter environment variables got 403s from Datadog, and only registering the exporter in code worked. Without the LLM Observability flag everything appears in APM and the AI view stays empty. And the app name comes from the root span's service name, not the variable you'd expect.

## Read the trace before optimising

A real trace for "how much would it cost to repair a dented bumper?" ran about six seconds. Nearly all of it was the model thinking; the repair estimator failed once with service unavailable in about 30 milliseconds, the second LLM call decided to retry, and the retry succeeded. Two lessons fall out: if you want the agent faster, the tools are not where to look, and without the trace you'd see one slow request that worked.

APM answers where the time went, LLM Observability what the agent decided, infrastructure whether the platform is healthy, and logs what exactly failed. Shared trace IDs plus consistent service, environment and version tags let you pivot between them.

## Build the kill switch first

Failed calls are loud; unexpected calls (wrong tool, out-of-range parameters, the same tool again and again) are quiet. A runaway loop raised zero errors in the demo; only the tool-call rate and token count gave it away. So: track tokens per session by agent, model and tool, tag by team and environment, and alert on rate of change rather than a fixed number.

The demo's kill switch is concrete. An alarm on more than four tool calls a minute invokes a Lambda that flips an SSM parameter; every tool checks it and returns "suspended" for 90 seconds. He's honest about the limits: it's global, pausing every user, and because the alarm evaluates once a minute it stops the next turn, not the one that tripped it. A switch that pauses everyone beats an invoice that surprises everyone.

He closes with example SLOs for agents: task success, p95 session latency, tool error rate, cost per session within twice the baseline, and guardrail trigger rates alerting in both directions.

## Who should watch

SREs and platform engineers who've been handed an agent in production, and anyone on AgentCore or Datadog who wants the exporter gotchas before losing the same afternoon. Teams on other stacks still get the signal list, the soft-failure lesson and the kill switch pattern.

## Related Conf42 talks

- [From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore) by Samuel Baruffi (AWS) at Conf42 MLOps 2025.
- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty (AWS) at Conf42 AI Agents 2026.
- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) by Michael Levan (Solo.io) at Conf42 DevOps 2026.

[Watch Indika Wimalasuriya's talk](https://www.conf42.com/Prompt_Engineering_2026_Indika_Wimalasuriya_agentcore_datadog_observability) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/CPCXvKH6pu0).

## Watch the talk

[Observing AWS AgentCore with Datadog: End-to-End Observability for Autonomous AI](https://www.conf42.com/Prompt_Engineering_2026_Indika_Wimalasuriya_agentcore_datadog_observability) at Conf42 Prompt Engineering 2026.
