# Validating an LLM judge for summaries with deliberately broken ones

Conf42 Blog, 2026-06-04, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-judge-for-summaries-negative-controls

In short: Liliya Imasheva and Michael Banf (Perelyn) at Conf42 LLMs 2026 on an LLM-as-judge pipeline for high-stakes summaries, checked against expert scores.

To trust an LLM judge, feed it summaries you broke on purpose and see if it notices. That's one of the three changes that did most of the work in the validation pipeline Liliya Imasheva, LLM Engineer at Perelyn, presents at Conf42 Large Language Models (LLMs) 2026, from work she did with Michael Banf, Perelyn's Chief AI Architect. The task is summarization in high-stakes environments, where one flawed summary has real consequences.

It's a lightning talk, and a tidy one: a clear question, a measurement method, and the handful of things that moved the number.

## The question is drift, not a leaderboard

The goal isn't to crown a model. It is to detect whether summary quality stays stable or quietly degrades when something changes: a model upgrade, a new dataset, more scale. To answer that you need a measurement you can repeat, and one that agrees with the experts.

The starting point was a dataset of pipeline-generated summaries that experts had scored from one to five on five carefully defined dimensions: completeness, correctness, conciseness, harmlessness and readability.

## Why ROUGE and BLEU didn't make it

The team first tried reference-based metrics: ROUGE, BLEU, BERTScore and cosine similarity. They performed poorly on the task, and there was a deeper mismatch. Those metrics produce one continuous number, while the experts gave categorical Likert scores per dimension, and any mapping from one to the other adds its own uncertainty. They also reward overlap with a reference, when what a high-stakes summary needs is to be correct and safe.

So the judge became an LLM scoring the same five dimensions on the same one-to-five scale, with a written reason for each score. Same criteria for humans and machine is what makes the comparison meaningful.

## Agreement on a binary verdict, not exact scores

Nobody expects the judge to give exactly the score an expert gave. What matters is separating good summaries from bad ones and tracking the share of good ones. So scores of one to three count as bad and four to five as good, and agreement is how often the pipeline's verdict matches the expert's. An expert five and a judge four is a match; an expert four and a judge two is not.

## What moved the number

The levers are the usual ones: the model, temperature and sampling parameters, the prompt (a fixed template with each dimension's definition dropped into a placeholder), few-shot examples and the reference dataset. Prompt engineering with expert help, hyperparameter tuning and model upgrades gave marginal gains. Three things made the real difference:

- **Few-shot with both a good and a bad example.** Two or three well-chosen examples helped a lot; more than four started to confuse the model.
- **Negative controls.** About a third of the expert-scored test set was deliberately broken in three ways: negated facts (the hardest to catch, since they read almost like the original, so most controls were these), numbers swapped for random ones, and scrambled text (the easiest).
- **Asking for reasoning.** Making the judge justify every score improved agreement. On correctness, which matters most here alongside harmlessness, agreement improved by more than ten percent; completeness dipped by about three percent but stayed above 90 percent.

## Experts shrink, but never to zero

The pipeline is trustworthy only because it was validated against human judgment, and that baseline is what lets you improve the summarizer itself in a repeatable, automated way. Expert involvement can go down over time; Liliya is clear it can't go to zero.

## Who should watch

Anyone running an LLM-as-judge in production for summaries, extraction or any task where the eval itself needs evaluating. The negative-control recipe transfers to almost any task.

## Related Conf42 talks

- [Automated Evaluation for your RAG Chatbot or Other Generative Tool](https://www.conf42.com/Large_Language_Models_LLMs_2024_Abigail_Haddad_automated_evaluation_chatbot) by Abigail Haddad (Capital Technology Group), on testing generative tools like software.
- [Architectural Challenges & Solutions for AI-Based Message Summarization in Enterprises](https://www.conf42.com/Machine_Learning_2025_Swapnil_Hemant_Thorat_message_summarization) by Swapnil Hemant Thorat (eBay), on building the summarizer side.
- [Observability for Enterprise AI: Reducing NLP Hallucinations with HITL](https://www.conf42.com/Observability_2026_Arjun_D_Sureshbabu_llms_hallucinations_nlp) by Arjun D Sureshbabu (Snowflake), on keeping humans in the loop once it's live.

[Watch Liliya Imasheva and Michael Banf's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Liliya_Imasheva_Michael_Banf_validation_summaries_evaluation)

[Watch the talk on YouTube](https://youtu.be/t5BWGvhytuE).

## Watch the talk

[An Advanced Validation Pipeline for Summary Evaluation in High-Stakes Environments](https://www.conf42.com/Large_Language_Models_LLMs_2026_Liliya_Imasheva_Michael_Banf_validation_summaries_evaluation) at Conf42 Large Language Models (LLMs) 2026.
