# Every dependency is code you outsourced to a stranger

Conf42 Blog, 2022-12-01. https://www.conf42.com/devsecops2022/every-dependency-is-outsourced-code

In short: Ixchel Ruiz (JFrog) at Conf42 DevSecOps 2022 on vetting dependencies before you add them, and keeping the alerts that follow down to what matters

Adding a dependency means handing the design, testing, debugging and maintenance of that code to someone you have probably never met. At Conf42 DevSecOps 2022, Ixchel Ruiz, Java Champion and developer advocate at JFrog, laid out the questions to ask before you take that deal and the tools that keep you honest afterwards.

Her starting numbers come from the 2022 Synopsys Open Source Security and Risk Analysis report: 78% of the code in the audited code bases was open source, and 85% of code bases contained open source that was more than four years out of date. Your artifact is mostly other people's work, and some of it is old.

## Not all dependencies are the same

Ixchel opens with a quiz. True or false: dependencies are collections of high-quality, tested code whose functionality took significant expertise to build. True. Also true: package managers like npm have made it possible to package and publish almost trivial functionality. Both live in your lockfile.

She separates the kinds you pull in. Resources are files such as templates, media or plain text that an application needs to run. Modules are self-contained sets of functions behind an interface. Packages group modules with the same purpose, usually a directory with a metadata file. A library is a set of functions you call that hand control back to you. A framework inverts that: it runs its own workflow and calls your code at the hooks it provides. The distinction matters because the bigger and more opinionated the dependency, the more its update cadence, migration cost and cleanup effort become yours.

## What does a bad dependency cost?

Every dependency earns its place by providing something, and every one carries a cost: you will update it, migrate it or remove it eventually. When one breaks, you choose between patching it, swapping it or refactoring around it, and each choice spends quality, performance and budget.

She leans on Russ Cox's paper Surviving Software Dependencies for the maths: the expected cost of adopting a bad dependency is the sum, over every possible bad outcome, of its cost times its probability. Outages and the people affected by them sit on top of the fix itself.

## The checklist, before you type the version number

Ixchel's inspection list, adapted from Cox, is the practical core of the talk:

- **Design.** Is the documentation clear, does the API have a clear design? Authors who explain the API well tend to explain the implementation well to the computer.
- **Code quality.** Read some of it. Would you want to debug it on a Friday night before a release?
- **Tests.** Are there tests, can you run them, do they pass?
- **Bug fixing.** How many open issues, for how long, and has anything been fixed recently?
- **Maintenance and people.** How long has the project been actively maintained, and by how many? A single maintainer is not automatically a red flag; she has met solo maintainers more responsive than whole teams. A project with a tight scope may simply be done.
- **Usage.** Who else uses it, and is there a community to answer questions?
- **Security.** Is it robust against malicious input, are packages signed, do maintainers use two-factor authentication?
- **Licence.** Is there one, and is it acceptable for your product? It is shocking, she says, how many GitHub projects have no clear licence.

The same questions apply transitively: your dependency's authors should be asking them about their dependencies too.

## Open source tools that help

Before her own company's products, Ixchel points to free options: OWASP Dependency-Track, and from the OpenSSF, which she contributes to, the one-page Concise Guide for Evaluating Open Source Software, its companion guide for developing more secure software, and Scorecard, which scores a project from zero to ten on security heuristics. If you maintain open source, she asks you to run Scorecard on your project.

## A CVE count is not a risk assessment

Her sharpest point is about alert fatigue. Not every CVE is exploitable, and not every user of a library is exposed. A library with no reported CVE can still be insecure if it's misconfigured. "So security is not only about CVE, security is about the information that we generate," Ixchel Ruiz said at Conf42 DevSecOps 2022. That information includes whether a new version still runs correctly in your context and still meets your service levels.

On notifications, she is blunt: if a thousand arrive and everything is a priority, nothing is. Filter them by policy.

## Who should watch

Developers who add dependencies with a single command and want a short checklist to run first, and team leads setting dependency policy. Java folks will feel at home: the demo is a Maven POM file in IntelliJ IDEA.

More on the same problem: [Kyle Kelly on the minefield of open source software](https://www.conf42.com/DevOps_2024_Kyle_Kelly_minefield_opensource_software), [Danish Tariq and Hassan Khan Yusufzai on npm supply chain attacks](https://www.conf42.com/DevSecOps_2023_Danish_Tariq_Hassan_Khan_Yusufzai_supply_chain_npm_attacks), and [Ciara Carey on making SBOMs actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) from the same event.

[Watch Ixchel Ruiz's talk](https://www.conf42.com/DevSecOps_2022_Ixchel_Ruiz_journey_thousand_binaries) from [Conf42 DevSecOps 2022](https://www.conf42.com/devsecops2022).

## From JFrog

In the talk, Ixchel shows JFrog Artifactory as the repository for whatever package types you consume and publish, with JFrog Xray scanning dependencies down to the binary level, including Docker image layers, and checking whether a CVE actually applies to you. She demos Frogbot, a Git bot that scans dependencies when they're added and filters findings through watches you define; the JFrog Docker Desktop extension for image reports; and the IDE extension that flags a vulnerable version as you type it into a POM file. She notes there is a free tier to start with.

- JFrog: [jfrog.com](https://jfrog.com/advanced-security/?utm_source=event-page&utm_medium=jfrog-logo&utm_campaign=conference-42&utm_term=event)

[Watch the talk on YouTube](https://youtu.be/GLV2Xxa9wFU).

## Watch the talk

[A journey of the thousand binaries](https://www.conf42.com/DevSecOps_2022_Ixchel_Ruiz_journey_thousand_binaries) at Conf42 DevSecOps 2022.
