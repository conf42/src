# Your chatbot understands the request. Can it cancel the order?

Conf42 Blog, 2026-05-06, updated 2026-11-09. https://www.conf42.com/blog/golang2026/chatbots-that-cancel-the-order-in-go

In short: Swati Kumari of NucleusTeq at Conf42 Golang 2026 on turning chatbots into systems that act, with a Go orchestration layer as the nervous system.

Most enterprise chatbots are good at talking and bad at doing. At Conf42 Golang 2026, Swati Kumari, Product Manager at NucleusTeq, argued that the hard part of useful AI support is not the language model but the backend integration behind it, and that a Go orchestration layer is the natural place to build it.

Her framing is blunt: the industry problem is no longer NLP quality, it is operational execution. Bots shine in the demo and in QA, then fail in production because they cannot tell a customer where the delayed package is, whether the refund is pending, or if the invoice exists at all.

## The bot is only as smart as the systems it can reach

Swati's diagnosis of failing bots is disconnection. A bot might be wired to the CRM but not to authentication or the refund system, so it understands a request to cancel an order perfectly and still cannot do it. She is careful not to say the bot should get access to everything; the point is that each action it promises needs a real path into the systems that own that action.

So she draws the stack in layers: the LLM and NLP on top, then integration and orchestration, then the core systems. The orchestration service in the middle handles backend coordination, retries, caching, authentication, event handling and response aggregation. She calls it the nervous system of the platform, which is a fair description of any service that has to know everything and gets blamed for everything.

## Orchestration is a concurrency problem, which is why Go

One cancel-my-order request turns into several independent checks: is the user authenticated, has the order shipped, is it refundable, is there a billing hold? Run those in series and the latency adds up fast. Swati's case for Go is that goroutines and channels make that fan-out straightforward without a lot of operational complexity, so concurrency becomes part of the architecture rather than a later optimisation.

Long-running flows (delivery exceptions, fraud reviews, ticket escalations) should not block the conversation at all. For those she moves from request-response to event-driven design: the bot publishes an event, independent consumers react, and the user is not left staring at a spinner.

## Cache by data type, not by habit

The caching section is the most practical part of the talk. Agent-style systems generate a lot of repeated lookups, and without caching the orchestration layer can overload the downstream services quickly. But not everything is equally safe to cache: a user profile can live with a longer TTL, while payment state and inventory usually need live reads. Her line: "the real design is not should we cache it, it is what is safe to cache and for how long."

Freshness ties into trust. When someone asks where their package is, they expect the current state, not a snapshot from an hour ago, so she points to WebSockets, server-sent events and live event ingestion feeding Go channels.

## Two worked flows, and the failure paths that matter more

Swati walks through two cases. Cancelling an order that is paid but not shipped means validating the request, checking order management status, verifying refund eligibility, coordinating with billing, handling retries and keeping the operation idempotent, ideally with no human agent involved. The billing dispute case shifts the focus to failure: timeouts, failed APIs and inconsistent downstream state are normal operating conditions, so she lists timeout propagation, retries with back-off, circuit breaking and graceful escalation as baseline requirements.

Then security. A conversational mistake is annoying; an unauthorised transaction is serious. Once a bot can act, the orchestration layer becomes both the execution layer and the security boundary, which means authorisation scopes, audit logging, rate limiting, validation and careful handling of sensitive data.

## Who should watch

This is an architecture overview, not a code walkthrough: no repo, no benchmarks. It suits backend engineers who have been asked to connect the chatbot to the real systems and want a checklist of what that involves, and product people who need to explain why the demo bot is not the production bot. If you already run agent tool calls through a hardened gateway, much of it will be familiar.

## Related Conf42 talks

- [Nagarajan Madhavan on customer service chatbots](https://www.conf42.com/Platform_Engineering_2024_Nagarajan_Madhavan_customer_service_chatbots) at Conf42 Platform Engineering 2024
- [Samuel Baruffi on enterprise chatbots with Amazon Bedrock](https://www.conf42.com/Machine_Learning_2025_Samuel_Baruffi_chatbots_bedrock_enterprise) at Conf42 Machine Learning 2025
- [SreenivasaRao Jagarlamudi on AI workflows with Kafka](https://www.conf42.com/Prompt_Engineering_2024_SreenivasaRao_Jagarlamudi_ai_workflows_kafka) at Conf42 Prompt Engineering 2024

[Watch Swati Kumari's talk](https://www.conf42.com/Golang_2026_Swati_Kumari_beyond_chatbots_building)

[Watch the talk on YouTube](https://youtu.be/LGE4CZcwB0w).

## Watch the talk

[Beyond Chatbots: Building Actionable AI with Scalable Backend Integrations in Go](https://www.conf42.com/Golang_2026_Swati_Kumari_beyond_chatbots_building) at Conf42 Golang 2026.
