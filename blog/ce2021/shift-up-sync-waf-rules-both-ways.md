# Your staging has no WAF, so your tests never see what production sees

Conf42 Blog, 2021-02-25. https://www.conf42.com/blog/ce2021/shift-up-sync-waf-rules-both-ways

In short: Swapnil Deshmukh (Certus Cybersecurity) at Conf42 Chaos Engineering 2021 on shift up, a feedback loop syncing security policy between production and non-production

Shift left puts security checks in the pipeline; red teams and chaos exercises probe production. At Conf42 Chaos Engineering 2021, Swapnil Deshmukh, CTO and co-founder of Certus Cybersecurity, argues that the two rarely talk to each other, so the same weaknesses keep flowing from non-production into production. His fix, which he calls shift up, is a continuous feedback loop: whatever one side learns becomes policy on the other.

It is a short talk, closer to a lightning talk than a tutorial, built on one idea and two stories from client work.

## Where is the gap?

Certus works with Fortune 500 companies, and the pattern he describes recurs across them. Non-production has shift left: security handed to developers and tools, with policies to follow through the whole software lifecycle. Production has red teaming, MITRE ATT&CK-style exercises, narrower threat-actor simulations, and chaos engineering, used as a pressure test of how vulnerable the infrastructure is.

Both are needed, he says. The trouble is that the lessons from each stay in their own silo, and the production exercises are point-in-time. Swapnil Deshmukh said at Conf42 Chaos Engineering 2021: "if I do my testing today, but if you push the code tomorrow itself, I would not be able to test it because the time has passed from a testing perspective itself."

## What does shift up change?

Shift up connects the two directions:

- **Production to non-production.** When production defences learn something new, say a WAF updating its rules from live attack patterns, those policies flow down so pre-production testing (pen tests, DAST) validates against them.
- **Non-production to production.** What application-level testing finds flows back up as policy in production.

This can run through APIs between matching infrastructure on both sides. He is clear that it is a journey: start manually, build up historical data on policies and controls, and only then automate the translation between the two networks.

## The WAF that was quietly misconfigured

His main story is a client whose production WAF updated its regexes automatically as it saw new attack patterns, while non-production had no WAF at all, so those policies never reached the test environment. One day the team found the WAF completely misconfigured for SQL injection, which meant traffic went straight to the application layer. What saved them was the application's own rule set: having never been able to lean on a WAF in testing, it was built to resist injection by itself.

Done properly, he says, non-production mirrors production, WAF included. Then you can test twice, with the WAF and without it, see how resilient the application is on its own, and break things freely, since taking down a non-production environment costs nothing. Both sides then sync the regexes they learn.

The counter-example is a very large telco, where a bug bounty program turned up a lot of SQL injection: Certus could get past the WAF's regexes and reach the application directly, because nothing fed what production saw back to the developers, or the other way round.

## Who should watch

Security engineers and DevSecOps teams whose pre-production environment is a simplified copy of production. It is an idea talk rather than a how-to: no tooling, no demo, and the automation is described, not shown.

## Related Conf42 talks

- Yury Nino and Jhonnatan Gil Chaves on [cloud security chaos engineering](https://www.conf42.com/Chaos_Engineering_2021_Yury_Nino_Jhonnatan_Gil_Chaves_cloud_security_chaos_engineering) at Conf42 Chaos Engineering 2021.
- Tanya Janca on [DAST in CI/CD](https://www.conf42.com/DevSecOps_2022_Tanya_Janca_dast_cicd) at Conf42 DevSecOps 2022.
- Joshua Fox on [web application firewalls](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Joshua_Fox_wafs_web_application) at Conf42 SRE 2024.

[Watch Swapnil Deshmukh's talk](https://www.conf42.com/Chaos_Engineering_2021_Swapnil_Deshmukh_shift_up_security_feedback_loop)

## From Certus Cybersecurity

Certus Cybersecurity is the security consulting firm Swapnil co-founded; the stories in the talk come from its client engagements.

- Certus Cybersecurity: [certuscyber.com](https://www.certuscyber.com)

[Watch the talk on YouTube](https://youtu.be/azofjyUDgJw).

## Watch the talk

[Shift up: Continous Security and feedback loop in production](https://www.conf42.com/Chaos_Engineering_2021_Swapnil_Deshmukh_shift_up_security_feedback_loop) at Conf42 Chaos Engineering 2021.
