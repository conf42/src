# AI personalisation fails silently, so give it circuit breakers

Conf42 Blog, 2026-03-09, updated 2026-11-09. https://www.conf42.com/blog/sre2026/personalisation-models-fail-quietly-build-circuit-breakers

In short: Yury Lysak of Lionsoul Global at Conf42 SRE 2026 on proactive SRE for AI personalisation: drift signals, small-data methods and black swan circuit breakers.

A recommendation engine can be 100% available, return zero errors and still lose you a client. At Conf42 Site Reliability Engineering 2026, Yury Lysak, Head of Strategic Projects at Lionsoul Global, a digital asset wealth manager, made the case that AI personalisation needs its own SRE playbook, because its failures never page anyone.

He brings a useful career arc to it: personalisation and commercial analytics for telcos at VEON and for retailers via McKinsey, now applied to wealth tech, where the client list is short and every client matters.

## Loud failures get fixed, quiet ones get quarterly reviews

His framing is the sharpest part of the talk. Traditional failures are loud: a 500, a timeout, a crash, and everyone mobilises. Personalisation failures are gradual. Features decay, embeddings go stale, recommendations get a little worse each week, and the dashboard stays green. He describes client lifetime value slipping a percent or two per month, unnoticed until a complaint or a quarterly review shows months of lost revenue.

Then there are the events no model was trained for. He cites the October 2025 crypto liquidation cascade and the February 2026 Bitcoin crash as moments when the engineering was fine and the models' assumptions about liquidity and correlation were catastrophically wrong. No latency alert catches a model that is confidently describing a market that no longer exists.

## When you have 50 clients, A/B testing is a fantasy

What transfers from telco and retail is a lot: next best action becomes fund allocation, churn prediction becomes attrition scoring, basket analysis becomes spotting which clients might fit a new strategy. What does not transfer is the sample size. With a few dozen clients you cannot A/B test or train a standard model.

His substitutes are concrete: Bayesian methods that start from priors learned elsewhere and update per client, Thompson sampling for exploration on tiny samples, transfer learning where similar data exists, and the relationship manager as a human sensor whose qualitative notes feed the loop. The architecture he shows layers this: data sources (including RM notes), an ML pipeline producing ranked recommendations with confidence intervals, an LLM layer that writes the client-facing narrative, and a guardrail layer with a rules engine and an RM review gate. The LLM drafts; it never has the last word.

## Three levels of admitting the model does not know

The circuit breaker design is the part to copy. Level one is an always-on market regime detector: volatility above twice the 90-day average, or correlations moving sharply, widens uncertainty bounds and escalates to humans. Level two watches confidence per recommendation and suppresses automation when inputs drift too far from training data. Level three, when both trip, switches off ML recommendations and falls back to conservative, pre-approved defaults. His guiding principle: silence beats a confident wrong answer.

Monitoring is tiered too: daily data quality and confidence, weekly PSI drift per feature plus the RM override rate (above 30% means the model is misaligned), monthly business metrics against a non-personalised baseline. And every alert should speak business, naming revenue at risk rather than just a threshold crossed.

## Compliance as a pipeline step

In regulated finance each recommendation is a potential regulatory event, so his pipeline logs inputs, model version and confidence at generation time, validates against concentration limits and client restrictions, has an LLM write a feature-referencing explanation, routes it through an RM, then archives it. Answering a regulator, he says, went from weeks of digging to a download.

## Who should watch

Anyone running ML in production where the feedback loop is slow and the dataset small: wealth, B2B, healthcare, anything with dozens of customers instead of millions. The business impact figures in the talk are his own, so treat them as one firm's experience; the circuit breaker and alert-design patterns stand on their own.

## Related Conf42 talks

- [Real-Time Personalization at Scale: Neural Ranking Systems and Operational Breakthroughs](https://www.conf42.com/Chaos_Engineering_2025_Vedant_Agarwal_personalization_ranking_systems) by Vedant Agarwal, the millions-of-users end of the same problem.
- [The AI Trust Triad for DevOps](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) by Saideepak Kandibanda, on shipping explainable AI in regulated systems.
- [Innovating FinTech: Leveraging AI for Transformative Financial Solutions](https://www.conf42.com/Internet_of_Things_IoT_2024_Andrei_Alekseev_ai_fintech_financial) by Andrei Alekseev.

[Watch Yury Lysak's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Yury_Lysak_beyond_observability_proactive) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/vuWZ9RMlQrg).

## Watch the talk

[Beyond Observability: Proactive SRE for AI-Driven Personalisation](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Yury_Lysak_beyond_observability_proactive) at Conf42 Site Reliability Engineering (SRE) 2026.
