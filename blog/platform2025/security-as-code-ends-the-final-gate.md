# Security as code turns the release-day gate into pipeline checks

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/security-as-code-ends-the-final-gate

In short: Naresh Yelkoti of U.S. Bank lays out at Conf42 Platform Engineering 2025 how scanning, policy as code and secrets detection move security into CI/CD.

If your security review happens the week before release, you have not got a security process, you have a scheduling problem. At Conf42 Platform Engineering 2025, Naresh Yelkoti, Senior Information Security Engineer at U.S. Bank, argues for security as code: scans, policies, data protection and compliance checks written down, versioned and run inside the pipeline, so security stops being the last gate and becomes something every commit passes through.

## The story every platform team has lived

Yelkoti opens with an example from his own pipelines. Releases used to depend on a manual security sign-off at the end of the cycle, so problems in Terraform and container images surfaced when the code was already nearly production-ready. Fixes landed late, release dates slipped, and both developers and security engineers ended the quarter annoyed with each other.

He frames it as the dual mandate of platform engineering: the business wants faster delivery, regulators and customers want secure, compliant, resilient platforms, and those pulls collide exactly at the release gate. Security as code is his bridge between them.

## Five pillars, one pipeline

The framework has five parts: automated security integration, serverless security, infrastructure security, intelligent risk management and secrets management. The useful bit is that each comes with concrete tools rather than vibes.

- **Automated integration** means scanning in the CI/CD system you already have: GitLab security scanning, Azure DevOps security tooling, AWS Inspector.
- **Serverless and infrastructure** means checking Lambda and Azure Functions before release and enforcing policy as code on cloud configuration during deployment.
- **Secrets** means scanning for hard-coded credentials before they ever reach production, with tools such as GitGuardian, Snyk and AWS Secrets Manager.

He quotes plenty of industry figures along the way (vulnerability reductions, faster time to market, prevented misconfigurations). Treat those as the sales case for your leadership deck; the architecture is the part to take home.

## Alert fatigue is the failure mode of shift-left

The most practical section is about what happens after you add all those scanners: a flood of findings that nobody reads. Yelkoti's answer is contextual risk scoring and smarter alerting. His example: GitGuardian detected hard-coded secrets in GitLab repositories, the findings flowed into a ServiceNow workflow, and contextual prioritisation let the team fix critical exposures immediately while parking the low-risk noise. That is the bit most shift-left talks skip, and the bit that decides whether developers keep the scanner on.

He also shares an audit angle: automating container and code scanning with Prisma meant compliance teams spent far less time on audit preparation, because the PCI evidence was always current instead of assembled by hand.

## A roadmap in four phases

The rollout plan is sensible and unglamorous. Phase one is pipeline scanning, baselines and training. Phase two adds policy as code, secrets detection and feedback loops. Phase three brings risk dashboards and automated remediation. Phase four is maturity: continuous improvement, threat modelling automation and even chaos engineering. Looking forward, he points at AI-assisted vulnerability prediction and zero trust pipeline architecture, and mentions piloting anomaly detection on API traffic to separate normal behaviour from suspicious calls.

## Who should watch

Platform and DevSecOps engineers who own a CI/CD system in a regulated shop (PCI, HIPAA, SOC 2), and security teams trying to get out of the release-blocker business. It is an overview rather than a hands-on demo, so experienced AppSec folks will know most of the tools; the alert-triage and audit-evidence examples are what earns the time.

## Related Conf42 talks

- [How to implement Security as Code?](https://www.conf42.com/Cloud_Native_2023_Christoph_Hartmann_security_as_code) by Christoph Hartmann, Conf42 Cloud Native 2023
- [Infrastructure as Code (IaC) Security Best Practices and Strategies](https://www.conf42.com/DevSecOps_2023_Joshua_Arvin_Lat_iac_security_best_practices) by Joshua Arvin Lat, Conf42 DevSecOps 2023
- [The Secret to Handling Dynamic Secrets](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security) by Rosemary Wang, Conf42 Cloud Native 2025

[Watch Naresh Yelkoti's talk](https://www.conf42.com/Platform_Engineering_2025_Naresh_Yelkoti_transforms_code_bulletproof)

[Watch the talk on YouTube](https://youtu.be/B3JDyvm4ARs).

## Watch the talk

[Building Bulletproof Pipelines: How Security as Code Transforms Platform Engineering at Scale](https://www.conf42.com/Platform_Engineering_2025_Naresh_Yelkoti_transforms_code_bulletproof) at Conf42 Platform Engineering 2025.
