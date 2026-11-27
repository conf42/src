# Prompts are not a permission system: identity for agents and pipelines

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/identity-authorization-ai-agents-ml-pipelines

In short: Bhavik Thakkar (Okta) at Conf42 MLOps 2026 on replacing shared API keys with workload identity, delegation and short-lived scoped tokens for agents.

Ask most ML platform teams who is calling their model and the honest answer is that somebody holding the shared API key is. At Conf42 MLOps 2026, Bhavik Thakkar, Senior Product Manager at Okta working on identity and authorization for AI agents, argues that every model call should answer three questions: who is calling, on whose behalf, and allowed to do what. He then walks through five building blocks that get you there using open standards, with no vendor required.

## The shared key was a fair trade until agents showed up

Bhavik sorts the callers into three groups: pipelines and ML jobs (nightly training, CI pushing a model to the registry, hourly batch scoring), services (inference endpoints calling the feature store), and AI agents. An agent decides at runtime which tools and models to call, often acts for a specific person, and can be manipulated by what it reads.

Almost none of these callers type a password, and most authenticate with one long-lived key. He lists what happens as the caller count grows. The key gets copied into notebooks, CI variables, laptop environment files and now MCP server config files. It carries the union of everyone's permissions. The logs show that the key was used and nothing about which job used it. And rotating it breaks every caller at once, so nobody rotates it and it lives for years.

## Identity should come from where the code runs

Building block one is workload identity: the platform attests the workload (namespace, service account, container image, repository and branch) and hands it a short-lived identity document. Bhavik covers two routes. SPIFFE gives each workload a URI-style ID and a verifiable credential, issued and rotated by SPIRE, typically every hour or less. OIDC workload federation does the same job with tokens that most clouds and CI systems already issue.

His worked example is a retailer running hundreds of agents. The admin sets up trust between the auth server and the company's SPIFFE trust domain once. After that, an inventory agent presents its SPIFFE credential in place of a client secret and gets back a scoped, short-lived OAuth access token. The API it calls only ever sees a standard token. In his words, "you add the hundred and first agent without creating a hundred and first secret".

Block two is delegation. A support rep asks an assistant to summarise a customer's last five tickets. If the agent uses its own broad credentials it can read every ticket in the company. With OAuth token exchange (RFC 8693) the agent presents the user's token plus its own identity and receives a token that names both: the user as subject, the agent as actor. Block three swaps the forever-key for tokens that live for minutes and cover one task. His tip is to start coarse, with one scope per model and one per tool, and to keep scope decisions in the auth server's policy so you can change them without redeploying agents.

## The model decides what it wants, the auth layer decides what it gets

The section most agent builders should replay is about MCP. A system prompt that says "only read records, never delete anything" is a hope. "Prompts are not a permission system," Bhavik Thakkar said at Conf42 MLOps 2026. A support ticket with hidden text asking to export every customer's email will get past a check that lives in the model's judgment.

The fix is to authorize at the tool. Under the MCP authorization spec an MCP server acts as an OAuth resource server and, on every tool call, validates the token, checks it was issued for this server, and checks the scope for that tool and that user. A tricked model can ask for the export; the export tool refuses because the token does not carry the scope.

He also covers how a server knows which agent client is connecting. Hand registration does not scale and open Dynamic Client Registration leaves thousands of anonymous one-off records. Client ID Metadata Documents make the client ID an HTTPS URL that the server fetches, which anchors the client to a domain somebody controls.

## Approvals people don't learn to ignore, and a kill switch you have timed

Block four is human approval for irreversible or sensitive actions: deleting data, sending external email, deploying to production, moving money. Synchronous confirmation works when the user is in the session; for background agents he points to OpenID's CIBA, where an approver gets a push on a trusted device and the agent waits for its token. Ask for everything and approval turns into theater, so ask only for what matters and let approvals expire with the task.

Block five is audit and revocation. Log six things per call: the caller, the user, the grant and scope, the model and version, the data touched, and the approval. Then practise revocation like a disaster recovery drill: pick one agent in staging and time how long it takes to cut it off. With short-lived tokens that is minutes, and every other caller keeps running.

He closes with four failure patterns (over-scoped tokens, the confused deputy, invisible agent-to-agent hops, the missing kill switch) and six steps to start with.

## Who should watch

ML platform engineers, security engineers and anyone putting an MCP server in front of real data. It is a vendor-neutral reference-architecture talk with diagrams and no live demo. If you already run SPIRE and token exchange in production, the MCP and CIMD sections are the new material.

## Related Conf42 talks

- [Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) by Ajay Munjuluru at Conf42 MLOps 2026.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar (AuthZed) at Conf42 Large Language Models 2026.
- [Adding Tamper-Evident Audit Trails to AI Agents in Production](https://www.conf42.com/MLOps_2026_Joao_Marques_audit_tamper_agents) by Joao Marques at Conf42 MLOps 2026.

[Watch Bhavik Thakkar's talk](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Who Is Calling Your Model? Identity and Authorization for AI Agents and ML Pipelines](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) at Conf42 MLOps 2026.
