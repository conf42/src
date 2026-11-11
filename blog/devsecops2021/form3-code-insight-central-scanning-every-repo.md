# Form3 moved code scanning out of 500 repos and into one place

Conf42 Blog, 2021-12-01. https://www.conf42.com/blog/devsecops2021/form3-code-insight-central-scanning-every-repo

In short: Adelina Simion and Ross McFarlane (Form3) at Conf42 DevSecOps 2021 on Code Insight, a central GitHub app that scans every PR and every repo nightly

If each repository configures its own security scan, each repository can also quietly switch it off. At Conf42 DevSecOps 2021, Adelina Simion, Technology Evangelist, and Ross McFarlane, Technical Lead for Information Security, both at payments platform Form3, showed Code Insight: the in-house tool that took Form3's scanning config out of 500-plus repos, runs on every pull request and every default branch nightly, and reports back as comments on the offending line.

It is a 15-minute talk with a clear arc: two earlier tools, the requirements they failed, the AWS architecture that replaced them, and an honest list of what did not work.

## Why did Form3 need a third scanner?

Form3 was founded in 2016 and had around 260 employees at the time, about 130 of them engineers, fully remote, with over 500 repositories in Terraform, Go, Java and YAML. Many new engineers were contributing to live services, and some repos were important but no longer under active development.

The first tool was Salus, open sourced by Coinbase, which bundled the analysis tools into one Docker container. It gave consistency but the containers grew to over 1 GB and got sluggish. The replacement, an in-house wrapper called SecScan, was lighter, but each repo wired it up through its own Makefile or Travis YAML and its own token. That meant no enforcement (new repos could skip it), no visibility into which repos were configured or failing, scans only on PRs (so dormant repos were never scanned), and an update rollout that touched every repo. As the slides put it, repositories were marking their own homework.

## How does Code Insight scan a pull request?

Code Insight is a GitHub app installed on every repo. A webhook hits a Lambda behind API Gateway, which fetches the code, tells GitHub that checks are coming, picks the scans from the repo's content and drops a request on a queue. An orchestrator Lambda records the scan; a scheduler Lambda launches it as a task on a serverless Fargate cluster.

The task design is the neat part. The scan container is kept dumb on purpose: one sidecar clones the repo to disk, the scanner reads from disk and writes results to disk, then other containers post GitHub comments, push results to an S3 bucket and signal completion. Adding a new scan means writing a very small container. A notifier sets the final check status on the PR, and output is moving to the SARIF format so comments can land beside the right line.

Default branches are scanned nightly too, with failures sent to the owning team on Slack. "Even the quietest project has its code scanned every 24 hours," Ross McFarlane said at Conf42 DevSecOps 2021.

## What does central config actually buy you?

Switching a scan off now needs a pull request to a central repository that the information security team reviews. Ross's phrase for it is that centralizing the config "keeps the honest people honest". It also closes a real attack path: nobody can add malicious code and disable the check that would catch it in the same PR. The mostly serverless setup follows the daily rhythm of PRs and goes quiet overnight apart from the nightly runs.

## How do you roll it out without breaking every build?

Not on day one. Existing repos started on soft failures that report without blocking, then a ratchet: once a repo passed, enforcement went on and stayed on. New repos got it enforced by default. To get teams to green, Form3 opened batch PRs across repositories for shared issues, ran mob sessions to raise coverage, and tried a team leaderboard.

The leaderboard flopped, and Ross says so. It rewarded teams that write little code and stigmatised those with many repos to manage. "Engineers can just see right through it," he said.

## What went wrong?

Three lessons worth stealing. First, the scanner is production infrastructure: a broken scan can halt the whole company's work, so Form3 added canary releases for new scans, a better test environment and monitoring. Second, big sprawling repos, especially Terraform ones, are hard to get passing; small repos improve incrementally. Third, scanners backed by external vulnerability databases can break many builds overnight when a minor vulnerability is added to one of them. Planned fixes: tell new issues from existing ones, track flaky and slow scans, and hard-fail only on Form3's age and severity remediation policy.

## Who should watch

AppSec and platform engineers running scanning across dozens or hundreds of repos, especially if your current setup lives in per-repo CI files. It is a practical architecture talk with no product pitch beyond Form3's hiring page.

## Related Conf42 talks

- Joseph Hejderup on [adopting static analysis for dependency tools](https://www.conf42.com/DevSecOps_2022_Joseph_Hejderup_going_beyond_metadata_adopting_static_analysis_dependency_tools) at Conf42 DevSecOps 2022.
- Safeer C M on [open-source SAST with Semgrep](https://www.conf42.com/DevSecOps_2025_Safeer_C_M_sast_open_source_semgrep) at Conf42 DevSecOps 2025.
- Peter De Tender on [GitHub code scanning and SAST](https://www.conf42.com/DevSecOps_2026_Peter_De_Tender_github_codescanning_sast) at Conf42 DevSecOps 2026.

[Watch Adelina Simion and Ross McFarlane's talk](https://www.conf42.com/DevSecOps_2021_Adelina_Simion_Ross_McFarlane_custom_Code_Insight_tool_Form3) from [Conf42 DevSecOps 2021](https://www.conf42.com/devsecops2021).

## From Form3

Form3 runs a cloud payment processing platform; the name comes from third-generation cloud technology plus a shortened form of the word platform.

- Form3: [form3.tech](https://www.form3.tech/)
- Form3 engineering site: [engineering.form3.tech](https://engineering.form3.tech/)
- Form3 tech podcast: [techpodcast.form3.tech](https://techpodcast.form3.tech/)
- Careers: [form3.tech/careers](https://www.form3.tech/careers)

[Watch the talk on YouTube](https://youtu.be/UvOdp38QVMs).

## Watch the talk

[Building our own custom Code Insight tool at Form3](https://www.conf42.com/DevSecOps_2021_Adelina_Simion_Ross_McFarlane_custom_Code_Insight_tool_Form3) at Conf42 DevSecOps 2021.
