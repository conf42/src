# An incident is when someone has to drop everything

Conf42 Blog, 2022-09-28. https://www.conf42.com/blog/im2022/incident-is-when-someone-drops-everything

In short: Nishant Roy (Pinterest) at Conf42 Incident Management 2022 on defining incidents, the runner and manager roles, blameless postmortems and what to measure.

Every incident is a bug, but not every bug is an incident, and the difference decides who gets woken up. At Conf42 Incident Management 2022, Nishant Roy, Engineering Manager for the Ads Serving Platform at Pinterest and a company incident manager on call with 150-plus incidents behind him, lays out a full incident process from the definition to the metrics, with ads examples that make the trade-offs concrete.

It's a sponsor talk with no product in it, just a complete, opinionated process.

## What makes something an incident, not a bug?

The textbook definition, an event outside normal operations that interrupts or degrades service, fits most bugs too. Nishant wants something actionable: an incident is when one or more people need to drop everything else and fix the bleeding immediately. A bug can have an urgent SLA too, but typically only during business hours and only for the owning team.

From there, five phases: detect, triage, mitigate, prevent (find and fix the root cause) and remediate (the follow-ups that make the system more resilient).

## Pull the andon cord

For declaring incidents he borrows Toyota's andon cord, which any worker could pull to halt the line. Software rarely needs to stop all production, but the rules carry over:

- **When:** whenever you need immediate support, with criteria per team. An ads team might use revenue impact; others login failures, app crashes, stale content, latency or content safety.
- **Who:** "Anybody who notices the impact should be empowered to declare an incident," Nishant Roy said at Conf42 Incident Management 2022.
- **How:** as easily as pulling a cord, whether that's a form or a particular Jira ticket type, and it must notify someone.

Severity follows from how many people need to respond or know. A slower home page is SEV3 or SEV4 for the owning team; login down for everyone is SEV0 or SEV1 and execs want to hear.

## Two roles, one priority

Once declared: open a channel, a video call or room, and optionally an investigation doc for latecomers. Then assign two roles. The **incident runner** owns the outcome and drives debugging and escalation. The **incident manager** coordinates: assesses impact and severity, picks the right runner, handles broader and external communication, and keeps the team calm and prioritised.

Impact assessment also picks the resolution style. Midday with everyone around, a hotfix or roll-forward may be fine; at 2am, roll back and introduce nothing new.

Priority one is stopping the bleeding. Roll back anything suspicious whose timing lines up (deploys, experiments, config flags), even if you don't think it's the cause. Or patch the symptom, for example a fallback path when a dependency starts returning empty data. Mark the incident mitigated, then fix the root cause to the point you're confident it won't recur for a while (he suggests a month), restore paused deploys and rolled-back experiments, and send a final update.

## Postmortems: what and why, never who

His postmortem template has five parts: impact, root cause, a detailed timeline, the time to detect, mitigate and resolve, and remediation items with owners. Hold an in-person review with the responders and system owners, and put an SLA on both the postmortem and its action items.

His five whys example ends one step later than many teams would. Users can't log in, because the API rejects the request, because it can't reach the authentication service, because it lacks the right SSL cert, because someone copied the wrong config to prod. A person can't be the root cause, so ask once more: there's no validation for the API config. That's the fix.

## Lessons from the incident manager seat

- **Destigmatise incidents.** At Toyota, workers weren't just allowed to pull the cord, they were obliged to. Praise reporters and responders publicly, reward them, and give them time off after late nights.
- **False positives beat false negatives.** Declare early and downgrade to a bug later; waiting lets impact balloon.
- **Be confident.** If ad load jumps from two in ten posts to six in ten and relevance drops, do you switch ads off and take the revenue hit, or show bad ads for a while? The manager doesn't make every call alone, but finds the information and the person who can.
- **Ask for help**, and keep a list of key decision makers and external support contacts for the cloud and third-party services you depend on.

## What should you measure?

Mean time to recovery, time between failures, and mean time to detect (if it's high, the action item is better alerting). And use error budgets to trade innovation work against keep-the-lights-on work: at three nines, the budget is a little under nine hours a year; once a service is out of budget, stability work comes first.

## Who should watch

Teams writing their first incident process, or new incident managers wondering what the job actually is. Pair it with [Kurt Andersen on the varieties of incident response](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response) at the same event, [Einat Mahat on effective on-call practices](https://www.conf42.com/Incident_Management_2023_Einat_Mahat_oncall_heroes_effective_practices) at Conf42 Incident Management 2023, and [Fred Moyer on SLOs and error budgets at scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) at Conf42 Observability 2023.

[Watch Nishant Roy's talk](https://www.conf42.com/Incident_Management_2022_Nishant_Roy_incident_management) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From Pinterest

Nishant's team runs the services behind Pinterest's ads business, and Pinterest Engineering was hiring when he gave the talk.

- [Pinterest engineering jobs](https://www.pinterestcareers.com/job-search-results/?primary_category=IT)

[Watch the talk on YouTube](https://youtu.be/CDuEB_uV2E4).

## Watch the talk

[Running an effective incident management process](https://www.conf42.com/Incident_Management_2022_Nishant_Roy_incident_management) at Conf42 Incident Management 2022.
