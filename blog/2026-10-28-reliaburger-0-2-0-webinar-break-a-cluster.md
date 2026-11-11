# Reliaburger 0.2.0: an hour spent breaking a cluster on purpose

Conf42 Blog, 2026-10-28. https://www.conf42.com/blog/2026-10-28-reliaburger-0-2-0-webinar-break-a-cluster

In short: The Conf42 webinar with Reliaburger 0.2.0: a three-node laptop cluster, a real Kubernetes app, injected faults, and a cluster that heals itself.

Most orchestrator demos end the moment the app comes up. The Reliaburger 0.2.0 webinar on 28 October 2026 started there: build a small cluster on your own laptop, run a real web app on it, then slow it down and switch parts of it off on purpose, and watch the cluster notice and fix itself. Mark Pawlikowski, Reliaburger's evangelist, hosted the hour for the Conf42 community.

## One agent, one CLI, no control plane to assemble

[Reliaburger](https://reliaburger.com/) is an open-source container orchestrator written in Rust. Each node runs one agent, `bun`, and you drive the cluster with one CLI, `relish`. Scheduling, clustering, service discovery, ingress, PKI, secrets, an image registry, metrics, logs, GitOps, jobs and fault injection are compiled into that agent, so there are no add-ons to install before the interesting part starts.

It also applies most Kubernetes manifests directly, and tells you what it had to change or drop on the way in. That matters for a webinar like this one: the demo app is not a toy written for the tool, it's podinfo, straight from its Kubernetes YAML.

## From zero to three nodes on a laptop

The setup is the project's own five-minute tour. One `curl | sh` installs `relish` and builds a three-node cluster in Linux VMs, with every download checked against a pinned digest. The bill of materials was in the invite: a Mac, or Linux with QEMU and KVM, about 8 GB of free memory and 15 GB of disk.

Then the app: `relish apply -f https://reliaburger.com/demo/podinfo.yaml` brings up podinfo's frontend, backend and Redis cache, plus a small load generator so there is always traffic to look at. `relish status` shows a frontend replica on each node, `relish council status` shows every node's view of the Raft council, and the built-in ingress serves the app in the browser.

## Breaking it, politely

This is the part the invite promised. Reliaburger's fault injection is a CLI verb, not a separate product:

- `relish fault delay redis 300ms --from frontend --duration 2m --acknowledge` makes Redis slow, but only for the frontends, and only for two minutes.
- `relish path frontend --to redis` walks the network path hop by hop (DNS, VIP, eBPF map, firewall, TCP), so you can see where the delay lives.
- `relish fault kill frontend --count 1 --acknowledge` takes a replica out, and `relish local stop node-3` takes a whole machine with it.

`relish inspect frontend` then shows three frontends again, spread over the surviving nodes, and `relish wtf` reports what's wrong and what to do about it. `relish dashboard` gives the same story as live charts in the browser.

## What 0.2.0 added: a million jobs

0.2.0, released on 16 October 2026, is the "A million jobs" release. Its headline is batch work: compact task arrays replicated through Raft, one lifecycle for singleton jobs, arrays, cron and deployment hooks, reusable container and native executors, bounded job storage on workers, and fair capacity between namespaces. On the CLI that's `relish batch submit`, `relish run --batch`, `relish batch watch` and `relish jobs`. The [release notes](https://github.com/reliaburger/reliaburger/releases/tag/v0.2.0) list every change.

## Who it's for

Anyone who has wanted to see failover happen rather than read about it, and anyone curious what an orchestrator looks like when the control plane is not a separate project. The tour runs on your own machine, so you can repeat the whole hour at your own pace: start at [reliaburger.com](https://reliaburger.com/) and the five-minute tour in its docs.

Future Conf42 webinars are listed on [conf42.com](https://www.conf42.com/).
