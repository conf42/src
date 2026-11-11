# The cheapest secret leak is the commit that never happened

Conf42 Blog, 2022-11-30. https://www.conf42.com/blog/devsecops2022/pre-commit-hooks-stop-hardcoded-secrets

In short: Dwayne McDaniel (GitGuardian) at Conf42 DevSecOps 2022 on using Git pre-commit and pre-receive hooks to stop hard-coded secrets before they are pushed

By the time GitHub scans your push for secrets, the secret is already on GitHub. Dwayne McDaniel, Developer Advocate at GitGuardian, made the case at Conf42 DevSecOps 2022 that the only reliable fix is to stop the commit on the developer's machine, and that Git already ships the mechanism: hooks. It's a short, practical talk that ends with three tools you can install the same afternoon.

## How bad is the hard-coded secret problem?

He opens with four 2022 incidents. Uber: a teenager from the Lapsus$ group phished a super admin's login and immediately found hard-coded credentials in PowerShell scripts. Toyota: a subcontractor pushed T-Connect source code to a public GitHub repository, exposing a data server credential and the emails of 296,019 customers; it stayed public from December 2017 to September 2022. Samsung: 160 GB stolen, including Galaxy source code with more than 6,000 secrets in it. AstraZeneca: credentials pushed to GitHub in 2021 gave access to a test environment that, through user error, held patient data, and stayed exposed for over a year.

Then the numbers from GitGuardian's State of Secrets Sprawl 2022 report: 6 million secrets found in public GitHub repositories in 2021, more than double the 2 million of 2020, and on average 3 commits in 1,000 exposing at least one secret.

## Why can't the security team just catch it?

They are outnumbered. He cites Alex Rice of HackerOne: in the best organisations, developers outnumber security staff 100 to 1. So the control has to sit with developers, inside a tool they already use every day, and that is Git.

The honest part of the talk: developers hard-code secrets for good reasons. You need to know whether the API endpoint is up and the key works, so you paste it in, meaning to take it out. .gitignore, a local secrets file and a vault (he names HashiCorp Vault and Azure Key Vault without plugging either) solve it in a perfect world. In ours, someone forgets, and cleaning a pushed secret out of every branch, rotating the key and explaining it to the team is painful. Dwayne McDaniel said at Conf42 DevSecOps 2022: "What we need is a robot." A robot that stops the commit every time.

## Git hooks are that robot

Git hooks fire your script when Git does something, and he calls them wildly underused. There are 17 of them (githooks.com lists them all); two matter here. A pre-commit hook on the developer's machine refuses the commit. A pre-receive hook on the server refuses the push, so the remote's owner can block a secret even if a laptop has no hook installed. Hooks are just scripts, in any language you like; his own personal projects print a dad joke on every commit.

You can build the secret check yourself with git grep and regular expressions: an AWS access key is 20 characters of capital letters and digits, and a plain password equals pattern catches the lazy cases. The catch is that you then own the patterns, the false positives, the allow list, and the job of getting the whole team to install it.

## Which off-the-shelf tools?

His three open source picks:

- **git-secrets from AWS Labs**: checks commits for AWS-shaped secrets before they land. Extensible, but other clouds such as Google Cloud or Azure DevOps mean writing their patterns in regex yourself.
- **TruffleHog**: best known for its GitHub Action; the pre-commit integration requires the pre-commit framework. He notes reports of high false positives and says plainly he hasn't run it in production.
- **ggshield from GitGuardian**: works as a pre-commit, pre-push and pre-receive hook, needs a GitGuardian account, and checks against 350 known patterns, extensible with regex.

All three behave the same in practice: commit a YAML file with a secret in it and the hook fails the commit. Of the three, he found only the pre-commit framework setup a little tricky.

His summary is three lines long: don't hard-code secrets; if you do, don't commit them; and use automation so you don't have to remember.

## Who should watch

Developers who have ever pasted an API key just to test it, and platform teams deciding whether to enforce secret scanning at the server with pre-receive hooks. It's 20 minutes and very easy to act on. Related: [Daniel Oates-Lee on secrets in Git repositories](https://www.conf42.com/DevSecOps_2023_Daniel_OatesLee_git_secrets_repos), [Dewan Ahmed on securing repositories with Gitleaks](https://www.conf42.com/DevSecOps_2024_Dewan_Ahmed_securing_gitleaks_repos_secret) and Dwayne McDaniel's follow-up on [detecting intruders with honeytokens](https://www.conf42.com/DevSecOps_2023_Dwayne_McDaniel_detecting_honeytokens).

[Watch Dwayne McDaniel's talk](https://www.conf42.com/DevSecOps_2022_Dwayne_McDaniel_stop_committing_your_secrets_git_hooks)

## From GitGuardian

- [GitGuardian](https://www.gitguardian.com/): secrets detection and remediation, including the ggshield CLI shown in the talk.

[Watch the talk on YouTube](https://youtu.be/PmZdsGJdKXg).

## Watch the talk

[Stop Committing Your Secrets - Git Hooks To The Rescue!](https://www.conf42.com/DevSecOps_2022_Dwayne_McDaniel_stop_committing_your_secrets_git_hooks) at Conf42 DevSecOps 2022.
