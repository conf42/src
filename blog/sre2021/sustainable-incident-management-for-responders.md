# The scarce resource in incident management is the responder

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/sustainable-incident-management-for-responders

In short: Ajuna Kyaruzi (Datadog) at Conf42 Site Reliability Engineering 2021 on making incident response sustainable for the people on call, not just fast

The page always arrives at the worst moment: your kid's birthday party, brunch, the middle of real work. Ajuna Kyaruzi, who works in developer relations at [Datadog](https://www.datadoghq.com/), uses her Conf42 Site Reliability Engineering 2021 talk to treat incident management as a sustainability problem. Her definition of sustainable is a process you can repeat without depleting the resource it runs on, and that resource is your responders. The talk is a short tour of the pain points that wear on-call engineers down, and what to do about each.

Ajuna Kyaruzi said at Conf42 Site Reliability Engineering 2021: "The resources that we're discussing right now are the people who are responders to your incidents."

## Why is responder happiness hard to measure?

She admits it is hard to track: other than people leaving the team, how do you know an incident responder is happy? Her workaround is to go after the pain points directly and make each one as small as possible. She frames incident management as the whole loop: get paged, read the alerts, find the root cause, mitigate customer impact, ship a fix or roll back, then review and write the postmortem.

## How do you make on-call less intrusive?

Start with the rotation. Many teams run a 24/7 on-call for a week, sometimes alone. She suggests shorter shifts, with 12-hour cycles as the ideal, which works best when another time zone can take over at sundown. Add tiers of responders, primary, secondary, tertiary, so someone can take the subway or a walk away from the laptop without being the single point of failure for a system.

For SRE teams on call for services they did not write, standardisation helps: the same reporting tooling everywhere and one production release path, so rollbacks look the same for every service.

## What do severity levels buy you?

Severities run from a minor SEV 5 (the app is a bit slower, nobody notices) to SEV 2 or SEV 1, where you lose money or customers. Beyond triage, they are a resourcing signal. A higher severity says bring in more people and more expertise, often teams that handle large-scale coordination and stakeholder communication. Escalating also tells the responder it is fine to ask for help, and a raised severity lets other teams spot that an incident might involve them.

## How do new responders ramp up without panic?

Joining a rotation means suddenly owning a system you barely know. Her toolkit: shadowing and reverse shadowing the current on-call, incident response training so everyone shares terminology, and runbooks or playbooks for common incidents such as running out of quota. Quick wins matter, because fixing the thing that broke is one of the rewarding parts of being on call. Practise too: game days, disaster recovery training of the kind Google runs, role-playing incidents and reading old postmortems.

## Where does communication go?

One place. Ajuna Kyaruzi said at Conf42 Site Reliability Engineering 2021: "Having a unified channel of information makes this a lot easier." A Slack or IRC channel lets newcomers and the next incident commander catch up without interrupting responders, and it leaves a single record for the review. Large incidents may need two channels, one for responders and one for stakeholder updates, but never direct messages, where nobody else sees the update.

## Can the postmortem write itself?

Partly, and this is where the Datadog product enters. The postmortem is one more chore after an exhausting incident, when everyone wants to get back to what they were doing. She shows Datadog generating a draft postmortem when an incident resolves, pulling in metrics, logs, dashboards and links to the Slack channels to build the timeline, plus the tasks done and the remediation still to come. The responder edits instead of reconstructing from memory.

## Who should watch

Engineering managers setting up a first on-call rotation, SRE leads with a team that looks tired, and new responders who want to know what good looks like. It is a short, practical talk, more checklist than theory.

## Related Conf42 talks

- Quintessence Anx on [effective incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Quintessence_Anx_dont_panic_effective_incident_response), also at SRE 2021.
- Einat Mahat on [on-call heroes and effective practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) at Conf42 Incident Management 2023.
- Sylvain Kalache on [burnout and on-call in SRE](https://www.conf42.com/Observability_2026_Sylvain_Kalache_burnout_oncall_sre) at Conf42 Observability 2026.

[Watch Ajuna Kyaruzi's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Ajuna_Kyaruzi_sustainable_incident_management_happy_SRE_teams)

## From Datadog

Datadog is a monitoring and observability platform for metrics, logs and traces, with incident management features such as the auto-drafted postmortems shown in the talk.

- [Datadog website](https://www.datadoghq.com/)

[Watch the talk on YouTube](https://youtu.be/u3Hwu8mw_E8).

## Watch the talk

[Sustainable Incident Management for happy SRE teams](https://www.conf42.com/Site_Reliability_Engineering_2021_Ajuna_Kyaruzi_sustainable_incident_management_happy_SRE_teams) at Conf42 Site Reliability Engineering 2021.
