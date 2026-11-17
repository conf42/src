# Why logistic regression beat a CNN and an LSTM on noisy product names

Conf42 Blog, 2026-11-15, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/logistic-regression-beats-neural-nets-product-names

In short: Vladimir Beskorovainyi (Besk Tech) at Conf42 MLOps 2026 on character n-gram logistic regression beating a CNN, an LSTM and DistilBERT on receipt text.

A character n-gram logistic regression beat a 1D CNN and an LSTM on product names from supermarket receipts in every category and every split: 30 cells out of 30. At Conf42 MLOps 2026, Vladimir Beskorovainyi, CTO and CPO at Besk Tech, reports that result, then spends most of his time on the parts that complicate it: the winner is also the slowest of the cheap models, the rules in front of it cap everything, and a benchmark score can fall apart on real data.

## The task: one receipt line, one six-digit category

Each line from a receipt has to be assigned a six-digit COICOP consumption category so prices can be compared. The text is short and dirty: abbreviations, typos, the seller's internal codes, words stuck together, and no product codes or retailer categories to lean on.

Vladimir is careful about where his numbers come from. Everything measured in the talk is from a public synthetic benchmark with six categories and five splits, with open code. The architecture has run in production since 2021 at national scale, taking in tens of millions of product lines a day, but that system is under NDA. The deploying organization reports 90 percent accuracy on the live stream; he says that is their figure for the whole pipeline and declines to explain it with his benchmark.

He also compares models in pairs, cell by cell, because an average can hide a model that wins two categories and loses four.

## The headline survives the overlap check

The character n-gram model with logistic regression reaches a mean F1 of 0.997. Then comes the check many papers skip: 34 percent of the test items also appear word for word in training. That is realistic for receipts and it inflates any score, so he measured the unseen items separately and got 0.996. The character model does not depend on the overlap. The word-level models do.

Across everything trained from scratch, four points separate the best from the worst. He also owns up to two corrections. An earlier version gave the deep models less training time; with a fair budget they are no longer the worst, just no better. And his old timing code made the cheap models look slow. The corrected gap in training cost is 212 times for the CNN and 258 times for the LSTM.

## Put cost in the same table as accuracy

Character n-grams are the most accurate and, among the cheap models, the slowest: 41,500 items a second. A plain bag of words does 191,300, which is 4.6 times faster and three points of F1 behind. At tens of millions of lines a day that difference decides whether the job finishes at all.

So his answer is three reasonable choices, picked by whether you are paid for accuracy or for speed, and the deep models are not on the list. He also trained DistilBERT: 0.993, good, but the character model still wins 18 cells to 3, and the transformer handles 82 items a second, about 460 times slower.

## The rules decide what the model ever sees

In the production design, rules pick the category and a small per-category model only confirms or rejects. People and the model vote under one rule, and a category is configuration that a methodologist can add without an engineer.

The catch is that the rule stage lets through 75 to 86 percent of the right items, and nothing downstream can do better than that. The rules stay anyway, because a rule is a phrase a person can read, change and defend to an auditor.

On labels, each annotator carries a reliability weight capped at two. In the data, strong and weak annotators both end up at two, so the weight saturates and stops telling them apart. Weighted voting still buys the classifier one to two points. "Labels are the cheapest points you can buy," Vladimir Beskorovainyi said at Conf42 MLOps 2026.

## Ninety-seven on a test set, forty-one in the field

The most useful slide is the one about limits. The benchmark is synthetic and real receipts are worse. He cites a published study that reported 97.4 percent on held-out test data and, with the same approach on real unlabeled data, coded about 41 percent of expenditure correctly. His summary: "Ninety-seven on a test set, forty-one in the field."

His four takeaways follow from that: on short noisy product names the character n-gram model was the strongest thing he measured, cost belongs next to accuracy, fix labels before tuning the model, and architecture matters more than model size. The preprint is arXiv:2606.02004 and under review at PeerJ Computer Science, with code on GitHub and data on Zenodo. Next on his list: run it on real receipts and raise the recall of the rule stage without losing explainability.

## Who should watch

Anyone classifying short, messy text at volume, and anyone about to propose a transformer for a job a linear model might already do. It is a compact, paper-style talk: slides and numbers, no demo, and a speaker who publishes his own corrections. If you want proof on real receipts, he says plainly that this study does not provide it.

## Related Conf42 talks

- [Agentic Text-to-SQL in Production: What 500+ Data Marts and 30M Users Taught Us About LLM Orchestration](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) by Vladimir Beskorovainyi (Besk Tech) at Conf42 AI Agents 2026.
- [Fast Confidence Estimation for Classification and Regression models](https://www.conf42.com/Machine_Learning_2025_Andrei_Stroganov_Andrei_Visochan_estimation_regression_confidence) by Andrei Stroganov and Andrei Visochan at Conf42 Machine Learning 2025.

[Watch Vladimir Beskorovainyi's talk](https://www.conf42.com/MLOps_2026_Vladimir_Beskorovainyi_noisy_trie_labeling) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Coding Noisy Product Names for Consumer Price Statistics: Trie Rules, Bag-of-Words and Reliability-Weighted Labeling](https://www.conf42.com/MLOps_2026_Vladimir_Beskorovainyi_noisy_trie_labeling) at Conf42 MLOps 2026.
