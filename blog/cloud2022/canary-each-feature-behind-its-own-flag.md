# Canary each feature behind its own flag, then delete the flag

Conf42 Blog, 2022-04-28. https://www.conf42.com/blog/cloud2022/canary-each-feature-behind-its-own-flag

In short: Hammad Mushtaq (Blameless) at Conf42 Cloud Native 2022 on staging releases to 25% of customers per sprint with feature flags, and picking the right canary group

Ship one feature to a quarter of your customers per sprint, keep a second feature on its own schedule, and make sure every flag has an owner who remembers to turn it on. That is the playbook Hammad Mushtaq, Engineering Manager at Blameless, laid out at Conf42 Cloud Native 2022, with Blameless's own rollout of a messaging feature as the case study, including the part that went wrong.

It is a short, practical talk aimed at teams that still do one big release per feature.

## Why start with reliability?

Mushtaq opens with the bluntest version of the SRE argument.

"Reliability is feature number one. Without reliability, nothing else matters," Hammad Mushtaq said at Conf42 Cloud Native 2022.

He describes the two extremes companies swing between. Startups ship features as fast as possible and let reliability slide until paying customers complain. Large companies, with a platform everyone depends on, slow to a crawl because every release needs a long test suite. The goal is the middle: fast innovation with high reliability, with SRE smoothing out the friction between dev and ops, and with unplanned work from production incidents counted as a cost to engineering, not just to customers.

His running example is an e-commerce journey: log in, search, add to cart. Login success matters most (if users can't get through the front door, no new feature helps), then search latency, then whether the cart works. Latency is the SLI, and the SLO is about latency over a window, not a single slow call. One slow response won't lose a customer; consistently slow ones will.

## What does a canary release change in the lifecycle?

Nothing, he says, except the deploy step. You still build, test, deploy, monitor, fix, review and learn. In a canary release the deploy is split into several steps, and the whole loop repeats for each group of customers. Because each step reaches only a small group, and the feature sits behind a flag you can switch off, fixes become less urgent.

He lists three payoffs: less impact when something breaks (stop or roll back before most customers see it), continuous feedback from each group (if the first customers can't use the workflow, you pause and revisit the design), and smoother operations, since a smaller audience means a smaller incident surface.

## How does it look sprint by sprint?

His timeline: feature A goes to 25% of customers in sprint one, 25% more in sprint two, 25% more in sprint three (time to finish the documentation before general availability), and everyone in sprint four. Feature B is ready in sprint three and starts its own 25% rollout while A is already at 75%.

The point of keeping them decoupled behind separate flags: if feature A misbehaves, you pause A and keep rolling out B. No reverts, no lost code, no merge conflicts from git surgery on a release branch.

Flags also tell you when something changed and for whom. He shows a Sumo Logic dashboard where a flag turns on around April 1 and Prometheus memory usage spikes right after. With the flag marker on the graph, the correlation is obvious, and turning the flag off is the fix. He still insists on a tested rollback strategy for the worst case.

## What went wrong in Blameless's own rollout?

The case study is Comms Flow, a Blameless feature that sends templated messages (with variables) to SMS, email, Slack, Microsoft Teams or status page recipients when incident status, severity or retrospective state changes. Almost every part could be flagged on its own: the trigger types, events versus reminders, template variables, recipient types.

The first iteration went to a hand-picked set of customer accounts in early December, who used it for the whole month; the next set of features followed, individually flagged, and then went to everyone. The wins were confidence in production readiness and a more agile roadmap, with engineers developing in parallel without stepping on each other.

The honest bits are the two lessons. Ownership: it wasn't clear whether the product manager, the engineering manager or the engineer should enable a flag, so some features they believed were released were never turned on for customers. And clean-up: once a feature is on for everyone, the flag checks are dead code and need removing, or the codebase fills with useless if statements.

## Who belongs in the first canary group?

Not the inactive users, who never asked for the feature, and not necessarily the most vocal ones, whose feedback can be noise. His pick is the power users already working in that product area, or the customers who asked for the feature. Their workflows are the ones you could break, and their feedback is the one you need. Telling them a staged rollout is coming also builds trust: it shows you have a plan.

## Who should watch

Teams moving from big-bang releases to progressive delivery, and engineering managers who need a simple sprint-based model to explain it. If you already run percentage rollouts in a flag platform, skip to the Comms Flow lessons.

## Related Conf42 talks

- Travis Gosselin on [deploy velocity with feature flags](https://www.conf42.com/Site_Reliability_Engineering_2022_Travis_Gosselin_unleashing_deploy_velocity_feature_flags) at Conf42 SRE 2022.
- Ran Isenberg on [smart AWS feature flags in CI/CD](https://www.conf42.com/DevSecOps_2022_Ran_Isenberg_level_up_cicd_smart_aws_feature_flags) at Conf42 DevSecOps 2022.
- Matthew Schillerstrom on [feature flags for reliability](https://www.conf42.com/Chaos_Engineering_2024_Matthew_Schillerstrom_feature_flags_reliability_agile_response) at Conf42 Chaos Engineering 2024.

[Watch Hammad Mushtaq's talk](https://www.conf42.com/Cloud_Native_2022_Hammad_Mushtaq_pushing_code_flag_your_canaries)

## From Blameless

Blameless builds an SRE platform covering incident response, SLOs and retrospectives; the Comms Flow feature in the case study is part of it. Kurt Andersen, the Blameless SRE Mushtaq quotes on reliability as a team sport, also spoke at Conf42 on [varieties of incident response](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response).

- Blameless: [blameless.com](https://www.blameless.com/)
- SRE blog: [blameless.com/sre](https://www.blameless.com/sre)
- Community: [Blameless SRE Slack channel](https://www.blameless.com/slack-community)

[Watch the talk on YouTube](https://youtu.be/efsa0DsZKLM).

## Watch the talk

[Pushing Code: Don't Forget to Flag Your Canaries?](https://www.conf42.com/Cloud_Native_2022_Hammad_Mushtaq_pushing_code_flag_your_canaries) at Conf42 Cloud Native 2022.
