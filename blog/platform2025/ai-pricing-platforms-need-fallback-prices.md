# An AI pricing platform is only as good as its fallback price

Conf42 Blog, 2025-08-18, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-pricing-platforms-need-fallback-prices

In short: Amaresh Sahoo of Xometry on real-time AI pricing at Conf42 Platform Engineering 2025, from cached predictions to circuit breakers and fallback prices.

Most ML systems can be wrong for a while before anyone notices. A pricing system cannot: a bad number shows up on the invoice. At Conf42 Platform Engineering 2025, Amaresh Sahoo, Vice President of Pricing, Sourcing and Analytics at Xometry, walks through the architecture of real-time AI pricing platforms, and his recurring theme is that the model is the easy part; low latency, consistent data and a sane fallback when things break are what keep revenue intact.

## Why pricing is a hard platform problem

Sahoo lists the constraints up front. Every decision has direct revenue impact. Inputs come from many places at once: competitor prices, inventory and sourcing data, customer behaviour. Customers expect an instant quote, not a spinner. And the system has to behave consistently across geographies while meeting each region's regulations.

The infrastructure answer is familiar but well assembled: edge computing to put pricing compute near each market, container orchestration that scales with demand, CDNs and dedicated links between data centres to trim API latency, and stream processing that ingests and validates data continuously. The detail worth noting is real-time data quality checks that catch anomalies without adding processing delay, because a stale competitor feed is how you end up underpricing a whole catalogue.

## Cache the common case, infer the edge case

The sharpest idea is about where models run. Rather than calling a model on every request, Sahoo describes caching predictions for common scenarios and reserving real-time inference for the edge cases, with memory allocated deliberately so the hot models answer fast. It is the pricing version of the read-heavy cache you already have in front of your database, with the twist that the cache needs to know when its inputs have gone stale.

Around that sits the model lifecycle: ensembles where models sit behind other models, weighting each by its strengths and controlling for its biases; strict version control so you can compare a new model against the old one and roll back; continuous training on fresh feedback; and monitoring that looks at customer and financial outcomes together, not only technical metrics. He also notes that off-the-shelf APM tools miss what matters here, so teams need custom tracking of prediction latency, model performance and business impact.

## Experiments need automatic brakes

Pricing has to be tested constantly, and Sahoo covers A/B tests, multi-armed bandits and contextual bandits. The platform lesson is the guardrail: automated rollback triggers tied to KPIs, so a pricing experiment that starts hurting the business reverts without waiting for someone to read a dashboard on Monday.

## Degrade to a boring price, not to an error

The reliability section is the one to bookmark. Circuit breakers isolate a failing data source or a degraded internal service before it drags everything down. Graceful degradation means serving cached prices, a simplified pricing algorithm or default pricing rules when the AI service is unavailable. Replication is split: synchronous for critical data, asynchronous for less time-sensitive information. Health checks go beyond a ping and verify that models actually loaded and predictions look sane, and disaster recovery plans have to account for rebuilding model state and warming caches, not only restoring data.

Security and compliance get their turn too: regional rules for European, North American and Asian customer data, federated learning where data cannot move, and role-based access with fine-grained authorisation.

## Who should watch

Engineers building any real-time decisioning system where an outage costs money directly: pricing, quoting, bidding, fraud scoring. It is an architecture overview from the business owner's chair, not a code walkthrough, which makes it a good primer for the platform team that will run such a system.

## Related Conf42 talks

- [Graceful Degradation: Keeping The Lights On When Everything Goes Wrong](https://www.conf42.com/Chaos_Engineering_2023_Tanveer_Gill_graceful_degradation_everything_goes_wrong) by Tanveer Gill, Conf42 Chaos Engineering 2023
- [AI-Powered Fraud Detection in Cloud-Native Digital Payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) by Sandeep Katuri, Conf42 Cloud Native 2025
- [Data Science Careers via A/B Testing: Scalable Experimentation in Cloud-Native Era](https://www.conf42.com/Kube_Native_2025_Bhavana_Reddy_Chadagonda_abtesting_experimentation_careers) by Bhavana Reddy Chadagonda, Conf42 Kube Native 2025

[Watch Amaresh Sahoo's talk](https://www.conf42.com/Platform_Engineering_2025_Amaresh_Sahoo_pricing_decision_time)

[Watch the talk on YouTube](https://youtu.be/8mejpGTmxgQ).

## Watch the talk

[Building Resilient AI Pricing Platforms: Engineering Real-Time Decision Systems at Scale](https://www.conf42.com/Platform_Engineering_2025_Amaresh_Sahoo_pricing_decision_time) at Conf42 Platform Engineering 2025.
