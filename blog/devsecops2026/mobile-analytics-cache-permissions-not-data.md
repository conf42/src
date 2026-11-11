# Mobile analytics security: cache the permission, never the data

Conf42 Blog, 2026-09-19, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/mobile-analytics-cache-permissions-not-data

In short: At Conf42 DevSecOps 2026, Tesla's Ashwin Kumar treats identity, authorization and latency as one problem for analytics on personal phones.

When the plant manager checks shift numbers on a personal phone, your perimeter has already lost. At Conf42 DevSecOps 2026, Ashwin Kumar, Senior Manager of Data Engineering and Analytics at Tesla, argued that identity, authorization and performance for mobile analytics are one design problem, and that splitting them across three teams is exactly where the gaps appear. He notes up front that the views are his own and were not reviewed by Tesla.

## Three teams, three seams

The usual org chart hands login to the identity team, data permissions to the data team and responsiveness to the app team. Each solves its slice. Kumar's point is that the seams between those slices are where attackers live, and that mobile makes the seams wider, because operational leaders now read dashboards on the floor, in meetings and at home, on devices nobody enrolled in management.

The talk is short and tightly structured: five areas, each with a concrete mechanism.

## Bind identity, not the device

He starts from a principle: a personal phone touching operational data must carry the same trust guarantee as a managed laptop. Asking everyone to enrol their own phone in MDM fails socially, and he thinks it should fail. So trust is layered instead. Device attestation checks the OS has not been tampered with and uses hardware-backed keys. Corporate identity federation adds SSO with certificate-backed tokens. Continuous session validation re-evaluates risk signals on every request rather than once at login.

His summary line is a good one: trust is an envelope that travels with every call, not a gate you pass once.

## Strict and fast means caching the decision

On desktop a half-second permission check goes unnoticed. On a phone it feels broken, and users either quit or invent workarounds, which is worse. Kumar's answer has three parts. Pre-compute role resolution and cache it at the edge, keyed to the identity token and the data scope. Give every entry a strict TTL and force revalidation when a role or policy changes. And fail closed: a cache miss or a degraded network means deny.

The trick in one phrase from the talk: cache the permission decision, not the data. That is how you get strictness the device context demands and speed the user expects.

## Enforce policy where data is joined

A mobile dashboard can pull manufacturing, sales, service and workforce data, each with its own owner and access rules. The common mistake is to join it all and hide what the user should not see in the UI. That means the sensitive data already sits in a payload on a personal device. His rule: enforce policy at integration, not presentation.

Drill-down sharpens it. Broad authorization is enough for the enterprise summary. Tapping into a facility revalidates regional or departmental scope. Tapping into individual performance data triggers a final check. A broad grant at the top must never quietly open restricted detail at the bottom.

Freshness gets the same treatment. Queries are scoped at read time in the distributed warehouse, so access changes show up on the next query. Payloads carry a permission fingerprint that is invalidated if policy changes mid-session. Push alerts are permission-checked on the server before they leave.

## Authorize the query, not just the user

The last section is about natural language querying and AI-generated alerts. An AI summary can aggregate across scope boundaries without anyone noticing, and a RAG pipeline that retrieves everything and filters afterwards has already touched data it should not have. His fix is query-scoped authorization: map the identity token to permitted data domains before retrieval, run retrieval only against those partitions, vector search included, and generate the answer from that scoped context alone. He calls it a first-class architectural concern, not a filter bolted onto the output.

## Who should watch

Anyone building internal analytics or RAG features that reach phones, and identity engineers who have been asked to make BYOD safe without MDM. It is an architecture talk at around twenty minutes, with patterns rather than code, so it suits a lunch break.

## Related Conf42 talks

- [Sohan Maheshwar on deterministic authorization for coding agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents), the agent-side cousin of query-scoped access.
- [Graziano Casto on a policy-as-code approach to RBAC](https://www.conf42.com/DevSecOps_2024_Graziano_Casto_policy_rbac_authorization).
- [Sheshananda Reddy Kandula on automating mobile app security assessments with MobSF and Jenkins](https://www.conf42.com/DevOps_2025_Sheshananda_Reddy_Kandula_mobile_security_automation).

[Watch Ashwin Kumar's talk](https://www.conf42.com/DevSecOps_2026_Ashwin_Kumar_mobile_authorization_identity)

[Watch the talk on YouTube](https://youtu.be/ZTEGZ_RHX-o).

## Watch the talk

[Securing Real Time Mobile Analytics: Identity Binding and Low Latency Authorization for Distributed Enterprise Data](https://www.conf42.com/DevSecOps_2026_Ashwin_Kumar_mobile_authorization_identity) at Conf42 DevSecOps 2026.
