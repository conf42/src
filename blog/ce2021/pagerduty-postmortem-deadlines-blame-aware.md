# PagerDuty gives a sev-1 postmortem three business days

Conf42 Blog, 2021-02-24. https://www.conf42.com/blog/ce2021/pagerduty-postmortem-deadlines-blame-aware

In short: Julie Gunderson (PagerDuty) at Conf42 Chaos Engineering 2021 on blameless postmortems - owners, deadlines, cognitive biases and action items that get done

A postmortem that waits two weeks for everyone's calendar is a postmortem nobody learns from. At Conf42 Chaos Engineering 2021, [Julie Gunderson](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture), DevOps advocate at PagerDuty, walked through how PagerDuty runs postmortems, with concrete deadlines and roles, and spent as much time on the human biases that turn incident reviews into blame sessions.

## When should you write one, and how fast?

After every major incident, and also whenever the incident response process was triggered, even if the severity turned out lower, it was a false alarm or it recovered on its own. A false trigger is worth understanding too: tuning that monitoring prevents alert fatigue later.

Completing the postmortem is treated as the last step of incident response and takes priority over planned work. PagerDuty's internal policy is three business days for a sev 1 and five business days for a sev 2, and people are expected to move their calendars for the meeting. At the end of the incident call, the incident commander names one responder to own the postmortem, to avoid the bystander effect. The owner coordinates; they are not the person who caused anything, and they do not write it alone.

## Why is blameless so hard?

Gunderson draws on Sidney Dekker's two views of human error: the old view, where bad apples cause failures, and the new view, where human error is a symptom of a system problem. Blame makes engineers quiet, and silence increases mean time to acknowledge and resolve. Julie Gunderson said at Conf42 Chaos Engineering 2021: "a blameless postmortem stays focused on how a mistake was made instead of who made the mistake."

She also cites J. Paul Reed's argument that fully blameless is a myth, since the urge to blame is wired in, so the practical goal is to be blame aware. Drawing on Lindsay Holmwood, she lists the biases to watch: fundamental attribution error (blaming character, not circumstances), confirmation bias (counter it with a devil's advocate or an outsider asking naive questions), hindsight bias (build the timeline forward from before the incident) and negativity bias (record what went well too).

Practical habits: ask what and how, not who and why, following John Allspaw's case for how questions. Abstract human actions to an unspecified responder. Bring in diverse perspectives, an intern included.

## Selling it to leadership and the team

Leadership must commit that nobody is reprimanded after an incident, and the pitch is business value: people who speak up early shorten incidents. Do not blame managers for blaming. Then get the same commitment from the engineers, because the instinct to blame is not unique to management. She ties this to psychological safety as defined by Amy Edmondson, to Google's finding that it was the most critical factor for team success, and to the DORA State of DevOps report.

Start small, as with blast radius: one team, minor incidents first, where the stakes and the pressure to scapegoat are lower. PagerDuty keeps a public guide at postmortems.pagerduty.com.

## Sharing and action items

PagerDuty puts every postmortem meeting on a company-wide shared calendar that anyone can join, emails finished postmortems to a list covering engineering, product, support and incident commanders, and keeps a community of experienced writers who review drafts posted in Slack at least 24 hours before the meeting.

Action items need owners, and engineering leadership makes system ownership clear. Policy: high-priority items from a sev 1 done within 15 days, from a sev 2 within 30. Bringing product and engineering managers into the meeting helps, because they prioritise the work. Items should be actionable, specific and bounded, as Google's SRE guidance puts it: not "investigate monitoring" but adding alerting for every case where the service returns more than 1% errors.

## Writing the document

The meeting is 30 minutes to an hour, with the incident commander, service owners, key engineers, managers and customer liaisons. The timeline sticks to facts, each with a link to the graph, log search or tweet behind it. Impact is described by duration, customers affected, support contacts and a business metric; for PagerDuty that means delayed event ingestion or slow notifications. Analysis looks for contributing factors, citing Richard Cook's How Complex Systems Fail: there is no single root cause. The external version is a sanitised summary. And one rule for that external text: "don't use the word outage unless it really was an outage".

A trained facilitator who does not join the discussion keeps the meeting on track; PagerDuty has a guild for that. She ends by suggesting postmortems after chaos experiments and mock incidents too.

## Who should watch

Anyone setting up or repairing an incident review process. It is dense and practical, close to a workshop in a talk slot.

Related Conf42 talks:

- Pranjal Deo on [postmortem culture](https://www.conf42.com/Chaos_Engineering_2021_Pranjal_Deo_postmortem_culture_blameless) at the same event.
- Ramon Medrano Llamas on [postmortem culture at Google](https://www.conf42.com/Site_Reliability_Engineering_2022_Ramon_Medrano_Llamas_postmortem_culture_google), Conf42 SRE 2022.
- Fabricio Buzeto on [postmortems beyond failure](https://www.conf42.com/Chaos_Engineering_2021_Fabricio_Buzeto_dia_de_los_muertos_postmortems), Conf42 Chaos Engineering 2021.

## From PagerDuty

PagerDuty makes an incident response platform and publishes the guides Gunderson referenced in the talk.

- [PagerDuty](https://www.pagerduty.com/)
- [PagerDuty postmortem guide](https://postmortems.pagerduty.com/)
- [PagerDuty incident response guide](https://response.pagerduty.com/)

[Watch the talk on YouTube](https://youtu.be/Gdm96CtmrL0).

## Watch the talk

[Postmortems, Continuous Learning and Enabling Blameless Culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) at Conf42 Chaos Engineering 2021.
