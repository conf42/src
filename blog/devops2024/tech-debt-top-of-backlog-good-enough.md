# Put tech debt at the top of every sprint, and stop over-analysing the rest

Conf42 Blog, 2024-01-26. https://www.conf42.com/blog/devops2024/tech-debt-top-of-backlog-good-enough

In short: Ewald Verhoeven (TestCoders) at Conf42 DevOps 2024 on why teams slow down, paying tech debt every sprint, and scoring decisions with AHP and Pugh

If you have ever held a dedicated bug sprint, or cancelled a retro to finish work that was almost done, this one is about your team. At Conf42 DevOps 2024, [Ewald Verhoeven](https://www.conf42.com/DevOps_2024_Ewald_Verhoeven_software_delivery_team), Quality Advocate Lead at TestCoders, argued that teams slow down for the same three reasons everywhere (bugs, legacy and technical debt) and offered two fixes: pay down tech debt first thing every sprint, and make big decisions with a scoring matrix instead of gut feeling.

It is a process talk from a test automation consultant, with examples from client teams and a personal closing story.

## What does a slowing team look like?

His symptoms: bug sprints, backlog items older than twelve months, cards piling up in the testing column, cancelled retros, product owners doing the testing. Such teams typically finish less than 90% of what they planned.

His definitions are pragmatic. A bug is something that was delivered, tested and worked, and now doesn't. Legacy has no crisp definition, but the signals are clear: the system outlives the team or the tech stack, people are afraid to touch it (some won't even clone the repo), and there are no tests, which means no way to learn what it is supposed to do.

## How should a team treat technical debt?

He uses the deliberate/accidental, prudent/reckless quadrant. Deliberate and prudent is fine: you know you are taking on debt and plan to pay it back. Deliberate and reckless means no plan at all. Accidental and prudent means you find out later and fix how you work. The one to avoid is finding out and ignoring it.

The money analogy makes the point stick. A €6,000 trip, €2,400 saved at €200 a month, and €3,600 borrowed to repay within a year leaves you €1,200 short, or €100 a month you have to find somewhere: rent, insurance, utilities, the car or food. Skip that planning and the debt decides for you; in software, that means more bugs and dirty fixes left in production.

His rule is blunt. Ewald Verhoeven said at Conf42 DevOps 2024: "You put technical debt on the top of your backlog every sprint, and you finish it first."

His example of the vicious cycle comes from test automation. A flaky end-to-end test blocks the pipeline, someone disables it to get the build green, coverage drops, bugs follow, a hotfix ships, nobody re-enables the test, and the loop starts again.

## Why are DevOps teams better at it?

In his experience, real DevOps teams with developers and operations engineers working together handle tech debt better because everyone feels the pain across the whole lifecycle, not just in their own phase. The first way of DevOps is flow, small changes moving from dev to ops without waiting, and that needs automation everywhere: tests, CI, deployment and release.

You don't need a DevOps team to start. His suggestion is to look at your definition of done. It lists the chores nobody likes (release notes, manual tests, quality gates, peer reviews), a ready-made automation backlog.

## How do you make a team decision without a week of opinions?

The second slowdown is decision making. DevOps favours data over gut feeling, but every decision is emotional underneath, so the trick is to quantify it. He uses two complementary tools, walked through with a real case: a team choosing a contract testing tool.

- **AHP matrix** (Analytic Hierarchy Process): list the criteria (pricing, collaboration and source control, OpenAPI 3.0 support, learning curve, a mock server, future GraphQL support) and compare them in pairs only, scoring how much more important one is with Fibonacci numbers (1, 2, 3, 5, 8). The output is a weight per criterion. That team ranked collaboration and source control and OpenAPI 3.0 highest.
- **Pugh matrix**: take the weights, pick one candidate as the baseline (here Pact), and score the others against it per criterion from -2 to +2. Postman and PactFlow were the alternatives; the numbers in his demo were made up on the spot to show the mechanics.

The argument stops being about who liked which tool at a previous job and becomes about the criteria this team agreed on.

## Why is good enough good enough?

His last point is the one he asked people to remember: Ewald Verhoeven said at Conf42 DevOps 2024, "So please make informed decisions, but stop overanalyzing. Good is good enough."

He learned it the hard way. About ten years before the talk, while serving in the Royal Netherlands Army, he was attacked by a man with a knife outside his home. He survived with minor injuries and was treated for PTSD, but the case was never solved and none of the facts made sense, and he kept analysing it. What helped was accepting that no new facts were coming, and moving on.

## Who should watch?

Scrum teams with a growing backlog of old items, team leads tired of tool debates, and test automation engineers who have watched a disabled test turn into a bug farm.

## Related Conf42 talks

- Giulio Vian on [whether technical debt is the right metaphor for continuous update](https://www.conf42.com/DevSecOps_2022_Giulio_Vian_technical_debt_right_metaphor_continuous_update) at Conf42 DevSecOps 2022.
- Dmitry Vinnik on [broken windows in legacy systems](https://www.conf42.com/Site_Reliability_Engineering_2021_Dmitry_Vinnik_broken_windows_legacy_systems__poor_quality_gaps) at Conf42 SRE 2021.
- Gil Zilberfeld on [TDD with legacy code](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code) at Conf42 Python 2022.

[Watch Ewald Verhoeven's talk](https://www.conf42.com/DevOps_2024_Ewald_Verhoeven_software_delivery_team), part of [Conf42 DevOps 2024](https://www.conf42.com/devops2024).

## From TestCoders

TestCoders is a Dutch test automation and software quality consultancy.

- [TestCoders website](https://testcoders.nl/)

[Watch the talk on YouTube](https://youtu.be/3AJMzuHgGB0).

## Watch the talk

[Accelerating Software Delivery: Why Your Team is Slowing Down](https://www.conf42.com/DevOps_2024_Ewald_Verhoeven_software_delivery_team) at Conf42 DevOps 2024.
