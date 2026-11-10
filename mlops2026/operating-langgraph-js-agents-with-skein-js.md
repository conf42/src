# Your LangGraph.js agent works. Can it survive a restart?

Conf42 Blog, 2026-11-09. https://www.conf42.com/mlops2026/operating-langgraph-js-agents-with-skein-js

In short: Maina Wycliffe (Garatropic) at Conf42 MLOps 2026 introduces skein-js, a self-hosted runtime for LangGraph.js agents that pause, retry and restart.

An agent that pauses for human approval has to outlive the human's lunch break, a deploy and a server restart. At Conf42 MLOps 2026 on November 19, Maina Wycliffe, founder and chief builder at Garatropic, introduces skein-js, an open-source, self-hosted TypeScript server runtime that gives LangGraph.js agents the infrastructure to do exactly that.

## The scenario that breaks most agent demos

Maina opens with a story every ops person will recognise. An agent reviews a support ticket, proposes an action, and pauses for approval. The reviewer comes back tomorrow. In the meantime the server has restarted, a new version has been deployed, and the system that submitted the request has retried it.

Three things now have to be true. The approval request must still exist. The retry must resolve to the original piece of work instead of spawning a twin. And an operator needs to be able to understand what happened. Building a useful agent is the start; running it as a dependable service is the rest of the job.

## LangGraph runs the graph, skein-js runs the service

The division of labour is clear. LangGraph already provides graph execution, checkpointing and interrupts. skein-js supplies what sits around those graphs in production: persistent API resources, background execution, streaming, and an operator console. Importantly for anyone with code already written, it keeps existing LangGraph.js graphs and SDK clients working.

So this is not a new agent framework. It is closer to the application server you wish had shipped with the framework you already use. Self-hosted, which matters if your agents touch data that is not allowed to leave your infrastructure.

## Postgres for memory, Redis for the work queue

The talk follows an issue-triage workflow through three failures: a duplicate submission, a human approval step, and a server restart. Along the way Maina shows how Postgres persistence and Redis-backed background work support reliable execution.

The part worth paying attention to is where Maina marks the limits. The abstract promises a look at where idempotency guarantees end. That is refreshingly honest. Every durable execution system has a boundary past which "exactly once" turns back into "at least once, good luck", and knowing where that line sits is more useful than a slide claiming there is none.

Telemetry closes the loop: when something does fail, the operator console and traces should explain why.

## A checklist you can use on any runtime

Even if you never install skein-js, the failure scenarios are a portable test suite. Restart the server mid-approval. Retry the same request twice. Deploy a new version while a run is paused. Ask your current agent runtime to survive those, and you will learn a lot about it in an afternoon.

## Who should watch

TypeScript teams on LangGraph.js who are moving agents from a notebook-shaped prototype to something that runs all week. Anyone building human-in-the-loop flows where approvals take hours or days. Python-only shops can still take the failure scenarios home; the runtime itself is JavaScript land.

## Related Conf42 talks

- [Orchestrating Agentic State Machines with LangGraph: Learnings from Automating clinical documentation](https://www.conf42.com/Machine_Learning_2026_Rajeshwari_Sah_labeling_annotation_quality) by Rajeshwari Sah, LangGraph in a regulated domain.
- [Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human) by Vishal Shah, more on keeping a human in the loop.
- [Enhancing Workflow Reliability with Dapr: Techniques to Minimize Failure Costs](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) by Siri Varma Vegiraju, durable workflows outside the agent world.

[Watch Maina Wycliffe's talk](https://www.conf42.com/MLOps_2026_Maina_Wycliffe_langgraph_skein_agent) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Your Agent Works. Will It Survive Tomorrow? Operating LangGraph.js with skein-js](https://www.conf42.com/MLOps_2026_Maina_Wycliffe_langgraph_skein_agent) at Conf42 MLOps 2026.
