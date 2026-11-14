# A digital PMO makes Jira the record and Confluence the memory

Conf42 Blog, 2026-05-19, updated 2026-11-09. https://www.conf42.com/blog/golang2026/digital-pmo-jira-confluence-walmart

In short: George Job of Walmart at Conf42 Golang 2026 on a Jira and Confluence PMO framework that replaced spreadsheet status reporting with live governance.

Status spreadsheets are where portfolio truth goes to get stale. At Conf42 Golang 2026, George Job, Principal Technical Program Manager at Walmart, presented a digital PMO framework that turns Jira and Confluence into one system of record from strategy to delivery, and reported what happened when an Automotive Care Center portfolio adopted it.

A scope note before you press play: this is a program management talk with no Go in it. It fits the conference as a governance story for engineering organisations, and it is most useful to the TPMs and engineering managers who live in those tools.

## What the traditional PMO costs

George's list of problems will be familiar to anyone who has assembled a Monday status deck. Status is tracked in spreadsheets and disconnected tools, so there is no single source of truth. Cross-team dependencies are discovered late, when mitigating them hits the timeline or the budget. Governance varies team by team.

The cost shows up in three places. Leadership makes reactive decisions because it lacks real-time data. Stakeholders work from stale reports, which erodes trust in program management. And TPMs spend their time assembling status by hand instead of managing risk and driving outcomes.

## Three layers in one system

The framework stacks a strategic layer (themes, initiatives and OKRs anchored to business outcomes), a delivery layer (epics plus delivery telemetry giving live progress and health signals), and a governance layer (risk signals and executive reporting that surface issues to leadership in time).

The division of labour between the two Atlassian tools is the practical core. Jira is execution intelligence: structured workflows, standardised custom fields so teams mean the same thing, and dashboards that update without anyone stitching data together. Confluence is living documentation fed by those Jira updates: program charter templates with owners, OKR alignment and RACI, risk and decision logs that form an auditable trail, and executive status pages built from live Jira data. The space hierarchy mirrors the portfolio structure so people can actually find things.

## Gates, conventions and a definition of done

George's workflow advice is about discipline at the edges. Gate intake so every requirement enters through one door, which stops scope creep before it reaches the portfolio. Agree on status conventions across teams so the model scales to the whole organisation. Define exit criteria and a definition of done, so finished means the same thing everywhere.

With one real-time record in place, automation follows: thresholds that raise risk signals when projects are at risk, blocked or stuck in discovery too long, dependency heat maps built from Jira components, and JQL queries embedded in Confluence so reports refresh themselves. It is the rare governance story where the paperwork writes itself, because the paperwork is a query.

## The results, and how he frames them

The abstract describes a portfolio of more than 20 cross-functional teams and around 50 initiatives per quarter, with a 30 percent reduction in PMO operational effort within six months and another 30 percent by twelve months. In the talk, George adds that the portfolio began with eight TPMs and finished the year with three, while keeping the same delivery velocity and quality. He is explicit that the point was not headcount: the effort moved from manual, ad hoc status work to strategic and tactical work.

His summary fits on a sticky note: unify your tooling, standardise before you scale, and make governance continuous.

## Who should watch

TPMs, PMO leads and engineering managers running multi-team portfolios on Jira and Confluence. Engineers looking for Go content can skip it, though anyone who has been asked to fill in a status spreadsheet might enjoy seeing it retired.

## Related Conf42 talks

- [Gobinath Kasimayan on SAP governance and agility](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility) at Conf42 Incident Management 2025
- [Jhonnatan Gil Chaves on agile efficiency with Git](https://www.conf42.com/DevOps_2024_Jhonnatan_Gil_Chaves_agile_efficiency_git) at Conf42 DevOps 2024

[Watch George Job's talk](https://www.conf42.com/Golang_2026_George_Job_digital_pmos_retail)

[Watch the talk on YouTube](https://youtu.be/Y08DRly0XTk).

## Watch the talk

[Digital PMOs in Retail with Jira and Confluence: Governance Through Transparency](https://www.conf42.com/Golang_2026_George_Job_digital_pmos_retail) at Conf42 Golang 2026.
