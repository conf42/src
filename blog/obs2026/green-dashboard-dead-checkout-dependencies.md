# Green dashboard, dead checkout - monitor what your app depends on

Conf42 Blog, 2026-08-29, updated 2026-11-09. https://www.conf42.com/blog/obs2026/green-dashboard-dead-checkout-dependencies

In short: Eleftheria Batsou of UptimeRobot at Conf42 Observability 2026 on dependency outages, the 200 that lies, and why status pages can't be your alarm.

Most outages now happen in something your code calls, not in the code itself, and most monitoring only watches the code. At Conf42 Observability 2026, Eleftheria Batsou, Developer Advocate at UptimeRobot, made that case in a tight, story-driven talk: inventory your dependencies, check them from the outside the way your app uses them, and stop trusting a 200.

## The 20 minutes nobody noticed

The talk opens with a scenario you've probably lived. Thursday afternoon, every check green: homepage 200, API 200, login 200. A support ticket says the checkout button does nothing. Then three tickets, then a sales demo fails in front of a prospect. An engineer finally digs in and finds the payment provider has been erroring on a subset of requests for about an hour. The app handled it gracefully, which in practice meant swallowing the error and showing a spinner.

Every check was telling the truth. Batsou's point: "The thing that broke isn't the thing you built." Swap the payment provider for your identity provider, your CDN or the LLM API you bolted on last quarter and the story still works.

## Three ways a healthy check misses a real failure

Adding more checks against your own endpoints just gives you "Ten green lights instead of three", more confidence without more coverage. She named three specific blind spots:

- **The 200 that lies.** The checkout page rendered. That says nothing about whether a payment can complete.
- **The partial failure.** A provider failing a slice of requests can slip past a check that runs every five minutes and happens to land on the good ones.
- **The slow success.** A 30-second timeout passes an 18-second response. The customer left long before that.

The fix is a different question: can a customer still do the thing they came for? That means checking for expected content, calling the dependency directly the way your app does, and setting latency thresholds to human patience rather than socket timeouts.

## Nobody knows their full dependency list

Batsou says she has never met a team that could list all its dependencies from memory. Payments and auth come first, then someone remembers email, then the analytics script that blocks page load, the font CDN, map tiles, feature flags, the error tracker, and the AI API a contractor wired in months ago.

Her method is a couple of hours of unglamorous work: inventory every external host your key pages load, grep the backend for outbound calls and API keys, read your DNS zone (CNAMEs pointing at someone else's infrastructure), and trace a real checkout. Group the list, then ask two questions per group: if this degrades, what does a customer feel, and would we know? Monitor the ones where the first answer hurts. Skip the font CDN; never skip the thing that takes money.

## Status pages describe the vendor's incident, not yours

The argument she said she's happy to defend: you can't rely on a platform to report its own outage. Not because vendors lie, but because of structure. They have reasons to describe incidents narrowly and to wait until they understand them. Partial degradations often stay within their tolerance and never get posted.

She backed it with UptimeRobot data: in the first half of the year, across services that publish a status page, 89% of user-reported incidents had no official filing within six hours, and where vendors did file, the crowd usually got there first by a median of about two hours. Your internal metrics live inside the failing system; the status page lives inside the vendor. Something has to stand outside both.

## Who should watch

Anyone who owns an on-call rotation and has watched a dashboard stay green through an incident. It's short, product-light (UptimeRobot comes up as the example tool, and the method is tool-agnostic), and it ends with a to-do list you can start this week.

## Related Conf42 talks

- [Palak Bhawsar on synthetic monitoring](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage) (Conf42 Observability 2025): outside-in checks before the outage.
- [Mandi Walls on managing vendor incidents](https://www.conf42.com/Incident_Management_2024_Mandi_Walls_25_vendor_incidents_management) (Conf42 Incident Management 2024): what to do once the third party is the problem.
- [Andrew Robinson on health checks and dependency management](https://www.conf42.com/Cloud_Native_2021_Andrew_Robinson_improving_reliability_health_check_dependency_management) (Conf42 Cloud Native 2021).

[Watch Eleftheria Batsou's talk](https://www.conf42.com/Observability_2026_Eleftheria_Batsou_healthchecks_outages_dependencies)

[Watch the talk on YouTube](https://youtu.be/3kp5FpqwTv0).

## Watch the talk

[Your App Is Up. Your Business Is Down.](https://www.conf42.com/Observability_2026_Eleftheria_Batsou_healthchecks_outages_dependencies) at Conf42 Observability 2026.
