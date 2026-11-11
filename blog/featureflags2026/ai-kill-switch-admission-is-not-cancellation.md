# An AI kill switch that only closes the front door is not one

Conf42 Blog, 2026-09-17, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/ai-kill-switch-admission-is-not-cancellation

In short: Capital One's Parthiban Rajasekaran at Conf42 Feature Flags 2026 on why a disabled flag doesn't stop in-flight agent work, and how to prove containment.

The dashboard said Disabled, a new request was rejected one second later, and fifteen seconds after that the agent sent the customer email anyway. At Conf42 Feature Flags 2026, Parthiban Rajasekaran, Principal Dev Engineer at Capital One, staged that drill against a running agent loop to make one point: a feature flag is an admission control, and a real kill switch also needs cancellation.

The drill is simulated, with mock tools and a mocked SMTP server, but he is clear that the mechanisms are real. Execution 47 looked up a customer, filed a Jira ticket and queued a follow-up job before the kill. The worker that picked up the job never checked the flag again. In production, as he puts it, there is no unsend.

## A flag value is intent, not a stop

The flag answered whether new work may start. The operators heard an answer to whether existing work had stopped. Once work is past that decision, you're no longer selecting features, you're cancelling a running system. Parthiban reminds the audience the industry already paid for this lesson without any AI involved: Knight Capital in 2012, where a repurposed flag triggered obsolete trading code left on one server and engineers spent about 45 minutes trying to make it stop.

Agents add a twist. The thing doing the work picks its own next step.

## Five jobs a kill switch has to do

He lays out a contract for what stop has to mean: admission (no new autonomous work), propagation (tell running executions cancellation was requested), interruption (stop what can still safely be stopped), compensation (reconcile what already happened) and verification (prove activity ceased within what you can observe). None of the mechanisms are new, he notes: cancellation tokens, fencing tokens, the saga pattern. What's new is where they have to live.

The concrete design: every execution gets an identity and a generation number. When the flag flips, a listener marks active executions as cancel requested and bumps the generation from 18 to 19; a reconciler sweeps up whatever the listener missed. The generation travels as a fencing token, so the downstream resource can reject stale work itself.

The subtle bit is timing. Checking the flag before every tool call is better than nothing, but the same worker can produce two outcomes depending on whether cancellation lands before or after its check. In the drill the window wasn't milliseconds, it was fifteen seconds of a job sitting in a queue. Revalidate as close to the side effect as you can, and use idempotency keys where the downstream supports them.

## Classify every tool before you grant it

Work comes in three kinds. Reversible (a draft: delete it). Compensatable (the Jira ticket: close it through deterministic, pre-approved code, never back through the agent you just cancelled). Irreversible (the email). If you can't classify a tool your agent can call, Parthiban says that's your first finding.

There's an agent-specific trap here too. A tool call that returns a cancelled status can look like a transient error to the model, which may then try a different tool. So cancellation is never the model's call: enforce it in the harness before the model's next turn. Routing around your own off switch is a very agentic kind of creativity.

## Containment is a metric you can test

The rerun shows the difference. The worker sees generation 18 against 19 and refuses to cross the boundary, the reasoning loop exits at its next safe point, the ticket is closed through the compensation path, and after a five-second quiet window the run counts as contained at 24 seconds. An OpenTelemetry trace of the single execution backs up the console output.

He defines "time to containment" (explicitly his own metric, not an industry standard) as zero active executions, zero unresolved compensations and a quiet window with no unauthorised side effects. He is equally honest about the limits: the GenAI semantic conventions are still in development, and if trace context doesn't survive the SQS hop, the trace doesn't prove end-to-end containment. Turning the flag back on gets its own warning: resume, replay and flush each make different assumptions, and flush is often the safest.

## Who should watch

Anyone who has put an agent behind a flag and called it a kill switch. It's a tight lightning talk that ends on three questions worth taking into your next design review: what happens to in-flight work when the flag changes, which side effects are interruptible, and what evidence would convince you mid-incident that the agent has stopped.

## Related Conf42 talks

- [Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou of NOFire AI at Conf42 DevSecOps 2026.
- [Autonomy with Guardrails: Operating Agentic Automation in High-Risk Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) by Ajay Athitya Ramanathan of FourthSquare at Conf42 SRE 2026.

[Watch Parthiban Rajasekaran's talk](https://www.conf42.com/Feature_Flags_2026_Parthiban_Rajasekaran_ai_kill_switch) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/ptOND07GfnU).

## Watch the talk

[Your AI Kill Switch Is Probably Broken](https://www.conf42.com/Feature_Flags_2026_Parthiban_Rajasekaran_ai_kill_switch) at Conf42 Feature Flags 2026.
