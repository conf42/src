# Security chaos needs a steady state, so borrow one from CIS and ATT&CK

Conf42 Blog, 2022-03-10. https://www.conf42.com/blog/ce2022/security-chaos-steady-state-from-benchmarks

In short: Sakshyam Shah (Teleport) at Conf42 Chaos Engineering 2022 on defining steady states for security chaos experiments from CIS benchmarks and MITRE ATT&CK

Classic chaos engineering has a convenient steady state: a million requests per second, a latency graph, a CPU chart. Security has no such number, since nobody can say a system is 90% secure. At Conf42 Chaos Engineering 2022, Sakshyam Shah, Developer Relations Engineer at Teleport, proposed a way around that: take the steady state and the hypotheses from security benchmarks and frameworks your organisation already follows, such as CIS controls and MITRE ATT&CK.

The pay-off he is after is adoption. Experiments that map to existing security processes are ones a security team and its executives will actually sign off on.

## Why do security teams need chaos experiments at all?

Sakshyam's parallel: developers write unit, integration and end-to-end tests, reach full coverage, and production still crashes, which is why chaos engineering exists. Security teams buy next-gen firewalls, run vulnerability assessments, pen tests and red teams, and train everyone, and breaches keep coming. Security chaos engineering applies the same idea: experiment to validate assumptions and find the unknowns, testing whether controls already in place actually work.

The assumptions he lists will sound familiar. A new infrastructure service can be running in under five minutes. Patches go out as soon as they are available. Credentials, API keys and certificate authorities can be rotated without downtime. The WAF policy will catch cross-site scripting. The SIEM will catch credential compromise and lateral movement. A compromised application can reach only its own database. Over time, configuration drift and new workflows quietly break some of these.

## Where does resilience come into security?

Through dependencies. His example is an infrastructure access solution, which looks like a bastion or VPN but depends on identity providers, certificate authorities, MFA providers, hardware security modules, approval systems, routers, firewalls and switches. Shut down containers or VMs, disconnect network interfaces or mock a dependency outage, and see whether access keeps working, and keeps working securely.

## Why is the steady state the hard part?

Sakshyam said at Conf42 Chaos Engineering 2022: "The problem with testing these type of assumptions when it comes to security chaos engineering is how can you define and measure a steady state appropriately?" A WAF that catches XSS today faces endless bypass cheat sheets tomorrow, and there is no metric that says the current state is the best possible one. Teams then struggle with what to test, which variables to introduce, and where this fits next to compliance.

## How do benchmarks supply the steady state?

His answer is to treat benchmarks and frameworks as the definition of normal: CIS benchmarks, cloud vendor IAM best practices from AWS, Azure and Google Cloud, compliance controls such as PCI DSS, HIPAA and SOC, and frameworks such as MITRE ATT&CK, the Cyber Kill Chain and the NIST Cybersecurity Framework.

From CIS Controls v8 access control, a team may have processes for granting and revoking access, MFA for externally exposed apps, remote network access and admin access, and role-based access control. An auditor checks that these exist. A security chaos experiment checks that they hold: can another policy override the MFA requirement, and if someone deploys a new app without MFA on admin access, is it detected?

From ATT&CK's enterprise matrix, he picks credential access and the sub-technique of modifying the authentication process. Hypothesis: the SOC is alerted when authentication changes. Experiment: switch authentication from SAML to OAuth while the log server is down for 20 minutes, then restore it. Then ask the SOC whether they saw it. If not, the log shipper probably lacks retries, and an attacker's change could slip through unnoticed.

## How is this different from a pen test?

He compares the practices on a just-in-time (JIT) access request system. Vulnerability scanning looks for known vulnerabilities in it, vulnerability research for unknown ones, and a pen test for a way to bypass it through exploits, logic flaws or social engineering. Security chaos asks a different question: if the JIT system crashes, does a degraded, insecure fallback kick in that someone can misuse? It closes gaps the other practices leave rather than replacing them.

## When should a team start?

Late, by his reckoning. Using a maturity model such as SP-CMM, he argues that without baselines and hardening in place you would just be firing experiments everywhere. Security chaos works best for finding the unknowns once the knowns are implemented.

## Who should watch

Security engineers curious about chaos engineering, and chaos practitioners who want to pitch security experiments to a sceptical security team in language it already uses.

## Related Conf42 talks

- Yury Nino and Jhonnatan Gil Chaves on [chaos engineering for cloud security](https://www.conf42.com/Chaos_Engineering_2021_Yury_Nino_Jhonnatan_Gil_Chaves_cloud_security_chaos_engineering) at Conf42 Chaos Engineering 2021.
- Kim Carter on [OWASP PurpleTeam](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam) at Conf42 Chaos Engineering 2022.
- Kennedy Torkura on [defeating ransomware attacks](https://www.conf42.com/Chaos_Engineering_2022_Kennedy_Torkura_defeating_ransomware_attacks) at Conf42 Chaos Engineering 2022.

[Watch Sakshyam Shah's talk](https://www.conf42.com/Chaos_Engineering_2022_Sakshyam_Shah_steady_states_developing_hypotheses)

## From Teleport

Sakshyam describes Teleport as passwordless access to infrastructure: SSH servers, Windows servers, Kubernetes clusters, databases and web applications across all environments, the same kind of access system his resilience example is built on.

- Teleport: [goteleport.com](https://goteleport.com/)
- About Teleport: [goteleport.com/about](https://goteleport.com/about)
- Teleport blog: [goteleport.com/blog](https://goteleport.com/blog)

[Watch the talk on YouTube](https://youtu.be/cYx5gVYj97Q).

## Watch the talk

[Defining Steady States and Developing Hypotheses for Security Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2022_Sakshyam_Shah_steady_states_developing_hypotheses) at Conf42 Chaos Engineering 2022.
