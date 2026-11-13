# The root account owner left, and the AWS access went with them

Conf42 Blog, 2020-08-28. https://www.conf42.com/blog/sre2020/security-chaos-gamedays-evolve-phase

In short: Yury Nino (Aval Digital Labs) at Conf42 Site Reliability Engineering 2020 on running chaos game days where the experiments are cyberattacks

SRE practice has SLAs and severity levels for almost every incident, except the security ones, which tend to get a disclaimer instead. At Conf42 Site Reliability Engineering 2020, Yury Nino, site reliability engineer at Aval Digital Labs in Colombia, which provides technology and innovation services for a banking group, presented a framework for security chaos game days: the classic before, during and after phases, extra considerations for attackers, and a new fourth phase called Evolve.

Yury is a chaos engineering advocate in the Spanish-speaking community, and the talk is built from the reading and experiments of a study group at ADL.

## Why does security fall out of incident management?

She opens with resilience as culture (Japan rebuilding after disasters, and the samurai Miyamoto Musashi choosing the weapon to fit the circumstance) and then gets specific. Cyberattacks such as NotPetya, the 2017 Equifax breach and the 2020 Twitter social-engineering attack behave like black swans: hard or impossible to predict, severe, and capable of hours of downtime.

Yet the SEV literature she studied leaves security out. Her evidence is personal: an SLA from a former employer listed attention and resolution times for high, medium and low priority incidents per environment, with a disclaimer that none of it applied when the incident was related to security. She argues security and reliability share the same concerns and should both be top priorities, citing Google's Building Secure and Reliable Systems, and Kolton Andrus's answer to her questions in a public Q&A: reliability is a core pillar of security testing, and penetration tests and chaos experiments share parallels but have different goals.

## Aren't red and purple teams enough?

Red teams imitate attackers as realistically as possible (ethical hacking, penetration testing), blue teams defend, and purple teams merge the two so both sides learn. They remain valuable, she says, but they're not enough on their own against attacks of that scale.

Security chaos engineering adds proactive experiments. Her definition, from the 2020 Chaos Engineering book: the identification of security control failures through proactive experimentation, to build confidence in the system's ability to defend against malicious conditions in production. Her slides add a practical angle: inject false positives into production to check whether your procedures catch security failures under controlled conditions.

## What changes in a security game day?

The base is the game-day framework from Russ Miles's Learning Chaos Engineering. Before: pick a hypothesis and a style, decide who, where and when, document, get approval. During: detect, take a deep breath, communicate, check dashboards, analyse, propose and apply a fix. After: a postmortem with what happened, impact, duration, resolution time, timeline and action items.

ADL's considerations for security:

- Understand the adversary: motivations, profiles and methods. Human factors are the hardest part.
- Choose a style with adversaries, at least two teams attacking each other (her slides call it Dungeons & Dragons), rather than a single master of disaster.
- Reconsider the roles, for example by bringing in a consultant who knows current attacks.

Her list of experiments to run during the game day is the part to steal: add latency to security controls, drop a folder the way a malicious script would in production, disclose a secret in clear text, create a permission collision in a shared IAM role policy, disable service event logging, shut down an API gateway, leave an S3 bucket unencrypted, disable MFA.

## What did a thought experiment find?

ADL also runs mental experiments. The hypothesis: after the owner of the AWS root account left the company, the team could keep using the cloud normally. Disproved. AWS access was tied to Active Directory, so when the employee's account was dropped, so was the access. The side effect was more valuable still: it made the team list every other application connected to Active Directory.

## What does the Evolve phase add?

A security postmortem has to cover the technology the attacker exploited and how incident handling could improve, then document time frames and effort for each action item. Evolve turns that into the next game day: improve the vulnerability database, refine the process, adjust metrics, validate the team's position on the Chaos Maturity Model, and adapt the next exercise. She ties this to Verica's idea of continuous verification, and proposes adding security to the maturity model to help newcomers start.

## What did the study group learn?

Human factors and an attacker's point of view are central to good hypotheses. Limiting blast radius is even more important in security. Communication and observability (she names Datadog and New Relic) decide whether a game day succeeds. Compliance requirements can collide with experimentation. And "you don't need to be an expert and security expert in order to start with security chaos engineering," Yury Nino said at Conf42 Site Reliability Engineering 2020.

## Who should watch

SRE and security teams who run game days for availability and want to aim them at controls. Pair it with [Aaron Rinehart and Jamie Dicken's applied security talk](https://www.conf42.com/Site_Reliability_Engineering_2020_Aaron_Rinehart_Jamie_Dicken_applied_security_resilient_distributed) from the same event, Yury's [postmortem culture talk at Conf42 Chaos Engineering 2020](https://www.conf42.com/Chaos_Engineering_2020_Yury_Nino_postmortem_culture), and [Kim Carter on OWASP PurpleTeam](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam).

[Watch Yury Nino's talk](https://www.conf42.com/Site_Reliability_Engineering_2020_Yury_Nino_security_chaos_engineering_gamedays__experiments__cybera) from [Conf42 Site Reliability Engineering 2020](https://www.conf42.com/sre2020).

## From Aval Digital Labs

Aval Digital Labs provides technology and innovation services for a banking group in Colombia; the framework in the talk comes from its internal chaos engineering study group.

- Aval Digital Labs: [adldigitallab.com](https://www.adldigitallab.com)

[Watch the talk on YouTube](https://youtu.be/hnoahDG03P0).

## Watch the talk

[Security Chaos Engineering: Considerations for Gamedays when the Experiments are Cyberattacks](https://www.conf42.com/Site_Reliability_Engineering_2020_Yury_Nino_security_chaos_engineering_gamedays__experiments__cybera) at Conf42 Site Reliability Engineering 2020.
