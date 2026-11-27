# An 80% SLO is a feature, if it is the one your users agreed to

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/slos-stop-gold-plating-account-vending

In short: Josh Armitage (Contino) at Conf42 Site Reliability Engineering 2021 on SLOs as the lean cure for gold-plating, shown on AWS landing zone account vending

A user story says what to build, never how well. Josh Armitage, AWS Practice Lead at [Contino](https://www.contino.io/), uses his Conf42 Site Reliability Engineering 2021 talk to fill that gap with lean theory and SLOs: write the quality bar down as a measurable objective, negotiate it with the people who consume your service, and stop spending effort past it. His example is deliberately unglamorous, account vending in an AWS landing zone, to prove SLOs are worth having on systems that handle ten requests a month, not ten million.

## What waste is an SLO supposed to remove?

Armitage calls himself a lean junkie and starts with the eight wastes from the Toyota Production System: defects, overproduction, waiting, unused talent, extra processing, transportation, motion and inventory. Toyota, he says, reckons a car's value stream is about 33% value and 67% waste. The figure usually quoted for software is 1% value.

The waste he targets is extra processing, building something fantastic when good would do. The story "as a development team I want to be able to provision AWS accounts so I can deploy my application" can be met with full automation or with a person doing it by hand on Fridays. Without a quality bar nobody knows when to stop, and if you give that story to ten engineers you get ten different systems.

## Who decides what good enough means?

Product management, he says, is tension management, and SLOs work on the tension between the delivery team and its many consumers. The quick vocabulary: the SLI defines success and failure, the SLO how often you may fail (never zero), the SLA the penalty for failing too often.

The common anti-pattern is an SLA on paper with no SLI behind it, such as 99.9% for on-premises network traffic with no definition of a failed packet. He calls that Schrödinger's SLA. Josh Armitage said at Conf42 Site Reliability Engineering 2021: "if you can't measure your slA, you don't know whether your system's alive or dead."

## How do you negotiate the number?

The account vending negotiation is the best part. Consumers ask for an account within five minutes, which on AWS means weeks or months of effort. The team counters with a week, a weekly manual task, which leaves consumers stuck waiting. They settle on one business day, which needs some automation and, in his words, is 100 times slower than what the consumer wanted and five times faster than the first offer.

Then he applies SMART goals, and attainable is where the nines come off. At 99%, allowing two failed accounts a month means vending 200 accounts a month, which no business does. At a realistic ten accounts a month with the same two failures allowed, the SLO lands at 80%: account vending within one business day, 80% of the time, over a rolling 30-day window. His rule of thumb is that every extra nine costs ten times the investment, team capacity is limited, so negotiate the minimum SLO you can.

## What does the error budget tell you to do next?

He shows a dashboard built for a client from Amazon EventBridge, CloudWatch, Managed Grafana and QuickSight, and reads decisions off it:

| Capability | Actual | SLO | Decision |
|---|---|---|---|
| Account vending | 95% | 80% | 15% budget: refactor, add features, or leave it alone |
| Access provisioning | 82% | 80% | 2% budget: pay down debt, no new features |
| IaC compliance scans | 63% | 95% | -32%: invest in stability or renegotiate the SLO |

He also warns about inflating expectations. Run at 95% against an 80% SLO for six months and consumers start expecting 95%, so spend the budget and remind people that systems fail. Review the numbers in every sprint review so the dashboard drives priorities instead of gathering dust. His sample table of landing zone SLOs includes user credentials within four business hours at 90%, egress to the public internet within 50 ms at 99.5%, and a full compliance scan in under five minutes at 95%. He expects you to disagree with some of them, which is the point of writing them down.

Josh Armitage said at Conf42 Site Reliability Engineering 2021: "Slos are not only for the googles of the world, they're for everyone."

## Who should watch

Platform and cloud teams with internal customers, product owners writing stories for infrastructure, and anyone told SLOs only matter at Google scale. There is a small GitHub repo, tf2eventbridge, that wires account events through to a Grafana dashboard if you want to try it.

## Related Conf42 talks

- Alayshia Knighten on [SLI negotiation](https://www.conf42.com/Site_Reliability_Engineering_2021_Alayshia_Knighten_SLI_negociation), also at SRE 2021.
- Joe Blubaugh on [not getting out of bed for anything less than an SLO](https://www.conf42.com/DevOps_2023_Joe_Blubaugh_bed_less_slo) at Conf42 DevOps 2023.
- Josh Armitage on [red teaming AWS](https://www.conf42.com/DevSecOps_2022_Josh_Armitage_red_teaming_aws_practice_preach) at Conf42 DevSecOps 2022.

[Watch Josh Armitage's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Josh_Armitage_lean_product_development_SLOs)

## From Contino

Contino is a global digital transformation consultancy working on cloud, DevOps and agile transformations with enterprises.

- [Contino website](https://www.contino.io/)

[Watch the talk on YouTube](https://youtu.be/R_Uz5nkigdQ).

## Watch the talk

[Lean Product Development Through SLOs](https://www.conf42.com/Site_Reliability_Engineering_2021_Josh_Armitage_lean_product_development_SLOs) at Conf42 Site Reliability Engineering 2021.
