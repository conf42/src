# Coding agents need deterministic authorization, not self-judgment

Conf42 Blog, 2026-06-16, updated 2026-11-09. https://www.conf42.com/blog/llms2026/coding-agents-need-deterministic-authorization

In short: Sohan Maheshwar of AuthZed at Conf42 LLMs 2026 demos SpiceBox, which scopes Claude Code by path, command and domain using SpiceDB and ReBAC.

Letting a coding agent decide for itself what is safe means accepting that it will sometimes be wrong. Sohan Maheshwar, Lead Developer Advocate at AuthZed, opened his Conf42 Large Language Models 2026 talk with Anthropic's own analysis of Claude Code's auto-permissions mode, which reported a 17 percent false-negative rate on dangerous actions. His answer is to keep the model probabilistic and make the permission check deterministic, and he demos SpiceBox, a new open-source tool from AuthZed built on SpiceDB, doing exactly that.

So yes, this is a vendor's open-source project, presented by the company that builds it. The authorization reasoning holds up regardless of which tool you pick.

## Why role-based access falls short for agents

Maheshwar gives a fast tour of access models. Access lists do not scale. RBAC is simple until it causes role explosion and stale roles. ABAC is rule-heavy and hard to audit. ReBAC, relationship-based access control, expresses relationships between subjects and resources and answers permission checks as graph reachability: can you walk from the document through the reader relation to Jill?

The model comes from Google's 2019 Zanzibar paper, which described the system behind access checks in Docs, YouTube and other Google products. SpiceDB is AuthZed's open-source implementation of it, written in Go and exposed over gRPC and HTTP.

The agent-specific argument is about granularity. A developer role gets all the code or none of it. A coding agent needs narrower grants: write only to src, run only go test, fetch only from github.com. Scoping by path, command prefix and domain is where RBAC breaks and relationships fit.

He also reminds the audience that broken access control sat at the top of the OWASP Top 10 in both 2021 and the latest edition, before agents arrived to make things more interesting.

## English in, deterministic checks out

SpiceBox's workflow has six steps. You describe the permissions in plain English. SpiceBox calls the Claude API to translate them into explicit permissions such as file read and write on Go files in src, bash go test, web github.com. A human reviews and approves. SpiceBox writes the relationships into an in-memory SpiceDB, installs a Claude Code hook, applies the OS sandbox and starts a local egress proxy. You run the agent. On exit it tears all of that down.

The AI only drafts the policy. Every check after approval is deterministic: same question, same answer, every time.

## Three layers, denied by default

Enforcement sits at three levels, each able to say no:

- **A hook server** checks every tool call against SpiceDB, including read, glob and grep, which share the same permission so one cannot route around another. It runs out of process, so a prompt-injected model cannot rewrite the rules.
- **A kernel sandbox** (macOS sandbox-exec for now) makes the working directory read-only without a write grant, which stops shell tricks the hook might miss.
- **An egress proxy** allows only listed domains, which shuts the exfiltration path.

Maheshwar maps this onto the lethal trifecta of private data access, external communication and untrusted content, with each layer closing one leg. Reads are auto-approved by default; writes and executes ask for confirmation.

## The live demo

On a small Vercel template, he scopes Claude Code to write .ts and .tsx files only in components and to fetch from GitHub. Creating test.py there is refused; test.ts goes through. Fetching the SpiceBox README fails at first because web fetch was not granted, until a `spicebox grant` gives a temporary grant (about 15 minutes, he says) backed by a cryptographic token exchange.

He is clear about the gaps: bash is Turing complete so broad bash prefixes can be abused, the English-to-policy step still needs a careful human review, the kernel sandbox is macOS-only, and there are no everything-except-.env exclusions yet. His closing advice applies with or without SpiceBox: "Don't ask the model to decide if something is safe or not."

## Who should watch

Anyone running Claude Code or similar agents with permission prompts turned off, security engineers writing agent policies, and developers curious how Zanzibar-style authorization works under the hood. The ReBAC primer alone is worth the time.

## Related Conf42 talks

- [Who Is Calling Your Model? Identity and Authorization for AI Agents and ML Pipelines](https://www.conf42.com/MLOps_2026_Bhavik_Thakkar_identity_authorization_agents) from Conf42 MLOps 2026 takes agent authorization beyond the coding laptop.
- [Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) from Conf42 MLOps 2026 is about testing that the boundaries hold.
- [A Policy-as-Code Approach to RBAC Authorization](https://www.conf42.com/DevSecOps_2024_Graziano_Casto_policy_rbac_authorization) from Conf42 DevSecOps 2024 shows the role-based approach he contrasts with.

[Watch Sohan Maheshwar's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents)

[Watch the talk on YouTube](https://youtu.be/-kv_hqNIJfs).

## Watch the talk

[Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) at Conf42 Large Language Models (LLMs) 2026.
