# Somebody has to get fired, right? Answering the blameful executive

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/someone-has-to-get-fired-right

In short: Emily Arnott and Christina Tan (Blameless) at Conf42 SRE 2021 on answering an executive who demands blame, and when accountability is due.

Blameless culture is easy to defend at an SRE meetup and much harder when a Fortune 500 executive asks you, point blank, whether somebody still has to get fired. That question is where Emily Arnott and Christina Tan of Blameless started their talk at [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021). Their answer: treat the blameful leader as someone with the same goals and different assumptions, surface those assumptions with questions once things are calm, and keep performance management a separate process from incident response.

## Why should a business leader care about blamelessness?

They make the business case first, because that is the language executives speak. Studies agree developer velocity drives business value, psychological safety drives velocity, and blameless culture drives psychological safety. Remove the last link and the first one weakens.

## The dark and stormy night

Their running example: an engineer making changes in what they think is the testing admin panel realises it is production, a major incident follows, and an executive walks in asking what happened and who is responsible. The engineers hear blame. Christina points to the fundamental attribution error: when we are hurt we assume bad intent, when we hurt others we call it an accident. Looked at again, the leader wants exactly what the engineers want: fix the incident, prevent a repeat, restore stakeholder trust. Both sides are tense and afraid of the consequences. That shared ground is the bridge.

## Which assumptions make blame look reasonable?

They sort the leader's likely assumptions into three areas and pair each with calm-time questions:

- **The incident**: it should never have happened, and punishment deters others. Ask whether 100% reliability is possible or worth its cost, and how to trade prevention against preparing to respond with limited engineering capacity.
- **The engineer**: a skilled engineer wouldn't do this, remove the bad apple and the problem goes. Ask whether incidents have causes deeper than individuals. They cite an emergency physician at Stanford on missed heart attacks: trained people err when interrupted or carrying other context. Also, hiring someone new costs far more than training the team.
- **Stakeholders**: they want to see someone fired, or a sense of fairness. Ask whether there are other ways to rebuild trust than retribution, such as a credible long-term plan, and remember internal stakeholders such as customer success, who own churn.

They borrow Dave Rensin's line that complex systems fail inevitably, and Aristotle's ethos, pathos and logos: with a leader likely to disagree, lead with credibility, then logic, and save the emotional appeal for last.

## What do you say in the moment?

Be direct and short, find common ground, state the shared goals, and say what happens next. In their role play the reply runs roughly: it could have been anyone, give the team space to resolve this, we take full ownership of contributing-factor analysis and follow-ups over the next two weeks. The reason for asking for space is practical, since engineers in fight-or-flight mode solve problems badly. Emily, playing the executive, explained the other side afterwards. "I tried to really embody the feeling that this was a big deal and that I had the entire company perhaps riding on resolving this quickly," Emily Arnott said at Conf42 SRE 2021.

The follow-up investigation then asks the useful questions. Why do the production and testing panels look so alike? Should production carry a big banner? Should one person alone be able to make such changes, and should fewer engineers have that access? Every answer is a systemic fix that outlives firing someone. Incidents also feed planning: headcount, runbooks, production readiness checklists, and sometimes uncomfortable findings about leadership and team structure.

## So is anyone ever accountable?

Sometimes, yes. Their prerequisites: were the expectations of the role clear, realistic and documented; was the mistake a lack of skill rather than of good intentions or honest effort; has performance feedback been shared consistently; and were all other contributing factors accounted for? That is performance management, and incidents are no substitute for it. Accountability, in their framing, faces forward: the accountable team owns improving reliability from the incident onwards, without cutting short the analysis. The story is true, they add: the real engineer was not punished, and the team made test and production unmistakably different.

## Who should watch

SRE leads and engineering managers who report incidents upwards, and anyone who has watched a postmortem turn into a hunt. Pair it with:

- [Julie Gunderson on postmortems, continuous learning and blameless culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at Conf42 Chaos Engineering 2021.
- [Robert Ross on pragmatic incident response](https://www.conf42.com/Site_Reliability_Engineering_2021_Robert_Ross_pragmatic_incident_response) at Conf42 SRE 2021.
- [Matty Stratton on the psychology of chaos engineering](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology) at Conf42 Chaos Engineering 2020.

[Watch Emily Arnott and Christina Tan's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Emily_Arnott_Christina_Tan_elephant_in_the_room) from Conf42 SRE 2021.

## From Blameless

Blameless builds an SRE platform around incident response and learning from incidents.

- [Blameless website](https://www.blameless.com/)
- [Blameless SRE blog](https://www.blameless.com/sre)
- [Blameless SRE community Slack](https://www.blameless.com/slack-community)
- [Blameless on Conf42](https://www.conf42.com/blameless)

[Watch the talk on YouTube](https://youtu.be/uAsYYSGyx8c).

## Watch the talk

[Elephant in the Blameless War Room - Accountability](https://www.conf42.com/Site_Reliability_Engineering_2021_Emily_Arnott_Christina_Tan_elephant_in_the_room) at Conf42 Site Reliability Engineering 2021.
