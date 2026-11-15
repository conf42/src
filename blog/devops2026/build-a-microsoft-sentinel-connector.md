# Extending Microsoft Sentinel with your own codeless connector

Conf42 Blog, 2026-01-20. https://www.conf42.com/blog/devops2026/build-a-microsoft-sentinel-connector

In short: Gareth Emslie of Dynatrace at Conf42 DevOps 2026 builds a Microsoft Sentinel solution with a codeless connector, KQL analytics rules and packaging.

If the SIEM your security team lives in doesn't know about your tool, you can teach it. At Conf42 DevOps 2026, [Gareth Emslie](https://www.conf42.com/DevOps_2026_Gareth_Emslie_sentinel_security_automation), Senior Product Manager and Tech Evangelist at Dynatrace, showed how to extend Microsoft Sentinel end to end: a Codeless Connector Framework data connector that polls a REST API, data collection rules that shape the data on ingest, KQL analytics rules that raise incidents, and the packaging that turns it all into a Content Hub solution.

The worked example is Dynatrace's own Sentinel solution, which pulls attacks detected by Dynatrace Runtime Application Protection, so this is a vendor's integration used as a tutorial. The steps apply to any product with a REST API, and the demo is detailed enough to follow along.

## Why a DevOps engineer should care about the SOC's tools

Emslie opens with the pressure on security operations: data breaches at a record high in the Identity Theft Resource Center's 2023 report, human error behind most of them, and SOC teams buried in alerts from fragmented tools. He also cites a Threat Stack report in which 52% of companies admitted cutting security corners to hit deadlines. His argument is that speed and security aren't mutually exclusive, and that DevOps people are well placed to build the automation that connects the two.

Sentinel is the stage for that: analytics rules for detection, SOAR-style playbooks and automation rules for response, hunting queries grouped by MITRE ATT&CK tactics, and a Content Hub where partners publish connectors and solutions.

## Pick the connector type that doesn't bill your customer

There are three ways to build a connector that calls a REST API. Logic Apps give you a what-you-see-is-what-you-get interface, and Azure Functions give you full code, but both deploy extra Azure resources into the customer's environment. The Codeless Connector Framework (CCF) has more limited REST support, but Microsoft hosts and runs it, so the customer deploys nothing. That's why he recommends CCF.

Data then goes through data collection rules at ingest: a KQL transformation filters, enriches and restructures the raw JSON into a defined table schema (the custom table keeps its `_CL` suffix, and `TimeGenerated` is required). At query time, ASIM parsers normalise data from different sources into one schema. He reminds viewers that billing follows the volume of data analysed and stored, which is a good reason to filter at ingest.

## The demo, file by file

The live part works in Microsoft's public Azure-Sentinel GitHub repository, where every solution lives under `Solutions/<Vendor>`. Emslie walks through the files a CCF connector needs:

- the data collection rule, with table schema, destinations and the transformation query;
- the polling configuration: endpoint URL built from the customer's environment URL, HTTP method, retries, time format for the start and end query window, headers, where the data sits in the JSON response (an attacks array here), and `nextPageKey` token paging;
- the table definition with typed fields and no type suffixes;
- the connector definition that drives the portal UI, with publisher, sample queries, permissions, prerequisites such as an access token, and a connect toggle.

He adds an analytics rule template in YAML: query frequency and period, MITRE tactics and techniques, a KQL query for attacks that aren't allow-listed, a custom alert name built from Dynatrace fields, incident creation, and grouping of alerts over seven days when entities match. In the portal, he creates a rule from that template, tweaking severity, entity mapping for IPs and hostnames, schedule and threshold.

## Package it, or side-load it to test

Packaging uses a PowerShell script from the repo's tools folder, `createSolutionV3`, which produces a versioned zip for Microsoft Partner Center plus an ARM template and UI definition. That ARM template is the handy bit: deploy it as a custom template in your own subscription to test the solution without publishing, which is how he ran the demo.

## Who should watch

DevOps and platform engineers who own an internal tool or product that the security team wants inside Sentinel, and anyone writing their first CCF connector. It's long and detailed, so keep the Azure-Sentinel repo open alongside it.

## Related Conf42 talks

- [Azure Attacks Unpacked: Real-World Threats and Lessons Learned](https://www.conf42.com/Cloud_Native_2026_Aleksandra_Drobnjak_security_zerotrust_encryption) by Aleksandra Drobnjak at Conf42 Cloud Native 2026.
- [Synergizing Threat-Informed Defense: When Cloud Attack Emulation Meets Detection Engineering](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense) by Kennedy Torkura at Conf42 Cloud Native 2024.
- [Runtime Kubernetes Security: Hands-On Threat Detection with Falcosidekick](https://www.conf42.com/Kube_Native_2024_Aleksandra_Drobnjak_kubernetes_security_falcosidekick_threat_detection) by Aleksandra Drobnjak at Conf42 Kube Native 2024.

[Watch Gareth Emslie's talk](https://www.conf42.com/DevOps_2026_Gareth_Emslie_sentinel_security_automation) or the [YouTube recording](https://youtu.be/pOvWKjPAxHA).

## Watch the talk

[From Zero to a DevSecOps Hero: Extending Microsoft Sentinel](https://www.conf42.com/DevOps_2026_Gareth_Emslie_sentinel_security_automation) at Conf42 DevOps 2026.
