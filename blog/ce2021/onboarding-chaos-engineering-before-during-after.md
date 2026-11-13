# Chaos engineering needs a microscope and a scalpel, not a hammer

Conf42 Blog, 2021-02-26. https://www.conf42.com/blog/ce2021/onboarding-chaos-engineering-before-during-after

In short: Karolina Rachwał (Nuaware) at Conf42 Chaos Engineering 2021 on onboarding chaos engineering - the business case, build vs buy, first experiments, game days

Getting a budget approved for something called chaos engineering is the easy part. At Conf42 Chaos Engineering 2021, [Karolina Rachwał](https://www.conf42.com/Chaos_Engineering_2021_Karolina_Rachwa_onboarding_chaos_engineering), Chaos Engineering Practice Lead at Nuaware, compressed a year of near-daily conversations with teams adopting the practice into a before, during and after guide: why you will benefit, what you need in place first, how to run the first experiments, and where to go once they work.

Nuaware is a software distributor specialising in cloud native technologies and in bringing newer vendors into the European market, which explains the vantage point: Rachwał hears the same questions from many organisations.

## Is it too early for us?

The definition she uses is a scientific method to uncover failures before they happen, covering processes and people as well as applications, infrastructure and network. Her analogy is a vaccine: a controlled dose of a pathogen to build immunity.

The business case starts with money. Rachwał puts the average cost of downtime at around $100,000 an hour, which is why it has become a KPI for many engineering teams. If profitability depends on your systems, you will benefit.

The common objection is legacy: why do chaos on bare metal? Her answer has three parts. Downtime hurts customer-facing apps on old systems as much as on Kubernetes. Almost no IT department has nothing outsourced, and you still need to know what happens when a third party goes down. And the migration to cloud or containers is coming, so teams that learn the practice early will migrate more smoothly.

## What do you need before the first experiment?

Monitoring and observability. Karolina Rachwał said at Conf42 Chaos Engineering 2021: "Would you do that with a blindfold and a hammer, or a microscope and a scalpel?" Without data you understand neither the steady state nor how the system behaves under stress.

Baseline metrics are resource consumption, state and performance, plus high visibility of SLOs, SLIs and SLAs. To track how chaos engineering improves incident response, measure mean time to detect, mean time to recovery and mean time between failures.

## Build or buy?

Building in house gives exact fit with your stack, monitoring and pipelines, keeps connections inside your network, can shorten feedback loops, and puts the roadmap under your control. The biggest argument for buying, she notes, is cost: chaos specialists are rare and expensive, and she estimates that a sophisticated fault injection platform takes 14 to 18 months of several engineers to build and maintain. Bought tools tend to support more stacks and infrastructure types and come with automation, which home-built ones usually lack at first.

## The first experiments

Do not start in production. Pick a small, precisely defined part of the system, preferably in dev or test. State a hypothesis, design an experiment with a magnitude far smaller than you think could cause trouble, examine the monitoring afterwards, fix what you found, and rerun to confirm the fix.

Do not be discouraged when nothing breaks: "The knowledge that our systems will withstand a particular failure is just as valuable as discovering an issue and fixing it." Increase the magnitude, change the failure type, or repeat the experiment elsewhere.

## After onboarding

Game days are the next step: a dedicated day for a team to attack a preselected part of the system and fix findings immediately. Later come automated chaos tests in CI/CD, champions per department or a centre of excellence. Her list of uses includes replicating common Kubernetes failures, rehearsing disaster recovery playbooks, verifying monitoring so alerts are not missed, comparing monitoring tools before buying one, validating cloud migrations, training new engineers and checking dependency failures degrade gracefully.

## Who should watch

Teams at the start of the journey and the managers deciding whether to fund it. It is a high-level guide, honest about trade-offs, without a product demo.

Related Conf42 talks:

- Mikolaj Pawlikowski on [chaos engineering in 2021](https://www.conf42.com/Chaos_Engineering_2021_Mikolaj_Pawlikowski_chaos_engineering_2021) at the same event.
- Ana Margarita Medina on [learning through fire and chaos](https://www.conf42.com/Chaos_Engineering_2021_Ana_Margarita_Medina_fire_chaos), Conf42 Chaos Engineering 2021.
- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering), Conf42 Incident Management 2022.

## From Nuaware

Nuaware distributes cloud native software and partners with vendors entering the European market, which is where Rachwał's view across many adopting teams comes from.

- [Nuaware](https://www.nuaware.com)

[Watch the talk on YouTube](https://youtu.be/Dxt1SjUtCDk).

## Watch the talk

[Onboarding Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2021_Karolina_Rachwa_onboarding_chaos_engineering) at Conf42 Chaos Engineering 2021.
