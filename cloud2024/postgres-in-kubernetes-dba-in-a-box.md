# Just don't do it, says the title. Then he tells you to do it

Conf42 Blog, 2024-03-20. https://www.conf42.com/cloud2024/postgres-in-kubernetes-dba-in-a-box

In short: Jan Karremans (CYBERTEC) at Conf42 Cloud Native 2024 on why Postgres belongs in Kubernetes once an operator plays the DBA

The title is a dare. At Conf42 Cloud Native 2024, [Jan Karremans](https://www.conf42.com/Cloud_Native_2024_Jan_Karremans_databases_kubernetes), Sales Leader at CYBERTEC and a self-described techie in sales, opened with "just don't do it" and spent the session arguing the opposite: running Postgres in Kubernetes is where data management is heading for the next decade, provided an operator such as CloudNativePG does the database administrator's job.

Set expectations accordingly. This is a short talk about mindset and history more than a hands-on guide: no YAML, no benchmarks, no failover demo. What it gives you is the case for why a database person should stop treating Kubernetes as the enemy.

## Why would a database person come round to Kubernetes?

His own route explains a lot of the framing. He spent decades in proprietary databases, Oracle in his case, migrated himself to Postgres, and got into Kubernetes about three years before the talk, working with the team that figured out how to put the elephant in a box.

His big-picture claim borrows a line from Marc Linster, PostgreSQL Fellow: Postgres is the most transformative technology since Linux. The first wave of open source replaced the easier layers, tools and then operating systems (VMS, Solaris and proprietary Unix all lost to Linux). The second wave is reaching the parts most deeply woven into an organisation: data processing, with community-governed projects like Postgres and Kubernetes. A quick tour from System R and the great debate of 1974 to Ingres, Postgres and today's multi-model Postgres, relational plus JSON documents, supports the point.

## What does cloud native actually change?

Most of the middle is about how applications are built now, and why the database cannot sit it out. The traditional model is a steam train: requirements, technical design, architecture, code, and a first testable build two years later, by which time the requirements have moved. The model he prefers is a flock of birds, where each microservice reacts to its neighbours and the whole shape shifts smoothly.

He picked four buzzwords that he thinks have now earned their keep: agile, microservices, DevOps and CI/CD. The DevOps point is the classic one: you do not fix a server, you change the Ansible playbook and rerun it, and in the container world you throw the container away and start a new one. On CI/CD he admitted a change of mind. He had assumed continuous delivery was the hard part, until he realised continuous integration is harder, because it means the application in the repository must be deployable at every moment. For a database person that drags in continuous testing and test data management.

Measurement comes from DORA: deployment frequency, how fast you restore a service, going from a release every year to one every couple of hours. And his warning about hype applies to the AI wave too: cloud took 10 to 15 years before people really understood how it changed day-to-day IT, so start from your own requirements, not the vendor's buzzword.

## What does the operator do?

The Postgres part arrives near the end. CloudNativePG, created by Gabriele Bartolini and team and now a CNCF project, runs Postgres the Kubernetes way. Jan Karremans said at Conf42 Cloud Native 2024: "rather than bringing Kubernetes to postgres, what we did is take postgres and actually bring it to Kubernetes". The operator covers day one and day two operations, including high availability, switchover and load balancing, so the user deploys and uses it. In his words, "it captures a database administrator, puts it in a box, right?"

At the time of the talk the project had just passed 3,000 GitHub stars. His closing point is that both projects are community governed, so the people using them decide where they go next.

## Who should watch?

DBAs and data people who still think of Kubernetes as infrastructure that is built to break, and platform teams who need an argument for why stateful workloads are no longer off-limits. If you already run CloudNativePG in production, this one is the why, not the how.

## Related Conf42 talks

- Chris Engelbert of simplyblock on [PostgreSQL on Kubernetes: dos and don'ts](https://www.conf42.com/Internet_of_Things_IoT_2024_Chris_Engelbert_kubernetes_postgresql_cluster) at Conf42 IoT 2024.
- Rohit Mishra on [how Kubernetes operators work](https://www.conf42.com/DevOps_2024_Rohit_Mishra_deepdive_kubernetes_operators) at Conf42 DevOps 2024.
- Natalie Pistunovich on [a Kubernetes operator for a distributed database](https://www.conf42.com/Cloud_Native_2021_Natalie_Pistunovich_k8s_operator_distributed_database) at Conf42 Cloud Native 2021.

[Watch Jan Karremans's talk](https://www.conf42.com/Cloud_Native_2024_Jan_Karremans_databases_kubernetes), part of [Conf42 Cloud Native 2024](https://www.conf42.com/cloud2024).

## From Cybertec

CYBERTEC is a pure-play PostgreSQL company that helps organisations adopt Postgres.

- [Cybertec website](https://www.cybertec-postgresql.com/en/)

[Watch the talk on YouTube](https://youtu.be/CnlvlA5jnh0).

## Watch the talk

[Just don’t do it – Databases in Kubernetes](https://www.conf42.com/Cloud_Native_2024_Jan_Karremans_databases_kubernetes) at Conf42 Cloud Native 2024.
