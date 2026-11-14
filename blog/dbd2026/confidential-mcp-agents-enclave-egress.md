# Your enclave is secure. The agent's SQL query is not

Conf42 Blog, 2026-05-06, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/confidential-mcp-agents-enclave-egress

In short: Ankur Aggarwal of Meta at Conf42 Database DevOps 2026 on Confidential MCP: attestation, PII transforms and egress policies for agents that query databases.

You can run an LLM inside a trusted execution environment where nobody can see what it is doing, and then watch it send a SQL query over a plain connection to a database that has no idea it is talking to an enclave. At Conf42 Database DevOps 2026, Ankur Aggarwal, Senior Software Engineer at Meta working on privacy-preserving AI infrastructure, introduced Confidential MCP (C-MCP), a backwards-compatible extension to Anthropic's Model Context Protocol that closes that gap.

The talk is about twenty minutes and dense. It is a design talk, with architecture and operational lessons, not a code walkthrough.

## Agents turn one door into a hallway

Why is this harder than ordinary API security? Ankur gives three reasons. Agents run long reasoning chains, so a single workflow can issue ten to twenty tool calls, each a possible exfiltration path. They query live, sensitive data: health records, ledgers, legal documents. And the subtle one: cumulative leakage. No single call reveals much, but fragments pile up in the context window until the model can reconstruct a full patient record or financial profile.

## Where plain MCP falls over

MCP assumes connected, trusted environments, and Ankur names three places it breaks at an enclave boundary:

- **Transport.** TLS encrypts the channel but cannot prove the other end is running inside a legitimate TEE. You need mutual attestation, and MCP has none.
- **Discovery.** Agents ask servers for their tool and schema manifests at runtime. In a confidential setting the schema itself is sensitive: it tells you which data and columns exist, before any query runs.
- **Credentials.** MCP expects bearer tokens, OAuth or API keys. Enclaves have attestation instead, and MCP has no native way to delegate credentials based on it.

## Three primitives, enforced by cryptography

C-MCP adds three pieces on top of MCP, with a design that draws on Meta's WhatsApp Private Processing work.

A **three-zone topology**: an untrusted client zone, the confidential enclave holding the C-MCP runtime and the agent (the only zone that ever sees raw data), and a data plane of databases and tool servers that answer only attested requests. Ankur compares it to a DMZ with cryptographic enforcement instead of firewall rules.

An **Anonymization Transform Layer** between the database and the model. It suppresses PII at the token level before results enter the context window, logs every redaction for audit, and runs an entropy budget across the whole workflow. That last part is the answer to cumulative leakage: once the total identifying information crosses a ceiling, further queries are blocked or restricted, even if each field passed on its own.

**Attested egress policies**. Security and compliance teams write rules for which fields may leave the enclave, at what cardinality and to whom. The policies are bound to the enclave measurement at boot through remote attestation, so a compromised runtime cannot loosen them. Every outbound response is checked; anything non-compliant is blocked and flagged. Think firewall rules for data semantics rather than packets.

## Production found the problems the diagram didn't

The operational section is where the talk earns its slot. The first surprise was query overreach: smaller open-source models, and some larger ones, reach for `SELECT *` or whole tables when they need two columns or one row. Redacting afterwards is the wrong layer, so Ankur argues for query normalization, a least-privilege query planner between the model's intent and the SQL that runs.

The second is cumulative risk made concrete. He describes cases where a model could not see a patient's name, but date of birth, ZIP code, diagnosis code and prescription history, fetched in separate calls, were enough to identify the person. Every redaction passed; the sum did not.

The third is latency. Attestation handshakes, transforms and policy checks add 15 to 40 milliseconds per tool call, and sometimes 100 to 200 milliseconds depending on policy complexity and response size. Fine for batch analytics, painful under a sub-100 ms SLA. Precomputed attestation caches, lazy policy evaluation and response streaming brought it back to acceptable levels.

## Compliance as boot configuration

Because egress policies are baked into the boot measurement, regulations become templates: HIPAA's minimum necessary standard for clinical pipelines, GLBA sharing limits and GDPR cross-border controls for AML analytics, attorney-client privilege for contract intelligence. Ankur's closing line is the takeaway: without enforceable egress policies you rely on "model behavior and hope".

## Who should watch

Anyone wiring agents to production databases in regulated domains, and security engineers who assumed confidential inference covered the data path too. It doesn't, and this talk explains why in plain terms. If your agents only read public docs, file it for later.

## Related Conf42 talks

- [Moritz Eckert on confidential computing with Intel SGX](https://www.conf42.com/Golang_2021_Moritz_Eckert_confidential_computing_Intel_SGX_security_cloud_native) at Conf42 Golang 2021.
- [Alex Shershebnev on securing MCP in the cloud](https://www.conf42.com/DevSecOps_2025_Alex_Shershebnev_cloud_mcp_secure) at Conf42 DevSecOps 2025.
- [Srinivas Vallabhaneni on enclaves and confidential security](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential) at Conf42 Golang 2025.

[Watch Ankur Aggarwal's talk](https://www.conf42.com/Database_DevOps_2026_Ankur_Aggarwal_llm_inference_models)

[Watch the talk on YouTube](https://youtu.be/8dLybdrZI6A).

## Watch the talk

[Securing Agentic AI Data Flows: Confidential MCP for Privacy-Safe Tooling in Database-Driven Systems](https://www.conf42.com/Database_DevOps_2026_Ankur_Aggarwal_llm_inference_models) at Conf42 Database DevOps 2026.
