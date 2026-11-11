# GitHub security from A to Z, well past the three GHAS features

Conf42 Blog, 2026-09-28, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/github-security-a-to-z-beyond-ghas

In short: At Conf42 DevSecOps 2026, Microsoft's Peter De Tender walks the alphabet of GitHub security, with CodeQL, Dependabot and push protection demos.

GitHub Advanced Security is three features, and the alphabet has twenty-six letters. That is the premise of Peter De Tender's talk at Conf42 DevSecOps 2026: the Senior Content Developer at Microsoft in Redmond takes the GHAS bundle as a starting point and walks A to Z through the rest of the GitHub settings that make up a DevSecOps posture, with live demos of the big three along the way. It is a Microsoft speaker showing GitHub, so expect the product front and centre.

## The three pieces you may already pay for

De Tender starts by unpacking the bundle. Secret scanning matches tokens from around 70 partner providers, and push protection can block the commit before it leaves your laptop. Code scanning uses CodeQL, which treats source code as data you can query. Dependabot flags vulnerable packages from the CVE database and can now hand fixes to GitHub Copilot to rewrite package files. His useful aside for small teams: a lot of this works on public repos with a personal account, and much of the foundation also exists in Azure DevOps.

## CodeQL from portal to VS Code

The first demo, on a public sample repo, enables code scanning and opens an alert where HTML built from library input could allow cross-site scripting, complete with the CWE link and a suggested fix. He then walks the generated CodeQL Actions workflow: push, pull request and cron triggers, a language matrix for JavaScript and C#, extraction, a .NET build, analysis and a SARIF file.

The part worth watching is the local loop. With the CodeQL CLI you create a database from the repo, and with the VS Code extension you write and run your own queries. His example query flags page models that are handed a logger they never use, and the results land inline on the offending methods.

## Dependabot and dependency review

The Dependabot demo shows alerts with affected versions, fix versions, CVSS details and an EPSS score, plus the cross-check to cve.org where other vendors list the same issue. He then adds a dependency review step to a pull request, deliberately adding a nokogiri version with known vulnerabilities, and the review flags it before merge, along with a license issue. Dependabot finds the problem; dependency review stops it at the PR.

## Push protection in action

The secret scanning demo plants a GitHub personal access token in an app settings file. Turning scanning on surfaces it from history within seconds. With push protection enabled, the next commit attempt is refused, and the developer has to state a reason, false positive, test, or "fix later", to bypass it. That last option, he notes, is not exactly best practice.

## The rest of the alphabet

The A to Z format turns into a checklist you can steal. A few of the letters:

- **B and Q:** branch protection, rulesets and quality gates, so a failing check is a barrier rather than a red badge.
- **E:** environment protection rules with approvals and branch restrictions before production.
- **F:** workflows from forks never automatically get repository secrets.
- **H:** hardening runners, GitHub-hosted or your own.
- **I:** infrastructure-as-code scanning for Terraform, Bicep, ARM and Kubernetes YAML.
- **K and O:** keyless auth via OpenID Connect, swapping short-lived tokens for cloud access instead of stored keys.
- **S:** SBOMs and SAST.
- **V:** vulnerability management, where dismissing an alert should be a documented risk decision, not a way to clean up the dashboard.
- **Z:** Zero Trust, never trust automatically, always verify, assume breach.

It is long, around 45 minutes, and deliberately broad rather than deep; with twenty-six letters some get a sentence each. The payoff is breadth: most teams have at least three of these settings off.

## Who should watch

GitHub org admins and DevSecOps engineers who switched on GHAS and stopped there, and Azure DevOps users wondering what transfers. If you want the mechanics of a single feature, the CodeQL section is the most hands-on.

## Related Conf42 talks

- [Peter De Tender's earlier lap around Dependabot, CodeQL and built-in security](https://www.conf42.com/DevSecOps_2025_Peter_De_Tender_github_dependabot_codeql), the companion piece.
- [Dewan Ahmed on preventing accidental secret commits with Gitleaks](https://www.conf42.com/DevSecOps_2024_Dewan_Ahmed_securing_gitleaks_repos_secret).
- [Gresshma Atluri on proactive supply chain defence](https://www.conf42.com/DevSecOps_2025_Gresshma_Atluri_supply_chain_threats).

[Watch Peter De Tender's talk](https://www.conf42.com/DevSecOps_2026_Peter_De_Tender_github_codescanning_sast)

[Watch the talk on YouTube](https://youtu.be/z772CLcVUqM).

## Watch the talk

[DevSecOps beyond GitHub Advanced Security](https://www.conf42.com/DevSecOps_2026_Peter_De_Tender_github_codescanning_sast) at Conf42 DevSecOps 2026.
