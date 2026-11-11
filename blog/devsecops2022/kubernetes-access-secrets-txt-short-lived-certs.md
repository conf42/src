# If secure access isn't the easy path, secrets.txt wins

Conf42 Blog, 2022-12-02. https://www.conf42.com/blog/devsecops2022/kubernetes-access-secrets-txt-short-lived-certs

In short: Kenneth DuMez (Teleport) at Conf42 DevSecOps 2022 on why Kubernetes access breaks at scale and how SSO-backed short-lived certificates replace shared kubeconfigs

At a previous job, Kenneth DuMez's team kept a file called secrets.txt on their laptops, full of cloud access keys. Not because they were careless, but because the official way to get credentials, a vault full of badly named and half-deprecated entries, was so slow that everyone copied the ones they used most. DuMez, Developer Relations Engineer at [Teleport](https://goteleport.com/), opened his Conf42 DevSecOps 2022 talk with that file and its lesson: the most secure path has to be the simplest one, or engineers route around it. He then applied it to Kubernetes access with open source Teleport.

## What does the data say about access gone wrong?

He brings numbers from three reports:

- **Beyond Identity, 2021**: one in four employees surveyed still had access to old passwords, and 41.7% admitted to sharing workplace passwords. People leave; their credentials don't.
- **GitGuardian, 2021**: over 6 million secrets leaked on GitHub, double the 2020 count, mostly cloud keys (AWS IAM, Azure, Google Cloud, Scaleway). And if you think you are safe because your code is private, 85% of corporate leaks came from developers' personal repositories, forks of company code that were never deleted; the other 15% from public corporate repositories.
- **Datadog's 2022 container report**, covering about 1.5 billion containers across tens of thousands of companies: over half of them run Kubernetes, and around 40% of clusters still use lax privileges, such as listing all secrets, creating workloads or certificates, or requesting tokens that escalate privileges.

Every breach, he argues, shares two things: a human error for the initial infiltration, and an attempt to pivot and maximise the blast radius. From a Slack workspace to a server to elevated privileges, and then, as his slide puts it, 50/50 Bahamas or jail.

## Why is Kubernetes access so hard?

His Kubernetes iceberg has three layers. At the tip: make it work, one cluster with networking, services and users, which is hard enough. Below the surface: make it work securely, with RBAC, identity-based or passwordless access and network policies that resist attack. At the bottom: make it work securely at scale, for 40 or 100 engineers and thousands of clusters.

"Kubernetes is not safe by default," Kenneth DuMez said at Conf42 DevSecOps 2022. The configuration surface he lists is long: etcd security and secrets management, network policies, pod-to-pod communication, application-level security, RBAC, audit logging, cluster onboarding and ephemeral clusters, each a file someone edits by hand.

## How does Teleport approach it?

He frames secure access as four pillars:

- **Authentication**: no SSH keys, passwords or long-lived certificates. Teleport is its own certificate authority and issues a short-lived X.509 certificate per user and session, tied to a Teleport role mapped from the SSO identity (Okta or GitHub).
- **Authorization**: requests to servers, databases, clusters and CI/CD systems are approved or denied against the user's roles.
- **Connectivity**: traffic goes through a reverse proxy tunnel from the Teleport server to the resource, encrypted with TLS.
- **Audit**: logs from every cluster in every region stream to one place.

In the architecture he shows, a Teleport kube agent runs in the cluster; the user logs in via SSO, Teleport checks their roles, then hands them a kubeconfig so kubectl works from their own machine. For automation, Machine ID gives each CI worker its own identity and fetches a fresh credential every 20 minutes (configurable) instead of a shared one.

## What does the demo show?

DuMez logs in with tsh using GitHub SSO, lists the Kubernetes clusters his role allows, runs tsh kube login, and gets a kubeconfig. Then the audit log: the SSO login, the certificate issued, and each Kubernetes request, down to the verb get on the resource pods. The role definition maps one Teleport role to Kubernetes groups, database users, SSH logins and Windows desktops, and active sessions can be revoked.

The point he stresses: even when several people share a Kubernetes RBAC group, every command maps back to an individual identity, which is what offboarding and incident reviews need.

He closes with Teleport 11, which added GitHub Actions support for reaching SSH, Kubernetes and databases without long-lived credentials, and Kubernetes auto-discovery that onboards clusters by label.

## Who should watch

Platform teams handing out kubeconfigs by hand or through a shared vault, and security engineers who need per-person audit trails across many clusters. The first half's numbers make a good slide for anyone arguing for SSO-backed access internally.

## Related Conf42 talks

- Federico Maggi on [RBAC for distributed applications with OPA](https://www.conf42.com/Cloud_Native_2022_Federico_Maggi_distributed_application_rbac_opa) at Conf42 Cloud Native 2022.
- Reza Ramezanpour on [Kubernetes security policy design](https://www.conf42.com/Cloud_Native_2023_Reza_Ramezanpour_kubernetes_security_policy_design_top10) at Conf42 Cloud Native 2023.
- Mofizur Rahman's [Kubernetes security jumpstart](https://www.conf42.com/Cloud_Native_2021_Mofizur_Rahman_kubernetes_security_jumpstart) at Conf42 Cloud Native 2021.

[Watch Kenneth DuMez's talk](https://www.conf42.com/DevSecOps_2022_Kenneth_DuMez_goodbye_manual_kubernetes_user_access_onboarding)

## From Teleport

Teleport unifies access for SSH servers, Kubernetes clusters, web applications and databases across environments, with an open source and an enterprise edition.

- [Teleport website](https://goteleport.com/)
- [About Teleport](https://goteleport.com/about)
- [Teleport blog](https://goteleport.com/blog)
- [Teleport on YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)

[Watch the talk on YouTube](https://youtu.be/mFxVAI-NOew).

## Watch the talk

[Say Goodbye to Manual Kubernetes User Access Onboarding](https://www.conf42.com/DevSecOps_2022_Kenneth_DuMez_goodbye_manual_kubernetes_user_access_onboarding) at Conf42 DevSecOps 2022.
