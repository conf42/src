# Treat subscription payments as a platform and failed charges come back

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/subscription-payments-as-a-platform

In short: George Thomas of Chegg at Conf42 Platform Engineering 2025 on payment gateways, smart retries, tokenisation and usage-based billing as self-service.

Every subscription business has a quiet revenue leak: the card that expired, the charge that bounced, the retry that went out at the wrong time. At Conf42 Platform Engineering 2025, George Thomas, Engineering Manager and Enterprise Integration Architect at Chegg, showed how treating payments as an internal platform (unified gateway, event-driven services, smart retries) turns that leak into recovered revenue and lets product teams ship pricing changes without an engineering ticket.

Thomas has worked across Zuora, Recurly, Stripe, Oracle and Salesforce, and it shows: this is a talk about the plumbing between those systems.

## From one processor to an event-driven platform

He sketches the evolution most companies lived through. A monolithic integration with one processor. Then several providers such as Braintree, Stripe and Adyen, each with its own custom integration code. Then API-first providers with abstraction layers, though teams still handled every failure themselves. And finally event-driven payment platforms where recovery and self-service are designed in from the start.

## Four building blocks

The architecture he describes has four parts:

- **A payment gateway** that hides the differences between providers behind one interface, so product code never cares whether a charge goes to Stripe or Braintree.
- **A subscription engine** owning the lifecycle: monthly, annual, bundles, price points, discounts and taxes, billing the right customer for the right period.
- **Event processing.** A renewal is an event; notifications, payment collection, general-ledger posting and revenue allocation react to it asynchronously instead of sitting in one synchronous transaction.
- **Revenue recovery** with automatic retries, because cards expire and balances run low.

The principles around them are the platform-engineering staples: abstract the card-network details away from product teams, make launches and pricing changes configuration-driven, build compliance into the APIs with audit logging, and offer a paved road for common payment scenarios while allowing deviations.

## Retries are a model, not a loop

The best section is the case study on failed payments. Before the platform, about 15% of subscription payments failed on the first attempt, retries were manual best guesses, error codes were not handled properly and only about 40% of failed payments were recovered.

You cannot just retry forever: Thomas points out that card networks such as Visa and Mastercard can fine merchants who keep retrying when they should not, so you get a handful of attempts over a few weeks. The platform version learns from the error codes and historical patterns which failures are retryable and when a retry is likely to succeed, A/B tests retry strategies against each other, and monitors the model in real time in case success rates start sliding. He reported recovery rising to 78%, which translated to millions in recovered revenue.

## Compliance and usage billing as self-service

On compliance, the trick is to never touch card numbers. Hosted payment fields from Stripe, Zuora or Recurly collect and tokenise the card, your systems keep only the token, and PCI scope shrinks accordingly. Infrastructure as code with Terraform keeps humans out of production consoles and gives auditors a change history.

Usage-based billing gets extra time because, as he notes, token-priced AI products made it mainstream. The hard parts are high-volume event ingestion, aggregation across systems and metering abstractions. His platform answer: predefined dimensions and metrics, self-service registration of new ones, and a usage-estimation API so customers can see what the next bill will be.

## Who should watch

Engineers and architects running subscription billing, especially anyone stitching several payment providers together or about to launch usage-based pricing. If you have never had to reconcile a renewal event with the general ledger, some of it will feel like inside baseball, in the best sense.

## Related Conf42 talks

- Venkata Majeti on [scaling subscription systems without losing uptime](https://www.conf42.com/Incident_Management_2025_Venkata_Majeti_subscriptions_scale_uptime) at Incident Management 2025.
- Michael A Johnson's [card payments lifecycle explained](https://www.conf42.com/Machine_Learning_2024_Michael_A_Johnson_card_payments_lifecycle) at Machine Learning 2024.
- Ashwin Das Gururaja and Devang Gaur on [end-to-end observability for commerce and payment systems](https://www.conf42.com/Observability_2025_Ashwin_Das_Gururaja_Devang_Gaur_dashboard_payment_commerce) at Observability 2025.

[Watch George Thomas's talk](https://www.conf42.com/Platform_Engineering_2025_George_Thomas_subscription_payment_service)

[Watch the talk on YouTube](https://youtu.be/iYD6vyTIPDQ).

## Watch the talk

[Platform Engineering for Subscription Payment Systems: Building Self-Service Infrastructure at Scale](https://www.conf42.com/Platform_Engineering_2025_George_Thomas_subscription_payment_service) at Conf42 Platform Engineering 2025.
