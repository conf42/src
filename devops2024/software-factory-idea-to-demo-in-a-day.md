# Start your software factory with a catalog, not a cloud

Conf42 Blog, 2024-01-24. https://www.conf42.com/devops2024/software-factory-idea-to-demo-in-a-day

In short: Murali Mallina (Softrams) at Conf42 DevOps 2024 on software factories that take an idea to a deployed demo in a day, and why you shouldn't build your own cloud.

How long does it take your organisation to go from a product manager's idea to a URL the customer can click? At Conf42 DevOps 2024, Murali Mallina, CTO of Softrams, argued that the answer can be a day, and that the way to get there is a software factory built catalog-first on managed cloud services, not a home-grown cloud stitched together from every project in the CNCF.

Softrams builds and operates mission-critical systems for US federal agency customers, so this is a talk from a team that has to ship inside real guardrails, not a startup with a blank AWS account.

## What problem is a software factory solving?

Mallina frames it with personas. Emma, the product manager, has a new idea from a customer call. Sneha, a full-stack developer, wants a sandbox with de-identified data to try an LLM feature. Avery has just joined and needs to land her first pull request. In most organisations, he says, each of those journeys takes months, at best weeks. His goal is days, then hours.

The origin story is a Slack message he sent in 2018: if I request a new project and give it a name, the platform should create a repository from an API boilerplate, create the dev branch (Softrams does trunk-based development with dev as main), wire the CI/CD hooks, build and test the sample, deploy the container, configure a CNAME, and hand back the URL of the health check. That one paragraph became the spec.

## Six capability areas, not four

He groups the capabilities into knowledge (a catalog of services, libraries, starters and design systems), infrastructure (repos, sandboxes, environments), delivery (CI/CD, configuration, observability) and governance (security, cost controls, access, data). Then he adds two that most platform engineering conversations skip: research (data analytics, existing research, policies) and design (branding, design systems, UI libraries). If the factory only covers build-deploy-operate, product teams still start every idea from scratch.

His working definition borrows the Wikipedia one: a product line that configures tools, processes and content from templates, so you assemble rather than reinvent. Softrams' internal implementation, codename Eagle, treats platform engineering and the internal developer portal as one product rather than two teams.

## Build it from the inside out

The rings, in order: catalog first, then self-service, then infrastructure, then automation, then governance. Treat it like a product and ship the most important use case first.

- The catalog needs no fancy tool: collect your scripts, generators, starters and wiki pages, document them, and you already have a chunk of a factory.
- Self-service with guardrails beats approval queues; approvals are fine as long as they don't add friction or delay.
- Governance is where to tread carefully: thresholds and policies, but never in the way of the experiment.

If you already run low-code platforms, he notes, you may have a working software factory for part of your workload.

## Why not just install the CNCF?

This is the sharpest part. For teams on one cloud, Mallina points at AWS Service Catalog before any new product; for multi-cloud, he names Cloud Foundry, Humanitec and OpsLevel as things to evaluate before building. Softrams went through AWS Amplify, Terraform modules and AWS CDK before landing Eagle on Kubernetes, with Crossplane to bring managed services such as S3 under the same workflow, Backstage as the portal and knowledge base, and Tekton for CI/CD.

On self-hosting every shiny project, he is blunt. "Every single service that you bring you are just increasing your total cost of ownership exponentially," Murali Mallina said at Conf42 DevOps 2024. Setup, backups, versions, migrations and security all land on you.

His first rule in the closing list follows from that. "Do not try to build your own cloud," Murali Mallina said at Conf42 DevOps 2024. Prefer serverless and fully managed services, map the journey (journey map, value stream map or service blueprint), automate the most expensive steps, then rinse and repeat. And to win the argument internally, build the MVP and show the difference instead of pitching the whole platform.

## Who should watch

Platform and DevOps leads deciding whether to buy, assemble or build an internal developer platform, and CTOs who want a vocabulary for the research and design side that most IDP talks leave out. There is no live demo; it is a strategy talk with concrete tool choices.

## Related Conf42 talks

- Jon Peck on [securing the software factory](https://www.conf42.com/DevSecOps_2022_Jon_Peck_securing_software_factory) at Conf42 DevSecOps 2022.
- George Hantzaras and Dan Mckean on [self-service DBaaS in an internal developer platform](https://www.conf42.com/Cloud_Native_2023_George_Hantzaras_Dan_Mckean_self_service_dbaas_internal_developer_platform) at Conf42 Cloud Native 2023.
- Natalie Lunbeck on [ephemeral environments](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments) at Conf42 Cloud Native 2024.

[Watch Murali Mallina's talk](https://www.conf42.com/DevOps_2024_Murali_Mallina_060_on_day1)

## From Softrams

Softrams builds and operates software systems for US federal agency customers, and its teams run the Eagle platform described in this talk.

- [Softrams website](https://www.softrams.com/)

[Watch the talk on YouTube](https://youtu.be/-isNp3F8Gh4).

## Watch the talk

[0 to 60 on Day 1: The Promise of Software Factories](https://www.conf42.com/DevOps_2024_Murali_Mallina_060_on_day1) at Conf42 DevOps 2024.
