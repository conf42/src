# SSH keys never expire, and OpenSSH certificates have existed since 2010

Conf42 Blog, 2021-10-01. https://www.conf42.com/blog/sre2021/ssh-certificates-expire-keys-dont

In short: Allen Vailliencourt (Teleport) at Conf42 SRE 2021 on why short-lived SSH certificates beat public keys, with a ssh-keygen and bastion demo.

Go and read the authorized_keys file on one of your production servers, then ask which of those keys are still valid. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), Allen Vailliencourt, Solutions Engineer at Teleport, made the case for replacing long-lived SSH keys with short-lived SSH certificates, and showed how to do it with plain ssh-keygen and two Docker containers. The pitch: OpenSSH has supported certificates since version 5.4, released in 2010, and most teams still haven't noticed.

## What's wrong with keys?

Nothing, at first. Public key authentication replaced passwords on sticky notes, works with AWS, GCP, routers, switches and Linux boxes, and is what GitHub, GitLab and Bitbucket want you to push with. Generating an Ed25519 key is one command. The trouble is everything after:

- **People move on.** Someone leaves the SRE team for product marketing, and their key is still on every server.
- **Laptops get stolen.** Without disk encryption, the private key goes with it.
- **Sprawl.** He cites an ssh.com piece on one financial-sector customer with 3 million keys, 750,000 distinct key pairs, across 15,000 servers. Even a small shop multiplies quickly: 30 developers on 50 servers is 1,500 authorized entries to rotate, or not.
- **Keys don't expire.** One found two years later still works.

He knows the sprawl first-hand: at a previous job with eight or nine developers and 80 to 90 servers, he collected public keys over Slack and pushed them to every server with an Ansible playbook, whether people needed access or not, and rarely found time to clean up.

## What happens when a key leaks?

His war story: a new DevOps engineer committed a private key for AWS to a public test repository. Bots found it within minutes. "And within hours we had over 200 servers being spun up on AWS data centers all over the world," Allen Vailliencourt said at Conf42 SRE 2021. The team deleted the servers, killed the key and held a postmortem about .gitignore. GitHub and others now scan for secrets, but the responsibility still sits with you.

## What does a certificate add?

A certificate is your key signed by a certificate authority, carrying metadata: a key ID, the type (user or host), the principals it is valid for, and valid-after and valid-before times. Tamper with it and the signature breaks, so access is denied. The cryptography is the same; what changes is that access now has an end date. A short time to live, as he puts it, should help your security team sleep better.

Host certificates also fix the prompt everyone clicks through: the client trusts the host CA, so there is no question about an unknown host fingerprint. Certificates are not exotic either: HTTPS made them the web's default, and Netflix open-sourced BLESS for SSH, with Lyft maintaining a fork. What held smaller organisations back, he argues, is in-house expertise and tooling for issuing, storing, auditing and rotating them.

## The demo

The flow uses only ssh-keygen. Create a host CA and a user CA, then generate a host key and sign it with the host CA, passing an identity, the host flag, a list of principals (hostnames such as the app node or localhost) and a validity window, two hours in his example. User certificates are the same minus the host flag, with Linux login names as principals and a shorter window. The validity option accepts relative ranges, such as from 30 minutes before to 30 minutes after, or fixed dates.

In the demo repository, Docker Compose starts an app node and a bastion. A script copies the host CA into known_hosts, copies the certificates and writes an SSH config with a proxy jump through the bastion. With a client certificate valid for about five minutes, the login succeeds without the host prompt, and the server log shows the accepted certificate. A few minutes later the same command is refused, because the certificate has expired. No key to revoke, no file to clean up.

## Who should watch

SREs and sysadmins still distributing public keys by hand or by playbook, and anyone who has inherited a long authorized_keys file. Expect a hands-on walkthrough you can follow at home; Teleport comes in at the end as the open source access plane that extends the idea. Pair it with:

- [Linda Ikechukwu on SSH certificates](https://www.conf42.com/Cloud_Native_2023_Linda_Ikechukwu_introducing_ssh_certificates) at Conf42 Cloud Native 2023.
- [Dwayne McDaniel on git hooks that stop committed secrets](https://www.conf42.com/DevSecOps_2022_Dwayne_McDaniel_stop_committing_your_secrets_git_hooks) at Conf42 DevSecOps 2022.
- [Kenneth DuMez on automating Kubernetes user access onboarding](https://www.conf42.com/DevSecOps_2022_Kenneth_DuMez_goodbye_manual_kubernetes_user_access_onboarding) at Conf42 DevSecOps 2022.

[Watch Allen Vailliencourt's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Allen_Vailliencourt_Keys_Certs_SSH_Access) from Conf42 SRE 2021.

## From Teleport

Teleport is an open source access plane that uses short-lived certificates to unify access to SSH servers, Kubernetes clusters, web applications and databases.

- [Teleport website](https://goteleport.com/)
- [About Teleport](https://goteleport.com/about)
- [Teleport blog](https://goteleport.com/blog)
- [Teleport on Conf42](https://www.conf42.com/teleport)

[Watch the talk on YouTube](https://youtu.be/HSsyT7kI3EM).

## Watch the talk

[Keys or Certs for SSH Access? Why should I care?](https://www.conf42.com/Site_Reliability_Engineering_2021_Allen_Vailliencourt_Keys_Certs_SSH_Access) at Conf42 Site Reliability Engineering 2021.
