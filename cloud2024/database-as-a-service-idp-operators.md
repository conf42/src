# An internal developer platform where a git push buys you a database

Conf42 Blog, 2024-03-21. https://www.conf42.com/cloud2024/database-as-a-service-idp-operators

In short: George Hantzaras and Dan Mckean (MongoDB) at Conf42 Cloud Native 2024 on Kubernetes operators as the engine of an internal developer platform

The cheapest way to add a capability to an internal developer platform is to teach Kubernetes about it. At Conf42 Cloud Native 2024, [George Hantzaras](https://www.conf42.com/Cloud_Native_2024_George_Hantzaras_Dan_Mckean_internal_developer_kubernetes), Director of Engineering for Kubernetes at MongoDB, and Dan Mckean, Senior Product Manager at MongoDB, showed how operators turn Kubernetes into the platform of platforms, then built a database-as-a-service golden path where developers get a MongoDB Atlas cluster and its credentials from a git push.

The first two thirds are a clear refresher on how Kubernetes extends itself, from the control loop to operators. The last third is a demo using MongoDB's own Atlas Kubernetes Operator, so you know whose product shows up.

## What is an internal developer platform supposed to do?

The talk starts from the CNCF definition. A platform is a foundation of tools and services for building, deploying and managing applications; an internal developer platform goes further by cutting developers' cognitive load, giving them a consistent experience through golden paths, and being designed around its users. Platform engineering is the work of building and running that thing.

Two terms carry the rest of the talk. Platform capabilities are what users get, such as observability, managed databases or secrets management. Platform interfaces are how they get them: a CLI, a GitOps workflow with Argo CD or Flux, or a portal like Backstage.

## Why is Kubernetes the default foundation?

The speakers are honest that no hard data proves most IDPs run on Kubernetes, only industry consensus, analyst coverage and vendor case studies. The reasons given are the familiar ones: containerisation, autoscaling, orchestration, running on any cloud or on premises, and declarative management. Kubernetes earned the platform of platforms role through extensibility, the CNCF ecosystem, standardisation, and the CSI, CRI and CNI interfaces for storage, runtimes and networking. He also flags the counter-argument that Kubernetes is getting too complex, and suggest abstraction may be the fix.

## From control loop to operator

This section is the best part for anyone who has used operators without thinking hard about what they are. The controller manager runs built-in controllers (replication, endpoints, namespace), and each one runs the same loop: get the desired state from the API server, get the current state, reconcile. That loop is where self-healing, scaling and consistency come from.

A custom controller, typically written in Go, runs that same loop against a custom resource whose schema you define in a CRD. An operator packages one or more custom controllers with the rest of what an application needs: CRDs, deployment and service manifests, Helm charts, documentation and monitoring tools. The useful distinction is between internal operators, which manage resources inside the cluster (deployments, stateful sets, persistent volumes), and external operators, which manage things outside it, a hyperscaler service or a SaaS such as Atlas, through their APIs.

## What did the demo build?

George Hantzaras ran the demo, focused on one IDP capability: database as a service.

- **Install the operator** with the Atlas CLI, which also creates API keys in Atlas and stores them as Kubernetes secrets.
- **Create an Atlas project** and then a cluster from short YAML files describing the cloud provider, instance type and region. `kubectl apply` creates the custom resources; the operator calls the Atlas Admin API to create the real things.
- **Add the interface**: install Argo CD, point an Argo CD application at the infrastructure-as-code repository, and repeat the same files with a `git push` instead of `kubectl apply`. No team needs direct access to the cluster any more.
- **Connect an app**: an AtlasDatabaseUser resource references a password secret; the operator writes back a secret with the connection string, and a pod running the Mongo shell reads it from an environment variable and connects.

The demo is undramatic, and he took that as the point. George Hantzaras said at Conf42 Cloud Native 2024: "when it comes to managing infrastructure in critical production environments, not having fireworks is a good thing."

## Who should watch?

Platform engineers deciding how to expose managed services to developers, and anyone who wants the clean version of the controller, custom controller, operator story. If you already write operators, skip to the demo for the external-operator plus Argo CD pattern.

## Related Conf42 talks

- George Hantzaras and Dan Mckean's earlier talk on [self-service DBaaS in an internal developer platform](https://www.conf42.com/Cloud_Native_2023_George_Hantzaras_Dan_Mckean_self_service_dbaas_internal_developer_platform) at Conf42 Cloud Native 2023.
- Rohit Mishra on [how Kubernetes operators work](https://www.conf42.com/DevOps_2024_Rohit_Mishra_deepdive_kubernetes_operators) at Conf42 DevOps 2024.
- Leonardo Murillo on [multicloud GitOps with Crossplane and Flux](https://www.conf42.com/Cloud_Native_2021_Leonardo_Murillo_gitops_multicloud_crossplane_flux2) at Conf42 Cloud Native 2021.

[Watch George Hantzaras and Dan Mckean's talk](https://www.conf42.com/Cloud_Native_2024_George_Hantzaras_Dan_Mckean_internal_developer_kubernetes), part of [Conf42 Cloud Native 2024](https://www.conf42.com/cloud2024).

## From MongoDB

MongoDB Atlas is MongoDB's developer data platform, and the Atlas Kubernetes Operator used in the demo manages Atlas projects, clusters and database users from Kubernetes.

- [MongoDB Atlas](https://www.mongodb.com/atlas)

[Watch the talk on YouTube](https://youtu.be/ogGYa_6Usd0).

## Watch the talk

[Building Internal Developer Platforms with Kubernetes Operators](https://www.conf42.com/Cloud_Native_2024_George_Hantzaras_Dan_Mckean_internal_developer_kubernetes) at Conf42 Cloud Native 2024.
