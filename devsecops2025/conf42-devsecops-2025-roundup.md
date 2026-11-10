# Conf42 DevSecOps 2025: securing pipelines that AI now writes into

Conf42 Blog, 2025-12-05. https://www.conf42.com/devsecops2025/conf42-devsecops-2025-roundup

In short: Conf42 DevSecOps 2025 roundup: 26 talks on AI in the delivery pipeline, SBOMs and provenance, safer deployments and security in finance and healthcare.

Conf42 DevSecOps 2025 ran on December 4, 2025, with 26 talks and one question underneath most of them: what happens to security when AI writes code, generates configuration and makes decisions inside the pipeline? Speakers from Harness, AT&T, Chevron, JPMorganChase, Microsoft, Dropbox, Cisco and others answered from the pipeline, the supply chain and some of the most regulated industries around. Everything is on the [event page](https://www.conf42.com/devsecops2025), and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCMXkZdQESvj8M_clmevDME).

## AI is in the pipeline, so secure the pipeline

Harness's keynote from [Dewan Ahmed](https://www.conf42.com/DevSecOps_2025_Dewan_Ahmed_secure_ai_delivery), Principal Developer Advocate, set the tone. Pipelines automate whatever you feed them, and AI makes them faster at shipping mistakes as well as good code. His framework for secure-by-default delivery has four pillars: contextual intelligence about what a change means, automatic verification of provenance and drift, behaviour-based anomaly detection, and continuous learning from every deploy and rollback.

Others took the same problem from different angles. [Rajkumar Sukumar](https://www.conf42.com/DevSecOps_2025_Rajkumar_Sukumar_ai_ml_ethics) of AT&T showed how to embed security, privacy-aware training, policy as code and audit-ready steps into machine learning pipelines. [Baradwaj Bandi Sudakara](https://www.conf42.com/DevSecOps_2025_Baradwaj_Bandi_Sudakara_ai_ml_secure) of Ascension Health covered AI-driven testing and defect prevention. [Alex Shershebnev](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure) of Zencoder demonstrated MCP workflows that let an LLM trigger CI jobs, query Grafana or debug from Sentry inside the IDE, and the risks to check before plugging that into your stack. [Murali Koney](https://www.conf42.com/DevSecOps_2025_Murali_Koney_ai_risk_llm) of Cox Automotive tied LLM adoption to governance, risk and cost, starting from his observation that most enterprise AI projects fail before production.

## Supply chain: know what you ship

[Bhaskar Bharat Sawant](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci) of Cornerstone Building Brands gave the most hands-on supply chain session: automated SBOMs, SLSA provenance and attestations, hermetic builds and artifact verification at deploy time, so every release is traceable by default. [Gresshma Atluri](https://www.conf42.com/DevSecOps_2025_Gresshma_Atluri_supply_chain_threats) of Chevron built a proactive defence framework from real-world supply chain incidents.

For teams starting closer to the code, [Peter De Tender](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql) of Microsoft toured GitHub Dependabot, CodeQL and the other built-in security features, and [Safeer C M](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep) of MoEngage explained how static analysis actually works using open-source Semgrep. Together they make a good afternoon for anyone whose SAST stage is a box nobody opens.

## Deploying without seeing red

[Rayenn Hamrouni](https://www.conf42.com/DevSecOps_2025_Rayenn_Hamrouni_deployments_aws) of Lenstra had the best title of the day, "From Blue to Green Without Seeing Red", and a real case study behind it: implementing blue/green deployment for a web application on AWS using Lambda@Edge, with the trade-offs spelled out. [Meenu Venkataarangam](https://www.conf42.com/DevSecOps_2025_Meenu_Venkataarangam_migration_cloud_auto) of Recode Solutions covered automation for enterprise migrations that closes security gaps along the way, and [Nishanth Sirikonda](https://www.conf42.com/DevSecOps_2025_Nishanth_Sirikonda_risk_secure_system) of First Day Foundation argued for risk-driven DevSecOps with compliance as code. [Raghavendra Reddy Kapu](https://www.conf42.com/DevSecOps_2025_Raghavendra_Reddy_Kapu_resilient_system_secure) brought fault-tolerance patterns and chaos engineering into the security conversation.

## Where the stakes are regulated

Finance had its own track. [Swamy Biru](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai) of JPMorganChase covered DevSecOps patterns for RAG and agentic systems in financial operations, [Janardhan Chejarla](https://www.conf42.com/DevSecOps_2025_Janardhan_Chejarla_trading_cloud_scale) of Calypso Technology secured event-driven order management for high-frequency trading, and [Silpa Potluri](https://www.conf42.com/DevSecOps_2025_Silpa_Potluri_payment_api_secure) of GoodLeap described keeping PCI compliance while moving a payment gateway to microservices with daily releases.

Healthcare and education followed. [Mahendar Ramidi](https://www.conf42.com/DevSecOps_2025_Mahendar_Ramidi_health_cloud_scale) of the Maryland Health Benefits Exchange shared how he built a HIPAA-compliant mobile platform for cancer patients with zero-trust architecture and compliance automation, and [Raghav Sai Cheedalla](https://www.conf42.com/DevSecOps_2025_Raghav_Sai_Cheedalla_ai_ethics_edu) of Meta looked at secure, ethical personalisation of learning for students with special needs. [Mallikarjun Bussa](https://www.conf42.com/DevSecOps_2025_Mallikarjun_Bussa_data_access_secure) of Dropbox addressed self-service BI that doesn't leak data.

## People are part of the system

Two talks were about the humans who run all of this. [Kuldeep Deshwal](https://www.conf42.com/DevSecOps_2025_Kuldeep_Deshwal_culture_teams_secure), Director of Engineering at Proofpoint, unpacked the productivity paradox in DevSecOps culture and how to avoid burning out the people expected to ship securely. [Sanjeevani Bhardwaj](https://www.conf42.com/DevSecOps_2025_Sanjeevani_Bhardwaj_health_secure_cloud) of Salesforce proposed a four-dimension technical health index to move teams from reactive to proactive security work. On the infrastructure side, [Nazim Khan](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra) of Cisco explained how Ethernet with RoCEv2 and Ultra Ethernet standards competes with InfiniBand for AI training networks.

## Sponsors

Thanks to [Harness](https://www.harness.io/), our diamond sponsor, to [SREday](https://www.sreday.com/) as gold sponsor, to [StarterAI](https://www.starterai.dev/) for the newsletter and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

All 26 talks are linked from the [Conf42 DevSecOps 2025 page](https://www.conf42.com/devsecops2025). The next edition, [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026), is set for October 1, 2026. Plenty of time to make the security stage the one that can't be skipped.
