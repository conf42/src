# LLM moderation works as a system, not as one big model

Conf42 Blog, 2026-06-09, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-moderation-is-a-system-not-a-model

In short: Andrei Shcherbinin of Social Discovery Group at Conf42 LLMs 2026 on rules, small classifiers, LLM judges and human reviewers in dating-app moderation.

Once scammers can generate a hundred polite variations of the same pitch, keyword filters stop being enough. At Conf42 Large Language Models 2026, Andrei Shcherbinin, who leads machine learning work at Social Discovery Group, walked through the production auto-moderation system his team built for user-to-user messaging on dating platforms. His thesis: LLM-powered moderation works when it is designed as a system of rules, lightweight models, LLMs and humans, each handling the risk it is best at.

## Dating raises the stakes

In dating products, safety is the product. Users share private and emotionally vulnerable content, romance fraud and payment manipulation are constant, and the hardest violations (grooming-like behaviour, coded language, attempts to move the chat off-platform) look harmless in any single message. Ten messages in a row can show a pattern that one message never does.

He also notes how LLMs changed the abuse itself. Old spam repeated itself. LLM-assisted abuse is fluent, varied and paraphrased, and on agentic platforms the risk extends to actions, not just text.

## Accuracy is the wrong scoreboard

With violations around one percent of traffic, a model that labels everything normal scores 99 percent accuracy and catches nothing. Shcherbinin's goal is controlled risk instead: category-specific thresholds, severity-aware evaluation, precision at low recall, recall on high-severity classes and false positive rates per category. Missing mild toxicity and missing a scam are different failures with different costs.

Policy is part of the model specification. Severity maps to a risk score, confidence to a threshold, context to features or prompt information, and reviewer decisions become corrected labels. If a label like suspicious off-platform behaviour is vague in the policy, the model will be vague too.

## Deduplicate or you train a template detector

The data section is the most practical part. Without deduplication, thousands of near-identical "help me with my phone bill" messages teach the model the template instead of the intent. It looks brilliant offline and fails the moment wording changes. "You have built a very expensive template historian," as he puts it.

His pipeline uses exact, normalized and near-duplicate deduplication, and treats it as evaluation hygiene that also cuts train-test leakage. For rare classes, progress is measured in positives found, not rows processed: sample a batch, skip anything already scored via a hash journal, pull few-shot examples from a human golden set, and let an LLM label each message as clear normal, clear violation or borderline.

The LLM is a pre-annotator, never the authority. It suggests a label, a reason and the supporting fragment; a human accepts or rejects; only validated labels enter the golden set. He likens the LLM to a very confident intern: fast, often right, and not the one who writes company policy.

## Each layer gets the risk it is good at

The production stack has four layers. Rules and keywords handle links, obfuscation and deterministic checks. Lightweight BERT-style classifiers handle high-volume categories cheaply. LLM judges take the grey zones where context and reasoning matter. Humans stay the policy authority for edge cases, appeals and high-severity categories. He expects more work to move to specialised LLM layers as they get cheaper, so the hybrid stack doubles as a migration path.

A score is not a decision. The same 0.82 can mean low-priority review for spam and immediate escalation for grooming-like behaviour, depending on severity, user risk and how full the reviewer queue is. "Prediction is machine learning. Decisioning is product engineering." Thresholds get recalibrated whenever policy, abuse mix, model or reviewer capacity changes.

## Honest about the headline numbers

The system handles millions of messages a day, with reviewer load down 60 percent and over 90 percent of violations caught. Shcherbinin spends a slide warning that such numbers mean nothing without the methodology behind them: which policy classes, what time window, how borderline cases count and what counts as caught. Rollout follows the same caution: offline validation, shadow mode, then monitoring of category mix, queue backlog and drift, because users adapt against the system and "scam evolves faster than static benchmarks".

## Who should watch

Trust and safety engineers, ML engineers working on rare-class problems and anyone tempted to point a frontier model at a moderation queue and call it done. It is a production talk with real trade-offs, light on code.

## Related Conf42 talks

- [Fighting Harmful Content with AI: Scalable Moderation for Real-World Safety](https://www.conf42.com/Machine_Learning_2025_Georgina_Tryfou_moderation_scalable_safety) from Conf42 Machine Learning 2025 is a second take on moderation at scale.
- [Prompting for Trust: Designing Transparent LLM Systems That Align With Human Judgment](https://www.conf42.com/Prompt_Engineering_2025_Raj_Kommera_trust_llm_judgment) from Conf42 Prompt Engineering 2025 pairs well with the LLM-as-intern idea.
- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) from Conf42 AI Agents 2026 covers the agentic side of the same risk.

[Watch Andrei Shcherbinin's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrei_Shcherbinin_moderation_safety_platforms)

[Watch the talk on YouTube](https://youtu.be/hPLtey3nseY).

## Watch the talk

[Building an ML Automoderation System for LLM-Augmented Online Platforms](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrei_Shcherbinin_moderation_safety_platforms) at Conf42 Large Language Models (LLMs) 2026.
