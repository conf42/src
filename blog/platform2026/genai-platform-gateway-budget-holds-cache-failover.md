# Treat tokens like money: a GenAI gateway with budget holds

Conf42 Blog, 2026-10-13, updated 2026-11-09. https://www.conf42.com/blog/platform2026/genai-platform-gateway-budget-holds-cache-failover

In short: Brindal Patel of Coinbase at Conf42 Platform Engineering 2026 on a GenAI gateway with card-style token budgets, safe semantic caching and eval-gated failover.

A background service hits a timeout, enters a fast retry loop, and every retry calls an expensive foundation model with a shared API key pasted into a config file. By morning the bill is enormous, nobody can tell which service did it, and revoking the key breaks production for every other team. At Conf42 Platform Engineering 2026, Brindal Patel, a senior software engineer at Coinbase, called that a missing platform contract, not an AI problem, and laid out the gateway that supplies one.

He's clear at the start that the talk is based on his own experience and independent work, not affiliated with or endorsed by his employer.

## The paved road is one YAML file

The product contract is small. A team opens one pull request with a short YAML file and gets back a model alias (no vendor SDK, no key in the repo), a budget with a named owner, and a distributed trace for every call. That replaces the N-times-M mess of every team wiring every provider: scattered keys, no owner for spend, uncoordinated rate limits, and the same prompt paid for again and again.

A request passes six stages: mTLS and a token identify the calling team; an Envoy external-processing filter strips PII and secrets; Open Policy Agent decides; the gateway places a budget hold; a tenant-scoped cache gets a chance to answer; otherwise the call routes to a model and the bill settles. Each stage emits an OpenTelemetry span, and MCP tool calls go through the same door and the same policy.

## Budget tokens like a card payment

The first idea is the one to steal. You don't know output cost until the model finishes, so ten parallel requests can all pass an under-budget check and overrun together. Brindal borrows from card payments: authorise a hold for the worst case (input tokens plus max output), capture only what the response reports, release the rest. For broken streams, cancel upstream, settle what was used, release the remainder. The check and the hold are one atomic step, so parallel calls can't spend the same budget twice.

## Similar is not the same when money moves

The second idea is a warning about semantic caching. "Send one hundred dollars to my savings" and "send one thousand" look almost identical to an embedding model. After PII redaction, everyone's balance question looks like the same text. So before serving a cached answer the gateway checks four things: same scope (tenant, model, system prompt, decoding settings), similarity above a threshold tuned per model, matching entities compared by hash so raw account numbers are never stored, and whether this prompt should be cached at all. Transactional and per-user prompts never are.

He frames caching as a ladder you climb only as far as your checks allow: provider prompt caching for shared prefixes, then exact-match, then semantic behind the four checks, and for self-hosted models, KV-cache-aware routing to GPU workers whose prefixes are already warm.

## Fail over only to models that passed your evals

The third idea: an untested backup might ignore your JSON schema or answer worse. Evals run in CI on every model change, and the runtime router only reads an in-memory passed flag. On a 500, timeout or 429, it walks the tenant's approved list, skips anything that didn't pass that tenant's evals, tags the span as a failover, and returns a clear error if nothing is left. Never a silent downgrade.

The policy itself is shown as Rego for OPA 1.x: default deny, allow only if the model is on the tenant's lease, the data scan is clean and the hold fits, with an optional degrade to a smaller internal model. Allow and degrade can never both match.

## Practical edges

The tracing tips are concrete: name model spans the OpenTelemetry way, keep gateway infrastructure on the resource and the calling tenant on each request span for chargeback, and pin your schema version because the GenAI conventions are still in development. His four review-time mistakes are worth a sticky note: shared caches across tenants, budget checks after the call, failover to any model that answers, and embedding prompts before redaction.

## Who should watch

Platform teams turning ad-hoc LLM usage into a shared service, and anyone who has had to explain a surprise model bill. It's short and dense with patterns; his advice is to start with quick wins and avoid writing a gateway from scratch.

## Related Conf42 talks

- [Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) by Elizabeth Fuentes Leone at Conf42 AI Agents 2026.
- [When AI Joins the Request Path: Securing API-Backed AI Systems](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) by Jayakumar Ramalingam at Conf42 DevSecOps 2026.

[Watch Brindal Patel's talk](https://www.conf42.com/Platform_Engineering_2026_Brindal_Patel_idp_generative_apis) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/g5ZSChaET_8).

## Watch the talk

[Building the Internal Developer Platform (IDP) for Generative AI: From Foundation Models to Self-Service APIs](https://www.conf42.com/Platform_Engineering_2026_Brindal_Patel_idp_generative_apis) at Conf42 Platform Engineering 2026.
