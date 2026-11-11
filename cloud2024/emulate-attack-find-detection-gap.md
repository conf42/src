# Your cloud SIEM caught 30 secret reads and missed the batch call

Conf42 Blog, 2024-03-22. https://www.conf42.com/cloud2024/emulate-attack-find-detection-gap

In short: Kennedy Torkura (Mitigant) at Conf42 Cloud Native 2024 on testing cloud threat detections by emulating real attacker techniques

The best moment in this talk is a detection that works 30 times and then misses the one call that matters. At Conf42 Cloud Native 2024, [Kennedy Torkura](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense), Co-Founder and CTO of Mitigant, made the case for threat-informed defense: pick the attacker techniques relevant to you, build detections for them, then emulate those techniques in your own cloud to prove the detections fire. His AWS example found a gap that a single new API call walked straight through.

It is a sponsor talk with a demo of Mitigant's cloud attack emulation product at the end, but the method in the middle needs nothing more than CloudTrail, a detection rule and an afternoon.

## What is threat-informed defense?

The definition comes from MITRE Engenuity: the systematic application of a deep understanding of adversary tradecraft and technology to improve defenses. He frames it as a signal-to-noise problem: most security news is not about your organisation.

It rests on three pillars that feed each other:

- **Defensive measures**, anchored on MITRE ATT&CK. The Enterprise matrix, version 14 at the time, has 14 tactics and 234 techniques. Nobody covers all of them, and his point is that you should not try. Pick the slice an attacker would actually walk through your infrastructure.
- **Cyber threat intelligence**, which narrows that slice further. His example is Scattered Spider, the group behind the MGM Resorts ransomware attack, which targets sectors such as entertainment, telecoms and technology. The free ATT&CK Navigator maps the group to the techniques it uses, and filtering to infrastructure as a service leaves a short list.
- **Testing and evaluation**, the pillar he says gets talked about least. MITRE recommends adversary emulation: mimicking real threat actors in a way that is safe and, crucially, repeatable, so you can rerun it after hardening and see whether anything improved.

## Why emulate instead of pen-test?

He walks through MITRE Engenuity's five questions for deciding whether you need adversary emulation. The one that lands for engineers is about data: are you collecting the right data and running the right queries to detect a given technique? Most cloud detection is a query over log events, and either half can be wrong. Get them wrong and you pay in false positives and alert fatigue, or worse, silence.

For a real-world model he points to GitLab, whose security team publishes its stealth red and purple team process. Emulation only starts at step six, after brainstorming, logistics, adversary profiling, tabletop exercises and capability development. Step seven, validating detection and response, is detection engineering under another name.

Detection engineering itself he describes as a young discipline that grew up once the perimeter collapsed. Firewalls, WAFs and IAM sit at the front door; SIEM, XDR, NDR and cloud detection and response deal with attackers already inside. Detection engineers write rules much like software, often as Sigma rules in YAML, such as one that fires when AWS CloudTrail is stopped, updated or deleted.

## How does one API call slip past?

The worked example ties the three pillars together. Threat intelligence says Scattered Spider harvests credentials from cloud secrets stores, ATT&CK technique T1555.006. You have a detection for it. So you emulate it against AWS Secrets Manager, with logs flowing from CloudTrail into Datadog Cloud SIEM.

Mitigant ran two variants. One reads secrets one at a time with GetSecretValue. The other uses BatchGetSecretValue, which AWS released in November 2023, to fetch about ten secrets in a single call. CloudTrail recorded both. Datadog flagged the 30 single GetSecretValue calls and missed the batch call entirely.

The cause was the query. The example rule he showed matched on GetSecretValue only, so the newer API was invisible to it, and the fix is one more event name. Kennedy Torkura said at Conf42 Cloud Native 2024: "the threat detection systems might miss some detections, either because the cloud service provider kind of had new APIs or they released new features".

## What did the demo show?

The demo runs Mitigant's attack actions against an AWS account: make a private S3 bucket public (mapped to ATT&CK discovery), create a new IAM user with API keys and full S3 access, and disable logging on an S3 bucket. It connects over the AWS API, and as he put it, "we don't install agents at all." Resources can be exempted with tags, CloudTrail evidence lands in the report after about ten minutes, and everything is rolled back automatically about five minutes after the attack. The report has fields for the objective and your observations of what your detection system did.

## Who should watch?

Detection engineers and cloud security teams who have written rules but never proved they fire, and SREs curious how the chaos engineering habit carries over to security. He is, after all, one of the people who pioneered security chaos engineering.

## Related Conf42 talks

- Kennedy Torkura's earlier talk on [defeating ransomware attacks](https://www.conf42.com/Chaos_Engineering_2022_Kennedy_Torkura_defeating_ransomware_attacks) at Conf42 Chaos Engineering 2022.
- Christopher Haller on [Atomic Red Team and closing the gap with threat actors](https://www.conf42.com/Incident_Management_2023_Christopher_Haller_atomic_red_team_threat_actors) at Conf42 Incident Management 2023.
- Josh Armitage on [red teaming AWS](https://www.conf42.com/DevSecOps_2022_Josh_Armitage_red_teaming_aws_practice_preach) at Conf42 DevSecOps 2022.

[Watch Kennedy Torkura's talk](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense), part of [Conf42 Cloud Native 2024](https://www.conf42.com/cloud2024).

## From Mitigant

Mitigant is a Berlin-based cloud security company; its cloud attack emulation runs agentless attack actions and scenarios mapped to MITRE ATT&CK against AWS accounts, with automatic rollback.

- [Mitigant website](https://mitigant.io/home)

[Watch the talk on YouTube](https://youtu.be/fkGbOjc6pW0).

## Watch the talk

[Synergizing Threat-Informed Defense: When Cloud Attack Emulation Meets Detection Engineering](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense) at Conf42 Cloud Native 2024.
