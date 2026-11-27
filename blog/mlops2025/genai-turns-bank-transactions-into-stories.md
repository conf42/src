# Generative AI turns bank transactions into stories customers read

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/genai-turns-bank-transactions-into-stories

In short: Pushpalika Chatterjee (Huntington National Bank) at Conf42 MLOps 2025 on generative AI for financial narratives, personalisation and synthetic fraud data.

Nobody reads their bank statement, but plenty of people would read one sentence telling them their coffee habit just ate into this month's savings. At Conf42 MLOps 2025, Pushpalika Chatterjee, Senior Software Engineering Manager for Enterprise Payments at The Huntington National Bank, argued that generative AI moves banking from recording transactions to telling customers what they mean, and she showed where that helps personalisation, fraud defence and stress testing.

## From ledger rows to narratives

For decades, banks treated each transaction as an isolated event in a structured ledger. Pushpalika's point is that generative AI can combine structured data (spending history) with unstructured data (even voice) into contextual insight. Her running example: instead of just recording a $50 spend at Starbucks, the system can explain how that spend raised this month's expenditure and dented savings. She calls the shift financial storytelling.

She is candid about the audience for this: younger customers who never open a statement, and people outside finance for whom 30 days of transactions are "just random numbers." A plain-language explanation reaches them where a dashboard does not.

## A short history of AI in banking

The talk traces the arc quickly. Rule-based fraud alerts and credit scoring in the 1990s and 2000s, rigid and full of false positives. Machine learning for personalisation and risk scoring in the 2010s. Deep learning for real-time fraud detection and NLP chatbots later that decade. Then generative AI, which does not only predict a problem but proposes what to do next: what-if simulations, tailored loan and investment offers, personalised reports.

The mortgage example lands well. If you pay a thousand dollars more each month, or a hundred thousand up front, how much shorter is the loan and what happens to the payment? That kind of tailored answer is what she means by personalisation, as opposed to picking from five predefined products.

## Synthetic fraud as a vaccine

The most engineering-relevant idea is defensive. Attackers already use AI, so Pushpalika proposes using generative models to create synthetic fraud patterns and adversarial transactions to train more robust detectors, and to stress-test liquidity and credit crises before they happen. Her metaphor is a digital vaccine: expose the system to the one-in-a-million edge cases deliberately, rather than learning about them in production.

## The bill comes due: bias, privacy, explainability, security

She does not skip the hard part. Bias, so that better protection does not flow only to the financially privileged. Privacy under laws like GDPR and CCPA, where banking data is among the most sensitive there is. Explainability, because regulators will not accept black-box answers. Security, where prompt injection is the new SQL injection.

Her mitigations: federated learning so banks can collaborate without sharing raw data, differential privacy so outputs cannot expose individuals, and explainable AI so regulators and customers can see why a decision was made.

## A pilot and a look ahead

The case study is a personalised wealth management assistant her team piloted. It ingested spending, saving and investment data, generated what-if projections and tax-optimisation suggestions in plain language. She reports customer engagement up 40% and noticeably better financial literacy scores.

Looking forward, she sketches multi-agent systems (separate agents for risk, liquidity and compliance that negotiate trade-offs), a personal finance copilot that schedules payments and moves funds the way GPS handles navigation, and large-scale simulations that let regulators stress-test something like a digital currency before launch.

## Who should watch

Product engineers and ML teams in banking thinking about customer-facing generative AI, and anyone building fraud models who wants an argument for synthetic adversarial data. It is a broad, strategy-level talk with one pilot, not an implementation walkthrough.

## Related Conf42 talks

- [AI-Powered Customer Insights for Financial Services](https://www.conf42.com/Machine_Learning_2025_Neha_Thakur_insights_financial_customer)
- [Optimizing Financial Operations with Large Language Models: A CFO's Perspective](https://www.conf42.com/Large_Language_Models_LLMs_2025_Andriy_Bagryantsev_financial_operations_cfo)
- [AI-Powered Payment Systems: Balancing Security and Experience Through Intelligent Fraud Prevention](https://www.conf42.com/Large_Language_Models_LLMs_2025_Arpit_Mittal_payment_security_fraud)

[Watch Pushpalika Chatterjee's talk](https://www.conf42.com/MLOps_2025_Pushpalika_Chatterjee_generative_ai_fintech)

[Watch the talk on YouTube](https://youtu.be/6bheymmeh48).

## Watch the talk

[Generative AI in Fintech: From Transactional Data to Personalized Financial Experiences](https://www.conf42.com/MLOps_2025_Pushpalika_Chatterjee_generative_ai_fintech) at Conf42 MLOps 2025.
