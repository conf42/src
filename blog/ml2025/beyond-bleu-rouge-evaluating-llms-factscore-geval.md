# Why BLEU gives a perfect answer 0.016, and what to measure instead

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/beyond-bleu-rouge-evaluating-llms-factscore-geval

In short: Alok Ranjan (Dropbox) and Saurabh Suman at Conf42 Machine Learning 2025 on replacing n-gram metrics with FactScore, LLM-as-judge, G-Eval and RAG evaluation.

A shopper asks a support bot what size a jacket is, the bot answers "34", and BLEU scores that correct reply at 0.016. At Conf42 Machine Learning 2025, Alok Ranjan, Engineering Manager at Dropbox, and Saurabh Suman of San José State University used examples like that to argue that n-gram metrics measure the wrong thing for LLMs, and walked through the evaluation toolkit that should replace them: atomic fact checking, human preference rankings, LLM judges, G-Eval and separate retriever and generator metrics for RAG.

It is a long, thorough talk, and one of the best overviews of LLM evaluation from the event.

## What BLEU and ROUGE actually measure

The first section is a fair-minded refresher. BLEU is precision-oriented n-gram overlap, a staple of machine translation; ROUGE is recall-oriented, built for summarisation. Both are fast, language-agnostic and need no human labels, which is why they spread.

Then the failure cases. Besides the jacket, their HR policy example pairs a reference ("employees are permitted to work remotely up to three days per week") with a paraphrase about staff telecommuting with supervisor approval. Same meaning, BLEU score of zero. The list of sins: surface-level, easy to game by repeating reference phrases, blind to factuality and coherence, and prone to penalising longer, more fluent answers. A metric that prefers the wrong answer with the right words is a regression test for vocabulary, not quality.

## What to measure instead

They define the dimensions a modern evaluation should cover: factual accuracy, semantic coherence, answer relevance, context precision and context recall, plus bias mitigation and reliability across prompts and personas.

For factuality, the method is FactScore: break a response into atomic facts (the Eiffel Tower is in Paris; it was built in 1889), check each against a trusted source, and score the supported fraction. The model-based version layers sentence-embedding alignment, natural language inference to label each fact as entailed or contradicted, and weighted aggregation.

Human evaluation stays in the loop, but structured: rubric-based scoring plus pairwise A-versus-B comparisons aggregated with a Bradley-Terry model into a global ranking, then compared against automated metrics to see where they disagree.

## Letting an LLM grade the LLM

Saurabh's half is about automation. An LLM judge brings context awareness, scale and consistency; humans audit the judge and feed corrections back. He demos the OpenAI Evals framework running GPT-3.5 Turbo on 25 Spider SQL samples from a single CLI command: 20 correct, 80% accuracy. One "failure" is instructive: the model used a LIKE pattern where the reference used exact equality, which is often right but not what was asked.

G-Eval gets the most attention. Define criteria, let the model write its own evaluation steps with chain of thought, then score. Assertions work like unit tests for LLMs, such as a rubric that fails any reply mentioning it is an AI assistant, which changes from fail to pass with a different persona prompt. On correlation with human judgment across coherence, consistency, fluency and relevance, the ROUGE variants trail, embedding metrics like BERTScore and MoverScore do better, and LLM-based evaluators such as G-Eval correlate best.

## RAG needs two report cards

For retrieval-augmented generation, evaluate the retriever and the generator separately: contextual precision, recall and relevancy for retrieval, and answer relevance and faithfulness for generation. A great generator still hallucinates when retrieval fails. They compare basic RAG, multi-query and RAG fusion across models and conclude no single metric is enough. The talk closes with a synthetic dataset pipeline (chunk documents, generate contexts and "goldens", evolve harder queries) and a practical checklist: clear objectives, mixed methods, representative datasets, continuous evaluation, strong baselines.

## Who should watch

Anyone shipping an LLM feature who still reports BLEU to their manager, and teams building their first eval harness. It is long, but it is the whole map in one sitting.

## Related Conf42 talks

- [Hilik Paz (Arato.ai) on how to evaluate your evals](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals), the next question once you have a judge.
- [Abigail Haddad (Capital Technology Group) on automated evaluation for RAG chatbots](https://www.conf42.com/Large_Language_Models_LLMs_2024_Abigail_Haddad_automated_evaluation_chatbot), a hands-on companion to the RAG section.
- [Liran Yushinsky (JFrog) on LLM-as-judge for non-deterministic code generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen), the judge pattern applied to agents.

[Watch Alok Ranjan and Saurabh Suman's talk](https://www.conf42.com/Machine_Learning_2025_Alok_Ranjan_Saurabh_Suman_modern_approaches_bleu)

[Watch the talk on YouTube](https://youtu.be/Q4iyw1miXaY).

## Watch the talk

[Beyond BLEU and ROUGE — Modern Approaches to Evaluating LLMs and AI Systems](https://www.conf42.com/Machine_Learning_2025_Alok_Ranjan_Saurabh_Suman_modern_approaches_bleu) at Conf42 Machine Learning 2025.
