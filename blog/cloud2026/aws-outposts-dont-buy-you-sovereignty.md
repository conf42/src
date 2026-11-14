# Sovereignty is about who runs the control plane, not where the rack is

Conf42 Blog, 2026-04-08. https://www.conf42.com/blog/cloud2026/aws-outposts-dont-buy-you-sovereignty

In short: Dmytro Hlotenko of Sage Austria at Conf42 Cloud Native 2026 on EU compliance on AWS: Cloud Act, DORA, NIS2, the Sovereign Cloud and the Outposts trap.

Putting servers in a European bunker does not make your data European. At Conf42 Cloud Native 2026, [Dmytro Hlotenko](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience), Senior Cloud Operations Engineer at Sage in Austria, argued that jurisdiction follows operational control, and then took AWS Outposts apart with benchmark numbers to show what keeping it on-prem actually costs.

He opens with a disclaimer worth repeating: he is an engineer, not a lawyer, and the talk is a starting point for your own conversation with legal and compliance. That honesty runs through the whole session. His abstract sums up the stance: "Sovereignty without operational maturity is just compliance theater."

## Geography is not jurisdiction

The core argument is about the Cloud Act. It targets service providers and the entities that manage data, not the people who wrote the software. So if you run licensed software on your own metal with your own staff, there is little for a US warrant to grab. Hand the management plane, the admin credentials or the telemetry to a US-controlled managed service, and your hardware in Munich is exposed exactly like a public cloud region would be.

That leads to his one question for every vendor pitch: who operates the control plane? Bring-your-own-key and bring-your-own-hardware do not change the answer if someone outside your jurisdiction holds root.

## DORA and NIS2 don't ban hyperscalers

Hlotenko spends a good chunk of the talk de-escalating regulatory panic. DORA cares about concentration risk and exit strategies for financial services. NIS2 cares about supply-chain security. Neither says you cannot use AWS, Azure or GCP. They ask you to stop doing it blindly: impact assessment, documented exit strategy, strong encryption, governance. A three-year migration plan is not a requirement.

He also makes the case against swapping one well-run AWS estate for a patchwork of smaller providers. The spreadsheet counts compute and storage. It misses hiring for a stack nobody knows, lost velocity, and mean time to recovery when you have, in his abstract's words, "seven SLAs, seven blast radiuses, and seven on-call rotations."

## The European Sovereign Cloud moves the needle, partly

The AWS European Sovereign Cloud, launched in January 2026, is a separate partition with its own legal entity, run by EU-resident staff, with metadata, CloudTrail and IAM staying in the Brandenburg region. He calls partition-as-perimeter a fundamental change compared to the regular EU regions, where some data still travels to us-east-1. The gap he flags: the ultimate parent is still a US company, which is why German and French authorities read it differently.

## Outposts solve physics, not law

The case study is the reason the talk exists. A regulated Austrian workload, a team with years of AWS muscle memory, and a business asking: why not put an Outpost in our own data center? Because Outposts were built for low-latency edge compute, and compliance came later. The control-plane metadata lives in the parent region, so Cloud Act exposure is the same as Frankfurt.

Then the service list shrinks: no Lambda, no Glue, no SageMaker, no Redshift, no Transit Gateway, a stripped-down ALB and EKS, and S3 that is limited and costs extra. What's left is plain compute that looks like AWS.

The team benchmarked it properly. They replayed real user behaviour with Locust and Playwright, generating load from Azure in Vienna so they weren't benchmarking AWS from inside AWS. Two findings stand out. A vCPU is often an SMT thread, so four real VMware cores can mean roughly eight vCPUs on AWS, with knock-on effects for database and OS licensing. And storage hurt: no io1 or io2, a ceiling of 16,000 IOPS against the 200K to 300K a SAN gave them, and internal database jobs that took two to three times longer.

The last trap is backups. EBS snapshots go to the parent region by default, which quietly undoes the data-residency story. Fixing that means local S3 from another provider and a more complex restore path.

## Who should watch

Platform and cloud ops engineers in the EU who keep getting forwarded articles about sovereignty, and anyone pricing Outposts as a compliance fix. The talk closes with a decision tree rather than a verdict, which is the right answer for a question this dependent on your regulator.

## Related Conf42 talks

- [How Geo-Distributed Apps Use Global Cloud Infra for Speed and Compliance](https://www.conf42.com/Cloud_Native_2022_Denis_Magda_geodistributed_apps_global_cloud_infra_speed_compliance) by Denis Magda at Conf42 Cloud Native 2022.
- [Mastering Multi-Cloud Database Resilience: Oracle & SQL Server in a Cloud-Native World](https://www.conf42.com/Incident_Management_2025_Adithya_Sirimalla_multicloud_databases_resilience) by Adithya Sirimalla at Conf42 Incident Management 2025.
- [My Step Functions DAG Was a Lie: Going Agentic on 8,000 Photos](https://www.conf42.com/AI_Agents_2026_Dmytro_Hlotenko_serverless_photos_aws), Hlotenko's own lighter AWS talk at Conf42 AI Agents 2026.

[Watch Dmytro Hlotenko's talk](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience) or the [YouTube recording](https://youtu.be/LQdH_BF4I-M).

## Watch the talk

[Keep Calm and Run on AWS: Engineering Compliance Without Abandoning Your Stack](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience) at Conf42 Cloud Native 2026.
