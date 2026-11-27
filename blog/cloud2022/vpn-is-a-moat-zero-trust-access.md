# Your VPN is a moat, and the bears are already inside

Conf42 Blog, 2022-04-27. https://www.conf42.com/blog/cloud2022/vpn-is-a-moat-zero-trust-access

In short: Nick Bergam (Teleport) at Conf42 Cloud Native 2022 on replacing VPNs and shared secrets with zero trust access, short-lived certificates and an access proxy

A VPN checks whether you got through the wall, then trusts you with everything behind it. Nick Bergam, Solutions Engineer at Teleport, argued at Conf42 Cloud Native 2022 that this castle-and-moat model can't cope with remote work and cloud infrastructure, and that zero trust access fixes it with three moves: verify identity on every request, replace shared secrets with short-lived certificates, and route all access through one identity-aware proxy.

It is an explainer more than a demo. Teleport shows up near the end as one open source implementation among others.

## Where did the perimeter model come from?

For about 30 years, Bergam says, network security meant strong walls: LANs and WANs built on an us-versus-them philosophy, with a moat between the interior network and everything outside. VPNs were born in that era, first developed by Microsoft in the late 1990s with the Point-to-Point Tunneling Protocol to link one trusted network to another, and then stretched far beyond that by remote work and the cloud.

The zero trust model came from Forrester Research, published in response to NIST's request for feedback on a framework for critical infrastructure cybersecurity. Its premise is to assume the threats are already inside. Forrester found that more than half the breaches it surveyed could be at least partly attributed to internal actors, through lost or stolen corporate assets or misuse of information by insiders and partners. A wall does nothing about a threat that is already a trusted source. So zero trust demands strict identity verification for every person, bot, service and device, least privilege, and inspection and logging of all traffic, at every level of the OSI model to limit lateral movement.

## What's wrong with VPNs, specifically?

His charge sheet:

- **They weren't built for continuous use.** A remote workforce turned them into always-on infrastructure, with overloaded servers, latency at peak hours, and the oddity of hauling all traffic to the corporate network only to send it back out to the cloud.
- **No authentication, authorization or audit of their own.** You can bolt those on with other tools, but that means more software, more overhead and more configuration.
- **They have a CVE list of their own.** At the time of recording he counted over 560 known vulnerabilities attributable to VPN technology itself.
- **They are blind to content.** A VPN doesn't know whether it is carrying ransomware in or data out.

## What does zero trust access require instead?

Continuous authentication comes first, because authorization and audit depend on it: single sign-on, a strong identity provider and MFA. Then authorization by least privilege, split by role or attribute, plus just-in-time access granted for a set period and a specific need. His illustration is Cincinnatus, granted a dictator's powers to steer Rome through a crisis, who handed them back and went home to his farm. Privileges that expire are privileges an attacker can't hoard.

Audit needs identities strong enough to attribute every action: who SSHed into a server as root and ran a command, who altered a table as the admin user.

## Why get rid of shared secrets?

"So one of the keys to securing your infrastructure is well eliminating keys," Nick Bergam said at Conf42 Cloud Native 2022.

Passwords and secret keys can be brute-forced, intercepted, or harvested and still valid months after a patch. Vaults full of them are landmines if the wrong person finds them, and they rely on the same hard-wall premise as the perimeter. And under pressure people paste credentials into Slack, Teams or, worst case, unencrypted email. Short-lived certificates tied to a strong identity remove that overhead: a hard time-to-live limits the damage, lateral movement with a stolen certificate gets much harder, and each access request is verified afresh.

## Isn't the safest SSH no SSH?

Removing access types altogether, risk avoidance, sounds great to a security team; he notes you'll rarely find an engineer who agrees. His alternative is a unified access plane: a proxy or gateway that every connection to databases, servers, Kubernetes and applications passes through. It lets only authenticated SSO users through, attaches their identity to every request, and ties activity under generic logins like root or admin back to a real user.

He points to Google's BeyondCorp, released in 2014 so employees could work from any network without a VPN, and to Google's Identity-Aware Proxy for GCP stacks. For cloud-agnostic setups there are open source tools, Teleport among them.

## Who should watch

Security and platform engineers still routing everything through a VPN concentrator, and anyone who needs the zero trust argument in plain language for a budget conversation. There is no live demo, so expect concepts rather than configuration.

## Related Conf42 talks

- Linda Ikechukwu on [introducing SSH certificates](https://www.conf42.com/Cloud_Native_2023_Linda_Ikechukwu_introducing_ssh_certificates) at Conf42 Cloud Native 2023.
- Atif Siddiqui on [cloud network segmentation in pursuit of zero trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) at Conf42 Platform Engineering 2023.
- Thibault Koechlin on [crowd power and zero trust architecture](https://www.conf42.com/Chaos_Engineering_2021_Thibault_Koechlin_crowd_power_internets_zero_trust_architecture) at Conf42 Chaos Engineering 2021.

[Watch Nick Bergam's talk](https://www.conf42.com/Cloud_Native_2022_Nick_Bergam_trust_by_verify_provide_secure_access)

## From Teleport

In the talk, Bergam describes Teleport as an open source access plane that provides authentication, authorization and audit across cloud resources, using short-lived certificates. Teleport covers SSH servers, Kubernetes clusters, web applications and databases.

- Teleport: [goteleport.com](https://goteleport.com/)
- About Teleport: [goteleport.com/about](https://goteleport.com/about)
- Teleport blog: [goteleport.com/blog](https://goteleport.com/blog)

[Watch the talk on YouTube](https://youtu.be/1OAEQSQ3PpE).

## Watch the talk

[Trust by verify - how to provide secure access to your team](https://www.conf42.com/Cloud_Native_2022_Nick_Bergam_trust_by_verify_provide_secure_access) at Conf42 Cloud Native 2022.
