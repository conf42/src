# NLP from bag-of-words to GPT, told through the benchmark numbers

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/nlp-history-in-benchmark-numbers

In short: UnitedLex director Shahzeb Akhtar traced NLP from n-grams to multimodal models at Conf42 Machine Learning 2025, one perplexity and BLEU score at a time.

GPT-1 was trained on about 5 GB of unpublished books; GPT-4's training set has been reported at around 13 trillion tokens. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Shahzeb Akhtar, Director of IP Strategy and Technology at UnitedLex, retold the history of natural language processing using the metrics each era was judged by, which turns a familiar story into a useful one.

Akhtar leads an IP data science team whose platform, Vantage for IP, processes hundreds of thousands of patents with NLP, so he has a practitioner's reason to care what each generation of models could actually do.

## Counting words had a ceiling, and perplexity showed it

The early part covers bag-of-words and TF-IDF: text as an unordered pile of words, good enough for classification and retrieval, blind to grammar. N-gram models added a little context, but perplexity, the measure of how surprised a model is by the next word, stayed above 120. Then the curse of dimensionality: with a 10,000-word vocabulary each document becomes a 10,000-dimensional vector that is mostly zeros, distances stop meaning much, and memory runs out. It's a tidy explanation of why the field had to move on.

## Each architecture fixed the last one's bug

Word2vec and GloVe gave dense embeddings where king sits near queen. RNNs added memory but lost it over long sequences thanks to vanishing gradients; LSTMs fixed that with gated memory cells and pushed Penn Treebank perplexity into the forties, at the cost of slow, sequential training. The 2017 transformer paper replaced recurrence with attention, enabling parallel training and a BLEU score of 41.8 on English-to-French translation. Akhtar shows the paper's attention-head visualisations, including heads resolving which noun a pronoun refers to, which is a nice touch for anyone who has only seen the architecture diagram.

BERT gets its own section: bidirectional context (so *bank* means different things by a river and in a city), masked language modelling with about 15% of tokens hidden, and the pre-train then fine-tune pattern that cut the need for big labelled datasets. Then the GPT line: 125 million parameters, then 1.5 billion, then 175 billion, with SuperGLUE moving from 45.2 to 71.8.

## Smaller, cheaper and greener is the next scoreboard

The last third looks forward. Multimodal models in medical imaging, visual question answering and video reasoning; then the efficiency toolkit: pruning, knowledge distillation into student models, quantisation down to 8 or 4 bits for edge devices, and sparse attention to tame the quadratic cost of long contexts. His prediction for future benchmarks is that energy use, causal reasoning and ethical alignment will matter alongside accuracy, citing a University of Massachusetts Amherst estimate of around 300 tons of CO2 to train a single large model.

## Who should watch

Engineers who arrived in NLP via ChatGPT and want the backstory in one sitting, and anyone who has to explain to a manager why perplexity and BLEU aren't the whole story. It's a history-and-concepts talk; there's no code. If you lived through the LSTM years, the transformer and efficiency sections are the part to keep.

## Related Conf42 talks

- [Superposition in LLM Feature Representations](https://www.conf42.com/Large_Language_Models_LLMs_2024_Boluwatife_BenAdeola_superposition_feature_representations) by Boluwatife Ben-Adeola looks inside the models this talk ends with.
- [Beyond Hype: The Practical Evolution of Data Science with Generative AI](https://www.conf42.com/Large_Language_Models_LLMs_2025_Omer_Ali_Omer_Syeda_Narmeen_science_evolution_practical) by Omer Ali and Syeda Narmeen carries the history into day-to-day data science.
- [The Evolution of Natural Language Processing: Leveraging Generative AI and Transformers in Healthcare](https://www.conf42.com/Python_2024_Deepak_Karunanidhi_neural_language_processingi_healthcare) by Deepak Karunanidhi tells a similar story with a healthcare ending.

[Watch Shahzeb Akhtar's talk](https://www.conf42.com/Machine_Learning_2025_Shahzeb_Akhtar_nlp_generative_revolution)

[Watch the talk on YouTube](https://youtu.be/PkuOlKBoN_c).

## Watch the talk

[Data-Driven NLP: Quantifying the Revolution from Statistics to Generative AI](https://www.conf42.com/Machine_Learning_2025_Shahzeb_Akhtar_nlp_generative_revolution) at Conf42 Machine Learning 2025.
