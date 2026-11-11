# Most of your app is other people's code - a first SCA talk

Conf42 Blog, 2021-12-01. https://www.conf42.com/blog/devsecops2021/sca-101-know-whats-inside-your-apps

In short: Magno Logan (Trend Micro) at Conf42 DevSecOps 2021 on software composition analysis, SBOMs and why open source dependencies are your biggest attack surface

If 70 to 90% of your application is open source, most of your attack surface is code your team never wrote. At Conf42 DevSecOps 2021, Magno Logan, Information Security Specialist at Trend Micro Research, gave a good first talk on software composition analysis (SCA): what it needs, what a software bill of materials is, why supply chain attacks made it urgent, and a short demo of finding a critical lodash vulnerability in OWASP Juice Shop.

It is billed as a 101 and it is one. If you already run Dependency-Track and argue about CycloneDX versus SPDX, skim the numbers and the reading list and move on.

## What does an SCA tool actually do?

SCA has had other names: library analysis, third-party dependency checks, open source security. Magno credits Gartner with the current term. The goal is governance, security and provenance for the open source you pull in: list every component and version, flag the outdated or vulnerable ones, and catch licence problems before legal does.

He breaks the inputs into three parts, the same across the major tools:

- **Application manifest**: how the software is meant to be built and run.
- **Dependency metadata**: which dependencies, at which versions.
- **Vulnerability data source**: a public or private database to compare against. The NVD is the common public one, and he warns it is usually not enough on its own.

## What is an SBOM?

A bill of materials for a chair lists the wood, foam and fabric and what they cost. A software bill of materials is the ingredients label on a packaged food: the components inside a piece of software. He points to three resources: CycloneDX, the lightweight SBOM standard that had just joined OWASP; SPDX, the Linux Foundation's open standard; and OWASP Dependency-Track, the lesser-known sibling of Dependency-Check, for tracking SBOMs and supply chain risk across an organization.

## Why should a developer care?

The numbers he cites from the Synopsys open source risk analysis report: 84% of codebases had at least one vulnerability, with an average of 158 per codebase, and the average number of open source components per application went from 84 in 2016 to 528 in 2020. Nobody tracks 528 components by hand.

The 70 to 90% figure comes from Mark Curphey, an OWASP founder and creator of SourceClear, now part of Veracode. "The attack surface of your application, it's much higher on the open source and on the third party code than on your custom code," Magno Logan said at Conf42 DevSecOps 2021. So keep doing SAST and DAST, but do not skip SCA.

Then the hard part: transitive dependencies. If the library you imported pulls in a vulnerable one, you often cannot upgrade it until your direct dependency does. Using components with known vulnerabilities sits in the OWASP Top 10 (A9 in 2017), and Equifax in 2017 is his reminder of what it costs: the entry point was a vulnerable Apache Struts 2 library.

## The whole pipeline is the supply chain

Libraries are one entry point. Source repos, build systems, artifact repositories and deployments are the others, and SolarWinds showed what a compromised build system does. Magno, part of the CNCF Security Technical Advisory Group, points to two free resources from that group's GitHub: a catalog of supply chain compromises from roughly the past decade, which he had recently updated, and the CNCF software supply chain security white paper. Trend Micro's own research looked at supply chain attacks on cloud development, such as online IDEs like AWS Cloud9, where your code lives somewhere you do not run. And the May 12, 2021 US executive order asks software sellers to the US government to maintain accurate, up-to-date provenance of their code and components.

## The demo

The tool list runs from free (OWASP Dependency-Check, mostly Java and .NET; Retire.js; Snyk, free for open source) to commercial (Trend Micro's Open Source Security, built in partnership with Snyk; Veracode SCA; Synopsys Black Duck). He demos Snyk inside Trend Micro Cloud One: connect GitHub, pick OWASP Juice Shop, and the scan reads package.json and flags a critical prototype pollution vulnerability in lodash with a CVSS score of 9.8, alongside the CVE, CWE, and fix advice. His caution on the fix: updating is the usual answer, but run regression tests so the upgrade does not break the app.

## Who should watch

Developers new to AppSec and teams about to roll out their first dependency scanner. It is a clear, well-sourced primer rather than new research.

## Related Conf42 talks

- Ciara Carey on [making SBOMs actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) at Conf42 DevSecOps 2022.
- Danish Tariq and Hassan Khan Yusufzai on [npm supply chain attacks](https://www.conf42.com/DevSecOps_2023_Danish_Tariq_Hassan_Khan_Yusufzai_supply_chain_npm_attacks) at Conf42 DevSecOps 2023.
- Sven Ruppert on [supply chain security for open source projects](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects) at Conf42 Cloud Native 2023.

[Watch Magno Logan's talk](https://www.conf42.com/DevSecOps_2021_Magno_Logan_software_composition_analysis_101) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Trend Micro

The talk shows Trend Micro Cloud One with Open Source Security, Trend Micro's dependency scanning built in partnership with Snyk.

- Trend Micro for business: [trendmicro.com](https://www.trendmicro.com/en_gb/business.html)
- Trend Micro research on supply chain attacks in the age of cloud computing: [trendmicro.com](https://www.trendmicro.com/vinfo/in/security/news/virtualization-and-cloud/supply-chain-attacks-cloud-computing)

[Watch the talk on YouTube](https://youtu.be/vqNviNKQWE8).

## Watch the talk

[Software Composition Analysis 101: Knowing what’s inside your apps](https://www.conf42.com/DevSecOps_2021_Magno_Logan_software_composition_analysis_101) at Conf42 DevSecOps 2021.
