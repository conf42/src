# From chroot to Codespaces, the long war on works-on-my-machine

Conf42 Blog, 2023-01-25. https://www.conf42.com/blog/devops2023/codespaces-ends-works-on-my-machine

In short: Rizel Scarlett (GitHub) at Conf42 DevOps 2023 on why developers code inside containers and how GitHub Codespaces turns dev containers into config as code

Every new hire has received the setup document that takes a day to a week to get through. Rizel Scarlett, Developer Advocate at [GitHub](https://github.com/enterprise), used her Conf42 DevOps 2023 talk to explain why developers moved their work into containers in the first place, then showed how GitHub Codespaces turns a development container into something a team keeps in the repository and opens in a browser.

The first half is a friendly container history for anyone who nodded along to Docker install instructions without knowing why. The second half is a tour of Codespaces features, from dev container configuration to GPU-backed notebooks.

## Why develop inside containers at all?

Scarlett starts with a confession: when she began her career in 2018 she received install instructions mentioning Docker and Kubernetes on day one and had no idea what containers were. Her answer now is the phrase every engineer has said or heard: it works on my machine. Slightly different environment variables or settings, and a fix that worked locally breaks for a teammate or in staging.

She quotes Docker's definition of a container as a standard unit of software that packages up code and all its dependencies so it runs reliably from one computing environment to another. The point is that development mirrors production, with the same operating system, configuration and dependencies.

## Docker didn't invent containers

Her short history lesson:

- **1979, chroot**: change the root directory for a process, an isolated environment for builds and dependencies.
- **2000, FreeBSD jails**: isolate and test changes without endangering the rest of the system, with designated IP addresses.
- **2006, Google's process containers**, later renamed control groups (cgroups): limiting and isolating CPU, memory, disk I/O and network.
- **2013, Docker**: founded by Solomon Hykes, which popularised containers by making them easy, with a suite of management and packaging tools.

All of it, she says, is one long pursuit of running software reliably from one environment to another.

## What Codespaces is, and what it isn't

Codespaces is an IDE in the browser (VS Code, JetBrains or JupyterLab) running inside a development container on a virtual machine. She separates it from the GitHub web editor you open by pressing the period key on a repository: that editor is fine for fixing a YAML indent, but has no terminal and cannot run code. Codespaces has a terminal, a choice of machine types, and runs your app. At the time of the talk users got 60 hours of free Codespaces usage a month; the web editor is free.

The benefits she lists are faster onboarding, coding from anywhere (she has used it on a plane and on an iPad), and uniform environments.

"I can commit code day one. I don't need to do the setup stuff," Rizel Scarlett said at Conf42 DevOps 2023, describing the new-hire experience when the environment comes preconfigured.

## How does configuration as code work here?

The setup lives in the repository, so it gets version control, a single source of truth, CI checks such as linting and security scanning, and a commit history to blame when a stray comma breaks things. Three files do the work:

- **devcontainer.json**: extensions to install (her Node.js example adds ESLint, Prettier and Live Share), environment variables, forwarded ports such as 3000, and post-create commands like yarn install.
- **Dockerfile**: the image itself; hers is a single Node 16 Bullseye line.
- **docker-compose.yml**: for multiple containers, for example a Postgres database next to a web server.

## Use cases beyond onboarding

She walks through several:

- **Teaching**: a front-end exercise where the browser preview and HTML, CSS and JavaScript files open side by side through the CodeSwing extension, with CodeTour prompts guiding students step by step, and everyone on the same theme so nobody asks why their highlighting is a different colour.
- **Experimenting**: templates for Rails, React, Jupyter, Express and Next.js skip the boilerplate; she edits a Next.js demo live and the preview updates.
- **Pair programming**: port forwarding with a shareable URL, visible publicly or only to your organisation, to prove it does work on your machine.
- **The command line**: the gh CLI lists, creates, renames (a display name, the permanent name stays) and deletes codespaces.
- **AI**: a GPU-powered codespace (then in limited beta) running Stable Diffusion from a Jupyter notebook, with the Hugging Face token stored as a Codespaces secret. The resulting images were, in her words, scary looking.

## Who should watch

Developers who use containers without quite knowing why, team leads tired of week-long onboarding, and instructors who run remote coding workshops. Teams already standardised on dev containers will mostly pick up the CLI and port-sharing tips.

## Related Conf42 talks

- Justin Dearing on [Docker and dev containers on Windows](https://www.conf42.com/Python_2025_Justin_Dearing_docker_windows_devcontainers) at Conf42 Python 2025.
- Anita Ihuman on [mirroring production on your local machine](https://www.conf42.com/Kube_Native_2024_Anita_Ihuman_local_machine_mirror_dev_environment) at Conf42 Kube Native 2024.
- Hamida Rebai on [.NET microservices and the Docker ecosystem](https://www.conf42.com/DevOps_2023_Hamida_Rebai_net_microservices_docker_ecosystem) at Conf42 DevOps 2023.

[Watch Rizel Scarlett's talk](https://www.conf42.com/DevOps_2023_Rizel_Scarlett_developing_inside_containers_codespaces_containerization)

## From GitHub

GitHub hosts code and the tooling around it, from Actions and Codespaces to security features, with an enterprise offering for larger organisations.

- [GitHub Enterprise](https://github.com/enterprise)

[Watch the talk on YouTube](https://youtu.be/Q-64335Gbwc).

## Watch the talk

[Why are people developing inside containers? How Codespaces takes containerization to the next level](https://www.conf42.com/DevOps_2023_Rizel_Scarlett_developing_inside_containers_codespaces_containerization) at Conf42 DevOps 2023.
