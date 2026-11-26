# In async commerce, failures whisper, so design for tracing first

Conf42 Blog, 2025-05-13. https://www.conf42.com/blog/obs2025/async-commerce-failures-whisper

In short: Anup Raja Sarabu of T-Mobile at Conf42 Observability 2025 on async payments, BOPIS events, eventual consistency and the observability that keeps it honest.

On a new iPhone launch day, T-Mobile's payment system went down in the first 15 minutes and customers sat on "oops, something went wrong" with orders they could not submit. At Conf42 Observability 2025, Anup Raja Sarabu, Senior Technical Product Manager at T-Mobile, used that incident to explain why the team is decoupling payments from order submission, and why observability has to be designed in before the first event is published.

His one-line summary of the trade-off: synchronous systems fail loudly, while in async flows failures don't scream, they whisper. Miss the whisper and you find out from a customer.

## The launch-day incident that started it

New product introductions, especially September Apple launches, are T-Mobile's busiest days, with Sarabu citing around 100,000 orders. Checkout was synchronous: build the cart, pay, and only then submit the order. Circuit breakers kept the rest of the system up, but with payments broken nobody could finish. That raised the question of whether payment really needs to block the order at all.

The redesign he describes puts payment on a queue. The customer gets an order number and confirmation immediately; card validity, fraud and funds checks happen behind the scenes; the order is only submitted once payment clears. If payment fails, the customer gets a text or email asking them to re-enter card details. T-Mobile already ran buy online, pick up in store (BOPIS) this way, with inventory validation, store notification and pickup scheduling as independent events working in parallel.

## Four things to observe in async systems

Sarabu's pillars for async observability are specific. Distributed tracing with OpenTelemetry context injected into requests and events, so spans correlate even across Kafka hops. Event audit and replay: structured events with user ID, order ID, timestamp and type, so you can reconstruct what happened and retry failed processing. Consistency monitoring that checks whole business transactions complete (inventory reserved, payment confirmed, shipment initiated) even when events arrive out of order. And domain dashboards in business language, so product managers and support see orders and payment states instead of raw traces.

On tooling he names OpenTelemetry, Jaeger, Grafana and AWS X-Ray for traces, Burrow for Kafka consumer lag, and Kibana, Metabase and Power BI for the order dashboards. The Kafka metrics that matter are queue depth, consumer lag, throughput and handler error rates.

## Eventual consistency, engineered on purpose

The CAP section is the most useful part for architects. In high-scale commerce, partition tolerance is non-negotiable, so T-Mobile chose availability and accepted eventual consistency. That only works with three techniques: idempotent handlers so a duplicated payment confirmation never charges twice, version numbers on orders and payments to resolve concurrent updates, and compensating transactions instead of rollbacks, such as a cancellation event that restores inventory when payment fails after confirmation. His warning about dashboards is worth framing: in async systems, every service can be green while the flow is broken.

## Lessons he closes on

Design for traceability from day one, because tracing cannot be bolted on later. Plan for eventual consistency rather than chasing real-time consistency. Align metrics to business events so observability becomes an organisational asset, not just a dev tool. He also reported BOPIS carts converting to orders at a markedly higher rate than standard online carts, and close to full availability during launch and promotional peaks.

## Who should watch

Anyone moving checkout, payments or fulfilment from synchronous calls to events, and product managers who want to understand what their engineers mean by eventual consistency. It is long and conversational, but the incident is real and the patterns are concrete.

## Related Conf42 talks

- [An Introduction to Saga Pattern for Distributed Transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) by Dmitry Khorev at Conf42 Cloud Native 2023.
- [The Art of Event Driven Observability with OpenTelemetry](https://www.conf42.com/Observability_2023_Henrik_Rexed_event_driven_observability_opentelemetry) by Henrik Rexed at Conf42 Observability 2023.
- [So You Want To Build An Event Driven System?](https://www.conf42.com/Cloud_Native_2024_James_Eastham_event_driven_system) by James Eastham at Conf42 Cloud Native 2024.

[Watch Anup Raja Sarabu's talk](https://www.conf42.com/Observability_2025_Anup_Raja_Sarabu_asynchronous_eventdriven_commerce) or the [YouTube recording](https://youtu.be/7tAZrdT7vIU).

## Watch the talk

[Building Resilient Asynchronous Commerce Systems: Observability Lessons from Event-Driven Architectures](https://www.conf42.com/Observability_2025_Anup_Raja_Sarabu_asynchronous_eventdriven_commerce) at Conf42 Observability 2025.
