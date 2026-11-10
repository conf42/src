# Cloudsmith: 10 ways to make your software pipeline more observable

Conf42 Blog, 2022-11-21. https://www.conf42.com/2022-11-21-cloudsmith-devsecops-sponsor-announcement

In short: Manage All Of Your Artifact Repositories, in the Cloud

#### Security into your software supply chain means visibility into how an artifact is built, packaged and signed.

A considerable part of the reason supply chain attacks are such a threat is that we are missing information to decide if the software we develop and use is safe.

Audit logs, SBOMs, automation, and package management are all essential aspects to bring visibility into your software supply chain so you can answer questions like:

- What are my build steps?
- Who wrote the code, who built that code, and who approved the code?
- What 3rd party dependencies do I use in my software, how trustworthy are they, and am I up to date?
- How do I trace my build from source to deployment?
- What vulnerabilities are in my code?

More than inspecting, scanning, and monitoring historical data, this information can be ingested by observability tools that can help you gain insights, identify unusual behavior and possibly prevent a software supply chain attack.

I've listed 10 ways to make your software pipelines more transparent and generate the information needed to gain your observability insights:

**1 Automated Build Steps**

Automate your builds using a CI/CD tool like Jenkins, CircleCI, or BuildKite. Make sure all the other tools you use in your build process, including your package repositories, tests and code scanners, facilitate automation using APIs, CLIs, and webhooks.

Having your build steps codified with no manual steps means they can be logged with timing and authentication information. You can gather unusual login attempts, policy changes, or build patterns. Using in-toto attestations at each build step can make this information verifiable and thus more trustworthy.

**2 Audit Logs**

Audit logs capture all actions the system, users, and service accounts perform for compliance and troubleshooting purposes.

All your build tools should produce audit logs, including your CI/CD, packaging, deployment, and cloud infrastructure tools.

Audit logs can be forwarded to the Security Incident and Event Management (SIEM) for visibility, tracking, and managing of security incidents. SIEM tools also provide next-generation detection, analytics, and response.

**3 Package Management**

It's much more difficult for people and scanners to figure out what is installed on a system when software is installed using scripts instead of a package manager.

A software package, artifact, or image is the output of building software- it groups files containing your software along with the metadata about the software and dependencies in a well-defined format.

A package manager is a software tool that uses the power of automation to create, upload, install, upgrade, and configure software packages. Most software languages, containers, or operating systems have a corresponding package manager, e.g., NPM, NuGet, Maven, or RPM.

Dependencies installed with a package manager ensure consistency and transparency in how software is included in your product and give a straightforward way to access your package's metadata, including version information, license information, dependencies, environment state, etc.

Let's make it easy to figure out what is on our system by installing software with a package manager.

**4 Versioning Software and Version Control**

Consistently versioning your software product releases, e.g., [Semantic Versioning](https://semver.org/), lets you keep track of all the changes and progress you make. For consumers of your software, the version numbers should inform them of when it's imperative to update and if there are backward compatibility issues.

Mistakes in build can be a hassle, but if at all possible and avoid republishing your builds.

**5 Pin your builds**

For visibility into your supply chain, we need to know all the 3rd party dependencies in your software. Some package managers, such as pip and npm, do their best to resolve package information look-ups when explicit guidance isn't provided. This means that a different dependency can be included in your software depending on when you build it e.g. if a dependency has a new update.

If you pin your dependencies to an exact version in your manifest files, no matter when you build your code, the same top-level dependencies should be pulled in, making your build more transparent and consistent.

**6 Automated dependency updates**

You need to know when your dependencies have updates for visibility into your software build.

The previous step recommended pinning your builds, but if you have many dependencies, it can be very difficult to update each one manually.

Several update tools help you check for updates in your code base, including Renovate and Dependabot (GitHub).

**7 Scorecards**

[Scorecard](https://github.com/ossf/scorecard) is an automated tool that gives developers a score on how safe their dependencies are. Understanding the trustworthiness of your dependencies is vital to improving the security posture of your project.

**8 Sign your artifacts**

Signing a package/artifact/image lets people know that this package was signed by a person or organization and proves that the code was not tampered with after it was signed.

There are issues with signing, including a lack of understanding of the signing process, cost, complexity of managing keys, implementation of code signing pipelines, and the lack of verification of signatures.

Recent developments in signing to reduce the complexity of signing and remove the cost barrier to signing with the [Sigstore](https://www.sigstore.dev/) project have invigorated efforts to sign artifacts.

**9 Generate SBOMs**

A Software Bill of Materials (SBOM) lists all the components in your software. The notion of the SBOM was popularized by the Whitehouse when it was namechecked in an [Executive Order](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) last year on improving software security.

An accurate SBOM would improve the transparency of your supply chain, which could allow for:

- Earlier identification of potentially vulnerable systems
- Support informed decisions for 3rd party dependencies
- Incentivize secure software development practices.

[Tooling around generating an SBOM](https://cloudsmith.com/blog/how-to-generate-and-host-an-sbom/) is still evolving, but hopefully, it will be integrated into build tools, making this process accurate and automatable.

**10 Provenance of your built artifacts**

It is no longer just about the published artifact at the end of your software pipeline. Instead, it is about providing the tools to ensure artifact integrity across the supply chain.

Information demonstrating the supply chain provenance of a built artifact includes a combination of the steps above, including signing, build attestations, and SBOMs.

Provenance allows you to know and prove the origin of your software.

Monitor and Observe your Software Supply Chain

Some of this information isn't so easy to generate but will help us monitor and observe our software supply chain, which will ultimately help secure it. This information will help us:

- Monitor software supply chain more effectively
- Enable visibility for DevOps, security analysts, and developers into the entire build process
- Find and connect events in our build and trace them back to the source
- Detect and mitigate against vulnerabilities earlier
- Detect and alert for unusual login activity or build activities

Observability tools are promising to answer questions relating to the information that your system is generating, even questions that are not currently anticipated- what could this do for our software supply chain?

For more content like this, visit our blog [https://cloudsmith.com/blog/](https://cloudsmith.com/blog/)
_By Ciara Carey, Developer Relations, Cloudsmith_
