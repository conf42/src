# Test your ransomware defences before the ransom note does

Conf42 Blog, 2022-03-10. https://www.conf42.com/blog/ce2022/ransomware-drills-with-security-chaos

In short: Kennedy Torkura (Mitigant) at Conf42 Chaos Engineering 2022 on using security chaos engineering to verify cloud ransomware controls, backups and runbooks

Most ransomware playbooks end with restore from backup, and almost nobody checks whether the backup restores. At Conf42 Chaos Engineering 2022, Kennedy Torkura, co-founder and CTO of Mitigant, argued that security chaos engineering is how you find out: treat each ransomware countermeasure as a hypothesis, inject the attack's steps into your own cloud, and see which controls fire. His sharpest point is about timing: incident response usually starts at the very end of an attack that took many earlier steps to set up.

## How big is the problem he describes?

He opens with the numbers circulating at the time: a Sophos report in which 79% of the managed incident response cases were ransomware, SonicWall's 148% rise in ransomware between Q2 2020 and Q2 2021, and 2,084 ransomware complaints to the FBI in the first half of 2021. The impacts he lists are familiar but worth stacking: money, data that never comes back even after paying, reputation, legal exposure under rules like GDPR, and plain business disruption, such as the attack on the German retailer MediaMarkt that knocked out its point-of-sale systems.

## Why is ransomware a chain, not an event?

Using a Windows ransomware family that enters through RDP brute force, he walks the steps: scan for targets, switch off security tools, network reconnaissance, lateral movement, credential theft, a backdoor, a coin miner on the side, and only at step eight the ransom demand. Ransomware-as-a-service lowers the entry bar further, because attackers no longer have to write any of it.

The point for defenders is that each of those steps is a chance to detect them. "Incident response in most cases is triggered at the end, after the attack is almost successful or is already successful," Kennedy Torkura said at Conf42 Chaos Engineering 2022.

## Is the cloud really a target?

Yes, and he spends a section on the misconceptions. The pandemic pushed companies into hurried migrations; hybrid setups blur the line between on-premises and cloud, giving attackers a bridge to move across. "The cloud is not immune to ransomware," he said, and the shared responsibility model leaves most logical security, like S3 bucket configuration, with the customer. He quotes Gartner's warning that misconfiguration will drive the overwhelming majority of cloud security failures.

## What does a security chaos experiment look like?

He defines security chaos engineering as finding security control failures through proactive experimentation, aimed at confidentiality, integrity and availability rather than uptime. His AWS scenario is hypothetical but concrete. An attacker creates a user, Bob. Bob reaches an EKS cluster, compromises a pod, notices the pod reads from an S3 bucket holding sensitive data, takes over the bucket, encrypts it, demands payment.

Run that as an experiment and every step becomes a question. Did AWS Config or your CSPM flag the unexpected user? Did Kubernetes controls, GuardDuty or Security Hub notice the pod compromise? Did IAM Access Analyzer react to suspicious bucket access? And at the end: are the backups accessible, uncorrupted and usable, and are the runbooks accurate?

## Where do you start?

With security game days: the security team, SREs and anyone in the incident response chain, in a planned session. For candidate experiments he points to AWS's paper on ransomware risk management using the NIST Cybersecurity Framework, which covers checks like backups, corruption testing, deny-listing, EC2 security groups and Route 53 configuration. He also insists on continuous verification of runbooks, because cloud infrastructure changes constantly and a runbook written for last quarter's architecture misleads more than it helps.

Kennedy did his doctoral research on security chaos engineering and contributed to the first book on the subject, by Aaron Rinehart and Kelly Shortridge.

## Who should watch

Cloud security engineers and SREs who own backup and incident response but have never tested them against an attack sequence. It is a conceptual talk with an AWS-specific scenario and no live demo.

## Related Conf42 talks

- Yury Niño and Jhonnatan Gil Chaves on [cloud security chaos engineering](https://www.conf42.com/Chaos_Engineering_2021_Yury_Nino_Jhonnatan_Gil_Chaves_cloud_security_chaos_engineering) at Conf42 Chaos Engineering 2021.
- Kim Carter on [OWASP PurpleTeam](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam), from the same event.
- Srihari Pakalapati on [ransomware readiness and backups](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Srihari_Pakalapati_ransomware_readiness_backup) at Conf42 SRE 2025.

[Watch Kennedy Torkura's talk](https://www.conf42.com/Chaos_Engineering_2022_Kennedy_Torkura_defeating_ransomware_attacks) from [Conf42 Chaos Engineering 2022](https://www.conf42.com/ce2022).

## From Mitigant

Mitigant describes itself as a continuous security verification platform, applying security chaos engineering to cloud environments.

- Mitigant: [mitigant.io](https://mitigant.io/home)

[Watch the talk on YouTube](https://youtu.be/y_Ve7jiHDFA).

## Watch the talk

[Defeating Ransomware Attacks with Security Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Kennedy_Torkura_defeating_ransomware_attacks) at Conf42 Chaos Engineering 2022.
