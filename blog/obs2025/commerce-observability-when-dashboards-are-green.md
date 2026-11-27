# Commerce observability starts where green dashboards stop

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/commerce-observability-when-dashboards-are-green

In short: Adobe's Ashwin Das Gururaja and Devang Gaur at Conf42 Observability 2025 on tracking checkout, payments and renewals as business signals.

Revenue drops, every dashboard is green, and the APIs keep returning 200. That is the failure mode Ashwin Das Gururaja, senior engineering manager at Adobe, and Devang Gaur, a payments product manager at Adobe, built their Conf42 Observability 2025 talk around. Their argument: in commerce and subscription businesses, the question is whether customers can buy, pay and renew, and service health only answers part of it.

The talk comes in two halves, engineering first and product second, which is a nice structure. Most observability talks never hear from the person who owns the renewal rate.

## Ask whether customers can buy

Ashwin contrasts traditional monitoring (is the service up, CPU, memory, response times, 4xx and 5xx rates) with commerce observability, which asks questions that map to money. Can customers complete a purchase, even when the checkout API returns 200 but the payment flow has a bug? Is fraud detection blocking good customers? Are payment forms actually loading in the browser? Are failed payments causing involuntary churn? Can customers update their wallets?

He then walks the full funnel (product discovery, add to cart, checkout, authorisation and fraud, fulfilment and confirmation) and the subscription lifecycle (trial signup, free-to-paid conversion, billing cycle, payment processing, renewal, usage and expansion), naming what to watch at each step. One detail worth keeping: a missed billing event can lead an entitlement system to remove access after a grace period from a customer who did nothing wrong.

## The three pillars, with a revenue column

The pillars stay the same, but each gets a business twist. Metrics include payment success rate per processor, conversion and churn alongside system health, because two processors can perform very differently on the same traffic. Logs capture why things happened: the processor's decline reason, the customer's journey breadcrumbs, why the fraud engine blocked a transaction, and error classification weighted by revenue. Traces follow a transaction from the click to settlement, including third-party gateways like Adyen or PayPal.

## Hunt for the failure you did not think to monitor

The section on unknown unknowns has the best example. 3-D Secure might start failing in France for certain card types. The dip is small for the whole system, so health checks stay calm, but it is still lost revenue. Ashwin's prescription is anomaly detection on business metrics, cross-system correlation and automated root cause analysis, so the system can ask why conversion dropped instead of whether services are healthy.

His practical do and don't lists are short and worth screenshotting: start from the subscriber journey, not the architecture; build runbooks with churn impact; test observability during billing cycles; don't alert on everything; don't ignore processor dependencies, in-app mobile metrics or the customer success team, who often hear first.

## The product manager's half

Devang's part is the reason to watch. He describes A/B tests that looked like failures until observability showed a silent JavaScript error on mobile, and a US churn creep with no alerts at all, traced to a config change that broke wallet updates with one payment processor. Customers could not update cards, so renewals failed. The team fixed it in under 48 hours.

His proposal: write observability into acceptance criteria like a product spec. For a new billing flow, can you see payment success by method, wallet errors by region, retry success by card type? Start with the golden flows (free-to-paid conversion, wallet updates, recurring billing and renewal). Adobe began by instrumenting retry success rate. You do not need hundreds of metrics, just the few that matter.

## Who should watch

Engineers and product managers in commerce, payments or subscription businesses, and anyone whose incident reviews keep concluding that the dashboards looked fine. The talk opens with industry-wide statistics; the stronger material is the Adobe examples in the second half.

## Related Conf42 talks

- George Thomas on [Platform Engineering for Subscription Payment Systems](https://www.conf42.com/Platform_Engineering_2025_George_Thomas_subscription_payment_service).
- Venkata Majeti's [AI-Driven Incident Resilience](https://www.conf42.com/Incident_Management_2025_Venkata_Majeti_subscriptions_scale_uptime) on subscription systems without losing uptime.
- Sandeep Katuri on [fraud detection for digital payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security), the other side of the approval-rate balance.

[Watch Ashwin Das Gururaja and Devang Gaur's talk](https://www.conf42.com/Observability_2025_Ashwin_Das_Gururaja_Devang_Gaur_dashboard_payment_commerce)

[Watch the talk on YouTube](https://youtu.be/VcD_I0i3Ndg).

## Watch the talk

[Beyond the Dashboard: Building End-to-End Observability for Commerce and Payment Systems](https://www.conf42.com/Observability_2025_Ashwin_Das_Gururaja_Devang_Gaur_dashboard_payment_commerce) at Conf42 Observability 2025.
