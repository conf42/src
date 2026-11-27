# Explainable recommendations by storing positives, not embeddings

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/store-positives-not-embeddings-to-explain-recs

In short: Lev Fedorov of Amazon at Conf42 Machine Learning 2026 on rebuilding a recommender so every card in the feed traces back to something the user liked.

A user profile that is a single embedding is efficient and impossible to explain: the vector lands somewhere between Java and Python and somehow recommends C#. At Conf42 Machine Learning 2026, Lev Fedorov, Software Engineer at Amazon, walked through how his team rebuilt a recommender so that each item in the feed can say "because you liked this", which helped both confused users and developers debugging complaints.

It is one of the more hands-on talks of the event: a full recsys pipeline, then the specific changes that made it traceable.

## The pipeline before

Lev described the classic funnel. Out of about 100 million items, candidate selection picks a couple of thousand; features are computed for each; a ranking formula scores them; business logic diversifies the top by author and topic and returns about 20 items.

Two places made explanations hard. The user profile was an embedding from collaborative filtering, or a set of k-means centroids for content models, and centroids can land in clusters the user never cared about. Candidate selection used KNN over an HNSW index, which returns neighbours that are not always close and knows nothing about quality or popularity.

The trigger for the work was practical: user reports about irrelevant content, and no tooling to say which past interaction led to a given card.

## Replace the vector with a list of IDs

The fix starts with the profile. Instead of an embedding, store the IDs of publications the user interacted with positively. No approximation, nothing to interpret.

Candidate selection then becomes a map: each positive is a key, and its value is a list of related candidates. Two models keep those lists sensible:

- A **relevance formula**, trained on crowdsourced annotations of similar and dissimilar pairs, using cosines from several content models as features, filters out unrelated items.
- An **attractiveness formula** orders what is left. Version zero is conditional CTR (the CTR of item A given a positive interaction with item B); the trained version adds metadata about both items and keeps conditional CTR as a feature.

Now explanation is a lookup. The shown item came from a positive, the positive has a title and an author, and the feed can say so.

## Keep the positives list honest

Positive lists only grow, so Lev uses a determinantal point process to keep a subset that is both high-weight (watch ratio, likes, shares, comments) and diverse. Each positive's downstream performance is tracked too: positives that lead nowhere get dropped, and a ranking formula for positives sorts the rest.

The last trick is quota allocation. Asked for 300 candidates from three positives, the system splits by each positive's CTR rather than evenly: in his example, 150 from the strongest positive and 60 from the weakest. He framed it as a bandit-style idea, and it is the part most teams could borrow tomorrow.

The results he claimed were transparent explanations for users, improved feed relevance, and backend traces developers can follow when someone files a complaint.

## Who should watch

Recommender engineers who are asked "why did it show me that?" and have no good answer. If your stack is pure two-tower retrieval, the talk is a useful counterweight.

## Related Conf42 talks

- [ML-Powered Search & Recommendation 101: From Core Concepts to Scalable Systems](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) by Sergey Polyashov, a good primer before this one.
- [Precision Metrics Framework: Context-Aware Evaluation for Search and Recommendation Systems](https://www.conf42.com/Python_2025_Aditya_Singh_precision_metrics_framework) by Aditya Singh, for measuring whether the changes help.
- [Real-Time Personalization at Scale: Neural Ranking Systems and Operational Breakthroughs](https://www.conf42.com/Chaos_Engineering_2025_Vedant_Agarwal_personalization_ranking_systems) by Vedant Agarwal.

[Watch Lev Fedorov's talk](https://www.conf42.com/Machine_Learning_2026_Lev_Fedorov_optimization_performance_efficiency) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/dqamvMp-sl8).

## Watch the talk

[Making recommendations explainable](https://www.conf42.com/Machine_Learning_2026_Lev_Fedorov_optimization_performance_efficiency) at Conf42 Machine Learning 2026.
