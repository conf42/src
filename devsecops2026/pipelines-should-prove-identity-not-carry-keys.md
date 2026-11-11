# Pipelines should prove who they are, not carry cloud keys

Conf42 Blog, 2026-09-14, updated 2026-11-09. https://www.conf42.com/devsecops2026/pipelines-should-prove-identity-not-carry-keys

In short: Venkata Velavarthipati at Conf42 DevSecOps 2026 replaces long-lived CI and MLOps cloud keys with OIDC workload identity, scoped claims and fail-closed design.

The usual question about pipeline credentials is where to store them safely. At Conf42 DevSecOps 2026, Venkata Velavarthipati, a lead cloud solution architect with about twelve years in cloud architecture and security, asked the better one: does the workload need a permanent credential at all? His answer is OpenID Connect workload identity federation, where each CI/CD or MLOps job proves who it is at runtime and receives cloud access that expires in minutes.

It's an architecture and security-model talk rather than a code walkthrough, backed by an AWS proof built with Terraform and GitHub, with the same pattern sketched for GCP and Azure.

## Rotation debt is the real cost

The traditional approach stores an access key in a secrets manager or parameter store and hands it to the pipeline. That works for one environment. Multiply it by clouds, accounts, data engineering and ML pipelines and runners, and the key ends up referenced in places nobody can list. Venkata's example will be familiar to anyone who has owned an IAM user: you lose track of where the old key is used, so you mint a second one on the same user to keep things running, and the first one lives on. Add contractors and a leaked key that sits exposed for months, and you have credential sprawl.

## Identity over credentials

The flow is short. The workload starts and gets a short-lived OIDC token describing itself. The target cloud validates the issuer, audience and workload-specific claims against a trust policy. If everything matches, it issues temporary credentials scoped to what that job needs (create one S3 bucket, nothing more) and they expire when the session ends. On AWS that's IAM and STS; on GCP, Workload Identity Federation; on Azure, Microsoft Entra federation. One identity source, several clouds, no stored keys.

Authentication alone isn't the control, though. Just because GitHub can issue a token doesn't mean every GitHub workflow deserves the same AWS access. His trust policy pins the subject to a specific repository and GitHub environment, and you can go further: only `main` reaches production, lower branches reach lower accounts. Add a session duration of 900 seconds and you get claim-level trust combined with short-lived authorization.

## The 99.99 percent number, read carefully

Venkata puts one number on the model: compare a key valid for 365 days with a 15-minute session, and the credential validity window shrinks by around 99.99 percent. What makes this section good is the caveat that follows. He's explicit that this is an exposure-window metric, not a breach probability metric. A long-lived key isn't guaranteed to be stolen, and a short one isn't guaranteed safe; the shorter window just gives least privilege, claim validation and monitoring much more to work with.

## Same pattern for training jobs

The MLOps case is the one worth stealing. A training job that reads data from another cloud or an on-prem store usually gets a secrets manager ARN baked into its environment, which is one more place for a long-lived credential to live. With workload identity, access is decided by the job's identity and can be scoped to the job, the environment and even the dataset. He deliberately shows no latency numbers here, since they vary by cloud, and calls it a reference pattern rather than a benchmark.

## Fail closed, and make it visible

Secretless doesn't mean failure-free. The identity provider can be down, STS can be slow, a runner's clock can drift, or a trust policy can be wrong. His rule: fail closed. When federation breaks, don't quietly fall back to a static key to keep the deploy moving; stop, make the failure visible and fix the trust configuration. The temptation to paste a secret back in is exactly how the old model returns.

Observability completes it. Capture identity and claim context at the federation boundary, use CloudTrail for role and API activity, and correlate each temporary session with the pipeline run that created it, so an API call is never from an anonymous-looking credential. Then watch for unexpected claims and unusual token requests. Trust relationships themselves are managed as code.

## Who should watch

Platform and DevOps teams still rotating CI access keys by hand, and ML engineers whose training jobs reach across clouds for data. If you already run OIDC federation for deploys, the MLOps section and the fail-closed argument are the parts to take back to your team.

## Related Conf42 talks

- [Access is the New Breach: Why Observability Must Start with Identity](https://www.conf42.com/Observability_2025_Cynthia_Akiotu_identity_access_breach) by Cynthia Akiotu at Conf42 Observability 2025.
- [Zero Trust MLOps: Securing AI Pipelines from Development to Production](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops) by Sudheer Obbu of JPMorgan Chase at Conf42 MLOps 2025.
- [Identity-Centric Security for AI Systems: IAM as Cybersecurity Infrastructure](https://www.conf42.com/Large_Language_Models_LLMs_2026_Arunkumar_Muthuramalingam_identity_security_iam) by Arunkumar Muthuramalingam at Conf42 Large Language Models 2026.

[Watch Venkata Velavarthipati's talk](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/gEToeVQD1wI).

## Watch the talk

[Secretless Multi-Cloud Authentication with Workload Identity for DevSecOps Pipelines](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) at Conf42 DevSecOps 2026.
