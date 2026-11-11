# A game day without a hypothesis is just breaking things

Conf42 Blog, 2022-09-29. https://www.conf42.com/blog/im2022/game-days-need-a-hypothesis

In short: Mandi Walls (PagerDuty) at Conf42 Incident Management 2022 on running game days as deliberate incident-response practice, with goals, hypotheses and follow-up.

To get better at incident response you need practice, and practice means more incidents, which is exactly what nobody wants. At Conf42 Incident Management 2022, Mandi Walls, DevOps Advocate at PagerDuty, resolves that dilemma the way PagerDuty has for nearly a decade: game days built on chaos engineering, run with a goal, a hypothesis and a plan for what happens afterwards.

Mandi mentions her employer once, at the top, promises it's the last time she will, and keeps the promise. This is a practice talk.

## Why practise incidents on purpose?

Incident response is a muscle. Workflows, communication patterns, who goes where: none of it happens by magic, and real customer-impacting incidents are a bad place to learn, because not everyone stays calm when things are on fire.

PagerDuty calls its version Failure Fridays, written up on their blog as early as 2013, and sometimes Failure Anydays when the timing doesn't suit. The big ones happen on Fridays, and individual teams run their own during the week. The point is to check that production operations do what you need when you need it: telemetry shows up where you can read it, escalation policies and notifications fire, people know where to go, and there's a known path for pushing a fix.

## Be intentional, not random

Walking through the data centre pulling cables, or deleting a random cloud resource, might sound fun. Mandi says that's not where to start. Chaos engineering, in the Gremlin definition she quotes, compares what you think will happen with what actually happens, and it improves both the technical system and the sociotechnical one around it.

So pick targets your users feel. On tests that only exercise a part of the app nobody uses: "It's like a tree falling in the forest. It's a lot of work with little impact on the overall success of your service," Mandi Walls said at Conf42 Incident Management 2022. Focus on the components that cause the most stress when they go down. Her recurring example is the black hole test: pretend a backend dependency is offline and watch what the frontend does.

## What do you need before the first game day?

Three prerequisites:

- **Basic monitoring and telemetry**, at least enough to know your test registered. Finding gaps is part of the exercise.
- **A response process.** Assign an incident commander and a scribe, and write a post-game-day review just as you would a post-incident review. It's also a safe place for newly trained incident commanders to get reps.
- **Improvement planning.** Too many teams plan and run game days and then never feed the findings back into the work stream.

During the exercise, walk the whole incident path: does the right alert fire for the right service, do people get notified (have they even entered their contact details), where is the coordination happening, and can responders actually reach the dashboards, hosts, repositories and tools to restart or scale things? Set an end, either a fixed time or once you've learned what you came for. One PagerDuty Failure Friday she shows ran from 1:07 to 1:31 pm.

## Set a goal, write the hypothesis, record everything

Make the goal specific. Did the fix for last month's incident really fix it? Customers report the sign-up flow is slow and staging can't reproduce it. Could key systems withstand a DDoS? Then write down what you expect: a failover, a scale-up, graceful degradation, or the whole thing falling over, which is a fine baseline too.

Save the charts, graphs and command history, write the review, and share what you learned with other teams. Findings go into the backlog: better or fewer log messages, new memory or garbage collection defaults, better timeouts, feature flags for dark launches.

## When should you not run one?

Her answers to the questions customers ask most:

- **Surprise game days:** usually no. If a team can't get through planned scenarios consistently, a surprise won't make it better and can hurt how the team works together.
- **When to run one:** when the system has been stable and SLOs are safe. Don't burn the error budget on testing when you may need it for real incidents. Test new features once they have a performance baseline.
- **When not to:** right after a reorg, or at the start of your busiest season (she's looking at you, retail), and reconsider if product managers won't take the findings into the backlog.

## Who should watch

Teams starting a game day programme, or running one that has drifted into ritual. It's a well-structured checklist rather than a war story, with no metrics from PagerDuty's own programme beyond the timeline. Pair it with [Eran Levy on using chaos engineering to improve incident response](https://www.conf42.com/Incident_Management_2022_Eran_Levy_chaos_engineering_cloud_native) at the same event, [Matty Stratton on the psychology of chaos engineering](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology) at Conf42 Chaos Engineering 2020, and [Yury Nino on game days where the experiments are cyberattacks](https://www.conf42.com/Site_Reliability_Engineering_2020_Yury_Nino_security_chaos_engineering_gamedays__experiments__cybera) at Conf42 SRE 2020.

[Watch Mandi Walls's talk](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From PagerDuty

Mandi closes with PagerDuty's public incident response guide and its podcast.

- PagerDuty: [pagerduty.com](https://www.pagerduty.com/)
- [PagerDuty incident response documentation](https://response.pagerduty.com)
- [Failure Friday at PagerDuty](https://www.pagerduty.com/blog/failure-friday-at-pagerduty/)
- [Page It to the Limit podcast](https://pageittothelimit.com)

[Watch the talk on YouTube](https://youtu.be/WMwD5UHoREs).

## Watch the talk

[Plan for Unplanned Work: Game Days and Chaos Engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) at Conf42 Incident Management 2022.
