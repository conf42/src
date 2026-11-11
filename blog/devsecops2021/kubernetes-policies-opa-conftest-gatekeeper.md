# One Kubernetes policy, written twice - OPA in CI and in the cluster

Conf42 Blog, 2021-12-03. https://www.conf42.com/blog/devsecops2021/kubernetes-policies-opa-conftest-gatekeeper

In short: Noaa Barki and Shimon Tolts (Datree) at Conf42 DevSecOps 2021 on centralized Kubernetes policy with OPA, Conftest in CI and Gatekeeper at admission

Sending an email asking 400 developers to set memory limits does not prevent the next outage. At Conf42 DevSecOps 2021, Noaa Barki, full-stack developer at Datree, and Shimon Tolts, Datree's co-founder and CEO, walked through centralized policy management for Kubernetes in three steps: meet Open Policy Agent, define your policies, then decide where in the pipeline to enforce them, with Conftest in CI and Gatekeeper in the cluster. Their honest catch: you end up maintaining the same policy twice.

It is a short, friendly tour, told from the seat of a Kubernetes administrator, and it applies just as well to serverless or anything else configured in YAML or JSON.

## What does OPA actually give you?

Open Policy Agent, a graduated CNCF project, is a general-purpose policy engine. You publish policies to it, send it a JSON input, and it tells you whether the input violates any of them. You can run it as a service and query it over HTTP, or embed it as a Go package. The point is decoupling: decision logic (may this user delete that, may this Deployment ship) lives in one place instead of being rebuilt inside every microservice, which puts admins in control.

Policies are written in Rego, a declarative language. Their example flags a Deployment based on its app label. The speakers call it easy to learn from experience, and more like SQL than JavaScript.

## How granular should a policy be?

Shimon's motivating story comes from a previous job as engineering manager for 400 developers: one mistake propagated to production, emails did not help, so they turned to guardrails everyone works by. His examples: every Kubernetes workload has memory and CPU limits plus liveness and readiness probes, and every Docker container has a health check.

The second half of the advice is granularity. A blanket 4 GB memory limit will hurt the AI workload that needs 50 GB. Start with broad policies at the top and go deeper to more granular ones.

## Where should you enforce them?

This is the decision that shapes developers' day, and the talk offers two answers.

**In CI, with Conftest.** Conftest, built on OPA, tests structured files (YAML, JSON, Dockerfiles, XML and more) against Rego policies, and can push and pull policy bundles to Docker registries. Download it, write Rego, run the conftest test command on a path; it reads like a unit-testing library. Their example is a GitHub Action that pulls the Conftest image and runs it.

**At admission, with Gatekeeper.** Shift left is good, but someone will still kubectl something straight into the cluster. Gatekeeper, also from the Open Policy Agent project, sits on Kubernetes' admission controller webhook. The analogy offered is an operating system asking the antivirus whether an executable may run. You define a constraint template, for example requiring a cost-center label on every resource, and Gatekeeper rejects anything that fails it. It also has audit and test modes.

Together they protect the whole path from dev to production. The catch: Conftest and Gatekeeper policies are both Rego and almost identical, but not quite, so you keep two copies of each policy.

## The part raw OPA doesn't solve

Shimon's old setup had 400 engineers and about 1,000 Git repositories. Adding one policy with raw Conftest and Gatekeeper means wiring it into every build: in his words, opening 1,000 pull requests. What is missing is the ability to change policies dynamically and full visibility into which policies ran on which resources, what passed and what was rejected: a command-and-control layer.

That is where they place Datree. "We do policies for a living," Noaa Barki said at Conf42 DevSecOps 2021. Datree's open source CLI, which had just passed 5,000 GitHub stars, ships predefined rules, supports custom ones, and adds central management so policies can change without touching each repo. Running it is a datree test command on the files you want checked, with output pointing at each violation and how to fix it.

## Who should watch

Platform and DevOps engineers starting with Kubernetes policy who want the OPA, Conftest and Gatekeeper map in one sitting. It is an overview, not a Rego masterclass.

## Related Conf42 talks

- Eyar Zilberman on [Kubernetes schema validation](https://www.conf42.com/DevSecOps_2021_Eyar_Zilberman_kubernetes_schema_validation) at Conf42 DevSecOps 2021.
- Noaa Barki on [OPA, Conftest and Gatekeeper in action](https://www.conf42.com/Cloud_Native_2022_Noaa_Barki_open_policy_agent_conftest_gatekeeper_kubernetes_policy_in_action) at Conf42 Cloud Native 2022.
- David Melamed on [Open Policy Agent as a control engine](https://www.conf42.com/Cloud_Native_2022_David_Melamed_open_policy_agent_control_engine) at Conf42 Cloud Native 2022.

[Watch Noaa Barki and Shimon Tolts's talk](https://www.conf42.com/DevSecOps_2021_Noaa_Barki_Shimon_Tolts_centralized_policy_management_at_scale) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Datree

Datree helps prevent Kubernetes misconfigurations from reaching production, with an open source CLI, built-in rules, custom rules and central policy management.

- Datree: [datree.io](https://www.datree.io/)

[Watch the talk on YouTube](https://youtu.be/JAs462LmzLY).

## Watch the talk

[Centralized Policy Management at Scale](https://www.conf42.com/DevSecOps_2021_Noaa_Barki_Shimon_Tolts_centralized_policy_management_at_scale) at Conf42 DevSecOps 2021.
