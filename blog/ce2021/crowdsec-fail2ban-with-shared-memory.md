# CrowdSec, or Fail2ban with a crowd-sourced memory

Conf42 Blog, 2021-02-26. https://www.conf42.com/blog/ce2021/crowdsec-fail2ban-with-shared-memory

In short: Thibault Koechlin (CrowdSec) at Conf42 Chaos Engineering 2021 on detecting attacks from logs locally and sharing only blocked IPs to build a crowd-sourced reputation feed

Every server on the internet gets scanned by the same botnets, and each one learns that on its own. At Conf42 Chaos Engineering 2021, Thibault Koechlin, CTO of CrowdSec, presents the open-source engine that reads your logs, detects attacks, lets you choose how to respond, and shares only one thing with everyone else: which IP you blocked, when, and for which scenario. Thousands of installs doing that, he argues, add up to threat intelligence no single defender could build.

It is the company's own project, shown by its CTO, with a live demo that makes up most of the middle.

## Why do defenders keep losing?

He lists what favours the attacker. Time: a weaponised exploit usually arrives long before every system is patched. Unfiltered access: many compromises go through applications a firewall lets straight in. The vanishing perimeter of public cloud. And money: attackers use their own time, stolen resources and free or stolen software, while defenders pay for teams, licences and upkeep.

Thibault Koechlin said at Conf42 Chaos Engineering 2021: "when you are attacking you need to be right only once, while when you are defending you need to be right every time."

His answer is that the castle model is over: every asset has to defend itself, and HTTP, spoken by the most vulnerable device and the newest smartwatch alike, is where to start.

## How does the engine work?

Think Fail2ban, he says, with the parts pulled apart:

- **The agent** reads logs (a web server file, AWS CloudTrail, more or less any stream), normalises and enriches them, and matches them against scenarios. Those range from brute force to distributed web vulnerability scans, targeted exploitation, and business attacks like credential stuffing or credit card abuse.
- **The local API** turns alerts into decisions and syncs with the central API.
- **Bouncers** enforce decisions where they make sense, because you rarely react where you detect, and the right response depends on your business. Ban the IP, show a CAPTCHA, or, in a corporate setting where the attacker is a botnet anyway, force multi-factor authentication on the targeted account.
- **The hub** shares scenarios, parsers and bouncers written by the community; external contributors were already sending all three.

The software is MIT-licensed.

## What does the demo show?

A Debian box with Nginx, MySQL and SSH. The install wizard spots the services, finds their logs and installs a collection for each. A Nikto scan gets flagged for its user agent, probes of missing and sensitive files, and crawling; the cscli command line shows the ban and lets him drill into each alert.

Detection alone doesn't stop anyone, so he installs the Nginx bouncer from the hub, restarts Nginx, and the attacker gets a 403. He adds the iptables collection with one cscli command, runs Nmap, and the port scan is caught and banned as well, for a new reason. Then come Metabase dashboards deployed with Docker (with a stranger's IP turning up during the demo, uninvited), replay of his web server's logs from January 2019 to check scenarios for false positives before trusting them, and Prometheus metrics on lines read, parsed and fed into scenario buckets.

## Who decides an IP is bad?

The crowd part is the point. Context changes fast: an IP attacking now was probably a legitimate machine until it got hacked, and will be clean again once its owner notices. CrowdSec treats an IP as good again after 72 hours without reports.

Against false positives and poisoning, he describes several layers. Each contributor gets a trust rank built on signals that are hard to fake, such as how long they have reported and whether others, especially higher-ranked users, report the same IPs. A honeypot network, first used to bootstrap consensus, now fills coverage gaps and can be spun up across public clouds when a big new vulnerability lands. Canaries, an allowlist of things never to ban, such as Google's SEO bot, also expose community scenarios prone to false positives. A predictive algorithm links low signals, like one IP fingerprinting, another exploiting and a third using the backdoor.

On privacy, the French team is firm. Thibault Koechlin said at Conf42 Chaos Engineering 2021: "CrowdSec never ever sends your log to the platform." What leaves your machine is the blocked IP, the scenario and the timestamp.

He was open about the business side too: features for managing large fleets of installs, and API access to the reputation database for people who want it without contributing.

## Who should watch

Ops and security engineers running internet-facing Linux boxes who already use Fail2ban and want something more modular. The demo is a quick tour of setting it up.

## Related Conf42 talks

- Andrey Slastenov on [IoT, 5G and the DDoS threat](https://www.conf42.com/DevSecOps_2023_Andrey_Slastenov_iot_5g_devices_ddos_threat_landscape) at Conf42 DevSecOps 2023.
- Joshua Fox on [web application firewalls](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Joshua_Fox_wafs_web_application) at Conf42 SRE 2024.
- Jonathan Vila on [securing microservices with a zero-trust approach](https://www.conf42.com/Kube_Native_2023_Jonathan_Vila_secure_microservices_zerotrust_approach) at Conf42 Kube Native 2023.

[Watch Thibault Koechlin's talk](https://www.conf42.com/Chaos_Engineering_2021_Thibault_Koechlin_crowd_power_internets_zero_trust_architecture)

## From CrowdSec

CrowdSec is the open-source security engine and crowd-sourced IP reputation network shown in the talk; the code, the hub's scenarios and the bouncers are public.

- CrowdSec: [crowdsec.net](https://crowdsec.net)
- CrowdSec on GitHub: [github.com/crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec)

[Watch the talk on YouTube](https://youtu.be/CpcJhMyCw3M).

## Watch the talk

[Leveraging the crowd power to regain faith in Internet’s zero trust architecture](https://www.conf42.com/Chaos_Engineering_2021_Thibault_Koechlin_crowd_power_internets_zero_trust_architecture) at Conf42 Chaos Engineering 2021.
