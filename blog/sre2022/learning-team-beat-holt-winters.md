# When Holt-Winters couldn't answer the CEO, a learning team could

Conf42 Blog, 2022-06-08. https://www.conf42.com/blog/sre2022/learning-team-beat-holt-winters

In short: Kurt Andersen (Blameless) at Conf42 Site Reliability Engineering 2022 on how a LinkedIn learning team answered the CEO's metric questions years before tooling could

Picture a CEO with a gift for pattern detection, an hourly report of key business metrics, and an email at 5am saying some numbers don't look right. At Conf42 Site Reliability Engineering 2022, Kurt Andersen, SRE Architect at [Blameless](https://www.blameless.com/), told how a team at LinkedIn stopped scrambling over those emails. The fix wasn't a better model. It was a learning team that calibrated its own intuition until it could answer the CEO before he asked.

It's a short, story-driven case study, and the story is the point: the tooling that eventually helped took three or four years to arrive, and the people had to cope in the meantime.

## Why were these questions so hard to answer?

The key business metrics report covered the last 24 hours for page views and a handful of crucial site activities, compared week over week. It lagged real time by two to four hours, after cleanup jobs had run. Engineering looked at something else entirely: InGraphs dashboards at one-minute resolution, about five minutes behind real time.

The questions also landed at the worst moment. The on-call teams sat about 12 hours apart, so the CEO's email tended to arrive right at shift change: the outgoing team wanted to go home, the incoming team had no context. And any dip could come from a dozen places, from an email send that went out late to a site change that shifted page latency.

## More data was the engineer's first answer, and it didn't work

The first instinct was to analyse harder. The team tried Holt-Winters seasonality, which can model several periodicities at once, hoping a sharper prediction would make the anomaly obvious. The variations stayed too extreme to explain what had gone wrong. Kurt is candid that getting more data and predicting in more detail simply didn't pay off. Too many systems fed each metric for any single forecast to say which one had misbehaved.

## Calibrating intuition, one week at a time

So they stepped back and got key practitioners from both geographies, plus an overseeing team, into a weekly meeting. Each week they went through the previous week's data: what did we see, what did we miss, and what didn't we know that would have let us answer in the moment? Kurt frames it as building common ground in a joint cognitive system.

What they learned was mostly about the world, not the servers. A US-only holiday such as Memorial Day changes how a professional network is used in the US while Canada and Europe behave normally. Sporting events showed up too: a colleague's analysis of the Super Bowl (with the San Jose Sharks playing the same day) found clear anomalies at key points in the game, and the World Cup, in football or cricket, hit different countries differently.

## Dual controls, then solo flights

The handover followed a flight-training model. First an experienced engineer answered the CEO while learners watched in real time. Then a first-line engineer drafted the answer and the experienced engineer reviewed it before sending. Then learners led and got offline feedback. Eventually every on-call engineer was, in Kurt's phrase, flight certified, and could anticipate questions: a holiday in India today, so traffic from India will look anomalous.

The calibration meetings stepped down from weekly to every other week, then monthly, then stopped. Automation came later: holiday data from Time and Date, and LinkedIn's ThirdEye, since open-sourced, which slices an anomaly by dimensions such as country or platform.

## Where does the learning team model come from?

Kurt maps the work onto the ASREDS learning loop: align on a joint purpose, sense by gathering insights from everyone, respond with plans for next time, experiment (an anomaly came along within a couple of days), distil the plans, and share them with the wider on-call group. He also ties learning teams to four of the five characteristics of high reliability organisations, including awareness of the imminence of failure and respect for front-line expertise.

"If it can't answer the question because of too much ambiguity, trust in your people. They have encountered it, they have dealt with it," Kurt Andersen said at Conf42 Site Reliability Engineering 2022.

## Who should watch

SRE leads who get questions from executives that no dashboard answers, and anyone who suspects their next tooling project will take longer than the problem can wait. There is no demo; it's a 20-minute argument for investing in people while the automation catches up.

For more on learning from operations, pair it with [Postmortem culture at Google](https://www.conf42.com/Site_Reliability_Engineering_2022_Ramon_Medrano_Llamas_postmortem_culture_google) by Ramon Medrano Llamas at the same event, Julie Gunderson on [postmortems and continuous learning](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture), and Lisa Karlin Curtis on [how incidents level up teams](https://www.conf42.com/Site_Reliability_Engineering_2022_Lisa_Karlin_Curtis_incidents_levelup_teams).

[Watch Kurt Andersen's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Kurt_Andersen_learning_team_casestudy) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From Blameless

Blameless builds an SRE platform covering incident response and the learning that follows it, which is where Kurt's case study sits.

- Blameless: [blameless.com](https://www.blameless.com/)
- [How to Become a Master at Incident Command](https://www.blameless.com/incident-response/best-practices-pragmatic-incident-command)
- [Join the Blameless SRE community Slack](https://www.blameless.com/slack-community)
- [Try Blameless](https://www.blameless.com/try-now)

[Watch the talk on YouTube](https://youtu.be/jz6ZXseTZzU).

## Watch the talk

[Implementing a Learning Team: A real-world case-study](https://www.conf42.com/Site_Reliability_Engineering_2022_Kurt_Andersen_learning_team_casestudy) at Conf42 Site Reliability Engineering 2022.
