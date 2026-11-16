# One staging cluster can replace your dev and CI clusters

Conf42 Blog, 2025-10-08, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/share-one-staging-cluster-with-mirrord

In short: Arsh Sharma (MetalBear) at Conf42 Kube Native 2025 shows mirrord running local code in a shared staging cluster to stop Kubernetes cluster sprawl.

Kubernetes adoption starts with one production cluster and somehow ends with a cluster per developer. At Conf42 Kube Native 2025, Arsh Sharma, Senior DevRel Engineer at MetalBear, traced how that sprawl happens and showed MetalBear's open source tool mirrord letting developers and CI share a single staging cluster safely, by running local code as if it were inside the cluster.

Honest scope: this is a vendor talk showing MetalBear's own project, with a live demo. The problem framing is useful even if you never install it.

## How one cluster becomes forty

Arsh's story will be familiar. Production gets a cluster. Shipping straight to production is scary, so staging gets one or two. Staging deploys are slow and one team's deploy blocks the others, so CI starts spinning up clusters. CI gets slow too, so developers get personal environments mirroring production. Then they want ephemeral on-demand environments, so you either provision many clusters or carve one huge cluster into namespaces. Either way, the outcome is the same: more environments than the DevOps team can manage and a cloud bill nobody can defend.

The costs he lists go beyond money: DevOps time spent maintaining environments instead of improving things, sometimes extra hires just to run them, and developers waiting 15 to 20 minutes for an ephemeral environment every time they want feedback.

## Run locally, behave as if remote

mirrord's idea is to keep the process on your laptop while mirroring its context from the cluster: incoming and outgoing traffic, the file system and environment variables. Your local process thinks it is running in the cluster. Outgoing requests go out via the cluster, so other services see them as coming from the target pod. All the dependencies, the databases and queues, are already in staging, so nothing needs to be set up locally.

## The demo: mirror, then steal

The demo uses an IP visit counter service backed by Redis, an IP info service and Kafka, all deployed in a staging cluster with nothing running locally. Arsh uses the mirrord extension in Cursor (there are extensions for VS Code, Windsurf and JetBrains IDEs, plus a CLI), picks the target deployment, and sets a breakpoint. A request to the cluster endpoint hits the breakpoint on his laptop. The config loads environment variables from the cluster, and the code reads a response file that exists only in the cluster.

Then he switches from mirror mode to steal mode in the mirrord JSON config, adding an HTTP header filter so only requests carrying his header come to his machine. He edits the response string, sends a request with the header, and gets his local change back from the shared cluster. Everyone else's requests still reach the deployed version.

That filter is the point. It is what lets many developers, CI jobs or, as he notes, AI agents share one staging cluster without stepping on each other.

## What keeps sharing safe

The obvious objection is safety, and Arsh addresses it after the demo:

- HTTP filters route each request to the right developer, once
- queue splitting lets several developers consume from the same Kafka or SQS queue without disrupting each other
- mirrord policies block forbidden actions, such as writing to a sensitive database
- any dependency can run locally instead, for example a database when you're testing a migration

The CLI also runs in CI, so CI jobs can use the staging cluster too. The end state he proposes: one production cluster and one production-like staging cluster that the platform team actually maintains.

## Who should watch

Platform teams staring at a growing pile of dev and preview environments, and developers tired of waiting on deploys to test a one-line change. If your org already runs ephemeral environments happily, the queue-splitting and policy features are still worth seeing.

## Related Conf42 talks

- [Mirror Mirror on My local machine](https://www.conf42.com/Kube_Native_2024_Anita_Ihuman_local_machine_mirror_dev_environment) is the earlier Kube Native take on the same local-to-cluster idea.
- [Ephemeral Environments 101](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments) makes the case for the approach Arsh wants to replace.
- [Designing Staging Environments: A Blueprint for Pre-production](https://www.conf42.com/Cloud_Native_2023_Lucas_da_Costa_staging_environments_blueprint_preproduction) helps you build the one staging cluster worth sharing.

[Watch Arsh Sharma's talk](https://www.conf42.com/Kube_Native_2025_Arsh_Sharma_kubernetes_environments_scalability)

[Watch the talk on YouTube](https://youtu.be/tEyyDJ4PsLo).

## Watch the talk

[Mirror Mirror on the Wall, How Many Kubernetes Environments Are Enough After All?](https://www.conf42.com/Kube_Native_2025_Arsh_Sharma_kubernetes_environments_scalability) at Conf42 Kube Native 2025.
