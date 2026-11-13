# Eight Copilot agents that build, deploy and document Azure demos

Conf42 Blog, 2026-08-27, updated 2026-11-09. https://www.conf42.com/blog/agents2026/azure-demo-scenarios-built-by-agents

In short: Peter De Tender of Microsoft at Conf42 AI Agents 2026 shows Trainer Demo Deploy, now with an agent pipeline that writes Bicep, deploys via azd and drafts the demo guide.

Deploying something in Azure is easy; turning it into a demo with real data, a working app and a script to follow is the part that eats your week. At Conf42 AI Agents 2026, Peter De Tender, Senior Content Developer at Microsoft, showed how his open source Trainer Demo Deploy catalog grew a multi-agent mode: eight GitHub Copilot agents that take a one-line prompt and produce a deployable, documented Azure scenario.

Peter has been in the Microsoft space for 30 years, starting with power cabling in physical data centers, and spent years as a Microsoft technical trainer who needed a fresh Azure demo for nearly every teaching day. That pain is the whole origin story.

## A deployment is not a demo

He opens with the problems anyone who has presented Azure will recognise. Quickstart templates spin up infrastructure but no sample data. A storage account with nothing in it shows nothing. A richer workload (storage, Event Grid, Functions, AI services, Logic Apps, Cosmos DB, Application Insights) needs application code deployed on top of the Bicep. And the moment the demo works, someone asks to reuse it or turn it into a proof of concept.

Trainer Demo Deploy started about four years ago as an internal Microsoft project for around 125 trainers, with an Azure DevOps back end. It is now fully open source and GitHub based, with around 80 community-authored scenarios and close to 12,000 deployments over the last three years. Each scenario card lists a 24-hour cost estimate, an install time, its app dependencies and a demo guide. Scenarios stay owned by their authors; they are not official Microsoft templates, and Peter is clear about that.

## Four commands and a purge flag

The deployment vehicle is the Azure Developer CLI. The live demo is refreshingly unedited: make a folder, `azd init` to clone the scenario, `azd up` to pick a subscription and region, wait about two and a half minutes for a storage scenario, then follow the guide through blob containers and file shares. He even hits the classic "no project" error from running in the wrong subfolder and leaves it in.

The practical tip worth remembering is `azd down` with purge and force. Without purge, soft-deleted resources such as Key Vault or AI services linger for weeks and block an identical redeploy. With it, you can run `azd up` again the next minute and get the exact same state back.

## The agentic part: a conductor and seven helpers

Users kept asking for custom scenarios, and building, testing and validating a new one is the slow part. So the repo now ships agents for GitHub Copilot in VS Code or the Copilot CLI, as plain Markdown agent, prompt and skill files under `.github`. No Foundry back end needed.

You talk only to the conductor. It asks follow-up questions (industry, sample app, security or high-availability needs), proposes an architecture validated against the Well-Architected and Cloud Adoption Framework guidance, and waits for your approval. Then it writes modular Bicep, preferably with Azure Verified Modules, builds a .NET sample app, deploys with azd, rolls back and retries when a deployment fails, runs Playwright UI tests, and writes a demo guide with screenshots. Finally it offers to contribute: the scenario lands in your GitHub account and a PR goes to the catalog, where Copilot and a human maintainer review it.

His example prompt asked for App Service plus Cosmos DB for healthcare. The result went further than asked: deployment slots, Application Insights, managed identity and private endpoints to the database, because the agent instructions bake those practices in. The run took long enough that he closed his laptop overnight, which is the most literal reading of "deploying while sleeping" you could hope for.

## Who should watch

Trainers, consultants, solution engineers and cloud admins who show Azure to other people and are tired of hand-building demos. It is also a useful reference for anyone designing an infrastructure agent pipeline, because the human approval gate sits at the architecture step and the agent's output is plain Bicep you can read. The first half is a product walk-through of the static catalog; the agents arrive around the fifteen-minute mark.

## Related Conf42 talks

- [Your Agent Can Write Terraform. It Can't Feel What It Breaks.](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) by Kevin Brown at Conf42 Prompt Engineering 2026.
- [Using Azure AI Foundry to manage all your Large Language Models](https://www.conf42.com/Large_Language_Models_LLMs_2025_Peter_De_Tender_azure_models_management) by Peter De Tender at Conf42 Large Language Models 2025.
- [Building Enterprise-ready CI/CD Pipelines using Agentic AI](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) by Chinmay Gaikwad at Conf42 DevOps 2026.

[Watch Peter De Tender's talk](https://www.conf42.com/AI_Agents_2026_Peter_De_Tender_azure_deployment_automation) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/4gDWlMCo11A).

## Watch the talk

[What if you could deploy Azure end-to-end scenarios while sleeping?](https://www.conf42.com/AI_Agents_2026_Peter_De_Tender_azure_deployment_automation) at Conf42 AI Agents 2026.
