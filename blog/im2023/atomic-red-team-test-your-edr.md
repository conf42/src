# No alerts can mean your EDR missed it - test with Atomic Red Team

Conf42 Blog, 2023-10-18. https://www.conf42.com/blog/im2023/atomic-red-team-test-your-edr

In short: Christopher Haller (Strong Crypto Innovations) at Conf42 Incident Management 2023 on testing EDR against real threat actor procedures with Atomic Red Team.

A quiet EDR console means either nothing bad happened or nothing bad was detected, and you cannot tell which without testing. At Conf42 Incident Management 2023, Christopher Haller, Offensive Security Practice Lead at Strong Crypto Innovations, showed a cheap way to find out: read the government advisories describing how real threat actors operate, look up their MITRE ATT&CK techniques in Red Canary's open source Atomic Red Team, run the matching tests on your own endpoints, and tune until the alerts fire.

It is a short, practical talk for blue teams who cannot afford a full red team engagement every time they want to check one control.

## Why is this urgent?

Haller, a US Navy veteran who did incident management at the Navy Cyber Defense Operations Command before moving to offence, frames the problem with numbers from the SANS report on the evolution of cybercriminal operations in 2023. Average breakout time, from initial infection to lateral movement, is down to 79 minutes, five minutes faster than the year before. Initial access brokers are up 147% since 2022. Use of remote monitoring and management tools such as AnyDesk, ScreenConnect and TeamViewer by attackers is up 312%, because legitimate admin tools blend in with legitimate admin traffic.

Crime has been commoditised: buy access from a broker, add ransomware-as-a-service and phishing-as-a-service, and you are in business. "All you have to be good at is just project management," Christopher Haller said at Conf42 Incident Management 2023.

## Known knowns and the false negative

He borrows the Rumsfeld matrix of known knowns, known unknowns, unknown knowns and unknown unknowns. The unknown unknowns are what keep him up at night, and attackers love them. The defender's practical version is the false negative: the control you assume works but never alerts.

The good news is that threat actor behaviour is well documented. Tactics are consistent across environments (initial access, privilege escalation, credential dumping, hunting for sensitive data), agencies publish the procedures in detail, and there are always indicators of compromise. So the gap to find is between known procedures and what your tools actually alert on or block.

## What is Atomic Red Team?

MITRE ATT&CK gives everyone a shared vocabulary for adversary tactics, techniques and procedures. Atomic Red Team, from Red Canary, supplies the smallest possible test for a single technique ID, hence atomic. At the time of the talk it covered 294 of the 750 ATT&CK IDs with 1,513 tests, more tests than IDs because one technique can be performed many ways and across several operating systems. The tests are open source on GitHub, browsable on the project website and runnable from PowerShell. Expect Windows Defender or your EDR to flag the downloaded scripts; that is the point, and you will need to allow-list them on a test machine to run them.

## Breach and attack simulation on a budget

The workflow: read a joint cyber advisory (his reference is the joint advisory on PRC state-sponsored actors living off the land, the Volt Typhoon activity), note the ATT&CK IDs it cites, find the atomics for them, run them, and see what your stack does.

Two examples. An atomic that downloads and runs Seatbelt, the C# host-survey tool, in memory: vanilla Windows Defender blocked it as malicious content, which is the result you want. And dumping the Active Directory database with ntdsutil, a living-off-the-land binary admins use legitimately. The NTDS file holds every password hash in the domain, so Haller wants an alert every single time it is copied, even when the copy is legitimate.

His conclusion is a loop: embrace the intelligence, identify the gaps, tune detection and prevention, rerun the atomics, repeat until you are confident.

## Who should watch

SOC analysts, detection engineers and IT teams who own an EDR or MDR contract and have never verified it against real procedures. Red teamers will know the material; the value is in how simple he makes the defender's version.

## Related Conf42 talks

- Josh Armitage on [red teaming AWS](https://www.conf42.com/DevSecOps_2022_Josh_Armitage_red_teaming_aws_practice_preach) at Conf42 DevSecOps 2022.
- Christopher Van Der Made on [automating threat hunting workflows](https://www.conf42.com/DevSecOps_2021_Christopher_Van_Der_Made_automate_threat_hunting_workflows) at Conf42 DevSecOps 2021.
- Kim Carter on [OWASP PurpleTeam](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam) at Conf42 Chaos Engineering 2022.

[Watch Christopher Haller's talk](https://www.conf42.com/Incident_Management_2023_Christopher_Haller_atomic_red_team_threat_actors)

## From Strong Crypto Innovations

Strong Crypto Innovations offers offensive security services, including the penetration testing, red teaming and phishing work Haller leads.

- [Strong Crypto Innovations website](https://www.strongcrypto.com/)

[Watch the talk on YouTube](https://youtu.be/Cazu31PAxBs).

## Watch the talk

[Atomic Red Team - Closing the Gap with Threat Actors](https://www.conf42.com/Incident_Management_2023_Christopher_Haller_atomic_red_team_threat_actors) at Conf42 Incident Management 2023.
