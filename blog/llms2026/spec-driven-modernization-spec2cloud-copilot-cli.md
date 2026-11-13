# Modernizing a .NET 4.8 app by writing the specs first

Conf42 Blog, 2026-05-31, updated 2026-11-09. https://www.conf42.com/blog/llms2026/spec-driven-modernization-spec2cloud-copilot-cli

In short: Marco Antonio Silva (Microsoft) at Conf42 LLMs 2026 takes a legacy .NET app to .NET 10 with the GHCP Modernization CLI, then reverse-engineers specs with Spec2Cloud.

Legacy modernization usually dies on the business case: three to five years of migration work with few new features to show for it. At Conf42 Large Language Models (LLMs) 2026, Marco Antonio Silva, a Senior Global Black Belt in Microsoft's EMEA migrate and modernize team, argues that LLMs can do most of the heavy lifting if you stop prompting your way through the code and make the specification the centre of the work.

The talk is two live demos on the same sample app, Contoso University: an ASP.NET MVC application on .NET Framework 4.8 with an old Entity Framework, SQL Server, IIS and Microsoft Message Queuing for notifications. Both tools shown are Microsoft's (one open source), so expect product on screen; Marco frames it as approaches rather than a pitch.

## Specs become the oracle, code the byproduct

The core idea is spec-driven development. Instead of vibe coding, you build human-readable and machine-readable documents first: features, acceptance criteria, business rules, schemas, APIs, architecture, tech stack. The model works against those, retrying until the acceptance criteria pass. The prompt matters less, the spec matters more, and specs can be reverse-engineered from existing code. Nothing about this is new for human teams, he notes; good documentation always made the target easier to hit.

## Path one: a deterministic assessment, then agents

The GitHub Copilot (GHCP) Modernization CLI handles Java and .NET. Its first step isn't an LLM at all: it downloads deterministic assessment tools such as AppCat that understand the frameworks and their dependencies. On Contoso University the assessment flagged the local file system, MSMQ that should move to Service Bus, Windows AD that should move to Microsoft Entra, and the framework itself, grouped into three waves with T-shirt sizes.

Only then do agentic skills take over. The plan step produced five tasks (messaging, authentication, the database, local files to Azure Storage, connection strings to Key Vault), written to a plan file you can read and edit before anything runs. Execution follows the critical path first, builds after each task and feeds compiler errors back into the loop. By the end of the demo the same app runs on .NET 10 with modern app settings and packages.

## Path two: get the documentation you never had

Spec2Cloud is the open-source option for when there's no tooling for your stack, or you want a deeper refactor than a framework upgrade. Run it in a brownfield repo and it installs dozens of skills into GitHub Copilot. The approach is fully agentic and, as Marco says plainly, non-deterministic but grounded.

On the same app it found the main issues the deterministic tool had found, then wrote architecture decision records with options, pros and cons and a recommended choice for a human to approve. Next it reverse-engineered product and feature requirement documents: student, course, instructor and department management, each with user stories, acceptance criteria and a pointer to where the current code implements them, plus Mermaid diagrams of the workflows. A state file and audit log keep the context in the repo, so a new session can pick up where the last stopped.

His point about that step is the one worth stealing. Even if you never modernize, a legacy system whose builders have left now has specs, and a new feature becomes one more requirement document on top of the rest.

## Keep the boring checks

Not everything should be agentic. Compiling, linting and CI checks you already run for humans should keep running for agents. Spec validation stays human-readable, an LLM can judge output against the acceptance criteria, and a human still signs off the pull request.

## Who should watch

Teams sitting on .NET Framework or old Java estates, architects writing a modernization business case, and anyone curious how spec-driven development works on code that already exists. If you're on a stack neither tool covers, the Spec2Cloud half is the part for you.

## Related Conf42 talks

- [Monolith to Microservices with AWS App2Container and Amazon Q](https://www.conf42.com/Cloud_Native_2024_Richard_Lees_Jorge_Alvarez_monolith_microservice_modernization) by Richard Lees (AWS), the Strangler Fig take on the same problem.
- [Modernizing Legacy Applications](https://www.conf42.com/Golang_2025_Rajkumar_Chindanuru_legacy_modernization_strategies) by Rajkumar Chindanuru (Tailored Brands), on strategy before tooling.
- [AI-Powered Zero-Touch Integration](https://www.conf42.com/Machine_Learning_2025_Narendra_Chennupati_migration_legacy_integration) by Narendra Chennupati, on AI-assisted legacy-to-cloud migration.

[Watch Marco Antonio Silva's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Marco_Antonio_Silva_modernization_specs_cloud)

[Watch the talk on YouTube](https://youtu.be/nhz-9_B3Ls0).

## Watch the talk

[Spec Driven Modernization: Modernize your Repository using Spec2Cloud and the GHCP Modernization CLI](https://www.conf42.com/Large_Language_Models_LLMs_2026_Marco_Antonio_Silva_modernization_specs_cloud) at Conf42 Large Language Models (LLMs) 2026.
