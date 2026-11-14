# Four levels of Azure automation, and the secret each one leaks

Conf42 Blog, 2026-04-18. https://www.conf42.com/blog/cloud2026/secure-powershell-cloud-automation-in-azure

In short: Leo Visser of OGD ICT-diensten at Conf42 Cloud Native 2026 demos PowerShell automation on Azure, from VM scripts to Functions behind API Management.

Every step up the Azure automation ladder makes your script easier to run and gives you a new secret to lose. At Conf42 Cloud Native 2026, [Leo Visser](https://www.conf42.com/Cloud_Native_2026_Leo_Visser_cloudarchitecture_infra_design), a consultant at OGD ICT-diensten in the Netherlands and Azure MVP for PowerShell, demoed the same small automation four ways, a scheduled script, an Automation runbook, an Azure Function and a Function behind API Management, and showed how to lock down each one.

It's a hands-on demo talk in the Azure portal and VS Code. The examples are Azure and PowerShell, but he notes most of it has equivalents on AWS and GCP.

## Why automate in the cloud at all

Visser's case is practical. Automation lets you shift tasks left: something that needed a high-privilege sysadmin can be wrapped so a service desk colleague with fewer rights can run it. In the cloud you pay per run instead of keeping compute sized for peak load, and it is easy to connect ticketing, monitoring and security systems.

## Level one: a script on a VM, made stateless

The first demo is a PowerShell script that reads the last hour of entries from a Storage table. Two improvements before anything fancy. Give the VM a managed identity and the script authenticates as that identity with a one-word change, no stored credentials. And fix the silent failure mode: if the job fails once and succeeds an hour later, a query for the last hour has skipped a whole hour of data.

His fix is a watermark. The script reads the last successful check date from Azure Key Vault, queries everything since then, and only writes a new value after success. He takes the new timestamp right after the query, not at the end of a long script, so entries added mid-run aren't skipped. Telemetry goes to Application Insights through the PowerShell module Telemetry Helper, which gives traces, alerts and run durations almost for free. With state in Key Vault, the script no longer cares which machine runs it.

## Level two: Automation runbooks and the webhook token

An Azure Automation account runs PowerShell or Python runbooks on shared infrastructure with managed identities and built-in logs kept for 90 days. Runbooks can be started by a webhook, which is handy for ticketing systems like TopDesk that trigger automation on a button press. The catch is that the webhook URL contains a token, a secret in the URL. Move it into Key Vault so it's out of your code and source control, and remember that arguments travel over the internet unless you add network integration for sensitive data.

## Level three: Azure Functions and rotatable keys

Azure Functions on the consumption tier start almost instantly, have live log streaming and send logs to Application Insights. Authentication is by function key, which works like an API key. You can issue different keys to different callers and revoke or renew one if it leaks. Better than one shared token, but still not a user identity.

## Level four: API Management in front

For user-level authentication, he puts API Management in front of the Function. The function key is stored inside APIM, and a validate-jwt policy on all operations rejects calls without a valid JWT. The demo hit a fun snag: the first call without a token still succeeded because headers were cached in his PowerShell session. After clearing them, the call returned unauthorised as intended. Tokens can then come from a service principal or user sign-in.

## Not every script needs level four

His closing advice is proportionality. A script on a management VM can be fine for something you run rarely. What makes automation resilient is combining the building blocks (managed identity, Key Vault, Application Insights, API Management) where the risk justifies it. His long-term goal, he admits, is a holiday while his automation keeps working.

## Who should watch

Ops engineers and Azure admins who write PowerShell to manage their platform and suspect some of those scripts have tokens in them. If you've ever pasted a webhook URL into a ticketing system, start here.

## Related Conf42 talks

- [The Secret to Handling Dynamic Secrets](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security) by Rosemary Wang at Conf42 Cloud Native 2025.
- [What if you could deploy Azure end-to-end scenarios while sleeping?](https://www.conf42.com/AI_Agents_2026_Peter_De_Tender_azure_deployment_automation) by Peter De Tender at Conf42 AI Agents 2026.
- [Why you should never use static shared secrets in GitHub Actions](https://www.conf42.com/DevOps_2023_Kenneth_DuMez_static_shared_secrets_github_actions) by Kenneth DuMez at Conf42 DevOps 2023.

[Watch Leo Visser's talk](https://www.conf42.com/Cloud_Native_2026_Leo_Visser_cloudarchitecture_infra_design) or the [YouTube recording](https://youtu.be/k6p-V-2asDQ).

## Watch the talk

[Secure your cloud automation](https://www.conf42.com/Cloud_Native_2026_Leo_Visser_cloudarchitecture_infra_design) at Conf42 Cloud Native 2026.
