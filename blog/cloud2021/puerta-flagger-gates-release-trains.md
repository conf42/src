# Merge at midnight, ship on Sunday morning - Flagger gates at StackPulse

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/puerta-flagger-gates-release-trains

In short: Or Elimelech and Eldad Rudich (StackPulse) at Conf42 Cloud Native 2021 on Puerta, a gating service that extends Flagger with release windows and E2E gates

Full continuous deployment from merge to production is great until someone merges at midnight and the canary goes out while the on-call is asleep. At Conf42 Cloud Native 2021, Or Elimelech, SRE Lead, and Eldad Rudich, Director of Engineering, both at StackPulse, show Puerta, their in-house gating service that plugs into Flagger's webhooks to add release windows, end-to-end test gates and developer-friendly notifications.

It's a tour of a real pipeline with the reasoning behind each gate, and a good model for anyone who has outgrown Flagger's defaults but doesn't want to replace it.

## What does the pipeline look like?

StackPulse builds a SaaS platform for SREs that it calls reliability as code: it ingests events from monitoring systems and runs automated playbooks to investigate and remediate incidents. The stack is Google Cloud with GKE, everything in Terraform, microservices talking gRPC, and no human between a merge to main and production.

The pieces are, in Elimelech's words, Lego bricks. GitHub hosts the code and CircleCI builds an OCI image per commit and pushes it to Google Container Registry. Flux watches both Git (for configuration) and the registry (for new images), updates the workload, and Flagger notices and starts a canary. During the rollout Flagger queries Prometheus for success rate and latency, with thresholds tuned to each service's SLOs; stray from them and the canary rolls back and traffic shifts to the primary.

A successful staging rollout fires Flagger's post-rollout webhook, which Puerta implements by creating a GitHub release. That release triggers a new CI build, and the whole dance repeats on production.

## Why build custom gates at all?

The motivation is cultural as much as technical. They want developers to push small PRs all day, whenever they're at their best, and rely on the gates to stop bad releases. They want only E2E-tested flows in production, deployment state that developers can actually see, full ownership from dev to prod (you build it, you run it), and an audit trail of every Flagger event for correlation and compliance.

## The release-train gate

The first gate uses Flagger's confirm-rollout webhook to hold releases outside working hours. "We don't want someone merging at midnight their commit to reach prod," Or Elimelech said at Conf42 Cloud Native 2021. The rollout waits for a 12-hour window during the day when people are around to answer for a bad deployment.

The example on screen is a canary waiting on a Friday, the start of the weekend in Israel, which will sit in the queue until Sunday morning. The effect is a simulated release train that still keeps changes small, since developers keep merging and the gate does the batching.

## E2E tests before a single percent of traffic

The second gate uses the pre-rollout webhook to trigger a CI job against each newly deployed canary. If it fails, the canary fails before any traffic reaches it. Tests use Playwright for the UI, and because every API is gRPC, the generated clients double as API test clients in the same job. That lets one run simulate a user hitting the system from the CLI, the API or the UI, and catch what unit and integration tests missed.

## Notifications developers actually read

The third gate looks trivial and wasn't. Flagger's built-in notifications weren't verbose enough, so Puerta added an event webhook that posted every event in detail to a central chat channel. Developers then complained about the noise from every microservice in dev and staging landing in one place.

The fix kept both audiences: the central channel stays for audit and for correlating incidents with deployments, and each developer gets a curated direct message saying which phase their commit is in, whether it reached staging or production, and why it failed if it did (a 500, a broken contract in an E2E test). The feedback loop got much shorter.

## Who should watch

Platform and SRE teams running Flux and Flagger who want time-based approvals or test gates without forking either project. The talk is about design choices; it doesn't walk through Puerta's code.

## Related Conf42 talks

- Leonardo Murillo on [GitOps across clouds with Crossplane and Flux 2](https://www.conf42.com/Cloud_Native_2021_Leonardo_Murillo_gitops_multicloud_crossplane_flux2), from the same event.
- Ismael Hommani and Clement Loiselet on [Flux versus Argo CD](https://www.conf42.com/DevOps_2023_Ismael_Hommani_Clement_Loiselet_flux_argocd) at Conf42 DevOps 2023.
- Ricardo Castro on [GitOps](https://www.conf42.com/Site_Reliability_Engineering_2021_Ricardo_Castro_GitOps) at Conf42 Site Reliability Engineering 2021.

[Watch Or Elimelech and Eldad Rudich's talk](https://www.conf42.com/Cloud_Native_2021_Or_Elimelech_Eldad_Rudich_open_source_gating_service_flagger) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From StackPulse

StackPulse builds a reliability-as-code platform for SREs: automated playbooks that investigate and remediate incidents from monitoring events.

- StackPulse: [stackpulse.com](https://stackpulse.com)

[Watch the talk on YouTube](https://youtu.be/Vs_kTJ8rOBw).

## Watch the talk

[How we used Open-Source tools to create Puerta, a gating service for Flagger](https://www.conf42.com/Cloud_Native_2021_Or_Elimelech_Eldad_Rudich_open_source_gating_service_flagger) at Conf42 Cloud Native 2021.
