# DevOps engineers should enable more and do less

Conf42 Blog, 2024-01-25. https://www.conf42.com/blog/devops2024/devops-engineers-enable-not-do

In short: Michael Zion (MeteorOps) at Conf42 DevOps 2024 on a CTO's DevOps handbook - developers operate, DevOps enables, and knowing when to do what.

Ask five engineers to define DevOps and you get six philosophies and a Slack thread. At Conf42 DevOps 2024, Michael Zion, co-founder of MeteorOps, offered CTOs a deliberately plain definition (developers operate the system; DevOps engineers enable them to, and operate some of it themselves) and a set of when-to-do-what rules that follow from it.

It is a short, practical talk built on MeteorOps' CTO DevOps Handbook, aimed at founders and engineering leaders who know they need DevOps but not what to expect from it.

## What is DevOps actually for?

Zion starts with the two goals of any software company: serve the product, and keep building and improving it. The second goal is an experiment loop. He borrows a point from Uncle Bob's retelling of Dijkstra: programming never became the mathematical discipline of proven functions Dijkstra hoped for. We treat it as a science instead; we change something and test whether it worked. DevOps is what makes that loop cheap.

"Operate" gets a concrete list: provision, deploy, monitor, secure, configure, and scale up and down. Every company picks its own split of those duties between developers and DevOps engineers. The word to remember from the slide, he says, is enable.

## Enabler, doer, automator

Within that split, a DevOps engineer chooses how much to enable, do and automate. His example is a developer asking for a database. The doer clicks through the console and creates it. The automator writes a script and runs it themselves. The enabler hands the developer a tool or the knowledge to create it on their own.

The principle he wants CTOs to keep: "tools have bigger leverage, better leverage than knowledge, and enable has much more leverage than doing," Michael Zion said at Conf42 DevOps 2024. Doing is the least scalable mode because it is capped by one engineer's free hours that week. He has seen companies at both extremes, from full freedom plus onboarding on the tools to DevOps teams that abstract everything away.

## How to pick tools without regret

His three biggest time savers in a tool:

- Native state management, as in Terraform, Kubernetes or Pulumi. As a system grows you cannot change it safely without knowing what exists, and building that yourself is not trivial.
- A big community and good docs, so somebody has already hit your bug.
- Multiple interfaces (API, CLI, UI), because the tool will be glued to scripts and services sooner or later.

## Goals worth setting

Two examples from the handbook. One-click environments: the whole system created with one command or pipeline run, because experiments need environments. And split shared and environment-specific resources: once a company is running, say, 30 open pull requests at any moment, a Kubernetes cluster per pull request is slow and expensive. Keep the cluster, network and database instance shared, and deploy only the application and a migration that creates its own database.

## When to do what

The scenarios are where the talk earns its title. Working alone on a simple system: Dockerize, add post-commit tests, keep it simple; he sees plenty of founders writing Terraform at this stage without a reason to. Need new environments quickly for developers or a client who wants their own cloud account: build the one-click environment. End-to-end tests start hurting: split shared and specific resources. Complexity grows and operations need standardising: bring in an orchestrator such as Kubernetes.

The recap fits on a sticky note: devs operate, DevOps enables and operates, choose the balance, use tools wisely, set useful goals, know when to do what.

## Who should watch

Early-stage CTOs and VPs of engineering deciding what their first DevOps hire should do, and DevOps engineers who want language for pushing back on doer work. Experienced platform teams will find it familiar; the value is in how simply it is put.

## Related Conf42 talks

- Tomasz Manugiewicz on [how a CTO views DevOps transformation](https://www.conf42.com/DevOps_2024_Tomasz_Manugiewicz_cto_view_transformation) at Conf42 DevOps 2024.
- Natalie Lunbeck on [ephemeral environments](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments) at Conf42 Cloud Native 2024.
- Karamveer Kaur Sangha on [platform engineering with GitHub Actions and Prometheus](https://www.conf42.com/DevOps_2024_Karamveer_Kaur_Sangha_platform_engineering_github_actions_prometheus) at Conf42 DevOps 2024.

[Watch Michael Zion's talk](https://www.conf42.com/DevOps_2024_Michael_Zion_cto_handbook_principles_examples)

## From MeteorOps

MeteorOps is a DevOps services company; the full handbook, with more when-to-do-what scenarios, is on its blog.

- [MeteorOps website](https://meteorops.com/)
- [The CTO DevOps Handbook: Simple Principles and Examples](https://www.meteorops.com/blog/the-cto-devops-handbook-simple-principles-and-examples)

[Watch the talk on YouTube](https://youtu.be/zm3_tonsdeM).

## Watch the talk

[The CTO DevOps Handbook: Simple Principles and Examples](https://www.conf42.com/DevOps_2024_Michael_Zion_cto_handbook_principles_examples) at Conf42 DevOps 2024.
