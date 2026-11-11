# Buying a treadmill doesn't make you a runner, or a DevOps team

Conf42 Blog, 2023-01-27. https://www.conf42.com/devops2023/buying-a-treadmill-devops-culture

In short: Christopher Harrison (GitHub) at Conf42 DevOps 2023 on changing team culture, not just tools - ask why, pick champions and a pilot, add habits

Every January thousands of people buy treadmills, and by February most of them hold laundry. Christopher Harrison, Senior Enterprise Advocate at [GitHub](https://github.com/enterprise), built his Conf42 DevOps 2023 talk on that image: a new CI/CD system or project tracker won't change how a team works on its own, and the roadmap he offers for changing culture is three steps long - ask the right questions, establish a plan, then implement and review.

It is a short, tool-free talk from someone who sells tools for a living, which is part of its charm.

## Why do new tools end up collecting dust?

Harrison took part in roundtables at GitHub Universe with DevOps practitioners, leaders and C-level folks, and one theme ran through every conversation: the most common blocker to new techniques and patterns was team culture. Money went into tools, and nobody used them. He is careful not to dismiss tools; the right one does make a difference, but only if it gets used.

## What are the right questions?

He became a runner about ten years earlier, he says, not because he wanted to run but because he was unhappy with his fitness. Running was the how. Teams need the same separation, through three questions:

- **Why do you want to change?** Not automating CI/CD for its own sake, but the outcome behind it. His running example is a mobile app whose real problem is that customer feedback and bug fixes take too long to reach users. The goal is responsiveness.
- **What are the challenges?** Only now look at what is missing: is the CI/CD pipeline actually the barrier?
- **Who is key to success?** Leadership matters, but so do individual developers, mentors and, crucially, the strongly opinionated ones.

He recalls helping a team move from waterfall to agile under a manager who kept saying he was all for it while quietly siding with a couple of developers who weren't. The project was doomed from the start. Win over the curmudgeons, his advice goes, and they become your champions.

"If we can get everybody on board, the rest kind of doesn't matter," Christopher Harrison said at Conf42 DevOps 2023.

## What does the plan look like?

- **Clearly define success**, measurably: for the mobile app, the time from a piece of feedback to it reaching the deployed application.
- **Identify teams and champions**, and consider forming new teams. People who keep doing the same work keep doing it the same way; a new team on a new project leaves the old habits behind, and mixing people from different parts of the organisation spreads lessons around.
- **Select a pilot project** that is just right, Goldilocks style: meaningful but not overwhelming. A shared internal library or service (auth, say) used by many applications is ideal, as is a new build such as an iOS app next to an existing Android one.

## Why add behaviours instead of changing them?

This is the most useful idea in the talk. Large pull requests are hard to review, hard to roll back and touch too many components, but ordering a team to make smaller PRs fights ingrained habits. Instead, add behaviours: code reviews if there are none, linting, automated code quality checks, unit tests. Small PRs make all of those easier, so the team drifts towards them on its own.

In the running version, he didn't give up burgers on day one; he laced up his shoes. Skipping the burger came later, because the morning run went better without it.

Then document successes and failures, learn why each happened, and grow to the next project and the next team. It is not change from the grassroots only, he adds when people push back; managers and developers both need to be on board.

Above all, he says, expect it to take time and expect setbacks. A clearly defined goal is what lets you bring a stalled effort back to the beginning: the questions.

## Who should watch

Engineering managers and team leads about to roll out a new platform or process, and anyone who has watched a tool purchase fail to move a single metric. It runs well under half an hour.

## Related Conf42 talks

- Zach Gardner on [why digital transformations fail and how to succeed](https://www.conf42.com/Cloud_Native_2023_Zach_Gardner_digital_transformation_fails__how_to_succeed) at Conf42 Cloud Native 2023.
- Tomasz Manugiewicz on [trust-driven development in a DevOps transformation](https://www.conf42.com/Chaos_Engineering_2023_Tomasz_Manugiewicz_trust_driven_development_devops_transformation_practice) at Conf42 Chaos Engineering 2023.
- Caio Medeiros Pinto on [smooth platform engineering adoption](https://www.conf42.com/DevOps_2024_Caio_Medeiros_Pinto_smooth_platform_engineering_adoption) at Conf42 DevOps 2024.

[Watch Christopher Harrison's talk](https://www.conf42.com/DevOps_2023_Christopher_Harrison_change_culture__not_just_tools)

## From GitHub

GitHub hosts code and the collaboration around it, from pull requests and code review to Actions and security tooling, with an enterprise offering for larger organisations.

- [GitHub Enterprise](https://github.com/enterprise)

[Watch the talk on YouTube](https://youtu.be/h_62AqF5OOA).

## Watch the talk

[How to change culture, not just tools](https://www.conf42.com/DevOps_2023_Christopher_Harrison_change_culture__not_just_tools) at Conf42 DevOps 2023.
