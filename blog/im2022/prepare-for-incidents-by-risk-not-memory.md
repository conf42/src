# Prepare for the incidents your risk table predicts, not the last page

Conf42 Blog, 2022-09-28. https://www.conf42.com/blog/im2022/prepare-for-incidents-by-risk-not-memory

In short: Jeff Nickoloff (Gremlin) at Conf42 Incident Management 2022 on picking which failures to prepare for by probability times severity, scored consistently.

Most teams prepare for whatever paged them last. At Conf42 Incident Management 2022, Jeff Nickoloff, Principal Engineer in the Office of the CTO at Gremlin, with 20 years on critical systems at places like Amazon, Venmo and PayPal, argues for a better selection method: run a reliability program that ranks failure modes by probability times severity, and let that ranking decide what your incident preparation pays for.

It's a short talk from the sponsor, with a product mention at the end and a useful frame in the middle.

## What is scrambling in the dark?

Jeff's starting point isn't the incident with the biggest customer impact. It's the one where nobody knows what's going on: miscommunication, just-in-time research, technicians "trading dashboards like trading cards." Those are the incidents that create a crisis of confidence, when people start asking whether they can rely on their systems at all.

The answer, he says, is preparation, and he refuses to make it sound cheap. The effort grows with the number of components, people, teams, dependencies and ways the system touches customers, and that's a hard story to tell when you're asking for budget.

## Automation or autopilot?

He splits preparation spending into two buckets.

- **Automation.** Continuous monitoring and automated recovery: release and rollback control, Kubernetes reconciling a failed process back to its desired state. Powerful, but tool- and stack-dependent, and expensive to build, maintain and keep improving.
- **Autopilot.** The human side: consistent skills, context and problem-solving workflows across responders, and a fairly deterministic set of remediation options. Without it, readiness varies by who's on call, who knows the recent changes, and who knows which dashboard or non-alarming monitor matters. The fix is awareness, training and reps, seeing failures before they show up in an incident.

You'll fund both. The harder question is which failures each should cover, because preparing for everything is a long tail nobody catches.

## How should you pick what to prepare for?

The naive answer is familiarity: people lean towards the failures they know or the last one they were paged for. Jeff's alternative is to connect two efforts that usually live apart. The reliability program proactively enumerates components, failure modes, dependencies and the value of each system, and tests what conditions each component survives. Incident management feeds back what actually happened: how long recovery took and what the last few occurrences cost.

The core tool he points to is failure mode and effects analysis (FMEA): a catalogue of components, each one's failure modes, their probability, their severity (ideally in money, because money tells the best funding story), and whether you can detect them. "It's rare that I've seen it implemented in SaaS and software space in a deep way," Jeff Nickoloff said at Conf42 Incident Management 2022, but even high-level inspiration from it helps. The output can be a big spreadsheet.

## Can you detect it before your customers do?

Detection gets its own section because it maps straight onto incident readiness. If you can't detect a failure mode, response time will be poor and responders will struggle to identify what failed. Jeff won't say detective controls for everything; decide per failure mode whether it warrants the investment. And test those controls regularly by creating the failure conditions, not once.

## Risk is probability times severity, measured the same way everywhere

Prioritisation then becomes arithmetic. A very expensive failure that is extremely unlikely can rank below a mild one that happens three or four times a day. Getting the probability right needs experiments; getting the severity right needs the business: volumes, revenue per interaction, contract penalties.

His sharpest point is about consistency. If ten groups score risk ten different ways, you're comparing apples to oranges and can't prioritise across the organisation. The specific scoring method matters less than everyone using the same one.

## Who should watch

Engineering leaders building a case for reliability or readiness budget, and SREs who suspect their game days are aimed at last quarter's outage. It's a framework talk with no numbers from a real FMEA, so treat it as a starting structure. Pair it with [Mandi Walls on game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) at the same event, [Kyle Shelton on disaster recovery preparedness](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) at Conf42 Chaos Engineering 2022, and [Kyle Shelton on chaos engineering in a risk-averse culture](https://www.conf42.com/Chaos_Engineering_2024_Kyle_Shelton_risk_averse_culture) at Conf42 Chaos Engineering 2024.

[Watch Jeff Nickoloff's talk](https://www.conf42.com/Incident_Management_2022_Jeff_Nickoloff_reliability_management) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From Gremlin

Jeff closes with Gremlin's then-new Reliability Management product, built around the consistency point: Gremlin regularly tests services for redundancy, scalability and surviving dependency issues and combines the results into one score per service, so teams can compare services and see which conditions each can and can't tolerate.

- Gremlin: [gremlin.com](https://www.gremlin.com)

[Watch the talk on YouTube](https://youtu.be/Q046xX-dagI).

## Watch the talk

[Get Ready to Recover with Reliability Management](https://www.conf42.com/Incident_Management_2022_Jeff_Nickoloff_reliability_management) at Conf42 Incident Management 2022.
