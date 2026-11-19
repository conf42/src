# Contact center AI fails on day one without the backstage crew

Conf42 Blog, 2025-08-26, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/mlops-for-contact-center-conversational-ai

In short: Manoj Kumar Vunnava (GoDaddy) at Conf42 MLOps 2025 on the MLOps that keeps contact center conversational AI reliable, from feature stores to drift.

A telecom chatbot that answers a network outage by telling customers to restart their router is a demo that met production. Manoj Kumar Vunnava, a senior telecom engineer at GoDaddy, opens his Conf42 MLOps 2025 talk with exactly that story and spends the rest explaining the MLOps that would have prevented it: consistent features, repeatable training, careful rollouts, monitoring at four levels and automated retraining when the world shifts.

It is an accessible talk, full of analogies, aimed at people building or running AI in customer support.

## Why contact centers are harder than they look

Manoj lists what makes this domain unusual. Volume runs to millions of conversations a day. The AI works next to human agents as a co-pilot, so it has to fit into their workflow. Errors are expensive in public: one bad answer can turn into a social media pile-on within hours. And every industry has its own vocabulary, so one generic model will not cover healthcare, insurance, retail and banking.

His metaphor for MLOps is a theatre's backstage crew. The actors get the applause, but someone has to make sure the lights work and the show starts on time.

## Features are context, not just text

For conversational AI, features include what was said earlier in the conversation, timing signals such as how quickly a customer replies and how often they contact support, and language signals like sentiment, intent and domain keywords. He manages these through a feature store, which he compares to a well-organised pantry: you do not want to discover halfway through cooking that the salt is gone. Teams that skip it, he says, end up with models that work in the lab and fall apart in production.

Training has to be robust and automated: data quality checks, synthetic data for rare but important cases like fraud, bias detection across languages and industries, experiment tracking, and validation against business KPIs like customer satisfaction and resolution time rather than accuracy alone.

## Shadow first, then canary, then everyone

Rollout follows a familiar ladder: shadow testing where the model predicts silently, canary releases on a sliver of traffic, staged rollouts as confidence builds, and a rollback switch always ready. His analogy is teaching someone to drive, from the passenger seat to the parking lot to the freeway.

CI/CD treats models like software. Code, configuration and features live in Git, tests run on every change, models are registered with metadata, and deployments are containerised and rolled out gradually. In his experience this cut deployment time from weeks to hours.

## Drift arrives on schedule and by surprise

Monitoring runs at four levels: technical metrics (latency, error rates), data quality, model performance (accuracy, agent overrides) and business outcomes. Drift gets special attention. Holiday seasons flood support with package questions, outages bring a sudden wave of identical calls, and language itself changes. A year earlier nobody asked support about ChatGPT; now it is a routine question. When drift shows up, retraining should be automatic: collect new interactions, verify them with agents, retrain, validate against old and new scenarios, and roll out carefully.

## Who should watch

Engineers and product owners building support bots, agent-assist tools or voice AI, and MLOps teams new to conversational systems. It is not a deep technical dive, but the four-level monitoring model and drift examples are practical. His golden rule: AI should free agents for empathy and complex cases, not replace them.

## Related Conf42 talks

- [Sujit Kumar (Copart) on incident-ready contact centers with AI and automation](https://www.conf42.com/Incident_Management_2025_Sujit_Kumar_contactcenters_automation_scale) at Conf42 Incident Management 2025.
- [Dmitry Kindrya (ToYou Delivery) on whether LLMs will remake or bury customer support](https://www.conf42.com/Large_Language_Models_LLMs_2024_Dmitry_Kindrya_customer_support_revolutionizing) at Conf42 LLMs 2024.
- [Shradha Kohli (Salesforce) on explainable AI and chatbot trust](https://www.conf42.com/DevSecOps_2024_Shradha_Kohli_conversational_ai_trust) at Conf42 DevSecOps 2024.

[Watch Manoj Kumar Vunnava's talk](https://www.conf42.com/MLOps_2025_Manoj_Kumar_Vunnava_scaling_conversational_ai) for the full architecture walkthrough.

[Watch the talk on YouTube](https://youtu.be/OcRzCsrCTgs).

## Watch the talk

[Scaling Conversational AI in Production: MLOps Strategies for Contact Center Transformation and Operational Excellence](https://www.conf42.com/MLOps_2025_Manoj_Kumar_Vunnava_scaling_conversational_ai) at Conf42 MLOps 2025.
