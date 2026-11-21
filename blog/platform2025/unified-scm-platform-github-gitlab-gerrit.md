# Treat GitHub, GitLab and Gerrit as one platform, not three tools

Conf42 Blog, 2025-08-08, updated 2026-11-09. https://www.conf42.com/blog/platform2025/unified-scm-platform-github-gitlab-gerrit

In short: Vasdev Gullapalli of Qualcomm at Conf42 Platform Engineering 2025 on unified access, policy and event-driven automation across Git systems for 50K+ engineers.

Source code management is where every developer starts and ends their day, yet many companies still run it as an IT tool. At Conf42 Platform Engineering 2025, Vasdev Gullapalli, Senior Staff DevOps Engineer and Manager at Qualcomm, explained how his global team runs GitHub, GitLab and Gerrit for a user base of more than 50,000 engineers (closer to 100,000 accounts once bots and service accounts are counted) as a single platform with unified access, policy and automation.

His thesis, stated bluntly: "SCM is considered as platform. It's not a tool." If you treat it as infrastructure or just another application, he argues, you already have a problem.

## The license lifecycle is developer experience

The first section is about something unglamorous that every large org gets wrong: user management. A developer cannot write a line until they have an SCM license, so activation has to be self-service. Licenses cost money, so deactivation has to be automatic too. And when someone rejoins a project, reactivation has to be just as easy. Cover all three cases, automate them, and onboarding stops depending on the one operations person who knows the process.

The same goes for the next steps of a new developer: which repository to use, read versus push permissions, which CI/CD templates exist, how Git objects are managed. Qualcomm publishes this through public internal repositories with pages and READMEs, so people do not have to ask around.

## Unified access and the minimum security baseline

Across the three systems the goal is one identity model: SCIM provisioning everywhere, SSO so a login in one system carries to the others, and project classification that says how sensitive a codebase is and whether it can be cloned locally. External collaboration, such as working with a partner company, needs explicit controls like GitHub's guest collaborator model so outsiders only see what they should.

Governance is built around a minimum security baseline agreed with the security team. His example policy: no public repositories in any GitHub org, only internal and private ones. Shift-left scanning runs on every push, using built-in options such as CodeQL and GitHub Advanced Security, because a bug found at push time is much cheaper than one found after release. Audit dashboards are centralised, since security, DevOps, developers and product managers all want different views of the same data.

## Automation as event listeners and runbooks

The automation story is the most transferable part. Vasdev's team runs an event-based listener on SCM events, with a runbook per event type:

- A user is created, so the system sends them the onboarding documentation.
- Someone creates a fork in a place it is probably not needed, so they get a proactive note suggesting a better location.
- An IP allowlist on a GitHub repository is changed, removing addresses, so security and the service owners are notified and can ask why.

None of these is exotic, which is the point: small, specific reactions to events, written once, run forever.

## Balance security with developer friction

He is candid that policy can backfire. AI code review is his example: a reviewer bot with strict generic policies floods developers with comments on code they consider fine. The fix is to scope policies at the repository, org or enterprise level and embed configuration per project in CI/CD, with input from developers and leads, rather than one global ruleset.

## The results

Vasdev reports access sprawl down 46%, user onboarding that used to take hours or even days now done in under 30 minutes, and incident response times down 73%, helped by AI chatbots fed with knowledge-base articles. Next on the list: predicting user load and security events from logs with AI tools the team has built.

## Who should watch

Anyone who runs more than one Git platform, or one Git platform for thousands of people. Platform teams fighting license sprawl and access tickets will find specific, copyable patterns here.

## Related Conf42 talks

- [Leo Diaz Longhi on GitHub as a platform engineering platform](https://www.conf42.com/DevOps_2024_Leo_Diaz_Longhi_github_platform_engineering) at Conf42 DevOps 2024.
- [Peter De Tender on GitHub Dependabot, CodeQL and built-in security features](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql) at Conf42 DevSecOps 2025.
- [Dewan Ahmed on preventing accidental secret commits with Gitleaks](https://www.conf42.com/DevSecOps_2024_Dewan_Ahmed_securing_gitleaks_repos_secret) at Conf42 DevSecOps 2024.

[Watch Vasdev Gullapalli's talk](https://www.conf42.com/Platform_Engineering_2025_Vasdev_Gullapalli_scm_git_policies), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/JjRDwRTinKo).

## Watch the talk

[Platform Engineering Meets SCM: Unified Policies, Access, and Automation Across Git Systems](https://www.conf42.com/Platform_Engineering_2025_Vasdev_Gullapalli_scm_git_policies) at Conf42 Platform Engineering 2025.
