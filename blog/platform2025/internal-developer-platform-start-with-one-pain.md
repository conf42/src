# Build your developer platform around one pain point first

Conf42 Blog, 2025-08-31, updated 2026-11-09. https://www.conf42.com/blog/platform2025/internal-developer-platform-start-with-one-pain

In short: Anil Kumar Veldurthi (US Bank) at Conf42 Platform Engineering 2025 says treat infrastructure as a product, start with one pain point, measure from week one.

How much of last week did your developers spend fighting infrastructure instead of shipping features? Anil Kumar Veldurthi, a cloud architect whose two decades include Wells Fargo, First Republic Bank and US Bank, opened his Conf42 Platform Engineering 2025 talk with that question, and his answer for the 40%-or-more crowd is an internal developer platform built like a product, one painful problem at a time.

This is a strategy talk with a roadmap attached. If you already run Backstage and Argo CD in anger, you will recognise most of it. If you are the person who has to convince a VP to fund a platform team, it is close to a ready-made pitch.

## DevOps hit a scaling wall, and developers are paying for it

Anil's diagnosis: practices that work for a team of ten become miserable at a hundred-plus microservices across several clouds. He has seen organisations where a test environment needs sign-off from six teams and takes about three weeks. Meanwhile the competition deploys several times a day.

Platform engineering, in his telling, does not replace DevOps. It stops asking every developer to be an infrastructure expert. Infrastructure becomes a product and developers become its customers, so you measure their satisfaction and iterate on their feedback. The example he uses lands well: instead of two days of learning Terraform, security groups and networking to get a database, a developer answers a few questions and has one in minutes.

## Hide Kubernetes, compose the rest

The technology section is refreshingly opinionated. Kubernetes is the default substrate, but his golden rule is not to expose it to developers. They should be able to ask for a scalable web service, not learn storage classes. GitOps is the operational backbone, so every change to infrastructure and config is auditable and reversible. A service mesh takes service-to-service auth, circuit breaking and observability off each team's plate.

His summary is "composition over creation": Backstage for the portal, Argo CD for GitOps, Istio for the mesh, and custom code only where the business is genuinely different. On build versus buy, he warns that a custom platform needs at least 10 to 15 full-time engineers, and that organisations routinely underestimate that by half. The hybrid route (off-the-shelf portal and GitOps, custom glue) is where most successful teams end up.

## The roadmap, and the traps

Phase one is a quick win on the worst pain, usually CI/CD or environment provisioning, owned by an actual product owner rather than a committee of engineers. Phase two adds self-service observability, automated security and templates. Phase three brings the advanced deployment strategies. Skipping the first two to build "the ultimate platform" is the failure he has watched most often: one organisation spent 18 months on it, launched, and watched developers go back to their old tools because it was too complex.

The other traps are familiar and still worth hearing: building for theoretical problems instead of real ones, not-invented-here syndrome (do not write your own service mesh), and governance that is either too rigid or too loose. He also hands out homework: send a developer survey this week with one question, what is the most frustrating part of getting code from laptop to production, and start tracking environment creation time, deployment frequency and satisfaction even if the numbers are embarrassing.

## Who should watch

Engineering managers and staff engineers making the case for a platform team, and new platform teams deciding what to build first. The back half includes an ROI framework and a pre-flight checklist (executive sponsor, product owner, pilot application), which is the part to send to your manager.

## Related Conf42 talks

- [Caio Medeiros Pinto (Citi) on three practices for a smooth platform engineering adoption](https://www.conf42.com/DevOps_2024_Caio_Medeiros_Pinto_smooth_platform_engineering_adoption), the organisational side of the same rollout.
- [George Hantzaras and Dan Mckean (MongoDB) on building internal developer platforms with Kubernetes operators](https://www.conf42.com/Cloud_Native_2024_George_Hantzaras_Dan_Mckean_internal_developer_kubernetes), for what "hide Kubernetes" looks like in code.

[Watch Anil Kumar Veldurthi's talk](https://www.conf42.com/Platform_Engineering_2025_Anil_Kumar_Veldurthi_internal_ops_impact)

[Watch the talk on YouTube](https://youtu.be/-yw9kT-CD0I).

## Watch the talk

[From Ops to Impact: Scaling Engineering Velocity with Internal Developer Platforms](https://www.conf42.com/Platform_Engineering_2025_Anil_Kumar_Veldurthi_internal_ops_impact) at Conf42 Platform Engineering 2025.
