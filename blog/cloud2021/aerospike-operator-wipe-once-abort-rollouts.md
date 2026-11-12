# A database operator must wipe a disk exactly once and abort a rollout midway

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/aerospike-operator-wipe-once-abort-rollouts

In short: Natalie Pistunovich (Aerospike) at Conf42 Cloud Native 2021 on building a Kubernetes operator for a distributed database and the challenges it solved

Writing a Kubernetes operator for a stateless app is a weekend project; for a distributed database that has to stay online, the hard part is knowing when not to act. At Conf42 Cloud Native 2021, Natalie Pistunovich, Lead Developer Advocate at Aerospike, explains the operator pattern from scratch, then walks through three engineering problems Aerospike hit building its operator: persistent storage on restart, aborting a rolling update halfway, and running at a scale where the cloud itself becomes the noisy part.

The first half is a solid refresher on operators; the second is where the lessons are.

## What is an operator, again?

Operators are clients of the Kubernetes API that act as controllers for a custom resource. A controller is a control loop that watches cluster state and requests changes to move it closer to the desired state; a custom resource, defined by a CRD, extends the API with your own object kinds. Combine the two and you can automate repeatable operational work. "It is used to take the human out of the equation, because doing such things is boring," Natalie Pistunovich said at Conf42 Cloud Native 2021, and boring work is where people make mistakes.

She also covers why databases live in StatefulSets rather than Deployments: Deployment pods are identical and interchangeable with random names, while StatefulSet pods keep their own identity across restarts and can be addressed individually. Controllers and operators are patterns, not frameworks, so any language that follows the conventions works.

## What makes Aerospike awkward to operate?

Aerospike is a NoSQL database with a hybrid memory architecture: the index lives purely in memory, the data on persistent storage, read directly from disk. Clients such as banks rely on it for strict SLAs, with petabytes handled at sub-millisecond latency, optional ACID transactions and strong consistency. Two features matter for the operator: rack awareness, which places replicas in different hardware failure groups, and multi-site setups, either one cluster stretched synchronously across racks, data centres or availability zones, or several clusters joined by asynchronous cross-data-centre replication (XDR).

The operator is driven by a single custom resource. Its spec covers cluster size and per-node resources, the full Aerospike configuration in YAML (converted to Aerospike's own format), and security (TLS, users). It handles deployment, scaling, server upgrades and downgrades, configuration, rack awareness, access control and XDR, and monitors the lot.

## How do you wipe a disk exactly once?

Each pod has dedicated persistent storage. New storage must be wiped, because, as she puts it, just like memory you can't assume a fresh allocation is empty. A restarted pod's storage must not be touched, because it holds the data you want back. Kubernetes gives you no clean way to tell a restart from a new pod, and a version update brings a new image too.

The fix is a flag. An init container prepares and wipes the device before the database container starts, and records in a file that it did so. On the next restart the init container finds the flag and leaves the data alone.

## How do you abort a rolling update on node four?

Say you start a server version update across ten nodes. Nodes one to three finish, and you realise it was a mistake. If the operator took a single command meaning update all ten, there's nothing to interrupt.

Aerospike's operator requeues the reconciliation request after every node, effectively asking the API what to do next. After node three, the answer can be: roll back, node one, two, three. It also asks for that answer with a delay sized to the node's data migration, which can't be aborted anyway, so any further changes made meanwhile collapse into one up-to-date instruction. She calls it trivial-sounding and recommends checking whether the operators you run do the same.

## When does the cloud become the problem?

The third challenge has no operator-shaped answer. Some customers hold half a trillion objects. Cloud hardware isn't homogeneous (a minimum CPU is promised, not a fixed one), Aerospike is disk heavy and shared I/O is hard to cap, and noisy network neighbours slow the constant messages and heartbeats a distributed database exchanges, with cascading effects that are hard to predict. Her spoiler: an operator alone won't solve these.

What customers at that scale do: private cloud, taking whole hosts and splitting resources internally, budgeting for overcapacity, reading from the nearest replica rather than the master, and keeping communication local because latency matters. Kubernetes and the operator still fit, she notes; Kubernetes started inside Google's private cloud. The operator's source is on GitHub.

## Who should watch

Anyone writing or evaluating an operator for a stateful system. The restart flag and the requeue-per-node rollout are small ideas that are cheap to borrow.

## Related Conf42 talks

- Rohit Mishra on [Kubernetes operators in depth](https://www.conf42.com/DevOps_2024_Rohit_Mishra_deepdive_kubernetes_operators) at Conf42 DevOps 2024.
- Dhiraj Hegde on [HBase and HDFS on Kubernetes in the public cloud](https://www.conf42.com/Cloud_Native_2021_Dhiraj_Hegde_hbase_hdfs_kubernetes_public_cloud), from the same event.
- Mary Grygleski on [stateful microservices with Open Liberty on Kubernetes](https://www.conf42.com/Cloud_Native_2021_Mary_Grygleski_stateful_microservices_open_liberty_kubernetes), from the same event.

[Watch Natalie Pistunovich's talk](https://www.conf42.com/Cloud_Native_2021_Natalie_Pistunovich_k8s_operator_distributed_database) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Aerospike

Aerospike builds the distributed NoSQL database the talk is about, with an open-source Kubernetes operator.

- Aerospike: [aerospike.com](https://www.aerospike.com)

[Watch the talk on YouTube](https://youtu.be/UfGy6jgjaTI).

## Watch the talk

[Building a K8s Operator for a Distributed Database](https://www.conf42.com/Cloud_Native_2021_Natalie_Pistunovich_k8s_operator_distributed_database) at Conf42 Cloud Native 2021.
