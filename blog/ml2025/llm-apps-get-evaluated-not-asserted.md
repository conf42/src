# You can't assertEqual an LLM, so evaluate it instead

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/llm-apps-get-evaluated-not-asserted

In short: At Conf42 Machine Learning 2025, Gaurav Bansal explained why LLM apps need scored evaluation, golden datasets and humans in the loop, not plain asserts.

Ask a model about the weather twice and you get 62 degrees the first time and 74 the second, both phrased differently. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Gaurav Bansal, a test infrastructure engineer who said in the talk he has spent about a decade at Amazon, used that tiny example to make one point: with LLM applications, "we don't test it. We evaluate it."

It's a short, practical talk aimed at people who own quality for services that now have a model somewhere in the request path.

## The unit test you grew up with stops working

Bansal starts from the most boring test in the world: a `sum` method, two and two in, four out, `assertEqual`, done. Then he swaps the method for an LLM. Same input, different output, and both answers might be fine. The assert fails while the product works, which is the worst kind of red build.

His fix is a doctor's-office analogy. A doctor asks how you feel on a scale from one to ten; nobody expects an exact string back. Evaluation works the same way: you score responses for accuracy, semantic similarity to an expected answer, context relevance, safety, logical coherence and instruction-following, then decide what score is good enough.

## Golden datasets go stale, so keep a human near them

The implementation roadmap he lays out is refreshingly unglamorous:

- Define the evaluation criteria first: which metrics, which thresholds.
- Build the infrastructure: a service with access to the model and your knowledge bases, plus a UI that shows how the golden dataset ran and whether it met the criteria.
- Keep humans in the loop, because the golden dataset itself can go stale and somebody has to notice.
- Automate the whole thing and put it in the CI/CD pipeline, because evaluation you run by hand is evaluation you stop running.

The before-and-after comparison is the bit that matters when you swap models. Run the evaluation on the current model, run it on the new one, compare, and alert if quality drops. Model upgrades become a diff you can read instead of a vibe.

## Break it on purpose before someone else does

Bansal spends a good chunk of time on adversarial work. Edge-case generation should throw strange and hostile inputs at the system so the guardrails get exercised. Red-team exercises try to mislead or break the model and check that confidential project data doesn't leak out of it. Stress testing checks that the service survives a high volume of complex queries, not just the happy path.

He also folds compliance into the testing job: document the evaluation methodology and its limitations, keep old and new evaluation results side by side, audit the data regularly, and follow the regulations of each country you operate in. Not thrilling, but it's the part auditors will ask about.

## Who should watch

Watch it if you're a QA or platform engineer who just inherited an LLM feature and your test suite is flaky in new and exciting ways. It's a framework talk rather than a tooling demo: no specific evaluation library is shown, so pair it with something hands-on. If you already run evals in CI with a curated golden set, you'll mostly be nodding along.

One honest note on the data: the event listing shows Uttar Pradesh Technical University as his affiliation, while in the talk he describes his roughly ten years at Amazon.

## Related Conf42 talks

- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz goes one level up and asks whether your evaluation is any good.
- [Automated Evaluation for your RAG Chatbot or Other Generative Tool](https://www.conf42.com/Large_Language_Models_LLMs_2024_Abigail_Haddad_automated_evaluation_chatbot) by Abigail Haddad is the hands-on companion with real automation.
- [AI vs. AI: How to Test AI Systems Using AI](https://www.conf42.com/Large_Language_Models_LLMs_2025_Robin_Gupta_test_systems_process) by Robin Gupta covers using models as testers.

[Watch Gaurav Bansal's talk](https://www.conf42.com/Machine_Learning_2025_Gaurav_Bansal_evaluation_enterprise_language)

[Watch the talk on YouTube](https://youtu.be/uAxurOFtLL0).

## Watch the talk

[Improving Large Language Model Performance: Scalable Evaluation & Advanced QA for Enterprise AI](https://www.conf42.com/Machine_Learning_2025_Gaurav_Bansal_evaluation_enterprise_language) at Conf42 Machine Learning 2025.
