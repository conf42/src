# Your agent can reason fine. It just remembers the wrong things

Conf42 Blog, 2026-05-19, updated 2026-11-09. https://www.conf42.com/blog/llms2026/agent-memory-failures-disguised-as-reasoning

In short: Anannya Roy Chowdhury (AWS) at Conf42 LLMs 2026: a Harry Potter game shows agent failures are memory failures, fixed with three memory layers.

Most agent failures are memory failures wearing a reasoning costume. That is the claim Anannya Roy Chowdhury, GenAI Developer Advocate at AWS, makes at Conf42 Large Language Models (LLMs) 2026, and she backs it with a game her own agent kept losing: eight times out of ten, before she changed how it remembered things.

The game is a Horcrux hunt. Harry gets 50 turns to find and destroy Horcruxes across 15 locations; Voldemort spends those turns relocating them and planting decoys. Same model, same tools, same retrieval. The fix in the talk never touches the model.

## The model knew how to think

Anannya started where everyone starts: she blamed the prompt, then the model, then the architecture. Reading the failures told a different story. Harry destroyed a location after the Horcrux had already moved (stale memory). He revisited a spot already confirmed empty, because the signal was buried under tokens (retrieval failure). And the most common problem was the agent remembering everything, so each turn got slower and more expensive.

Her framing for the last one is worth stealing. A context window is less a storage limit and more a compounding tax: replay the whole history on every one of 50 turns and you are rereading the book every time you turn a page. Add more agents and the bill multiplies.

## Memory is entropy management

The lens for the rest of the talk comes from information theory. At turn one Harry knows nothing, so every location is equally likely. Each observation should lower that uncertainty; each Voldemort move raises it. Every memory decision then answers one question: does this help reduce uncertainty or add to it?

From there she builds three layers, each with one job. Working memory is what the LLM sees right now: small, expensive, precious. Retrieval memory is what the agent can pull in when it needs it. Persistent memory records everything the agent has ever experienced. The trouble starts when the layers do each other's jobs.

## Let the maths remember the probabilities

The optimisations are refreshingly unglamorous. First, stop sending the transcript. The model needs state, so she sends a compact belief map, valid actions, remaining budget and cooldowns. That alone gave 97% token compression, and the agent got better, because it stopped being distracted.

Second, keep the probabilities outside the model. A belief map updates in code, and the LLM sees something like "Chamber of Secrets, 50%", which is eight to 15 tokens instead of 5,000. Her rule of thumb: whenever memory can be structured state, use structure, because language is expensive and maths is cheap.

Third, route by uncertainty. Low entropy gets a heuristic and no LLM call at all; medium gets compressed memory; high gets richer retrieval. When Harry finds a Horcrux, Voldemort's next move is obvious, so why pay a model to predict it?

Finally, persistence: store abundantly, retrieve selectively, present minimally. The architecture diagram she asks you to remember has the LLM as a small box. Belief management, constraint solving, entropy maths and compression all live outside it.

The results on the same game: 97% fewer tokens, 75% lower latency, more than 80% lower cost, and a win rate that doubled. In Anannya's words, the LLM is not the memory system; it consumes it.

## Who should watch

Anyone whose agent gets worse the longer a session runs, or whose token bill grows faster than its usefulness. The game setting keeps it light, but the five closing principles transfer straight to support bots, coding agents and multi-step workflows. If you want a framework or a vendor product, this is a design argument with numbers from one well-instrumented toy.

## Related Conf42 talks

- [AI Gardening for MLOps: Managing Context, Memory, and Entropy in Agentic Systems](https://www.conf42.com/MLOps_2026_Ishan_Shah_gardening_context_memory) by Ishan Shah, which reaches for the same entropy vocabulary from the operations side.
- [Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) by Elizabeth Fuentes Leone, the same "show the model less" idea applied to tools instead of memory.
- [Make your LLM app sane again: Forgetting incorrect data in real time](https://www.conf42.com/Large_Language_Models_LLMs_2024_Olivier_Ruas_llm_app_forgetting) by Olivier Ruas, on the stale-memory problem from the data side.

[Watch Anannya Roy Chowdhury's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anannya_Roy_Chowdhury_memory_agents_context)

[Watch the talk on YouTube](https://youtu.be/TVvo_Atx8lk).

## Watch the talk

[Make Agents Remember the Right Context at the Right Time](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anannya_Roy_Chowdhury_memory_agents_context) at Conf42 Large Language Models (LLMs) 2026.
