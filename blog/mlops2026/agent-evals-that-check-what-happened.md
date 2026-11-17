# Grade the agent on what the service recorded, not on its reply

Conf42 Blog, 2026-11-12, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/agent-evals-that-check-what-happened

In short: Sajal Garg (Microsoft AI) at Conf42 MLOps 2026 on agent evals that compare the reply, the tool actions and the service state before a release decision.

An agent's reply tells you what it claims. Its tool calls tell you what it tried. Only the service tells you what changed. At Conf42 MLOps 2026, Sajal Garg, Principal Software Engineer at Microsoft AI, follows one small request from a normal run through planted failures to a release decision, and shows why an update with nicer writing scores still gets blocked. Every job, trace and score in the talk is a hand-constructed teaching example, which he says up front.

## One task, four boxes, three records

The task: prepare a training job, wait for approval, submit it once, then return its real job ID and current status. Four actors stay on screen the whole time: the user, the assistant, a job tool that can create or look up jobs, and the training service. Approval is stored separately, because an assistant saying the user approved cannot create permission.

Sajal pins down success before running anything. It needs one matching accepted job, its real ID, and a reply that matches the observed status. Submitted does not mean finished. Reporting "submitted and queued" satisfies the task; reporting that training finished needs evidence of completion. And seeing job A in the reply does not rule out an unseen second job, so the check reads the service's record.

To make this repeatable he adds a test runner and a checker. Each attempt starts in a fresh sandbox, the expectation is fixed before the run, and both the current build and the updated build get the same four cases: approved work, no approval, a lost reply, and a result too uncertain for another write. "The reply is an input to check, not its own answer key," Sajal Garg said at Conf42 MLOps 2026.

## A harmless message can sit on top of an unauthorized job

In the no-approval case he plants a defect in the tool that skips the approval check. The tool sends the create request, the service accepts a job, and the assistant returns a calm message that the plan is ready. The check expected zero accepted jobs and found one. The friendly reply cannot cancel the effect, and the build is blocked.

He also separates facts from prose. A writing rubric gives points for a findable ID and status, plain language and a clear next action, but a failed or unknown factual check gets no style score at all. If the writing judge has an outage, the reply is unscored and the execution evidence stands.

## A timeout is missing knowledge

The lost-reply case is the one most teams will recognise. The first create request is accepted as job A, the test drops the service's reply, and the assistant sees a timeout. After a restart, the updated build creates again and the service accepts job B. The assistant then reports that it submitted one job. The independent observer sees two accepted IDs.

The corrected recovery looks up the original operation before any new write. If the lookup is unreliable, an empty search does not prove rejection. A retry needs valid approval plus either a real provider guarantee against duplicates or authoritative proof that the first request was not accepted. When time runs out without a safe answer, the right behaviour is to pause further writes and say what remains unknown.

Clean evidence takes more than clearing the chat. Each trial needs isolated service state, approval records and deduplication history, and a trial is not closed just because the assistant returned: a pending request could still create a job after you declared a pass.

## Block, hold or pass, and missing scores are never zeros

In the comparison ledger, four cases run twice each, so eight attempts per build. The current build satisfies all eight. The updated build satisfies four, with an unauthorized job, a duplicate and two unknown outcomes among the rest, while its writing average looks better on a smaller rated subset. A known unauthorized or duplicate job means block. Missing required evidence without a known critical failure means hold. Neither is a pass, and a better writing average cannot buy back a duplicate job.

After the fix, the retest satisfies all eight, which supports a limited pilot and nothing broader. The imagined pilot then finds a case the suite missed: the job count is right, the service says queued, and the assistant tells the user training finished. "Queuing is not a failure, misreporting it is," as Sajal puts it. The new test pairs a queued example with a succeeded one, so a lazy fix that always answers "queued" fails too. The suite grows to twelve attempts and the loop repeats.

## Who should watch

Engineers who own evals or release gates for tool-using agents, especially where an action costs money or cannot be undone. This is a methodical, diagram-driven session with no product demo and no measured production data. If your current agent eval is an LLM judge reading final answers, the failure taxonomy here is the upgrade path.

## Related Conf42 talks

- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler (Adobe) at Conf42 MLOps 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.
- [Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) by Ajay Munjuluru at Conf42 MLOps 2026.

[Watch Sajal Garg's talk](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) at Conf42 MLOps 2026.
