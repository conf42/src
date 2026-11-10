# Kafka won't make your retail supply chain resilient on its own

Conf42 Blog, 2026-10-18, updated 2026-11-09. https://www.conf42.com/platform2026/kafka-wont-make-your-supply-chain-resilient

In short: Nidhin Jose (Walmart) at Conf42 Platform Engineering 2026 on the ownership, idempotency and recovery patterns that make event-driven retail systems hold up.

Putting a message broker between your services doesn't remove failures; it moves them into asynchronous workflows where they're harder to see. That's the opening claim from Nidhin Jose, Staff Software Engineer at Walmart, at Conf42 Platform Engineering 2026, and the rest of his talk is a compact checklist of what actually makes an event-driven retail platform resilient, and which parts a platform team should own.

The setting is retail: one customer order crosses order management, inventory, fulfillment, logistics, stores and delivery. The customer sees one promise. Behind it sit many systems with different owners and different ways to break.

## Publish only the facts you own

Resilience starts with ownership, not infrastructure. Order management owns the order lifecycle; inventory owns availability and reservations; logistics owns shipment progression. Each domain publishes only what it's authoritative for. Order management emits *order placed*; inventory answers with *stock reserved* or *reservation rejected*.

Nidhin draws a firm line between commands and events. *Reserve stock* is a command: intent, which can be refused. *Stock reserved* is an event: a recorded outcome. Blurring the two quietly rebuilds synchronous request-response over a message bus, with all the coupling and none of the honesty.

## Assume every event arrives twice

On Kafka specifics, he keeps it precise. Producers don't wait for consumers; consumer groups move at their own pace. Partition by order ID and you get ordering within an order, not global ordering, a distinction that bites teams who assumed otherwise. Rebalances and retries mean reprocessing, so consumers must be safe against duplicates.

Two patterns carry the load:

- **Transactional outbox** to close the dual-write gap: write the business update and the outgoing event in the same local transaction, and let a separate publisher deliver it. That fixes lost events but can still publish twice.
- **Idempotent consumers** with stable event IDs and business-level checks, so processing *stock reserved* twice doesn't trigger two fulfillments.

Failures get classified too. Transient ones get bounded retries with back-off; invalid contracts or impossible states go to a dead-letter queue, and that queue needs an owner, alerting and controlled replay. A DLQ nobody reads is just a slower way to lose orders.

## Use the heavy patterns selectively

Event sourcing, CQRS and sagas each get a fair, unhyped treatment. Event sourcing earns its keep where history matters, such as inventory receipts, reservations, releases and adjustments, but brings snapshots, schema evolution and retention costs. CQRS lets the storefront, the operator dashboard and analytics each get their own read model, at the price of lag, so critical decisions still check authoritative state. Sagas coordinate reserve, authorise payment and dispatch without a global transaction; compensation is a new business action (release the reservation, reroute, sometimes a human), not a database rollback.

Ordering is scoped, so a projection may see a logistics event before the related inventory update. Versions, transition rules, buffering or reconciliation handle that, and teams should know which views are authoritative and which may lag.

## Where the platform team comes in

The platform owns the reusable mechanism; domains own the business logic. In Nidhin's paved path that means topic provisioning, schema registration, access control, producer and consumer templates, retries, DLQ handling, tracing, replay and contract testing. Event contracts get treated like APIs: adding an optional field is usually safe, removing or redefining one breaks consumers, and compatibility checks should catch that before production.

His adoption advice is refreshingly modest: start with one bounded business event, define owner, contract, consumers, failure modes and replay, then expand. And if a caller needs an immediate authoritative answer, a synchronous API may still be the right call.

## Who should watch

Teams early in an event-driven migration, or platform engineers deciding what belongs in a shared eventing toolkit. It's a patterns talk without code or numbers, short and dense; seasoned Kafka operators will find it a good checklist rather than new territory.

## Related Conf42 talks

- [Building Resilient Asynchronous Commerce Systems: Observability Lessons from Event-Driven Architectures](https://www.conf42.com/Observability_2025_Anup_Raja_Sarabu_asynchronous_eventdriven_commerce) by Anup Raja Sarabu (T-Mobile)
- [Resilient by Design: Data-Driven Migration from Monoliths to Event-Driven Microservices](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Amlan_Ghosh_resilient_design_data) by Amlan Ghosh
- [Scaling Kubernetes-Native Systems with Event-Driven Patterns on Azure](https://www.conf42.com/Kube_Native_2025_Ashif_Anwar_azure_eventdriven_patterns) by Ashif Anwar (Wolters Kluwer)

[Watch Nidhin's talk](https://www.conf42.com/Platform_Engineering_2026_Nidhin_Jose_retail_supply_event)

[Watch the talk on YouTube](https://youtu.be/xQcIAiOvuBs).

## Watch the talk

[Platform Engineering for Resilient Retail Supply Chains with Event-Driven Design](https://www.conf42.com/Platform_Engineering_2026_Nidhin_Jose_retail_supply_event) at Conf42 Platform Engineering 2026.
