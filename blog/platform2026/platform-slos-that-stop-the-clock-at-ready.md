# Platform SLOs should stop the clock at ready, not provisioned

Conf42 Blog, 2026-10-30, updated 2026-11-09. https://www.conf42.com/blog/platform2026/platform-slos-that-stop-the-clock-at-ready

In short: Amith Reddy Ravuru (Reltio) at Conf42 Platform Engineering 2026 on journey SLOs that measure a developer's path from request to production-ready.

Every platform SLO can be green while a developer spends four days getting a working environment. At Conf42 Platform Engineering 2026, Amith Reddy Ravuru, Staff Platform Architect at Reltio, an SAP company, made the case for journey SLOs: measure the developer's trip from asking for something to putting real traffic on it, because the waiting lives between your services, where no dashboard looks.

He says the examples come from things his team got wrong and then fixed, and the numbers in the talk are illustrative. The method is the point.

## The watermelon week

Amith's opening story: on Monday a developer asks for a new tenant environment, the textbook golden-path request. The platform dashboard has a great week: 99.95% API availability, 180 ms p99, tiny error rate. The developer's week: a quota ticket Monday, a chat thread about network access Tuesday, a policy exception from another team Wednesday, first deploy works Friday.

Lay the request out on a timeline and the services did perhaps 40 minutes of work. The rest was queues, approvals and manual fixes, none of which has an SLO or an owner. IT service management folks call it the watermelon effect: green outside, red inside. Operational SLOs stop at the service boundary; developers live in the gaps.

## Five stages and one journey ID

His journey has five stages: requested, provisioned, usable (log in and do a first real deploy, not just get a 200), policy-compliant (no open exceptions), and operationally ready (monitoring set up, alerts routed to a real on-call). Many dashboards declare victory at provisioned. Amith's rule is that provisioned is the platform's milestone and first deploy is the developer's.

A journey SLI is good journeys over total journeys in a window, where good means reaching ready in time without rework. It spans five services and maybe three teams, so someone has to own the whole path, and on a platform team that's you. The glue is a journey ID minted at request time and carried everywhere as a tag or label, so workflow events, pipeline events, tickets, chat and policy checks can be joined into one record per journey.

## Six indicators in three honest pairs

Each pair keeps the other from being gamed, an idea he credits to the SPACE paper:

- **Faster**: time to first environment (request to first successful deploy) and time to operational readiness (until the last readiness check passes; record which check was last, and for his team it was usually alert routing).
- **Safer**: failed-workflow recovery time, split by cause (quota, permissions, policy, cloud API, product bug), and rework rate, any redo within 14 days after handoff.
- **Easier**: self-service completion rate, where one manual runbook step or side-channel approval disqualifies the journey, and support dependency, help requests per 100 journeys. A nice trick: have the platform channel's bot ask which journey a question is about.

Data is mostly already there. Add one pulse question when a journey ends, rated one to five, because telemetry and people each miss things: a step can be fast and confusing, or slow and so familiar nobody complains anymore.

His multi-cloud tenant example adds orchestration metrics: planning accuracy on the bill of materials, hand-off wait to each component team, and which component lands last on the critical path. One example record shows a flow efficiency of 18%, so the tenant spent most of its life sitting in queues.

## Six ways to get it wrong

The anti-patterns are worth the watch alone. Reporting averages (four two-hour journeys and one four-day one average to 21 hours, hiding the person who lost a week). Stopping the clock at provisioned. Pushing one indicator alone. Hiding a human step behind a portal button. Setting targets before a baseline. And ranking component teams on a league table, which makes people manage the number instead of the journey.

His rollout plan fits in a month: define done for one painful journey, instrument it with a journey ID, watch real journeys for a baseline, then set targets and a journey error budget.

## Who should watch

Platform product owners asked to prove the golden path works, and SREs who want to point SLO thinking at internal users. It pairs well with any DORA or SPACE reading you've already done.

## Related Conf42 talks

- [SLOs for Event-Based Systems: Navigating the Triad of Availability, Freshness, and Correctness](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Ricardo_Castro_slos_eventbased_navigating) by Ricardo Castro (FanDuel)
- [Breaking Down the Principles of Platform Engineering: How to Empower Developer Experience](https://www.conf42.com/Platform_Engineering_2024_Cedric_Clyburn_Valentina_Rodriguez_Sosa_platform_empower_experience) by Cedric Clyburn and Valentina Rodriguez Sosa (Red Hat)
- [Starting the SLOs Implementation](https://www.conf42.com/Site_Reliability_Engineering_2023_Muhammad_Jihad_starting_slos_implementation) by Muhammad Jihad

[Watch Amith's talk](https://www.conf42.com/Platform_Engineering_2026_Amith_Reddy_Ravuru_slos_uptime_journey)

[Watch the talk on YouTube](https://youtu.be/ciQKpu_JmN4).

## Watch the talk

[Platform SLOs Beyond Uptime: Measuring the Journey from Request to Value](https://www.conf42.com/Platform_Engineering_2026_Amith_Reddy_Ravuru_slos_uptime_journey) at Conf42 Platform Engineering 2026.
