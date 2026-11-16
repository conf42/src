# Multi-agent AI fits ERP when autonomy is bounded and logged

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/multi-agent-erp-bounded-autonomy

In short: Kasee Palaniappan (Ariba, SAP America) at Conf42 Prompt Engineering 2025 on multi-agent AI for ERP and hybrid IT, from frameworks to bounded autonomy.

A marketing chatbot here, a finance tool there, an onboarding bot somewhere else, and a human copying data between them: that's how Kasee Palaniappan describes most enterprise AI so far. At Conf42 Prompt Engineering 2025, Kasee, from Ariba Inc (SAP America), made the case for coordinated multi-agent systems across ERP and hybrid IT, plugged into existing systems through APIs, with bounded autonomy, audit logs and a human on every critical decision.

It's a concise strategy talk for people who own enterprise systems. It names real frameworks and use cases, and spends as much time on the brakes as on the engine.

## Think team, not chatbot

Kasee's definition of a multi-agent system is helpfully plain. Stop picturing one AI and picture a team of specialists: a data analyst agent, a compliance agent, an inventory agent, each with a role, sometimes subdivided further. They communicate, collaborate and delegate, and they work towards a high-level business objective. His example goal: reduce procurement cost by 10%, with agents splitting the work and minimal human intervention.

## Four pillars of orchestration

He organises the architecture into four pillars. Goal-directed planning breaks a big objective into executable tasks per agent, and he calls it the most important. Dynamic reflection lets the system review its own successes and failures and improve. Tool orchestration gives agents access to real APIs, databases and ERPs; without it they're just chatting. Collaborative problem solving lets agents share insights across departmental silos.

For building it today he points to three frameworks: LangGraph for graph-based, cyclical workflows where agents may need to rethink a step; AutoGen from Microsoft for conversational agents that solve tasks together; and CrewAI for role-based crews defined like a team with a hierarchy.

## Where it lands in the business

The use cases are the back-office ones where ERP lives. Procurement: supplier evaluation and contract compliance monitoring around the clock across global supply chains. Finance: invoice processing, real-time expense reconciliation, and anomaly detection that also generates the audit trail. HR: onboarding workflows and conversational answers to employee questions. Document management: classify, extract, structure and route documents to the right person. He cited figures from multi-agent deployments of a 68% reduction in processing time, 92% better accuracy on tasks like data extraction and 45% better cost efficiency.

## Don't rip and replace

The question every ERP owner asks is how this works with a massive SAP or Oracle estate. Kasee's answer is modularity: agents connect to existing cloud and on-prem systems through standard APIs and middleware, so you can automate one small piece of a process first. That lowers risk and gets value earlier without betting the ERP on it.

## Bounded autonomy is the safety model

He's direct about the three hard problems: security and data privacy when agents touch sensitive data; scalability in compute and cost as you go from ten agents to a thousand; and governance, because when an agent decides on someone's behalf, regulators will want to know what it considered and why. His three safeguards: comprehensive audit logging of every decision, action and piece of data an agent touches; bounded autonomy, with clear operational limits and programmed escalation paths to humans; and incremental deployment, starting with a low-risk, high-value use case. His recurring line: don't try to boil the ocean.

The roadmap follows: foundation, pilot, scale, optimise, ending in what he calls a self-optimising digital ecosystem.

## Who should watch

Enterprise architects and ERP owners being asked about agents, and IT leaders who need a shared vocabulary for agent roles, frameworks and governance before a vendor supplies one. If you've already shipped LangGraph or CrewAI in production, the related talks get into implementation patterns.

## Related Conf42 talks

- [Building Event-Driven AI Agents for Proactive SAP Incident Management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events) by Pon Murugesh Devendren at Conf42 AI Agents 2026.
- [AI Orchestration: Getting Super Agents to Complete a Mission](https://www.conf42.com/Prompt_Engineering_2024_Batandwa_Mgutsi_ai_orchestration_superagents) by Batandwa Mgutsi at Conf42 Prompt Engineering 2024.
- [Orchestrating AI Agents with Pattern Matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) by Michael Haim at Conf42 AI Agents 2026, for a more deterministic take.

[Watch Kasee Palaniappan's talk](https://www.conf42.com/Prompt_Engineering_2025_Kasee_Palaniappan_enterprise_erp_intelligence) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/2TTHrtTop70).

## Watch the talk

[Orchestrating Enterprise Intelligence: Designing Multi-Agent AI for ERP and Hybrid IT Systems](https://www.conf42.com/Prompt_Engineering_2025_Kasee_Palaniappan_enterprise_erp_intelligence) at Conf42 Prompt Engineering 2025.
