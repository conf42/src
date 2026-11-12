# During a major incident, the incident commander outranks the CEO

Conf42 Blog, 2021-10-01. https://www.conf42.com/blog/sre2021/incident-commander-outranks-the-ceo

In short: Quintessence Anx (PagerDuty) at Conf42 Site Reliability Engineering 2021 on the incident command system, its roles, and why a wrong call beats no call

Wildland firefighters figured out incident response decades before anyone got paged about a Kubernetes cluster. Quintessence Anx, Developer Advocate at [PagerDuty](https://www.pagerduty.com/), builds her Conf42 Site Reliability Engineering 2021 talk on that inheritance: the incident command system, adapted for software teams, with defined roles, a clear switch into emergency mode, and one person in charge who outranks everyone on the call, the CEO included. The goal, in her repeated phrase, is to replace chaos with calm.

## What counts as an incident, and a major one?

She starts with definitions, because you cannot respond to something until you agree what it is. Quintessence Anx said at Conf42 Site Reliability Engineering 2021: "An incident is any unplanned disruption or event that requires immediate attention or action." PagerDuty defines a major incident as any incident that needs a coordinated response across multiple teams, optionally tied to a business metric such as a percentage of customers affected. Keep the definitions short so nobody argues about them mid-outage.

Her severity walk-through uses an imaginary online shop. Product images not loading but checkout working is a SEV 5. Trouble at checkout climbs toward SEV 3. Crossing from SEV 3 to SEV 2 is the line where the major incident process starts. Metrics work best when tied to business impact; at PagerDuty one of them is outbound notifications per second.

Two rules follow. Anyone must be able to trigger an incident at any time, because monitors miss things and opening an incident you then close is cheaper than waiting. And once triggered, the team switches from peacetime to wartime (or normal to emergency, if you prefer less military words), where risks such as deploying with minimal testing can become acceptable.

## Where does the incident command system come from?

ICS was developed after large Southern California wildfires, when thousands of firefighters who each knew how to fight a fire could not coordinate with each other at scale. The FIRESCOPE effort produced the model, and in 2004 FEMA's National Incident Management System made it the standard for US public agencies, from house fires to natural disasters. Standardised process means responders spend their energy on the fire, not on inventing a process during it.

## Who does what on the call?

The lifecycle is triage, mobilise, resolve, prevent. The roles:

- **Incident commander**: runs the response, breaks ties, assigns every task to a named person, time-boxes it and follows up. The highest authority on the call, whatever their day job, which needs buy-in in advance.
- **Deputy**: an active role, not a shadow. Takes on overflow, nudges the IC when a check-in is late, and stands by for handoff.
- **Scribe**: writes the timeline with context, short sentences such as why a cluster was rebooted, which feeds the postmortem.
- **Internal and customer liaisons**: send updates, about every 30 minutes, so executives and customers are not pinging responders.
- **Subject matter experts**: the people actually fixing it.

The roles scale down for a 20-engineer company: a scribe can double as liaison, but keep the incident commander dedicated. She also notes that PagerDuty used to require every incident commander to be an engineer and calls that a big mistake. ICs coordinate rather than fix, and the rule shrank the pool of people who could do it.

## How does the commander keep decisions moving?

Decision paralysis is the enemy. Quintessence Anx said at Conf42 Site Reliability Engineering 2021: "Making a wrong decision in this case is better than making no decision." The PagerDuty technique is to ask the call whether there are any strong objections; if nothing outweighs the proposal, pick it, move, and learn from the result.

Her tips for new commanders: introduce yourself as the IC, avoid acronyms (PR is a press release to one team and a pull request to another), speak slowly, remove disruptive people, time-box tasks and declare explicitly when the response is over. The pitfalls include the executive swoop, failing to notify, red herrings, debating severity, and assuming silence means no progress.

## How do you get ready?

Write the process down, then practise it, for example in PagerDuty's Failure Friday chaos sessions, with checklists. And do the postmortem while memories are fresh. Her slides point to PagerDuty's open Response Ops guide, an expanded version of the talk.

## Who should watch

Teams whose incident calls are a crowd of people typing over each other, new incident commanders, and managers who want to know why the on-call engineer just asked them to leave the call.

## Related Conf42 talks

- Robert Ross on [pragmatic incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Robert_Ross_pragmatic_incident_response), also at SRE 2021.
- Kurt Andersen on [varieties of incident response](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response) at Conf42 Incident Management 2022.
- Emily Arnott and Nick Mason on [too many people in the room](https://www.conf42.com/Incident_Management_2022_Nick_Mason_Emily_Arnott_too_many_people) at Conf42 Incident Management 2022.

[Watch Quintessence Anx's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Quintessence_Anx_dont_panic_effective_incident_response)

## From PagerDuty

PagerDuty runs on-call scheduling, alerting and incident response, and publishes the Response Ops guide the talk is drawn from.

- [PagerDuty website](https://www.pagerduty.com/)
- [PagerDuty Incident Response documentation](https://response.pagerduty.com/)

[Watch the talk on YouTube](https://youtu.be/s0Cs1PkJ-UA).

## Watch the talk

[Don't Panic! Effective Incident Response](https://www.conf42.com/Site_Reliability_Engineering_2021_Quintessence_Anx_dont_panic_effective_incident_response) at Conf42 Site Reliability Engineering 2021.
