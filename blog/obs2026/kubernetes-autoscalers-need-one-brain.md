# Your Kubernetes autoscalers need one brain, not three

Conf42 Blog, 2026-08-26, updated 2026-11-09. https://www.conf42.com/blog/obs2026/kubernetes-autoscalers-need-one-brain

In short: Joshua Fox of DoiT at Conf42 Observability 2026 on layered telemetry and a unified controller that ends HPA/VPA fights and resizes pods in place.

Kubernetes gives you a horizontal pod autoscaler, a vertical pod autoscaler and a cluster autoscaler, and lets them argue. At Conf42 Observability 2026, Joshua Fox, Senior Cloud Architect at DoiT International and a Google Developer Expert, argued that the fix is a single controller fed by four layers of telemetry, deciding between scaling axes instead of letting each one act alone.

Fox advises DoiT customers on cost and resilience, and DoiT ships PerfectScale for exactly this problem. He was clear that the talk is about principles, not the product, and it holds up that way: everything he describes can be built from open source parts.

## Cost and risk sit on one frontier

The framing is a Pareto frontier. Cut resources to the bone and something crashes; pad everything and you pay for air. You pick where on the frontier you want to live, but the goal is to get onto it rather than somewhere wasteful behind it.

Standard autoscaling misses that frontier in three ways, per Fox:

- **Signal granularity.** Average CPU hides microbursts. Then again, chasing a burst that lasted a few milliseconds with new capacity is its own waste.
- **HPA vs VPA conflict.** The horizontal scaler adds pods at the same moment the vertical one grows each pod. Both are right on their own and wrong together.
- **Eviction.** Resizing a pod used to mean killing it and starting a bigger one. Fine for stateless toys, painful for StatefulSets, slow-starting JVMs and cache-warm workloads.

## Four layers of telemetry, one question each

The middle of the talk is a tour of what to measure and why. At the infrastructure layer: node CPU, memory and GPU, with NVIDIA DCGM for streaming multiprocessor utilisation and memory bandwidth, plus cAdvisor at the container level so normal page-cache churn doesn't read as memory pressure. At the workload layer: kube-state-metrics for requested resources, replicas and pending pods, because a fourth replica that isn't ready yet shouldn't trigger a fifth.

At the application layer the question shifts from whether the workload is under pressure to why it is. Kubernetes sees memory climbing; eBPF and a JVM agent can show the Java app choking on garbage collection. Above that sits change and risk: revision history, which scale-downs caused crashes before, and whether a new revision is an app change or just a resize. Fox's line for the whole stack: "We're not here to make the metrics happy. We're here to make the customers happy."

## A controller that arbitrates, cools down and checks itself

The unified logic aggregates those signals, arbitrates between node, horizontal and vertical scaling, waits out a cool-down so an overheated system can catch up, then reconciles: looks at telemetry again to confirm the change helped. Fox mentioned building such a custom controller with Akka as one option. Once the scalers stop fighting, their outputs compound: better pod requests mean better bin packing, which means fewer half-empty nodes for the cluster autoscaler to remove.

The enabling feature is in-place pod resizing, stable from Kubernetes 1.35 according to the talk. A pod can be given more memory without a restart, which removes the eviction tax for stateful and slow-starting workloads.

## Write your trade-offs down as SLOs

The closing point is a policy one. How much latency is worth $100,000 to you? Fox stressed that he made the figure up, and that's the point: most teams answer that question by gut feel or by panic after a crash. Expressing it as SLOs gives the controller something real to optimise against. His summary: stop scaling on CPU or memory utilisation and start scaling on a combined view of cost, service health and risk.

## Who should watch

Platform and SRE engineers who own cluster spend and have seen HPA and VPA thrash each other. If you've only ever set a CPU target on an HPA, this is a useful map of what you're not looking at. If you already run a custom scaler, the four-layer breakdown is a decent checklist.

## Related Conf42 talks

- [Aritra Ghosh on shrinking the observability bill for Kubernetes](https://www.conf42.com/Observability_2025_Aritra_Ghosh_shrinking_kubernetes_cost) (Conf42 Observability 2025): the other half of the cost story, the telemetry itself.
- [Chris Nesbitt-Smith on proactive cluster autoscaling](https://www.conf42.com/Cloud_Native_2023_Chris_NesbittSmith_proactive_cluster_autoscaling_kubernetes) (Conf42 Cloud Native 2023): scaling nodes before demand arrives.
- [Chakkree Tipsupa on Karpenter for scaling and upgrades](https://www.conf42.com/Kube_Native_2024_Chakkree_Tipsupa_karpenter_kubernetes_scaling) (Conf42 Kube Native 2024): the node layer Fox's controller would hand off to.

[Watch Joshua Fox's talk](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability)

[Watch the talk on YouTube](https://youtu.be/me6U2iMklVw).

## Watch the talk

[Kubernetes Scaling for Savings and Stability:  Beyond HPA and VPA](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability) at Conf42 Observability 2026.
