# It took 30 seconds to learn the on-call could not update the status page

Conf42 Blog, 2021-02-26. https://www.conf42.com/blog/ce2021/chaos-test-your-incident-process

In short: Robert Ross (FireHydrant) at Conf42 Chaos Engineering 2021 on chaos experiments for incident response - break things, watch people fix them, drill the techniques

Robert Ross once pulled his co-founder into a room and asked him to update the status page for a pretend sev-1. About 30 seconds later they knew the on-call engineer could not: only Ross had the Statuspage credentials. At Conf42 Chaos Engineering 2021, [Robert Ross](https://www.conf42.com/Chaos_Engineering_2021_Robert_Ross_incident_response_process), CEO and co-founder of FireHydrant, argued that you should run chaos experiments on your incident process the way you run them on your systems, and that what you are really testing is people's techniques, not the runbook.

## From technical to process experiments

He starts with the textbook definition from principlesofchaos.org, the flu shot and controlled burn analogies, and a few classic technical experiments: latency on a Postgres instance that makes app server requests queue until the site topples over, blackholing Redis so caching breaks but the site limps on, killing processes so requests are half fulfilled and data is left inconsistent.

Process experiments work the same way with more possible outcomes, because people solve problems differently. One engineer finds logs by one route, another by a different one. One rolls back by reverting a merge, another through Spinnaker. The status page drill is the simplest version: a surprise meeting, one common incident task, and a stopwatch. Publicly disclosing incidents fast was part of FireHydrant's SLA, so the gap mattered.

## People mitigate incidents, not process

Robert Ross said at Conf42 Chaos Engineering 2021: "Because the reality is that people mitigate incidents, not process."

Heavy process, such as manually creating the Jira ticket, the Slack room and the status page update, can slow mitigation down; automating that overhead is what FireHydrant sells, and Ross says so and moves on. The other failure is prescription: a runbook that says the only way to fix storage errors is to add storage, when the error might be a mislabelled red herring.

His alternative is technique bricks. Think of each technique as a Lego brick: find logs, SSH into a box, purge a cache, roll back a bad deploy. None was designed for a stale-cache incident, but someone who knows each brick can assemble them into a fix quickly. Someone who only knows how to build one complete set, one spaceship front to back, is stuck when a different incident arrives.

## The boring part is the point

Bricks are boring to practise, which is why nobody does. Ross, who marched in Drum Corps International, as did his co-founder, describes three-hour rehearsals spent marching eight steps forward with horns up, over and over. Mastering that is what let the corps make shapes on the field.

## How to run it

Two formats from the talk:

- **The secret agent.** At Namely, where Ross worked as an SRE, a small group secretly decided how and when someone would break staging. The responding team only knew to be at their computers at a given time, with no hints. Then everyone watched how they found and fixed it. You will find missing permissions, missing runbooks, capabilities the system lacks, and things that cannot be rolled back.
- **The single-technique drill.** Mine your retrospectives for the techniques people used and break them down to the smallest pieces. Then roll out a benign change, in production because staging is rarely the same, get a newer teammate on a recorded Zoom call sharing their screen, and ask them to roll it back. Do the same for finding all logs for 500 status codes, so nobody learns query syntax during an incident.

You may discover that someone has a faster method nobody else knew, and then it becomes the team's technique. Write the techniques down in Notion, Confluence or wherever you keep knowledge, and practise them regularly, because logging systems and metric labels will change underneath you. His estimate of the cost: "This will take you an hour to do with a small team."

The abstract promises stress tests of three parts of the process: declaring an incident, communicating it, and escalating to stakeholders. The recording covers the status page drill and then focuses on response techniques rather than walking through all three.

## Who should watch

On-call leads and incident commanders who have a process document and suspect nobody could follow it at 3am. Quick, practical, with good stories.

Related Conf42 talks:

- Julie Gunderson on [postmortems and blameless culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at the same event.
- Paul Marsicovetere on [optimizing incident response](https://www.conf42.com/Chaos_Engineering_2022_Paul_Marsicovetere_optimizing_incident_response), Conf42 Chaos Engineering 2022.
- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering), Conf42 Incident Management 2022.

## From FireHydrant

FireHydrant is an incident management platform that automates the process around a response: service catalogues, incident channels, status pages and retrospectives.

- [FireHydrant](https://firehydrant.io)
- [How FireHydrant works](https://firehydrant.com/how-it-works)
- [FireHydrant demo](https://firehydrant.com/demo)
- [FireHydrant blog](https://firehydrant.com/blog)

[Watch the talk on YouTube](https://youtu.be/GohmewqmwqM).

## Watch the talk

[Incident Ready: How to Chaos Engineer Your Incident Response Process](https://www.conf42.com/Chaos_Engineering_2021_Robert_Ross_incident_response_process) at Conf42 Chaos Engineering 2021.
