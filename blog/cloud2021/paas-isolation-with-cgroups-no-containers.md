# A PaaS that has isolated customers with plain cgroups for 15 years

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/paas-isolation-with-cgroups-no-containers

In short: M4dz (alwaysdata) at Conf42 Cloud Native 2021 on running a PaaS on POSIX permissions and Linux cgroups instead of Docker or Kubernetes

Every container runtime is, underneath, a wrapper around a Linux kernel feature you can drive yourself by writing numbers into files. At Conf42 Cloud Native 2021, M4dz, Tech Evangelist and Developer Advocate at alwaysdata, explains how the hosting provider has isolated its customers' processes for 15 years with POSIX permissions and cgroups, no Docker, no Kubernetes, and why that was a deliberate choice rather than a legacy one.

It's an opinionated talk at a cloud native conference, which is part of the fun. The first half questions whether you need microservices; the second shows the cgroup mechanics in production.

## Do you really need microservices?

He defines them carefully: business-oriented services that do one thing, expose a standard API, run independently (his example interface service falls back to defaults when the settings service is down), talk through a message bus, and stay stateless with data on a dedicated backend. Running that means orchestration, a storage backend and a messaging system such as Redis, so it's complex to run, maintain and deploy.

His checklist says yes if you have a monolith to split, business units to map services onto, real scaling needs (he stresses most apps don't), a team big enough to split and strong DevOps skills. It says no if you lack an observability culture, lack DevOps, don't know containers and isolation, or are building the web version of Flappy Bird.

His own preference is a multi-language architecture: components chosen by technology (Rust for some tasks, Python for others, Node.js and an Ember PWA for the front end) on a platform that can run the different interpreters, keeping scalability without the operational load.

## Isolation without containers

Containers exist to isolate processes: a crash shouldn't take the app down, data shouldn't leak, resources should be shared fairly, each part can pin its own language version, and small parts are easier to observe. "You can run isolation without containers," M4dz said at Conf42 Cloud Native 2021. POSIX already gives you processes, I/O controls, message passing and permissions, and the kernel feature behind Docker and containerd, cgroups, is also what systemd uses.

The catch he admits: it takes solid Linux skills, and it's not as simple as building an image and pushing it to a registry. His argument is that isolating processes is an easier long-term job than isolating near-complete system images.

## What does a cgroup look like in production?

When alwaysdata started as a hosting provider 15 years ago, there was no Docker, only Linux and cgroups. The model is one cgroup per process per user, with POSIX permissions on resources. In the kernel's pseudo file system, their own orchestrator (the container service) holds a group per user, and inside it, for example, a group for that user's Apache upstream.

Adding a process to a group is writing its PID into the group's `cgroup.procs` file. Limiting it is writing a value into another file: put 4 GB into `memory.max` for the Apache upstream group and the kernel enforces it, balancing resources so one hungry process doesn't starve the others. An orchestrator is still needed at their density, many users per server, but it's a central piece of code that creates groups, assigns PIDs and edits limit files, far smaller than Kubernetes. Without automation, he notes, you could do it all by hand.

## SSH sessions, private IPs and hidden processes

Three production details stand out:

- **SSH**: OpenSSH doesn't support cgroups natively, so users authenticate through PAM with a custom script that attaches the session's process to the user's own cgroup, transparently.
- **Networking**: each user gets private IPs. Instead of iptables, which he finds complex and unhandy, they patch the kernel so access to a private IP is allowed only if it's registered to that user, comparing GIDs and addresses. He recommends iptables if you'd rather not patch a kernel.
- **Process visibility**: they enable an option so that a user running `ps` sees only their own processes.

They don't use namespaces, the other kernel layer containers rely on to partition network interfaces and similar resources. For their use case it's overkill.

## Where this goes next

He closes with a bet: WebAssembly serverless functions running as isolated processes, combining WebAssembly's security model with cgroup limits, with no containers at all. That, he says, is a talk for another time.

## Who should watch

Platform engineers who want to know what Docker and Kubernetes actually do to a process, and anyone running a multi-tenant Linux platform who suspects a full container stack is more than they need.

## Related Conf42 talks

- Adam Gordon Bell on [how BuildKit compiles containers](https://www.conf42.com/Cloud_Native_2021_Adam_Gordon_Bell_compiling_containers), from the same event.
- Lahiru De Silva on [Kubernetes multi-tenancy isolation](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) at Conf42 DevSecOps 2026.
- Lerna Ekmekcioglu on [moving from a monolith to microservices on AWS](https://www.conf42.com/Cloud_Native_2022_Lerna_Ekmekcioglu_monolith_microservices_aws) at Conf42 Cloud Native 2022.

[Watch M4dz's talk](https://www.conf42.com/Cloud_Native_2021_M4dz_cgroups_container_technologies_paas_provider) from [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From alwaysdata

alwaysdata is a cloud and hosting provider whose platform has run on cgroup-based isolation for 15 years.

- alwaysdata: [alwaysdata.com](https://www.alwaysdata.com/en/)

[Watch the talk on YouTube](https://youtu.be/ao0yfZ7U_84).

## Watch the talk

[Cgroups for the best: Using container technologies as a PaaS provider](https://www.conf42.com/Cloud_Native_2021_M4dz_cgroups_container_technologies_paas_provider) at Conf42 Cloud Native 2021.
