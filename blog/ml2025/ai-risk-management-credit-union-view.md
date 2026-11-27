# Fraud, collections and payments through one AI risk lens

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/ai-risk-management-credit-union-view

In short: Deepu Komati, Lead Engineer at PenFed Credit Union, at Conf42 Machine Learning 2025 on AI for fraud detection, loan collections, payments and compliance.

Ten small transfers across different accounts look boring one at a time. Together they can look like a fraud ring. Deepu Komati, Lead Engineer at PenFed Credit Union, built his [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) talk around that idea: AI earns its place in financial risk management by seeing patterns across transactions that rules and humans miss, and the same lens applies to fraud, loan collections, payment routing and regulatory work.

It is an overview of where AI fits in a financial institution's risk stack, with figures drawn from industry results. There is no code and no single system under the microscope, so treat it as a map with Komati's priorities marked on it.

## Rules catch yesterday's fraud

The problem framing is familiar but well put. Traditional risk management combed through records and reacted after an incident. Static rules and models trained once on history fall behind fraudsters who change tactics. Komati's alternative is a system that compares every transaction against the customer's own baseline (amount, time, location, device) and against wider historical patterns, then acts in the moment: hold the payment or route it for extra verification before it completes.

He cites three gains for that approach: better detection accuracy, fewer false positives, and much faster responses than traditional systems. The false-positive point deserves the emphasis he gives it. Every legitimate card declined is a customer annoyed and a support call queued, so a model that only gets more paranoid is not an improvement.

## Collections that call at the right moment

The most distinctive section is loan collections, an area most ML talks skip. Instead of one-size-fits-all reminders, models use borrowing history, payment behaviour, seasonal spending and wider economic factors to estimate each borrower's likelihood of repayment, then personalise the timing and content of outreach, for example a reminder shortly after a borrower's usual pay cycle, or an alternative payment plan when their situation changes. Komati reports recovery improvements for personal loans and a large jump for business loans, which are usually the hardest to recover. His framing is that collections become less of a confrontation and more of a conversation, which is good for recovery and for the relationship.

## Payments that route themselves

On payment processing, he contrasts batch systems with manual exception handling against AI-assisted processing that runs adaptive authentication checks, routes each transaction along the path that best balances speed and security, and resolves many exceptions automatically. The payoff is lower processing time and operating cost, plus fewer stalled payments.

## Explain every flag

The ethics and regulation half of the talk is where engineers should pay attention. Fairness means auditing decisions across demographics so models do not reinforce historical bias. Transparency means every flagged transaction or declined loan comes with a documented reason. Privacy means encryption and anonymisation. Accountability means governance, review committees and audit trails. Komati also describes AI that scans regulatory changes and flags compliance gaps, and decision logs that give regulators a readable path through each automated call. The rollout he recommends is the sensible one: assess, pilot with real feedback, develop skills, and keep retraining as threats evolve.

## Who should watch

Engineers and product people new to financial ML who want a tour of use cases beyond fraud, and anyone who has to explain to a compliance team why a model said no. Practitioners after architecture diagrams or model details will want to pair it with the talks below.

## Related Conf42 talks

- [AI-powered fraud detection in cloud-native digital payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security), Sandeep Katuri, Conf42 Cloud Native 2025
- [AI-powered payment systems: balancing security and experience through intelligent fraud prevention](https://www.conf42.com/Large_Language_Models_LLMs_2025_Arpit_Mittal_payment_security_fraud), Arpit Mittal, Conf42 Large Language Models 2025
- [Building resilient MLOps pipelines for illiquid loan portfolio valuation](https://www.conf42.com/MLOps_2026_Ankur_Mehra_loan_valuation_pipelines), Ankur Mehra, Conf42 MLOps 2026

[Watch Deepu Komati's talk](https://www.conf42.com/Machine_Learning_2025_Deepu_Komati_financial_management_fintech)

[Watch the talk on YouTube](https://youtu.be/UttJUSEEMrE).

## Watch the talk

[AI at the Financial Frontier: Reimagining Risk Management for Modern FinTech](https://www.conf42.com/Machine_Learning_2025_Deepu_Komati_financial_management_fintech) at Conf42 Machine Learning 2025.
