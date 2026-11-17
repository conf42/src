# Gate the agent's claim, not its confidence

Conf42 Blog, 2026-09-15, updated 2026-11-17. https://www.conf42.com/blog/featureflags2026/confidently-wrong-agents-need-inline-sources

In short: Girish Konda (Microsoft) at Conf42 Feature Flags 2026 on three boundaries for agents: evidence before recommendation, approval before action, observation after.

Errors went from ten to six, so the agent reports a 40 percent reduction. Requests went from a thousand to six hundred, so the error rate is one percent before and one percent after. At Conf42 Feature Flags 2026, Girish Konda, Principal Software Engineer at Microsoft and tech lead for capacity management in Microsoft Fabric, uses that sample to show how a well-formatted agent answer can be wrong without a single error message, and what to build so it cannot drive the next step. He notes the views are his own.

His opening rule: "Gate the claim, not the confidence." An agent proposes a claim, a read tool returns something inspectable, a record says what was read, which version and what it covers, and a validator checks those inputs. The agent's confidence is not one of them. If validation fails, the path is a refusal with the exact reason.

## A filled-in source field is not support

His illustrative bad answer says the error rate fell 80 percent, cites a retry policy section, recommends a config change and calls the status confirmed. Line by line, nothing holds. The percentage needs a numerator, a denominator and a matched time window. The policy reference needs a real document. The confirmation needs an observation of the effect, not a sentence saying the work is finished.

Resolving a reference is several checks, kept separate. A plausible link can point nowhere. A real document can be the wrong version. The right version can say something unrelated: in his example the runbook exists and describes rollback steps, which says nothing about error rates. Open the source, pin the version, match the scope, then ask whether it supports the claim. For code review that means a commit, the changed code and a test asserting the claimed behaviour. A test with a nearby name does not count.

## One wrong fact becomes three agreeing documents

The triage note cites the unsupported claim. The review note reuses it. The runbook note takes it as a reason to proceed. Three artifacts agree, and there are zero independent observations among them. Fixing the claim in a new revision does not repair anything by itself; the old artifacts must be blocked until rebuilt. That is his answer to the agent that accepts a correction and repeats the old claim later. The test is whether the old fact can still drive the next action.

Facts also expire. In his sample, data is as of 9:05, read at 9:06, used at 9:07 under a five-minute freshness limit. A second decision at 9:15 needs a reread. The clock that matters is the data's as-of time, a cache hit does not reset it, and five minutes is an example, not a recommendation.

He also refuses to collapse states. An input is established positive, established negative, not established, stale or not applicable. A probe that times out is neither healthy nor unhealthy. The refusal may read the same, but each reason sends the next person to different work.

## The check lives outside the prompt

If the same model can skip a check and declare it passed, he says, you have a request and not an enforced boundary. His short Python gate has the caller own the required checks, and any result that is not established positive returns a refusal. A pass only sends the recommendation to human review. It is not an authorised write.

Writes get their own boundary. He describes a development session in which an agent, told to get explicit permission before pushing to a remote, found its own way through the authorisation step. He frames it as a failure mode to guard against: more capable agents find more routes to a goal, and prompt-only restrictions are not enforced across permission boundaries. His design is a separate write broker, isolated credentials, and approval bound to an exact operation with an approver, an action ID, a payload digest, an expiry and single use. Change staging to production and the approval is void.

Resuming a paused session carries no approvals with it. "An old conversation is not evidence of a current permission.", Girish Konda said at Conf42 Feature Flags 2026. Restore context, not side effects.

## Submitted, accepted, executed and confirmed are four signals

Submitted means we sent something. Accepted means something admitted it. Executed is a component reporting on itself. Confirmed needs a separate observation matched to the claim, and reading back a retry setting confirms the setting, not that users see fewer errors.

He grounds this in a regression test from an open-source A2A repository. A task reaches completed and is persisted while the notification endpoint returns service unavailable or a redirect. With three persisted events and two attempts per event, that is six requests for the unavailable case and three for redirects, and zero accepted notifications. The task is still completed. Completion does not prove delivery, and failed delivery does not entitle the sender to rewrite task state.

## Who should watch

Engineers running agents against incident triage, telemetry, code review and runbooks, and anyone designing approval flows for agent writes. Be aware that the abstract promises failures from his day job, while the talk works through fictional and synthetic examples plus one public test, and he names the limits of his offline example himself. It is dense and slide-driven. The three boundaries he closes on are evidence before recommendation, approval before action, observation after it.

## Related Conf42 talks

- [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal of ArmorCode at Conf42 DevSecOps 2026.
- [From Agent Trace to Reproducible Regression Test](https://www.conf42.com/MLOps_2026_Raju_Dandigam_trace_regression_agent) by Raju Dandigam of Navan at Conf42 MLOps 2026.
- [Make Agents Observable: Tracing Decisions, Tool Calls and Recovery](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) by Emerson Braun of Plan A Technologies at Conf42 Observability 2026.

[Watch Girish Konda's talk](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/9VbGcnTuUCk).

## Watch the talk

[Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) at Conf42 Feature Flags 2026.
