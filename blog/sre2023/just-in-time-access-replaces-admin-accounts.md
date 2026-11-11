# For now turns into forever, so make admin access expire

Conf42 Blog, 2023-05-04. https://www.conf42.com/blog/sre2023/just-in-time-access-replaces-admin-accounts

In short: Travis Rodgers (Teleport) at Conf42 Site Reliability Engineering 2023 on replacing standing admin accounts with approved, expiring just-in-time access

Every SRE team has a shared kubeconfig somewhere that it would rather not talk about. At Conf42 Site Reliability Engineering 2023, Travis Rodgers, Developer Relations Engineer at Teleport, made the case for getting rid of standing privileged access altogether: everyone gets least privilege, anything more is requested, approved by someone else and expires on its own, and chat tools carry the approvals so nobody drowns in tickets.

The first half is vendor-neutral; the second half demos how open source and enterprise Teleport implement it.

## What does the end state look like?

Instead of history and definitions, he opens with four requirements:

1. Everyone has a least-privilege policy, privileged users included.
2. Privilege can be elevated on request and approval.
3. Elevated privilege is just-in-time, temporary, never perpetual.
4. Automation eases the request-and-approve workflow.

The first point is aimed at admins as much as anyone. Someone has to create accounts and assign roles, but that does not mean blanket access to everything. His example is a role for production Kubernetes clusters that nobody holds by default and everybody has to request, which shrinks the attack surface of production to the people who asked today.

## Why does access sprawl in the first place?

Because working out exactly what someone needs is slow, and handing over a whole group is fast. He tells it from the receiving end: as an SRE seconded to a developer project, he needed Azure storage access, had to file a ticket with the SRE team, and waited days. The fix that eventually came was the convenient one.

"I'll just give you admin access for now, and for now turns into perpetually," Travis Rodgers said at Conf42 Site Reliability Engineering 2023.

The other leak is shared secrets: a PIM key or a kubeconfig handed across with "Oh, you need admin access. Just use mine for now." Now the audit trail shows the wrong person, and the credential outlives the task. Multiply the ticket approach by 20 engineers a day, he notes, and the approvers get nothing else done, which is why requirement four exists. The automation stays partial on purpose: the security comes from a second human approving.

## Doesn't a hacked privileged account still win?

He raises the objection himself and answers it with identity. A password only claims to be you; it can be shared or stolen. Remove passwords, keys and other shared secrets, force users and machines to prove identity (biometrics, hardware security keys, SSO), and RBAC plus just-in-time access start to mean something.

## How does Teleport implement it?

Teleport puts an identity-aware proxy in front of servers, Kubernetes clusters, databases, Windows desktops and web applications. Users authenticate with WebAuthn or SSO, and a built-in certificate authority issues short-lived certificates, so there are no static credentials to pass around. Logging in through GitHub SSO in the demo gets him a certificate valid for 12 hours.

Three scenarios follow:

- **Open source, CLI.** Bob from security needs the minikube dev cluster for an hour to run scans. His role only allows him to request the Kubernetes dev admin role. He runs a request create with tsh, giving a reason; an admin lists pending requests with tctl and approves it. Bob's certificates refresh, the cluster appears in his kube list, and the role shows 51 minutes left. Admins can also deny with a reason, such as a cluster upgrade in progress.
- **Enterprise, Slack.** Alice, a project manager, requests the same role from the web UI. The approvers get a Slack message with the user, role and reason, approve it from a link, and she assumes the role with 56 minutes on the clock.
- **Resource-based requests.** Tim the contractor never sees roles at all, only the servers he may ask for. He requests one, it is approved through Slack, he logs in, and the session lands in the audit log, where it can be played back command by command.

Beyond Slack, the access request plugins he lists cover Mattermost, Microsoft Teams, Jira, PagerDuty, email and Discord, and the Teleport API lets you script custom approval workflows in a language of your choice.

## Who should watch

SREs who are the approval queue for other people's access, and platform or security engineers trying to retire shared admin accounts without becoming a bottleneck. The principles in the first half apply whatever tool you use; the demos are Teleport-specific. Pair it with Teleport colleague [Kenneth DuMez on Kubernetes user access onboarding](https://www.conf42.com/DevSecOps_2022_Kenneth_DuMez_goodbye_manual_kubernetes_user_access_onboarding), [Linda Ikechukwu on SSH certificates](https://www.conf42.com/Cloud_Native_2023_Linda_Ikechukwu_introducing_ssh_certificates) and [Nick Bergam on providing secure access](https://www.conf42.com/Cloud_Native_2022_Nick_Bergam_trust_by_verify_provide_secure_access).

[Watch Travis Rodgers's talk](https://www.conf42.com/Site_Reliability_Engineering_2023_Travis_Rodgers_automated_justintime_access_requests)

## From Teleport

- [Teleport](https://goteleport.com/): identity-based access for SSH servers, Kubernetes clusters, databases and web applications.
- [About Teleport](https://goteleport.com/about)
- [Teleport blog](https://goteleport.com/blog)
- [Upcoming events](https://goteleport.com/about/events)
- [Teleport on YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)

[Watch the talk on YouTube](https://youtu.be/3ySS8c5Ja0E).

## Watch the talk

[Replacing Privileged Users With Automated Just-in-Time Access Requests](https://www.conf42.com/Site_Reliability_Engineering_2023_Travis_Rodgers_automated_justintime_access_requests) at Conf42 Site Reliability Engineering 2023.
