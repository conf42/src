# Fraud detection and personalization can share one Go pipeline

Conf42 Blog, 2026-05-16, updated 2026-11-09. https://www.conf42.com/blog/golang2026/fraud-and-personalization-share-one-go-pipeline

In short: Sridhar Muthineni of Capgemini at Conf42 Golang 2026 on one detect, personalize and govern framework for fintech apps, with Go running real-time inference.

Banks usually split fraud prevention and personalization between different teams with different tools. At Conf42 Golang 2026, Sridhar Muthineni, Product Tech Lead at Capgemini, argued they belong in one framework (detect, personalize, govern) because they run on the same data, the same plumbing and often the same models, with Go handling the real-time path.

It is an accessible overview, pitched so that a product manager can follow it, and it covers a lot of ground quickly: model families, a streaming inference pipeline, personalization techniques, and the regulation that shapes all of it.

## Four threats, one impatient customer

Sridhar opens with the threats: account takeovers, synthetic identities built from a real Social Security number plus invented details, and money laundering through many small transactions. The fourth pressure is the customer, who wants a banking app that is both safe and as personal as the streaming service they use every evening. The talk is an attempt to do both at once.

## Pick the model for the trade-off, not the hype

There is no single best fraud model, he says; the choice depends on accuracy, response time, explainability and cost. He walks through four families:

- **Gradient-boosted decision trees** as fast pattern matchers on structured, tabular data, good for quick yes-or-no calls.
- **RNNs** for sequences, such as a spending pattern over the last ten transactions that looks off.
- **Graph neural networks** for relationships, such as several unrelated accounts all funnelling money into one hidden account.
- **Transformers** for long-range behaviour across months.

## Why Go sits in the hot path

The Go argument is about the milliseconds a bank has when you tap a card: compiled speed, goroutines handling thousands of concurrent transactions, and short, predictable garbage collection pauses. The pipeline is three steps: ingest through Kafka, pre-process (clean, format, add context such as location and how many transactions the user has made that day), then infer a fraud score. He judges the model on three metrics together: detection accuracy, false-positive rate (the card declined at the checkout for no reason) and latency, since a slow decision means a timed-out payment.

## Personal without being creepy

On the personalization side, recommendation systems suggest financial actions instead of films, such as a high-yield savings product for a consistent saver. Reinforcement learning adapts, for example by dropping alert types a user always ignores, or tuning the timing and size of credit offers. LLM agents answer questions like whether you can afford a holiday, or explain in plain English why a transaction was flagged. Adaptive credit scoring rounds it out by tracking behaviour over time instead of a dated snapshot, so the app can warn before overspending rather than punish after.

## Governance is an architecture choice

The governance pillar is the part Sridhar calls most important. Explainability, fairness and privacy are requirements: GDPR Article 22 gives people a right to an explanation of automated decisions, so he points to SHAP and LIME for human-readable reasons, and lending models get bias tests across demographic groups before deployment. Privacy techniques include federated learning, differential privacy and small models compiled with Go running on-device so transaction details need not leave the phone.

The frontier problems he lists are honest: fraudsters use AI too, real-time graph analytics on live fraud rings is computationally huge and the Go tooling is still young, and responsible AI at scale needs stronger governance. His last takeaway is the one to pin on the wall: "once AI is live, watch it like a hawk," because models quietly degrade as the world changes.

## Who should watch

Engineers and product leads new to ML in payments who want the map before the details. Experienced fraud teams will find it introductory; there are no benchmark numbers or code, and the Go material is about why rather than how.

## Related Conf42 talks

- [Rahul Ganti on fraud detection in financial systems](https://www.conf42.com/Platform_Engineering_2025_Rahul_Ganti_fraud_detection_financial) at Conf42 Platform Engineering 2025
- [Vinod Upputuri on fraud ML with NumPy](https://www.conf42.com/Python_2025_Vinod_Upputuri_fraud_ml_numpy) at Conf42 Python 2025
- [Srinivas Reddy Mosali on scaling fintech infrastructure](https://www.conf42.com/Golang_2025_Srinivas_Reddy_Mosali_fintech_infrastructure_scaling) at Conf42 Golang 2025

[Watch Sridhar Muthineni's talk](https://www.conf42.com/Golang_2026_Sridhar_Muthineni_driven_fraud_detection)

[Watch the talk on YouTube](https://youtu.be/waDLRZSDqQA).

## Watch the talk

[AI-Driven Fraud Detection & Personalization in Scalable Go Fintech Systems](https://www.conf42.com/Golang_2026_Sridhar_Muthineni_driven_fraud_detection) at Conf42 Golang 2026.
