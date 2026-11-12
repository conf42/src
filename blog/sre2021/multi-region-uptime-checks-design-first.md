# Global uptime checks take an afternoon to set up and weeks to design

Conf42 Blog, 2021-09-29. https://www.conf42.com/blog/sre2021/multi-region-uptime-checks-design-first

In short: Andrei Danilov (Typeform) at Conf42 SRE 2021 on designing multi-location availability monitoring - which locations, how often, what fails, who reacts.

Your production monitor says the platform is up because it pings the same data center the app runs in, while users on another continent are filing support tickets. At [Conf42 Site Reliability Engineering 2021](https://www.conf42.com/sre2021), Andrei Danilov, Platform Engineer at Typeform, walked through the questions to answer before monitoring availability from multiple locations. His point is that the tool is the easy part: Postman, Datadog, New Relic and the rest make a check trivial to create, and all the work is in deciding what to check, from where and who gets woken up.

## Where is the hard part?

He frames it as Typeform's growing pains. As the user base spread across regions the company hadn't expected, outages seen only from far away surfaced as support tickets that took engineers longer to understand. The goal was to catch those proactively and wire them into alerting. "So if the challenge is not setting up the tool, where is the challenge?" Andrei Danilov asked at Conf42 SRE 2021. His answer, as with everything in engineering: understand what needs to be built and how it will be used before you touch the implementation.

## Which locations, and what is a location?

Unless you are a telco, you can't watch every corner of the globe. Pick by what matters to the business: top locations by user base, by visits, by premium accounts, plus whatever your SLAs and legal agreements require. Typeform's baseline mixed top locations by visits with top locations by number of customers.

A location can be a city, a country or a region. A food delivery company concentrated in one big city should watch that city, since a failure there can vanish inside a country-wide average. Typeform settled on a mix of countries and regions, expecting it to change.

Ideally every location alerts the same way, Barcelona and San Francisco alike. Realistically, use your company's priority system. Typeform treats its small set the same, though the mix makes some count a little more.

## How often, and how do you keep it out of the data?

Frequency follows traffic. For high-traffic locations, once a minute is a sensible start; anything coarser leaves you blind to a regional outage for too long. The catch is volume. A once-a-minute check comes to around 45,000 runs a month and almost half a million a year, enough to pollute analytics and trip security rules. So flag the traffic: allow-list the IPs, add bypass headers, set user agents or parameterised requests. Typeform needed a mix, because each downstream system had different requirements.

## When is a failure worth an alert?

Not on every failure: the monitoring vendor's own server in that location may be down while your users are fine, and alerting on that spams engineers and erodes trust in the tool. Alert on consecutive failures, using a retry or the next scheduled run depending on frequency.

For what counts as failure, the tools agree on defaults: HTTP errors and timeouts. You can add custom error codes, tighter timeouts, latency thresholds or assertions on the response, guided by your SLAs. His advice is to start with the defaults and learn how your system behaves before customising.

## Who reacts, and how do you avoid an alert storm?

In an ideal DevOps world the owning team reacts first; in practice it is whoever has the access and knowledge, SRE, ops, incident management or the platform team. At Typeform his team took the alerts first to route them, then experimented with owning teams responding directly. A defect that takes everything down will fire every location at once into an already noisy on-call channel. Grouping tools exist, Moogsoft among those he had read about, but he recommends starting small and keeping these alerts separate at first.

## What should the check actually hit?

Keep it simple. Your test suites already cover user journeys; this only asks whether the platform is reachable from a region, and a GET or a ping to a URL usually does it. For a monolith, one monitor on the main URL can be enough. With microservices, map how things are deployed and connected, then choose a few powerful monitors rather than one per endpoint.

## Who should watch

Platform and SRE teams at companies whose users have outgrown one region, especially before buying a multi-location monitoring product. It is a design checklist rather than a tool demo. Pair it with:

- [Ana Van Straaten on going multi-region](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region) at Conf42 Cloud Native 2022.
- [Palak Bhawsar on synthetic monitoring](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage) at Conf42 Observability 2025.
- [Chris Riley on incident response, incident management and alerts](https://www.conf42.com/Site_Reliability_Engineering_2021_Chris_Riley_incident_response_incident_management_alerts_CloudOps) at Conf42 SRE 2021.

[Watch Andrei Danilov's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrei_Danilov_go_global_monitoring_platform_multiple_locations) from Conf42 SRE 2021.

## From Typeform

Typeform builds online forms and surveys, and its platform serves users around the world, the setting for this talk.

- [Typeform website](https://try.typeform.com/)

[Watch the talk on YouTube](https://youtu.be/vKF08huEnrM).

## Watch the talk

[Go global or go home! Monitoring your platform from multiple locations](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrei_Danilov_go_global_monitoring_platform_multiple_locations) at Conf42 Site Reliability Engineering 2021.
