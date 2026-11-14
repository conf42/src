# Azure attackers don't break MFA, they borrow your legitimate flows

Conf42 Blog, 2026-04-17. https://www.conf42.com/blog/cloud2026/azure-attackers-abuse-legit-sign-in-flows

In short: Security engineer Aleksandra Drobnjak at Conf42 Cloud Native 2026 walks through ten Azure and Entra ID attack techniques from Microsoft's MDDR 2025, with defenses.

In device code phishing, the login page is real, the certificate is valid and MFA works perfectly, and the attacker still gets your tokens. At Conf42 Cloud Native 2026, security engineer [Aleksandra Drobnjak](https://www.conf42.com/Cloud_Native_2026_Aleksandra_Drobnjak_security_zerotrust_encryption), who works across Entra ID, Defender XDR and Purview in Microsoft 365 environments, walked through ten attack techniques highlighted in the Microsoft Digital Defense Report 2025, each paired with concrete defenses.

It's a long, dense talk, built on the report but translated into settings you can check on Monday.

## Passwords still get sprayed

The report's baseline: modern MFA still cuts compromise risk by more than 99%, yet over 97% of identity attacks are still password spray or brute force. Drobnjak describes what that looks like in logs: waves of failed sign-ins from different IPs and countries, often with the BAV2ROPC user agent that signals legacy authentication, which bypasses modern MFA by design. Her first checklist covers spotting brute force in Defender for Cloud Apps, filtering Entra sign-in logs for legacy auth clients, checking basic auth protocols like SMTP, POP3 and IMAP, and conditional access policies that block legacy auth. Turning it off can break old scripts and integrations, which is exactly the window attackers wait for.

## Social engineering moved into Teams and the Run dialog

Two techniques target people. In the first, attackers flood an inbox with spam, then message on Teams or call, posing as IT support, and talk the user into a Quick Assist session. She names Storm-1811 as linked to such campaigns. Defenses: limit external Teams communication, tell users plainly that IT never asks for Quick Assist through Teams, let them report suspicious messages and calls, and approve only specific remote management tools.

The second is ClickFix: a fake error or "verify you are human" prompt tells the user to press Win+R and paste a command the page put on their clipboard. It runs PowerShell or mshta and pulls a payload into memory with no file on disk. She cites Storm-1865 and phishing that impersonated booking.com. Defenses include awareness training, PowerShell constrained language mode, and hardened enterprise browsers.

## Device codes, sessions and consent: no password needed

The identity section is the core. In device code phishing (Storm-2372), the attacker starts a sign-in, gets a device code, and persuades the victim to enter it on the genuine Microsoft page. The victim completes MFA for the attacker's session. Block the device code flow in conditional access if you don't need it, and watch sign-in logs for it.

Session hijacking skips authentication altogether by stealing tokens through adversary-in-the-middle phishing, infostealers, malicious extensions or tokens left in code. Her layers: conditional access requiring compliant devices, token protection that binds tokens to a device, Continuous Access Evaluation, Credential Guard and LSA protection, then revoke and force re-authentication when in doubt.

Consent phishing gets an attacker's app granted permissions like reading mail, and that access survives a password reset. Her takeaway: "Attackers don't always need credentials. Sometimes they just need your permission." Restrict user consent, require admin approval for sensitive scopes, review app permissions regularly, and report malicious apps to MSRC.

## Help desks, SMS codes and identities that can't do MFA

Temporary Access Passes count as strong authentication, so a convinced help desk can hand an attacker the whole chain. SMS one-time codes fall to callers asking victims to read them back, and to SIM swaps, including cases with insiders at carriers. Workload identities (service principals, managed identities) can't do MFA, often hold broad rights and rarely get reviewed; she cites Storm-0558 forging tokens. Then come proximity tricks and MFA fatigue, countered with number matching, risk-based conditional access and at least two break-glass accounts.

## After the break-in, it looks like admin work

Post-exploitation in Azure often means living off the tenant: Azure Run Command executes scripts on VMs through the agent with no open ports, which looks like an admin troubleshooting. Restrict who can run it, monitor activity logs for it and for role and service principal changes, keep logs tamper-proof and backups isolated and tested.

## Who should watch

Anyone who owns an Entra ID tenant or responds to Microsoft 365 incidents. Even if you know half the techniques, the defense checklists per technique make it a good audit companion.

## Related Conf42 talks

- [Old Services, New Tricks: Cloud Metadata Abuse by Threat Actors](https://www.conf42.com/Cloud_Native_2023_Nader_Zaveri_Brandan_Schondorfer_cloud_metadata_abuse_threat_actors) by Nader Zaveri and Brandan Schondorfer at Conf42 Cloud Native 2023.
- [Secretless Multi-Cloud Authentication with Workload Identity for DevSecOps Pipelines](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) by Venkata Velavarthipati at Conf42 DevSecOps 2026.
- [Synergizing Threat-Informed Defense: When Cloud Attack Emulation Meets Detection Engineering](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense) by Kennedy Torkura at Conf42 Cloud Native 2024.

[Watch Aleksandra Drobnjak's talk](https://www.conf42.com/Cloud_Native_2026_Aleksandra_Drobnjak_security_zerotrust_encryption) or the [YouTube recording](https://youtu.be/yaTtoU-9KHc).

## Watch the talk

[Azure Attacks Unpacked: Real-World Threats and Lessons Learned](https://www.conf42.com/Cloud_Native_2026_Aleksandra_Drobnjak_security_zerotrust_encryption) at Conf42 Cloud Native 2026.
