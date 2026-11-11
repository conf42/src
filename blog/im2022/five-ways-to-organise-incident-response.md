# Five ways to organise incident response, and none is always right

Conf42 Blog, 2022-09-29. https://www.conf42.com/blog/im2022/five-ways-to-organise-incident-response

In short: Kurt Andersen (Blameless) at Conf42 Incident Management 2022 on the work inside every incident and five ways to organise it, from pass-the-baton to ICS.

Your incident process probably copies one of about five models, and each has a predictable failure mode. At Conf42 Incident Management 2022, Kurt Andersen, SRE Architect at Blameless, maps the work every incident involves (diagnosis, therapy, recruiting, communication, coordination) onto five ways companies organise responders, and argues that adaptive incident command is the current consensus without being the right answer everywhere.

It's a compact, conceptual talk with no product pitch, the kind that gives you vocabulary to describe what your own process is actually doing.

## What is everyone in the incident channel doing?

Kurt starts in the middle of the story: the pager goes off, a technical responder from the service team picks it up and, especially in business hours, pulls in colleagues. Each of them, and the group as a whole, is running an OODA loop: observe the signals, orient by adding context (what was deployed recently, what else changed), decide on a response, act, and repeat to see what the action did.

Technically, that work splits into two kinds. Diagnosis is figuring out what's happening, what to do and what can be done about it. Therapy is acting to mitigate the issue and checking that the action worked. He adds a useful, slightly uncomfortable observation: sometimes an attempt at therapy is the diagnosis, and if it works, everyone concludes that must have been the problem.

## The work nobody counts

Then he backs up to what he glossed over. Recruiting the right people is real work, and it sits badly on a technical responder's shoulders, which is why it often moves to an incident commander, paged in by the responder's flare or by the pager directly. With even three or four people, someone has to coordinate who does what and when. And outside the response team are other concerned people (executives, managers, customers) who want updates, which is where a communications lead earns their keep.

So the functional model is: diagnosis and therapy on the technical side, recruiting and communication on the logistical side, coordination in the middle.

## Five organisational models

- **One at a time, or pass the baton.** Team A gets paged, decides team B is sending bad data, passes it on, and eventually someone decides it's DNS. There's often no incident commander, the problem can loop back to a team that already handed it off, and outsiders don't know who to ask.
- **All hands on deck.** Page all four teams plus an incident commander, or a cross-functional team, or literally everyone; some organisations pull 100 or 200 people into the channel. At least outsiders know who to talk to, but teams start looking for the exit and leave others holding the bag.
- **Escalation or tiered.** A NOC triages at tier one and tries to solve a large share itself, tier two takes another chunk, and tier three experts get pulled in only occasionally. Whether there's an incident commander depends on the organisation.
- **Strict ICS.** The incident command system adapted from wildland fire and FEMA emergency response, arriving in tech roughly a decade before the talk. The commander directs every team. Communication is handled, but it fits poorly with engineering cultures where everybody takes responsibility.
- **Adaptive ICS.** Thanks to the work of Laura Maguire, technical teams work in a largely self-directed way while the incident commander and communications lead wrap and protect them from the outside world. His colleague Matt Davis calls it the response trio: commander, comms lead, problem solvers.

## What does the incident commander actually do?

Kurt is precise about the role. The commander isn't in the graphs and logs; that's the problem solvers' job. "The incident commander's key role is to be focused on the coordination aspects of these problem," Kurt Andersen said at Conf42 Incident Management 2022: how the response is being conducted, not the incident itself. That includes keeping the common ground across the response team, bringing newcomers up to speed without distracting the responders, and noticing when people are getting worn out.

## Is adaptive ICS always the answer?

No, and that's the point of the title. Follow-the-sun support is pass the baton by design, with time-zone teams handing off every eight hours, and handoffs have a literature of their own. All hands on deck can be the right call in particular situations. Know each model's strengths and weaknesses and adapt.

He closes with a question worth taping to the monitor, why is this thing making noise, and a reading list: Laura Maguire on the hidden costs of coordination, Gary Klein and colleagues on common ground in joint activity, and Sidney Dekker on why things go right.

## Who should watch

Incident commanders, SRE leads and anyone redesigning an on-call structure who wants a vocabulary for the trade-offs. It's short and theoretical, no war stories, so pair it with something practical: [Nick Mason and Emily Arnott on keeping the incident room lean](https://www.conf42.com/Incident_Management_2022_Nick_Mason_Emily_Arnott_too_many_people) and [Nishant Roy on running an effective incident management process](https://www.conf42.com/Incident_Management_2022_Nishant_Roy_incident_management), both at the same event, or [Quintessence Anx on effective incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Quintessence_Anx_dont_panic_effective_incident_response) at Conf42 SRE 2021.

[Watch Kurt Andersen's talk](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From Blameless

Blameless builds an SRE platform covering incident response, communication and retrospectives.

- Blameless: [blameless.com](https://www.blameless.com/)
- [Blameless SRE blog](https://www.blameless.com/sre)
- [Resilience in Action podcast with John Allspaw](https://www.blameless.com/podcast/resilience-in-action-e14-resilience-is-the-audacity-of-adaptive-capacity-ft-john-allspaw)

[Watch the talk on YouTube](https://youtu.be/sWby8vdc7gk).

## Watch the talk

[Varieties of Incident Response](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response) at Conf42 Incident Management 2022.
