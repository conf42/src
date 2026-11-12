# Chaos engineering takes quarters, not sprints, to reach production

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/chaos-engineering-staging-to-production-quarters

In short: Uma Mukkara (Chaos Native) at Conf42 Cloud Native 2021 on why cloud native needs chaos engineering, a staged rollout for SREs, and LitmusChaos

Cloud native changed how often production changes, and that is the whole argument for chaos engineering. At Conf42 Cloud Native 2021, Uma Mukkara, founder and CEO of Chaos Native and co-creator and maintainer of the CNCF project LitmusChaos, lays out what reliability means once your app is a pile of fast-moving microservices, how SREs and developers should each adopt chaos engineering, and where Litmus fits.

It's an overview talk, light on demos and heavy on adoption advice, with the Litmus part at the end clearly marked as the vendor's own project.

## What does reliability mean in cloud native?

Running without an outage is only the start, in his definition. Reliability also means meeting SLOs and business SLAs while you scale up for peak days and while you upgrade services in production. Cloud native makes that harder in two ways: an application is now many microservices, and they change fast because of everyone's CI/CD pipelines, including the services you consume and don't own.

"It's very common to see big changes happen in production environments every quarter or two, but in cloud native they are happening almost every week," Uma Mukkara said at Conf42 Cloud Native 2021. With that pace you can't freeze upgrades into scheduled windows; you automate them and need a separate way to know the system stays reliable. His answer is chaos engineering from the beginning, at scale.

## Why break things on purpose?

The case is familiar but well put. Outages are expensive, even small ones depending on your SLAs, and you can't prevent them no matter how well you test, so prepare for them. Inject the failure before it happens, and you learn how fast you recover and how your team responds instead of guessing.

The business benefits he lists: shorter outages, revenue losses caught in pre-production, customers retained, faster migrations to microservices because you can benchmark reliability before and after, and right-sized scaling you've actually tested. He names banking, retail and e-commerce as sectors where it has proven itself, and edge computing as a place where failure testing needs automating.

## Four principles for picking a chaos platform

For cloud native chaos engineering he offers principles rather than a product pitch:

- **Open source and community-built experiments**, which are better tested and less prone to false positives or negatives, and leave you in control of what fault goes in.
- **Lifecycle management** through APIs or operators, because experiments need maintaining like any code.
- **Scale**: killing containers when there are thousands of them needs chaos infrastructure that scales too.
- **Open observability**: you should see exactly when chaos was injected, what it was and how, typically in a Prometheus-based stack.

## A rollout plan for SREs

The most practical part is the timeline. Start in staging, or as a trigger in your CD, with simple experiments: inject faults and check that Kubernetes autoscaling actually kicks in. Run a simple game day to build the culture. Keep that up for a quarter while raising complexity, then move to pre-production. Real failure testing in production generally takes more than a couple of quarters, because you first need to convince yourself and your team that the chaos tooling is stable, produces no false results, and that you can respond to the outages it causes.

## Chaos engineering for developers

For developers he frames it as continuous verification inside CI pipelines, independent of whether the SREs practise chaos engineering. Your pipeline depends on microservices you didn't write and on platforms you don't control, so inject failures of those dependencies and platforms in the pipeline and see how your code behaves, ideally across several clouds or on-prem since you don't know where a microservice will end up running.

## Where does LitmusChaos fit?

Litmus was a CNCF sandbox project at the time of the talk, with more than 50,000 installations or operators running, he says. It installs as a Helm chart, publishes experiments in the public ChaosHub (which you can mirror into an air-gapped environment), and gives you a central control plane, the Litmus portal, to run predefined chaos workflows or build your own. Targets include Kubernetes resources and also VMs, bare metal and AWS, GCP and Azure, with initial VMware experiments. GitOps integration with Argo CD or Flux can trigger chaos when an application changes, and the chaos logic is a library that CI systems call; he cites GitLab, GitHub Actions, Spinnaker and Keptn examples.

## Who should watch

SREs who need a staged plan to sell chaos engineering to their team, and developers wondering what a chaos stage in CI would even test. If you already run game days, the principles and timeline sections are the useful bits.

## Related Conf42 talks

- Akram Riahi on [chaos engineering with Litmus and Jenkins](https://www.conf42.com/Chaos_Engineering_2022_Akram_Riahi_chaos_engineering_alongside_litmus_and_jenkins) at Conf42 Chaos Engineering 2022.
- Mandi Walls on [game days and chaos engineering](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering) at Conf42 Incident Management 2022.
- Henrik Rexed on [Kubernetes chaos engineering in production](https://www.conf42.com/Site_Reliability_Engineering_2022_Henrik_Rexed_kubernetes_chaos_engineering_production).

[Watch Uma Mukkara's talk](https://www.conf42.com/Cloud_Native_2021_Uma_Mukkara_reliability_cloud_native_systems) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Chaos Native

Chaos Native provides enterprise support for teams running LitmusChaos in production and non-production environments, and has run a Cloud Native Chaos Engineering workshop.

- Chaos Native: [chaosnative.com](https://www.chaosnative.com/)
- [Cloud Native Chaos Engineering Workshop by ChaosNative](https://www.chaosnative.com/cnce-workshop)
- [Chaos Native on LinkedIn](https://www.linkedin.com/company/chaos-native)

[Watch the talk on YouTube](https://youtu.be/VNhGNy10QnM).

## Watch the talk

[Chaos Engineering for Cloud Native](https://www.conf42.com/Cloud_Native_2021_Uma_Mukkara_reliability_cloud_native_systems) at Conf42 Cloud Native 2021.
