# The database risk someone saw but never said out loud

Conf42 Blog, 2026-05-26, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/database-risk-visibility-gap

In short: Sheena Yap Chan at Conf42 Database DevOps 2026 on the VISIBLE framework for getting database risks to decision-makers before they get expensive.

Most postmortems ask what broke. Sheena Yap Chan wants them to ask what stayed hidden too long. At Conf42 Database DevOps 2026, the founder of The Tao of Self-Confidence argues that the most expensive database risks are often already known to someone on the team; they just never reach the people who can act in time.

This is the non-technical talk of the event, and it says so. There's no SQL in it. It's about the human path a signal takes from the DBA who spots it to the leader who signs off on the fix.

## The gap sits between seeing and deciding

Sheena defines the visibility gap as the distance between what the technical team sees and what decision-makers understood in time to act. Risks hide in incident response, migration planning, performance conversations, reliability reviews, postmortems and handoffs. She compares it to a child hiding a mistake from their parents: the longer it stays hidden, the bigger and more expensive it gets.

Her reframe is that visibility isn't about attention, it's about protection, for you, the organisation and the customer. And confidence isn't about being loud; it's about saying what needs to be said when it needs to be said.

## Three ways a signal dies

The most practical slide lists three failure modes:

1. **Seen but not shared.** Someone noticed, assumed someone else had it, or was afraid to speak.
2. **Shared but not understood.** The concern was raised in language the listener couldn't parse.
3. **Understood but not acted on.** No owner, no channel, no spotlight.

Anyone who has read an incident timeline with a message from three days earlier saying "this looks odd" will recognise all three.

## VISIBLE, letter by letter

Her framework spells out seven pillars. Voice: can people raise concerns early, and if speaking up is hard, are there other routes such as one-to-ones or anonymous channels? Identity: do people see themselves as part of reliability? Spotlight: what deserves attention right now? Inner work: what keeps people silent? She calls this 80% of the work and draws on her own upbringing, where she was taught to stay in the background. Belief: do people think raising a concern will change anything? If the first one went nowhere, there won't be a second. Leverage: teams working in silos, one person doing everything until burnout. Elevation: turning a technical concern into something a decision can be made from.

## Templates you can steal

The concrete takeaways are phrasing. For migrations, replace "we should be fine" with the risks, the impact and the decision needed. During incidents, people need clear updates, next steps and owners, not more noise. And a five-line visibility statement for any escalation: here is what we are seeing, why it matters, the possible impact, the options, and the decision we need.

For leaders she offers four questions: what are we not seeing yet, what are people afraid to say, where are signals getting stuck, and who needs this information sooner?

## Who should watch

Team leads, incident commanders and the engineer who always notices the slow query first but doesn't like to make a fuss. Engineers after technical depth should skip it; those whose last outage had a Slack message nobody read should not.

## Related Conf42 talks

- [Postmortems, Continuous Learning and Enabling Blameless Culture](https://www.conf42.com/Chaos_Engineering_2021_Julie_Gunderson_postmortem_continuous_learning_blameless_culture) by Julie Gunderson, the postmortem side of speaking up.
- [People-Powered Security: The Role of Soft Skills in a DevSecOps Culture](https://www.conf42.com/DevSecOps_2024_Victor_Onyenagubom_security_soft_skills) by Victor Onyenagubom, the same argument for security teams.
- [How to change culture, not just tools](https://www.conf42.com/DevOps_2023_Christopher_Harrison_change_culture__not_just_tools) by Christopher Harrison, for when the problem is the organisation.

[Watch Sheena Yap Chan's talk](https://www.conf42.com/Database_DevOps_2026_Sheena_Yap_Chan_incident_reliability_platform)

[Watch the talk on YouTube](https://youtu.be/r7L5k3L86D0).

## Watch the talk

[When Database Risk Stays Hidden: Closing the Visibility Gap in Data Operations](https://www.conf42.com/Database_DevOps_2026_Sheena_Yap_Chan_incident_reliability_platform) at Conf42 Database DevOps 2026.
