# Watch the business workflow, not the service, to detect faster

Conf42 Blog, 2026-03-06, updated 2026-11-09. https://www.conf42.com/blog/sre2026/watch-the-workflow-not-the-service

In short: Rohit Wadhwa (Walmart) at Conf42 SRE 2026 on Predictive Workflow Integrity, which models workflows as state machines and cut detection time below a minute.

A burnt pizza alarm fires after the damage is done; a better system checks the oven temperature and the dough on the way. That analogy opens the talk by Rohit Wadhwa, Senior Software Engineer at Walmart, at Conf42 Site Reliability Engineering (SRE) 2026. His model, Predictive Workflow Integrity (PWI), moves observability from individual services to end-to-end business workflows, and he reports mean time to detection dropping from about 12 minutes to 58 seconds.

It's a short talk, more of a model and results summary than an implementation guide, but the reframing is worth the time.

## Service signals miss workflow failures

Event-driven microservices across regions bring three problems Rohit sees in practice. State divergence, where services stop agreeing about what's going on. Latency variability, where one slow service compounds across the whole call path. And cascading failures, where one failing component ripples into a wide outage. Service-level dashboards can look fine while a business workflow is stuck halfway, and with a 12-minute detection time you're only starting to fix things after customers have noticed.

## Workflows as state machines

PWI models each workflow as a distributed state machine and keeps evaluating its transitions. It looks for three red flags:

- **Delayed convergence.** The workflow doesn't reach its expected state within the expected time, a sign some service didn't follow its instructions.
- **Conflicting ownership.** Several teams acting on the same workflow or platform, which slows down resolution.
- **Abnormal execution paths.** A service routes the workflow down an unexpected path, which leads to degraded performance and then failure.

None of these are visible from a single service's latency graph, which is the point.

## Autonomous triage on a causal graph

To act on those signals, PWI correlates logs, metrics and traces into one map of the system (the abstract calls it an event-driven causal graph) and applies machine learning on top to prioritize incidents by severity. From there it moves to automated remediation. Rohit claims it predicts likely issues and fixes some before they surface, which reduced incident creation and level-two escalations. He doesn't walk through the models themselves, so treat this part as the outline of an approach rather than a recipe.

The numbers, from the talk and its abstract: MTTD went from roughly 12 minutes to under one minute (58 seconds in his example), mean time to mitigation from about 45 to 50 minutes down to 10 to 12, and false-positive alerts from around 18% to about 4%. That last one matters most for on-call morale.

## Rings by geography

The second idea is Ring-Based Geolocation Routing. If users are on the East Coast and servers on the West Coast, you pay latency on every call, and a regional failure can take down the whole application. Rohit's team localized event processing and decisions into rings per region. He reports edge-to-cloud latency falling from about five seconds to under one, roughly an 80% improvement, and says PWI runs across thousands of nodes at edge and cloud.

## Who should watch

SREs whose dashboards are green while customers report stuck orders, and teams thinking about workflow-level SLIs. If you want implementation detail (which models, how the state machines are defined), you will need to follow up with the speaker; the value here is the reframing and the before/after numbers.

## Related Conf42 talks

- [Enhancing Workflow Reliability with Dapr: Techniques to Minimize Failure Costs](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) by Siri Varma Vegiraju (Microsoft), workflow reliability at the runtime level.
- [Optimize end user connectivity for multi-region architectures](https://www.conf42.com/Site_Reliability_Engineering_2022_Christian_Elsen_Lerna_Ekmekcioglu_reliable_multiregion_arch) by Christian Elsen (AWS), on the routing side.
- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz (Ilert), for the false-positive problem.

[Watch Rohit Wadhwa's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Rohit_Wadhwa_predictive_workflow_integrity)

[Watch the talk on YouTube](https://youtu.be/uOm-lmrkIK0).

## Watch the talk

[Predictive Workflow Integrity for SRE: Autonomous Triage at Global Scale](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Rohit_Wadhwa_predictive_workflow_integrity) at Conf42 Site Reliability Engineering (SRE) 2026.
