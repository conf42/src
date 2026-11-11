# Ten thousand findings at release, or one or two per commit?

Conf42 Blog, 2022-12-02. https://www.conf42.com/blog/devsecops2022/ten-thousand-findings-or-one-per-commit

In short: Stefania Chaplin (GitLab) at Conf42 DevSecOps 2022 on moving security scans into the developer's merge request, with culture first and tools second

Stefania Chaplin, Solutions Architect at GitLab and a former Python developer, spent her Conf42 DevSecOps 2022 talk on one choice: find 10,000 vulnerabilities at the end of the lifecycle, when you're already late and over budget, or let each developer fix one or two at the commit that introduced them. Her answer is the second, and she spends as much time on people and process as on scanners.

This is an overview talk with a GitLab workflow as the worked example, not a hands-on demo. If your team is arguing about where security scans belong, it gives you the vocabulary.

## Why start with people and process?

She frames DevSecOps as a Venn diagram. People plus process lets you scale (her example: McDonald's serves roughly the same thing everywhere). People plus technology lets you innovate. Process plus technology lets you automate. Missing one shows up as a symptom: not fast enough means you are not automating, not scaling means the process isn't standardised, scaling without value means innovation is missing.

Culture comes first. Stefania Chaplin said at Conf42 DevSecOps 2022: "You could buy all the tools and all the platforms in the world." If teams still work in silos, the new platform inherits the old problems, plus the burnout and the unplanned firefighting. She recommends Gene Kim's The Phoenix Project and The Unicorn Project, where the protagonist spends a good part of the book just trying to get a build to run.

## What does shifting left actually change?

The cost argument uses the familiar NIST curve: a flaw found during requirements or threat modelling is cheap, one found in testing is still fixable, one found in production is expensive and already exposed.

She is just as clear about what shift left must not mean. Don't make developers run scans outside their normal workflow, and don't expect them to know which tools to run, when, and how to read the output. Security and development use different words and priorities; dumping a tool on developers without translation widens the gap.

## The old loop and the new one

The old workflow: commit, CI, merge, deploy to a test environment, run dynamic testing, then the security team hands over a list and tickets go back to development. Security is an afterthought.

The newer one moves the scans into the merge request. A developer opens an issue, creates a feature branch, and the pipeline runs static analysis, dependency (software composition) analysis, licence scanning, secret detection and unit tests. An ephemeral review app even lets them run dynamic application security testing from their own branch. They see the results, fix or dismiss them, and only then merge. The CD pipeline runs more scans and everything lands on a security dashboard the security team can watch.

The maths is on the developers' side: there are many more of them than security people. She put it this way: "If we could make every developer 1% better in security all of a sudden that would be a massive improvement."

## What about compliance and the security team?

Security gets consistency, earlier visibility, and a dashboard showing who is working on which finding, rather than a stack of reports. Her memory of the old way: security printed a long report, developers read the first few false positives, and the pile went in the bin. For compliance she covers defining the controls you need, exporting audit reports instead of stitching together output from several tools, and keeping audit events so you can trace what a bad actor did during an incident.

The GitLab part: security scanners configured in the CI YAML file, picked per application (SAST, DAST, SCA, secret detection), with stricter policies for tier one apps than internal ones, and existing scanners plugged in rather than thrown out.

## Who should watch

Engineering managers and AppSec leads making the case for scanning in merge requests, and developers who want to hear a former developer argue for fewer tools and less context switching. Pair it with [Tanya Janca on DAST in CI/CD](https://www.conf42.com/DevSecOps_2022_Tanya_Janca_dast_cicd), [Roman Zhukov on fitting security into DevOps](https://www.conf42.com/DevSecOps_2022_Roman_Zhukov_fit_sec_into_devops_security_team) and [Christopher Harrison on changing culture, not just tools](https://www.conf42.com/DevOps_2023_Christopher_Harrison_change_culture__not_just_tools).

[Watch Stefania Chaplin's talk](https://www.conf42.com/DevSecOps_2022_Stefania_Chaplin_people_processes_technologies)

## From GitLab

- [GitLab](https://about.gitlab.com/): the DevSecOps platform used as the example workflow in the talk.

[Watch the talk on YouTube](https://youtu.be/ir0qo9mdiuw).

## Watch the talk

[Implementing True DevSecOps with People, Processes, and Technologies](https://www.conf42.com/DevSecOps_2022_Stefania_Chaplin_people_processes_technologies) at Conf42 DevSecOps 2022.
