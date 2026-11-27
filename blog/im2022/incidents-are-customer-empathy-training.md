# The support person yelling in your incident channel is on your side

Conf42 Blog, 2022-09-28. https://www.conf42.com/blog/im2022/incidents-are-customer-empathy-training

In short: Ryan McDonald (FireHydrant) at Conf42 Incident Management 2022 on using incidents to build customer empathy, partner with support and widen retros.

When someone from customer support bursts into the incident channel asking how bad it is, the usual reflex is a process fix: a tighter RACI, an incident commander as a firewall. At Conf42 Incident Management 2022, Ryan McDonald, Responder Advocate at FireHydrant and a founding member of Twilio's incident command group, proposes a different diagnosis: a deficit in customer empathy, and incidents as the place to fix it.

Ryan's path explains the angle. He started as an Outward Bound instructor leading 22- to 30-day mountaineering and rafting expeditions, where incidents meant search and rescue. His first software outage, as an intern, was a botched deploy and a lot of running around, and his main thought was that nobody was bleeding. Lower stakes, more complexity, and he was hooked.

## What does empathy buy you during an outage?

He defines customer empathy plainly, as understanding and vicariously experiencing what your customers feel, and admits that the word "feelings" sounds squishy next to ARR-threatening outages. Then he lists the payoff: incidents that hurt customers less, better working relationships with the other responding teams, and deeper learning with better process and product fixes afterwards.

The talk is built as three actions, each mapped to one of those outcomes.

## Understand what customers expect

Missed expectations, Ryan says, are behind almost every relationship problem, and customers are no exception. His three habits:

- **Use the product.** Not as a power user, just the basic workflows. If you can't, ride along with support, customer success or user research, who know the common use cases and the friction points.
- **Put customer impact front and centre.** Split the effort early: one person digs into the backend, another works out what customers actually see. Keeping that impact visible to everyone who joins frames the incident as people in pain, not a logic puzzle.
- **Use the app when it's broken.** Chaos engineering gives you degraded states on purpose; during real downtime, he suggests responders try the product in its degraded state too.

The point of all this is mitigation over curiosity. "Oftentimes in incidents response is not to resolve the issue or even understand it, but just to stop the bleeding, stop the pain for our customers," Ryan McDonald said at Conf42 Incident Management 2022. He ties it to money as well: net retention, ARR and upsells all depend on customers feeling understood on bad days.

## Why partner with support instead of fencing it off?

Ryan concedes his opening story cast support as the villain, and walks it back. Breaking down a sample panicked request from a customer-facing team, he finds that what reads as aggression is mostly desperation: support sits between the customers and the outage with almost no control over either.

His suggestions:

- **Build rapport before the crisis.** The ride-alongs double as relationship building. At SendGrid, support ran the product orientation every new employee went through, which made them the go-to experts on the customer experience. Many support folks also want mentors.
- **Set clean communication interfaces.** Agree when updates about customer impact will come, and if you miss the time, say so. A short note that there is nothing yet and the next check-in is in 30 minutes beats silence, and keeps execs in the loop at a safe distance.
- **Let support behind the curtain.** Treat them as responders: they can test from the customer's side, bring direct reports that help you skip red herrings, and verify fixes in lower environments or behind feature flags. Advocate for them, too, since support is often measured on tickets per hour and needs cover to focus on an incident.

The bonus outcome is a hiring bench. A senior support person brings domain and organisational knowledge no outside hire has, for roles from product manager to incident commander to junior engineer.

## Retrospectives, plural

The third action widens the post-incident review. Bring customer-facing responders into the retro, or at least do a quick async check-in with them and carry their experience into the room. For big incidents, plan several sessions in advance: one on the technical cause, one on the response process, one on customer communication.

Then capture every improvement, not just the technical action items. Should the product degrade gracefully instead of failing outright? Did the error messages make sense to a customer, and did they give the people escalating internally a useful signal? Feed those into the backlogs and make sure the PMs and TPMs see them. Ryan calls retros a flywheel for improvement, and customer empathy "an organizational lubricant".

## Who should watch

On-call engineers who dread the support ping, incident commanders designing their comms cadence, and anyone running retros that stop at the root cause. It's a practice talk with no product demo; FireHydrant comes up only as Ryan's employer. Pair it with [Julie Gunderson on postmortems as continuous learning](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at Conf42 Chaos Engineering 2021, [Ramon Medrano Llamas on postmortem culture at Google](https://www.conf42.com/Site_Reliability_Engineering_2022_Ramon_Medrano_Llamas_postmortem_culture_google) at Conf42 SRE 2022, and [Amir Shaked on creating a learning culture](https://www.conf42.com/Incident_Management_2022_Amir_Shaked_create_learning_culture) at the same event.

[Watch Ryan McDonald's talk](https://www.conf42.com/Incident_Management_2022_Ryan_McDonald_incidents_customer_empathy_workshop) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From FireHydrant

FireHydrant builds incident management tooling: service catalogs, incident response, status pages and retrospectives.

- FireHydrant: [firehydrant.io](https://firehydrant.io)
- [How FireHydrant works](https://firehydrant.com/how-it-works)
- [FireHydrant blog](https://firehydrant.com/blog)

[Watch the talk on YouTube](https://youtu.be/vgneAnJCcl4).

## Watch the talk

[Incidents: the customer empathy workshop you never wanted](https://www.conf42.com/Incident_Management_2022_Ryan_McDonald_incidents_customer_empathy_workshop) at Conf42 Incident Management 2022.
