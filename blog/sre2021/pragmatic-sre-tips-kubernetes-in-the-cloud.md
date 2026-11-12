# Autoscaling won't save you when the database is the bottleneck

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/pragmatic-sre-tips-kubernetes-in-the-cloud

In short: Joshua Arvin Lat (NuWorks Interactive Labs) at Conf42 Site Reliability Engineering 2021 on pragmatic SRE habits for running Kubernetes on AWS

How many apples are in the picture? Nobody can say, because some are hidden under the top layer, and that is the point Joshua Arvin Lat, CTO of [NuWorks Interactive Labs](https://ecommerce.nuworks.ph), makes with a quiz in his Conf42 Site Reliability Engineering 2021 talk. Ten tips on running Kubernetes in the cloud follow, and the thread through all of them is pragmatism: organise your data before you need it, use tools people actually know, push work out of the cluster when a managed service does it better, and find the real bottleneck before reaching for autoscaling.

Lat, an AWS Machine Learning Hero and author of Machine Learning with Amazon SageMaker Cookbook, keeps the examples on AWS: EKS, RDS, CloudWatch, X-Ray, App Mesh and SageMaker.

## Why does organised data decide your response time?

The first tip is to find ways to see what is happening inside: many nodes, application logs, network logs. Detection is shared work, because if the checkout flow on an e-commerce site breaks, software engineers and SREs both need the right access and the right charts.

The apples make the case for preparing data ahead of time. A heap cannot be counted; ten by ten by ten in neat layers is obviously 1,000. Clean, connected logs are the stacked version. And in production, time is the constraint, so self-healing automation is the first layer, with humans for the custom problems such as a deploy that destabilised the system and needs a rollback.

## Do the tools solve the problem?

Tip two is to know the options before building your own: Rancher, Prometheus, Kiali, Istio, App Mesh and Helm, so the problem someone else already hit comes with a solution. Tip three is the warning. The tools are enablers, used by people. Picture everything set up and 80% of the team not knowing how to use it, or everyone saying they have used it and only one or two people able to troubleshoot with it a month later. Training is the fix, and so is management listening. Joshua Arvin Lat said at Conf42 Site Reliability Engineering 2021: "sometimes the best words, the most important things we need to hear about are the words never said." Audits and simulations tell you more than feedback does.

## What should live outside the cluster?

Not everything belongs inside Kubernetes. If SageMaker has operators for Kubernetes, hand the ML workloads to SageMaker. Send logs to CloudWatch, traces to X-Ray. Put the database in RDS rather than in the cluster, so scaling it vertically is RDS's job. Less inside the cluster means less to manage there.

## How do users and costs shape the plan?

Know your users' behaviour: if traffic peaks between midnight and 3 a.m. and again from 3 p.m. to 7 p.m., schedule risky migrations outside those windows, and plan ahead for holidays and events instead of trusting autoscaling. Then budget for logs, the cost that shows up on the bill months later because more logs felt safer. Know where to store them, what a centralised log store costs to run, and how long a person needs to search them and connect logs across components A, B and C in different pods.

## Where is the real weak link?

When the site slows down, the reflex is to scale the cluster. Joshua Arvin Lat said at Conf42 Site Reliability Engineering 2021: "Because even if you auto scale and the database is the bottleneck, auto scaling will not help solve the latency issues." Find where the problem is first: unoptimised queries, or a need for read replicas.

Then prepare for failure so nothing fails. Simulate the common failure modes before launch: high CPU, CPU throttling, node failure, an unavailable region, sudden latency, service failure and packet loss. Match the availability to the audience, too: if most users are in one country, such as the Philippines, a global multi-region setup may be money you don't need to spend.

## What is the weakest link in security?

Sometimes it is not the cluster. His example is an AWS Cloud9 instance with kubectl installed to manage the cluster: compromise it and an attacker can delete the cluster outright. Think about IAM PassRole abuse and about an over-privileged EC2 instance that could wipe the whole account, and use multiple AWS accounts so one compromise does not take everything. The last tip is about timing: plan when there is minimal pressure, because nobody writes a thorough plan mid-emergency.

## Who should watch

Teams running their first production Kubernetes on AWS, and leads who suspect their tooling is ahead of their team's skills. It is a checklist talk, broad rather than deep.

## Related Conf42 talks

- Noaa Barki and Shimon Tolts on [100 Kubernetes postmortems](https://www.conf42.com/Site_Reliability_Engineering_2021_Noaa_Barki_Shimon_Tolts_100_Kubernetes_Post_Mortems), also at SRE 2021.
- Itiel Shwartz on [troubleshooting Kubernetes independently](https://www.conf42.com/Site_Reliability_Engineering_2021_Itiel_Shwartz_troubleshoot_K8s_independently), also at SRE 2021.
- Joshua Arvin Lat on [IaC security best practices](https://www.conf42.com/DevSecOps_2023_Joshua_Arvin_Lat_iac_security_best_practices) at Conf42 DevSecOps 2023.

[Watch Joshua Arvin Lat's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Joshua_Arvin_Lat_Pragmatic_Site_Reliability_Engineering_Kubernetes)

## From NuWorks Interactive Labs

NuWorks Interactive Labs is the company Joshua Arvin Lat leads as CTO.

- [NuWorks Interactive Labs website](https://ecommerce.nuworks.ph)

[Watch the talk on YouTube](https://youtu.be/hw3ezm246aI).

## Watch the talk

[Pragmatic Site Reliability Engineering for Kubernetes in the Cloud](https://www.conf42.com/Site_Reliability_Engineering_2021_Joshua_Arvin_Lat_Pragmatic_Site_Reliability_Engineering_Kubernetes) at Conf42 Site Reliability Engineering 2021.
