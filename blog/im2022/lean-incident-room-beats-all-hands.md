# A crowded incident room is slower, not safer

Conf42 Blog, 2022-09-29. https://www.conf42.com/blog/im2022/lean-incident-room-beats-all-hands

In short: Nick Mason and Emily Arnott (Blameless) at Conf42 Incident Management 2022 on why crowded incidents slow down and how types, roles and comms keep teams lean.

When production breaks, the instinct is to page everyone who might know something. At Conf42 Incident Management 2022, Nick Mason, Solutions Engineer at Blameless, and Emily Arnott, Blameless's Community Manager, argue that this all-hands reflex makes incidents slower, louder and more stressful, and that a lean team with clear types, roles and communication beats a crowded room.

It's a conversational two-hander from the sponsor's team, more practice than product.

## What does too many people actually cost?

Emily lists the symptoms anyone who has lived through a big Slack incident channel will recognise: nobody knows what each person is doing, redundant work, both poor and excessive communication (hours of scrollback), people standing around, extra stress, and anxiety from those who want to help and can't find anything to do.

Nick puts a number on it. An SRE manager at an e-commerce company told him it takes someone 10 to 15 minutes just to get up to speed on an incident. Multiply that by everyone who joins, and the crowd itself becomes a cost. Or, as the slide headline has it, you can't help if you don't know what's happening.

## Why do incidents get crowded?

Their diagnosis comes down to three things: poor classification that leads to over-escalation, too many subject matter experts deemed necessary, and a lack of confidence that tasks will get done without someone checking. Nick adds that on-call and ownership data often lives outside the chat tool running the incident, which means constant context switching.

## Classify by customer impact, not by blast radius

Nick's first fix is to define incident types and severity levels. A type can be use-case based (customer-facing, security, planned outage), team based, or service based. Severity then decides headcount: a SEV3 might need one person, a SEV0 everyone. His three words before opening an incident: "stop, think and assess," Nick Mason said at Conf42 Incident Management 2022. What kind of problem is this, who does it hurt, and how fast must it be fixed?

Emily sharpens the impact part with a riff on the tree falling in the woods. A full outage of a service hardly anyone uses can be lower severity than a mild slowdown in the feature everybody uses. Judge by customer impact and you stop overreacting.

## Escalate sideways, not just upwards

The second fix is escalation. A linear, hierarchical policy that pulls in more people or more senior people tends to swarm the incident. They suggest a network built on expertise and working relationships, with two filters: people you're comfortable asking (so you don't hesitate before pinging your VP) and people who actually have the bandwidth. Paging someone whose calendar is full just adds a body to the room and sends you off to find another.

Emily borrows an idea from a Blameless webinar guest: incident buddies, a first person you can always ask for a sanity check before escalating further. Being nervous to escalate is human, and the policy should account for it.

## Roles stop the paranoia that fills the room

The third fix is roles and checklists. Their core trio: an incident commander who drives towards resolution, a communications lead for internal and external updates, and a technical lead. Emily's point is that the roles answer the fear that brings people in, that something will fall through the cracks. If people can see communications, recording and the technical front are covered, they don't need to join.

Communication is where the room fills fastest, usually from management. Emily describes layers of managers dropping in with questions for the board and customers, putting pressure on engineers who are trying to focus. Their fix is proactive updates: automated messages to stakeholders when status changes, plus a way to send ad hoc updates to email, text or a status page, and different detail for people who need it now versus those who only need outcomes.

## Trust the process, then improve it

The closing section is about culture. Anyone in the channel should be able to mark a message as important so the commander can pull key findings into the timeline. Retros should ask whether the right team was added automatically and whether the right people got notified.

And people need the safety to stay out. On joining an incident just to learn how it ends: "That's not the best reason to actually be involved in an incident and be in the response room," Emily Arnott said at Conf42 Incident Management 2022. Trust that someone is recording it and a document will follow; and if someone panics and invites the whole dev team, treat it as a learning opportunity, not a reprimand.

## Who should watch

Teams writing their first severity matrix or escalation policy, and incident commanders tired of 40-person channels. It's short on hard data beyond the 10-to-15-minute figure, and long on habits you can adopt on Monday. For more, see [Kurt Andersen on the varieties of incident response](https://www.conf42.com/Incident_Management_2022_Kurt_Andersen_varieties_incident_response) at the same event, [Chinyere Chinekezi on incident response playbooks](https://www.conf42.com/Incident_Management_2024_Chinyere_Chinekezi_12_incident_playbooks_response) at Conf42 Incident Management 2024, and [Julie Gunderson on postmortems and blameless culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at Conf42 Chaos Engineering 2021.

[Watch Nick Mason and Emily Arnott's talk](https://www.conf42.com/Incident_Management_2022_Nick_Mason_Emily_Arnott_too_many_people) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From Blameless

Blameless builds an SRE platform covering incident response, communication and retrospectives.

- Blameless: [blameless.com](https://www.blameless.com/)
- [Blameless SRE blog](https://www.blameless.com/sre)
- [Blameless SRE community Slack](https://www.blameless.com/slack-community)

[Watch the talk on YouTube](https://youtu.be/6qBMikBwZ70).

## Watch the talk

[Too many people in the room?](https://www.conf42.com/Incident_Management_2022_Nick_Mason_Emily_Arnott_too_many_people) at Conf42 Incident Management 2022.
