# The Twitch leak shows nobody cares about your servers, only what they can reach

Conf42 Blog, 2021-12-03. https://www.conf42.com/blog/devsecops2021/twitch-breach-blast-radius-segment-access

In short: Josh Stella (Fugue) at Conf42 DevSecOps 2021 uses the 2021 Twitch leak to show cloud breach damage is set by IAM segmentation, not by how attackers got in

How the attacker got in is the boring part of a cloud breach. What matters is what one set of credentials could reach from there. At Conf42 DevSecOps 2021, Josh Stella, CEO and CTO of cloud security company Fugue, spent a whiteboard session on the October 2021 Twitch leak to make that point, and to argue that blast radius is a design property of your system, not something a tool bolts on later.

Fair warning on scope: the abstract promises IAM evaluation, penetration-testing methods and policy as code. The talk itself is three slides and a whiteboard, built almost entirely around one breach and the segmentation lessons from it. That turns out to be the good part.

## What is blast radius?

Josh defines it as how much damage a breach does, as opposed to how the attacker got in. Damage is not bytes. Stealing every product image from Amazon.com would be enormous and harmless. The stolen US security-clearance records, his own included, were small and devastating, especially, as a senior NIST figure once speculated to him, if someone cross-referenced them with the Ashley Madison leak. Ransomware, he adds, usually has the ugliest profile of all.

He insists on real breaches over generic advice. "Real world breaches are the only way to actually understand cloud security topics," Josh Stella said at Conf42 DevSecOps 2021.

## Why is IAM the network now?

Fugue's annual State of Cloud Security survey, run that year with Sonatype across 300 organizations operating at scale, had IAM at the top of the list of most common cloud misconfiguration incidents for the first time. Josh says IAM is a factor in most, if not all, of the cloud breaches Fugue tracks. "It is the network in the cloud," he said.

Security groups and firewall rules are mostly about the way in. In-transit encryption inside an application matters less than it did in the data center: he has yet to see a real cloud breach where attackers read packets off the network. They call control-plane APIs and go after data at rest, such as a database snapshot or an S3 bucket, so the question becomes how much data any given key can decrypt.

## Ships have bulkheads for a reason

His mental model comes from naval architecture. A hull is segmented so that one breached compartment floods and the rest stay dry. The USS Cole survived a bomb at port because the damage stayed contained; the Titanic sank because the iceberg dragged along enough compartments. Computer systems need the same bulkheads.

## What did one Twitch server reach?

Twitch said a misconfigured server was the starting point. More than 100 GB was posted to 4chan, reportedly including three years of creator payout data, source code from almost 6,000 internal Git repositories covering all of twitch.tv, mobile, console and desktop clients, proprietary SDKs and internal red-teaming tools, plus, in other reporting, code for AWS services and an unreleased Amazon competitor to Steam.

Josh plays which-one-doesn't-belong. Payout data is application data; a public-facing server touching it is understandable, and on its own he would not lose much sleep over it. The client and web source code living behind the same access is already a stretch: teams in a services architecture should live by API contracts, not read each other's source. Code for the parent company's public cloud services being reachable from that server and its API keys is, in his word, madness.

He also flags that none of it was an attack on production systems that we know of. "Hackers like getting into Dev," he said. Non-production is where teams keep long-lived, highly privileged keys and copies of databases for convenience.

## Four things to do on Monday

His closing list:

1. Understand what you have that is valuable, thinking like an attacker about what can be done with it in combination.
2. Understand the potential damage, and segment access to the high-damage things. Separate repos are one way, not the only way; monorepo shops segment differently.
3. Think architecturally: avoid designs that break segmentation on purpose, such as production code that can list S3 buckets.
4. Worry about dev, stage and test, not just prod.

## Who should watch

Cloud security and platform engineers who own IAM design, and anyone who has to explain to leadership why a non-production breach can be the worst kind. It is an architecture talk with no demo.

## Related Conf42 talks

- Josh Stella on [cloud security with Open Policy Agent](https://www.conf42.com/Open_Source_Showcase_2020_Josh_Stella_cloud_security__open_policy_agent_opa) at Conf42 Open Source Showcase 2020.
- Ashish Rajan on [cloud security assessments in 2021](https://www.conf42.com/Cloud_Native_2021_Ashish_Rajan_Cloud_Security_Assessments_in_2021) at Conf42 Cloud Native 2021.
- Atif Siddiqui on [cloud network segmentation in pursuit of zero trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) at Conf42 Platform Engineering 2023.

[Watch Josh Stella's talk](https://www.conf42.com/DevSecOps_2021_Josh_Stella_Minimizing_the_Blast_Radius_of_a_Cloud_Breach) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Fugue

Fugue is the cloud security software company Josh Stella co-founded; it publishes the annual State of Cloud Security survey he cites in the talk.

- Fugue: [fugue.co/conf42](https://www.fugue.co/conf42)

[Watch the talk on YouTube](https://youtu.be/ddBbKQHlFpU).

## Watch the talk

[Minimizing the Blast Radius of a Cloud Breach](https://www.conf42.com/DevSecOps_2021_Josh_Stella_Minimizing_the_Blast_Radius_of_a_Cloud_Breach) at Conf42 DevSecOps 2021.
