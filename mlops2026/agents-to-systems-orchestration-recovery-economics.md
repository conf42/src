# Agentic AI in banking breaks on orchestration and cost, not the model

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/agents-to-systems-orchestration-recovery-economics

In short: Rajesh Gupta (Skan AI) at Conf42 MLOps 2026 on multi-agent systems in BFSI: split planning from execution, add repair agents, put budgets on autonomy.

Rajesh Gupta, Head of Agentic AI Product at Skan AI, has been deploying multi-agent systems in banking, financial services and insurance, and his talk at Conf42 MLOps 2026 on November 19 is about what those deployments surfaced. His short version: the hard problems sit far beyond model performance, in orchestration across legacy systems, recovery when an agent gets it wrong, and the economics of letting software act on its own.

## Regulated environments are the stress test

BFSI is a useful place to learn about agents because it is unforgiving. Legacy cores, audit trails, approval chains and regulators who want to know who did what. An agent that works in a sandbox meets mainframes, batch windows and compliance reviews in production.

Rajesh frames the talk around three areas: reliable orchestration across legacy systems, recovery through verification and repair agents, and the economics of autonomous execution. Each is a place where a promising pilot can stall.

## Separate who plans, who acts, who approves, who fixes

The architectural claim at the centre of the talk is that planning, execution, authorization and recovery should be separate concerns. Rajesh calls that separation essential for both compliance and resilience.

It is the agent-shaped version of separation of duties, a principle any bank auditor already understands. The component that decides what should happen is not the one that does it, and neither of them is the one that signs off. If an executing agent goes wrong, a distinct recovery path exists, with its own checks.

Why this matters in practice: when the planner, the actor and the approver are one prompt, you cannot explain an action after the fact, and you cannot stop a bad one before it lands. Splitting them gives you seams to put controls and logs into.

## Verification and repair agents

Recovery gets its own agents. Rather than assuming a run succeeds and cleaning up by hand when it does not, the system verifies outcomes and routes failures to repair agents. In a regulated setting this is less about elegance and more about having a defined, auditable answer to the question of what happens when the agent is wrong.

## Agent costs are not linear

The economics section is the one finance teams will want to hear. Rajesh points out that cost behaviour in agentic systems is non-linear. Picture a task that usually takes a few steps and occasionally takes many, with retries, verification loops and extra tool calls stacking up. That makes cost per outcome hard to predict from cost per call.

His answer is budget guardrails plus outcome-based evaluation: measure what a completed, correct outcome costs, cap what any single run may spend, and judge the system on results delivered instead of tokens consumed. That is how you get to the predictable ROI a CFO will sign off on.

## Who should watch

Product and engineering leaders taking agents into regulated industries, and architects who need to explain an agent system to a risk committee. Engineers will get the most from the orchestration and recovery split; managers from the economics. This is a lessons-from-deployment talk, so expect patterns and trade-offs more than code.

## Related Conf42 talks

- [Orchestrating AI Agents with Pattern Matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) by Michael Haim, more on how to orchestrate agents you can predict.
- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) by Michael Levan, on watching what agents spend.
- [Orchestrating Enterprise Intelligence: Designing Multi-Agent AI for ERP and Hybrid IT Systems](https://www.conf42.com/Prompt_Engineering_2025_Kasee_Palaniappan_enterprise_erp_intelligence) by Kasee Palaniappan, multi-agent design against enterprise legacy.

[Watch Rajesh Gupta's talk](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[From Agents to Systems: Orchestration, Recovery, and Economics](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) at Conf42 MLOps 2026.
