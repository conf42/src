# Your GitHub Actions secret is already in 13 places

Conf42 Blog, 2023-01-25. https://www.conf42.com/blog/devops2023/github-actions-secrets-short-lived-certs

In short: Kenneth DuMez (Teleport) at Conf42 DevOps 2023 on replacing static GitHub Actions secrets with short-lived certificates from Teleport Machine ID

The safest secret in a CI pipeline is the one that doesn't exist. Kenneth DuMez, Developer Relations Engineer at [Teleport](https://goteleport.com/), made that case at Conf42 DevOps 2023: GitHub's encrypted secrets are better than plaintext, but any long-lived credential will eventually leak, so the fix is to stop storing them and have the runner fetch short-lived certificates instead. He then shows it working with Teleport Machine ID.

It is a vendor talk with a vendor demo, but the first half is a tidy argument any team running GitHub Actions can use, whatever they end up buying.

## How big is the secret-leak problem?

DuMez starts with numbers. HG Insights data showed a 71.88% rise in companies using GitHub Actions over twelve months, to 9,406 tracked companies. Then GitGuardian's 2022 State of Secrets Sprawl report: 6 million secrets leaked in 2021, double the 2020 figure. A typical company with 400 developers and four AppSec engineers found 1,050 unique leaked secrets, each appearing on average 13 times across the code base, which works out at 3,413 secrets per AppSec engineer per year.

"Those poor appsec engineers need a break," Kenneth DuMez said at Conf42 DevOps 2023.

## What is wrong with GitHub encrypted secrets?

Nothing dramatic, which is the point: the problems are structural. He lists four.

- **Redaction is best effort.** GitHub tries to mask secrets in run logs, but values get mutated and transformed during a run, and accidental exposure happens.
- **Dynamic credentials escape.** Sign a JWT with a stored private key and the JWT itself is not registered as a secret, so it can end up in stdout or stderr unredacted.
- **No chain of custody.** Anyone with write access to the repository can read every secret configured in it, which makes auditing who used what close to impossible at the scale of hundreds of engineers.
- **Duplication.** The same credential usually also lives in a password vault so humans can reach the resource by hand. When an engineer leaves or a key leaks, rotation means hunting down every copy, and every copy is more attack surface.

Scanners such as GitGuardian help, and he says they are not mutually exclusive with anything else, but they are reactive. A hit still pages someone to rotate the credential and scrub it from Git history, which anyone who has rewritten commits on a shared repository knows is its own small incident.

## What replaces the static secret?

His answer is to remove the long-lived credential entirely. With Teleport Machine ID (GitHub Actions support arrived in Teleport 11), each infrastructure resource joins a Teleport cluster, and the CI worker gets short-lived certificates it renews on a cadence. For Kubernetes, the bot refreshes its kubeconfig from the Teleport host. Nothing persistent sits in the repository, and every action lands in an audit log, so automated workers get the same chain of custody as humans.

## What does the demo show?

The walkthrough is short and concrete:

1. Write a join token resource in YAML (role bot plus kube, the join method, the bot name and the GitHub repository allowed to use it) and create it with tctl, then confirm it with a token listing.
2. Add a bot with tctl bots add, giving it a role and an SSH login. DuMez uses the default access role for the demo and is explicit that production should get a least-privilege role and a username created for the bot alone.
3. A workflow uses two Teleport actions: one installs Teleport on the runner, the other fetches Machine ID credentials for the bot. The job lists reachable SSH nodes, then SSHes into one and writes the triggering commit SHA to a file.

After a push to main the job runs green with no secret in the repository, and the Teleport audit log shows the certificate being issued, the session starting, and the exact command run on the node.

## Who should watch

Platform and DevOps engineers whose GitHub Actions workflows hold cloud keys, kubeconfigs or SSH keys, and security folks tired of rotating the same credential in five places. If you already use OIDC federation to your cloud provider, the argument will feel familiar; the demo extends the same idea to SSH nodes, databases and Kubernetes clusters behind Teleport.

## Related Conf42 talks

- Chris Ayers on [CI/CD with GitHub Actions](https://www.conf42.com/DevSecOps_2022_Chris_Ayers_cicd_github_actions) at Conf42 DevSecOps 2022.
- Michael Levan on [Kubernetes secret management with Vault](https://www.conf42.com/Cloud_Native_2023_Michael_Levan_kubernetes_secret_management_vault) at Conf42 Cloud Native 2023.
- Rob Earlam on [multi-cloud deployments with GitHub Actions](https://www.conf42.com/Cloud_Native_2023_Rob_Earlam_multicloud_deployments_github_actions) at Conf42 Cloud Native 2023.

[Watch Kenneth DuMez's talk](https://www.conf42.com/DevOps_2023_Kenneth_DuMez_static_shared_secrets_github_actions)

## From Teleport

Teleport unifies access for SSH servers, Kubernetes clusters, web applications and databases across environments, with an open source and an enterprise edition.

- [Teleport website](https://goteleport.com/)
- [About Teleport](https://goteleport.com/about)
- [Teleport blog](https://goteleport.com/blog)
- [Teleport on YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)

[Watch the talk on YouTube](https://youtu.be/R8Y-dvN9enw).

## Watch the talk

[Why you should never use static shared secrets in GitHub Actions](https://www.conf42.com/DevOps_2023_Kenneth_DuMez_static_shared_secrets_github_actions) at Conf42 DevOps 2023.
