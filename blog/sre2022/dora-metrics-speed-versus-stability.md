# DORA's four metrics are two about speed and two about stability

Conf42 Blog, 2022-06-10. https://www.conf42.com/blog/sre2022/dora-metrics-speed-versus-stability

In short: Cristina Buenahora (Cortex) at Conf42 Site Reliability Engineering 2022 on the four DORA metrics, what drags each one down and how to measure them with tools you have

Shipping more often feels riskier, and the DORA research says the opposite. At Conf42 Site Reliability Engineering 2022, Cristina Buenahora, Founding Engineer at [Cortex](https://www.cortex.io/), walked through the four DORA metrics (lead time for changes, deployment frequency, mean time to recovery and change failure rate), what pushes each into the bad zone, and how to measure them with the Jira, GitHub and pager data a team already has.

It's an introductory talk, and a practical one: every metric gets a list of causes, a list of fixes and a set of questions to measure it by. The numbers come from the Accelerate State of DevOps 2021 report.

## Where do the four metrics come from?

DORA stands for DevOps Research and Assessment, the team that surveyed thousands of development teams across industries to work out what separates high performers from low ones. The four metrics are what came out of it. Cristina's summary at the end is the useful frame: lead time and deployment frequency measure speed, MTTR and change failure rate measure stability.

## Lead time for changes: the giant pull request problem

Lead time is the time from commit to production, though teams can start the clock at ticket-in-sprint or at merge, as long as they pick one. In the 2021 report elite performers had under an hour; low performers six months or more.

The usual culprits: huge changes in one go (the PR with hundreds of files that every reviewer closes again), reviews that sit too long, requirements that change mid-PR, and a CI/CD pipeline that makes releases painful. Her fixes are blunt. Make sure everyone on the team can review PRs. Reject tickets that aren't fleshed out, rather than starting work while design is promised for later. When someone asks for just one more thing, finish the PR you scoped and file a follow-up ticket. To find the bottleneck, split lead time into three buckets: developer working time, PR open and in review, and merged-to-production.

## Deployment frequency: small changes are easier to blame

Elite performers deploy multiple times a day; low performers less than once every six months. The misconception she targets is that more deploys means more incidents. Small changes are easier to understand and easier to pinpoint when something breaks, which also drives MTTR down.

"A high deployment frequency will end up actually reducing your overall risk, even though you are deploying more often," Cristina Buenahora said at Conf42 Site Reliability Engineering 2022.

What holds it back: weak pipelines, only three engineers who know how to deploy (one of them on holiday), lengthy manual testing. For large teams with a monolith, where one PR per deploy isn't realistic, she suggests release trains that ship at fixed intervals through the day. Measure it as releases per sprint and average time between releases.

## Mean time to recovery: don't host your status page next to your outage

Elite performers recover in under an hour. To show why it matters, Cristina uses two 2021 outages. Meta's October 4 outage lasted about five and a half hours after a backbone maintenance command, missed by a buggy audit tool, disconnected its data centres, and losing DNS broke the internal tools engineers needed to diagnose it. She put the cost at over $60 million. Roblox was down for more than three days, about $25 million by her figure, partly because the failure took out the monitoring that would have shown what was wrong.

The lesson she draws from both is a circular dependency: keep your observability stack independent of the system it watches, and don't put your status page on the same DNS as your site. Short MTTR comes from a tight incident process, quick rollback that lots of people know how to do, diagnostic tools and accessible runbooks. Measure outage length, time from fix found to fix released, and time to discover the outage at all.

## Change failure rate: count the rate, not the failures

The 2021 report put elite teams at 0 to 15%. The common mistake is counting failures instead of the rate, which punishes teams that ship often. High rates trace back to sloppy reviews, thin testing and staging environments with unrealistic data. Measure releases that caused downtime, tickets that led to incidents and tickets that spawned follow-up bugs, then ask whether a unit test, an end-to-end test or better staging data would have caught each one.

## Who should watch

Engineering managers and team leads starting to measure delivery, and engineers who want a vocabulary for arguing against the giant PR. If you already run DORA dashboards, the outage stories and the measurement questions are the part worth your time.

For more, see Steve Pereira on [flow engineering and value streams](https://www.conf42.com/DevSecOps_2022_Steve_Pereira_flow_engineering_boost_velocity_quality_happiness_value_stream), Travis Gosselin on [deploy velocity with feature flags](https://www.conf42.com/Site_Reliability_Engineering_2022_Travis_Gosselin_unleashing_deploy_velocity_feature_flags) and Dotan Horovits on [DevOps observability in 2022](https://www.conf42.com/Site_Reliability_Engineering_2022_Dotan_Horovits_devops_observability_in_2022), both from the same event.

[Watch Cristina Buenahora's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Cristina_Buenahora_4_key_metrics_team_performance) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From Cortex

In the talk Cristina shows two Cortex features: the service catalog, as one place to find service owners, runbooks and logs during an incident, and Scorecards, which score every service against rules a team defines (test coverage, for example) and back initiatives such as improving deployment frequency by a set quarter.

- Cortex: [cortex.io](https://www.cortex.io/)
- [Cortex Scorecards](https://www.cortex.io/products/scorecard/?utm_source=conf42)
- [Case study: how Clever standardised service quality across 500+ services](https://www.cortex.io/case-study/clever/?utm_source=conf42)
- [Book a demo](https://www.cortex.io/demo/?utm_source=conf42)

[Watch the talk on YouTube](https://youtu.be/AzUe2PsDXCQ).

## Watch the talk

[Is your team any good? 4 key metrics for measuring your team's performance](https://www.conf42.com/Site_Reliability_Engineering_2022_Cristina_Buenahora_4_key_metrics_team_performance) at Conf42 Site Reliability Engineering 2022.
