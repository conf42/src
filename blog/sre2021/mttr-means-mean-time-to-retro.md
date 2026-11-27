# The MTTR worth tracking is mean time to retro

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/mttr-means-mean-time-to-retro

In short: Robert Ross (FireHydrant) at Conf42 SRE 2021 on five pragmatic incident response tips, from retros for small incidents to clear service ownership.

Robert Ross tells you to track MTTR, waits for the incident-science crowd to object, and then admits he means mean time to retro. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), the CEO and co-founder of FireHydrant gave five incident response tips meant to be adopted this week rather than after a reorg: run retros on small incidents, hold them fast, alert on customer pain, keep responders few, and decide who owns what before the pager goes off.

## Why start with the small incidents?

His elevator, in an old candy factory in Williamsburg, Brooklyn, has buttons that don't light up, a display that says cellar when you press basement, and a race condition that sometimes sends two empty cars at once. When it finally showed an out-of-order sign, nobody was surprised. Small issues piling up become a big one, the same way an error tracker with thousands of ignored exceptions hides the one that matters.

So tip one: run retros for tiny incidents, not the biggest. A first retrospective on a giant outage tends to end with a ticket to re-architect the async pipeline, which will never happen. A minor data inconsistency in an export, with no user data lost, is low-stakes enough to practise on and produces small action items people actually do.

## What should you measure?

"The thing that I'm actually saying is meantime to retro," Robert Ross said at Conf42 SRE 2021. He cites Hermann Ebbinghaus on how fast memory fades: you can have the right people, the right process and an accurate timeline and still write a poor retrospective by waiting two weeks. A Sev 1 should clear the next day's calendar; a Sev 5 gets a few days at most.

His second metric is the ratio of retrospectives to incidents. Ten Sev 1s and two retros is a bad ratio, and moving it up is a measurable sign that behaviour is changing.

## What should page someone?

Incidents exist only because someone on the other side is in pain, so tip three is to alert on degraded customer experience and little else. A CPU at 95% or a disk at 80% at 2am, with nobody affected, is a heart beating fast during a sprint; it is designed to do that. Passing out on the pavement is the symptom worth a page. He points to SoundCloud's post on alerting on SLOs: alert on symptoms, not causes. Paging people for things nobody felt is the easiest way to lose good teammates.

## Who needs to know about the incident?

At a former employer, a payroll provider with 500 to 600 staff, a payroll outage pulled in HR, customer success, sales and engineering, and everyone wanted a seat in the channel. Tip four: focused teams mitigate best, and over-communicating causes distraction. Decide in advance whether a small team can handle it, how support and success get pushed updates without sitting in the kitchen, and when to escalate. His analogy: in some New York high-rises the fire department tells people two or more floors above a fire to stay put, because a street full of evacuees keeps the fire trucks from reaching the building.

## Who owns the service on fire?

Tip five: clear ownership, set before the outage. The team that owns the authentication service knows its dependencies and where the bodies are buried; another team may be perfectly capable but slower to get its bearings, like a fire company from northern Manhattan sent to southern Brooklyn. A service catalog with owners routes responders faster, and building one is a useful exercise in itself, because it makes you list everything you run.

## Who should watch

Teams starting or rebooting an incident process, and on-call leads fighting alert fatigue. It is short, funny and practical, and FireHydrant appears only in the closing line. Pair it with:

- [Robert Ross on the incident response process](https://www.conf42.com/Chaos_Engineering_2021_Robert_Ross_incident_response_process) at Conf42 Chaos Engineering 2021.
- [Quintessence Anx on effective incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Quintessence_Anx_dont_panic_effective_incident_response) at Conf42 SRE 2021.
- [Ajuna Kyaruzi on sustainable incident management for happy SRE teams](https://www.conf42.com/Site_Reliability_Engineering_2021_Ajuna_Kyaruzi_sustainable_incident_management_happy_SRE_teams) at Conf42 SRE 2021.

[Watch Robert Ross's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Robert_Ross_pragmatic_incident_response) from Conf42 SRE 2021.

## From FireHydrant

FireHydrant is a reliability platform for service ownership, incident management and retrospectives; Robert Ross says it grew out of the problems behind these tips.

- [FireHydrant website](https://firehydrant.io)
- [How FireHydrant works](https://firehydrant.com/how-it-works)
- [FireHydrant blog](https://firehydrant.com/blog)
- [FireHydrant on Conf42](https://www.conf42.com/firehydrant)

[Watch the talk on YouTube](https://youtu.be/T3I4g1igWOM).

## Watch the talk

[Pragmatic Incident Response: 5 lessons learned from failures](https://www.conf42.com/Site_Reliability_Engineering_2021_Robert_Ross_pragmatic_incident_response) at Conf42 Site Reliability Engineering 2021.
