# An SBOM only matters when it can quarantine something

Conf42 Blog, 2022-11-30. https://www.conf42.com/blog/devsecops2022/sbom-to-quarantine-syft-grype-cosign

In short: Ciara Carey (Cloudsmith) at Conf42 DevSecOps 2022 on when to generate SBOMs, where to host them, and a Syft, Grype and cosign workflow that quarantines images

A software bill of materials that sits in a folder is paperwork. Ciara Carey, who works in developer relations at [Cloudsmith](https://cloudsmith.com/?utm_source=conf_42&utm_medium=referral&utm_content=cloudsmith_homepage&utm_campaign=conf_42_python_event), used her Conf42 DevSecOps 2022 talk to explain what SBOMs are, the trade-offs of generating them at each stage of the lifecycle, and a container workflow where a vulnerability scan of the signed SBOM automatically quarantines the image.

It is a clear primer that ends in a working pipeline, built mostly from open source tools.

## Why did SBOMs suddenly matter?

Carey starts with the supply chain: source code, scripts, IDE plugins, CI/CD, package managers, artifact repositories, and above all third-party dependencies, most of them open source. A conservative estimate, she says, is that over 80% of software contains open source.

Attacks come through how you consume it (dependency confusion, typosquatting on public registries such as Maven Central, PyPI and npm), but the most common source is critical vulnerabilities. She cites a Palo Alto Networks incident response analysis of over 600 incidents: software vulnerabilities were the suspected initial access vector in 31% of cases, second only to phishing, and Log4Shell was the most used open source vulnerability despite only becoming public that December. Heartbleed, patched in 2014, was still exploitable in research from 2020. The long tail comes from abandoned packages, patching not being a priority, and not knowing you are exposed through a dependency of a dependency.

Policy followed. After SolarWinds, the US executive order required organisations selling to the federal government to provide SBOMs and asked the NTIA for minimum elements. After Log4Shell, a White House summit produced a ten-point plan with backing from big tech, one point being SBOMs everywhere, and the EU's Cyber Resilience Act mentioned SBOMs for the first time.

## What is in an SBOM?

Every component of a product, including transitive dependencies, with names, versions and suppliers, in a standard machine-readable format so automation can act on it. The two standards are SPDX, which leans towards licensing, and CycloneDX, which leans towards vulnerability management.

"So sboms, at their core, answers the question, what is in my software?" Ciara Carey said at Conf42 DevSecOps 2022.

## When should you generate one?

Each stage has a catch:

- **Source code**: early and very shift-left, but often inaccurate on versions and may miss transitive dependencies.
- **Build time**: the NTIA's recommended point, with tooling such as the CycloneDX and SPDX generators, but not much of it.
- **Built artifact**: sometimes the only option for a legacy binary, but less accurate.
- **Container image**: the most mature workflows, with Anchore's Syft and Aqua's Trivy; accurate, but slower, later in the lifecycle, and weaker for software installed outside package managers.
- **Runtime**: tools like jbom for Java report what is actually running. That matters because, she says, less than 10% of listed components are actually exploitable.

Her wish is a generator combining the accuracy of one with the exploitability insight of another. It does not exist yet.

## Where do you store SBOMs, and what do the scores mean?

For container images, Sigstore's cosign signs images and attaches SBOMs and attestations to them, which Cloudsmith integrates with. For non-OCI packages such as Maven, RubyGems or npm, she admits the best practice is not yet understood.

She also gives a short vulnerability vocabulary: CVE IDs, CVSS scores from one to ten (Log4Shell got a ten for easy remote code execution in very common software), EPSS for predicted likelihood of exploitation, the National Vulnerability Database, and ecosystem advisories (GitHub, PyPI, Rust) that often publish before a CVE exists. VEX, the companion standard for stating whether a component is actually exploitable, is promising but barely used in the wild.

## What does the actionable workflow look like?

The demo pushes a Ruby container image to a Cloudsmith repository, then:

1. Generates a cosign key pair and signs the image, which adds the signature as a layer.
2. Generates an SPDX SBOM with Syft.
3. Attaches the SBOM to the image with cosign, signed as well, and verifies it with the public key.
4. Extracts the SBOM payload with jq and scans it with Grype, producing a vulnerability JSON that can be attached as another attestation.
5. If Grype fails on vulnerabilities above a threshold, quarantines the image with the Cloudsmith CLI, so it can no longer be downloaded or deployed.

Step five is the point of the talk. The rest of the pipeline exists so that step can happen without a human.

## Who should watch

Engineers asked to produce SBOMs for a customer or regulator who want to know which stage to generate them at, and security teams looking for a first automated gate. The future, she says, is mostly better tooling and workflows.

## Related Conf42 talks

- Marek Najmajer and Aleksander Baranowski on [risk assessment beyond the SBOM](https://www.conf42.com/DevSecOps_2023_Marek_Najmajer_Aleksander_Baranowski_beyond_sbom_risk_assessment) at Conf42 DevSecOps 2023.
- Danish Tariq and Hassan Khan Yusufzai on [npm supply chain attacks](https://www.conf42.com/DevSecOps_2023_Danish_Tariq_Hassan_Khan_Yusufzai_supply_chain_npm_attacks) at Conf42 DevSecOps 2023.
- Sven Ruppert on [supply chain security for open source projects](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects) at Conf42 Cloud Native 2023.

[Watch Ciara Carey's talk](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable)

## From Cloudsmith

Cloudsmith is a cloud-native artifact repository: 28+ package formats in one place, with multi-format repositories you can organise per environment, project or format.

- [Cloudsmith website](https://cloudsmith.com/?utm_source=conf_42&utm_medium=referral&utm_content=cloudsmith_homepage&utm_campaign=conf_42_python_event)
- [Start a 14-day trial](https://cloudsmith.io/user/signup/?utm_campaign=20221201-conf42-devsecops&utm_medium=conference&utm_source=virtual-booth)
- [How to manage package promotion workflows with Cloudsmith](https://cloudsmith.com/blog/how-to-manage-your-package-promotion-workflows-with-cloudsmith/)
- [O'Reilly report: The Rise of Continuous Packaging](https://cloudsmith.com/developers/resources/the-rise-of-continuous-packaging/)

[Watch the talk on YouTube](https://youtu.be/LVSHkqXtETU).

## Watch the talk

[Making Software Bill of Materials (SBOMs) Actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) at Conf42 DevSecOps 2022.
