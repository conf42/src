# Cross-channel attribution starts with identity resolution

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/attribution-starts-with-identity-resolution

In short: Ashutosh Verma of Meta at Conf42 Machine Learning 2026 on an ML framework that joins online and in-store journeys to measure marketing ROI.

Last-click attribution gives all the credit to whoever touched the customer last, which is roughly like crediting the goalkeeper's final pass for the whole match. At Conf42 Machine Learning 2026, Ashutosh Verma, a software engineer at Meta in Seattle, laid out a machine-learning framework for attributing conversions across both digital and physical channels, and his central claim is that none of it works until you can tell that the phone, the laptop and the shopper at the till are the same person.

This is a compact framework talk: no demo, but a clear checklist.

## Why the old models miss the middle

Ashutosh named three failures. Channel silos give each team its own analytics view, so nobody sees how touchpoints influence each other. Linear assumptions in first-click and last-click models ignore the mid-funnel interactions where decisions actually form. And the offline blind spot leaves point-of-sale data and in-person visits disconnected from everything that happened online.

## Four components, identity first

His unified framework has four parts: integrate touchpoint data from every channel into one repository; resolve identities across devices and contexts; model channel contribution and interaction effects; and activate the results in budget and campaign decisions.

Identity resolution gets the most attention. It combines deterministic matching (logged-in states), probabilistic matching on device fingerprints and behaviour, graph-based entity resolution that weighs evidence across touchpoints, and privacy-preserving hashing. The balance he describes is precision against coverage: match too eagerly and you merge strangers, too cautiously and the journey falls apart.

## Synergies are the point

Once journeys are joined, feature engineering adds recency and frequency signals plus cross-channel interaction features, and ensembles of gradient boosting, neural networks and survival analysis estimate each channel's incremental contribution, including diminishing returns.

The payoff Ashutosh highlighted is the interaction effect. On his slides, social engagement does little for conversions directly but lifts the effectiveness of later email campaigns by 34%, and store visits preceded by website browsing convert at 2.8 times the rate of walk-ins. Analyse each channel alone and both effects vanish, so budgets drift towards the wrong places.

## Close the loop, then keep it legal

Attribution only matters when it changes spend. The framework feeds automated budget reallocation, validated with A/B tests, and pushes scores into campaign tools for timing and creative. For durability, he recommends a privacy-first design (on-device processing, federated learning, differential privacy), continuous retraining as behaviour shifts, and LLMs for feature discovery and causal inference.

His roadmap is pleasingly modest: start with two channels, invest in identity before modelling, get cross-functional buy-in early, and ship an MVP you can measure.

## Who should watch

Marketing data scientists and analytics engineers asked to prove ROI across online and offline channels. If you work on identity graphs already, the modelling half is the part to focus on.

## Related Conf42 talks

- [Cloud-Native Data Architectures for Real-Time Marketing Analytics in Database DevOps](https://www.conf42.com/Database_DevOps_2026_Kamini_Murugaboopathy_agents_pipelines_o11y) by Kamini Murugaboopathy, on the data-unification problem underneath attribution.
- [ML & GenAI for Vibe Marketing: Designing the Future of Audience Connection](https://www.conf42.com/Machine_Learning_2025_Udipta_Basumatari_vibe_marketing_genai) by Udipta Basumatari.

[Watch Ashutosh Verma's talk](https://www.conf42.com/Machine_Learning_2026_Ashutosh_Verma_scalability_architecture_distributed) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/hmm03ACR8EE).

## Watch the talk

[Unifying Online and Offline Worlds: A Machine-Learning Framework for Cross-Channel Attribution and Marketing ROI](https://www.conf42.com/Machine_Learning_2026_Ashutosh_Verma_scalability_architecture_distributed) at Conf42 Machine Learning 2026.
