# Your dashboards observe SLOs, chaos experiments validate them

Conf42 Blog, 2021-10-01. https://www.conf42.com/blog/sre2021/chaos-as-continuous-slo-validation

In short: Uma Mukkara (Chaos Native) at Conf42 SRE 2021 on validating SLOs continuously with scheduled chaos experiments and LitmusChaos probes.

A monitoring dashboard tells you your SLO was met yesterday and is being met now. It can't tell you whether it will survive the next dependency failure. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), Uma Mukkara, CEO of Chaos Native and co-creator and maintainer of LitmusChaos, made the case for SLO validation: keep injecting dependency faults on a randomised schedule and check, every time, that the objective still holds. It is the SRE's use of chaos engineering, as opposed to the game day or the CI pipeline.

## Why is cloud native reliability harder?

His framing: teams ship faster and run many more microservices and containers, so more changes land in the environment more often and the chance that something else fails rises, maybe 10 times, maybe 100. Your own microservice code is less than 10% of the service; the rest is other cloud native services, Kubernetes and the infrastructure underneath. Negative testing covers your app's own failure paths. Chaos testing asks what happens to your service when part of that other 90% breaks.

He is clear that this is incremental: you don't fix a system's reliability with chaos engineering in a quarter or two. Done as an engineering process, it pays back as faster fault identification, lower MTTR, better MTTF and more distance between failures.

## Observation versus validation

This is the core distinction. SLO observation answers whether the service is fine now and how it did last day, week or month. SLO validation answers the next-minute question: if something goes wrong, can I guarantee the service stays up? You get there by continuously scheduling faults against dependencies and checking the SLO each time.

The schedule matters. With tens or hundreds of chaos scenarios, you randomise what runs, so it is a surprise, but something is always running. Both outcomes are useful. "If it's not, that's also good news. You found a weakness and you're going to fix it," Uma Mukkara said at Conf42 SRE 2021.

## How does LitmusChaos model an experiment?

He calls a Litmus experiment a Lego block with two parts: the fault, declared with its duration and parameters, and the probe, the steady-state hypothesis checked before, during and after the chaos. Blocks from ChaosHub combine into a workflow, like building a Lego toy, which you schedule and which reports a resilience score. A good score means the service holds; a bad one is a fix to make.

Around that sits ChaosCenter, where developers, SREs and QA design workflows, store fault templates in a Git-backed or built-in database (MongoDB or Percona), and split roles between those who write experiments and those who view or schedule them. Targets go beyond Kubernetes to cloud platforms, bare metal and VMware. An SDK covers new experiments, and existing chaos logic can be wrapped in a Docker container. Command probes during or after the chaos can trigger remediation when the blast radius grows bigger than intended.

He cites LitmusChaos at about four years old, with 2.0 recently generally available and more than 1,000 downloads a day.

## Where should you start?

Start with a platform rather than building your own, then spend the time on identifying and designing scenarios, then automate, and move experiments that prove useful into regular QA, which is shift-left chaos testing. For the stack, he suggests the infrastructure layer first, then middleware such as Kafka, proxies and API servers, then databases and stateful apps, then the application layer.

Two more uses he highlights: checking that your observability investment actually catches a real outage by causing one on purpose, and adding chaos to performance tests.

## Who should watch

SREs who already have SLOs and dashboards and want proof they hold under failure, and teams evaluating LitmusChaos. The second half is a tour of Litmus by its maintainer, so expect the product where the talk puts it. Pair it with:

- [Uma Mukkara on continuous resilience](https://www.conf42.com/Chaos_Engineering_2023_Uma_Mukkara_continuous_resilience) at Conf42 Chaos Engineering 2023.
- [Gunnar Grosch on improving resilience with automated chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Gunnar_Grosch_resiliency_performance_automated_chaos_engineering) at Conf42 SRE 2021.
- [Akram Riahi on chaos engineering with Litmus and Jenkins](https://www.conf42.com/Chaos_Engineering_2022_Akram_Riahi_chaos_engineering_alongside_litmus_and_jenkins) at Conf42 Chaos Engineering 2022.

[Watch Uma Mukkara's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering) from Conf42 SRE 2021.

## From Chaos Native

Chaos Native provides chaos engineering for cloud native and hybrid services, built on the open source LitmusChaos project, with a hosted Chaos Native Cloud and an on-premises option.

- [Chaos Native website](https://www.chaosnative.com/)
- [Chaos Native on Conf42](https://www.conf42.com/chaosnative)

[Watch the talk on YouTube](https://youtu.be/sbR0zEDZYGY).

## Watch the talk

[Improving resilience through continuous SLO validation using chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering) at Conf42 Site Reliability Engineering 2021.
