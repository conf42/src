# AI pricing in SAP works when the model can recommend but never write

Conf42 Blog, 2026-09-20, updated 2026-11-09. https://www.conf42.com/devsecops2026/ai-pricing-sap-recommends-sap-decides

In short: At Conf42 DevSecOps 2026, Sirisha Ayyagari shows a zero-trust pattern for AI pricing in SAP: stateless AI, BAdI hooks, ABAP guardrails, full audit.

The safest AI integration in a financial system is one where the model never holds a pen. At Conf42 DevSecOps 2026, software developer Sirisha Ayyagari walked through an architecture for plugging an external AI pricing engine into SAP, built on one rule she repeats throughout: "AI recommends, SAP validates, and SAP decides."

## Why pricing is the dangerous place to start

Pricing sits inside order-to-cash. A price lands on a sales order, then an invoice, then revenue recognition and financial reporting. Ayyagari's opening point is that most AI conversations ask what the model can do, and in ERP you also have to ask what it must never be allowed to do. Her three concerns are system integrity, auditability and financial control, and she is blunt that security has to be in the design from day one rather than retrofitted after the first audit finding.

## Stateless AI, stateful SAP

The boundary is drawn before any model is picked. The AI engine receives pricing context and returns a recommendation. It does not own the transaction, does not update the sales order or the billing document, and has zero write access to core financial objects. SAP keeps sole authority over transactional consistency and validation.

Her threat model explains why. An AI service account with write access is an external system with too much authority. Model output that is not sanitised can fall outside the expected range or arrive in the wrong structure. Security deferred "until later" is how financial controls end up full of exceptions. And without a rollback path, a model that starts producing bad numbers keeps doing so across thousands of orders before anyone pulls the plug.

## Clean core: BAdIs and an HTTP boundary

Technically, SAP sends context over an authenticated HTTP API, and the recommendation comes back through a BAdI extension point. That matters for two reasons. BAdIs are SAP-sanctioned extensibility, so no standard object is modified and upgrades stay safe. And the extension has its own life cycle, so it can be audited or replaced independently of the AI vendor.

The API boundary itself carries the security: mutual authentication, least privilege so the AI service only sees the context it needs, strict request and response schemas, and rate limiting at the gateway. The design does not rely on the model to protect the enterprise system. Anyone who has been asked to trust an LLM's self-restraint will appreciate that.

## Four guardrails and an ABAP sequence

At runtime she layers four controls: authenticated, logged and rate-limited calls; output validation against price boundaries, business rules and the schema; least-privilege access that keeps the AI out of SD and FI write paths; and circuit breakers. If the service goes down, latency spikes or recommendations drift out of range, the breaker trips and pricing falls back to native rule-based SAP pricing, so order-to-cash keeps running.

On the ABAP side the sequence is short and worth copying. Call the API with a hard timeout. Validate the response: out-of-range values are rejected, not shown as a warning, and a malformed structure raises an exception before it reaches the pricing transaction. Apply or fall back. Log the outcome either way.

## The audit trail answers "why this price?"

Logging here means a business audit trail, not HTTP status codes. For each decision she records the input context sent to the model, the raw recommendation, the validation outcome (accepted, rejected or fallback), the price SAP actually applied, the SAP document where it was committed, plus timestamp and service identity. When an auditor asks why a transaction got a particular price, there is a chain from recommendation to commit.

Her closing blueprint: threat-model first and decide what AI can read and never write; use BAdI plus HTTP for a clean core pattern; build failure into the design; log and justify every decision.

## Who should watch

SAP architects and ABAP developers being asked to "add AI" to pricing, discounting or any other money-moving process, and security reviewers who need a reference pattern to hold vendors to. It is a design talk without a live demo; the value is the boundary and the order of checks.

## Related Conf42 talks

- [Pon Murugesh Devendren on event-driven AI agents for SAP incident management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events).
- [Gobinath Kasimayan on AI-driven master data governance in SAP](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility).
- [Vijayakumar Venganti on automating zero-trust verification in DevOps pipelines](https://www.conf42.com/DevOps_2026_Vijayakumar_Venganti_zerotrust_security_networks).

[Watch Sirisha Ayyagari's talk](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing)

[Watch the talk on YouTube](https://youtu.be/K2-KFfvy9cY).

## Watch the talk

[Securing the AI Perimeter: Building Zero-Trust Integration Patterns for AI-Driven Pricing in SAP](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing) at Conf42 DevSecOps 2026.
