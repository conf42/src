# Most Kubernetes misconfigurations are one-line fixes nobody made

Conf42 Blog, 2024-01-24. https://www.conf42.com/devops2024/kubernetes-benchmark-one-line-fixes

In short: Joe Pelletier (Fairwinds) at Conf42 DevOps 2024 on what 330,000 scanned workloads say about Kubernetes cost, reliability and security hygiene

Developers guess their resource requests, and they guess high. At Conf42 DevOps 2024, [Joe Pelletier](https://www.conf42.com/DevOps_2024_Joe_Pelletier_kubernetes_benchmark_report), Vice President of Product Strategy at Fairwinds, walked through the 2024 Kubernetes Benchmark Report, built from more than 330,000 workloads scanned by Fairwinds Insights. The pattern across cost, reliability and security: many of the worst findings are one-line fixes that never got made, often because a bad manifest got copied from one team to the next.

It is the third year of the report and the largest sample so far, with more than a dozen policy types. The talk covers about a quarter of the full report, by his estimate, and finishes with a short pitch for Fairwinds Insights.

## How do you read the charts?

Every chart plots the share of an organisation's workloads affected by a check against the share of organisations at that level. The useful reading tip: when the group of organisations with fewer than 10% of workloads affected shrinks year over year, the problem is getting harder to control, even if the average looks similar.

## Where is the money going?

The headline finding, measured for the first time this year: 37% of organisations need to right-size 50% or more of their containers. Without tooling or feedback loops telling them what to set, developers over-provision memory and CPU, and nobody notices until the bill arrives. The other end of the chart is encouraging, with 57% of organisations at 10% or fewer workloads affected, so some teams do get it right.

Missing requests are the bigger trend. 78% of organisations have at least 10% of their workloads missing CPU requests, up from about 50% the year before. Kubernetes treats requests as optional, but the scheduler cannot place a workload well without them. His view is that this is one of the easiest problems to fix with guardrails: flag it at pull request or at admission, and use the moment to teach.

## Which reliability basics are being skipped?

- **Image pull policy**: about 24% of organisations rely on a cached image for 90% of their images because the pull policy is not set to Always, which risks inconsistency and stale, unpatched images.
- **Health checks**: about 66% of liveness probes and 69% of readiness probes are missing. These need some application-specific input, which may explain why teams skip them.
- **Replicas**: 30% of organisations have fewer than 10% of deployments missing replicas, better than in 2023, but many still have far more.

He calls the replicas case the copy and paste problem: one team's manifest without replicas becomes the starting point for the next team, and the misconfiguration spreads. Joe Pelletier said at Conf42 DevOps 2024: "this is usually a very quick fix, like a one line change to your infrastructure as code."

## Is security getting better or worse?

Both, depending on the check. About 28% of organisations run 90% of their workloads with insecure capabilities such as NET_ADMIN, sometimes needed, often copied in by accident. Running as root is the good-news story: 30% of organisations run 70% or more of their containers as root, down from 44% in the previous report. It is also a one-line change, and he guesses its fame as the textbook Kubernetes misconfiguration helped.

Image vulnerabilities improved too. 26% of organisations have fewer than 10% of workloads affected, up from 12% in 2023, which he reads as teams upgrading third-party images and scanning more. Almost 84% of organisations now have near-complete scan coverage of running containers, up from 64%.

Fairwinds added checks from the NSA's Kubernetes hardening guidance, including one for network policies. The picture is split: 37% of organisations have fewer than 10% of workloads without a network policy, while a majority have more than half their workloads without one, which means those pods can talk to anything in the cluster.

## What does he suggest doing about it?

Guardrails at two points in the pipeline: at pull request, when infrastructure-as-code changes are made, and at admission, when workloads are deployed. Give developers the feedback and an easy way to fix it, and keep configurations consistent. This is where the Fairwinds pitch comes in: Insights covers configuration checks against standards such as the NSA guide, SOC 2 and ISO 27001, image scanning, Kubernetes cost allocation and right-sizing recommendations.

## Who should watch?

Platform teams who own a multi-tenant cluster and want numbers to bring to the next argument about whether admission policies are worth it. It is a short, data-driven talk; download the full report for the breakdowns.

## Related Conf42 talks

- Ara Pulido on [policy as code for Kubernetes with OPA and Gatekeeper](https://www.conf42.com/Cloud_Native_2021_Ara_Pulido_poilcyascode_kubernetes_opa_gatekeeper) at Conf42 Cloud Native 2021.
- Reza Ramezanpour on [Kubernetes security policy design](https://www.conf42.com/Cloud_Native_2023_Reza_Ramezanpour_kubernetes_security_policy_design_top10) at Conf42 Cloud Native 2023.
- Manpreet Singh Sachdeva on [securing Kubernetes with best practices](https://www.conf42.com/Incident_Management_2024_Manpreet_Singh_Sachdeva_26_kubernetes_security_practices) at Conf42 Incident Management 2024.

[Watch Joe Pelletier's talk](https://www.conf42.com/DevOps_2024_Joe_Pelletier_kubernetes_benchmark_report), part of [Conf42 DevOps 2024](https://www.conf42.com/devops2024).

## From Fairwinds

Fairwinds makes Fairwinds Insights, a Kubernetes governance platform with configuration guardrails, image scanning, cost allocation and right-sizing, and publishes the yearly Kubernetes Benchmark Report.

- [Fairwinds website](https://www.fairwinds.com/)

[Watch the talk on YouTube](https://youtu.be/9BqNSWGQlmk).

## Watch the talk

[The 2024 Kubernetes Benchmark Report](https://www.conf42.com/DevOps_2024_Joe_Pelletier_kubernetes_benchmark_report) at Conf42 DevOps 2024.
