# Rushed cloud migrations skipped the boring security settings

Conf42 Blog, 2022-01-28. https://www.conf42.com/blog/python2022/cloud-security-basics-teams-skip

In short: Radu Vunvulea (Endava) at Conf42 Python 2022 on the simple Azure security fixes rushed pandemic migrations skipped, from preview features to RBAC

The pandemic compressed three-year cloud plans into one financial year, and the security settings were the first thing to slip. At Conf42 Python 2022, Radu Vunvulea, Group Head of Cloud Delivery at Endava, walked through the fixes he sees teams forget most often, mostly in Azure terms: stay off preview features in production, stop using master keys, scope access with RBAC, keep default protections switched on, and actually read the logs.

His framing: most organisations that rushed are now running in the cloud with enough time and budget to consolidate, which makes it the moment to go back and review.

## Why does he call COVID-19 a catalyst?

He opens with the figures he cites for the period: 48% of organisations accelerating cloud migration, a 250% rise in cyber attacks in the EU over twelve months, and phishing up 45% with people working from home. He adds a story from that morning's spam folder, a PayPal lockout email arriving two days after a real PayPal payment had tripped his card's fraud check, to show how plausible these scams get.

Then the developer scenario. A dev hero keeps the full Azure storage account key in a private infrastructure repo, on a well-secured laptop they also use for personal things. Malware lifts their Windows credentials, and with them the repo and the key, and from there every environment that key opens, customer data included. "Developers should never have access directly for long periods of time on environments, testing or pre production where customer data are used or sensitive data," Radu Vunvulea said at Conf42 Python 2022. Temporary access, an hour or two, is fine; forgetting to revoke it is not.

## What are the forgotten basics?

**Keep preview features out of production.** Azure services and features move through private preview (no SLA, no formal support), public preview (some support, no SLA) and general availability. With sensitive customer data, his rule is to use only general availability services. He points to the Cosmos DB security issue of August 2021, which hit a feature still in public preview. The service list in the portal tags previews, but individual features inside a service are trickier, especially for teams writing ARM templates; each service's docs list its preview features.

**Educate everyone, not just IT.** HR and finance touch cloud services too. Free foundation-level material, the content behind Azure Fundamentals or AWS Cloud Practitioner, gives people the basics in four or five hours.

**Stop using master keys.** Prefer identity-based access between services, managed identities and service principals, and scoped shared access signatures for third parties. Scan repositories for secrets before push and in nightly runs; reject commits that contain them, fail the build, freeze the pipeline, and ideally rotate the exposed credentials automatically.

**Use RBAC properly.** An Azure role assignment ties a security principal (user, group or managed identity) to a role and a scope (subscription, resource group or single resource). Assign to groups, not individuals, segregate duties inside teams, and prune leftover access from old projects.

**Lock down endpoints.** Firewall rules on storage and compute, at least an IP allow list, and a web application firewall such as the one on Azure Application Gateway for OWASP-style attacks.

## How do you know it is working?

Leave default security features on even when they are annoying; cost in time and money is the most common reason recommendations go unimplemented, he says. Use Azure Security Center even on the free tier for its secure score and recommendations, with Azure Defender as the premium layer, and Azure Advisor for cost and reliability advice. Keep and review the activity log of configuration changes and your application logs, stored securely. For the bigger picture he points to Microsoft's Cloud Adoption Framework and the Well-Architected Framework.

The abstract promises a demo-heavy session; the talk is mostly slides and advice, with a brief look at Security Center.

## Who should watch

Teams that migrated to Azure in a hurry and never went back to harden it, and anyone who needs a checklist of low-effort, high-value cloud security fixes. AWS and GCP users will recognise most of it, with different product names.

## Related Conf42 talks

- Joshua Arvin Lat on [pragmatic security automation in the cloud with Python](https://www.conf42.com/Python_2022_Joshua_Arvin_Lat_pragmatic_security_automation_cloud), from the same event.
- Ashish Rajan on [cloud security assessments](https://www.conf42.com/Cloud_Native_2021_Ashish_Rajan_Cloud_Security_Assessments_in_2021) at Conf42 Cloud Native 2021.
- David Melamed on [minimum viable security for Python apps](https://www.conf42.com/Python_2022_David_Melamed_minimum_viable_security_applications).

[Watch Radu Vunvulea's talk](https://www.conf42.com/Python_2022_Radu_Vunvulea_covid19_cloud_security_catalyst) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From Endava

Endava is a technology services company working on digital transformation and cloud delivery.

- Endava: [endava.com](https://www.endava.com/)

[Watch the talk on YouTube](https://youtu.be/YXE_iLR8If8).

## Watch the talk

[COVID-19 is a cloud security catalyst](https://www.conf42.com/Python_2022_Radu_Vunvulea_covid19_cloud_security_catalyst) at Conf42 Python 2022.
