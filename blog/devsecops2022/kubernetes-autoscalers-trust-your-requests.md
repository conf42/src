# Your autoscalers are only as good as your pod requests

Conf42 Blog, 2022-12-02. https://www.conf42.com/blog/devsecops2022/kubernetes-autoscalers-trust-your-requests

In short: Eli Birger (PerfectScale) at Conf42 DevSecOps 2022 on why HPA and Cluster Autoscaler can't fix bad pod requests, and how to right-size them

Installing a Horizontal Pod Autoscaler and a Cluster Autoscaler does not make a Kubernetes cluster efficient. At Conf42 DevSecOps 2022, Eli Birger, Co-Founder and CTO of PerfectScale, showed why: both autoscalers make every decision from pod requests, so badly sized pods mean a cluster that throttles, gets OOM-killed and still costs too much. The talk is credited to Eli and his co-founder Amir Banet, PerfectScale's CEO; Eli presents it.

Eli ran DevOps and infrastructure teams for years before PerfectScale, building large SaaS systems on Kubernetes, and the talk is about day two: the long stretch after go-live when the goal is the best customer experience at the lowest cost.

## Why doesn't horizontal scaling fix it?

The theory is tidy. The HPA (Eli prefers KEDA) scales pods, the Cluster Autoscaler (some prefer Karpenter) scales nodes, and cost follows demand. The real graphs show uneven resilience and cost that only goes up.

The reason is mechanical. A pod requesting four cores and 8 GB lands on an eight-core, 16 GB node, and that slice is reserved. A pod requesting 12 GB that doesn't fit the remaining allocatable space goes to the unschedulable queue, and the Cluster Autoscaler adds a node. Scale-down only happens when the sum of requests on a node falls below a threshold, by default 50% of allocation, even if its pods would fit elsewhere. A resource-based HPA starts new replicas when utilisation passes a percentage of the request. Both autoscalers are tightly coupled to requests, so horizontal scaling depends on vertical sizing.

## What goes wrong at each end?

The goal is to provision as little as possible without hurting performance: requests guarantee enough resources to run, limits protect nodes from overuse. Eli walks through the failure modes:

- **Requests too high:** waste and extra CO2.
- **Requests too low or missing:** no guaranteed resources, and evictions under memory or CPU pressure.
- **Limits too low:** CPU throttling or out-of-memory kills during bursts, even with free capacity in the node.
- **Limits too high:** a wrong cutoff that can take down the whole node under a spike, and from there a domino effect into a full outage.

One nuance worth noting: he says it is sometimes fine to drop the CPU limit entirely, because CPU is compressible and the kernel's Completely Fair Scheduler shares time between containers. The memory limit stays.

## Data is not the same as an answer

Telling every service owner to read the metrics for hundreds of workloads across clusters, and redo it after every code, architecture or traffic change, is not a plan. A VPA recommendation is a start, not a process. Eli's view is that good DevOps solutions are 70% philosophy and 30% technology. The philosophy is a feedback loop that pinpoints, quantifies and routes problems; the technology turns raw metrics into something you can act on.

"Data is not considered intelligence until it is something that can be applied or acted upon," Eli Birger said at Conf42 DevSecOps 2022.

## What the demo found

The demo cluster runs 240 workloads and cost $3,687 in the last month. 99% of the time it used 61 cores and 261 GB of memory or less, while requests reached 156 cores and 407 GB. The cluster is nearly four times bigger than it needs to be most of the time, and it still had 131 resilience issues from missing or misconfigured requests and limits.

Two examples make it concrete. A Couchbase StatefulSet in production, averaging three replicas, requested 1,000 millicores with a 3,000 millicore limit. It used two cores 95% of the time, and spikes ran very close to the limit, hence the throttling. Eli's point: the values were probably right when someone set them, before more customers, more data and more services hitting the same database.

On the other side, a collector deployment cost $94 in the month, $76 of it wasted. Its business container requested 10 GB per replica and used around 2 GB. A third workload needed three times its requests and showed a rising memory trend, an OOM kill waiting to happen.

## Who should watch

Platform teams who set up autoscaling and still get a growing cloud bill, and SREs chasing throttling that dashboards don't explain. The first half is a clear, vendor-neutral explanation of how requests drive scheduling and scaling; the second half is a product demo.

For more on scaling, see [Chris Nesbitt-Smith on proactive cluster autoscaling](https://www.conf42.com/DevSecOps_2022_Chris_NesbittSmith_proactive_cluster_autoscaling_kubernetes) from the same event, [Rob Richardson on horizontal autoscaling](https://www.conf42.com/Kube_Native_2022_Rob_Richardson_horizontal_autoscaling), and [Raja Ganesan on cluster autoscaling with Karpenter](https://www.conf42.com/Cloud_Native_2022_Raja_Ganesan_cluster_autoscaling_karpenter).

[Watch Eli Birger and Amir Banet's talk](https://www.conf42.com/DevSecOps_2022_Eli_Birger_Amir_Banet_kubernetes_environment_flourish_resources) from [Conf42 DevSecOps 2022](https://www.conf42.com/devsecops2022).

## From PerfectScale

In the demo, PerfectScale analyses every replica of a workload and recommends requests and limits, packaged as a YAML snippet to paste into infrastructure as code, or as a Jira task for the service owner. You can set a resilience level per workload (a production database gets wider margins) and see the cost impact; for the Couchbase example, the highest level meant roughly 70-80% more monthly cost. A multi-cluster, multi-cloud view sums up cost, waste, risk and carbon footprint per cluster and organisation.

- PerfectScale: [perfectscale.io](https://www.perfectscale.io/)

[Watch the talk on YouTube](https://youtu.be/pW2gw_F1Wqo).

## Watch the talk

[Let your Kubernetes environment flourish with just the right amount of resources](https://www.conf42.com/DevSecOps_2022_Eli_Birger_Amir_Banet_kubernetes_environment_flourish_resources) at Conf42 DevSecOps 2022.
