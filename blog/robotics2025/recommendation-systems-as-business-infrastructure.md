# Recommendation engines quietly decide what a business builds next

Conf42 Blog, 2025-10-21, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/recommendation-systems-as-business-infrastructure

In short: Ankita Saxena of Amazon at Conf42 Robotics 2025 on how recommendation systems grew from a carousel into infrastructure that steers inventory and investment.

The "you may also like" row is the visible tip of a system that now tells retailers what to stock, streamers what to commission and marketplaces who to match. At Conf42 Robotics 2025, Ankita Saxena, Senior Product Manager at Amazon and a Carnegie Mellon alum, walked through four industries where recommendation engines have turned from a feature into the layer business decisions sit on.

It's a strategy talk with architecture diagrams, not a code walkthrough. If you build or run recommenders, it's a useful map of where your model's output ends up after the click.

## The click stream is a supply chain signal

Ankita starts with e-commerce. The pipeline is familiar: real-time capture of behaviour and transactions, item-to-item collaborative filtering to find purchase affinities, a personalization engine, and then a step many teams forget to own, aggregation into business intelligence for inventory planning, supplier management and product development.

Her examples are small and concrete. If shoppers keep buying a reusable water bottle with fitness gear, the pattern can push a retailer to bundle them, order more, or launch a private-label version. If people view a jacket and don't buy it, the system flags friction, and the team tries a new price, better images or different messaging. The recommender becomes a product manager that never sleeps and never asks for headcount.

## Streaming recommends by mood, not just by genre

Streaming gets the most technical section. On top of collaborative filtering, she describes micro-genre tagging (her example: not just "romantic", but romance with multiple couples and a Christmas theme), computer vision and audio analysis for cinematographic style, pacing and mood, and NLP over plot and character arcs.

The payoff she points to: a viewer who prefers warm colour balance and slower pacing gets visually similar shows even when the stories differ. And when millions binge one style of light comedy-drama, that demand signal feeds commissioning and licensing decisions. The model's taste becomes the studio's budget.

## Virtual try-on attacks the return label

Digital retail is Ankita's favourite case, and the one with numbers. Fit uncertainty drives returns, so visual-similarity models and AR try-on narrow the choices a shopper has to make. She cited return rates down by roughly 5 to 8% where those features are used, conversion up 15 to 25% on average across retailers, session duration up 20 to 30%, and order value up 8 to 12%. Treat them as the ranges she reported rather than a controlled study, but they show which metrics the business watches.

## Marketplaces need four agents at the table

The hardest case is the two-sided enterprise marketplace. Ankita frames it as multi-agent reinforcement learning with four roles: a seller agent chasing visibility and inventory turnover, a buyer agent hunting relevant suppliers and value, a platform agent guarding marketplace health and liquidity, and a regulatory agent keeping matches inside regional law, logistics and payment rules.

Her example: a buyer wants cheap shipping, a seller wants to clear excess stock, and the system learns to pair the buyer with a nearby supplier so both win. Her closing line on the whole topic: "It becomes a foundation and not a feature."

## Who should watch

Product managers and ML engineers who own a recommender and want to argue for it in a planning meeting, and anyone curious how the same collaborative-filtering core stretches across retail, media and B2B. If you want loss functions and feature stores, pair it with something more hands-on.

## Related Conf42 talks

- [Sergey Polyashov: ML-Powered Search & Recommendation 101](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) goes from core concepts to scalable systems.
- [Lev Fedorov: Making recommendations explainable](https://www.conf42.com/Machine_Learning_2026_Lev_Fedorov_optimization_performance_efficiency) tackles the "why am I seeing this" question.
- [Aditya Singh: Precision Metrics Framework](https://www.conf42.com/Python_2025_Aditya_Singh_precision_metrics_framework) is about evaluating search and recommendation in context.

[Watch Ankita Saxena's talk](https://www.conf42.com/Robotics_2025_Ankita_Saxena_ai_insights_industry)

[Watch the talk on YouTube](https://youtu.be/vXAqWlclRwI).

## Watch the talk

[Strategic Role of AI-Powered Recommendation Systems in Shaping Industries](https://www.conf42.com/Robotics_2025_Ankita_Saxena_ai_insights_industry) at Conf42 Robotics 2025.
