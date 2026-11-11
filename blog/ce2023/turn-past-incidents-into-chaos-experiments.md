# Turn last quarter's incidents into this sprint's chaos experiments

Conf42 Blog, 2023-02-15. https://www.conf42.com/blog/ce2023/turn-past-incidents-into-chaos-experiments

In short: Benjamin Wilms (Steadybit) at Conf42 Chaos Engineering 2023 on turning past failures into pre-production chaos experiments that run after every deploy

Your monitoring already knows which failures will hit you next, because it recorded them last time. At Conf42 Chaos Engineering 2023, [Benjamin Wilms](https://www.conf42.com/Chaos_Engineering_2023_Benjamin_Wilms_reliability_uncertainty), Co-Founder and CEO of Steadybit, argues that past incidents are the best source of chaos experiments: recreate them in pre-production on top of your existing load tests, define the behaviour you expect, and run the whole set after every deployment.

It is a vendor talk, and the experiments in the demo are built in Steadybit, but the method is tool-neutral and the two worked examples are the useful part.

## Why is reliability so hard to deliver?

He defines reliable as consistently good in quality and performance, from the end user's point of view. Customers who get an answer in reasonable time come back; customers who get errors or long waits move on to another vendor.

Meanwhile the systems keep getting harder. Microservice dependency graphs, rolling updates under load, autoscaling instances that must also be cleaned up (or "your cloud provider is getting happy but not you"), with Kubernetes, cloud providers and third-party auth underneath. He quotes Richard Cook: it is not surprising that your system sometimes fails, what is surprising is that it ever works at all.

The numbers come from a FireHydrant report on 53,034 incidents resolved on its platform between 2019 and 2022: even small organisations deal with around ten incidents a month, the count climbs with company size, and the average incident takes 24 hours and 5 minutes from open to close.

## Failures are your system asking for help

His framing is that failures are normal and that each one carries information. He goes further: a failure is the system trying to get in touch with you, pointing at the spot that needs fixing. That makes failures the foundation of experiments. Before production you should already know the answers to questions like: can users keep shopping during a rolling update, will a service start when its dependencies are unreachable, can customers still buy during a cloud zone outage?

"We need to test under real conditions, early as possible," Benjamin Wilms said at Conf42 Chaos Engineering 2023. Happy-path testing is not enough, because production is not a happy place.

## Experiment one: a slow inventory service

The demo is a Kubernetes shop: a load balancer in front of two gateway instances, which call hot deals, fashion and toys services, all depending on one inventory service. That makes inventory a key service, the one whose slowness spreads.

Monitoring and load tests say inventory normally answers in about 25 ms, with historical spikes up to 500 ms. So the experiment injects up to 500 ms of latency while an existing load test runs, with verification steps checking that instances are up and endpoints respond, plus an explicit expected-behaviour check that fails the experiment if the system misbehaves. This one passed: the system handled short-term slow responses from inventory, which is now a known fact rather than a hope.

## Experiment two: the incident that hurt

The second scenario comes straight from a past failure that hit hard: the hot deals service delayed in two cloud zones, followed by a DNS outage inside the Kubernetes cluster. The experiment replays exactly that, zone-limited latency for hot deals then no DNS in the cluster, with a check that an endpoint keeps returning HTTP 200 at a 100% success rate. It failed, mostly red. The system could not survive its own history, and customers would have been locked out again. Now the team knows where to work, before the next occurrence instead of during it.

## When should these experiments run?

The same answer the industry reached for unit and integration tests: as part of the development process, not as an occasional game day. He treats experiments as end-to-end integration tests built from production conditions. The list grows with every incident, and a GitHub Action or API call runs it after each pre-production deployment. Ten experiments, five pass, five fail: now you know the risk before you ship.

## Who should watch

Teams that have load tests and postmortems but have never connected the two, and anyone looking for a concrete first chaos experiment rather than a philosophy. It is a short talk with two clear demos.

Related Conf42 talks:

- Benjamin Wilms on [reliable systems in an unpredictable world](https://www.conf42.com/Chaos_Engineering_2025_Benjamin_Wilms_reliable_system_unpredictable), Conf42 Chaos Engineering 2025.
- Uma Mukkara on [continuous resilience](https://www.conf42.com/Chaos_Engineering_2023_Uma_Mukkara_continuous_resilience) at the same event.
- Saranya Jena and Sarthak Jain on [resilience in CD pipelines](https://www.conf42.com/Chaos_Engineering_2024_Saranya_Jena_Sarthak_Jain_embracing_resilience_power_cd_pipelines), Conf42 Chaos Engineering 2024.

## From Steadybit

Steadybit builds the chaos engineering platform used to design and run the experiments in the demo, including triggering them from a GitHub Action after a deployment.

- [Steadybit](https://steadybit.com/)

[Watch the talk on YouTube](https://youtu.be/mdwAMxxKKRA).

## Watch the talk

[Reliability in the Face of Uncertainty](https://www.conf42.com/Chaos_Engineering_2023_Benjamin_Wilms_reliability_uncertainty) at Conf42 Chaos Engineering 2023.
