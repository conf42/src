# Conf42 DevSecOps 2026 roundup: checking agents before they act

Conf42 Blog, 2026-10-02. https://www.conf42.com/devsecops2026/devsecops-2026-roundup-agents-at-the-gate

In short: Conf42 DevSecOps 2026 in review, from hooks that gate coding agents and SBOMs that stop at the model to cell isolation, masking checks and safe recovery.

[Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026) ran online on October 1, 2026, with 24 talks, and one question kept coming back: what happens to security controls built for a human pace when the code is written, installed and shipped by agents? Speakers from Harness, ArmorCode, Keeper Security, WSO2, SAP, Microsoft, Tesla, T-Mobile and AWS answered it from different corners: before the tool call, inside the artifact, at the tenant boundary, in the test data and during recovery.

## Put the check before the action, not after the alert

The busiest track was about coding agents, and its speakers converged on timing. [Artemis Leonardou](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) (NOFire AI) described an incident where the alerting worked exactly as designed and was still useless, because it reported something that had already broken. Humans hesitate before acting; agents don't. The talk is about evaluating an action before it executes, using the pipeline you already have.

[Karan Bansal](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) (ArmorCode) made hooks the enforcement layer: they intercept every tool call between the agent's decision and its execution and run outside the model, so prompt injection can't talk its way past them. His blocking scripts cover dangerous commands, secret exfiltration, typosquatted installs and agents that mark failing tests as skipped to fake a green build. [Oleksandr Kryvchenko](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) (Keeper Security) showed why that matters: Claude Code's `permissions.deny` rules can be silently bypassed, and PreToolUse hooks put policy in your own code instead of the model's.

[Yunhao Jiao](https://www.conf42.com/DevSecOps_2026_Yunhao_Jiao_aicoding_verification_gates) (TestSprite) brought numbers from CoderCup, a public competition where four frontier coding agents built the same ten-phase app. Every agent broke previously working features between 31 and 57 times in a single build, and the breaks stayed invisible until something ran the application. His argument: the PR gate is too late, so verify while the agent works. [Deepanshu Kukreja](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) looked at the other side, using agents to automate DevSecOps chores across IaC, CI/CD and incident response.

## The supply chain now includes weights, memory and RAG

The keynote from [Roshan Piyush](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security), Head of Security Research at Harness, traced supply chain attacks from SolarWinds and XZ Utils to Shai-Hulud, then argued that agent configuration (hooks, skills, CLAUDE.md files, memory, MCP servers) is where the trust has moved. He ran a discovery script on his own laptop and found more than a thousand agent artifacts, half of them unknown to him.

[Emmy Eide](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain) (Realign Labs) went after the artifact itself. DevSecOps got good at proving what's in a build, but a model-bearing service ships a multi-gigabyte blob that no scanner parses and no SBOM format meaningfully describes. The talk maps which gates still fire and which wave through what they can't inspect. [Jayakumar Ramalingam](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) (SiriusXM) covered APIs where a single request can now trigger inference, retrieve user context and call downstream tools. [Ananda Kumar Dey](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) (Quadrant Technologies) and [Sirisha Ayyagari](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing) applied the same thinking to enterprise RAG and to AI-driven pricing inside SAP.

## Isolation and identity, without long-lived secrets

[Lahiru De Silva](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) (WSO2) gave one of the most concrete talks of the day. Namespaces and NetworkPolicies stop accidents, not a determined neighbour, so OpenChoreo, a CNCF Sandbox internal developer platform, gives each tenant environment its own cell: a namespace with a Cilium policy boundary, its own observability scope, and four directional gateways (northbound, westbound, southbound, eastbound) built on Envoy and the Kubernetes Gateway API.

[Venkata Velavarthipati](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) removed stored credentials from multi-cloud pipelines with OpenID Connect and workload identity federation. [Perumalsamy Ravindran](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) covered Terraform across providers, [Sonu Kumar](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai) (Peoplefluent) governed platform engineering, and [Rahul Kizhakkepachilamakol](https://www.conf42.com/DevSecOps_2026_Rahul_Kizhakkepachilamakol_distributedsystems_vulnerabilities_latency) (AWS) the anti-entropy mechanisms that keep vulnerability findings flowing within minutes at cloud scale, where every minute of delay widens the exposure window.

## Test your detection and your recovery, not just your build

[Aleksander Kryukov](https://www.conf42.com/DevSecOps_2026_Aleksander_Kryukov_detection_exploits_simulation) asked whether your alert would have fired in time, then answered it with a harness that replays candidate detection rules against 46 historical Web3 exploits using state-forked execution. Detection deadlines come from observed exfiltration curves, not arbitrary SLAs. [Sanjay Iyer](https://www.conf42.com/DevSecOps_2026_Sanjay_Iyer_recovery_eventdriven_rto) made a point that deserves more airtime: a recovery can meet RTO and RPO and still replay duplicate transactions past fraud controls or restore stale permissions. [Mridula Chilakamarri](https://www.conf42.com/DevSecOps_2026_Mridula_Chilakamarri_kubernetes_opentelemetry_diagnostics) (Dell Technologies) built deterministic request-level diagnostics on OpenTelemetry and W3C Trace Context.

## Data, privacy and the browser

[Siyuan Feng](https://www.conf42.com/DevSecOps_2026_Siyuan_Feng_datamasking_testdata_validation) (CSC) tackled a problem every test-data team hits: validating masking when legacy tables have no stable keys. The trick is to intersect sensitive values first and build composite identifiers only for the overlapping subset. [Mary Sirisha Duggimpudi](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) (T-Mobile) covered AI-driven sensitive data discovery, [Vinay Puri](https://www.conf42.com/DevSecOps_2026_Vinay_Puri_ml_compliance_monitoring) (Amazon) ML-based compliance monitoring, and [Ashwin Kumar](https://www.conf42.com/DevSecOps_2026_Ashwin_Kumar_mobile_authorization_identity) (Tesla) identity binding for executives reading analytics on unmanaged phones.

Two talks stayed close to the pipeline. [Elena Darevskaya](https://www.conf42.com/DevSecOps_2026_Elena_Darevskaya_csp_browser_javascript) (SAP) showed how a customer's Content Security Policy or COOP headers break an embedded SDK that worked fine in development, and how to catch it earlier. [Peter De Tender](https://www.conf42.com/DevSecOps_2026_Peter_De_Tender_github_codescanning_sast) (Microsoft) walked through what GitHub Advanced Security covers out of the box.

## Sponsors and where to watch

Thanks to [Harness](https://www.harness.io/) and [SREday](https://www.sreday.com/), the event's diamond sponsors, to [HockeyStick](https://www.hockeystick.show/) as podcast partner, and to the media partners who spread the word. Every talk is on the [Conf42 DevSecOps 2026 playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCZ8u5VHJAm9eOB9KJTCZT8) and linked from the [event page](https://www.conf42.com/devsecops2026).

The series continues with [Conf42 DevSecOps 2027](https://www.conf42.com/devsecops2027). If this year is a guide, expect the agent track to get bigger.
