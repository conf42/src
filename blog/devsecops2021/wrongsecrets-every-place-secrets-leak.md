# Every place you can hide a secret, and how each one leaks

Conf42 Blog, 2021-12-01. https://www.conf42.com/blog/devsecops2021/wrongsecrets-every-place-secrets-leak

In short: Jeroen Willemsen (Xebia) at Conf42 DevSecOps 2021 on why no single secrets store is enough, from hard-coded strings to Vault, AWS and Terraform state

Every secrets strategy is a journey, and most of them start with a password in a Java constants class. At Conf42 DevSecOps 2021, [Jeroen Willemsen](https://www.conf42.com/DevSecOps_2021_Jeroen_Willemsen_secretsmanagement), Principal Security Architect at Xebia, walks the whole route: code, Docker images, Kubernetes ConfigMaps and Secrets, HashiCorp Vault, AWS Systems Manager Parameter Store and Secrets Manager, and finally Terraform. His conclusion is that there is no single place that solves it, only places with different failure modes.

Each stop is backed by a challenge in WrongSecrets, the deliberately vulnerable app he builds with others under OWASP, where you hunt for the secret and submit it for points. The demos are short and slightly embarrassing in the useful way.

## Why is a hard-coded secret a problem if it only runs in the backend?

That is the question he says developers ask him after every review. The prototype needed an API key, it went into code or an application properties file, and nobody found the time to take it out. Moving it into a Docker build argument or environment variable feels like progress, but both end up in the image layers, where anyone who can pull the container can read them.

He lists what goes wrong: visibility (anyone with Git or registry access sees it), rotation (rotate at the API, forget a copy in code, lock the account), authorization (the people who can pull an image far outnumber the people allowed to use the secret, ex-employees with a local copy included), history (every old value stays in Git and in old images, which can make the next one guessable), auditability and identification. A secret named password tells nobody what it opens, so the usual cleanup is deleting it and waiting for something to break.

For detection he points to open source scanners: TruffleHog on the Git history, Dockle on the image, then BFG to rewrite history, with a backup at hand. He is clear that scanners miss secrets that are concatenated, encoded or encrypted with a key stored next to them.

## Are Kubernetes Secrets good enough?

ConfigMaps are not: they get committed to Git, they are readable unless RBAC is set up properly, and by default they sit unencrypted in etcd. Kubernetes Secrets are the intended tool and, in his view, a solid basis, provided you do the work: least-privilege RBAC, secrets scoped to the namespace and services that consume them, etcd encryption, a restricted security context enforced by admission controllers (or PodSecurityPolicies on older clusters), hardened worker nodes and regular validation. Add metadata saying what each secret is for, so a later migration does not turn into archaeology.

Jeroen Willemsen said at Conf42 DevSecOps 2021: "Your secrets are the diamonds in your cluster, and at some point they're just the key to the other diamonds in your cluster".

## What does Vault add, and what does it cost?

HashiCorp Vault brings static and dynamic secrets, temporary database credentials, a PKI backend, encryption as a service through the transit backend, versioned secrets, an audit trail and the ability to seal everything during an incident. His demo has a Spring Boot app authenticating with its Kubernetes service account token, which Vault checks against the Kubernetes API before issuing its own token.

The cost is configuration. All of it lives in HCL plus the Kubernetes or Terraform code that deploys it, every auth backend is a place to get revocation wrong, and developers need training. He also makes a point that is easy to miss: the secrets manager needs credentials of its own, so you always end up with a secondary secrets store for the root and break-glass secrets. Then the punchline: scroll down the WrongSecrets repository and you find the project's own Vault root tokens committed to Git.

## What goes wrong in AWS and Terraform?

Parameter Store and Secrets Manager need proper KMS encryption, rotation, CloudTrail monitoring and metadata. The common failure is the policy written in a hurry to make it work: a role that is too broad and can read far more than it should. His advice is fine-grained policies, not all attached to one role, and authentication as close to the consuming pod as possible, which is more work and more secure.

The Terraform demo is the one to watch. The secret was created through a provider that does not encrypt it, so it sits in plain text in the state file. Use providers that encrypt, and remember the pipeline that runs Terraform holds cloud credentials too. WrongSecrets keeps its own cloud secrets out of GitHub Actions for that reason.

## Who should watch?

Developers and platform engineers who own a Kubernetes cluster and have never audited where their secrets actually live. It is a broad survey with short demos rather than a single-tool tutorial, and the WrongSecrets challenges make good homework.

## Related Conf42 talks

- Dwayne McDaniel on [stopping secrets from being committed with Git hooks](https://www.conf42.com/DevSecOps_2022_Dwayne_McDaniel_stop_committing_your_secrets_git_hooks) at Conf42 DevSecOps 2022.
- Michael Levan on [Kubernetes secret management with Vault](https://www.conf42.com/Cloud_Native_2023_Michael_Levan_kubernetes_secret_management_vault) at Conf42 Cloud Native 2023.
- Jhonnatan Gil Chaves on [secrets in the cloud and Kubernetes](https://www.conf42.com/DevSecOps_2021_Jhonnatan_Gil_Chaves_secrets_cloud_kuberentes) at Conf42 DevSecOps 2021.

[Watch Jeroen Willemsen's talk](https://www.conf42.com/DevSecOps_2021_Jeroen_Willemsen_secretsmanagement), part of [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Xebia

Xebia is the consultancy behind this talk; Jeroen Willemsen works there as a Principal Security Architect.

- [Xebia website](https://xebia.com/)

[Watch the talk on YouTube](https://youtu.be/EsMS7gOBrY4).

## Watch the talk

[Secrets-management: challenges from code to cloud](https://www.conf42.com/DevSecOps_2021_Jeroen_Willemsen_secretsmanagement) at Conf42 DevSecOps 2021.
