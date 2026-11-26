# Let a robot customer find the outage before a real one does

Conf42 Blog, 2025-05-09, updated 2026-11-09. https://www.conf42.com/blog/obs2025/synthetic-monitoring-before-outage

In short: Telstra DevOps engineer Palak Bhawsar explains synthetic monitoring at Conf42 Observability 2025, from monitor types to thresholds that won't bury you in alerts.

Palak Bhawsar's team once had a payment gateway API crash at 2 AM and only found out when 50 customers complained. At Conf42 Observability 2025, Bhawsar, a DevOps Engineer at Telstra and technical blogger, used that night as the case for synthetic monitoring: scripted robots that click, submit and call your APIs around the clock from around the world, so the first person to notice a failure is on your team. It's a clear introduction, aimed at people setting up their first synthetic checks.

## Traditional monitoring waits for something to break

The contrast she draws is simple. Classic monitoring is reactive: it tells you once the thing is broken, often once a user has already hit it. Synthetic monitoring simulates the user's interaction every minute, every five minutes, or whatever interval you pick, from multiple regions. Think of it as a robot customer that never sleeps and never files angry support tickets.

Why now? Bhawsar gives three reasons: systems made of microservices, serverless functions and APIs have more ways to fail; users expect instant responses (she cites a 2024 study claiming a two-second delay makes 20% of customers leave); and your users are spread across countries, so a check from one region proves very little. She also cites market forecasts for synthetic monitoring growing from $1.42 billion in 2024 to about $3.78 billion by 2033, driven by cloud adoption, AI in monitoring tools and the shift from reactive to proactive.

## Five monitors, five questions

The talk's taxonomy is a handy checklist:

- **API monitors**: is the endpoint up and returning a 200?
- **Browser monitors**: can a simulated user add to cart and pay?
- **Scripted monitors**: does a fixed multi-step journey (log in, add to cart, place the order) work end to end?
- **Ping monitors**: is the server reachable at all?
- **SSL/TLS certificate monitors**: is the certificate still valid, or did it quietly expire on a Sunday?

## Start from the journey you can't afford to lose

Her implementation steps start with the business, not the tool. Identify the critical user journeys: for a healthcare app that's booking an appointment or reaching a prescription, for a bank it's moving money between accounts. Script those flows end to end, pick a tool that fits (she names New Relic, Dynatrace and Datadog), schedule runs around the clock from the locations your users are in, and review the results regularly so last night's failure becomes next sprint's fix.

What to look for in a tool: multi-region testing, integration with the rest of your observability stack (logs, traces, metrics), custom scripting in the languages your team uses, and AI-driven insights. Bhawsar gives a personal example of the last one: a null pointer exception buried in a large Java codebase that an AI feature pinned to the exact method.

## Thresholds decide whether anyone reads the alerts

The best-practice section is where the experience shows. Set realistic thresholds: a non-critical app can fail once or twice a day, a payment or banking flow can't fail even once. Alert only on critical issues, because alerting on everything is how the one that matters gets missed. And validate full flows, not single features: add-to-cart working doesn't mean a customer can complete a payment.

## Who should watch

Developers and junior SREs who own uptime but don't yet have synthetic checks, and teams who have them but only ping the homepage. Experienced observability engineers will find it introductory. Either way, it's a good prompt to write down your top three critical journeys and check whether anything tests them at 2 AM.

## Related Conf42 talks

- Natalie Lunbeck on [E2E Test Before Merge](https://www.conf42.com/DevOps_2024_Natalie_Lunbeck_e2e_test_merge), the same journeys tested earlier in the pipeline.
- Gil Zilberfeld on [Playwright In An Hour](https://www.conf42.com/JavaScript_2024_Gil_Zilberfeld_26_playwright_automation_testing), a common engine for scripted browser checks.
- Amith Reddy Ravuru on [Platform SLOs Beyond Uptime: Measuring the Journey from Request to Value](https://www.conf42.com/Platform_Engineering_2026_Amith_Reddy_Ravuru_slos_uptime_journey).

[Watch Palak Bhawsar's talk](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage)

[Watch the talk on YouTube](https://youtu.be/TG-z2QrLbPo).

## Watch the talk

[Observability Starts Before the Outage: Synthetic Monitoring for Modern Systems](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage) at Conf42 Observability 2025.
