# 14% of developers don't care about security. Run a game day anyway

Conf42 Blog, 2021-02-24. https://www.conf42.com/blog/ce2021/security-chaos-game-days-for-developers

In short: Yury Nino and Jhonnatan Gil Chaves (Aval Digital Labs) at Conf42 Chaos Engineering 2021 on getting developers into security through chaos game days

Before trying to get developers interested in security, Aval Digital Labs measured how interested they were. At Conf42 Chaos Engineering 2021, Yury Nino and Jhonnatan Gil Chaves, DevOps engineers at Aval Digital Labs (ADL) in Colombia, share a survey of 130 of their own engineers, in which 14% showed no interest in security and 23% had no security steps in their pipelines, and propose security chaos engineering game days as the way to change that.

The talk has three parts: Jhonnatan's tour of what the big cloud providers recommend, Yury's survey and the case for security chaos engineering, and a closing list of practical recommendations.

## What do the cloud providers already tell you?

Jhonnatan starts with the security pillar of the AWS Well-Architected Framework: a strong identity foundation (least privilege, separation of duties, centralised identity, no long-term static credentials), traceability, security at every layer from VPC and subnets to instances and S3 buckets, automated security alerts, data protection in transit and at rest, and preparing the team for security events. Azure's version stresses defence in depth and single sign-on through the company directory; Google Cloud's adds layered security and automating sensitive tasks so people aren't running scripts against sensitive data by hand. Different words, same advice.

## Why is security not the same as reliability?

Yury's framing: both care about confidentiality, integrity and availability, but through different lenses, and the difference is the adversary. Yury Nino said at Conf42 Chaos Engineering 2021: "In the absence of an adversary, systems often fail safe."

A door that fails open in a power cut is safe for people and a gift to a burglar. Reliability design assumes things will go wrong at some point; security design has to assume someone is trying to make them go wrong at any point. The first step to closing the gap, she says, is educating developers, while accepting that even well-trained engineers make mistakes.

## What did the survey find?

ADL surveyed 130 engineers, mostly backend and DevOps engineers, plus software architects and frontend engineers. Roughly one in seven had no interest in security topics, which the team found significant for a mostly backend group. And 23% had no security steps in their pipelines.

Tooling told the same story. ADL's Jenkins pipelines run Sonar, so 49 people reported using it; for scanning dependencies for vulnerabilities, only three used Black Duck, two used Snyk and one used Fortify.

She adds outside numbers: a 2019 study of 32 web applications found 82% of vulnerabilities in the application code itself, with unauthorised access possible on 30% of the sites. Her conclusion: an exploited vulnerability is only a matter of time, and organisations have to build training and culture internally.

## Why game days and not more training?

Security chaos engineering, as defined in the book by Aaron Rinehart and Kelly Shortridge, is the identification of security control failures through proactive experiments, to build confidence that a system can defend itself against malicious conditions in production. Yury's argument is that classroom training won't change a developer's mindset, but gamified, risk-free exercises might.

The game day has three phases: before (pick a hypothesis, a style, who, where and when), during (detect, communicate, read the observability dashboards, analyse, fix) and after (a postmortem on impact, duration, resolution time and actions). The experiments they suggest:

- introduce latency on security controls;
- disclose a secret in clear text in non-production;
- disable service logging;
- create permission collisions, for example in AWS API Gateway;
- create an unencrypted S3 bucket;
- disable multi-factor authentication.

## What do they recommend day to day?

Jhonnatan's closing list is practical: no sensitive data in logs (debug production some other way), MFA on critical actions, not just login, short-lived one-time links for delivered documents and removing them from storage afterwards, only a session id (never sensitive data) in cookies or browser storage, auditable user actions, dependency scanning and security steps in CI/CD, hash checks on artifacts, containers that don't run as root, separate environments and databases, and locking accounts after repeated failed logins, with an email to tell the user.

## Who should watch

Platform and security leads trying to bring developers into security, and anyone planning a first security game day who wants a list of starter experiments.

## Related Conf42 talks

- Yury Nino on [security chaos engineering game days](https://www.conf42.com/Site_Reliability_Engineering_2020_Yury_Nino_security_chaos_engineering_gamedays__experiments__cybera) at Conf42 SRE 2020.
- Swapnil Deshmukh on [a continuous security feedback loop in production](https://www.conf42.com/Chaos_Engineering_2021_Swapnil_Deshmukh_shift_up_security_feedback_loop) at Conf42 Chaos Engineering 2021.
- Aaron Rinehart and David Lavezzo on [cyber chaos engineering](https://www.conf42.com/Chaos_Engineering_2021_Aaron_Rinehart_David_Lavezzo_cyber_chaos_engineering) at Conf42 Chaos Engineering 2021.

[Watch Yury Nino and Jhonnatan Gil Chaves's talk](https://www.conf42.com/Chaos_Engineering_2021_Yury_Nino_Jhonnatan_Gil_Chaves_cloud_security_chaos_engineering)

## From Aval Digital Labs

Aval Digital Labs provides technology and innovation services in Colombia; the survey and the experiments in the talk come from its own engineering teams.

- Aval Digital Labs: [adldigitallab.com](https://www.adldigitallab.com)

[Watch the talk on YouTube](https://youtu.be/W_wazXG70-Y).

## Watch the talk

[Securing the Cloud: Empowering Developers to practice Security Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2021_Yury_Nino_Jhonnatan_Gil_Chaves_cloud_security_chaos_engineering) at Conf42 Chaos Engineering 2021.
