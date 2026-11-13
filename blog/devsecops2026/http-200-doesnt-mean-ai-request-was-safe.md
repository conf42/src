# An HTTP 200 doesn't mean the AI-backed request was safe

Conf42 Blog, 2026-09-07, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/http-200-doesnt-mean-ai-request-was-safe

In short: Jayakumar Ramalingam of SiriusXM at Conf42 DevSecOps 2026 secures AI-backed APIs hop by hop with deterministic checks around a probabilistic model.

"Can you explain this charge on my bill?" looks like one API call. Behind it sit identity, private account data, a model inference, a policy decision and possibly a refund in the system of record. At Conf42 DevSecOps 2026, Jayakumar Ramalingam, Staff Software Engineer at SiriusXM, used that billing assistant as a running example to show how to secure an API once AI joins the request path: keep the model in the middle, and make every check around it deterministic.

This is a checklist talk in the best sense. No new framework, just the boundaries you already have, drawn more carefully.

## Draw the path before you defend it

Jayakumar splits the request into six hops: client, gateway, context, model, tools, response. Each hop can add data, change authority, time out or return half an answer. A valid identity at the gateway doesn't prove every retrieved document belongs to that customer, and a model suggesting a tool doesn't mean it may run one.

His first exercise is cheap: pick one endpoint, draw the whole path, and mark where untrusted data enters, where private data is added, where credentials are used and where state changes elsewhere. That gives you a threat model and a shared picture for design reviews and incident reports, so people point at a hop instead of talking about "the AI" as one box.

The classic controls stay: authentication, object-level authorization, request size and rate limits, an endpoint inventory, the OWASP API Top 10. AI makes them matter more, because a weak authorization check now leaks into retrieval, logs and downstream actions.

## A valid request can still end badly

The new problem is ambiguity inside a perfectly valid request. The response can be well formed and still reveal too much. Retrieved text can carry instructions aimed at the model. A fallback can run with weaker controls than the main path. An HTTP 200 tells you the transport completed, not that the right documents arrived or the action was authorized.

His sharpest example: the model returns a valid tool name and a $900 refund amount. The JSON passes the schema. The application still has to check the customer's entitlement, the amount limit, the account state and whether confirmation is needed. The schema tells you the answer has the right shape, not whether the action is allowed. So validation happens before inference (limit what context can be retrieved, send only what's needed) and after it (structure, allowed fields, sensitive data, policy), with permission decisions in code and policy systems rather than prompts.

## Authorization is a chain, not a front door

The confused deputy shows up here: an agent with broad credentials acting for a user with narrow rights, while taking instructions from text it retrieved. The fix is a check at every hop: endpoint, object, context, tool and downstream service, with the downstream service enforcing its own rules even after the broker approved. A household member may see their own bill but not another account's, and may ask for an explanation without being allowed to change a payment.

Retrieved content is data, not instructions. Filter by tenant before retrieval, keep source and chunk IDs, and remember that citations are evidence, not permissions. He also flags the quieter risk: write access to the index deserves the same attention as read access, because whoever can publish material can steer later answers.

## Narrow tools, one budget, honest fallbacks

Tools go through a narrow broker that checks the tool, validates arguments, confirms the caller's permission, applies limits and picks a scoped credential. A tool that fetches one order's status is far safer than one that can call any URL. State-changing calls get an idempotency key so a retry doesn't refund twice.

Rate limits count requests, but one AI request can cost far more than another, so Jayakumar wants one budget per request covering tokens, retrieval fan-out, model latency and tool calls. When it runs out, fail usefully. Fallbacks should do less under the same authorization rules; never quietly switch to a less protected model or a more privileged credential to finish the job.

The rest is operational: log trace IDs, policy outcomes, prompt and model versions and source IDs without copying documents into logs; alert on shifts in policy denials or stale retrieval, not just latency; version prompts, policies and retrieval config together, because rolling back only the model won't restore old behaviour; and run a regression corpus with a pass-rate threshold, since a flaky security gate eventually gets switched off.

## Who should watch

Backend and platform engineers adding an LLM call to an existing API, and AppSec folks reviewing one. You'll recognise most controls; the value is seeing where each one goes on a request that now has a probabilistic step in the middle.

## Related Conf42 talks

- [Building the Internal Developer Platform (IDP) for Generative AI: From Foundation Models to Self-Service APIs](https://www.conf42.com/Platform_Engineering_2026_Brindal_Patel_idp_generative_apis) by Brindal Patel of Coinbase at Conf42 Platform Engineering 2026.
- [From Self-Service to Safe Autonomy: The Authority Shift](https://www.conf42.com/Platform_Engineering_2026_Ruby_Agarwal_autonomy_service_authority) by Ruby Agarwal of Avaya at Conf42 Platform Engineering 2026.
- [Securing Payment Gateway Evolution: DevSecOps in Microservices Migration](https://www.conf42.com/DevSecOps_2025_Silpa_Potluri_payment_api_secure) by Silpa Potluri of GoodLeap at Conf42 DevSecOps 2025.

[Watch Jayakumar Ramalingam's talk](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/itML9SKOziQ).

## Watch the talk

[When AI Joins the Request Path: Securing API-Backed AI Systems](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) at Conf42 DevSecOps 2026.
