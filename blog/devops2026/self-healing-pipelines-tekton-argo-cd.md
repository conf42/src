# Self-healing deploys start with Git as the only source of truth

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/self-healing-pipelines-tekton-argo-cd

In short: Srinivas Pagadala Sekar of Karsun Solutions at Conf42 DevOps 2026 on self-healing CI/CD with Tekton, Argo CD and Argo Rollouts, plus an airline case study.

The 3am page about a deployment gone sideways usually starts the same archaeology dig: what changed, who deployed it, where did it drift. At Conf42 DevOps 2026, Srinivas Pagadala Sekar, senior site reliability manager at Karsun Solutions, laid out how to write a different ending with GitOps: Tekton for CI, Argo CD for continuous reconciliation, Argo Rollouts for canaries that roll themselves back, and observability feeding every decision.

It is a long, structured talk that goes from GitOps basics to a reference architecture, six failure scenarios, an airline case study and a careful take on where AI fits. Treat it as a blueprint walk-through rather than a live demo.

## Git is the rollback button

Srinivas starts by grounding GitOps in four principles: Git as the single source of truth, declarative desired state, automated reconciliation and full auditability. The resilience payoff follows directly. Rollback is a `git revert`, every change goes through a pull request, and drift is detected because the cluster is constantly compared with the repository.

His stack has four parts: a Git repo holding code, infrastructure and manifests; Tekton pipelines, themselves Kubernetes resources, for build, test, scanning and image promotion; Argo CD as the reconciliation engine; and a cluster with Prometheus, Grafana and OpenTelemetry built in.

## Six ways a deploy goes wrong, and the GitOps answer

The scenarios are the most practical section, because each one is a real failure most teams have seen:

- **A slow memory leak** that passes testing. Argo CD health checks spot the degradation and roll back to the last good version in under two minutes, instead of a 30-minute human loop.
- **A hotfix made with kubectl** and never committed. The drift is detected within seconds, and Argo CD either alerts or reconciles back to Git.
- **Works in staging, fails in prod.** The same commit is promoted through environments, so the manifests match.
- **An exhausted database connection pool**, where pods look healthy but requests fail. Watching error rates and latency, not just pod status, catches it.
- **A canary that degrades.** Promotion halts automatically and traffic stays on stable.
- **A network partition** that leaves state inconsistent. Once it heals, reconciliation brings everything back to what Git says.

## The canary config that does the work

The Argo Rollouts walkthrough is the bit to copy. Start with 5% of traffic on the new version, watch error rates, latency and resource use, then step up through 10%, 20% and 50% with analysis at each stage. Analysis templates point at Prometheus queries for success rate. Two settings carry the safety: auto-promotion off, so a step only advances when analysis passes, and rollback on failed health checks. A slow problem that only shows under load still gets caught before the whole user base sees it.

The same layer extends to autoscaling with HPA, VPA or KEDA, and to traffic shifting with Istio or Linkerd, with every remediation written back to Git so the audit trail stays complete.

## An airline that could not take maintenance windows

The case study is a flight booking system with strict uptime commitments, holiday peaks around ten times normal load, multiple regions and heavy regulation. Before GitOps they deployed in planned windows, rollbacks took 15 to 20 minutes, and regions drifted apart.

The fix was one Git repository with an Argo CD instance per region, blue-green deployments with traffic switched on real-time metrics, automatic regional failover, and self-healing for connection pool pressure, latency spikes and memory leaks. Srinivas reports MTTR falling from 20 minutes to 90 seconds and no manual rollbacks over six months.

## AI as an advisor first

The AI section covers anomaly detection that learns normal patterns, predictive rollback based on similarity to past failed deployments, canary analysis that stretches its window when traffic is unusual, and automated root cause hypotheses. The guidance is sensibly cautious: build observability before automation, start with a manual gate, add auto-rollback to the most critical services first, test it with chaos engineering, and let AI suggest while humans decide until trust is earned.

## Who should watch

Teams running Argo CD who have not yet wired health-based rollback into it, and anyone pitching GitOps to a reluctant ops team. If you already run Argo Rollouts with analysis templates, the first half will be review; the scenarios and the adoption advice are still worth the time.

## Related Conf42 talks

- [GitOps, Kubernetes and ArgoCD](https://www.conf42.com/Kube_Native_2022_Utibeabasi_Umanah_gitops_argocd) by Utibeabasi Umanah is a good primer if Argo CD is new to you.
- [Your Rollback Is Untested and You Will Find Out at 3am](https://www.conf42.com/MLOps_2026_Artemis_Leonardou_rollback_untested_3am) by Artemis Leonardou is the healthy dose of doubt about rollbacks this talk relies on.
- [AI-Driven Self-Healing Infrastructure: The Next Evolution of SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Vijaybhasker_Pagidoju_selfhealing_infrastructure) by Vijaybhasker Pagidoju pushes further on the AI side.

[Watch Srinivas Pagadala Sekar's talk](https://www.conf42.com/DevOps_2026_Srinivas_Pagadala_Sekar_gitops_resilience_automation)

[Watch the talk on YouTube](https://youtu.be/LY48sTwSz1w).

## Watch the talk

[Building Self-Healing CI/CD Pipelines with Tekton and ArgoCD: A GitOps-native Approach to Resilience](https://www.conf42.com/DevOps_2026_Srinivas_Pagadala_Sekar_gitops_resilience_automation) at Conf42 DevOps 2026.
