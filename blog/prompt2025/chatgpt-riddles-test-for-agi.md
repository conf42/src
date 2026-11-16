# Riddles show where ChatGPT predicts instead of understanding

Conf42 Blog, 2025-10-09, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/chatgpt-riddles-test-for-agi

In short: Aroma Rodrigues (Microsoft) at Conf42 Prompt Engineering 2025 probes GPT-3-era ChatGPT with riddles, translated Hindi puzzles and word problems to test AGI claims.

Ask ChatGPT "when is a door no longer a door?" and it gives you a dictionary answer. Tell it the question is a riddle and it says: when it's ajar. At Conf42 Prompt Engineering 2025, Aroma Rodrigues of Microsoft used dozens of riddles like that one to probe what a pure language model actually does, and her conclusion is blunt: ChatGPT is not AGI, and the places it fails tell you why.

The experiments were run on the GPT-3 version of ChatGPT on a free personal account, which she flags up front. That's the point rather than a weakness: before retrieval and tool layers were bolted on, you could watch the language model think without it looking things up.

## Riddle mode is a context, and it sticks

Once ChatGPT decides it's in a riddle conversation, it stays there. It answers classic riddles well (all twelve months have at least 28 days; a hole makes a bucket lighter; today comes before yesterday in a dictionary) and Aroma suspects most of those were simply in the training data. The interesting part is what happens off the beaten path. Asked what has a bottom at the top, it said a staircase. The answer is legs. Prompted for another answer, it invented a second, equally confident story. She describes the model spinning an imaginative narrative and then bending the answer to fit it.

The same sticky context breaks maths. Asked how many apples ten rabbits eat in ten minutes if five eat five in five, it stayed in riddle mode and produced reasoning she calls incredibly weird. A bus-passenger word problem fell apart as the model lost track of its own running total, which she compares to young children losing count across multiple steps.

## Translated riddles strip away the memory

Her best methodological move: to get riddles the model probably hadn't seen, she took riddles from Hindi and regional sources with no common English translation. The results got much stranger. One crude translation produced the claim that ducks give both milk and eggs. A riddle about ants (two ants ahead, two behind) got the wrong answer, and she bets the classic version with ducks would have got the right one. A question about ten birds on a wall, one shot with an arrow, got the arithmetic answer of nine, as if birds were inanimate objects that don't fly away.

The pattern she draws out: the model handles a familiar surface form, and stumbles when the same logic arrives in unfamiliar words. Your parents have six sons and each has a sister; it added six and six, twice.

## What would count as AGI, anyway

The second half takes the historical definitions one by one: the Turing test, the coffee test, the robot college student test, the employment test. Her view is that several of them are either already passed or not very meaningful, which says more about the tests than about the models. Her own definition leans on observation. Humans learn by perceiving the physical world, not only by reading about it; the model relies on available knowledge, from training or from search.

She closes with her own heavy ChatGPT use: good at context-linked creative writing in theory, but in practice it loses the thread, and a travel itinerary it wrote assumed she could cover a half-hour cab ride in about ten minutes. Retrieval helps today's versions answer her riddles correctly, but she calls that cheating in the riddle-game sense: looking up the answer isn't solving it.

## Who should watch

Anyone building on LLMs who wants an intuitive feel for failure modes before reading the papers: context lock-in, multi-step arithmetic drift, surface-form matching. It's a long, conversational talk built on examples rather than benchmarks, so treat it as a field notebook, not a study. People who want rigorous evaluation methods should pair it with the related talks.

## Related Conf42 talks

- [The Secret Language of Models: Prompt Psychology & Behavior](https://www.conf42.com/Prompt_Engineering_2025_Shashank_Shivam_models_psychology_behavior) by Shashank Shivam at Conf42 Prompt Engineering 2025.
- [Measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) by Ofer Mendelevitch at Conf42 Large Language Models 2024, for the retrieval side of the story.
- [How you can trick your company into hiring ChatGPT](https://www.conf42.com/Prompt_Engineering_2024_Daniel_Pries_chatgpt_hiring_trick) by Daniel Pries at Conf42 Prompt Engineering 2024.

[Watch Aroma Rodrigues's talk](https://www.conf42.com/Prompt_Engineering_2025_Aroma_Rodrigues_chatgpt_talk_conversation) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/r3c9Gcu4lkw).

## Watch the talk

[I talk to ChatGPT about things](https://www.conf42.com/Prompt_Engineering_2025_Aroma_Rodrigues_chatgpt_talk_conversation) at Conf42 Prompt Engineering 2025.
