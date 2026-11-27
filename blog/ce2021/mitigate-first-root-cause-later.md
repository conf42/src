# Mitigate first, find the root cause later, and rehearse both with chaos

Conf42 Blog, 2021-02-24. https://www.conf42.com/blog/ce2021/mitigate-first-root-cause-later

In short: Leonid Belkind (StackPulse) at Conf42 Chaos Engineering 2021 on pairing chaos experiments with generic mitigations to restore service before the root cause is known

Chaos experiments show you where a system breaks; they don't tell you how to get it back up at 3am. At Conf42 Chaos Engineering 2021, Leonid Belkind, CTO and co-founder of StackPulse, pairs chaos engineering with generic mitigations: rehearsed, reusable actions such as rollback, traffic drain or quarantine that restore service before anyone has finished the root-cause analysis. Each practice, he argues, is what makes the other worth the money.

It is a conceptual talk, no demo, built around one cost curve and one outage timeline.

## How much resilience do you actually want?

He opens with a waiter asking how delicious you would like your dish. Nobody answers "passable", and nobody asks for a merely decent email or HR service either. But resilience costs, and the curve bends the wrong way: early gains are cheap, each further step costs more, and the last increments can cost twice as much again.

So the real target sits between two points: the minimum service level consumers will accept, and the level where the cost of delivering it exceeds what they will pay. Price sensitivity varies, which is why premium tiers exist, but a margin only lives in between. That reframes the job. Leonid Belkind said at Conf42 Chaos Engineering 2021: "When talking about resilience, we define proficiency as the ability to deliver more resilient services for less cost."

No single technique gets you there, in his view; it takes a combination of tools and methods, each applied to the problem it suits.

## Isn't a generic mitigation just a band-aid?

A mitigation is any action that prevents the impact of a breakage, from an emergency hotfix to someone logging into a production box to restart a process. A generic mitigation is one that applies across many kinds of outage, sometimes before the cause is known.

He sees the objection coming: restarting a leaky service once a day so nobody notices is not what he means. The idea, he says, comes from organisations like Google and Facebook, and the outage timeline shows why. The usual sequence runs source, alert, context, triage, root-cause analysis, fix, review, deploy, and only then does user impact end. That takes minutes at best and, even at leading services, hours or days. Move the mitigation to triage, restore service, and do the analysis and the fix afterwards. The root cause still gets found; users just aren't waiting for it.

To put a number on the waiting, he cites a Twitter thread among practitioners that put good continuous deployment at around 15 minutes from verified fix to production. That is 15 minutes of outage for the deploy step alone, before anyone has understood or reviewed the fix, or found the right person awake to write it.

## What do generic mitigations look like?

His catalogue, each with the reason it is harder than it sounds:

- **Rollback** of business logic, binaries, configuration or data to the last known good state. Easy for one component; a multi-component rollback with dependencies and schema changes needs preparation and regular testing.
- **Upsizing or downsizing.** Scaling one stateless service is simple with a modern orchestrator; scaling without regard to how components relate can just move the problem. Scaling down often wants a human in the loop.
- **Draining traffic** to another cluster, member or region, ideally with zero user impact.
- **Quarantine**: pull an instance out of rotation, rebalance to healthy peers, then investigate it.
- **Block lists** for a user, account or session sending problematic requests, granular and in real time, with quotas and guardrails rather than just on or off.
- **Disabling a noisy neighbour** on a shared resource such as a database, with quotas or a pause.

The bar he sets for each: mature, tested, kept warm, and usable by the least technical person on staff in the middle of the night.

## Why do the two belong together?

Chaos engineering recreates turbulent conditions; generic mitigations keep the service within its objectives when they happen. Experiments verify that the mitigations actually remediate the failures, and they surface the spots that still lack one, which sets the next investment. Chaos alone leaves you with findings and an expensive re-architecture as the only fix. Mitigations alone are tested only against surrogate scenarios, so you can't tell which one buys the most resilience per dollar.

## What do you need to start?

For mitigations: a platform to write modular, reusable flows that go through the normal lifecycle (versioning, review, tests); an orchestrator that triggers them, monitors success and brings humans in when needed, running on infrastructure separate from production so an outage doesn't take out the cure; and visibility into every invocation. For chaos: injection at the infrastructure, network and user-simulation layers, plus guardrails that contain an experiment and stop it when containment fails.

## Who should watch

SREs with a chaos programme that produces findings faster than the team can fix them, and anyone writing runbooks who wants to turn them into something safer to run at night.

## Related Conf42 talks

- Nick Hodges on [self-healing systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) at Conf42 Chaos Engineering 2022.
- Uma Mukkara on [continuous SLO validation using chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering) at Conf42 SRE 2021.
- Fred Moyer on [SLOs and error budgets at scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) at Conf42 Observability 2023.

[Watch Leonid Belkind's talk](https://www.conf42.com/Chaos_Engineering_2021_Leonid_Belkind_generic_mitigations_self_healing_systems)

## From StackPulse

Leonid is CTO and co-founder of StackPulse. The talk itself stays vendor-neutral: the product never comes up beyond his introduction.

- StackPulse: [stackpulse.com](https://stackpulse.com)

[Watch the talk on YouTube](https://youtu.be/Zl0q_JJzCUQ).

## Watch the talk

[Chaos Engineering + Generic Mitigations: The Path to Self-Healing Systems](https://www.conf42.com/Chaos_Engineering_2021_Leonid_Belkind_generic_mitigations_self_healing_systems) at Conf42 Chaos Engineering 2021.
