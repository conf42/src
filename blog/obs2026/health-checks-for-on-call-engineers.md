# You health-check every service. Health-check the on-call team too

Conf42 Blog, 2026-08-28, updated 2026-11-09. https://www.conf42.com/blog/obs2026/health-checks-for-on-call-engineers

In short: Sylvain Kalache of Rootly at Conf42 Observability 2026 on observed and self-reported signals that spot on-call overwork before it turns into resignations.

Your services get liveness probes, SLOs and a dashboard each. The engineers carrying the pager get asked how they are, and they say fine. At Conf42 Observability 2026, Sylvain Kalache, Head of AI Labs at Rootly, laid out a way to monitor responder health with the same discipline you apply to systems: collect two kinds of signal, score them, and watch the trend rather than the number.

It's a short, practical talk, and it ends with a free open source tool. Kalache is upfront that Rootly built that tool, so this counts as a vendor talk, though the framework works without it.

## Being on call costs something even when nothing pages

Kalache opened with survey data from Catchpoint: most engineers are on call, most feel stress during incidents, and most still feel it after the incident ends. His guess at why is the follow-up work: write-ups, tickets, and in less blameless shops, being blamed for not fixing it faster. More than half reported worse sleep while on call even without getting paged. Knowing the phone might ring is enough.

## GenAI makes the formula worse

He anchored the next part in a simple incident-rate idea: the number of changes shipped multiplied by the chance any one of them breaks something. Generated code pushes the change count up. He looked at Rootly's own customer data since 2023 and saw average incident counts climb, with a careful correlation-is-not-causation caveat.

Two quieter effects matter as much. Developers lose touch with code they prompted rather than wrote, so the person a responder escalates to may not know how it works. And as engineers get pushed towards broader, full-stack roles, the deep specialist you need for that one MySQL outage gets harder to find. More incidents, less help, and a manager reminding you that you have AI now.

## Two kinds of data: observed and self-reported

The framework splits signals in two.

**Observed data** is what your tooling already knows: shifts covered, pages and incidents handled, severity, nights and weekends. Kalache added one newer signal: token consumption. He pointed to public accounts of founders and engineers losing sleep to round-the-clock agentic coding, including Rootly's own CTO. Heavy token use at night might mean someone automated their job. It might also mean someone needs a conversation.

**Self-reported data** comes from two questions, borrowed from a clinical method called EMA (ecological momentary assessment): how are you feeling today, and what's having the biggest impact on you? Ask in one-on-ones and through Slack or a survey, since people differ in where they'll answer honestly.

## Read the trend, not the score

Combine the signals into a risk score (his example used 0 to 100), then resist comparing people with it. His example: Mary at 80 with fifteen years of on-call may be fine; Bob at 25 in his first year may be drowning. Context beats the number.

What matters more is the slope. A score climbing fast, or creeping slowly over months, is when to step in. None of it is diagnostic, Kalache stressed. It's a conversation starter, and the worst case is a check-in that turns out to be unnecessary.

## The tool and two stories

Rootly's AI Labs built this as OnCall Health, open source under Apache 2.0, hosted or self-hosted, with integrations for Rootly, PagerDuty, Datadog, Linear, Jira, Slack and more. Kalache shared two adopters: Casey Brown at Weights & Biases used it for a before-and-after when changing the on-call setup, and Joshua Inoa at Brex replaced anecdotal weekly responder-health reports with data-backed ones. His closing advice was the shortest possible version of the talk: start measuring.

## Who should watch

Engineering managers and SRE leads with a rotation to look after, especially anyone who has watched a strong engineer quietly burn out. Individual responders get a vocabulary for raising the topic. If you want hard research numbers, expect a framework talk with a few cited surveys rather than a study.

## Related Conf42 talks

- [Ajuna Kyaruzi on sustainable incident management for happy SRE teams](https://www.conf42.com/Site_Reliability_Engineering_2021_Ajuna_Kyaruzi_sustainable_incident_management_happy_SRE_teams) (Conf42 SRE 2021).
- [Einat Mahat on creating on-call heroes](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) (Conf42 Incident Management 2023).
- [Mandi Walls on tackling alert fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) (Conf42 SRE 2025): fewer pages is the cheapest wellbeing fix.

[Watch Sylvain Kalache's talk](https://www.conf42.com/Observability_2026_Sylvain_Kalache_burnout_oncall_sre)

[Watch the talk on YouTube](https://youtu.be/fu97UJfOoIA).

## Watch the talk

[Health Checks for Systems. What About Your Team?](https://www.conf42.com/Observability_2026_Sylvain_Kalache_burnout_oncall_sre) at Conf42 Observability 2026.
