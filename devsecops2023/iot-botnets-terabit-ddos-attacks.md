# Terabit DDoS attacks are built from unpatched IoT devices

Conf42 Blog, 2023-11-30. https://www.conf42.com/devsecops2023/iot-botnets-terabit-ddos-attacks

In short: Andrey Slastenov (Gcore) at Conf42 DevSecOps 2023 on how insecure IoT and 5G devices power terabit-scale botnet DDoS attacks, and how to stop them.

A server farm cannot generate a terabit-per-second attack on its own, but a few hundred thousand unpatched cameras, routers and kiosks can. At Conf42 DevSecOps 2023, Andrey Slastenov, head of security at Gcore, explained why the growth of IoT and 5G devices tracks the growth of DDoS attacks, how those botnets recruit and attack, and what both device owners and network operators can do about it.

It is a threat briefing grounded in Gcore's own traffic statistics and one detailed mitigation case.

## How fast are attacks growing?

Gcore's figures for the average attack size: 300 Gbps at the start of 2021, 650 Gbps at the start of 2022, 800 Gbps at the start of 2023. In the first half of 2023, IoT-driven DDoS attacks rose by 300%, with an estimated $2.5 billion in losses, and the number of IoT devices engaged in botnet attacks rose from about 200,000 to a million within a year. 90% of complex, multi-vector attacks are botnet-based.

The arithmetic explains the link. Attacks above a terabit per second are beyond what a cluster of servers or VMs can produce; they need thousands of widely spread devices with good uplinks, which is precisely what IoT on fast 5G connections offers.

## Why are IoT devices such easy recruits?

Firmware that never gets updated and factory-default passwords. "When was the last time you updated your home thermostat connected to the Internet or changed its factory set password?" Andrey Slastenov said at Conf42 DevSecOps 2023. He shows a Shodan search for MikroTik devices with port 80 open to make the scale of the exposure visible, and adds that 5G turns a small security gap into a large problem quickly, because every compromised device brings more bandwidth.

## Anatomy of a botnet

The attack has three steps: the operator picks a target (a device, website or service, often chosen for maximum disruption), the command-and-control server sends instructions to every bot and coordinates them, and the bots flood the target until legitimate users cannot get through.

Recruitment, modelled on Mirai, is the part that makes botnets self-propagating. Bots scan IP ranges for vulnerable devices, brute-force weak passwords or exploit outdated firmware, report the victim's address and credentials to a loader server, which sends the malware, and the new bot joins and waits for orders, often undetected.

The damage is easy to price. His example: an online store earning $50,000 an hour loses $50,000 for every hour offline, before counting customers who leave for competitors, SLA compensation for SaaS clients, and negative reviews.

## What should you actually do?

For devices: change default passwords, update firmware regularly, use strong authentication (two-factor or certificates) and follow an IoT security framework. For networks: use a specialised DDoS protection service, usually cloud-based, because few organisations can absorb attacks at terabit scale on premises.

## The kiosk botnet case

The case study is the most concrete part. A Gcore client was hit by a carpet-bombing attack: UDP traffic spread across many of the client's addresses, so no single IP looked like the target while the cumulative traffic overloaded the uplinks. The attack peaked at almost one terabit per second. The key was that botnets tend to be made of similar devices doing the same thing, so Gcore's analytics found a common pattern inside the packets and blocked on it. The post-incident investigation showed the botnet was built from compromised health check kiosks.

Three things, he says, make that possible: a distributed infrastructure integrated with Gcore's CDN so no single point absorbs the load, an AI-driven analytics system that learns from each attack, and deep packet inspection that blocks on packet content rather than only IP and protocol headers. Gcore's slides put the network at 150+ points of presence, 110 Tbps of protection capacity and a maximum mitigated attack of 1.4 Tbps.

## Who should watch

Network and security engineers sizing their DDoS exposure, IoT product teams who ship devices with default credentials, and anyone who wants a clear explanation of carpet-bombing attacks.

## Related Conf42 talks

- Jonathan Williams on [IoT security threats](https://www.conf42.com/DevSecOps_2021_Jonathan_Williams_IoT_Security_Threats) at Conf42 DevSecOps 2021.
- Allon Mureinik on [DoS attacks on Node.js and how to prevent them](https://www.conf42.com/JavaScript_2024_Allon_Mureinik_4_dosattacks_nodejs_prevention) at Conf42 JavaScript 2024.
- Susie Su on [IoT and the workforce](https://www.conf42.com/DevSecOps_2023_Susie_Su_revolution_iot_workforce) at Conf42 DevSecOps 2023.

[Watch Andrey Slastenov's talk](https://www.conf42.com/DevSecOps_2023_Andrey_Slastenov_iot_5g_devices_ddos_threat_landscape)

## From Gcore

Gcore runs a global edge network with CDN and DDoS protection services, the infrastructure behind the mitigation described in the talk.

- [Gcore website](https://gcore.com/)

[Watch the talk on YouTube](https://youtu.be/cQs6JZbSClA).

## Watch the talk

[The Role of IoT and 5G Devices in DDoS Attacks: A Growing Threat Landscape](https://www.conf42.com/DevSecOps_2023_Andrey_Slastenov_iot_5g_devices_ddos_threat_landscape) at Conf42 DevSecOps 2023.
