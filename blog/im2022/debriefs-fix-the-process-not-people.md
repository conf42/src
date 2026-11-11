# The bug that shipped because main didn't mean production

Conf42 Blog, 2022-09-30. https://www.conf42.com/blog/im2022/debriefs-fix-the-process-not-people

In short: Amir Shaked (HUMAN) at Conf42 Incident Management 2022 on blameless debriefs that fix processes, not people, and the follow-up that makes them stick.

An engineer merges failing code to main late at night, planning to finish it tomorrow, confident it won't deploy. That same week a DevOps engineer had added a process that deploys the service whenever it auto-scales, and that night traffic spiked. At Conf42 Incident Management 2022, Amir Shaked, Senior VP R&D at HUMAN, uses that story to show why debriefs should ask what happened and what must change, never who did it, and how his team turned that into a culture.

HUMAN is the sponsor here, and Amir talks about its world only briefly: moving target defence against threat actors, where shipping changes fast is part of the product. The rest is a practical playbook for post-incident debriefs.

## Where did they start?

The goal was rapid deployment, zero downtime, and every mistake happening once but never twice. The starting point was minor changes in code or config breaking production, and instability from the underlying cloud. Both were worrying for a fast-growing system, where today's minor issue becomes tomorrow's catastrophe.

But the real blocker was fear of judgement. Every attempt to dig into an issue met pushback: why so many questions, don't you trust people? Amir's view is that people who feel judged underperform, and a team that's afraid can't learn. Hence his focus on process, summed up in the quote he leans on, that a bad system will beat a good person every time.

## What was the real root cause?

Back to the late-night merge. A customer reported odd behaviour, support couldn't work it out and paged engineering, who were in another time zone. They found and fixed the problem, went back to bed a little resentful, and moved on. Without a debrief, Amir says, similar issues are certain to come back.

The debrief could have stopped at why the engineer merged buggy code or why the DevOps engineer added auto-deploy. Both miss the point. The flaw was that merging to main didn't signal deployment to anyone. The fix was aligning every engineer on one rule: main always equals production, whether or not it's deployed automatically.

## The four steps and the questions

His process:

1. **The incident and the immediate fix.** A mature team opens incidents even for supposedly minor things, just to learn from them.
2. **The debrief, 24 to 72 hours later**, depending on how much sleep people got and whether a weekend got in the way.
3. **A checkpoint two weeks after the debrief** to review the action items.
4. **Follow-up** that the changes were actually implemented.

In the debrief he asks for a detailed timeline from the moment the problem actually started (the merge, not the customer's complaint), and the full impact in cost, customers and complaints, so everyone understands why the digging matters. Then two questions with explicit targets: did we identify the issue in under five minutes, and did we fix it in under an hour? Any no leads to what needs to change or be built so the answer becomes yes.

"Now, this part, while seemingly simple, led to a drastic culture change over time," Amir Shaked said at Conf42 Incident Management 2022. Whoever caused the incident is irrelevant; tomorrow it could be someone else.

## What got in the way?

- **Lack of trust.** People suspected a new manager's process was the blame game in a new format. Doing it properly and consistently fixes that.
- **Blame in the room.** When someone says another person is at fault, stop that line and steer back to the questions.
- **Action items nobody followed up.** Every debrief ticket in Jira got a debrief label, reviewed monthly alongside the regular checkpoints.
- **Secrecy.** Every debrief was published widely inside the company, with what happened and what would change.
- **Looking too narrowly.** Don't stop at the one repository that broke; ask whether every repository has the same problem.

His four rules for running the meeting: avoid blame, go easy on the whys (five whys about a person's choices can feel like judgement), be consistent, and keep calm.

## Lessons worth copying

His list of recurring action items reads like a reliability starter kit: assume humans make mistakes and fix the process; gradual rollout is a great tool but not a silver bullet; define crisis-mode processes before you need them; use feature flags, because flipping config on thousands of containers beats redeploying thousands of servers; split a replacement into an add and a later remove instead of one dual change; look for the 10x breaking point; and treat config as code, with PRs, reviews and rollback.

## Who should watch

Engineering managers introducing debriefs to a sceptical team, and anyone whose postmortems end with an action item nobody owns. There's no product content, and the lessons list alone justifies the time. Pair it with [Ramon Medrano Llamas on postmortem culture at Google](https://www.conf42.com/Site_Reliability_Engineering_2022_Ramon_Medrano_Llamas_postmortem_culture_google) at Conf42 SRE 2022, [Pranjal Deo on blameless postmortem culture](https://www.conf42.com/Chaos_Engineering_2021_Pranjal_Deo_postmortem_culture_blameless) at Conf42 Chaos Engineering 2021, and [Yury Nino on learning from failure](https://www.conf42.com/Chaos_Engineering_2020_Yury_Nino_postmortem_culture) at Conf42 Chaos Engineering 2020.

[Watch Amir Shaked's talk](https://www.conf42.com/Incident_Management_2022_Amir_Shaked_create_learning_culture) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From HUMAN

HUMAN works on defending against bots and threat actors, the moving-target world Amir describes, where fast, safe deployment is part of the product.

- HUMAN: [humansecurity.com](https://www.humansecurity.com/)

[Watch the talk on YouTube](https://youtu.be/bo6-aI37Wq8).

## Watch the talk

[Create a learning culture](https://www.conf42.com/Incident_Management_2022_Amir_Shaked_create_learning_culture) at Conf42 Incident Management 2022.
