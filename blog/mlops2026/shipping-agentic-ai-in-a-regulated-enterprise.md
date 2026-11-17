# Name it, scope it, gate it, record it: agents in a regulated enterprise

Conf42 Blog, 2026-11-13, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/shipping-agentic-ai-in-a-regulated-enterprise

In short: Shanker Valipireddy (Aflac) at Conf42 MLOps 2026 on a four-step control plane for agents: identity, scoped grant, policy gate and immutable audit.

Teams spend months on model quality while the agent still runs under a shared service account with broad access and no record of what it did. At Conf42 MLOps 2026, Shanker Valipireddy, Principal Architect and AI Enablement Lead at Aflac, argues that the gap between an agent demo and production is control: who the agent is, what it may touch, and what happens when it goes wrong. His answer is four steps in the path of every call (identity, scoped grant, policy gate, audit) and a ten-item checklist to run before anything ships.

"You can swap the model and keep the same risk.", Shanker Valipireddy said at Conf42 MLOps 2026. He speaks as a platform person: more than twenty years in software and data, including a migration of twenty thousand data pipelines that he says saved about three million dollars in licences. His lens is that an agent is a caller on your platform, and should be treated like one.

## Why "regulated" changes the design

Four things. The data cannot be leaked, guessed or shown to the wrong caller, so access is the design and not a setting. Some actions need a human to agree before they happen; a log entry saying it already happened is not an approval. Audit must show who did it, when and under which approval, exactly. And a named person is accountable, because an agent has no judgment and no accountability.

## A shared service account tells you nothing

Identity comes first because everything else hangs off it. One identity per agent, carrying an owner, a purpose and a scope. When three agents share an account, the audit trail says the account did it, and you cannot stop one without stopping all. Revocation is his test: if killing a misbehaving agent means breaking four others, you will hesitate, and hesitation is how a small problem runs for hours. His rule from the slide: "If you cannot name the caller, you cannot trust the call"

The grant then says what that caller may do this time. Scoped to the data and tools the task needs, timed to expire when the task ends, issued per task. Standing access is how one wrong input becomes a large incident. Narrow the reach and shorten the time, and the same wrong input is a contained error you can explain.

## The agent never grades its own homework

The policy gate sits outside the agent and sorts actions into three bands. Low risk and reversible: auto-approve and log. Medium risk: approve, with a tighter scope and a shorter grant. High risk or irreversible: stop and escalate to a human. The risk comes from the action and the data, never from the agent's own view. And the bands get written down before shipping, because bands that live in reviewers' heads get drawn in different places, which you discover during an incident.

Every tool call and data operation is then recorded immutably: which agent, which grant, which policy decision, which human. His audit test is practical. Pick an old run at random and rebuild it from the record alone. If you have to guess at any step, the record is not finished. And there are no side doors: a tool that can be called directly will be, usually under pressure.

## Evaluation blocks promotion or it is a report

An agent ships only after passing evaluation, enforced by the platform the way a failed test blocks a release. If a failing result can be noted, discussed and shipped anyway, you have a report people read on the way to shipping. Regression evaluation runs on every change to the model, the prompt, the tools or the data access, and on a schedule, because the agent approved three months ago is not quite the agent running today.

Observability answers three questions in order: what it did, why (the grant, the policy decision, the inputs), and where it stopped. If a run stops at step 14, you need step 14.

## Reviewers sleep

What goes wrong mid-run is ordinary systems failure. Data changes under the agent. A tool fails halfway and nobody knows which half is done. A stuck agent loops, and every repeat writes or charges again. His controls are scoped grants, step limits and a kill switch. None of them make the agent smarter. They make its mistakes cheaper.

Then the 2 a.m. question. If the design assumes a reviewer is always there, it will make its own decision at night, and the wrong one. So high-risk work waits, reversible steps continue under a pre-approved grant, and the run records where it paused and why. He says how work should continue safely when the person is away is an area he is researching, and claims no results.

Rollout goes pilot, then shadow (the agent's actions are compared, not executed), then narrow production. Do not skip shadow because the pilot went well: a pilot is watched closely by definition.

## Who should watch

Platform, security and MLOps leads in banks, insurers and healthcare who have to say yes or no to an agent project. There is no demo, no vendor and no incident story from his employer; it is a reference pattern delivered slide by slide. If you already run per-agent identity and risk-banded approvals, the evaluation-as-gate and unattended-pause sections are the parts to watch.

## Related Conf42 talks

- [Securing the AI Stack: From Models to Agents to Infrastructure](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) by Kriti Faujdar of Yelp at Conf42 MLOps 2026.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026.
- [From Agent Trace to Reproducible Regression Test](https://www.conf42.com/MLOps_2026_Raju_Dandigam_trace_regression_agent) by Raju Dandigam of Navan at Conf42 MLOps 2026.

[Watch Shanker Valipireddy's talk](https://www.conf42.com/MLOps_2026_Shanker_Valipireddy_agentic_regulated_enterprise) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Shipping Agentic AI to Production: What a Regulated Enterprise Learned the Hard Way](https://www.conf42.com/MLOps_2026_Shanker_Valipireddy_agentic_regulated_enterprise) at Conf42 MLOps 2026.
