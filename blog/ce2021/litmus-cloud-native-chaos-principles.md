# Cloud native chaos needs GitOps, a hub and Prometheus, says Litmus

Conf42 Blog, 2021-02-24. https://www.conf42.com/blog/ce2021/litmus-cloud-native-chaos-principles

In short: Uma Mukkara (Chaos Native) at Conf42 Chaos Engineering 2021 on five principles for cloud native chaos and how Litmus turns them into Argo workflows

If your microservices change every week and your developers provision infrastructure through APIs, the yearly game day is not going to keep up. That is the argument [Uma Mukkara](https://www.conf42.com/Chaos_Engineering_2021_Uma_Mukkara_cloud_native_at_scale), CEO of Chaos Native and a maintainer of the CNCF sandbox project Litmus, made at Conf42 Chaos Engineering 2021: chaos engineering in a cloud native shop has to be declarative, versioned, shared and wired into the same GitOps machinery as everything else.

It is a vendor talk in the honest sense. Chaos Native had just been spun off from MayaData to work on Litmus full time, and the second half of the talk is a tour of the project. The abstract promises a live demo of a node failure, a CPU hog and network slowness in an e-commerce app; the recording is a slide walkthrough of the architecture instead, with no demo.

## Why does cloud native need a different kind of chaos?

Mukkara's definition is refreshingly blunt. Uma Mukkara said at Conf42 Chaos Engineering 2021: "cloud native is nothing but microservices are being delivered faster."

He sees two forces. The first is dynamism: monoliths that shipped every 90 or 180 days became dozens of services, and in a large system something changes at least once a week. The second is that infrastructure provisioning went fully declarative, so developers now change the ground their services run on, often. Faults tend to live in that infrastructure, which means more change underneath and more change on top.

Traditional chaos engineering, in his telling, was a practice for experts at large companies, usually started after a painful outage, run as rare game days with manual scripts and no standard way to measure results. That does not scale to weekly change.

## The five principles

Mukkara lists the principles he had been writing about on his blog, plus a fifth he added recently:

- **Open source.** The chaos stack should be built and reviewed in the open, like Kubernetes itself.
- **Community-collaborated experiments.** He expects common chaos experiments to become a commodity, so they should be shared and hosted rather than rewritten by every team, and vetted so they do not raise false alarms.
- **Chaos managed at scale.** Experiments need versioning, a lifecycle and an open API.
- **GitOps.** The whole setup should be declarative and driven by tools such as Argo CD, Flux or Spinnaker.
- **Open observability.** When you inject a fault you need to tell whether a change in behaviour came from your fault or from something that happened at the same time.

## How Litmus maps onto them

Litmus installs from a Helm chart. The Litmus Portal is the central place where experiments are pulled from a public ChaosHub or a team's private hub, and where workflows are launched against any number of targets, cloud or on-prem. The point is in one line: "You install Litmus once per your enterprise or a team", and then connect targets to it.

The unit of work is the Litmus chaos workflow, which is an Argo Workflow made of chaos experiments run in sequence, in parallel or both, with consolidated results. A ChaosEngine resource kicks off the run, the chaos operator executes the experiments, a ChaosResult resource records the outcome, and the Litmus exporter pushes metrics into Prometheus. Steady-state hypotheses are written declaratively as probes, and annotations mark the chaos window on Grafana graphs.

For pipelines there is a chaos CI library with integrations for GitLab, GitHub Actions, Spinnaker and Keptn. Non-Kubernetes targets work too: the control plane stays on Kubernetes while the fault is executed through the target's API, with experiments such as EC2 terminate and EBS detach. As Mukkara put it, if you have an API to reach a resource, you can kill it with that API. At the time Litmus 2.0 was about to ship with the GitOps and observability features.

## Who should watch

SREs running Kubernetes who want chaos to live in Git rather than in someone's head, and anyone comparing chaos tooling from that era. It is an architecture talk, not a hands-on one.

Related Conf42 talks:

- Uma Mukkara again on [continuous SLO validation using chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering), Conf42 SRE 2021.
- Akram Riahi on [chaos engineering alongside Litmus and Jenkins](https://www.conf42.com/Chaos_Engineering_2022_Akram_Riahi_chaos_engineering_alongside_litmus_and_jenkins), Conf42 Chaos Engineering 2022.
- Henrik Rexed on [Kubernetes chaos engineering in production](https://www.conf42.com/Site_Reliability_Engineering_2022_Henrik_Rexed_kubernetes_chaos_engineering_production), Conf42 SRE 2022.

## From Chaos Native

Chaos Native was founded to support the Litmus project and its enterprise users; Mukkara pointed questions to the Litmus channel on the Kubernetes Slack.

- [Chaos Native](https://www.chaosnative.com/)
- [Chaos Native on LinkedIn](https://www.linkedin.com/company/chaos-native)

[Watch the talk on YouTube](https://youtu.be/yQiISxndExA).

## Watch the talk

[Increasing Kubernetes Resilience for an SRE](https://www.conf42.com/Chaos_Engineering_2021_Uma_Mukkara_cloud_native_at_scale) at Conf42 Chaos Engineering 2021.
