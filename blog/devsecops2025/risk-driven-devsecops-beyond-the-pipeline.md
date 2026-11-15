# Risk-driven DevSecOps starts outside the CI/CD pipeline

Conf42 Blog, 2025-11-19, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/risk-driven-devsecops-beyond-the-pipeline

In short: Nishanth Sirikonda at Conf42 DevSecOps 2025 on ranking security work by business impact and mapping the SaaS, identity and API layers pipelines never see.

Most DevSecOps programmes guard the pipeline and call it a day, while the real exposure sits in a SaaS admin console nobody scans. At Conf42 DevSecOps 2025, [Nishanth Sirikonda](https://www.conf42.com/DevSecOps_2025_Nishanth_Sirikonda_risk_secure_system), a Workday solutions architect at First Day Foundation, argued for risk-driven DevSecOps: find the assets that would hurt most if they failed, protect those first, and let risk decide where the automation goes.

It's a short, slide-driven talk, closer to a playbook than a war story. That makes it a good fit for anyone who has to explain to a steering committee why the security backlog is ordered the way it is.

## The pipeline is a small part of the attack surface

Sirikonda's starting complaint is about scope. Classic DevSecOps concentrates on CI/CD: scanning, gating, blocking releases. The gaps he lists are everywhere else. SaaS platforms, identity and access management, and the integration layer between systems mostly live outside any pipeline, so they never get the scanner's attention.

He adds two more failure modes. Security turns into a downstream checkpoint instead of a design principle, and findings arrive scattered across tools with no central view of risk, so nobody can say which fix matters most. His summary line is the old one, and it still holds: you cannot protect what you cannot see.

So step one is a map of the whole ecosystem. He names four layers to cover: cloud misconfigurations (storage buckets, network rules, encryption settings, resource permissions), third-party risk (API connections, vendor access, data sharing), identity surfaces (service accounts, grants, privilege escalation paths), and the data flows and dependencies that tie systems together.

## Compliance as a continuous signal, not an audit season

The second idea is to stop treating compliance as an annual event. Sirikonda describes three moves: set baselines and guardrails for the usual failure points across cloud, SaaS, identity and API configuration; run automated policy checks continuously so drift gets caught when it happens instead of at the next audit; and feed the results back into engineering decisions.

His key point is that monitoring here is a discipline, not a shopping list. More tools don't help if nobody runs validation as a routine operational practice. Anyone who has inherited three overlapping CSPM dashboards will recognise the problem.

Inside the pipeline he keeps it practical: automate early checks in developer workflows, audit and update third-party dependencies consistently, and hold custom scripts and integration glue to the same security standard as product code. That glue is often where the shortcuts live.

## Least privilege is a boring superpower

The access governance section is the most concrete. Sirikonda wants RBAC roles that map to real job responsibilities rather than generic templates, regular reviews that keep permissions in line with current duties, conditional access (device health, location, risk signals, behaviour) as the default rather than an exception, and tamper-evident audit logs. He frames audit data as a strategic asset: it supports accountability and tells you where to improve.

## Speak in business impact, report in risk metrics

The last part is about getting leadership to care. Translate findings into revenue loss, compliance violations and reputational damage instead of raw CVE identifiers, plug DevSecOps into the existing enterprise risk framework and board reporting, and track metrics executives understand: mean time to remediate critical exposures, attack surface reduction, control effectiveness.

He closes with a cadence: quarterly security reviews, annual API penetration tests, a seven-day target for remediating critical risks, SCA and SAST in CI/CD that halt critical flaws, policy as code and configuration as code with auto-fixes, plus monthly risk meetings and leadership dashboards. Treat those as his suggested targets, not results from a measured rollout.

## Who should watch

Security leads and platform owners building a risk register, and architects who own SaaS-heavy estates (Workday, CRM, ITSM) where the pipeline tooling stops at the API boundary. If you want deep tooling demos, this isn't that talk. If you need a framework to argue priorities with, it's a quick watch.

## Related Conf42 talks

- [Securing the software supply chain: beyond SBOM](https://www.conf42.com/DevSecOps_2023_Marek_Najmajer_Aleksander_Baranowski_beyond_sbom_risk_assessment) turns vulnerability findings into risk assessment.
- [AI-Driven Risk-Aware Decision-Making for Scalable Reliability Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Oreoluwa_Omoike_driven_risk_aware) brings the same risk lens to reliability work.
- [Cloud MCP Servers Under Fire](https://www.conf42.com/Cloud_Native_2026_Aleksandr_Pinaev_security_vulnerabilities_compliance) looks at a newer integration layer that pipelines rarely cover.

[Watch Nishanth Sirikonda's talk](https://www.conf42.com/DevSecOps_2025_Nishanth_Sirikonda_risk_secure_system)

[Watch the talk on YouTube](https://youtu.be/nvq6a3Vnygw).

## Watch the talk

[Building Unbreakable Systems: Risk-Driven DevSecOps in Action](https://www.conf42.com/DevSecOps_2025_Nishanth_Sirikonda_risk_secure_system) at Conf42 DevSecOps 2025.
