# Part-time SRE lost to the backlog, so bol.com went full time

Conf42 Blog, 2021-02-24. https://www.conf42.com/blog/ce2021/bol-sre-pilot-part-time-failed

In short: Bart Enkelaar (bol.com) at Conf42 Chaos Engineering 2021 on a year of SRE failures - the part-time pilot, the 45 SLIs and why buy-in needs every level

Giving five engineers 40% of their time to do SRE on the side sounds like a sensible pilot. At bol.com it mostly did not work, and [Bart Enkelaar](https://www.conf42.com/Chaos_Engineering_2021_Bart_Enkelaar_sre_failures), Lead SRE at the largest online retailer in the Netherlands and Belgium, spent his Conf42 Chaos Engineering 2021 talk running a blameless postmortem on the company's first year of SRE: what failed, what they changed, and what a large enterprise needs before SLOs change anyone's behaviour.

## How did bol.com get to SRE?

Some context first. bol.com is a retail platform where other sellers list alongside bol.com itself, with around 10 million active users, a couple of hundred thousand parcels a day, and about 600 to 700 engineers working on a microservice estate whose back end dates to around 1999.

The road to SRE was long. An agile transformation in 2009. Operations brought in house from an external partner in 2013, running a handful of big monoliths in their own data centre. A DevOps transformation around 2016 under the catchphrase "you build it, you run it, you love it". A move to the cloud from 2018, along with a reorganisation around product value chains instead of technical components. Interest in SRE had been growing since Google's books appeared, and in early 2019 the enthusiasts got a pilot.

Enkelaar's framing of why SRE was worth it: developers who ask for DevOps often just want smoother CI/CD, operations people who ask for SRE often want infrastructure as code and less toil, and management sometimes hears "fewer ops people". Following Google's line that SRE implements DevOps, bol.com set up its SRE team to build tooling and practices that help product teams balance reliability and innovation, without taking run responsibility itself.

## Failure one: SRE on the side

The pilot gave five software and operations engineers 40% of their time for SRE. It did not achieve what was hoped, and the analysis is the most quotable line of the talk. Bart Enkelaar said at Conf42 Chaos Engineering 2021: "SRE as a part time role next to full time software engineer doesn't really work so well because the pressures of backlog innovation always outcompeted our SRE work."

The investigation also found real problems around the organisation that SRE could solve, given capacity. So in 2020 bol.com formed a dedicated, full-time central SRE team with three goals: spread knowledge of DevOps and SRE practices, make product value chains observable, and sort out out-of-hours support for cloud applications.

## Failure two: the presentation that did not stick

The team ran trainings and talks, and teams left excited. A month later, with a second presentation, nothing had moved: in between, people had been doing completely different work. The uptime-versus-availability conversation had to start from scratch with every new team. The lesson: "we can't run ahead of the pack and then expect the pack to catch up." Knowledge spreads one engagement at a time, much slower than an individual learns.

## Failure three: 45 SLIs and no owner

For value chain observability they picked a deliberately small, isolated chain: the content product catalogue that manages product text and images on the shop pages. Mapping it produced 45 SLIs. They cut that to five high-level SLIs covering the chain's availability.

The catch was that six teams worked on parts of that chain, and nobody owned a chain-wide SLI. Error budget policies never really took hold; budgets were not burned and recovered the way the book describes. Enkelaar's fix is two layers: lower-level SLIs that each team owns, a clear relation from those to the product-level SLIs that product managers own, and buy-in from the top for the error budget policy.

## The takeaways

bol.com is not Google, and it does not need to copy Google's scale. SRE is a full-time, long-term investment that touches every part of how a company innovates. It needs engagement at every level of the vertical stack. And because the change is slow, celebrate the wins, or the team will run out of stamina first.

## Who should watch

Anyone pitching or rebooting SRE inside a large company, especially after a first attempt fizzled. There are no tools here, just a candid account of what did not work.

Related Conf42 talks:

- Vishnu Vardhan Chikoti on an [enterprise SRE adoption framework](https://www.conf42.com/Site_Reliability_Engineering_2021_Vishnu_Vardhan_Chikoti_enterprise_SRE_adoption_framework), Conf42 SRE 2021.
- Alayshia Knighten on [negotiating SLIs](https://www.conf42.com/Site_Reliability_Engineering_2021_Alayshia_Knighten_SLI_negociation), Conf42 SRE 2021.
- Reuben Rajan George on [why quality engineers think like SREs](https://www.conf42.com/Chaos_Engineering_2021_Reuben_Rajan_George_sre_quality_engineers), Conf42 Chaos Engineering 2021.

## From bol.com

bol.com is the online retail platform behind the story in this talk, with its own SRE team working across its product value chains.

- [bol.com](https://www.bol.com/nl/?country=BE&approved=true&language=nl-BE)

[Watch the talk on YouTube](https://youtu.be/MjGRhsBfrUo).

## Watch the talk

[One year of SRE failures](https://www.conf42.com/Chaos_Engineering_2021_Bart_Enkelaar_sre_failures) at Conf42 Chaos Engineering 2021.
