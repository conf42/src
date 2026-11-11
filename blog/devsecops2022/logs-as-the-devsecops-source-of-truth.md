# You can't SSH into a container that died an hour ago

Conf42 Blog, 2022-12-01. https://www.conf42.com/blog/devsecops2022/logs-as-the-devsecops-source-of-truth

In short: Arfan Sharif (CrowdStrike) at Conf42 DevSecOps 2022 on centralised log management as the shared source of truth for dev, ops and security teams

Arfan Sharif, Lead Technical Marketing Engineer on CrowdStrike's Falcon LogScale team, argued at Conf42 DevSecOps 2022 that centralised logs are what lets developers, IT engineers and security engineers look at the same facts. His case rests on a simple observation about cloud native systems: the thing you need to debug is often gone before you start, so the logs have to be somewhere else already.

It's a fundamentals talk, and it says so up front: what DevSecOps is, what log management is, which log sources matter, and a short list of practices. Good for a team writing its first logging policy; seasoned SIEM people will recognise most of it.

## Why does cloud native make logging harder?

The usual move used to be logging into a server and grepping a file. Containers break that on three counts. They write to standard output rather than files, Kubernetes moves them between hosts as demand shifts, and an average container lives a short time. Arfan Sharif said at Conf42 DevSecOps 2022: "On top of that, you don't have the practice to SSH in and tail and grep the logs to troubleshoot." So the logs need to be captured and shipped to a central store while the container is still alive, or the evidence for the next incident leaves with it.

Mobile devices are the extreme case: little disk, flaky network, no easy way to read system logs on iOS or Android, so you cannot assume logs reach a central place in real time.

## What does log management actually buy a DevSecOps team?

He walks through five uses. Monitoring and troubleshooting, the classic one, where logs plus metrics cut mean time to recovery. Operations, where trends across the infrastructure let you fix things before they catch fire. Resource usage, spotting a node that is close to overload or slow 90th percentile queries. User experience, tracing slow responses down to the API or database level. And security and compliance, where network, system, audit and application logs show anomalies as they happen and, with enough retention, the trail an attacker left behind.

On compliance he is practical: write a logging and monitoring policy that says what to log, where it is stored, how long it is kept and how often someone reviews it.

## Which logs matter?

From the long list of things that emit data, he picks the sources most relevant to DevSecOps: network data (historically Syslog), server and application logs (kernel messages, service status, user logins, NGINX or Tomcat errors and HTTP status codes), container logs and mobile logs. If you write your own application, use structured logging, key-value or JSON, so the pipeline downstream doesn't have to guess.

## Logs as the shared view

The core argument comes near the end. Developers should log security-relevant events while writing code: authorisation failures, even successes, and input validation problems. CI servers, test runs and builds all emit logs that can show anomalous code before deployment, and production logs catch what slips through. During an incident, waiting for someone to manually share sensitive data slows everyone down; if every stakeholder can query the same logs, access stops being the bottleneck.

He put the collaboration point bluntly: "You can't practice devsecops if your developers, IT engineers and security engineers lack shared visibility into the state of each application release." Meetings and Slack threads help, but they do not give everyone the same view; a central log store does.

His best-practice list is short: build security testing into the whole development cycle and let the development team run it, let developers manage and fix what testing finds, automate recurring security tasks, and log every relevant source so DevOps and SecOps have context. A security champion inside each development team, someone with more AppSec training who reviews security fixes, is the cultural half.

## Who should watch

Teams moving workloads to containers who still think of logs as files on a box, and anyone drafting a logging policy who wants a checklist of sources and uses. The product section at the end is brief: Falcon LogScale for ingesting and querying data from the whole estate, and CrowdStrike's cloud security platform.

Related Conf42 talks: [Leonid Yankulin on structured logging in Google Cloud](https://www.conf42.com/DevSecOps_2022_Leonid_Yankulin_structured_logging_google_cloud), [Kenneth DuMez on the Kubernetes audit log](https://www.conf42.com/Cloud_Native_2023_Kenneth_DuMez_kubernetes_audit_log) and [Phil Wilkins on logs with Fluentd](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd).

[Watch Arfan Sharif's talk](https://www.conf42.com/DevSecOps_2022_Arfan_Sharif_log_eat_log_world_crucial_log_management_skills)

## From CrowdStrike

- [CrowdStrike](https://www.crowdstrike.com/): Falcon LogScale, the log management product covered in the talk, and Falcon Cloud Security.

[Watch the talk on YouTube](https://youtu.be/f67kscTQrYY).

## Watch the talk

[It’s a log eat log world. Crucial Log Management Skills for DevSecOps](https://www.conf42.com/DevSecOps_2022_Arfan_Sharif_log_eat_log_world_crucial_log_management_skills) at Conf42 DevSecOps 2022.
