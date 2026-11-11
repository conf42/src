# Microsoft's chaos lesson - test failure scenarios, not single faults

Conf42 Blog, 2022-03-09. https://www.conf42.com/blog/ce2022/azure-chaos-studio-scenarios-over-faults

In short: John Engel-Kemnetz (Microsoft) at Conf42 Chaos Engineering 2022 on how 50+ Microsoft teams use Azure Chaos Studio, and why chaos often belongs in pre-production

The folk wisdom says chaos engineering belongs in production. At Conf42 Chaos Engineering 2022, John Engel-Kemnetz, Principal Program Manager on the Azure Chaos Studio team at Microsoft, explained why that advice fits poorly for many mission-critical services, and what over 50 Microsoft cloud service teams learned running chaos with Azure Chaos Studio, the same product Azure sells to customers.

The talk is mostly about practice and culture, with Chaos Studio as the vehicle, not a feature tour.

## Why is resilience a shared job in the cloud?

John starts with the stakes. Disruption ranges from a full blackout to brownouts such as higher latency or a slight dip in availability, and the cost goes beyond revenue: financial institutions must give regulators audit evidence that they can recover from disaster, and emergency services increasingly run on cloud providers.

Cloud makes resilience harder in two ways. Architectures such as Azure Kubernetes Service or App Service are distributed and less familiar, so resilience patterns are less mature in many organisations. And a serverless app may sit three, four or five layers of compute above the physical data centre, which sometimes leaves you hoping the platform is stable. Hence shared responsibility, as with security: a provider with perfect availability cannot save a consumer with no resilience practices, and the reverse holds too.

## Is production really the place to start?

Often not, he argues. John frames the choice between running chaos in a CI/CD pipeline and running it later (shift right) by traffic: if a load test can generate what you need on demand, put the experiment in the pipeline as a deployment gate; if you need real or very realistic customer traffic, shift right.

Shifting right still does not have to mean production. Teams early in a journey, say just starting with availability zones, have not built the confidence to cause that failure in production yet, so production becomes the final checkbox. And some services cannot accept the risk at all: his example is a healthcare provider deciding whether emergency prescriptions are issued.

## What does Chaos Studio do?

It is a fully managed Azure service, in public preview at the time, so there is no tooling to install, update or secure. Experiments deploy the way your infrastructure does, through Azure Resource Manager, Azure Policy and Bicep, with the same access control. It integrates with observability tooling and has a growing fault library, with an aim to ship experiment templates that replicate the most severe Azure outages so customers can test their defences against them.

The faults are real, not simulated: a shut-down VM is really shut down, and CPU pressure on an AKS cluster really happens. So safety comes from permissions: restrictions on which resources can be targeted, which faults can be used on each, and what the experiment itself may access.

## How does Microsoft use it internally?

Two priorities. First, failure scenarios over individual faults: incident analysis showed that what matters is a region failure, an inability to scale, a network configuration change, an availability zone going down, or an Azure Active Directory or DNS outage, and faults are just the ingredients. Second, shifting high-blast-radius scenarios left, with the goal that every new Azure deployment validates specific failure scenarios as a pre-production gate.

The examples are concrete. The Power Platform team shut down all compute in a region, found that failover to a secondary region did not come up, and fixed it; recreating an outage also showed where their monitoring was too thin. The Azure Key Vault team ran availability zone and scale-up experiments and found, in pre-production, an autoscale rule that had drifted so the virtual machine scale set stopped scaling under stress.

## Lessons for everyone else

- **Mature tooling and process first**: observability, backups, live-site process, troubleshooting guides, automatic mitigations. John said at Conf42 Chaos Engineering 2022: "chaos engineering is not suitable for a case where you're learning something you already knew."
- **Quantify and analyse past outages.** Put a currency figure on downtime to get stakeholders invested, then start with high-blast-radius and high-frequency incidents.
- **Build confidence in pre-production.** Azure runs two canary regions closed to customers, where almost every service has a stamp and must bake before production; Microsoft's own Teams traffic runs through a dogfood environment there.
- **Make quality everyone's job**, including product managers and leadership. Quality is in the core priorities of every employee in the Azure division.

## Who should watch

Teams on Azure weighing Chaos Studio, and anyone in a regulated or safety-critical domain who has been told chaos must run in production and suspects otherwise.

## Related Conf42 talks

- Peter De Tender on [stress testing with Azure Chaos Studio](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Peter_De_Tender_stresstesting_azure_chaos) at Conf42 SRE 2024.
- Gunnar Grosch on [hypothesis development and resilience modelling](https://www.conf42.com/Chaos_Engineering_2024_Gunnar_Grosch_hypothesis_development_resilience_modeling) at Conf42 Chaos Engineering 2024.
- Kyle Shelton on [disaster recovery preparedness](https://www.conf42.com/Chaos_Engineering_2022_Kyle_Shelton_disaster_recovery_preparedness) at Conf42 Chaos Engineering 2022.

[Watch John Engel-Kemnetz's talk](https://www.conf42.com/Chaos_Engineering_2022_John_EngelKemnetz_azure_chaos_studio)

## From Microsoft

Azure Chaos Studio is the managed chaos engineering service the talk is built around; John points to its page for documentation, getting started and customer studies.

- Microsoft: [microsoft.com](https://www.microsoft.com/en-ie/)
- Azure Chaos Studio: [aka.ms/AzureChaosStudio](https://aka.ms/AzureChaosStudio)

[Watch the talk on YouTube](https://youtu.be/c63JZRgRxIQ).

## Watch the talk

[Chaos engineering at Microsoft with Azure Chaos Studio](https://www.conf42.com/Chaos_Engineering_2022_John_EngelKemnetz_azure_chaos_studio) at Conf42 Chaos Engineering 2022.
