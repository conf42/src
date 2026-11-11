# Minimum viable security is five jobs in your CI pipeline

Conf42 Blog, 2022-01-27. https://www.conf42.com/blog/python2022/minimum-viable-security-in-ci

In short: David Melamed (Jit) at Conf42 Python 2022 on minimum viable security, wiring Bandit, Gitleaks, Safety, ZAP and an MFA check into GitHub Actions

Startups ship features first and security when a customer asks, which is rational right up to the first incident. At Conf42 Python 2022, David Melamed, co-founder and CTO of Jit, proposed a middle path he calls minimum viable security: like an MVP, the smallest set of controls that keeps you from embarrassing yourself, added on day zero and grown iteratively. Then he built it live, as a GitHub Actions workflow guarding a deliberately vulnerable FastAPI app.

"Start minimal and add security iteratively," David Melamed said at Conf42 Python 2022. Security is a continuous investment, he argues, and it costs less if you start managing it early, as long as you do not try to boil the ocean on the first day.

## Where are the risks in a typical cloud app?

He maps a standard containerised setup end to end: a manager grants a developer access, code lands in GitHub or GitLab, CI builds an image into a registry, microservices run in the cloud behind an API gateway. Every hop carries risk: access nobody revokes when a developer leaves, credential theft, typosquatted packages, code vulnerabilities, infrastructure-as-code misconfigurations, supply chain attacks on the pipeline, data leakage at runtime and unauthorized access at the edge. He groups them into layers (code, pipeline, runtime, third parties, operations) and picks a short starter list across them.

## Which controls make the minimum?

The demo stack, each one a job in a `security.yaml` workflow triggered on push:

- **Bandit** for static analysis of Python, an open source linter with 35 built-in rules.
- **Gitleaks** for hard-coded secrets, around 100 regular expressions for services like AWS, Slack and GitHub, including in git history.
- **Safety** for known vulnerabilities in dependencies, with an open source database updated monthly and a commercial one updated more often.
- **OWASP ZAP** for dynamic API scanning, which reads the OpenAPI spec to find endpoints, with 17 built-in rules.
- **A custom MFA check** that calls the GitHub API with an admin-read token and fails if any organisation member has two-factor disabled.

KICS gets a mention for infrastructure as code, with 2,000+ queries across CloudFormation, Terraform, Kubernetes, Docker and Ansible, but stays out of the demo.

## What did the pipeline find?

The target is a small movies API on FastAPI with IMDb data, flawed by design, and every job failed, as intended. Bandit reported three medium-confidence issues, flagging possible SQL injection where user input was formatted straight into a query. Gitleaks found the planted AWS key, and David's advice there is the bit people skip: deleting the key from the repo is not enough, because it is already on GitHub, so disable it and issue a new one.

ZAP ran against the app as a GitHub Actions service container with a health check, crawled the endpoints from FastAPI's generated OpenAPI JSON, tried SQL injection on the title search and opened a GitHub issue with its findings. Safety flagged a package for writing Alexa skills that pulled in a vulnerable pyOpenSSL, fixed by bumping the version. The MFA job named the user without two-factor.

One practical note he adds himself: the MFA check belongs on a schedule, not on every push, since your org's MFA status does not change with a commit. He put it on push only to show everything in one run.

## Who should watch

Python teams with no security tooling at all who want a concrete first workflow they can copy, and engineers who need to argue for day-zero security with something more convincing than a checklist. The tools are open source and run in any CI that runs containers; Jit, his company, appears at the end as a platform that automates the same approach.

## Related Conf42 talks

- Gajendra Deshpande on [security considerations in Python packaging](https://www.conf42.com/Python_2022_Gajendra_Deshpande_security_considerations_packaging), from the same event.
- Joshua Arvin Lat on [pragmatic security automation in the cloud](https://www.conf42.com/Python_2022_Joshua_Arvin_Lat_pragmatic_security_automation_cloud).
- Kim Carter on [OWASP PurpleTeam security tests in CI](https://www.conf42.com/Chaos_Engineering_2022_Kim_Carter_owasp_purpleteam) at Conf42 Chaos Engineering 2022.

[Watch David Melamed's talk](https://www.conf42.com/Python_2022_David_Melamed_minimum_viable_security_applications) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From Jit

Jit builds a continuous security platform for developers that automates security controls like these in the pipeline.

- Jit: [jit.io](https://www.jit.io)

[Watch the talk on YouTube](https://youtu.be/kUyCyTezQSo).

## Watch the talk

[Minimum Viable Security for Python Applications](https://www.conf42.com/Python_2022_David_Melamed_minimum_viable_security_applications) at Conf42 Python 2022.
