# If banks moved their core to the cloud, your packages can follow

Conf42 Blog, 2022-04-27. https://www.conf42.com/blog/cloud2022/banks-moved-core-to-cloud-packages-next

In short: Ciara Carey (Cloudsmith) at Conf42 Cloud Native 2022 on why going cloud native is now worth the effort, with banking as the case study

When the most conservative buyers in tech stop asking for the on-prem version, something has shifted. Ciara Carey, Developer Relations at Cloudsmith, built her Conf42 Cloud Native 2022 talk on that observation: banks have started moving core systems to the cloud, the cloud is mature enough to carry them, and the package repository at the heart of your build pipeline belongs there too.

It is a sponsor talk from a company that only sells a cloud-native SaaS, so the conclusion is not a surprise. The useful part is the honest cost column and the banking case study in the middle.

## What does cloud native actually mean here?

Carey, a software engineer for over ten years before moving into DevRel, describes the usual stack: automated provisioning and configuration, resources allocated at deploy time, microservices behind REST APIs, Docker containers orchestrated by Kubernetes, Kafka or RabbitMQ for messaging, and CI/CD shipping several times a day. Cloudsmith sees the trend in its own storage: from 2020 to 2021, new Helm packages were up 271% and new Docker packages up 236%.

## Why doesn't everyone just move?

She doesn't pretend it is free. Moving is an executive decision with big upfront costs: rearchitecting a monolith into microservices, renegotiating supplier contracts, new tooling and build processes, retraining developers and IT staff (and maybe customers), possibly hiring a consultancy. Your cloud provider's outages also become yours. Her example is the AWS outage in the US East region in December 2021, which took out Tinder, IMDb, Netflix and Disney among others.

"So it's no joke moving to the cloud," Ciara Carey said at Conf42 Cloud Native 2022.

The reasons to do it anyway, in her telling:

- **Cost.** No data centre electricity and air conditioning, no patching or replacing hardware, economies of scale you can't match alone, and the opportunity cost of engineers working on something other than your core product.
- **Performance.** Elastic scaling for growth spurts, redundancy and failover across regions.
- **Security.** 24/7 monitoring and expertise beyond most in-house teams, plus inherited accreditations (HIPAA, ISO, FIPS, SOC 2). She says being cloud native made Cloudsmith's own ISO 27001 certification faster.
- **Distributed teams.** Multi-region services, CDNs and edge caching mean the team in the US and the team in Europe both get decent latency. She works from Dublin; head office is in Belfast.
- **Innovation.** Shipping several times a day, data analytics on aggregated data, and tooling that improves without an upgrade project.

## Why did banks move during the pandemic?

Banks long knew the cloud was cheaper but judged it not worth the risk: heavy regulation, privacy concerns, and core systems processing millions of transactions a day that work, so nobody wants to touch them. Then several big banks went the other way. Capital One announced in November 2020 that it was closing all its data centres and moving everything to AWS, and she points to JP Morgan, HSBC and Wells Fargo too.

Her explanation is a set of pressures arriving together. Cloud offerings matured and added compliance services built for banking. Regulators in the US, UK and EU became more open to cloud-only banks. Customers stopped walking into branches and expected real-time results. Fintechs such as Revolut and big tech launching financial products raised the competitive bar. And the pool of engineers who understand the legacy systems is shrinking and ageing. The payoff she lists: one app for mortgage, credit card and savings, fraud detection, and real balances instead of waiting days for batch processing.

## Where does the package repository fit?

If you ship several times a day, every build pushes a package (Maven, NuGet, npm, Docker and so on) to a repository, which makes it the potential bottleneck in the middle of the pipeline. Cloudsmith's answer is to make it a managed service: it supports over 28 package formats, sits on a content delivery network with over 225 points of presence, has no on-prem variant at all, and reports per-repository analytics on who downloaded what and where, plus storage, bandwidth and token usage so overages don't surprise you.

She also makes a point about support that applies beyond Cloudsmith: supporting one version on your own infrastructure is far easier than supporting many versions running on customers' hardware.

## How should you pick a cloud-native tool?

Her checklist is short and vendor-neutral. You should get access the moment you sign up, with no waiting for accounts or permissions. Features and APIs should be well documented. It needs robust APIs, integrations and webhooks so it fits into your source control, CI/CD, observability (Datadog, Splunk), security scanning and infrastructure tooling (Ansible, Terraform). And when something breaks, you should reach a person quickly.

## Who should watch

Engineers and managers making the case for (or against) a cloud migration, especially in regulated industries, and anyone still running a self-hosted artifact server out of habit. It is an overview talk, light on implementation detail.

## Related Conf42 talks

- Sven Ruppert on [supply chain security in open source projects](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects) at Conf42 Cloud Native 2023.
- Charles Akl on [chaos engineering at Citi](https://www.conf42.com/Chaos_Engineering_2024_Charles_Akl_citi_bank) at Conf42 Chaos Engineering 2024.
- Narendra Bhargav Boggarapu on [cloud banking security](https://www.conf42.com/DevOps_2025_Narendra_Bhargav_Boggarapu_cloud_banking_security) at Conf42 DevOps 2025.

[Watch Ciara Carey's talk](https://www.conf42.com/Cloud_Native_2022_Ciara_Carey_future_is_cloudnative_your_organization)

## From Cloudsmith

Cloudsmith is a cloud-native, fully managed artifact repository for 28+ package formats, the service Carey describes in the talk.

- Cloudsmith: [cloudsmith.com](https://cloudsmith.com/?utm_source=conf_42&utm_medium=referral&utm_content=cloudsmith_homepage&utm_campaign=conf_42_python_event)
- Blog: [How to Manage Your Package Promotion Workflows with Cloudsmith](https://cloudsmith.com/blog/how-to-manage-your-package-promotion-workflows-with-cloudsmith/)
- O'Reilly report: [The Rise of Continuous Packaging](https://cloudsmith.com/developers/resources/the-rise-of-continuous-packaging/)

[Watch the talk on YouTube](https://youtu.be/88X5_tDnku0).

## Watch the talk

[The Future is Cloud-native and Your Organization Should Be Too](https://www.conf42.com/Cloud_Native_2022_Ciara_Carey_future_is_cloudnative_your_organization) at Conf42 Cloud Native 2022.
