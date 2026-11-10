# Five LLMs taught a small model to spot 70 kinds of news bias

Conf42 Blog, 2026-10-16, updated 2026-11-09. https://www.conf42.com/prompt2026/llms-as-teachers-for-news-bias-model

In short: Aleem Khan at Conf42 Prompt Engineering 2026 on replacing five LLM API calls per story with an owned model trained on expert-checked labels.

Aleem Khan's team started out thinking five frontier LLMs would be the product. They ended up as the teachers. At Conf42 Prompt Engineering 2026, Aleem, an independent AI entrepreneur, told the story of a news pipeline that flags around 70 types of linguistic bias, and how it moved from asking OpenAI, Anthropic, Qwen, Grok and DeepSeek the same question about every story to a single in-house model that answers in one pass.

It's a talk about prompts as one component of a system: data collection, deduplication, domain experts, smaller specialist models and a retraining loop that never ends.

## Bias you can't fact-check

The problem framing is sharp. Calling the same crowd protesters or rioters, choosing whose quote leads, leaving out context: none of it is fake news, and every fact can still be correct. You have to read the language itself. Trained linguists can do that for a few dozen articles a day; the news cycle produces thousands of stories an hour.

The pipeline pulls trending topics from X and then the full articles from Google News, because bias lives in headlines, lead paragraphs and quote order, not in tweets. Many outlets covering one event is the point: the contrast between "clashes" and "attack" is the signal.

## Deduplication decides what the model learns

Stage two sounds boring and, Aleem says, shaped everything after it. Wire stories reposted word for word get grouped into one event, but the different outlets' versions are kept, since that comparison is the whole game. Follow-ups and analysis on day two and three are linked into one thread over time. Skip this and your dataset is dominated by the month's three biggest stories; the model learns what was in the news rather than how it was written.

## When the prompt becomes an interface

The wrapper sent every story to five models with the same prompts and forced the same structured answer: which bias, where in the text, and why. Aleem's lesson for a prompt engineering crowd is that once more than one model is involved, the prompt is a contract that five very different systems have to honour, and the output format matters as much as the instructions.

The surprise was what the disagreements meant. When all five flag the same sentence, the bias is probably real. When two flag it and three don't, the text is either genuinely ambiguous or one model has a blind spot. Instead of averaging that away, the team treated it as a map of where human judgment was needed.

## Linguists wrote the prompts

The humans were PhD linguists specialising in bias and hate speech, not crowd workers. They built the taxonomy (what separates loaded language from framing, or one-sided sourcing from omission), wrote the prompts with engineers turning them into something models follow reliably, chose which stories entered the dataset, and broke ties where the LLMs disagreed. A layer of small specialist models trained on public datasets acted as a second opinion, so every label passed through three filters before training.

After 11 months that produced roughly half a million stories, labelled for 70 biases and balanced across bias types, topics and outlets so rare biases had enough examples.

## What the owned model does better

The trained model reads each sentence in the context of the whole article, checks all 70 biases in one pass on the team's own infrastructure, and returns spans, not a yes/no. Aleem's example is "The minister finally admitted the plan had failed." The model marks the loaded verb phrase, grades the severity, gives a short reason a human can accept or reject, and proposes a rewrite that says the minister reported the plan had not worked. It changes only the biased words, so the writer's voice survives, and the editor stays in charge.

Against the five-LLM pipeline it was more consistent (same input, same answer, which matters when you measure an outlet month over month), faster (one pass instead of waiting for the slowest of five calls) and cheaper. He's careful about scope: a specialist wins at one narrow job done millions of times, not at everything. A monthly loop of sampling, expert review, retraining and benchmarking keeps it from missing next year's euphemisms. His closing line for any team: ship the loop, not the model.

## Who should watch

Teams paying per-call LLM bills for a narrow classification task, anyone designing a labelling pipeline with LLMs and humans together, and people working on trust and safety or media tooling. The talk shares no exact cost or latency figures, so come for the architecture rather than benchmarks.

## Related Conf42 talks

- [Fine-tuning LLMs: A Cost-Benefit Analysis for Businesses](https://www.conf42.com/Large_Language_Models_LLMs_2025_Muddassar_Sharif_fine_tuning_business) by Muddassar Sharif (Virtuans.ai) at Conf42 Large Language Models 2025.
- [The Fairness Paradox: Why Your Compliant ML Model May Be Causing the Most Harm](https://www.conf42.com/MLOps_2026_Neelima_Verma_fairness_compliant_harm) by Neelima Verma at Conf42 MLOps 2026.
- [AI's Hidden History: Unpacking Bias, Power, and the Builders Who Shaped It](https://www.conf42.com/Machine_Learning_2025_Lianne_Potter_bias_builders_history) by Lianne Potter (Compromising Positions) at Conf42 Machine Learning 2025.

[Watch Aleem Khan's talk](https://www.conf42.com/Prompt_Engineering_2026_Aleem_Khan_bias_news_llm) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/HCMY0dxbkA0).

## Watch the talk

[Detecting 70 Kinds of Bias with a Model You Own: Replacing LLM API Calls in a Real-Time News Pipeline](https://www.conf42.com/Prompt_Engineering_2026_Aleem_Khan_bias_news_llm) at Conf42 Prompt Engineering 2026.
