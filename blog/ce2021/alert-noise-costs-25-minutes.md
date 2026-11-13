# Every dismissed notification costs you 25 minutes of focus

Conf42 Blog, 2021-02-25. https://www.conf42.com/blog/ce2021/alert-noise-costs-25-minutes

In short: Quintessence Anx (PagerDuty) at Conf42 Chaos Engineering 2021 on cutting alert noise by sorting sources, urgency and routing, then cleaning up every sprint

Muting Slack feels like peace and quiet until you remember you made the quiet yourself. At Conf42 Chaos Engineering 2021, [Quintessence Anx](https://www.conf42.com/Chaos_Engineering_2021_Quintessence_Anx_monitoring_sensory_friendly), Developer Advocate at PagerDuty, argued that noisy monitoring is a cognitive problem before it is a tooling one, and that the fix is to sort every alert by who needs to know, how soon, and through which channel, then keep pruning.

## What does a small interruption actually cost?

The talk opens with research rather than dashboards. Quintessence cites Gloria Mark's work at UC Irvine on interrupted work: when you are holding a mental model of a complicated system and a notification pops up in the corner of your screen, even dismissing it costs about 25 minutes to get back to where you were. You are not ignoring the alert; you are multitasking badly.

Two more studies follow. In a George Mason University experiment with AP essay tests, interrupted students scored about half a point worse on a zero-to-five scale, and 96% did worse; a follow-up that gave back roughly 30 minutes of extra time still saw the same group underperform. And on simple sequential tasks, the closest thing to writing lines on a chalkboard, adding background noise tripled the error rate. Engineers building a cluster are closer to the essay than the chalkboard.

The trap is the obvious response. Quintessence Anx said at Conf42 Chaos Engineering 2021: "The silence isn't because nothing's wrong. The silence is because you've turned on mute."

## Find the source, then the category

The method is: be aware, not overwhelmed. Identify where the noise comes from, categorise it, channel it, and set a routine to clear it.

Sources come in two kinds. Machine noise includes chatty services, legacy checks nobody remembers and conditions that measure the wrong thing; a classic is treating HTTP 200 as healthy when the body is an error message, a false negative that never pages anyone. Human noise includes you: checking email between tasks, a phone face up on the desk, the smart speaker a colleague tries to trigger during a video call. The human fix is boundaries that are communicated: announce focus time, say how long it lasts, and say how to reach you for something genuinely urgent.

For machine alerts the categories are false positives and negatives, fragile systems and anything frequent. Fragile systems that fire low-priority alerts at high-priority urgency train people to ignore pages, so the real one gets buried. If you cannot delete such an alert, at least downgrade it to email or chat.

## Route by who needs it and how soon

Quintessence describes, from earlier SRE work, getting alerts for services outside her area, which means lost minutes in an active incident while she hunts down the right owner. Track every misroute, fix them one by one, and audit the whole flow if it keeps happening.

Urgency should follow service criticality: a tier 0 or tier 1 service earns a phone page at 4am, a tier 2 or 3 service can wait for business hours. Redundancy matters for the quiet channel too. The talk points at the major Slack outage at the start of 2021: if Slack was the only home for low-urgency alerts, those alerts went nowhere that day. The goal is trust, so that silence means nothing is happening.

## Sprint cleaning

The closing practice is a recurring cleanup. Each time an alert fires, ask: is it needed, was it resolved, can it be automated, is there a permanent fix, and was it actually urgent? If a failure now self-heals, alert on the healing failing instead: "you don't care if it's starting to fail, you care if it can't recover". The first pass will be a project; doing it every sprint keeps it from becoming one again.

## Who should watch

Anyone whose on-call phone buzzes more than it should, and team leads who suspect their engineers have quietly muted half the alert channels. It is a practices talk, light on tooling, with the research up front.

Related Conf42 talks:

- Mandi Walls on [tackling alert fatigue](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue), Conf42 SRE 2025.
- Birol Yildiz on [AIOps and alert noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise), Conf42 DevSecOps 2024.
- Julie Gunderson, also of PagerDuty, on [postmortems and blameless culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at the same event.

## From PagerDuty

PagerDuty makes the incident response and on-call platform that sits at the end of many of the alert flows described in the talk.

- [PagerDuty](https://www.pagerduty.com/)

[Watch the talk on YouTube](https://youtu.be/F6czQRpCjiw).

## Watch the talk

[Sensory Friendly Monitoring: Keeping the Noise Down](https://www.conf42.com/Chaos_Engineering_2021_Quintessence_Anx_monitoring_sensory_friendly) at Conf42 Chaos Engineering 2021.
