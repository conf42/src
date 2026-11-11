# Your supply chain is 46% unpaid volunteers

Conf42 Blog, 2022-12-02. https://www.conf42.com/devsecops2022/open-source-maintainers-are-your-supply-chain

In short: Floor Drees (Aiven) at Conf42 DevSecOps 2022 on why scanning is not enough and open source sustainability is a security problem

Scanning dependencies for CVEs treats the symptom. At Conf42 DevSecOps 2022, Floor Drees, Staff Developer Advocate at Aiven, made the case that the root causes sit upstream: licence changes, burnt-out maintainers and sabotaged packages. If 97% of commercial code bases contain open source, the health of those projects is your security posture.

Floor opens with a confession: at DevOpsDays Eindhoven she proposed an open space arguing that DevSecOps is a band-aid for a bullet wound, right after a talk about supply chain security tools. The talk is that argument, with receipts.

## How much of your code is somebody else's?

The numbers come from the 2022 Synopsys Open Source Security and Risk Analysis report: over 2,400 audited commercial code bases, 97% of them containing open source. In four of the 17 industries (computer hardware and semiconductors, cybersecurity, energy and clean tech, IoT) the figure was 100%. Installing Electron pulls in 87 packages, which means 87 licences to comply with before you count their dependencies.

She frames it as a scale problem. A typical Java project has around 150 dependencies; at roughly ten releases a year each, that is 1,500 updates to consider. A single npm install implicitly trusts 79 third-party packages and 39 maintainers.

## Licences: the cloud-restricted turn

The middle of the talk is a tour of licences written to stop cloud providers from reselling a project: the Commons Clause, MongoDB's move to SSPL in 2018, the Redis Source Available License, Elastic License 2.0, Timescale's TSL and the Confluent Community License. Floor also covers ethical licences such as the Hippocratic License and points to ethicalsource.dev.

Her verdict is nuanced. These licences did stop free riding, but they also pushed the community to fork or build alternatives, and they can drive users away. She doesn't buy the claim that MongoDB and Elastic were never really open source; she thinks they confused open source with their business model. Lightbend's switch of Akka from Apache 2.0 to the Business Source License from version 2.7 is another example, with the usual talk of a fork. She is upfront about her own angle: Aiven is heavily invested in OpenSearch, the fork of Elasticsearch.

The practical advice is reassuring. There are over 300 open source licences, but around 20 cover 80% of the open source enterprises commonly use, so an allow and deny list plus a scanner gets you far.

## The single individual in Nebraska

The xkcd comic gets its moment. For every curl, maintained largely by Daniel Stenberg alone, there is a Log4j. Floor cites a 2021 Tidelift survey of 400 maintainers: 46% are not paid at all, only 26% earn as much as $1,000 a year for maintenance, and 59% have quit or considered quitting.

Then the case files. left-pad in 2016, unpublished after a naming dispute and forcibly restored by npm. Seth Vargo deleting his code after learning of a contract between Chef and ICE. colors.js, with over 3.3 billion downloads, trapped in an infinite loop printing liberty, alongside a gutted faker.js. node-ipc, with over a million weekly downloads, shipping versions that overwrote files on machines in Russia and Belarus: protestware.

"Open source is part of our infrastructure, products and tooling, and for this reason we need to care about them like they were our own projects," Floor Drees said at Conf42 DevSecOps 2022.

## Many eyes, wrong places

Log4Shell scored ten out of ten on CVSS, and checking your own code wasn't enough: she quotes Snyk's finding that 60% of Java applications relied on Log4j indirectly. The project came from the Apache Software Foundation, which signals health, and it still happened. "I find that developers are looking at open source for solutions, not problems," she says.

Yet the picture is better than the panic suggests. 98% of projects have safe versions available, and Log4j was patched in 15 days, with the fix out by the time the CVE went public. The problem is management: 68% of IT leaders are confident they don't use vulnerable versions, and 68% of applications do.

The tooling she recommends: SBOMs, SCA tools such as the OSS Review Toolkit with SPDX, the OpenSSF Census II, the criticality score and the OpenSSF Scorecard.

## So what can a company do?

Floor's list is concrete:

- Contribute code, reviews and docs where the project needs them, and stay graceful when a PR doesn't land.
- Sponsor projects, steadily: money one month and nothing the next can be as bad as none.
- Treat licence exposure like security exposure, be careful with automated dependency updates in CI/CD, and prefer plugins over downstream modifications.
- When vetting a component, ask about its licence, who is behind it and its governance.
- Follow the principles of authentic participation from Sustain Summit 2020: start early, put the community first, start by listening, be transparent, enforce respectful behaviour, and end gracefully.
- Support foundations such as Apache, the Linux Foundation, CNCF and Eclipse, and send the right people to the seat you get.

## Who should watch

Engineering leaders who sign off on dependencies, AppSec teams tired of chasing the same class of incident, and anyone who has never asked who maintains the library holding up their build. It's a policy talk more than a tooling talk, and a well-sourced one.

Pair it with [Ciara Carey on making SBOMs actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) and [Henrik Plate on open source vulnerability management](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source), both from the same event, and [Trista Pan on growing a healthy open source community](https://www.conf42.com/DevOps_2023_Trista_Pan_n_tips_growing_healthy_community_open_source_project) at DevOps 2023.

[Watch Floor Drees's talk](https://www.conf42.com/DevSecOps_2022_Floor_Drees_sustainable_open_source) from [Conf42 DevSecOps 2022](https://www.conf42.com/devsecops2022).

## From Aiven

Floor introduces Aiven as a company that runs managed open source data tools, and mentions its investment in OpenSearch and Apache Kafka.

- Aiven: [aiven.io](https://aiven.io)

[Watch the talk on YouTube](https://youtu.be/0yAZIVLLrcA).

## Watch the talk

[SOS: Sustainable Open Source](https://www.conf42.com/DevSecOps_2022_Floor_Drees_sustainable_open_source) at Conf42 DevSecOps 2022.
