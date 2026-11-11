# Reliability keeps your job, resilience gets you promoted

Conf42 Blog, 2026-08-20, updated 2026-11-09. https://www.conf42.com/blog/remix2026/resilience-testing-belongs-in-the-sdlc

In short: Uma Mukkara of Harness, co-creator of LitmusChaos, at Conf42 Remix 2026 on resilience gates, SLIs in chaos experiments and AI risk reports.

Your provider will go down eventually; the question is whether you go down with it. At Conf42 Remix 2026, [Uma Mukkara](https://www.conf42.com/Remix_2026_Uma_Mukkara_resilience_testing_enterprise), Head of Resilience Testing at Harness and co-creator of the CNCF projects LitmusChaos and OpenEBS, made the case that SREs should treat resilience as a separate goal from reliability, test it inside the delivery pipeline, and use AI to make the business case for doing so.

Uma has spent years helping teams practise chaos engineering, and he is candid about why most don't: everyone agrees it matters, but they aren't allowed to run it. Much of this keynote is about getting that permission.

## Reliability and resilience are different goals

Uma's opening distinction: reliability is about staying available, resilience is about how you behave and how fast you come back when something pushes you over. Your cloud provider, your CDN or a security agent update can all fail on a day when your own code is fine, and no number of nines on their SLA makes that impossible.

Resilience is controlling the blast radius when that happens. Does one region go down, or all of them? Do you have the runbooks, and are people trained on them? Do you understand the dependencies well enough to recover? He also had the line of the session for anyone writing a promotion packet: "If you want to keep your job, focus on reliability. If you want to get yourself promoted, focus on resilience." When a shared provider fails and you stay up while a competitor doesn't, that difference gets noticed.

## Chaos engineering is how you find weaknesses

Uma pushes back on the idea that chaos engineering means breaking things on purpose. The goal is data about weaknesses. A known weakness is already valuable: you can prepare a recovery plan, or tell your most important customer about the risk before it bites, which he argues is often enough to keep that relationship intact.

He describes an experiment as two kinds of boxes. Fault injections are one; checks that the system is still healthy are the other. Real incidents rarely come from one fault, so good experiments chain them: a network path fails over, load shifts, a memory leak starts, and the second provider slows down at the same time.

The SRE's job is defining those health checks. Observability experts know which service level indicators matter in production, and that knowledge rarely makes it back to engineering. Hand over the SLIs and the blast radius map, and pre-production chaos tests start measuring the right things.

## Put resilience gates in the pipeline

Pipelines already gate on test coverage and regressions. Uma asks why they don't gate on resilience: is this release more or less resilient than the last one? If production experiments are off the table, push for chaos tests in staging, then low-intensity game days in production, and escalate if the answer to both is no.

He offers a maturity scale to aim at. In his view most organisations have moved from level one to level two in recent years; the target is level three, where critical services go through chaos testing in lower environments and a few game days run every year. Fully autonomous resilience, he admits, nobody does yet.

## AI writes the risk report for you

The third part is about AI, and it's where the product enters. Uma calls it passive risk detection: feed deployment, incident and service data to an LLM, for example through MCP, and ask for a resilience risk report without running a single experiment. A report that says risk has grown over the last few releases is something you can take to management.

He then describes Harness doing the same from Argo CD or Harness CD data: listing likely incidents and proposing the chaos experiments to run, generated from a prompt. Active testing then confirms what the passive scan suggested.

## Who should watch

SREs who believe in chaos engineering but can't get it approved, and engineering managers deciding where resilience fits in the SDLC. If your team already runs regular game days with SLO-based checks, the AI section is the new material. Uma also gave this keynote at Conf42 SRE 2026.

## Related Conf42 talks

- [Chaos Validation Made Easy: Plug & Play with Resilience Probes](https://www.conf42.com/Chaos_Engineering_2024_Neelanjan_Manna_Sayan_Mondal_chaos_validation_resilience_probes), the health-check half of an experiment, from the Harness chaos team.
- [Implementing Chaos Engineering in a Risk Averse Culture](https://www.conf42.com/Chaos_Engineering_2024_Kyle_Shelton_risk_averse_culture) by Kyle Shelton (Toyota), on the permission problem.
- [Enhancing Hypothesis Development Through Resilience Modeling](https://www.conf42.com/Chaos_Engineering_2024_Gunnar_Grosch_hypothesis_development_resilience_modeling) by Gunnar Grosch (AWS).

[Watch Uma Mukkara's keynote](https://www.conf42.com/Remix_2026_Uma_Mukkara_resilience_testing_enterprise).

## From Harness

Harness was the diamond sponsor of Conf42 Remix 2026. Uma leads its resilience testing product, which groups chaos, load and disaster recovery testing.

- [Harness](https://www.harness.io/)
- [Harness Resilience Testing](https://www.harness.io/products/resilience-testing)
- [Chaos engineering docs](https://developer.harness.io/docs/chaos-engineering/)

[Watch the talk on YouTube](https://youtu.be/NLcbLfj3mEA).

## Watch the talk

[Why Is Resilience Testing Non-Negotiable in an Enterprise SDLC?](https://www.conf42.com/Remix_2026_Uma_Mukkara_resilience_testing_enterprise) at Conf42 Remix 2026.
