# Automate the toil, then climb from scripts to automation you only see as a metric

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/automation-ladder-from-scripts-to-metrics

In short: Mandi Walls (PagerDuty) at Conf42 Site Reliability Engineering 2021 on what makes good automation, idempotency, and a maturity ladder for reducing toil

Toil is like brushing your teeth: skip a day and nobody notices, skip it for a month and people start worrying about you. Mandi Walls, DevOps Advocate at [PagerDuty](https://www.pagerduty.com/), opens her Conf42 Site Reliability Engineering 2021 talk with that comparison and then turns automation from a vague good intention into something you can plan: what toil is, what good automation needs, how to pick what to automate first, and how a team's trust in its automation grows over time. Rundeck shows up at the end as the example platform.

## What is toil, and why automate it?

Her definition: repetitive, tactical work that grows linearly with the size of the environment. Deploying software everywhere, adding accounts on every system, scaling environments, testing backups (if you ever do). Even in fully modern systems, rebuilding short-lived environments by hand becomes a new kind of toil. It adds no value in the moment, but neglect it and you get a security breach or degraded performance later.

The drivers are complexity, speed, fewer mistakes and less toil. Manual steps mean typing in the wrong terminal, dropping an option from a long command, or skipping a step while pasting from a wiki. And with auto scaling, any hard-coded list of instances is out of date before you finish writing it, so query an API instead.

## Will automation take my job?

She tackles two myths. The first is automating yourself out of a job. Mandi Walls said at Conf42 Site Reliability Engineering 2021: "you're really automating yourself into a new job." What is left is the creative and strategic work: better disaster recovery plans, more features for users.

The second is that nobody needs to know anything once it is all automated. Research suggests fully automated environments can hinder skill development for junior engineers, and somebody has to understand the system deeply to automate it well. Mandi Walls said at Conf42 Site Reliability Engineering 2021: "Maintaining the automation tools for a service is part of maintaining that service itself." Updating the start-stop script or the new log location is how new team members learn the service.

## What does good automation look like?

She borrows a requirements list from Lee Atchison's book Architecting for Scale:

- **Testable**, ideally with TDD-style tests for the automation code.
- **Flexible**: variables, version numbers and API queries instead of hard-coded lists.
- **In version control with code review**, not a directory of script.sh_back files.
- **Consistent** across related systems, with official libraries for common components made the easiest path.
- **Repeatable and auditable**: predictable results and a record of who ran what.

Then idempotency, the property that running something twice changes nothing after the first run. What happens when the user already exists, the logs are already rotated, the package is already installed, or the config line is appended again? There is no human reading the output, so the automation has to check state first and report success when the work is already done rather than failing. She still has nightmares about a 2001 version of Mandrake Linux whose log rotation created empty files.

## What should you automate first?

Two XKCD cartoons frame it: the one where automating a task turns into maintaining the automation, and the chart of how long you can spend automating before it stops paying back. Start with tasks you do most often or that take longest. Then plot incident-response tasks by impact and complexity. Simple, no-impact tasks such as gathering logs are where a team builds confidence; restarting services is higher impact; firewall changes and rollbacks are the top.

## How does trust in automation grow?

Her maturity ladder is the most reusable part of the talk:

1. **Automation opportunities**: still manual, but identified.
2. **Human-initiated automation**: scripts people run on demand.
3. **Automation with oversight**: triggered by the environment, such as cron or restarting a service that stops answering, with a notification so humans can check.
4. **Automation with fallback**: runs alone and escalates only when it hits an error or an edge case.
5. **Monitor and evaluate**: the work produces a metric, task X completed N times this week, instead of tickets.

Not every task reaches the top, and complex ones may stop at fallback. That is fine.

## Where does Rundeck fit?

Rundeck is the automation platform she uses as the example. Subject matter experts encode the right way to restart or patch something, and other teams run it themselves with the proper permissions, without touching the nodes. Instead of a ticket asking the SRE team to rebuild a dev environment, the requester runs the job, reads the green or red output, and auditors get a log of who did what. Combined with PagerDuty it can auto-remediate issues before they become incidents.

## Who should watch

SRE and platform teams buried in requests, and teams nervous about automation. The maturity ladder is worth stealing for planning.

## Related Conf42 talks

- Mandi Walls brought [her automation and toil talk](https://www.conf42.com/DevOps_2024_Mandi_Walls_improve_automation_reduce_toil) to Conf42 DevOps 2024.
- Dylan Etkin on [why you shouldn't toil but automate](https://www.conf42.com/DevOps_2024_Dylan_Etkin_dont_toil_automate) at Conf42 DevOps 2024.
- Joshua Arvin Lat and Sophie Soliven on [incident automation strategies](https://www.conf42.com/Incident_Management_2023_Joshua_Arvin_Lat_Sophie_Soliven_automation_strategies) at Conf42 Incident Management 2023.

[Watch Mandi Walls's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Mandi_Walls_automation_toil)

## From PagerDuty

PagerDuty runs incident response and on-call alerting, and pairs with Rundeck for runbook automation and auto-remediation.

- [PagerDuty website](https://www.pagerduty.com/)

[Watch the talk on YouTube](https://youtu.be/WgE0V65RL6k).

## Watch the talk

[Improve Your Automation to Reduce Toil](https://www.conf42.com/Site_Reliability_Engineering_2021_Mandi_Walls_automation_toil) at Conf42 Site Reliability Engineering 2021.
