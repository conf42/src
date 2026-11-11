# If customers report your JavaScript errors, they are your monitoring

Conf42 Blog, 2022-11-16. https://www.conf42.com/blog/js2022/your-customers-are-your-error-monitoring

In short: Finbar Fleming (Rollbar) at Conf42 JavaScript 2022 on why client-side errors go unseen in production and how error monitoring shortens the fix

Most front-end teams find out about production JavaScript errors when a customer calls. At Conf42 JavaScript 2022, Finbar Fleming, lead customer engineer at Rollbar, explained why JavaScript teams in particular end up there and what an error response process looks like when the browser, not the support queue, tells you first.

Finbar spent about 15 years as a developer and development manager, much of it building CI and test-driven development processes, and says about 30% of the teams he now works with are JavaScript developers. It is a sponsor talk, and the product appears in the second half, but the diagnosis holds whatever tool you pick.

## What do production errors actually cost?

He quotes Rollbar's State of Software Code report, a survey of about 950 developers. 34% say losing users is the biggest risk of errors in their applications, and 28% report actually losing a significant number of users to them. The headline: 88% said bugs and errors are reported by customers first.

On the developer side, 32% spend up to 10 hours a week fixing bugs and 16% up to 15 hours. If a developer writes code for 25 to 27 hours a week, that is a big slice of feature time. The survey also found that 21% of developers would rather go to the dentist and 26% would rather pay bills than fix bugs, which is the most relatable statistic in the deck.

## Why are JavaScript teams worse off?

Finbar focuses on client-side errors and gives four reasons.

**Users are always affected.** A back-end failure can sometimes be retried quietly; in the UI, the user sees it.

**The tools are too convenient.** Developers, QA and support all know how to open the browser developer tools and read console.log output. That works until the users are strangers, and then the visibility vanishes, because nobody formalised an error response process before launch.

**Nobody owns it.** SRE teams own site reliability, but an intermittent error in an odd browser version on a flaky network rarely lands on their plate.

**Noise.** Network glitches, browser quirks and third-party scripts make it tempting to wait for customers to complain. He calls that a flawed way to look at the problem.

At a recent conference he asked a few hundred JavaScript developers, and 75% of them had no visibility into production errors. Of those that did, most relied on logging, often through an APM tool, and many didn't know dedicated error monitoring existed.

## Logging versus error monitoring

The distinction is the useful part of the talk. Logging is built for querying after the fact: you hear from a customer, then you search. Error identification in logging tools tends to be basic and bolted on.

Error monitoring intercepts the onerror event for uncaught errors, sends the stack trace off to be analysed and gives the error a fingerprint the moment it happens. From then on, sameness is decided by that fingerprint, not by a query you write later. That lets you notify a team when an error is new, or when a release from 15 minutes ago is hitting ten users a minute.

He breaks the typical error lifecycle into five steps: the customer hits the error, calls support, support tries to reproduce it, a developer reproduces it, the developer finds the root cause. The first three steps are slow and make users unhappy. "Once you understand the error and once you have the stack trace associated with an error, you can really generally very quickly deduce the root cause and get a fix out there," Finbar Fleming said at Conf42 JavaScript 2022.

## Error monitoring is a journey

His five phases are a reasonable roadmap whatever you use:

1. Install it and get real-time visibility.
2. Fix the low-hanging errors you didn't know about. One team he worked with went from 40,000 errors a month to 2,000 in six weeks.
3. Turn on notifications for the categories you care about.
4. Add context: geography, or whether an error hits free-tier or top-paying customers.
5. Integrate with source control, testing tools, session replay and back-end logs, then automate: block a build, or roll back a canary.

His advice for JavaScript developers: add it at the start of a new code base, so a central place for errors from every environment becomes part of the team's culture. If logging is all you have, use it, because some visibility beats none.

## Who should watch

Front-end leads whose error process is a support inbox, and full-stack developers who suspect their console.log habit won't scale. It is a process talk, not a code walkthrough, and short.

Related Conf42 talks: [Shai Almog on debugging Node.js in production](https://www.conf42.com/JavaScript_2021_Shai_Almog_Debug_NodeJS_Lightrun) at JavaScript 2021, [DeveloperSteve Coochin on debugging Schrödinger's app](https://www.conf42.com/DevSecOps_2022_DeveloperSteve_Coochin_debugging_schrodingers_app), and [Sarah Morgan on observability versus performance monitoring](https://www.conf42.com/DevOps_2023_Sarah_Morgan_observability_vs_performance_monitoring).

[Watch Finbar Fleming's talk](https://www.conf42.com/JavaScript_2022_Finbar_Fleming_debugging_errors_in_production) from [Conf42 JavaScript 2022](https://www.conf42.com/js2022).

## From Rollbar

Finbar describes Rollbar as a platform to group, respond to and gain insights from errors. Its fingerprinting is designed to stay stable across code changes and library upgrades, so the same error keeps the same identity. In the talk he shows occurrence patterns over time, the number of people affected and a browser breakdown, and notes that setup means importing an SDK and turning on error tracking, usually within 30 to 60 minutes.

- Rollbar: [rollbar.com](https://rollbar.com/signup/?utm=conf42)

[Watch the talk on YouTube](https://youtu.be/jCH-aLbcYUA).

## Watch the talk

[Improving the process of debugging JavaScript errors in Production for better end user experience and happier developers](https://www.conf42.com/JavaScript_2022_Finbar_Fleming_debugging_errors_in_production) at Conf42 JavaScript 2022.
