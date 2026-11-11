# A postmortem without action items is a wasted hour

Conf42 Blog, 2023-10-20. https://www.conf42.com/im2023/postmortems-premortems-team-resilience

In short: Dor Amram (SimilarWeb) at Conf42 Incident Management 2023 on building teams that absorb an incident, handle it, and come out of it better.

You know the next bug is coming; you just don't know where, when or how bad. At Conf42 Incident Management 2023, Dor Amram, Data / Server Engineer at SimilarWeb, argued that the real question is how resilient your team is when it lands, and answered it with three smaller ones: can the team absorb the shock, respond to it, and evolve from it?

This is a people-and-process talk, not a tooling one. There's no product in it, no dashboard and no war story with numbers; it's nine years of team experience distilled into a checklist. The best bits are the ones teams nod along to and then don't do.

## Can your team absorb the shock?

Dor calls the first layer growth culture, and he splits it into five habits.

**Focus on learning.** Courses and meetups are the obvious part. The less obvious part: start a guild if your company doesn't have one, actually read your own system's documentation (its weak spots are where the next storm will hit), run design reviews before implementation rather than after, and read tests as the original author's statement of intent instead of just checking they pass. Then put it in the diary. "If it's not in your calendar, it does not exist," Dor Amram said at Conf42 Incident Management 2023.

**Continuous communication.** Open communication (say the feature is wrong, say the solution is too complex), clear goals that you and your manager would describe the same way, transparency about the bad stuff, including telling the other team about your breakage before they find it, and regular check-ins that happen more than once a year.

**A supportive environment.** Collaborate, give people the time and tools they need, and forego blame: the useful questions are what we learn and how we stop it recurring, not who did it.

**Space for experimentation.** Something working doesn't mean it can't work better, with the standing caveat about premature optimisation. Give people time to investigate properly rather than ship something that just makes the manager happy.

**Empower champions.** Celebrate wins as loudly as you dissect failures. Dor's two concrete ideas are worth stealing: task pitching, where each sprint keeps a slot for work the engineers propose themselves (the scary module nobody touches, the algorithm someone wanted to try), and handing initiatives such as hackathons to junior people to lead.

## Can it handle the incident?

The response section is a compact, familiar sequence: identify the incident, activate the response team (from your team or others), contain it so the damage doesn't spread (shift traffic, stop using corrupted data), investigate the root cause, then restore, reproduce and verify the fix, and deploy.

The step Dor leans on hardest runs alongside all of them: communicate with stakeholders while the incident is still open, not after it's solved hours later. People act on what you tell them, and finding out late is how you lose their trust.

## Can it evolve from it?

Here the talk gets opinionated. Every postmortem needs action items, and every set of action items needs a follow-up meeting scheduled before you leave the room. Skip either and, in Dor's words, you've wasted an hour of your team.

Then flip the cycle. Instead of waiting for the next incident and running a postmortem, run a premortem on the parts of the system you already know are weak or new, plan the fix and do it before anything breaks. "Instead of waiting for the storm to come to us, let us come to the storm, but better prepared," Dor said.

The rest of the evolve step is resilience work: upgrade the code you know is fragile, invest in documentation, tests and alerting so you hear about problems before a customer calls, write playbooks so a stressed responder doesn't miss a step, and share what you learned so other teams don't fall into the same pit.

## Who should watch

Team leads and engineers who already run incidents but whose postmortems have quietly turned into rituals. If you want metrics, tooling or a case study, look elsewhere; this is a culture checklist, delivered with enthusiasm and a Churchill quote.

Good pairings from the Conf42 archive: [Lisa Karlin Curtis on using incidents to level up your teams](https://www.conf42.com/Incident_Management_2022_Lisa_Karlin_Curtis_incidents_levelup_your_teams), [Amir Shaked on creating a learning culture](https://www.conf42.com/Incident_Management_2022_Amir_Shaked_create_learning_culture), and [Laurent Parenteau on premortems](https://www.conf42.com/Platform_Engineering_2024_Laurent_Parenteau_hack_premortem_success) for the proactive half.

[Watch Dor Amram's talk](https://www.conf42.com/Incident_Management_2023_Dor_Amram_rise_crisis_growth_improvement) from [Conf42 Incident Management 2023](https://www.conf42.com/im2023).

## From Similarweb

Dor's talk draws on his team experience as an engineer at Similarweb, which supported Conf42 Incident Management 2023.

- Similarweb: [similarweb.com](https://www.similarweb.com/)

[Watch the talk on YouTube](https://youtu.be/V1IIQuBT4_0).

## Watch the talk

[A Team That Rises From Crisis: Leveraging Incidents for Growth and Improvement](https://www.conf42.com/Incident_Management_2023_Dor_Amram_rise_crisis_growth_improvement) at Conf42 Incident Management 2023.
