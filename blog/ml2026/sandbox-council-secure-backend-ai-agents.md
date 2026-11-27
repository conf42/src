# Securing AI coding agents: contain the body, convene a council

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/sandbox-council-secure-backend-ai-agents

In short: Booking.com payments engineer Marat Kenzhebulatov at Conf42 Machine Learning 2026 on sandboxes, multi-model review councils and audits for agents.

Marat Kenzhebulatov gave an AI agent one boring task: update the dependencies and run the tests. The build failed, the agent decided the environment was the problem, and 30 seconds later it had left the project folder and was rewriting his global Maven configuration. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), the Booking.com software engineer, who builds and maintains payment systems, explained what he built after that moment so that an agent's mistakes stop mattering.

The agent wasn't malicious. It was, in his words, trained to be aggressively helpful. In payments, where breaking things means people don't get on flights and hotels don't get paid, that helpfulness is the threat model.

## Prompts are guidelines, not guardrails

His first attempt was to talk the agent into being good: rules about PCI requirements, never hardcode secrets, don't make mistakes. It doesn't hold. Prompt injection is always possible, models are non-deterministic, and they can hallucinate past any rule. If a prompt is all that stands between the agent and a bug in production, "you don't have security strategy, you have hopes and prayers."

So if you can't trust the brain, contain the body. His playground has three walls:

- **A Docker container with a restricted file system.**
- **A command allowlist,** including which websites the agent may reach and no destructive commands. Where you draw the line is up to you: autonomous but not destructive.
- **A secrets manager.** The agent may work with credentials, but secrets never land in its context.

Treat the environment as hostile, and the agent's intent stops mattering. Malicious or merely clumsy, the result is the same: access denied.

## A council beats a single reviewer

The box stops the house burning down; it doesn't stop buggy code. Kenzhebulatov rejects both camps: the one that lets AI do the security review alone and the one that insists only humans can. His answer is a council, a pattern he credits to Andrej Karpathy: several agents on different LLMs, each with a role. A PCI expert that follows the standard. A code-quality reviewer explicitly prompted to be mean. An arbiter that weighs their views. If they can't agree, each writes its take and a human makes the call. Like a serious diagnosis, you want a second and third opinion, partly because a single model can reward-hack its way out of actually reviewing.

## The feature workflow

The loop he runs: a brainstorm where the agent questions the developer until it understands the feature, a plan that breaks the design into bite-sized tasks, execution by subagents with a small single-reviewer check after each task, then the full council on the finished change. He stays in the loop throughout. The agents amplify his input; they don't replace it.

## Audit everything, start small

After ten years in fintech he assumes something will go wrong. You can't debug an agent like a normal program, so record the sessions and the reasoning, log as much as possible and keep the logs. If an agent tries to escape the playground, you want to know exactly how.

None of this needs a big infrastructure project on day one. Start by having the agent describe your project in a markdown file and review what it writes. Then turn your team's routine tasks into skills, then add the council. His checklist: no secrets in context, a physical playground instead of rules, a human approving critical actions, and cross-validation of everything.

## Who should watch

Backend and platform engineers letting coding agents near production repositories, especially in regulated domains. It's short, practical and opinionated; security teams will find a vocabulary for a policy, and developers a setup they can build in an afternoon.

## Related Conf42 talks

- [Hardening AI coding agents with hooks: enforcing least privilege](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks), Karan Bansal (ArmorCode), Conf42 DevSecOps 2026
- [Your AI has too much access: deterministic authorization for coding agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents), Sohan Maheshwar (AuthZed), Conf42 LLMs 2026
- [The harness decides what to trust: running AI coding loops without shipping fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence), Ruben Marcus Luz Paschoarelli (MultiVM Labs), Conf42 AI Agents 2026

[Watch Marat Kenzhebulatov's talk](https://www.conf42.com/Machine_Learning_2026_Marat_Kenzhebulatov_vision_computer_imaging)

[Watch the talk on YouTube](https://youtu.be/qYNGvp_ECsU).

## Watch the talk

[Building Secure Backend Services with AI Agents](https://www.conf42.com/Machine_Learning_2026_Marat_Kenzhebulatov_vision_computer_imaging) at Conf42 Machine Learning 2026.
