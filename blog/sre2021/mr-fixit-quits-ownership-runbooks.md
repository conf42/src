# When Mr. Fixit quits, ownership and runbooks are all you have

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/mr-fixit-quits-ownership-runbooks

In short: Cristina Buenahora Bustamante (Cortex) at Conf42 SRE 2021 on spreading the SRE mindset through ownership, runbooks, blameless retros and tech debt as debt.

Every team has a Mr. Fixit, the engineer everyone calls at 3am because nobody else knows the service. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), Cristina Buenahora Bustamante, founding engineer at Cortex, argued that a culture of reliability rests on three unglamorous things: clear ownership of every service, documentation and runbooks someone keeps current, and retros that are routine rather than a hunt for culprits. Her case for it is a single on-call night told twice.

## What is an SRE supposed to be now?

She compares how SREs and engineers describe the role. Both stress efficiency, scalability and reliability, but the engineer's version is broader: daily help with technical problems, tools and metrics, and SRE as a conduit between engineering teams and management. That, she says, is the change. The SRE as the resident Kubernetes or AWS expert is over; SREs at leading companies are expected to level up how the whole engineering organisation works.

## Who are your systems for?

Her first job, at the hedge fund Bridgewater Associates, built portfolio analytics used for decisions affecting pension funds for teachers and firefighters and sovereign wealth funds. The team ran to four nines, which she puts at 53 minutes of downtime a year, and her first production outage felt like letting down the team, the analysts and the clients at once. One analyst described a slow app as being sent into war without a sword.

What made it survivable was how incidents were handled. After the dust settled, the team pulled up the offending code and asked who wrote it, how it was tested, who reviewed it, why staging didn't catch it and who ran the release checklist, without pointing fingers. Knowing that in advance gave her, as a junior engineer, room to grow without being let off the hook. Her checklist for any team: do engineers know why the app matters, are uptime expectations explicit, and does the person who joined six months ago know how incidents are handled as well as someone who has been there two years?

## One night, told twice

The bad version: paged at 3am about a service you have never heard of, no docs, no runbook, no owner to be found. At 3:45 you call Mr. Fixit, who suggests a restart because it worked for something similar. Nobody at the 10am standup knows it happened, there is no retro, and a month later it breaks again. "He quit to go work at a company that actually cares about reliability," Cristina Buenahora Bustamante said at Conf42 SRE 2021.

The good version: the alert names a service you can find, with documentation, logs and a runbook. You restart it yourself, without calling anyone, monitor for 15 minutes and go back to sleep. At 10am the owning team prioritises a real fix.

## How do you apply it to the delivery machine?

Ownership comes first: if it is unclear who is responsible for what, you have no chance. Each owner keeps documentation and runbooks current and dependencies defined. SREs should go toe to toe with product managers so the work behind a robust delivery system is prioritised like features, not pushed down the backlog. And retros should become as much of a non-event as prioritising Jira tickets.

## How do you sell tech debt to a non-technical leader?

Call it debt. She cites Stripe's 2018 survey on engineering efficiency and its $3 trillion impact on global GDP: the average developer spends more than 17 hours a week on maintenance, 13 on tech debt and 4 on bad code. Those 4 hours are 9.25% of a 40-hour week, which she equates to $85 billion a year. Debt is something every leader understands, and eventually the collector calls.

Her three repayment options: pay it down steadily (10% of each sprint, or one tech-debt ticket per engineer), dedicate a team or a sprint each quarter to it, or go bankrupt through breaches, downtime and degraded performance. She prefers the first; nobody wants to sit on a tech-debt-only team, the team that created the debt should fix it, and some critical team always gets exempted from a debt sprint.

## Who should watch

Engineering managers and SREs trying to make reliability everyone's job, especially with a growing on-call rotation. The Cortex part is a short pitch at the end, where she names ownership, service documentation and dependency mapping as what the product is built to do. Pair it with:

- [Joey Parsons on service ownership and organisational chaos](https://www.conf42.com/Chaos_Engineering_2021_Joey_Parsons_service_ownership_organizational_chaos) at Conf42 Chaos Engineering 2021.
- [Giulio Vian on the right metaphor for technical debt](https://www.conf42.com/DevSecOps_2022_Giulio_Vian_technical_debt_right_metaphor_continuous_update) at Conf42 DevSecOps 2022.
- [Mandi Walls on automation and toil](https://www.conf42.com/Site_Reliability_Engineering_2021_Mandi_Walls_automation_toil) at Conf42 SRE 2021.

[Watch Cristina Buenahora Bustamante's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Cristina_Buenahora_Bustamante_evangelizing_culture_ownership) from Conf42 SRE 2021.

## From Cortex

Cortex builds a tool to help teams manage their services and define best practices across the organisation, including service ownership and scorecards.

- [Cortex website](https://www.cortex.io/)
- [Cortex scorecards](https://www.cortex.io/products/scorecard/?utm_source=conf42)
- [How to improve your influence as an SRE](https://www.cortex.io/post/4-ways-to-improve-your-influence-as-an-sre/?utm_source=conf42)
- [Cortex on Conf42](https://www.conf42.com/cortex)

[Watch the talk on YouTube](https://youtu.be/S-JZL1j-X2c).

## Watch the talk

[Evangelizing the SRE mindset: Building a culture of reliability and ownership](https://www.conf42.com/Site_Reliability_Engineering_2021_Cristina_Buenahora_Bustamante_evangelizing_culture_ownership) at Conf42 Site Reliability Engineering 2021.
