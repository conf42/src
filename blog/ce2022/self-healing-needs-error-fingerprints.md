# Self-healing systems start with knowing which errors matter

Conf42 Blog, 2022-03-09. https://www.conf42.com/blog/ce2022/self-healing-needs-error-fingerprints

In short: Nick Hodges (Rollbar) at Conf42 Chaos Engineering 2022 on self-healing SaaS systems, where grouped critical errors trigger rollbacks or flag flips

A self-healing system cannot heal what it cannot see, and a log file full of colourless errors is a poor pair of eyes. At Conf42 Chaos Engineering 2022, Nick Hodges, Developer Advocate at Rollbar, argued that error tracking is the thread that runs through both the problem and the cure: group errors well enough to trust which ones are critical, and a system can roll itself back or switch off a feature flag before anyone's phone rings at 2am.

It is a conceptual talk, light on code and heavy on metaphors, from a Delphi veteran and former naval intelligence officer who reports that intelligence work is far more boring than TV suggests.

## What counts as self-healing?

Nick's working definition: a system that recognises it is not working right and fixes itself without outside help. Fixing here does not mean rewriting the bug. It means getting back to a known working state, by turning off a feature flag or rolling back to the previous release.

He frames it as three levels. Level one is fully manual: a customer reports a bug, someone opens a debugger, ships a fix. Level two adds some automation, such as monitoring that tells you something broke but not where, followed by a manual fix and deploy. Level three, fully automated detection and restoration, is what he calls self-healing. It became possible with SaaS: when you control the backend and the web client, you no longer have to reproduce a customer's machine to find a bug.

## What does a system need before it can heal itself?

Three requirements: it is always up (a deploy that needs downtime rules it out), it is monitored (no signal, no healing), and it has a restoration mechanism. On top of those, he lists the characteristics:

- **Cattle, not pets.** Deploy to any server in a cloud fleet, not a hand-fed machine with a name.
- **Zero-downtime deploys**, typically blue-green behind a load balancer.
- **Dynamic capacity**: watch CPU and network load and spin up machines as demand rises.
- **Real-time service monitoring and reaction to failure**, which he identifies as the chaos engineering part.
- **Acting on predictable futures**, such as scaling up ahead of a known Monday 9am spike.

## Why a circuit breaker beats a dashboard light

The best section is a run of three metaphors for error detection. Old series-wired Christmas lights: one bad bulb and the whole string goes dark, and you swap bulbs one at a time to find it, the works-on-my-machine era of desktop software. A car's overheating light: you know there is a problem, not why. A household circuit breaker: it stops the fire and tells you exactly which circuit failed. That last one is his model for self-healing. A critical error firing is the breaker snapping, and the automated response is the rollback or the flag flip.

His caution is sensible. Nick said at Conf42 Chaos Engineering 2022: "You can't automate the response for every error, but you can automate the response for some errors." The ones you automate are the ones you trust are truly critical.

## Why grouping errors is the hard part

In a busy SaaS application, errors arrive almost constantly, many harmless, a few urgent. Traditional monitoring and log files give humans a firehose that people are bad at reading. Nick's point is that you need errors grouped and classified as new, reactivated, resolved, critical or informational before any automation can act on them.

He ties this to how development changed: from boxed software on CDs that had to be perfect before shipping, to agile teams that fix the bugs that matter most first and ship continuously (he cites Amazon deploying thousands of times a day). That speed only works with automated releases and automated feedback.

## Who should watch

Engineering managers and SREs sketching the case for automated remediation, and anyone who wants a clear, metaphor-driven vocabulary for it. Engineers looking for implementation detail, thresholds or code will not find it here.

## Related Conf42 talks

- Leonid Belkind on [generic mitigations for self-healing systems](https://www.conf42.com/Chaos_Engineering_2021_Leonid_Belkind_generic_mitigations_self_healing_systems) at Conf42 Chaos Engineering 2021.
- Matthew Schillerstrom on [feature flags for reliability and agile response](https://www.conf42.com/Chaos_Engineering_2024_Matthew_Schillerstrom_feature_flags_reliability_agile_response) at Conf42 Chaos Engineering 2024.
- Ayelet Sachto on [minimising incident impact](https://www.conf42.com/Chaos_Engineering_2022_Ayelet_Sachto_reliable_systems_minimize_incidents_impact) at Conf42 Chaos Engineering 2022.

[Watch Nick Hodges's talk](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems)

## From Rollbar

In the talk, Rollbar is the error tracking layer: it uses machine learning to give each error a fingerprint and group occurrences, flags critical ones, and fires a webhook so a pipeline can roll back a release, turn off a feature flag, and notify the developer through email, Slack or PagerDuty.

- Rollbar: [rollbar.com](https://rollbar.com/signup/?utm=conf42)

[Watch the talk on YouTube](https://youtu.be/UBqouRXnslA).

## Watch the talk

[Self Healing Systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) at Conf42 Chaos Engineering 2022.
