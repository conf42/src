# One monorepo, two clouds, and a pipeline per target, not one big YAML

Conf42 Blog, 2023-03-30. https://www.conf42.com/cloud2023/github-actions-reusable-workflows-monorepo-multicloud

In short: Rob Earlam (Sitecore) at Conf42 Cloud Native 2023 on deploying a headless CMS monorepo to Azure and Vercel with path-filtered, reusable GitHub Actions workflows

A one-line change to a Next.js site should not redeploy a .NET app in another cloud. At Conf42 Cloud Native 2023, Rob Earlam, Senior Developer Advocate at Sitecore, showed how his team moved four sites into one open source monorepo backed by a SaaS headless CMS, deployed them to Azure and Vercel, and got there by throwing away their first single pipeline in favour of one pipeline per target built from reusable GitHub Actions workflows.

Sitecore's XM Cloud is the CMS in the story, but the talk is about the CI/CD pattern, and the YAML walkthrough applies to any monorepo with mixed deployment targets.

## What were they migrating from?

Two separate monoliths: one on Azure Web Apps hosting the SUGCON Events and SUGCON ANZ sites, one on AKS hosting the MVP site (with its application process) and SUGCON EU. Two code bases meant always checking which one you were in, one was open source and the other closed, and the infrastructure behind both made for an Azure bill his manager was presumably not thrilled about. A migration from the first to the second had stalled halfway.

When Sitecore released its SaaS CMS, XM Cloud, most of that infrastructure moved into the product. What was left to host was the heads of a headless CMS, so each site could go wherever suited its technology.

## Why two clouds?

Technology fit. The MVP site is an ASP.NET 6 application with real interactivity, ported mostly as-is, so it went to an Azure Web App. The three SUGCON sites are content-heavy, largely static Next.js sites, so they went to Vercel. One of them is purely static content with no CMS behind it, but it still lives in the same repository. They kept the open source model because the community interaction around the old public repo had been worth it.

## What went wrong with the first pipeline?

The first iteration was one big YAML file: push configuration and content to XM Cloud, deploy the three Vercel sites, deploy the .NET site to Azure, on every commit. "And it worked. It did, but it was really heavy," Rob Earlam said at Conf42 Cloud Native 2023. Developers needed targeted deployments to iterate quickly.

## How is it split now?

By target system: separate CI/CD workflows for XM Cloud, the MVP site, SUGCON EU and SUGCON ANZ. The workflows folder has a naming convention that makes the structure obvious:

- **build_** workflows say how to build a type of application (.NET, Next.js).
- **deploy_** workflows deploy an artifact to one platform (Azure Web App, Vercel, XM Cloud).
- **CI-CD_** workflows wire them together for one site.

Each CI-CD workflow triggers on push and pull request only for the paths that matter: the site's own source folders plus the build and deploy workflows it uses, so a change to the shared deploy template retests every site that depends on it. A workflow_dispatch trigger adds a manual run button in the Actions UI.

## What does a deployment look like?

For the MVP site, the build job uses MSBuild rather than the dotnet CLI because some old .NET Framework code remains: check out, set up MSBuild, install NuGet, restore, build in Release. The deploy job declares needs on the build, so ordering is explicit, and receives parameters (debug configuration for staging, so it logs more), plus the Azure publishing profile from GitHub secrets. On a Windows runner it sets up .NET 6, then restores, builds and publishes with the dotnet CLI and pushes the output to the web app. Every commit goes to staging. A production job guarded by an if on the main branch runs only after a merge, in Release mode.

Vercel works differently. There is one deploy job for both preview and production, because the Vercel CLI takes a production flag instead of separate apps. The Next.js build runs on lightweight Ubuntu runners: set up Node, npm install, build and lint. The deploy uses a community-built Vercel action with the token, organisation ID and project ID as secrets, adding the production flag on merges to main. Because all three sites use the same shared templates, their workflows differ only in values and secrets.

The Actions tab then shows every deployment per workflow, which branch went where, and each step's full log.

## What did they learn?

GitHub Actions is flexible, and when an integration is missing you can use a community action, as they did for Vercel, or publish your own. And code reuse in templates matters: without shared workflows, each of the three Vercel sites would have duplicated the build and deploy code, and every later change would have had to be made three times. Still on his list: build once and share the artifact with later jobs instead of rebuilding.

## Who should watch

Anyone with a monorepo whose pipeline deploys everything on every commit, and teams deploying to more than one platform from GitHub. The repository is public at [Sitecore/XM-Cloud-Introduction](https://github.com/Sitecore/XM-Cloud-Introduction). Pair it with [Ranjan Mohan on managing GitHub Actions across multiple projects](https://www.conf42.com/DevSecOps_2022_Ranjan_Mohan_setting_up_managing_github_actions_multiple_projects), [Chris Ayers on CI/CD with GitHub Actions](https://www.conf42.com/DevSecOps_2022_Chris_Ayers_cicd_github_actions) and [Kenneth DuMez on removing static shared secrets from GitHub Actions](https://www.conf42.com/DevOps_2023_Kenneth_DuMez_static_shared_secrets_github_actions).

[Watch Rob Earlam's talk](https://www.conf42.com/Cloud_Native_2023_Rob_Earlam_multicloud_deployments_github_actions)

## From Sitecore

- [Sitecore developer portal](https://developers.sitecore.com/?utm_source=conference&utm_medium=presentation&utm_campaign=Conf42_CloudNative): docs and resources for building on Sitecore, including XM Cloud.

[Watch the talk on YouTube](https://youtu.be/f4xCMCPI8yg).

## Watch the talk

[Multi-Cloud Deployments with GitHub Actions](https://www.conf42.com/Cloud_Native_2023_Rob_Earlam_multicloud_deployments_github_actions) at Conf42 Cloud Native 2023.
