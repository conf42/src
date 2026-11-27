# No QA team? Borrow quality management from the factory floor

Conf42 Blog, 2021-06-23. https://www.conf42.com/blog/golang2021/quality-without-a-qa-team-tqm

In short: Dana Scheider (Envato) at Conf42 Golang 2021 on running software quality without dedicated QA staff, using Total Quality Management ideas

When there's no QA department to throw code over the fence to, quality has to come from somewhere else. At Conf42 Golang 2021, Dana Scheider, Senior Software Engineer at Envato, argues it should come from everyone, and that manufacturing worked out how decades ago: Total Quality Management (TQM). The talk then gets very practical about what that means for a dev team's code review, pull requests and testing.

Fair warning for the Go track: there's no Go in it. It's a process and culture talk that applies to any team shipping software.

## What does quality mean if bugs are only one part?

Dana's working definition is the suitability of a product for its intended purpose, judged by the customer. That widens quality beyond freedom from defects to functionality, performance, UX and security. Traditional QA, in this framing, arrives late, doesn't shape the product's definition or design, and mostly hunts bugs and edge cases. It also carries training and experience most developers don't have, which has to be passed on if developers are going to take over the work.

Dana built a quality process at Envato and only afterwards noticed how much it had in common with TQM, the philosophy the talk credits to management consultant W. Edwards Deming in the 1950s and to Japan's manufacturing strength.

## The TQM ideas that carry over to software

Four principles do most of the work:

- **Customer focus**, from the very start: are we building the right product, the right way, and does it serve what customers need? The cautionary tale is the US railroads, which saw their business as running trains on tracks rather than moving people and goods from A to B, and lost out to trucks and planes.
- **Employee empowerment**: anyone can intervene for quality without fear of repercussions, people have autonomy, get ongoing training, and aren't overworked. Dana cites data suggesting knowledge workers do their best work at under 40 hours a week.
- **Fact-based decision making** over political decision making. At Envato, Dana says, a disagreement can go straight to the CEO, and the worst outcome is that he disagrees.
- **Continuous improvement** of products and processes. Dana's example is a checklist on the Jira card so the ticket isn't done until tests and docs are.

Not having a QA department can even help, Dana argues, because no one can pretend quality is somebody else's job.

"Quality is always the responsibility of the entire organization," Dana Scheider said at Conf42 Golang 2021.

The talk is honest about prerequisites: full management buy-in (management accepting it is responsible too), accepting that quality always costs time and resources, existing automated test coverage, multidirectional communication across product, design and development, and people who aren't rushed or burned out. Rushed people cut corners, and quality is usually the corner that goes, along with security.

## What should a dev team actually change?

The second half is the part to bookmark:

- **Talk to product and design continuously**, in both directions. There's no moment when design is done and development begins.
- **Use the agile rituals for quality**: kickoffs, pairing and mobbing, retrospectives, and blameless post-mortems that ask what went wrong, not who did it.
- **Code review is where you look for bugs.** At least one qualified reviewer who didn't write the code, who knows the stack and the problem space, runs it locally or in staging, and hunts edge cases. Dana's rule of thumb: on a substantial pull request, a reviewer with no suggestions probably wasn't thorough enough.
- **Test beyond the happy path.** A head of product once told Dana that 5% of customers followed it.

"It's important to keep in mind in this process that the happy path is often not the most common one," Dana Scheider said at Conf42 Golang 2021.

- **Track even small changes** as issues, so they get review and testing too.
- **Use detailed pull request templates**: context and ticket links, a summary of changes, the alternatives considered and why they lost, how it was tested, step-by-step manual test cases, docs updated, screenshots where useful, and what could still go wrong, including security risks. Envato's template reminds authors that a PR is the start of a conversation, not the end.
- **Test after release** too, in staging and production, across browsers, devices and operating systems your users actually have.

## Who should watch?

Engineering managers and leads at companies that have no QA team, are losing one, or have one that's become a silo. Developers who've been told quality is now their job will get a concrete checklist. If you want tooling or automation specifics, look elsewhere; this is about the habits and culture that make tools work.

For the testing side in Go specifically: [Francisco Daines on Go testing 101](https://www.conf42.com/Golang_2022_Francisco_Daines_testing_101), [Ivan Pesenti on test-driven development of a complex Go app](https://www.conf42.com/Golang_2023_Ivan_Pesenti_complex_app_tdd), and [Julien Breux on integration tests with Testcontainers](https://www.conf42.com/Golang_2024_Julien_Breux_test_testcontainers_container).

[Watch Dana Scheider's talk](https://www.conf42.com/Golang_2021_Dana_Scheider_testing_qa_quality_process) from [Conf42 Golang 2021](https://www.conf42.com/golang2021).

## From Envato

Envato is where Dana built the quality process behind this talk; one of its core values, per the talk, is that "we tell it like it is".

- Envato careers: [envato.com/about/careers](https://envato.com/about/careers/)

[Watch the talk on YouTube](https://youtu.be/eGC4aZRkYzI).

## Watch the talk

[Choose Your Own (QA) Adventure](https://www.conf42.com/Golang_2021_Dana_Scheider_testing_qa_quality_process) at Conf42 Golang 2021.
