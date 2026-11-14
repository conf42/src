# CruiseKube right-sizes Kubernetes pods in place, minute by minute

Conf42 Blog, 2026-03-09, updated 2026-11-09. https://www.conf42.com/blog/sre2026/cruisekube-right-sizes-pods-in-place

In short: Shubham Rai (Truefoundry) and Raman Tehlan (Zurich Lab) at Conf42 SRE 2026 show CruiseKube, open source CPU right-sizing with in-place pod resize and PSI.

Everyone knows lower CPU requests mean a cheaper cluster, and almost nobody lowers them. At Conf42 Site Reliability Engineering 2026, Shubham Rai of Truefoundry and Raman Tehlan, Cloud Native Consultant at Zurich Lab, presented CruiseKube, an open source controller that keeps correcting pod requests in place, using two features that only recently became usable in Kubernetes.

It is a builders' talk: the problem, the design choices, the components and a dashboard demo, closing with an honest list of where not to turn it on.

## Over-provisioning is a fear problem, not a knowledge problem

Shubham opens with why clusters stay expensive. Teams fear CPU throttling and OOM kills, because an under-provisioned pod that gets killed is a business outage. So they pad requests. Then nobody wants to keep re-analysing workloads and editing YAML. The padding compounds: inflated requests force the cluster autoscaler to add nodes that sit half empty.

His point about where to fix it is worth hearing. You cannot solve this at the node level, because node over-provisioning is downstream of request over-provisioning. Fix requests first, or the node autoscaler is just efficiently buying the wrong amount of hardware.

## Predict a little, correct often

The contrast with the Vertical Pod Autoscaler is the core idea. VPA does periodic analysis and produces a recommendation that has to hold for a long time, per workload, across whatever nodes its pods landed on. CruiseKube runs a continuous feedback loop that only needs to be right for a short window ahead, and it decides per pod, in the context of the node that pod is on.

Two things make that viable. In-place pod resource updates went GA in Kubernetes 1.35, so a request can change without a restart. Pressure Stall Information (PSI) metrics, beta in 1.34, give per-container contention data on each node, even when you set no CPU limits. CruiseKube combines CPU usage with CPU PSI to pick the request.

The node view matters because of headroom, the gap between a pod's base need and its bursts. Bursts are big and rare, so the gap between the 75th percentile and the maximum is large. Instead of every pod reserving its own worst case, CruiseKube reserves the largest headroom among the pods on a node and lets them share it. It is the same bet as a shared on-call rota: not everyone has a bad night at once.

## Two entry points and a lot of guardrails

Raman walks through the loop: observe the cluster from Prometheus, store stats, learn patterns (a peak at the same time over the last seven days), then apply. Changes land in two places. A mutating admission webhook sets requests when a pod is created, informed by history, so a pod that was OOM-killed comes back with more memory. A continuous optimizer applies recommendations to running pods in place, evicting only when a pod needs more than its node can give.

The guardrails are the part SREs will check first. Everything starts in recommend-only mode; nothing changes until you enable cruise mode per workload. Eviction respects criticality (a single-replica workload ranks higher than one with fifty pods) and you can edit priorities. OOM kills feed back into memory sizing. There is also a disruption window for Karpenter users whose do-not-disrupt annotations block node consolidation.

The demo dashboard shows monthly cost, current and untapped savings, allocatable versus requested versus recommended resources, per-workload recommendations and an event log of every change. On the demo cluster, enabling it for all workloads showed savings of about 60%.

## Where they say not to use it (yet)

Their recommendation is stateless services, dev and staging, and short-lived jobs. Latency-sensitive services, stateful apps like databases and queues, and workloads under HPA should stay in recommend mode for now; HPA support was still in progress at the time of the talk.

## Who should watch

Platform and FinOps engineers who have tried VPA, found it too slow or too disruptive, and still pay for idle cores. It is a short, practical tour with a demo; you will come away knowing whether to install it in recommend mode and look.

## Related Conf42 talks

- [Kubernetes Scaling for Savings and Stability: Beyond HPA and VPA](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability) by Joshua Fox.
- [The Frugal k8s Engineer: Strategies for Amazon EKS](https://www.conf42.com/Kube_Native_2024_Piyush_Mattoo_Dariush_Azimi_karpenter_kubernetes_optimization) by Piyush Mattoo and Dariush Azimi, including Karpenter.

[Watch Shubham Rai and Raman Tehlan's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Raman_Tehlan_Shubham_Rai_unlocking_just_time) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/HIyWAigDygI).

## Watch the talk

[Unlocking Just-in-Time CPU Optimization with In-Place Pod Resize](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Raman_Tehlan_Shubham_Rai_unlocking_just_time) at Conf42 Site Reliability Engineering (SRE) 2026.
