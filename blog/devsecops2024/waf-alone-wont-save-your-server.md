# Twenty WAFs in a row won't save a server that is down at layer 4

Conf42 Blog, 2024-12-05. https://www.conf42.com/blog/devsecops2024/waf-alone-wont-save-your-server

In short: Lukasz Karwacki (Gcore) at Conf42 DevSecOps 2024 on why web app protection and L3/L4 DDoS protection only work together

A perfect web application firewall is no help when the box behind it has been flooded off the network. At Conf42 DevSecOps 2024, [Lukasz Karwacki](https://www.conf42.com/DevSecOps_2024_Lukasz_Karwacki_protection_Infra_web_apps), Security Solution Architect (Edge Network) at Gcore, argued that web application and API protection (WAAP) and infrastructure DDoS protection are two halves of one job, and that attackers will probe both until they find the half you skipped.

This is a vendor talk: it explains the attack types and the reasoning first, then shows how Gcore puts the pieces together. The examples lean heavily on game servers, which makes it more fun than the usual e-commerce slide deck.

## What kinds of DDoS attack are we talking about?

He sorts them into three families:

- **Volumetric attacks** swamp bandwidth with UDP and ICMP floods, IPSec floods and amplification. Near-zero good traffic, a whole ocean of junk.
- **Connection attacks** open connections and never close them. His webshop example is 10,000 fake shoppers who add something to the cart and then sit there; his game server example is one fake player opening 20,000 connections. SYN, ACK and RST floods live here, along with Slowloris.
- **Application attacks** at layer 7 use little volume and a lot of cleverness: requests that send the server into expensive loops until CPU and memory run out. HTTP GET/POST floods and game-server-specific attacks sit in this group.

The trend line is the usual one, pointing up. His slides cite 7.9 million DDoS attacks in the first half of 2023, a 31% year-on-year increase.

## Why is mitigation within a minute too late?

The sharpest argument in the talk is about timing. Compare a service that filters all traffic from the first packet with one that catches 100% of an attack but only after a minute. Sixty seconds of a terabit per second is enough to take any single server down, and a web app might shrug off a restart while a game server full of players will not. His conclusion is that traffic has to arrive at the origin already clean, which means always-on filtering, as close to the attack source as possible so the latency penalty stays small.

## Why do you need both layers?

His scenario: a Minecraft server with an in-game shop on the same machine and the same network. Protect the shop with a WAF and leave the game server bare, and the attacker takes the whole host down through the game port. Protect only the game server, and the shop becomes the way in. Attackers, he said, will hit both and keep hammering whichever one falls over.

Even a flawless WAF that only lets valid HTTP requests through cannot help once the network layer is saturated. Lukasz Karwacki said at Conf42 DevSecOps 2024: "layer seven will have nothing to do with it because there will be no server to, to proceed the layer seven requests."

The WAAP side, in his list, means a WAF for the OWASP Top 10 and zero-days, bot management that lets search indexers in and keeps scrapers and automated pen-testers out, layer 7 DDoS protection for HTTP floods, and API security.

## Which controls did he show?

The infrastructure side came down to a handful of concrete controls, each tied to an attack type from earlier:

- **Geo access control**: a US game server only accepts US traffic, a European one only European, which blocks most of the world by default.
- **Rate limits per user**: if a normal Minecraft player opens at most five connections, cap it at six. The connection attack stops being interesting.
- **Packet validation**: drop malformed packets, whether they come from an attacker or from a misbehaving router at some ISP.
- **Behaviour analysis**: nobody legitimate adds 10,000 items to a cart, so the WAF can block that session on behaviour alone.

He also showed side-by-side gameplay of Counter-Strike on an unprotected server under attack and on a Gcore-protected one. The unprotected server stayed up, but lagged so badly that nobody could play. A server that responds but stutters loses players just as surely as one that is down.

## Where does the CDN fit?

The last piece is putting the CDN, the WAF and DDoS protection with one provider. On the network side his slides note that Gcore's infrastructure carries 80-85% outbound and 15-20% inbound traffic as a CDN, so there is plenty of inbound headroom to absorb attack traffic. The numbers in the slides for the network itself: 180+ points of presence, 50+ cloud locations, 14,000+ peering partners and 200+ Tbps of capacity.

## Who should watch?

Anyone running game servers, or a web app and its backend on the same network, who has bought a WAF and assumed the DDoS problem was solved. It is an introduction rather than a tour of mitigation internals, and the second half is a Gcore product walkthrough.

## Related Conf42 talks

- Joshua Fox on [what WAFs do for web applications](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Joshua_Fox_wafs_web_application) at Conf42 SRE 2024.
- Andrey Slastenov on [DDoS threats from IoT and 5G devices](https://www.conf42.com/DevSecOps_2023_Andrey_Slastenov_iot_5g_devices_ddos_threat_landscape) at Conf42 DevSecOps 2023.

[Watch Lukasz Karwacki's talk](https://www.conf42.com/DevSecOps_2024_Lukasz_Karwacki_protection_Infra_web_apps), part of [Conf42 DevSecOps 2024](https://www.conf42.com/devsecops2024).

## From Gcore

Gcore runs a global edge network with CDN, infrastructure DDoS protection and web application and API protection, the stack this talk walked through.

- [Gcore website](https://gcore.com/)

[Watch the talk on YouTube](https://youtu.be/L8IBGQvNDo8).

## Watch the talk

[Comprehensive protection for Infrastructure and Web Applications: Key Differences and Strategies](https://www.conf42.com/DevSecOps_2024_Lukasz_Karwacki_protection_Infra_web_apps) at Conf42 DevSecOps 2024.
