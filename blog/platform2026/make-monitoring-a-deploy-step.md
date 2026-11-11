# Monitoring belongs in the deploy, not in someone's memory

Conf42 Blog, 2026-10-28, updated 2026-11-09. https://www.conf42.com/blog/platform2026/make-monitoring-a-deploy-step

In short: Eleftheria Batsou (UptimeRobot) at Conf42 Platform Engineering 2026 on creating monitors from the pipeline with a CLI, and what still needs a human.

Platform teams automated the repo template, the pipeline, the secrets, the infrastructure and the dashboards, and then left monitoring to a human with a web form, later, if anyone remembers. At Conf42 Platform Engineering 2026, Eleftheria Batsou, Developer Advocate at UptimeRobot, gave a lightning talk on closing that gap by making monitor creation a deploy step from the command line.

Scope note: the examples use UptimeRobot's own open-source CLI, because that's what she works on. The argument, about where monitoring sits in the workflow, applies to any tool.

## One root cause, three symptoms

Eleftheria names the failure modes precisely. No monitor at all, so the first alert is a customer support ticket. The wrong monitor: it checks the marketing homepage instead of the health endpoint, or pages someone who left last spring, and stays green while telling you nothing. And orphaned monitors for renamed or retired services, alerting on nothing or quietly checking a URL that now belongs to something else.

Every monitoring tool can hit an HTTP endpoint, so this isn't a tooling gap. Monitoring sits outside the golden path, so it runs on discipline rather than defaults, and discipline doesn't scale: 50 new services a year means 50 separate acts of remembering. Her fix is one default: build, test, deploy, register the monitor, confirm the service reports up. The pipeline already knows the service name, URL, owning team and environment, the exact fields someone would otherwise copy into a form.

## Dry-run in the pull request

The CLI installs from npm, stores your key in the OS keychain locally, and reads it from an environment variable in CI. Creating a monitor is one command with type, name, URL, interval and timeout. Her favourite feature is `--dry-run`: it validates the request and prints the exact POST it would send, without credentials or network. That means a service's monitoring config can be checked in a PR the way you'd lint a Dockerfile. Leave out the timeout and it exits with code 2 and names the missing field.

Then the platform team gets opinionated. Template what's decided once: interval per tier, timeout, HTTP method, success codes, SSL and domain expiry reminders, tag conventions, alert-contact mapping. Take from service metadata what genuinely varies: name and environment, health endpoint, owning team, tier, a job's schedule. If you're copying the same value into every service, it belongs in the template.

## The details that bite on the first run

This part is the most practical in the talk:

- **No upsert.** The CLI retries reads but never POST, PATCH or DELETE. Call create on every deploy and you get a duplicate monitor every deploy. Look up first, create if missing, otherwise update; the name filter is a partial match, so compare exact names yourself and use something predictable like service plus environment.
- **Keys.** Creating monitors needs the main API key. A read-only key gets a 403 and exit code 5.
- **Flags and plans.** Interval and timeout are both required and everyone forgets timeout. The free plan's minimum interval is five minutes, so a template that hard-codes 30 seconds fails for every team.
- **HEAD by default.** Without a method, HTTP monitors send HEAD, which some frameworks route differently from GET. Pass GET explicitly.

Exit codes are distinct (2 invalid input, 4 and 5 auth, 7 rate limit, 8 conflict) and errors arrive as JSON on stderr. Her policy: fail the deploy on config errors, since they mean shipping unmonitored, but don't block a release because a third-party API is briefly rate-limiting you. For cron jobs and queue workers with no URL, flip direction with a heartbeat monitor the job calls on completion; the CLI redacts that URL by default because it's effectively a secret.

## Where a CLI is the wrong tool

Eleftheria is upfront about it. For whole-fleet desired state with drift detection, use a declarative tool. For AI agents investigating incidents, an MCP server beats shelling out. At 3am, a human in the dashboard wins. Whatever you choose, keep one source of truth per monitor; pipelines that create monitors people then edit by hand are a drift factory. And some monitoring can't be templated at all: which third-party services you depend on, journeys that cross services, who gets woken up, and response-time thresholds for a service with no traffic yet. Those stay human decisions, made consciously.

## Who should watch

Platform teams with a golden path that stops at deploy. It's short, concrete and directly copyable, with CLI specifics you can skip if you use something else.

## Related Conf42 talks

- [Observability Starts Before the Outage: Synthetic Monitoring for Modern Systems](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage) by Palak Bhawsar (Telstra)
- [Go global or go home! Monitoring your platform from multiple locations](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrei_Danilov_go_global_monitoring_platform_multiple_locations) by Andrei Danilov
- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) by Mandi Walls (PagerDuty)

[Watch Eleftheria's talk](https://www.conf42.com/Platform_Engineering_2026_Eleftheria_Batsou_monitoring_automated_nobody)

[Watch the talk on YouTube](https://youtu.be/0ZAasoB9Zjw).

## Watch the talk

[Monitoring is still the one thing nobody automated](https://www.conf42.com/Platform_Engineering_2026_Eleftheria_Batsou_monitoring_automated_nobody) at Conf42 Platform Engineering 2026.
