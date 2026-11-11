# Conf42 Incident Management 2025: work the incident, not the tools

Conf42 Blog, 2025-10-03. https://www.conf42.com/blog/im2025/conf42-incident-management-2025-roundup

In short: Conf42 Incident Management 2025 roundup: Twilio on incident comms, AI for detection and RCA, incidents under HIPAA and GDPR, and the platforms underneath.

Conf42 Incident Management 2025 took place on October 2, 2025, with 22 talks about the moment something breaks and everything that decides how badly it goes. AI showed up in most of them, as a summariser, a detector, a root cause assistant and a tester, but the talk that stuck was about something older: telling people what is going on. The lineup is on the [event page](https://www.conf42.com/im2025) and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBU25vUS7hZWANfG6r4D4oK).

## Communication is the incident customers see

[Gandhi Mathi Nathan Kumar](https://www.conf42.com/Incident_Management_2025_Gandhi_Mathi_Nathan_Kumar_ai_automation_resilience), Principal Incident Commander at Twilio, chose incident communications because, as he put it, there is plenty of content on detection and resiliency and very little on how responders keep everyone informed. He walked through the tool stack a single Twilio incident touches: FireHydrant to declare and run it, PagerDuty to page, Zoom for the bridge, Slack for the asynchronous work where most incidents actually happen, Datadog, Atlassian Statuspage, Google Docs for retrospectives, Confluence and Slack canvases for action items.

His warning applies to any shop with that many tabs open: the trouble starts when "You end up working the tools instead of working the incident". From the customer's side, the status page is still green, nobody has told them anything, and support tickets start to flood in. He then demoed how AI can take on the updates and bring late joiners up to speed so the incident commander can keep the room focused on mitigation.

Two more talks looked at the screens responders stare at. [Priyanshi Deshwal](https://www.conf42.com/Incident_Management_2025_Priyanshi_Deshwal_visual_interfaces_intelligence) of Mode argued for AI-powered visual interfaces that replace static dashboards with real-time insight, and [Sujit Kumar](https://www.conf42.com/Incident_Management_2025_Sujit_Kumar_contactcenters_automation_scale), VP of Technology at Copart, covered contact centres built to stay calm and coordinated when incidents push call volume up.

## AI for detection and root cause, with receipts

[Mallikarjun Ramasani](https://www.conf42.com/Incident_Management_2025_Mallikarjun_Ramasani_intelligence_cloud_future) of Barclays surveyed ML-driven detection, root cause analysis and auto-remediation in cloud operations. [Vasanth Mudavatu](https://www.conf42.com/Incident_Management_2025_Vasanth_Mudavatu_transparency_algorithms_ai) of Dell Technologies asked the question every on-call engineer should ask of these tools: can you trust your AI during a breach? His answer was algorithmic transparency, so responders can see why the model flagged something before they act on it.

[Pushap Goyal](https://www.conf42.com/Incident_Management_2025_Pushap_Goyal_graph_spanner_security) of Google showed Spanner Graph tracing security incidents across distributed systems, turning scattered events into a connected attack story. [Mahmood Nawaz](https://www.conf42.com/Incident_Management_2025_Mahmood_Nawaz_knowledge_cloud_resilience) of LTIMindtree focused on knowledge systems that turn each incident into something the next responder can find, which is the part of the postmortem that usually goes missing.

## When the regulator is on the other line

[Nisheedh Raveendran](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr), Senior Staff Engineer at LinkedIn, opened with three short sentences every compliance-adjacent engineer will recognise: system down, regulators calling, patients waiting. His talk covered why normal incident response fails when HIPAA, GDPR or the EU's Digital Markets Act are in play, and the playbooks that work instead.

[Nirup Baer](https://www.conf42.com/Incident_Management_2025_Nirup_Baer_finance_modernization_resilience) of Wells Fargo looked at how financial firms embed compliance into cloud architecture so resilience and speed don't trade off against each other. In healthcare, [Sreenivasul Reddy Meegada](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security) drew on deployments of NICE and Omilia voice biometrics to tighten security without slowing patient workflows.

## The platforms underneath the incident

A good chunk of the day was about systems that shouldn't need an incident commander in the first place. [Sruthi Erra Hareram](https://www.conf42.com/Incident_Management_2025_Sruthi_Erra_Hareram_databricks_analytics_reliability) presented a cross-cloud analytics pipeline on Azure Databricks and AWS built with incident-aware orchestration. [Adithya Sirimalla](https://www.conf42.com/Incident_Management_2025_Adithya_Sirimalla_multicloud_databases_resilience) of Enliven Technologies covered running Oracle and SQL Server across AWS, Azure and OCI with automation, monitoring and disaster recovery. [Vijaykumar Pasunoori](https://www.conf42.com/Incident_Management_2025_Vijaykumar_Pasunoori_apigateways_microservices_serverless) of Valet Living made API gateways part of detection and recovery, and [Rehana Sultana Khan](https://www.conf42.com/Incident_Management_2025_Rehana_Sultana_Khan_ratelimiting_api_protection) of Versa Networks showed AI-driven rate limiting that adapts to malicious traffic instead of relying on fixed thresholds.

## Preventing the next one

Prevention got its own track of sorts. [Vijay Kumar Kola](https://www.conf42.com/Incident_Management_2025_Vijay_Kumar_Kola_sap_salesforce_testing) of Intuitive used AI-powered testing to catch SAP and Salesforce failures before production, [Gobinath Kasimayan](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility) of Deloitte Consulting treated SAP master data governance as an incident prevention tool, and [Krishna Chaitanya Yarlagadda](https://www.conf42.com/Incident_Management_2025_Krishna_Chaitanya_Yarlagadda_supplychain_automation_prevention) of Mercury Financial applied anomaly detection to supply chain disruptions that cascade into incidents within hours.

## Sponsors

Thanks to [SREday](https://www.sreday.com/), our gold sponsor, to [StarterAI](https://www.starterai.dev/) for the newsletter and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

All 22 talks are linked from the [Conf42 Incident Management 2025 page](https://www.conf42.com/im2025). Next in the series is [Conf42 Kube Native 2025](https://www.conf42.com/kubenative2025) on October 16, and the reliability conversation picks up again at [Conf42 SRE 2026](https://www.conf42.com/sre2026) on March 19, 2026. Meanwhile, check whether your status page knows about your last incident.
