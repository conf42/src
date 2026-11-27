# Platform-first cloud starts with pilot teams, not a big bang

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/platform-first-cloud-starts-with-pilot-teams

In short: Srikanth Vissarapu (Crusoe) at Conf42 Platform Engineering 2025 on self-service infra, golden paths, hub-and-spoke multi-cloud and phased rollout.

A cloud migration that hands developers a console login and a wiki page is just a ticket queue with extra steps. At Conf42 Platform Engineering 2025, Srikanth Vissarapu, Staff Software Engineer at Crusoe, argued for a platform-first approach: self-service infrastructure, golden paths, policy as code, and a rollout that starts with a few pilot teams before the whole company is asked to move in.

The talk is a broad tour rather than a single case study. Think of it as a checklist of what an internal platform has to cover before it earns the name, delivered by someone who has clearly sat on both sides of the provision-me-a-VM ticket.

## The gap is between what developers build and what they must know

Vissarapu frames the problem as a mismatch. Developers want to ship features; classic DevOps models also make them carry infrastructure, networking and compliance in their heads. That cognitive load slows everything down.

His answer has three parts. Self-service, so engineers provision VMs, run workloads and manage configuration without going through a ticketing system. Golden paths, the predefined and optimised routes through common scenarios like building, testing and deploying a service. And central governance, because more freedom needs more guardrails: least-privilege access, security and privacy checks baked in, not bolted on.

## Multi-cloud needs a hub, a mesh and codified rules

Most companies he sees have drifted into more than one cloud, each picked for its own strengths. The pattern he recommends is hub and spoke: a central hub owns the shared foundations (authorisation, monitoring, governance) and teams build services on top.

Between those services sits a service mesh such as Istio on Kubernetes, so developers stop hand-rolling inter-service communication. Over everything sits policy as code: governance rules written down, versioned and enforced automatically, so compliance doesn't depend on someone remembering a spreadsheet.

## Self-healing deploys are part of developer experience

The developer experience section covers the expected ground (AI coding assistants like GitHub Copilot for boilerplate and tests, CI/CD with automated unit and integration tests) and then lands on a point worth stealing: a canary deployment that rolls itself back to the last healthy build is a developer-experience feature, not only an ops feature. Nobody codes confidently when a bad release means a weekend.

On the infrastructure side he lists reusable infrastructure-as-code modules and template libraries, autoscaling templates that kick in when workloads outgrow what you bought, GitOps workflows for an audit trail of what changed and what rolled back, and container scanning so known-vulnerable libraries never reach production.

## Measure the platform three ways

How do you know it worked? Vissarapu splits the scorecard into three:

- **Technical:** lead time for changes, mean time to recovery, change failure rate.
- **Business:** cloud spend, cost per deployment, time to market. His example: launching in a new country no longer means buying hardware there.
- **Developer:** surveys and feedback, because a platform people hate is a platform people route around.

## Roll it out in phases

The most practical slide is the adoption plan. Start with pilot teams and build the base layer with them: a consistent way to package and deploy, canary and blue-green as built-in options. Once the pilots are confident, widen to cross-functional teams and turn the platform into shared ownership, where other teams contribute and extend it. Then keep iterating on feedback. A platform is a product with users, and this plan treats it like one.

The abstract quotes headline gains for faster deployments and lower overhead; the talk itself spends its time on the patterns rather than on a measured case, so treat those figures as the goal, not a benchmark.

## Who should watch

Engineering managers and architects starting an internal platform, or explaining one to leadership, will get a clean map of the territory in one sitting. If you already run Backstage, Crossplane and a mature GitOps setup, you will recognise most of it; skip to the rollout and metrics sections.

## Related Conf42 talks

- George Hantzaras and Dan Mckean on a [self-service DBaaS inside an internal developer platform](https://www.conf42.com/Cloud_Native_2023_George_Hantzaras_Dan_Mckean_self_service_dbaas_internal_developer_platform) at Cloud Native 2023: one golden path, built for real.
- Hoang Dinh Nguyen on [building a developer platform with Kusion](https://www.conf42.com/DevSecOps_2024_Hoang_Dinh_Nguyen_developer_platform_kusion) at DevSecOps 2024, the platform-as-code angle.

[Watch Srikanth Vissarapu's talk](https://www.conf42.com/Platform_Engineering_2025_Srikanth_Vissarapu_success_transformation_enterprise)

[Watch the talk on YouTube](https://youtu.be/H_6IDsng6Xw).

## Watch the talk

[Platform-First Cloud Transformation: Engineering Scalable Infrastructure for Enterprise Success](https://www.conf42.com/Platform_Engineering_2025_Srikanth_Vissarapu_success_transformation_enterprise) at Conf42 Platform Engineering 2025.
