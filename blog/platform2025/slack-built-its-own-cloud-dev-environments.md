# How Slack built its own cloud dev environments, and when you should

Conf42 Blog, 2025-08-16, updated 2026-11-09. https://www.conf42.com/blog/platform2025/slack-built-its-own-cloud-dev-environments

In short: Jayant Tyagi of Salesforce (Slack) at Conf42 Platform Engineering 2025 on remote dev VMs, 90-second warm pools, SSH agent forwarding and frontend grafting.

"Works on my machine" stops being a joke when your product spans two code bases in two GitHub Enterprise accounts and no laptop can build both. At Conf42 Platform Engineering 2025, Jayant Tyagi, Software Engineer at Salesforce on the Slack engineering team, described the remote development platform he led at Slack: one CLI command, a provisioned VM in about 90 seconds, and features no off-the-shelf cloud IDE offered.

This is a build-it-yourself story. If you use Gitpod or Codespaces you will recognise the shape; the interesting parts are the choices Slack made because it controlled the whole stack.

## Two code bases, one product

The trigger was integration after acquisitions. One product had features living in multiple repositories, some in different GitHub Enterprise accounts. Changing one side, waiting for a sync, then changing the other, glued together with feature flags, was slow. Slack's dev environment runs both code bases side by side in two Docker containers that talk to each other port to port, so the product can be tested end to end on one machine with both tool chains installed.

The broader case for cloud development environments is familiar but well put: large code bases make laptop builds take minutes or hours, iOS, Android, web and ML tool chains break with every OS patch, confidential code ends up on laptops, and new hires spend their first days installing things.

## Ninety seconds, because the VM already exists

Each developer gets an isolated workspace VM reached over an encrypted SSH tunnel, built from hardened base images that bake in whatever all flavours share. SSO, the corporate firewall and role-based access come along by default.

Speed comes from not starting cold. Slack runs on AWS Auto Scaling Groups with a warm pool of pre-provisioned VMs, prebuilt images and cached dependencies and builds, giving roughly 90-second startup. The developer runs a command with a branch name and a configuration (frontend, backend, ML), and Chef recipes and shell scripts mount volumes, fetch secrets from the secret store and install linters, hooks and utilities. Then you connect from VS Code or Cursor and the branch is already checked out. The configuration also picks the instance size, so ML work gets more cores and RAM than someone editing HTML.

## SSH agent forwarding beat OAuth tokens

A small decision worth copying: how the VM talks to GitHub. Slack evaluated a GitHub OAuth app (managed and easy, but you own token scopes, expiry, rotation and the blast radius of a leaked token) against SSH agent forwarding, where the VM uses the developer's laptop credentials over the encrypted connection. They chose agent forwarding: nothing to rotate, and git behaves exactly as it does locally.

## Frontend grafting is the custom feature

The feature Tyagi is proudest of is frontend grafting. With special query parameters, a staging or production page loads its frontend bundles (HTML, JavaScript, React) from a developer's remote VM instead of its own. You get to test your unshipped frontend against production-shaped data and configuration, which dev environments rarely have. It only works inside the company firewall, and it only exists because the platform was built in-house.

## Treat it like a product and watch the bill

The rollout advice: pilot team first, take their feedback, onboard teams in phases, and write runbooks, since some developers have never lived in a Linux terminal. On cost: environments are ephemeral with a lifetime of a week or two, they suspend after idle periods, instance sizes map to the use case, and billing dashboards with budget alerts catch growth. Environment flavours help here; he notes Uber runs six, and Slack has at least four.

The results he reported: about 75% shorter build times thanks to bigger machines and remote caching, and developers productive from day one. For this product, almost nobody develops locally any more.

His honest caveat is the best line of advice in the talk. This is a non-trivial investment; if your laptops still cope, it may not pay off yet.

## Who should watch

Platform and developer-experience teams deciding between buying a cloud IDE and building one, and anyone stuck with a multi-repo product that is painful to run locally. Small teams with one tidy repo can skip it for now.

## Related Conf42 talks

- Rizel Scarlett on [why people develop inside containers with Codespaces](https://www.conf42.com/DevOps_2023_Rizel_Scarlett_developing_inside_containers_codespaces_containerization) at DevOps 2023, the buy side of the same decision.
- Anita Ihuman's [Mirror Mirror on My local machine](https://www.conf42.com/Kube_Native_2024_Anita_Ihuman_local_machine_mirror_dev_environment) at Kube Native 2024, on mirroring production in local dev.

[Watch Jayant Tyagi's talk](https://www.conf42.com/Platform_Engineering_2025_Jayant_Tyagi_development_ides_performance)

[Watch the talk on YouTube](https://youtu.be/d_QkKuPDuH0).

## Watch the talk

[Scaling Enterprise Development with Cloud IDEs: Security and Performance at Scale](https://www.conf42.com/Platform_Engineering_2025_Jayant_Tyagi_development_ides_performance) at Conf42 Platform Engineering 2025.
