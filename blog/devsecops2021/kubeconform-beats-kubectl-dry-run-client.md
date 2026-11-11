# kubectl dry-run client mode needs your cluster anyway, so use kubeconform

Conf42 Blog, 2021-12-02. https://www.conf42.com/blog/devsecops2021/kubeconform-beats-kubectl-dry-run-client

In short: Eyar Zilberman (Datree) at Conf42 DevSecOps 2021 on Kubernetes schema validation, kubectl dry-run modes, kubeval vs kubeconform and filling the gaps

Kubernetes validates your manifest's schema every time you apply it, which is exactly when you least want to find out it is broken. At Conf42 DevSecOps 2021, Eyar Zilberman, co-founder and CPO of Datree, compared the ways to catch schema errors earlier: kubectl's two dry-run modes, and the offline tools kubeval and kubeconform. His verdict: kubeconform, plus something else to cover the checks only the API server does.

He also wears pink bunny ears throughout. That pays off at the end.

## What is schema validation, and what isn't it?

Eyar's definition: a set of unit tests that verify your manifest has the correct keys and values. His example has two bugs a schema catches: kind deployment with a lowercase d, and nameSpace with a capital S. The community writes those tests, and you can contribute more upstream.

What it does not cover: YAML syntax such as indentation, best practices such as memory and CPU limits on every container, and team policies such as pulling images only from a private registry. Those are a different flow.

## Can kubectl dry-run catch it earlier?

kubectl has a dry-run flag with client and server modes. Both do schema validation. Only server mode does the extra validations the API server performs. Neither lets you validate against a different Kubernetes version, so you cannot check today's 1.18 manifests against 1.20 before upgrading.

And then the twist: server mode needs a cluster connection, which makes sense, but client mode also needs one. It is a long-standing bug (kubernetes/kubernetes issue 51475), and with more than 1,000 open bugs on the project, Eyar would not hold his breath. That leaves client mode with no reason to exist.

## Offline tools vs the API server

kubeval and kubeconform both convert the OpenAPI (Swagger) definition in the Kubernetes project into JSON Schema files and validate against a local copy, so no cluster is needed.

His two QA rounds show the gap. A Pod with a label value of three dashes: kubectl server mode rejects it with the label regex error, both offline tools pass it. A container with no image: same result. Both checks are API-server validations you would expect in the schema, but they are not, and Eyar admits he does not know why.

So if a cluster connection is allowed, dry-run server mode wins. Most teams do not want every developer laptop or CI runner talking to production, and then the offline tools win.

## kubeval or kubeconform?

At the time of the talk the comparison was lopsided:

- **Version support.** kubeval's schema repo had its last commit in April 2020 and covered Kubernetes up to 1.18.1. kubeconform covered up to 1.22.4, the latest then, and both can be pointed at the version you plan to upgrade to.
- **CRDs.** kubeval cannot validate resources using CRDs; missing CRD support is why kubeconform was started.
- **Community.** kubeval had more than 2,000 stars and 200 forks but little activity; kubeconform had about 340 stars and a commit from eight days before the talk.

Eyar's pick is kubeconform. kubeval may be better known, but kubeconform, in his view, "still have a strong community to consider."

## Four strategies

1. **Shift left.** Even CI can be too late; run checks in the developer's environment, for example as a pre-commit hook.
2. **Fill the gap.** kubeconform misses the server-side checks, so pair it with a policy enforcement tool on every change.
3. **Alternatives.** Run a throwaway cluster with kind or minikube in CI and use dry-run server mode against it. The catch is keeping it like prod (same namespaces, volumes and so on), or it rejects valid manifests.
4. **Buy vs build.** kubeconform plus Conftest is a solid open source combination if you enjoy the engineering overhead. Datree, he says, offers it out of the box: its schema validation is powered by kubeconform, with custom rules to fill the gap. "There's no dark magic in what we are doing," Eyar Zilberman said at Conf42 DevSecOps 2021.

The bunny ears? The talk's GitHub repository is named after them so you remember it, with the slides, links and an issue tracker for questions.

## Who should watch

Anyone validating Kubernetes manifests in CI, and especially teams planning a version upgrade. It is short and very practical.

## Related Conf42 talks

- Noaa Barki and Shimon Tolts on [centralized policy management at scale](https://www.conf42.com/DevSecOps_2021_Noaa_Barki_Shimon_Tolts_centralized_policy_management_at_scale) at Conf42 DevSecOps 2021.
- Noaa Barki on [OPA, Conftest and Gatekeeper in action](https://www.conf42.com/Cloud_Native_2022_Noaa_Barki_open_policy_agent_conftest_gatekeeper_kubernetes_policy_in_action) at Conf42 Cloud Native 2022.
- Reza Ramezanpour on [Kubernetes security policy design](https://www.conf42.com/Cloud_Native_2023_Reza_Ramezanpour_kubernetes_security_policy_design_top10) at Conf42 Cloud Native 2023.

[Watch Eyar Zilberman's talk](https://www.conf42.com/DevSecOps_2021_Eyar_Zilberman_kubernetes_schema_validation) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Datree

Datree is an open source CLI that runs in CI/CD and checks every Kubernetes manifest change against the organization's policies, with schema validation powered by kubeconform.

- Datree: [datree.io](https://www.datree.io/)

[Watch the talk on YouTube](https://youtu.be/qM5blt2JL00).

## Watch the talk

[A Deep Dive Into Kubernetes Schema Validation](https://www.conf42.com/DevSecOps_2021_Eyar_Zilberman_kubernetes_schema_validation) at Conf42 DevSecOps 2021.
