# Gate the three to six agent actions you can't take back

Conf42 Blog, 2026-09-01, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/gate-irreversible-agent-actions-only

In short: Artemis Leonardou of NOFire AI at Conf42 DevSecOps 2026 swaps "is it risky?" for "can I undo it?" and gates only the agent actions that fail that test.

Your alerting can work perfectly and still be useless, because it reports on an agent action that already ran. At Conf42 DevSecOps 2026, Artemis Leonardou, founding engineer at NOFire AI, argued that agent safety is an ordering problem, and that the fix is a short, written-down list of the three to six things your agent can do that cannot be undone, each gated before it executes.

It's a tool-agnostic talk with no product pitch, and it comes with homework that takes about an hour.

## Humans hesitate, agents don't

The setup is simple. Review, CI and monitoring have worked for twenty years because the thing taking the action was a person, and a person about to do something irreversible pauses. Every incident review has the moment where someone had a bad feeling and stopped. An agent has no half second: the decision and the action happen together, and the alert arrives after both.

Artemis learned this the expensive way. An agent wrote a change, a human approved it, CI passed, and it then did something that could not be taken back. Every control did exactly what it was built to do. As the talk puts it, when you cannot undo an action, the report "is not a control. It is a receipt."

## Ask "can I take this back?" instead of "is this risky?"

Risk needs a probability and an impact, and you end up with a spreadsheet nobody believes. Reversibility is a fact about your system that its owner can answer in seconds. That question sorts every agent action into three buckets:

- **Freely reversible** (drafts, scratchpad writes, any read): never gate. A gate here is pure tax on every execution.
- **Reversible with effort** (needs a deploy, or another person): don't gate, bound it. Make the change small and the undo path one step until it behaves like bucket one.
- **Not reversible**: gate before execution, every time.

Bucket three is the part to steal. Artemis's categories: sending a message to a person, publishing anything externally visible (a release, a status page, a registry package, DNS), moving money, deleting or overwriting without a snapshot, granting access, rotating or revoking credentials, merging to a branch that deploys, and calling a third-party API with a side effect. In a real system that usually comes to three to six distinct actions, not three hundred. The list only feels endless because nobody wrote it down.

The one-hour exercise: list what the agent is *permitted* to do (tools, credentials, what the token actually authorises), then for each item write how long the undo takes and who has to be awake for it. A ten-minute rollback that needs one specific person at a laptop is a two-hour rollback at 3am. Gate the "never" row, bound the "hours" row, leave the "minutes" row alone.

## The call site beats the platform

You don't need a control plane. Artemis walks through four placements in a pipeline you already have, in order of how late they fire: a wrapper at the call site of the send, delete or payment function; a required pre-merge check on the deploying branch; a CI job that inspects the *output* rather than the prompt or the diff; and a policy check at the boundary to the external system. The call site is the cheapest and the only one that catches an action triggered from somewhere you forgot about. Artemis uses the first and third, and skipped the boundary check as too much architecture for a small number of already-wrapped calls.

## The gate that caught nothing

The honest section is the best one. Gates add latency and block legitimate work, and a badly scoped gate is worse than none because people route around it and the paper still says you're covered. Artemis's own first attempt gated file writes, because they felt dangerous and were easy to intercept. Writing a file was bucket one, and the message that actually mattered went out three steps later, untouched. The lesson: gate the action, not the layer that's convenient to hook.

The final list is short and specific: anything that sends to a human, deletes without a snapshot, or grants access. Pull requests, branch writes, reads and non-production deploys are deliberately ungated. Two limits are stated plainly too: a gate doesn't make the agent correct, it bounds what an incorrect one can reach, and the system in the story was small.

## Who should watch

Anyone whose agents already have write access to something they care about, and especially the team that's about to wrap every tool call in an approval prompt. Skip it if you want a policy engine walkthrough; this is the thinking you do before picking one.

## Related Conf42 talks

- [Autonomy with Guardrails: Operating Agentic Automation in High-Risk Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) by Ajay Athitya Ramanathan at Conf42 SRE 2026.
- [Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda at Conf42 Feature Flags 2026.
- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis at Conf42 AI Agents 2026.

[Watch Artemis Leonardou's talk](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/_PzgoRu8Wd0).

## Watch the talk

[Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) at Conf42 DevSecOps 2026.
