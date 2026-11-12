# If developers can deploy, let them roll back

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/developers-who-deploy-should-roll-back

In short: Itiel Shwartz (Komodor) at Conf42 SRE 2021 on getting developers to troubleshoot Kubernetes themselves - buy-in, training, tools and permissions.

Plenty of teams let developers ship to production and then make them call DevOps to press the rollback button. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), Itiel Shwartz, CTO and co-founder of Komodor, argued that if developers are expected to own their services on Kubernetes, operations has to hand over four things in order: a reason to care, training, tools that suit how developers look at a system, and the permissions to actually fix it.

## Why is Kubernetes so hard to troubleshoot?

He starts from speed: elite teams deploy hundreds or thousands of times a day, and Docker and Kubernetes became the default to support that, with 88% of organisations, by his figure, already on Kubernetes. The price arrives after the migration. Kubernetes makes it easy to build very complex systems and to shoot yourself in the foot. Lots happens in a cluster that nobody sees: the control plane changes, nodes change, and not every change is surfaced. Splitting a monolith into many microservices means a small, innocent change in one can crash the whole application.

Add permissions (some organisations don't let everyone see all the data) and a shortage of real Kubernetes expertise, and you get developers asked to own services without knowing what happens under the hood.

## Whose job is troubleshooting now?

A few years ago it was the NOC and ops. With shift-left, organisations are pushing it onto developers, who already deploy the code. His point is that dumping it on them, Kubernetes is yours now, doesn't work.

## The four steps

**Buy-in first.** You don't need the whole organisation, a few champions will do. They have to want it, not out of masochism, but because troubleshooting brings ownership, responsibility and independence. If you expect them to wake up at night and read a cluster, they need to be engaged.

**Then training.** Developers have long been measured on code quality and features shipped, not on troubleshooting, and tend to look at the system through a microscope where ops looks at the macro picture. Write the playbooks and teach both Kubernetes itself and how your company runs it.

**Then tools.** Most monitoring and troubleshooting tools, he says, are built for operations people at the macro level, and he names Komodor as an exception. Build developers the relevant dashboards in Datadog or Prometheus, show them how to change them, and make sure they know where to look when something breaks.

**Then permissions.** You can't hold someone responsible for production when they can't see logs, roll back or add replicas. "One of the most frustrating things that I see in organization is that the developers can deploy the code to production, but for some reason they can't really roll back to the previous version," Itiel Shwartz said at Conf42 SRE 2021. Everyone loses: DevOps has to be in the loop for every rollback, and developers wait for someone to click a button.

## A marathon, not a sprint

Find one or two tech leads in the dev organisation as partners and expect it to take time: playbooks, tools and access mechanisms will all need changing. He reframes the extra work for ops as automating yourself out of the process, so you stop being woken up. The payoff he describes runs both ways: developers fix their own issues and ship faster, and SREs stop fielding why-is-my-app-crashing messages. For teams just adopting Kubernetes, his advice is to involve developers from day one, in picking technologies and in troubleshooting, rather than lifting legacy systems over and hoping.

## Who should watch

Platform and SRE teams who own a Kubernetes platform and want developers on call for their own services, and engineering managers planning that shift. It is a process talk, short, with no demo; Komodor gets a mention in the tools step. Pair it with:

- [Noaa Barki and Shimon Tolts on lessons from 100+ Kubernetes post-mortems](https://www.conf42.com/Site_Reliability_Engineering_2021_Noaa_Barki_Shimon_Tolts_100_Kubernetes_Post_Mortems) at Conf42 SRE 2021.
- [Joshua Arvin Lat on pragmatic SRE for Kubernetes in the cloud](https://www.conf42.com/Site_Reliability_Engineering_2021_Joshua_Arvin_Lat_Pragmatic_Site_Reliability_Engineering_Kubernetes) at Conf42 SRE 2021.
- [Dan Slimmon on clinical troubleshooting](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Dan_Slimmon_clinical_troubleshooting_diagnose) at Conf42 SRE 2024.

[Watch Itiel Shwartz's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Itiel_Shwartz_troubleshoot_K8s_independently) from Conf42 SRE 2021.

## From Komodor

Komodor describes itself in the talk as a Kubernetes-native troubleshooting platform.

- [Komodor website](https://komodor.com/)

[Watch the talk on YouTube](https://youtu.be/yuoTwL117aY).

## Watch the talk

[How to Empower Developers to Troubleshoot K8s Independently](https://www.conf42.com/Site_Reliability_Engineering_2021_Itiel_Shwartz_troubleshoot_K8s_independently) at Conf42 Site Reliability Engineering 2021.
