# When 100,000 agents check in, the agent is the riskiest part

Conf42 Blog, 2022-03-10. https://www.conf42.com/blog/ce2022/osquery-fleet-agent-chaos-experiments-per-week

In short: Zach Wasserman (Fleet) at Conf42 Chaos Engineering 2022 on keeping osquery agents and self-hosted Fleet servers resilient at 100,000-device scale

An endpoint agent that takes down the production server it was installed to protect has failed at its one job. At Conf42 Chaos Engineering 2022, Zach Wasserman, CTO of Fleet and co-creator of osquery, explained how Fleet ranks the risks in an agent-plus-server system, why the agent is high risk and the server only medium, and the metric that drives their testing: how many experiments can we run per week?

A grounded talk: every mitigation comes with its downside.

## What are osquery and Fleet?

Osquery, which Zach helped create at Facebook and which is now a Linux Foundation project, exposes the operating system's internals on macOS, Linux and Windows as a relational database you can query. It is read-only by design, which narrows the blast radius. Fleet is the open-core management server that runs osquery across 100,000+ devices. It has two very different kinds of client: osquery agents checking in for configuration and sending data, and API clients, usually a human in the UI or a script. The agent traffic is orders of magnitude larger, so the two get treated differently.

## How do you decide where to spend reliability effort?

Zach's order of priorities is availability, then data integrity, then cost, and he applies the Pareto principle and Amdahl's law: a small part of the system generates most of the load, so focus there.

On the agent side, the stakes add up to high risk: it runs on production servers that make the company money, on workstations people need to do their jobs, it must not miss security events, and at that scale a small percentage increase in resource use becomes a large compute bill. The Fleet server scores medium: availability and integrity of monitoring data matter, latency a bit less, and even a big scale-up of a few dozen servers plus MySQL and Redis costs little next to a few percent across every endpoint.

## How does osquery avoid hurting the host?

Each mitigation comes with its trade-off:

- **Watchdog.** A worker/watcher process pair. If a query exceeds CPU or memory limits, it is terminated and blocked for 24 hours. That protects production and workstations, at the cost of monitoring gaps.
- **Linux cgroups.** The kernel enforces hard CPU and memory limits as a final backstop. Linux only.
- **Query profiling before deploy.** Osquery's tooling estimates user time, system time, memory and file accesses per query, so you know which queries would trip the watchdog and what they will cost.
- **Query performance monitoring.** Fleet records real execution statistics from every host and shows them in the UI, so operators can check reality against expectations.

## And the server?

Standard scaling practice: several Fleet processes behind a load balancer, clustered MySQL and Redis with failover, cloud autoscaling. The less elastic dependencies need proper sizing or costs creep. The more interesting piece is backpressure: agents buffer data locally and only clear it after the server acknowledges receipt. Pushing a little storage to the clients, who vastly outnumber the servers, buys a lot of availability, though latency can rise and an overflowing buffer eventually drops old data.

## Self-hosted means chaos you do not control

Customers run everything: agents, servers and dependencies. That means inconsistent environments (MySQL 5.7 or 8, MariaDB or Aurora; Redis in cluster, Sentinel or single-host mode), slow deploys outside Fleet's control, outdated versions, and slow debugging loops. Fleet pushes consistency with Terraform and reference architectures that pin MySQL versions, task counts and memory.

On testing, Zach said at Conf42 Chaos Engineering 2022: "the more experiments that we run, the more different combinations of things we can try, things going wrong, things going right, the more edge cases we'll encounter". Generic HTTP load tools do not know your hot path, so Fleet built its own: osquery-perf, a Go simulator of osquery agents that runs tens or hundreds of thousands of fake agents on one virtual machine, with templated host data to inject randomness. Varied hosts, staggered start-ups, degraded networks: each is a cheap experiment.

For debugging, the rule is collect first, ask questions later. One command, fleetctl debug archive, gathers memory allocations, errors, concurrency and CPU profiles and database status including locks. It serves both load tests and production, and it saves round trips with self-hosting users.

## Who should watch

Anyone building agents, SDKs or self-hosted software that runs in environments they do not own, and Go developers who need a model for load-testing a check-in-heavy server.

## Related Conf42 talks

- Zach Wasserman on [securing endpoints with open software](https://www.conf42.com/DevSecOps_2023_Zach_Wasserman_securing_endpoint_open_software) at Conf42 DevSecOps 2023.
- Adelina Simion and Andy Kuszyk on [load testing with F1](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1) at Conf42 Golang 2022.
- Vishnu Vardhan Chikoti on [using results from chaos experiments](https://www.conf42.com/Chaos_Engineering_2022_Vishnu_Vardhan_Chikoti_utilising_results_from_chaos_experiments) at Conf42 Chaos Engineering 2022.

[Watch Zach Wasserman's talk](https://www.conf42.com/Chaos_Engineering_2022_Zach_Wasserman_glitches_in_the_matrix__or_taming_agent_chaos)

## From Fleet

Fleet is the open-core osquery management server shown throughout the talk, with the fleetctl CLI, Terraform modules and published reference architectures for self-hosted deployments.

- Fleet: [fleetdm.com](https://fleetdm.com/)
- Fleet source code: [github.com/fleetdm/fleet](https://github.com/fleetdm/fleet)
- Reference architectures: [fleetdm.com/docs](https://fleetdm.com/docs/deploying/reference-architectures)

[Watch the talk on YouTube](https://youtu.be/hBtYFm2m2Lo).

## Watch the talk

[Glitches in the Matrix, or Taming Agent Chaos](https://www.conf42.com/Chaos_Engineering_2022_Zach_Wasserman_glitches_in_the_matrix__or_taming_agent_chaos) at Conf42 Chaos Engineering 2022.
