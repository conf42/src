# Two cloud databases from one git push, with Flux and Crossplane

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/gitops-crossplane-flux-cloud-databases

In short: Leonardo Murillo (Qwinix) at Conf42 Cloud Native 2021 on GitOps for multi-cloud resources, live-provisioning RDS and Cloud SQL from manifests in git

What if creating a database in AWS and another in Google Cloud took nothing but a commit, and deleting them took nothing but another one? At Conf42 Cloud Native 2021, Leonardo Murillo, CTO at Qwinix and co-chair of the CNCF GitOps Working Group, showed exactly that: an empty k3s cluster and an empty repository, Flux to keep the two in sync, and Crossplane to turn Kubernetes manifests into Amazon RDS and Cloud SQL instances.

Most of the talk is a live demo, and the rule he holds himself to is the interesting part: after the first bootstrap command, he never touches the cluster directly.

## What GitOps actually requires

Murillo frames GitOps as four principles. The desired state is declarative: you describe what the system should look like, not the steps to get there. That state is immutable and versioned: once committed, it never changes, and the only way forward is a new commit. Automated agents continuously reconcile the declared state with what is running. And there is no other way in: every change goes through a declaration in the repository.

The tools map onto that. Crossplane, created by Upbound and donated to the CNCF, exposes cloud resources as Kubernetes custom resource definitions, for AWS, Google Cloud, Azure, Alibaba and more. Flux, created by Weaveworks (the company that coined the term GitOps) and by then a CNCF incubating project, watches a repository path and makes the cluster match it.

## Bootstrapping, then hands off the cluster

The Flux CLI bootstraps the cluster against a GitHub repository, branch and path. Flux installs its controllers (Helm, Kustomize and others) and commits its own manifests back to the repo, so repo and cluster start consistent.

The path is the useful design choice. Several clusters can live in one repo under different paths, or a fleet of clusters can point at the same path, so one file change updates them all. He recommends a directory structure that means something, following Flux's own pattern: a flux-system directory for the flux-system namespace, a crossplane-system directory for Crossplane.

## Installing Crossplane without running helm install

Crossplane's docs recommend Helm, and the fourth principle forbids running it by hand. So the install is two Flux objects: a HelmRepository with the same URL you would pass to helm repo add, and a HelmRelease naming the Crossplane chart and version. Push, wait for the reconcile loop, and Crossplane pods appear. Even the namespace came from a pushed manifest first.

## Providers, configs and secrets

Crossplane talks to each cloud through a provider (one package for AWS, one for Google Cloud) and a provider config that points at a secret holding credentials, plus a project ID for Google Cloud. One provider can have several provider configs, which he highlights as a way to use different billing accounts or identities and restrict who can provision where.

## The payoff: RDS and Cloud SQL from YAML

The database manifests are a CloudSQLInstance and an RDSInstance, each naming its provider config and parameters such as engine version and region. After a commit and a minute or two, both databases appear in the AWS and Google Cloud consoles.

The feature he calls super powerful is the connection secret reference: Crossplane pulls the endpoint, port, username and password from the cloud provider and writes them into a Kubernetes secret, so applications can connect without anyone copying credentials around.

Clean-up is the same move in reverse. Delete the two manifests, push, and Flux reconciles the databases out of existence.

"I did not interact with the cluster directly at all," Murillo said at Conf42 Cloud Native 2021, pointing at what he got in return: auditability, versioning, and a history of how the platform evolved.

## Who should watch

Platform engineers who already run GitOps for applications and want the same model for cloud infrastructure, or Terraform users curious about a Kubernetes-native alternative. It is hands-on and moves fast; the Crossplane and Flux versions have moved on, but the workflow holds. His demo repository was published alongside the talk.

## Related Conf42 talks

- Ricardo Castro on [GitOps](https://www.conf42.com/Site_Reliability_Engineering_2021_Ricardo_Castro_GitOps) at Conf42 Site Reliability Engineering 2021.
- Ismael Hommani and Clément Loiselet on [Flux and Argo CD](https://www.conf42.com/DevOps_2023_Ismael_Hommani_Clement_Loiselet_flux_argocd) at Conf42 DevOps 2023.
- Yuriy Bezsonov on [multi-cluster Kubernetes with GitOps](https://www.conf42.com/Kube_Native_2024_Yuriy_Bezsonov_multicluster_kubernetes_gitops) at Conf42 Kube Native 2024.

[Watch Leonardo Murillo's talk](https://www.conf42.com/Cloud_Native_2021_Leonardo_Murillo_gitops_multicloud_crossplane_flux2)

## From Qwinix

Qwinix supported Conf42 Cloud Native 2021; this talk came from its CTO.

- [qwinix.io](https://www.qwinix.io/)

[Watch the talk on YouTube](https://youtu.be/AyRhi92v9O0).

## Watch the talk

[Doing GitOps for multi-cloud resource management using Crossplane and Flux2](https://www.conf42.com/Cloud_Native_2021_Leonardo_Murillo_gitops_multicloud_crossplane_flux2) at Conf42 Cloud Native 2021.
