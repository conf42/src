# GenOps treats the AI in your pipeline like a supervised junior engineer

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/genops-governance-ai-agents-cicd

In short: Meta staff engineer Neeraj Kumar Singh Beshane at Conf42 DevOps 2026 on GenOps, a governance model with blast-radius scores and signed AI changes.

Ask an LLM to optimise the same Dockerfile three times and you get three different Dockerfiles. In a CI/CD pipeline, that variance is a bug. At Conf42 DevOps 2026, Neeraj Kumar Singh Beshane, a staff software engineer at Meta whose career runs through Wayfair, JPMorgan Chase and American Express, presented GenOps: a governance-first way to let generative agents act inside pipelines by giving them the same supervision you would give a new hire.

## Faster coding, shakier delivery

He frames the problem with industry numbers: high reported AI adoption, the promised productivity boost from coding assistants, and the 2024 DORA finding that delivery stability dropped for teams rushing to adopt AI. His metaphor: a faster car with the seat belts taken out.

Then a near miss from his own experience. An AI agent working through Terraform looked at a legacy authentication handler, saw no recent commits, decided it was unused and tried to delete it. That service authenticated 20 million users. A human caught it, and he admits it kept him up for a week.

## From helper to pipeline actor

The mental shift is the core of the talk. A chatbot or coding assistant is an external helper with zero accountability: if its suggestion breaks the build, you broke the build. In GenOps the AI is a pipeline actor with a service account and permissions, it triggers builds and opens its own pull requests. That sounds terrifying until you compare it with onboarding a junior engineer: sandbox first, every PR reviewed, no unsupervised production deploys at 5pm on a Friday.

## Four pillars of governance

- **Context.** RAG over build history, incidents, postmortems and Slack threads. Before the AI prepares a deployment, the prompt is intercepted and the relevant recent builds plus current infrastructure state are injected, so it knows that the last time someone touched this config it leaked memory.
- **Blast-radius scoring.** Before a merge, the dependency graph is analysed: a README change scores low and auto-merges, a change to a core auth library used by dozens of services scores high and needs a human. Scores map to error budgets per service, enforced with Open Policy Agent as a pass-or-fail gate, not a PDF.
- **SLO-based canaries.** Deploy to 1% of traffic, watch latency, error rate, CPU, memory and IO, and roll back automatically if latency drifts by two standard deviations. No waiting for a customer tweet or a PagerDuty alert.
- **Runtime assurance.** Every AI-generated change is cryptographically signed with the exact model version, prompt and injected context, so you can later query every service touched by a given model. Auditors, he suggests, will like this better than human changes.

## The 14.4% that would have been outages

His headline result is a protection rate: in 14.4% of cases, despite all the context and prompting, the AI tried something dangerous (an SLA-violating change, a vulnerable dependency) and the governance layer blocked it. He also reports a 55% faster cycle time and a Meta tool that turned a multi-hour onboarding task into a five-minute automated flow. The blocks are fed back into memory, so the system learns from its near misses.

## Who should watch

Platform and DevOps leads being asked to put agents into CI/CD, and security teams being asked to approve it. If you want a vocabulary for that negotiation (blast radius, error budgets, signed provenance), this talk has it. His Formula One line sums it up: the brakes are there so the driver can go fast.

## Related Conf42 talks

- [Oleksandr Kryvchenko on what happens when AI ignores the deny list](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) at Conf42 DevSecOps 2026, a hands-on look at guardrails failing.
- [Sonu Kumar on AI-native DevSecOps with governed platform engineering](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai) at Conf42 DevSecOps 2026.
- [Karishma Velisetty on governing AI code assistants under SOX and ICFR audits](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants) at Conf42 Large Language Models 2026.

[Watch Neeraj Kumar Singh Beshane's talk](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity)

[Watch the talk on YouTube](https://youtu.be/YcGxfYXwUvI).

## Watch the talk

[GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) at Conf42 DevOps 2026.
