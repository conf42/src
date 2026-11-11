# A 1999 threat model still fits your 2022 CI/CD pipeline

Conf42 Blog, 2022-12-01. https://www.conf42.com/devsecops2022/stride-threat-model-for-ci-cd-pipelines

In short: Darren Richardson (Eficode) at Conf42 DevSecOps 2022 on applying Microsoft's STRIDE model to every trust boundary of a modern DevOps toolchain

Microsoft published the STRIDE threat model on 1 April 1999, which is not a date that inspires confidence. Darren Richardson, Cloud Security Architect at Eficode, used his Conf42 DevSecOps 2022 talk to show that it still works on a modern pipeline of Git, Jenkins, SonarQube, Trivy, Artifactory, Ansible and containers, and that the only thing that changed in 23 years is how many trust boundaries you have to walk through.

It is an introduction, and a funny one: the 1999 half is based, by his own admission, on what a 12-year-old who skipped homework learned about IT from Friends and Frasier.

## What is threat modelling, in one paragraph?

Three steps. Map how data flows through the system. Mark the trust boundaries, which he defines as the places where ownership or control of the data changes; in most practical cases that means data in transit. Then apply a model to each boundary: list the inputs and outputs, note the possible threats, and plan mitigations. It works on software, networks, systems and business processes alike.

He prefers STRIDE over PASTA, VAST or DREAD mainly for the mnemonic: Spoofing (against authentication), Tampering (integrity), Repudiation (the ability to plausibly deny you did something), Information disclosure (confidentiality), Denial of service (availability) and Elevation of privilege (authorisation).

## The 1999 version: floppies in a coffee shop

The warm-up data flow: developer Steve hands source code to Dave from operations in a 90s coffee shop, Dave drives the floppy disks to the data centre, and end user Barry watches compressed cat videos over dial-up on port 80. Three trust boundaries. Spoofing: can Dave prove he is Dave? Information disclosure: everyone in the coffee shop can hear the install plan. Tampering: does the disk sit in his car overnight? Denial of service: lose disk two of eight and Barry gets no cats.

## The 2022 version: same method, more boundaries

Steve Jr. now pushes to GitHub, GitLab or Bitbucket; Jenkins pulls the code, SonarQube tests it, Trivy scans the Docker image, Artifactory stores it, infrastructure as code and Ansible over SSH roll it out to containers, and Barry streams HD cats over 100 megabits. The trust boundary definition is literally the same slide. What is new are internal and nested boundaries: systems within systems.

He then walks STRIDE across each one:

- **Source code repository**: your company's DNA. Spoofed credentials, tampered source, deleted logs that break the chain of changes, IP leakage, admin takeover.
- **Pipelines**: read from Git, write to binary storage, so the most dangerous spot. Darren Richardson said at Conf42 DevSecOps 2022, quoting a colleague, that "Jenkins, or pipelines in general are just formalized remote code execution". Tamper with the pipeline and you can build anything; denial of service can block an emergency patch.
- **Static analysis**: less critical, since it only returns pass or fail; the worst case is forcing a skip.
- **In-pipeline security tools**: Trivy is a favourite, but downloading tools during a build opens a spoofing path from outside.
- **Artifact storage**: the single source of truth for deployments, so tampered images get distributed and downtime stalls every later container.
- **SSH installation interface, containers and the public communication interface**: the standard threats, plus coin miners in the wrong image and container escape.

Mitigations were mostly obvious in his examples (least privilege, immutable logs), but he insists on writing them all down, several per category if you have several concerns.

## Repudiation has one answer

One category barely changed between 1999 and 2022. His mitigation for it is the same at every boundary: log everything centrally and make it impossible to edit. He challenged the audience: "If someone can tell me a repudiation threat that is not mitigated by central logging, I would love to hear it, because I've so far not encountered one."

## Where STRIDE falls short

STRIDE assumes every attacker is external and malicious. History says otherwise: misconfiguration, mismanagement and the employee with a grudge account for a large share of real incidents, and his slides cite an estimated 82% of attacks involving the human element. He has no tidy place for mishandling and internal malice in the model, so his advice is to aim the threat model inward as well. And repeat it: revisit every six months, or whenever the platform changes enough.

## Who should watch

Platform and DevOps engineers who have never run a threat model and want one worked example end to end, and security people who need a light way to introduce STRIDE to a pipeline team. Related: [Krishna Chaitanya Rudraraju on threat modelling for developers](https://www.conf42.com/DevOps_2025_Krishna_Chaitanya_Rudraraju_threat_modeling_developers), [Jagdsh Chand on iterative threat modelling in agile development](https://www.conf42.com/DevSecOps_2023_Jagdsh_Chand_iterative_threat_modelling_agile_development) and [Mert Coskuner and Cenk Kalpakoglu on securing CI/CD runners](https://www.conf42.com/Cloud_Native_2024_Mert_Coskuner_Cenk_Kalpakoglu_securing_ci_cd_runners).

[Watch Darren Richardson's talk](https://www.conf42.com/DevSecOps_2022_Darren_Richardson_threat_modelling_cicd_environments)

## From Eficode

- [Eficode](https://hubs.li/Q01sqjR80): DevOps and cloud consultancy, the speaker's employer.

[Watch the talk on YouTube](https://youtu.be/Qki3nMIzcR4).

## Watch the talk

[Threat Modelling in CI/CD environments](https://www.conf42.com/DevSecOps_2022_Darren_Richardson_threat_modelling_cicd_environments) at Conf42 DevSecOps 2022.
