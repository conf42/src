# Chaos engineering is a people problem with a pager attached

Conf42 Blog, 2020-01-23. https://www.conf42.com/blog/ce2020/failure-fridays-remember-the-humans

In short: Matty Stratton (PagerDuty) at Conf42 Chaos Engineering 2020 on the human side of chaos engineering, from careful words to Failure Fridays

The hard part of chaos engineering is rarely the fault injection. It is the risk officer who hears a pitch for breaking production and ends the meeting. Matty Stratton, DevOps Advocate at PagerDuty, closed Conf42 Chaos Engineering 2020 with a talk on the psychology of the practice: how the words you pick decide whether you get to run an experiment at all, why a game day should lower stress rather than simulate it, and why every percentage on your dashboard is a crowd of actual people.

As the last speaker of the day, Stratton leaned into it, tying back to Adrian Hornsby and Russ Miles from earlier sessions and admitting that most of his level-setting had already been done for him. What remains is the part most chaos talks skip: the humans on both ends of the experiment.

## Why does perception matter more than being right?

Because the goal inside a company is to change how it works, and you can't do that with people who misunderstand you. "It's not about being right. That's what Twitter is for," Matty Stratton said at Conf42 Chaos Engineering 2020. The joke everyone makes about chaos (isn't all engineering chaotic?) annoys him, partly because it isn't funny, but mostly because it reinforces the idea that the practice is about breaking things. It is about experiments: a hypothesis that the system will keep working under a given condition. If your hypothesis is that everything will fall over, he suggests running it in a lower environment, or not at all.

He also warns against expert amnesia. People who sit through a whole day of chaos talks forget that colleagues are still at step one, and the first principles need repeating.

## Which words should you be picky about?

Stratton separates words that change behaviour from words that only win pedantry points. From his Chef days: calling a recipe a script nudges people towards step-by-step thinking, so he corrected it. Postmortem versus post-incident review? Rename it if you like, but the name alone doesn't change how you run it. Root cause is the one he does push on, because it makes people look for a single cause in a complex system that doesn't have one.

The same logic applies to selling chaos engineering. People are wired for risk aversion, and many colleagues judge everything by how much risk it adds. Pitch it as more risk and the conversation is over. With management, accuracy matters less than access: if a CFO-friendly name gets you into the room, use it. Stratton offers no single replacement term, because the right one depends on your organisation.

## How does PagerDuty run Failure Fridays?

In the middle of the business day, at lunchtime Pacific time, because there is no good time for PagerDuty to be down and the most people are in the office then. Each one runs like a real incident, with incident response started as part of the experiment. Two habits stood out:

- Monitoring is treated as live, because the impact on production is real. In his words, "use your monitoring like it's for real."
- Anyone who wants to be an incident commander at PagerDuty must have run a Failure Friday before going on call in that role.

He is firm that a game day isn't stress training. "Your people don't need training and practice of being under stress. They get plenty of that already," he said. The value is going through the motions in a low-stress setting, where the team knows which systems were touched.

## What about the people outside the team?

He asked the audience how they feel about Netflix running chaos in production (fine) and about their bank doing it (less fine), and points out that blast radius is what makes the difference. His informal Twitter polls, with the caveat that they are not scientific at all, found most people reassured when a service they use practises chaos engineering, but noticeably more uneasy or cynical about doing it on their own team. Understanding flips that: teams who know what an experiment does gain trust in the system and make changes more comfortably.

Chaos also pairs with learning from incidents. If a postmortem exists only to write down a root cause, reviewing a chaos experiment is pointless; you already know you turned the thing off. If the review is about learning, it fits.

## The three rules to take home

- Know your stop conditions, tied to business metrics such as average cart size, not a database's memory use.
- This is not about stressing your people. Be transparent: "Never surprise anybody with your chaos experiment."
- Remember the humans. A tenth of a percent of users can be 10,000 people who just had a bad hour.

## Who should watch

Engineers who already believe in chaos engineering and now have to convince a manager, a risk team or their own colleagues. It is light on tooling and heavy on persuasion and culture, delivered with jokes about vanity licence plates and sticker engineering. Pair it with [Adrian Hornsby on getting out of the starting blocks](https://www.conf42.com/Chaos_Engineering_2020_Adrian_Hornsby_getting_out_of_the_starting_blocks) from the same day, [Yury Niño on postmortem culture](https://www.conf42.com/Chaos_Engineering_2020_Yury_Nino_postmortem_culture), and Stratton's PagerDuty colleague [Mandi Walls on game days](https://www.conf42.com/Incident_Management_2022_Mandi_Walls_game_days_chaos_engineering).

[Watch Matty Stratton's talk](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology)

## From PagerDuty

- [PagerDuty](https://www.pagerduty.com/): incident response and on-call platform.

[Watch the talk on YouTube](https://youtu.be/QbcrJKjWQGE).

## Watch the talk

[Psychology of Chaos Engineering](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology) at Conf42 Chaos Engineering 2020.
