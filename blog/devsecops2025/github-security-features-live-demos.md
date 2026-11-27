# GitHub ships most of a DevSecOps toolchain in the Security tab

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/github-security-features-live-demos

In short: Peter De Tender of Microsoft at Conf42 DevSecOps 2025 demos GitHub rulesets, secret scanning with push protection, Dependabot and CodeQL in VS Code.

Before you buy another scanner, check what is already sitting in your repository settings. At Conf42 DevSecOps 2025, [Peter De Tender](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql), lead technical trainer at Microsoft, gave a demo-heavy tour of GitHub's built-in security: repository best practices, secret scanning with push protection, Dependabot for vulnerable dependencies and CodeQL for code scanning, including running CodeQL on your own workstation.

It's an introductory talk and says so, built from live demos on public sample repos you can inspect afterwards. By his own account at the end, every demo worked, which in a live security demo is a minor miracle.

## Start with the repo you already have

De Tender begins with hygiene. Decide who collaborates versus who merely contributes to a public repo (not the same thing), limit who can do code reviews, and protect the main branch. GitHub nags when a branch is unprotected, and his advice is to protect both the default branch and branches matching a pattern such as main, since the default can be changed. He admits that after years on Azure DevOps he still calls rulesets branch policies.

Rulesets restrict deletions and block force pushes by default. He usually also restricts branch creation and requires code scanning and code quality results; with GitHub Copilot you can request an automatic AI code review too. Secrets used by Actions belong in encrypted repository secrets rather than plain variables, and a SECURITY.md file gives every visitor a visible link to your security policy.

## Secret scanning, then stop secrets before the push

Secret scanning checks repositories against a long list of known secret formats from partner platforms: AWS and Azure keys, API keys, connection strings, SSH keys. He commits a GitHub personal access token through the web editor and gets blocked with options: mark it as a false positive, as used in tests, or "I'll fix it later". He's not a fan of the last one, since it lets the secret land in the repo anyway.

Push protection moves the check earlier. He pastes the same token into a file in VS Code, tries to sync, and the push is rejected because it contains a secret. If it never reaches the repo, there's nothing to scan for.

## Dependabot reads the CVE feed so you don't have to

Dependabot works on public and private repos, using the public CVE database plus the GitHub Advisory Database. Enabling alerts also enables the dependency graph, and you can add custom rules, security updates as pull requests and version updates. On his pre-scanned demo repo it flagged a command injection issue in lodash with attack vector, complexity, severity, the CVE ID and a suggested package upgrade. The dependency graph can also export an SBOM as a detailed JSON file.

## CodeQL treats your code as data

CodeQL builds a database from your code and runs queries against it, from GitHub's research team, the community or your own. Enabling code scanning generates a GitHub Actions workflow under .github/workflows that you can edit: change triggers, run it on a schedule or fold it into your build pipeline. He also points out the permission settings in that workflow, so the scanning job can read but not change code.

The bit worth the watch is shifting it further left. With the CodeQL extension for VS Code, or the CLI, developers run the same queries locally before merging. His example query hunts for the token from the secret-scanning demo; out of the CodeQL database it was flagged by 115 different prebuilt C# queries. Secrets are just the relatable example, he notes, since CodeQL can query for far more.

## Who should watch

Teams already on GitHub who haven't switched these features on, and anyone setting a baseline for repository security. Experienced AppSec engineers will know the features but may pick up the local CodeQL workflow.

## Related Conf42 talks

- [DevSecOps beyond GitHub Advanced Security](https://www.conf42.com/DevSecOps_2026_Peter_De_Tender_github_codescanning_sast) is De Tender's follow-up on what to add beyond the built-ins.
- [Why you should never use static shared secrets in GitHub Actions](https://www.conf42.com/DevOps_2023_Kenneth_DuMez_static_shared_secrets_github_actions) tackles the pipeline secrets problem head on.
- [Open-source vulnerability management? Use the source, Luke!](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source) asks what dependency alerts miss.

[Watch Peter De Tender's talk](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql)

[Watch the talk on YouTube](https://youtu.be/PHmnkhLZWj0).

## Watch the talk

[A lap around GitHub Dependabot, CodeQL and other built-in security features](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql) at Conf42 DevSecOps 2025.
