# An 80% accurate agent pipeline, and the 20% that needs QA

Conf42 Blog, 2026-09-06, updated 2026-11-09. https://www.conf42.com/blog/agents2026/qa-view-of-80-percent-agent-pipeline

In short: Suneet Malhotra of Motorola Solutions at Conf42 AI Agents 2026 on running Claude Code and MCP from requirements to tests, and governing the chain, not the file.

An agent that reports success on a checkout test has told you almost nothing about whether you can release. At Conf42 AI Agents 2026, Suneet Malhotra, Senior Manager of Test Engineering at Motorola Solutions with around 20 years in software quality, looked at an agent pipeline built on Claude Code and MCP from the QA leader's chair, and argued that the unit of governance is the whole chain from requirement to release, not the code artifact the agent hands back.

The talk is short and conceptual. Its abstract carries the hard numbers from the pipeline itself; the talk spends its time on the questions a release owner has to answer.

## What the pipeline does

Per the abstract, the system runs at a Fortune 500 telecom and earlier ran at a top-25 consumer mobile app. Three MCP servers (Confluence and Jira, a structured test-case repository, and the automation codebase) let the model turn product requirements into Jira stories, test cases and executable Appium and TypeScript code. In the talk Suneet lists the wider MCP layer around it: Confluence, Jira, TestRail, GitHub, Firebase, Slack and Salesforce, with MCP defining tool contracts and routing requests so the requirement document, tickets and test cases no longer have to be written by hand.

The headline is roughly 80% accuracy: about 80% of generated automation runs the intended scenario without edits after generation. Suneet is careful on stage that he isn't claiming every agent produces exactly 80% correct code. He uses the figure to describe a system that works often enough to look useful and fails often enough that the remaining work is where QA lives.

## Five questions before you trust the green tick

His recurring checklist: what did the agent see, what context did we give it, what tools did it call, what changed, and what evidence supports the result? If you can't answer them, you can't call the release good.

He frames the agentic lifecycle as five stages: specify (requirements, constraints, acceptance criteria), plan (tickets and task sequences), build (code and config changes), verify (do the tests actually run correctly) and operate (monitor, roll back). A file can look right while the chain is broken. A test can pass with a hallucinated locator. A ticket can be closed against acceptance criteria that were never precise enough to evaluate.

## Record enough for someone who wasn't in the room

Observability here means reconstructing a decision later: what the agent received, which model, which tool versions, which permissions, what evidence, and which human approved or rejected what in Jira. That evidence trail is what turns an agent into something an engineering team can inspect, instead of a box that announces its own final state.

## Put humans where the risk is

The last 20% is edge cases, context, test data quality and decisions that depend on consequences rather than syntax. Common failures are sparse specs, unclear acceptance criteria, hallucinated API or parameter names, schema drift and lost context. Suneet tiers the response by risk: production configuration, payments and authentication keep a human in the loop; medium-risk regression changes can be automated with reliable review; low-risk changes can lean on unit tests and documentation. The pipeline creates specifications and tests, but there is no autonomous path to release approval.

The abstract adds the scars from a year of running it: don't ask the model to do deterministic work such as flaky-test detection, constrain output to a JSON schema or review time blows up, keep the human PR gate after a silent regression caused a multi-week mess, measure quality before cutting cost (a 25% token cut came with more hotfixes), and layer agents on top of the existing automation runtime instead of replacing it. With guardrails, the ratio of cheap failures to expensive ones went to 4:1, from 1:1 without.

## Measure rework, not output

The metric advice is the part to take back to your team. Track rollback frequency, defect escape rate, unsafe tool call rate and audit trail completeness, not how much the agents generated. Agents earn more autonomy by showing reliable behaviour under clear controls.

## Who should watch

QA and test engineering leads being asked to sign off on agent-generated tests, and engineering managers deciding how much of the delivery pipeline to hand to agents. If you want implementation detail, read the abstract alongside the video; the talk is the governance layer on top.

## Related Conf42 talks

- [Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) by Ajay Munjuluru at Conf42 MLOps 2026.
- [Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda at Conf42 Feature Flags 2026.
- [Adding Tamper-Evident Audit Trails to AI Agents in Production](https://www.conf42.com/MLOps_2026_Joao_Marques_audit_tamper_agents) by Joao Marques at Conf42 MLOps 2026.

[Watch Suneet Malhotra's talk](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/P22u-_LDTXM).

## Watch the talk

[Less Theater, More Engineering: A Production Claude Code + MCP Agent Pipeline at 80% Accuracy](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) at Conf42 AI Agents 2026.
