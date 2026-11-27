# Your ranking model is learning from items nobody saw

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/fixing-exposure-bias-ranking-systems

In short: Devavrat Khanolkar (Cisco Systems) at Conf42 MLOps 2026 on fixing exposure bias by logging what the screen rendered, not what the server sent.

A server log that says an item was sent to a device is a poor witness to whether anyone saw it. At Conf42 MLOps 2026, Devavrat Khanolkar, machine learning engineering technical leader at Cisco Systems, explains how that gap turns into exposure bias: items below the fold get logged as impressions, nobody clicks them because nobody saw them, and the ranking model learns they are bad. His fix, drawn from a past project of his own, is to measure exposure on the client and then run the old and new data pipelines side by side until an A/B experiment settles it.

## The failure that never throws an error

Most ranking models are trained by joining two logs: impressions (what was shown) and actions (what the user did). Anything with an action becomes a positive, everything else a negative. That implicit labeling works only if the impression log tells the truth.

With server-side tracking it often is not. Content below the fold is logged as an impression. A failed network call can still count as served. Scroll position and viewport may be ignored entirely. So the item a user chose to skip and the item that never reached their screen end up with the same label.

"Recommendation systems degrade when your training data lies," Devavrat Khanolkar said at Conf42 MLOps 2026. The degradation is quiet. Popular items collect more exposure and more positives, while everything lower down collects false negatives and sinks further. In his words: "The rich got richer, and in this case, an even more important effect is that the poor got poorer". Offline metrics can look perfectly stable through all of this, because they mostly measure how well the model surfaces known positives. Meanwhile users keep seeing the same content every time they open the page.

## Three signals that your labels are wrong

Before fixing anything, he wants proof the problem exists. He names three proxies:

- An impression-interaction gap: items with very high impression counts and almost no engagement. Unless the item is truly terrible, which he says rarely happens, something is off in the logging.
- A diversity metric that declines over time, with recommendations converging near the top of the page.
- Negative labels concentrated on a small number of items in the training set.

None of these needs new infrastructure, which makes them a cheap first step.

## An impression means rendered, dwelled on and unobstructed

The fix is client-side exposure measurement. The event to log changes from the server sent this item to the item appeared on this screen. Devavrat adds two conditions that are easy to forget: the item stayed in the viewport long enough for the user to register it, and nothing such as a pop-up covered it.

Then comes the part that makes this an MLOps talk. He keeps the legacy pipeline running next to the corrected one, because without the old dataset there is no control model to compare against. Retire it too soon and the experiment is gone. The cost is a stretch of maintaining two pipelines.

His validation checklist for the new signal: schema and coverage across every surface (TVs, laptops and phones, in his video example) and across rank positions, join latency between client and server events, label distribution shift (the invalid negatives should drop meaningfully), and stability over time before any model is trained on it.

## Cleaner labels shrink the dataset

Here is the detail teams tend to trip on. If the server logged 100 impressions and only some of them were truly seen, the corrected dataset is smaller. A model trained with the old sampling setup may not converge. He raises sampling rates and revalidates the model before trusting it.

Evaluation then pulls in two directions. Offline, diversity goes up and precision at K or recall at K goes down, because the label distribution itself changed. Online, he expects a short-term engagement drop as the model stops leaning on historically overexposed items, followed by recovery if the experiment runs long enough to see it.

That is why his last piece of advice is about people. Tell stakeholders about the dip before the experiment starts, so nobody dials it down in week one. He also lists who has to be in the room: client and UI engineers for viewport tracking, data engineering to own the new dataset, ML engineers for training and experiment design, and product and analytics for success metrics and the rollout decision.

## Who should watch

ML engineers and data engineers who own a recommender or search ranking pipeline, and anyone who has stared at a healthy offline metric while the product felt stale. The talk is a method, with no production numbers from the project behind it, so come for the sequence of steps and the traps. If you already log viewport impressions with dwell time, you can skim to the training and experiment sections.

## Related Conf42 talks

- [ML-Powered Search & Recommendation 101: From Core Concepts to Scalable Systems](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) by Sergey Polyashov (Microsoft), a good primer first.
- [Real-Time Personalization at Scale: Neural Ranking Systems and Operational Breakthroughs](https://www.conf42.com/Chaos_Engineering_2025_Vedant_Agarwal_personalization_ranking_systems) by Vedant Agarwal (Walmart Global Tech).
- [Making recommendations explainable](https://www.conf42.com/Machine_Learning_2026_Lev_Fedorov_optimization_performance_efficiency) by Lev Fedorov (Amazon).

[Watch Devavrat Khanolkar's talk](https://www.conf42.com/MLOps_2026_Devavrat_Khanolkar_containers_vulnerability_inference) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Fixing Exposure Bias in Production Ranking Systems Through Reliable MLOps Pipelines](https://www.conf42.com/MLOps_2026_Devavrat_Khanolkar_containers_vulnerability_inference) at Conf42 MLOps 2026.
