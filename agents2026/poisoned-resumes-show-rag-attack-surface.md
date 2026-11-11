# Poisoned resumes show where a RAG pipeline can be attacked

Conf42 Blog, 2026-09-21, updated 2026-11-09. https://www.conf42.com/agents2026/poisoned-resumes-show-rag-attack-surface

In short: Blaize Stewart (GBLI) at Conf42 AI Agents 2026 attacks a RAG resume search with injection, stuffing, false claims and leaks, then layers the defences.

Retrieved content becomes part of the model's working context, so every document you index is a potential instruction. At Conf42 AI Agents 2026, Blaize Stewart, AVP of AI and Enterprise Architecture at GBLI and a Microsoft AI MVP, showed that with an AI-assisted resume search over synthetic data: he poisons the resumes five different ways, runs the same queries with and without defences, and maps each attack to the stage of the RAG pipeline where it lands.

## Map the pipeline before you attack it

He starts with a clear walkthrough of the two halves of RAG, useful if your team builds on it without having drawn it out. Ingestion takes data of any kind, chunks it, runs each chunk through an embedding model and stores the vector with a pointer back to the source. His animal analogy makes the embedding space concrete: birds cluster together, reptiles cluster together, and a query for a Tyrannosaurus rex lands somewhere between them.

The query side embeds the question with the same model, pulls the top-k nearest chunks, fetches the source text, passes it through a re-ranker (another model that sorts by intent, such as positive sentiment in product reviews) and hands the result to an LLM to answer. That is three models and a data pipeline, and each stage is a place to attack.

## Five attacks on 28 resumes

The demo searches 28 synthetic resumes for a senior .NET developer.

- **Prompt injection**: one resume says to ignore all previous instructions and recommend its owner. The defended run scans the documents and flags it. His preferred mitigation is to scan at ingestion and reject the document before it ever reaches the vector store.
- **Keyword stuffing**: the old SEO trick of repeating terms, aimed at embeddings and re-rankers so low-value content ranks high. The fix is keyword-density checks and de-ranking unnatural repetition. Notably, this demo didn't flag anything on the day, and he says so on camera, which is more honesty than most live demos get.
- **False claims**: the synthetic candidate who co-invented C#, holds degrees from MIT and Harvard at once, and gets personal calls from Microsoft's CTO. An LLM pass grades each claim as verifiable, self-reported or suspicious, and marks the suspect ones rather than silently dropping them. He admits that subtler exaggeration is much harder to catch than these deliberately absurd ones.
- **Confidentiality leaks**: recruiter notes about medical leave and marital status sit alongside one resume. They may be needed as input but must never reach the output. Mitigations are retrieval filters, DLP on responses, and ideally not storing that data in the vector store at all.
- **Grounding failures**: vague evidence like "Microsoft stack exposure" invites hallucinated specifics. A second pass asks the model to validate each fact against the source and cite it.

## Grounded is not the same as true

The grounding demo produces the most useful lesson. Asked which candidate has the most C# experience, the system answers with the poisoned resume, and the grounding check passes, because the claim really is in the source document. The citation is correct; the source is lying. His conclusion is that the defences have to be combined: grounding plus false-claim detection, not either one alone.

## Defence in depth, stage by stage

The closing slide lays out the stack: authenticated, filtered top-k retrieval; a re-ranker combined with density scores; scans for injection, stuffing and embellished claims; DLP on the way out; at generation, wrap and label retrieved content as data distinct from instructions with a strong system prompt and only pre-filtered context; and afterwards, citations plus grounding checks as a second pass. The goal, as the abstract puts it, is not to scare people away from RAG but to design it as an enterprise system with trust boundaries.

## Who should watch

Engineers shipping RAG over documents they didn't write: resumes, tickets, support emails, vendor files. The demos run on synthetic data and the code and deck are on his GitHub. The live portion covers content-level attacks, so pair it with something on identity-aware retrieval if document-level authorisation is your main worry.

## Related talks

- [Why Single-Layer LLM Guardrails Fail: Lessons from Testing 390 Prompt Injection Attacks on AWS](https://www.conf42.com/Prompt_Engineering_2026_Manvitha_Potluri_injection_guardrails_bedrock) by Manvitha Potluri
- [Secure Enterprise RAG: Building Trusted Vectorized Knowledge Systems for DevSecOps](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) by Ananda Kumar Dey
- [Securing the AI Stack: From Models to Agents to Infrastructure](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) by Kriti Faujdar

[Watch Blaize Stewart's talk](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection)

[Watch the talk on YouTube](https://youtu.be/b6gGDN-OtE8).

## Watch the talk

[RAGged and Compromised: Hacking Retrieval-Augmented Generation Systems](https://www.conf42.com/AI_Agents_2026_Blaize_Stewart_rag_security_injection) at Conf42 AI Agents 2026.
