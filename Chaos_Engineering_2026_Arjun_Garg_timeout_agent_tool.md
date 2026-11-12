# A Timeout Is Not a Failed Action: Chaos Testing AI Agent Tool Calls

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Arjun Garg](https://www.conf42.com/speaker_Arjun_Garg) (Senior Engineering Manager @ Intuit). Page: https://www.conf42.com/Chaos_Engineering_2026_Arjun_Garg_timeout_agent_tool

## Abstract

Chaos engineering is most valuable when it tests assumptions that ordinary success-path metrics cannot reveal. This session injects a deterministic lost response after an AI agent's mutating tool has committed an external effect. The agent observes a timeout, retries with a fresh request ID, and produces two effects for one logical operation. Using a public MCP reproduction and independent third-party replication, the session distinguishes transport request identity, logical-operation identity, and durable effect state. It compares caller-supplied idempotency keys, server-local ledgers, downstream cooperation, and reconciliation through independent read-back. Each defense has limitations: reserving a key does not establish that an external effect completed, and missing read-back does not necessarily establish non-execution. Attendees leave with a fault-injection matrix, positive and negative controls, and a recovery decision tree for safe retry, reconciliation, and explicitly unknown outcomes.
