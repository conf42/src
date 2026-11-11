# No changes outside code, no tickets - Terraform your Okta for SOC 2

Conf42 Blog, 2021-12-02. https://www.conf42.com/blog/devsecops2021/terraform-okta-instead-of-jira-tickets

In short: Travis Gary (Teleport) at Conf42 DevSecOps 2021 on passing SOC 2 audits with Terraform and pull requests instead of Jira tickets, down to Okta access

A Jira change ticket describes a change; somebody then makes it by hand with credentials a hacker could have stolen. At Conf42 DevSecOps 2021, Travis Gary, IT Director at Teleport, argued that pull requests are better change tickets and that the same infrastructure-as-code discipline teams apply to AWS belongs on the SaaS apps that control everything else, starting with Okta. His rule of thumb fits on a sticker: tickets are only for changes made outside of code.

He scopes it up front. The advice is tested on SOC 2 Type II, the certification Teleport holds; he believes it carries over to similar frameworks, while NIST and SOX are stricter. Ticketing systems still matter for support teams. And IaC pipelines hold powerful API keys that need their own protection, which the talk does not cover.

## Why did we start doing tickets at all?

"Hackers don't care about your change management process," Travis Gary said at Conf42 DevSecOps 2021. He lists the usual reasons tickets exist and takes them apart one by one.

**We already plan in Jira.** GitHub issues now do project boards, kanban, labels for automation and audit, and milestones, and they are linked to pull requests natively. Two systems means integration work for no gain.

**Change management lives in Jira.** A merged pull request approves the exact code or infrastructure change, not a description of it. A compromised developer account would still need a PR, a second reviewer and passing tests. Rollback is a revert, and the audit trail shows who approved and who reverted; GitHub's API can produce whatever CSV the auditors want.

**IT is a service organization.** Every extra team slows things down: a request filed Monday, picked up Tuesday, sent to a change advisory board, a week gone. His target is two developers, preferably on the same team, like a normal code review. Where stricter rules demand an independent approver such as an application owner, code owner files handle it. Request queues also need a 24x365 desk once your developers span time zones, which most small companies cannot staff.

**ITIL.** He suggests picturing a dead dinosaur. ITIL was built for racking servers, when a rollback meant hours of re-imaging. Now you can revert a commit and let Terraform rebuild.

## Why Okta and GitHub, specifically?

Teams that forbid console changes in AWS often still let admins click around in GitHub and Okta, which are arguably more powerful. The slide puts it plainly: if you use GitHub to manage your infrastructure, then a compromised GitHub admin owns your infrastructure. So the goal is to get rid of GitHub admins, Terraform GitHub, Okta and even Terraform Cloud itself, and remove console access across the stack.

## Terraforming Okta in three steps (plus step n)

Teleport's worked example replaces access-request tickets with attribute-based rules in Terraform:

1. **A group for every app and every role.** One base group per app (prefixed app, as in app-Salesforce) that grants least-privilege login via SAML, populated by attribute rules such as department equals sales or marketing. Bigger entitlements, like Salesforce admin, get their own group with rules or, for the odd exception, named people. Create these groups even for apps that cannot provision roles automatically: the PR history becomes the request, approval and audit system, and it is future-proof when the app catches up. The Terraform is a short loop over apps creating groups and group rules.
2. **Remove group-admin access.** IT roles such as a help-desk admin may only manage groups that Terraform does not own. A help-desk associate should not decide who gets AWS admin.
3. **Alert on changes outside Terraform.** Send Okta events to your SIEM and fire whenever anyone other than the Terraform service user changes a group; check the source IP matches Terraform Cloud too. No SIEM budget? Okta webhooks plus Zapier will do. Still run a quarterly or annual log review.

Then repeat for authentication policies, app setup and everything else until coverage hits 100%, and remove console access entirely. For incidents, keep a break-glass super-admin in 1Password, with an alert whenever those credentials are accessed: outside an incident, that is either a rule-breaker or an attacker.

## What does it buy you?

You cannot bin Jira on day one; ticket count falls as code coverage rises. The payoff Travis describes is fewer teams in the loop, work across time zones, changes that cannot bypass review, and an IT team that writes code instead of draining a queue. Teleport, he says, already spends the time it used to spend on access requests automating more systems.

## Who should watch

IT and security engineers facing a SOC 2 audit, and platform teams whose Okta or GitHub org is still run by hand. Expect a philosophy section, then real Terraform patterns.

## Related Conf42 talks

- Ismael Hommani and Tanguy Combe on [compliance as code with Cloud Custodian](https://www.conf42.com/DevSecOps_2021_Ismael_Hommani_Tanguy_Combe_compliance_as_code_cloud_custodian) at Conf42 DevSecOps 2021.
- Hila Fish on [Terraform best practices](https://www.conf42.com/Cloud_Native_2022_Hila_Fish_terraform_practices) at Conf42 Cloud Native 2022.
- Pooja Ranjan on [compliance and SaaS governance](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance) at Conf42 DevOps 2026.

[Watch Travis Gary's talk](https://www.conf42.com/DevSecOps_2021_Travis_Gary_Infraascode_Jira_tickets) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Teleport

Teleport unifies access to SSH servers, Kubernetes clusters, web applications and databases across environments, and supports mapping Okta groups to its own roles, as Travis mentions in the talk.

- Teleport: [goteleport.com](https://goteleport.com/)
- About Teleport: [goteleport.com/about](https://goteleport.com/about)
- Teleport blog: [goteleport.com/blog](https://goteleport.com/blog)

[Watch the talk on YouTube](https://youtu.be/8XEzepW_Jtk).

## Watch the talk

[Using Infra-as-code, not Jira tickets to pass security and compliance audits](https://www.conf42.com/DevSecOps_2021_Travis_Gary_Infraascode_Jira_tickets) at Conf42 DevSecOps 2021.
