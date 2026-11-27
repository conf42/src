# Why the big public clouds left multicast behind, and what to use

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/why-public-clouds-left-multicast-behind

In short: Srinivas Shamkura of SADA explains at Conf42 Platform Engineering 2025 why clouds skip native multicast and how overlays, pub/sub and CDNs fill the gap.

Multicast is one of those protocols that works beautifully in your data centre and then quietly fails to exist in the cloud you are migrating to. At Conf42 Platform Engineering 2025, Srinivas Shamkura, Senior Cloud Infrastructure Engineer at SADA, explained why most major cloud providers don't support it natively, what that does to infrastructure automation, and which workarounds are worth their cost.

## One sender, many listeners, no sessions

Shamkura starts with the case for multicast. With unicast, one sender serving a thousand receivers holds a thousand TCP sessions, which burns CPU on the sender for nothing but bookkeeping. With multicast the sender pushes packets to a group, receivers join and leave, and there are no per-receiver sessions at all. His analogy is a radio station: tune to the frequency and you hear what everyone else hears. Financial market data, telecom and media streaming are built on it for exactly that reason.

## Five reasons the cloud said no

The heart of the talk is a list of five barriers:

1. **State explosion in software-defined networks.** Every join and leave means recalculating forwarding tables consistently across a huge virtual network, which loads the control plane.
2. **Multi-tenancy.** Multicast assumes one administrative domain; a shared physical fabric serving many customers cannot risk group traffic leaking between tenants.
3. **Operational complexity.** Unicast can be routed statically and predicted. Multicast membership changes constantly and is hard to automate.
4. **Performance in virtualised networks.** The cost of processing multicast through virtual switches can eat the bandwidth savings it was supposed to bring.
5. **Architecture mismatch.** Microservices prize loose coupling and explicit service boundaries; multicast couples publishers and subscribers implicitly.

## The automation bill arrives later

For platform engineers the pain is downstream. A legacy app that relied on multicast cannot be lifted and shifted. Terraform and CloudFormation have no native multicast resource, so teams end up with custom scripts beside their declarative code, which breaks the consistent, state-file-driven workflow they rely on.

Kubernetes adds its own wrinkles. Service discovery is DNS and point to point, so apps that discovered peers via multicast must be rewritten for the Service abstraction. Network policies govern pod-to-pod traffic but not multicast, leaving a security gap. And pods may be created and destroyed faster than multicast trees can be recalculated. A protocol designed for long-lived routers meets workloads that live for minutes.

## Three ways out, each with a cost

Shamkura is candid that every option has trade-offs:

- **Application-level replication.** The app manages group membership, delivery and error handling itself. It lets you migrate, but now the network is the developers' problem, and performance can suffer.
- **Overlay networks.** Deploy a marketplace router, build GRE tunnels from senders and receivers to it, run BGP between the hosts and that router, and let PIM handle the multicast. It moves the work back into the network layer, at the price of more moving parts to run.
- **Cloud-native rewrites.** Use managed messaging such as Amazon SQS or Google Cloud Pub/Sub, or a CDN when the workload is content distribution rather than real-time data.

His own lean is clear: the workarounds bring monitoring complexity, harder capacity planning, longer incidents and inconsistent environments between on-prem and cloud. Redesigning toward cloud-native and serverless event architectures is usually where the total cost of ownership comes out ahead.

## What might change

Looking ahead he points at SDN-native multicast scoped to specific use cases, SmartNICs and DPUs taking the per-packet burden off virtualised hosts, and service meshes such as Istio and Consul possibly growing multicast-like features. None of those exist as a drop-in answer today, which is why the talk's practical advice is about design choices you can make now.

## Who should watch

Anyone planning a migration of trading, telecom or media systems to AWS, Azure or Google Cloud should watch before the design review, not after. Platform teams already fully on Kubernetes with no legacy multicast can treat it as a well-explained piece of networking history.

## Related Conf42 talks

- Dumlu Timuralp on the [life of a packet in Amazon EKS](https://www.conf42.com/Cloud_Native_2025_Dumlu_Timuralp_networking_performance_optimization) at Cloud Native 2025.
- Federica Ciuffo on [application networking on Kubernetes](https://www.conf42.com/Cloud_Native_2023_Federica_Ciuffo_application_networking_kubernetes) at Cloud Native 2023.

[Watch Srinivas Shamkura's talk](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Shamkura_ditched_multicast_challenge)

[Watch the talk on YouTube](https://youtu.be/Td7EABbElkk).

## Watch the talk

[Platform Engineering's Hidden Network Challenge: Why Cloud Platforms Ditched Multicast and How It Impacts Your Infrastructure Automation](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Shamkura_ditched_multicast_challenge) at Conf42 Platform Engineering 2025.
