# Continuous Agentic Deployment runs a Kanban board of AI agents

Conf42 Blog, 2026-05-30, updated 2026-11-09. https://www.conf42.com/blog/llms2026/continuous-agentic-deployment-github-kanban-agents

In short: Denis Ermakov at Conf42 LLMs 2026 shows CAD, an open-source GitHub-only pipeline where agents analyse, code and test, and a human kicks the deploy.

Getting a model to write code is the easy ten percent; the other ninety is retries, validation, cost control and a clear point where a human stays in charge. That is the claim Denis Ermakov, Lead Software Engineer at Tehpotok, makes at Conf42 Large Language Models (LLMs) 2026, and he backs it with a live, open-source pipeline called Continuous Agentic Deployment (CAD) that keeps shipping features while he talks.

The talk opens on a project board where cards move with nobody touching a keyboard. The app those agents built, CAD Console, is the dashboard that visualises the pipeline itself, which is a pleasingly recursive demo.

## GitHub is the whole runtime

There's no orchestrator service: no Temporal, no Airflow, no database. A GitHub Project board is the state machine (columns are states, moving a card is a transition), GitHub Actions is the agent runtime (each agent is one workflow run, with the secrets and logs you already trust), and issue comments are the context bus. Every station writes its output as a comment the next one reads, so the comment thread doubles as the audit trail.

The board has eight columns: to do, ready, SABA (system and business analysis), dev, test, human review, deploy, done. A one-line request like "show a KPI card naming the quickest shipped feature" goes in; the analysis agent turns it into affected files, approach, acceptance criteria and edge cases for the agents downstream.

## Work in progress limits make it a pull system

A dispatcher ticks over the board, checks each station's WIP limit and spawns a workflow run for any free slot. In the demo dev has a limit of one and analysis two, so analysis stalls when dev is busy, exactly like a human Kanban team. Idle agents don't exist, so idle capacity costs nothing.

Models and WIP limits live in repository variables, not code. Denis shows Claude Sonnet 4.6 on analysis and test, with pricier models reserved for dev and for the fixer and merge-conflict agents. Changing the economics of the line is editing a variable.

Every station has the same five-part shape: workflow, prompt file, WIP limit, model, board column. Adding a security-review stage means a new prompt, a copied workflow, a column and one hop in the dispatcher, with no changes to existing stations. That inversion of control is why he calls it a framework rather than a clever repo.

## Reliable lines from unreliable parts

Agents get things wrong, so the conventions carry the reliability:

- The spec lives in the tests. Acceptance criteria from analysis become the test suite, and code moves only when it passes.
- Self-correction is bounded. A failing card gets up to three fix attempts; as Denis puts it, "Three, not infinite, because infinite is just a way to burn money and stack the problem." After that the line stops and hands it to him.
- Every card works on its own branch, so parallel agents never share a working copy. When two features edited the same stylesheet, a resolver agent rebased and fixed the conflict without him.
- The deploy has no model in it. It is a deterministic script that merges, builds, ships and then checks that the live URL reports the exact commit it just built. A human presses the button, by design.

He is candid about the limits too. Agents do well on small, well-scoped, test-backed changes and struggle with ambiguous specs and big cross-cutting refactors. The real bottleneck was good issues on a codebase where features are additive, not the model. And today the engine is still fused to the one app it builds; pulling them apart is next.

## Who should watch

Platform and DevOps engineers wondering how to put coding agents into CI/CD without buying an orchestration product, and anyone who has run Kanban and wants to see WIP limits applied to agents. If you only want a prompt library, skip it; the prompts are the least interesting part.

## Related Conf42 talks

- [Building Enterprise-ready CI/CD Pipelines using Agentic AI](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) by Chinmay Gaikwad (Harness), the vendor-platform take on the same goal.
- [Green Checkmarks, Red Flags: What CI/CD Can't Catch](https://www.conf42.com/DevOps_2026_Tilda_Udufo_cicd_quality_testing) by Tilda Udufo, a reminder that passing tests are not the same as quality.
- [When AI Ignores the Deny List](https://www.conf42.com/DevSecOps_2026_Oleksandr_Kryvchenko_claude_cicd_pretooluse) by Oleksandr Kryvchenko (Keeper Security), on fencing in agents that run in pipelines.

[Watch Denis Ermakov's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Denis_Ermakov_deployment_cicd_automation)

[Watch the talk on YouTube](https://youtu.be/4sVcBDulFFg).

## Watch the talk

[Continuous Agentic Deployment: An Open-Source Framework for AI-Powered CI/CD Pipelines](https://www.conf42.com/Large_Language_Models_LLMs_2026_Denis_Ermakov_deployment_cicd_automation) at Conf42 Large Language Models (LLMs) 2026.
