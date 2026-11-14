# AI answers for API support should pass an expert before developers

Conf42 Blog, 2026-03-02, updated 2026-11-09. https://www.conf42.com/blog/sre2026/api-support-answers-need-an-expert-gate

In short: Vishal Shah (Visa) at Conf42 SRE 2026 on agentic RAG for API support where owners approve every answer and each correction trains the system.

A developer hits a 401 on an OAuth 2 call, searches, and finds a Stack Overflow answer from 2021 describing an auth flow that has since been deprecated. By the time a human expert sees the ticket, the misconfiguration is already in production. At Conf42 Site Reliability Engineering (SRE) 2026, Vishal Shah, a staff software engineer at Visa who works on LLMs and agent systems, presented Reliable API Support: an agentic RAG framework where the API owners approve every AI answer before a developer sees it, and every correction feeds back into the system.

## Too slow or too fast and wrong

Vishal calls the status quo a structural failure, not a documentation one. Support either waits on human bandwidth, which is slow, or runs a chatbot that produces confident, fluent answers with no grounding in current API behaviour. Docs go stale after a fast release; a model trained before the change will happily describe behaviour that no longer exists. For SREs, both paths end in incidents caused by your own support channel.

## Three components

**Multi-source retrieval.** The knowledge base is federated: API docs, versioned changelogs, internal incident reports, curated FAQs and verified community examples, each indexed with version, confidence tier and last-verified date. Retrieval is hybrid, dense embeddings plus sparse keyword search, because exact error codes need exact matching. With one such collection per product API, the corpus gets large fast.

**Provisional answers with a confidence score.** The agent runs a ReAct-style reason-act-observe loop until it has enough context, reconciles conflicting sources, and produces a proposed solution, the evidence behind it and a calibrated low, medium or high confidence. High confidence can be fast-tracked; low confidence is escalated as a priority.

**The expert gate.** Senior engineers on the owning team review the draft against the live API spec and approve, edit or reject. Vishal's preference is to push these reviews into Microsoft Teams, Slack or Discord so owners can approve from a phone. The corrected answer goes to the developer and is stored as a labelled example for the next retrieval re-ranking or fine-tuning cycle.

## The feedback loop is the product

The part Vishal is most excited about: every expert edit is a labelled signal (the agent proposed A, the expert changed it to B). Developer thumbs up or down adds another layer. More queries produce more corrections, which improve retrieval, which raises confidence, which lowers review load. The system earns autonomy through demonstrated accuracy rather than being granted it on day one.

He adds a realistic caveat: a product in early development with lots of new API features will produce low confidence for a while, while stable APIs get high scores quickly.

## A roadmap in three phases

He deliberately frames this as a slow build. Phase one is plumbing: the retrieval pipeline, initial indexing, a review interface, and baseline retrieval metrics (precision at K, mean reciprocal rank) measured before touching the LLM layer. Phase two puts real queries through, tunes confidence thresholds and wires corrections back in; that's where they first saw repeat ticket volume drop. Phase three is scale and dashboards for accuracy, satisfaction and expert review time.

His four principles are worth pinning up: ground every response, calibrate confidence explicitly, make human review a first-class component, and close the loop. The warning attached to the third is the most practical line in the talk: if reviewing a draft takes more effort than writing the answer, experts will route around your system.

To start, he suggests pulling the last three months of support tickets, finding the top 10 recurring error types, and building the retrieval layer for those first.

## Who should watch

Platform and developer-experience teams running internal API support, and anyone shipping RAG where a wrong answer causes an outage rather than an awkward reply. It is an architecture talk; there are no published results beyond the qualitative drop in repeat tickets.

## Related Conf42 talks

- [Human-in-the-Loop MLOps: Production Patterns](https://www.conf42.com/MLOps_2025_Tejasvi_Nuthalapati_human_loop_mlops) by Tejasvi Nuthalapati (Amazon), the same gate applied to model operations.
- [RAG Beyond Chatbots: Transforming Customer Support with Observable Intelligence](https://www.conf42.com/Observability_2025_Vaibhav_Fanindra_Mahajan_rag_chatbots) by Vaibhav Fanindra Mahajan.
- [Beyond Basic RAG: Better Context for More Reliable Enterprise AI](https://www.conf42.com/Prompt_Engineering_2026_Ravi_Ray_rag_context_enterprise) by Ravi Ray, on the retrieval side.

[Watch Vishal Shah's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human)

[Watch the talk on YouTube](https://youtu.be/i4Hn2umVFtM).

## Watch the talk

[Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human) at Conf42 Site Reliability Engineering (SRE) 2026.
