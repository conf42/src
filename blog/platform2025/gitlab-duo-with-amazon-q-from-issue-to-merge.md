# GitLab Duo with Amazon Q: from issue to merge request in a slash command

Conf42 Blog, 2025-08-10, updated 2026-11-09. https://www.conf42.com/blog/platform2025/gitlab-duo-with-amazon-q-from-issue-to-merge

In short: AWS's Mohamed Najaaf at Conf42 Platform Engineering 2025 demos GitLab Duo with Amazon Q: code from issues, Java 17 upgrades and security reviews.

Type `/q dev` in a GitLab issue and a merge request comes back. At Conf42 Platform Engineering 2025, Mohamed Najaaf, a solutions architect at AWS, demoed GitLab Duo with Amazon Q, the integration that puts Amazon Q Developer inside GitLab so the AI help happens where the code review already lives.

To be clear about scope: this is a vendor product walkthrough by AWS, built around three recorded demos, and at the time of the talk it was only available to GitLab Self-Managed Ultimate customers.

## Why put the assistant inside the DevSecOps platform

Mohamed opens with a figure from GitLab's Global DevSecOps report: 74% of organisations using AI for software development want to consolidate their toolchain. The pitch follows from that. Developers already juggle an IDE, a chat assistant, a scanner and a CI system; putting the assistant in the issue tracker and merge request cuts down the tab switching and the confusion.

He lists four jobs for the integration: turning an idea into code, optimising code by generating unit tests from a merge request, security code review, and modernising legacy Java.

## Demo one: issue to merge request

The first demo starts with a TypeScript sample project and an issue: add a signup flow with email, password and username, plus a sign-in flow for existing users, linked from the home page. A `/q dev` comment kicks off Amazon Q, which replies that it is generating code and will open a merge request when done. A few seconds later, it does.

The interesting bit is the loop afterwards. The reviewer notices there is no logging, comments asking for logging, invokes `/q dev` again, and Q adds a new logger file to the same merge request. Mohamed stresses that a human still reviews every change; the tool shortens the path, it doesn't remove the reviewer.

## Demo two: Java 8 or 11 to Java 17

The modernisation demo is the one most teams will care about. An issue titled "Upgrade project to Java 17" with `/q transform` in the description triggers a GitLab CI job that uploads the code, produces a transformation plan (lines of code, dependencies to replace, files to change), transforms the code and opens a merge request. The traceability is the selling point: what was upgraded, what was removed, and what you should check is all documented in the merge request.

Mohamed is candid that upgrades like this used to take weeks or months depending on code size, and that you may still need to make small fixes by hand afterwards.

## Demo three: review, then fix

The last demo runs `/q review` on a merge request. Q flags a likely SQL injection, highlights the offending code inline, and a follow-up `/q fix` proposes the patched version for the developer to review and apply. Think of it as a second reviewer who never gets bored of reading string concatenation.

## Who should watch

Teams on GitLab Self-Managed Ultimate with an AWS footprint, especially anyone sitting on a pile of Java 8 services. If you are on GitLab.com or another forge, it is still a useful look at how slash-command AI workflows can live inside merge requests, but check current availability before planning around it.

## Related Conf42 talks

- [Shubham Singh on how AI is changing code review](https://www.conf42.com/Python_2025_Shubham_Singh_ai_code_review) puts the review demo in a broader context.
- [Rajkumar Chindanuru on legacy modernization strategies](https://www.conf42.com/Golang_2025_Rajkumar_Chindanuru_legacy_modernization_strategies) covers the planning around a big upgrade.
- [Hila Fish on migrating an entire R&D org from Bitbucket to GitLab](https://www.conf42.com/Site_Reliability_Engineering_2022_Hila_Fish_migrating_entire_rd_scmbitbucket_gitlab), for the step before any of this.

[Watch Mohamed Najaaf's talk](https://www.conf42.com/Platform_Engineering_2025_Mohamed_Najaaf_developer_gitlab_level)

[Watch the talk on YouTube](https://youtu.be/3wNlz6Z4UI4).

## Watch the talk

[GitLab & Amazon Q Developer for a next-level developer experience](https://www.conf42.com/Platform_Engineering_2025_Mohamed_Najaaf_developer_gitlab_level) at Conf42 Platform Engineering 2025.
