# You can't build four nines on top of three nines

Conf42 Blog, 2022-06-08. https://www.conf42.com/blog/sre2022/four-nines-on-three-nines-disappoints

In short: Kolton Andrus (Gremlin) at Conf42 Site Reliability Engineering 2022 on reliability basics - expect failure, keep it simple, test redundancy and dependencies for real

A recovery mechanism you have never exercised is a second failure waiting for the first one. At Conf42 Site Reliability Engineering 2022, Kolton Andrus, Founder and CTO of [Gremlin](https://www.gremlin.com), who earlier worked on reliability at Amazon and Netflix, gave a compact Reliability 101: expect failure, keep systems simple, build redundancy and prove it works, design for operations, and know which of your dependencies can actually take you down.

It's billed as a 101 and it is one, delivered by someone who has been paged for the consequences. Good first talk for a team starting out; a useful checklist for one that isn't.

## Expect failure, then keep it simple

The first tenet is to design for the paths users take when things go wrong, not just the happy path. Failure can arrive at any level at any time. The second is to prefer the simpler option over the clever one. Kolton's rule of thumb: an optimisation that buys an order of magnitude is worth its complexity; one that buys an incremental gain probably isn't.

He admits the tension with the third tenet. Redundancy in hosts, containers, data and the ways work gets done is essential, and redundant everything is a more complicated system than one of everything. Weigh both.

## Are you comfortable taking down a zone?

His test for redundancy is a question: are you comfortable bringing down a host, a service, a zone, a region? If you'd rather not try, you probably aren't there yet. That, he points out, is why Chaos Monkey exists: in the cloud hosts fail, and forcing the failure on engineers is a social strategy as much as a technical one.

## Design for operations from the start

Operations usually get attention after the service ships or after the first incident. Kolton wants it earlier: observability beyond front-door error rates, so you know the components underneath are healthy; configurability that lets you tune the system's edges; and runbooks, alerts, monitors and scripts in source control like the code. Thinking about failure modes up front, test-driven style, beats duct-taping a fix on later.

Every new dependency is a prompt for three questions: is it critical, can I degrade gracefully without it, do I need it at all? For traffic, never accept more work than you can complete; shedding load gives callers a fast failure instead of an unknown wait. On the calling side, circuit breakers stop you hammering a failing service and force the question of what to do instead.

## Failure modelling, borrowed from security

He recommends a team brainstorm borrowed from threat modelling: what can go wrong, what happens if two things go wrong at once, which failures you must live with, and which you can turn into non-failures by degrading gracefully. With thousands of moving parts, combinations that seem rare become routine.

His e-commerce example makes the dependency point concrete: the checkout service is critical, while the recommendation service can fail quietly and the user still completes the purchase. Knowing which is which is often a guess, and failure testing replaces the guess with evidence. The maths matters too, because availability gets worse as you compose services.

"If we're trying to build a service with four nines of uptime on top of a bunch of services that have three nines of uptime, we're probably going to be disappointed," Kolton Andrus said at Conf42 Site Reliability Engineering 2022.

He also quotes James Hamilton's paper On Designing and Deploying Internet-Scale Services, still worth reading after 15 years: if you won't fail your data centres on purpose, you don't really know your system survives it, and untested recovery mechanisms tend not to work when needed.

## What to do first

Three starting points. Redundancy: lose a host, graduate to a zone or data centre, then turn the disaster recovery plan from a paper exercise into a real failover or traffic shift, which he promises will turn up lots of small surprises. Dependencies: know all of them, find the critical ones by failing them hard, and tune timeouts, back-off and when to stop calling. Training: give people a place to practise, with current runbooks, known alerts and working access, during the day after the coffee has kicked in rather than at 2am.

## Who should watch

Teams early in their reliability work and engineers who want a crisp list to take into a design review. Experienced chaos practitioners will know the material.

Related Conf42 talks: Henrik Rexed on [chaos engineering for Kubernetes in production](https://www.conf42.com/Site_Reliability_Engineering_2022_Henrik_Rexed_kubernetes_chaos_engineering_production) and Christian Elsen and Lerna Ekmekcioglu on [reliable multi-region architecture](https://www.conf42.com/Site_Reliability_Engineering_2022_Christian_Elsen_Lerna_Ekmekcioglu_reliable_multiregion_arch), both from the same event, and Nick Hodges on [self-healing systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems).

[Watch Kolton Andrus's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Kolton_Andrus_reliability_101) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From Gremlin

Gremlin is a chaos engineering company; the hard-failure tests of hosts, zones and dependencies Kolton recommends are the kind of experiment it runs.

- Gremlin: [gremlin.com](https://www.gremlin.com)

[Watch the talk on YouTube](https://youtu.be/NMG_JWYN_28).

## Watch the talk

[Reliability 101](https://www.conf42.com/Site_Reliability_Engineering_2022_Kolton_Andrus_reliability_101) at Conf42 Site Reliability Engineering 2022.
