# Set the SLO, then break things on purpose to see if it holds

Conf42 Blog, 2021-10-01. https://www.conf42.com/blog/sre2021/slos-and-chaos-engineering-reduce-trauma

In short: Julie Gunderson (Gremlin) and Mandi Walls (PagerDuty) at Conf42 Site Reliability Engineering 2021 on SLOs as team tools and chaos experiments that test them

Two former PagerDuty colleagues, now at two vendors, make the case that SLOs and chaos engineering belong in the same sentence. At Conf42 Site Reliability Engineering 2021, Julie Gunderson, Senior Reliability Advocate at Gremlin, and Mandi Walls, DevOps Advocate at [PagerDuty](https://www.pagerduty.com/), argue that service level objectives tell a team what users will tolerate, and failure injection is how you check that those numbers, and the dependencies under them, are the right ones before an incident checks for you.

## What is the vocabulary, minus the lawyers?

Walls sets the baseline quickly and leaves SLAs to legal: they are the contract, with chargebacks or credits attached. The engineering side is the SLI, the metric you care about, and the SLO, the point past which users start leaving. Whatever is left over is the error budget, the wiggle room for experiments, blue-green deploys and changes that might not land perfectly.

The maths is deliberately plain. Mandi Walls said at Conf42 Site Reliability Engineering 2021: "And our SlI is going to be the number of good things that happen divided by the number of all the things that happened." At 100,000 events, a 99% target leaves 1,000 events of budget. Gunderson adds a worked buffer: an SLA promising 90% of web requests under 500 milliseconds for the month, an internal SLO of 95%, and a 5% gap the team can spend on new features without anyone getting a refund.

## What do users actually care about?

The talk keeps returning to the user experience. Some users are sensitive to slow pages, others to heavy payloads on mobile. Search and the shopping cart may matter more than updating billing details. YouTube is the example of a page that loads the main thing first: the player appears, the rest builds around it.

CPU and memory still matter as early warnings, but users never see them. They see slow searches. So SLIs should describe behaviour at the edge of the service, and sometimes the only way to learn what users value is to ask them, because the feature the team loved may be the one nobody uses.

## Where does chaos engineering fit?

Gunderson walks the SRE pyramid: monitoring and observability, incident response, post-incident analysis, testing and release, capacity planning, product. Chaos engineering shows up twice. After a blameless postmortem you replay the incident on purpose to prove the fix works and keeps working. In testing and release you run experiments against new features.

It also answers the worry that a team lacks the metrics to start. Injecting failure validates the monitoring itself. Take the email server down: did the customer still check out, inside the agreed time, even without the confirmation email? Experiments also find surprise critical paths, like the Redis cache everyone assumed was optional, which may force the SLOs to be redrawn.

Production is not a prerequisite. Julie Gunderson said at Conf42 Site Reliability Engineering 2021: "So some people say that you can only do chaos engineering in production. That's the only way." Her answer is that it is not true: start with tabletop exercises, move to development and staging, start small and grow the blast radius, the same way code moves up through environments.

## What about dependencies you don't own?

A service cannot promise more than its backends deliver. If an upstream dependency, internal or third-party, publishes a lower availability, you either code defensively around it (turn it off, take it out of the user path, red-button it) or find another provider. Latency attacks are the natural experiment here, since SLOs are time-sensitive.

Their lifecycle closes the loop: start from user behaviour, set SLIs and SLOs, keep them green, run chaos tests on new features, and feed error budget burn into postmortems and sprint planning. Some teams freeze features when they get close to the edge. And the SLOs are for the team, not a cudgel for punishing people.

The demo scenario is a three-vendor relay: Gremlin injects instance downtime in staging, Datadog picks it up, PagerDuty fires the alert that the SLO is breached.

## Who should watch

Teams that have SLOs on a wiki page and nothing testing them, or teams nervous about chaos engineering because they think it starts in production. A friendly double act and a good first talk on combining the two.

## Related Conf42 talks

- Uma Mukkara on [continuous SLO validation with chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering), also at SRE 2021.
- Marco Coulter on [Goodhart's law and SLOs](https://www.conf42.com/Site_Reliability_Engineering_2021_Marco_Coulter_aviuding_Goodharts_Law_SLOs_Tools_Cudgels), also at SRE 2021.
- Julie Gunderson on [the road to reliability](https://www.conf42.com/Chaos_Engineering_2022_Julie_Gunderson_the_road_to_reliability) at Conf42 Chaos Engineering 2022.

[Watch Julie Gunderson and Mandi Walls's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Julie_Gunderson_Mandi_Walls_trauma_production_SLOs_chaos_engineeri)

## From PagerDuty

PagerDuty runs incident response and on-call alerting, the piece that pages a human when an SLO is breached in the scenario above.

- [PagerDuty website](https://www.pagerduty.com/)

[Watch the talk on YouTube](https://youtu.be/MU97UqRP5mw).

## Watch the talk

[Reducing Trauma in Production with SLOs and Chaos Engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Julie_Gunderson_Mandi_Walls_trauma_production_SLOs_chaos_engineeri) at Conf42 Site Reliability Engineering 2021.
