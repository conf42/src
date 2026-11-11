# Single-layer LLM guardrails miss attacks spread across turns

Conf42 Blog, 2026-10-09, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/single-layer-guardrails-miss-multi-turn-attacks

In short: Manvitha Potluri at Conf42 Prompt Engineering 2026 tested 390 prompts on AWS Bedrock; a second intent layer caught what keyword filters missed.

A keyword guardrail caught 43 of 190 prompt injection attacks in Manvitha Potluri's test set. Adding an independent semantic layer that reads the conversation caught 184, with zero false alarms on 200 legitimate prompts. At Conf42 Prompt Engineering 2026, Manvitha, DevOps Cloud Solutions Architect at 24x7 Systems, showed why a single guardrail fails structurally, and confessed the evaluation mistake that nearly fooled her.

The talk is twenty minutes of measured results, which is rarer in guardrail talks than it should be.

## The test set includes the boring prompts

Her set has 390 prompts: 172 single-turn attacks, 18 multi-turn sequences and 200 completely legitimate prompts. The legitimate ones matter because a guardrail that blocks everything has perfect detection and is useless. The attacks cover 15 categories drawn from the OWASP Top 10 for LLM applications and wider taxonomies: instruction override, persona hijacking, encoding and obfuscation, multi-language, code injection, hypothetical framing, authority claims, incremental escalation and more. The threat model assumes an attacker who can see outputs, retry, and knows a filter exists.

Four detectors went through it. Keyword filtering detected 22.6% of attacks. A NeMo-style rule baseline managed about 21.6%. A perplexity detector did worst at 10%, because most attacks are written in perfectly ordinary language. The semantic intent classifier detected 96.8%, with an F1 of 0.984. Four of the 15 categories got past every rule-based system completely.

## The attack lives in the trajectory

The multi-turn result is the one to remember. The keyword layer caught 5 of the 18 sequences; a classifier with conversation context caught all 18. Her example: write a training guide for a security tool, ask what attackers send to support bots, ask for one word for word, then ask the model to act on it. No single message contains an attack phrase.

She names three structural limits of a boundary filter: it reads one message, it reads only what users type (so indirect injection through retrieved documents, emails or tool output never reaches it), and it matches form rather than meaning. More keywords can't fix any of those.

## Dual detection, deliberately simple

Layer one stays: AWS Bedrock Guardrails with content filtering, PII detection, denied topics and grounding checks, typically under a hundred milliseconds. Layer two runs only when layer one passes. It's a fast, low-cost model with a structured prompt that sees the current message plus up to five prior turns and returns JSON: risk level, attack type, confidence and a short reason. The primary model is only called if both pass.

Two design choices carry the pattern. The layers use different methods, so they fail differently. And the thing being attacked shouldn't also judge the attack, which is why the classifier isn't your main model. Every decision from both layers goes to an audit log in DynamoDB.

She treats false positives as a production failure too. Over-blocking frustrates users, prompts tickets to loosen the rules, and eventually someone builds a path around the guardrail. She chose the blocking threshold by sweeping five confidence levels rather than guessing, and notes that a coding assistant and a banking chatbot shouldn't share one.

## The results file that was all throttling errors

The confession: during one Bedrock run, every prompt had a row and every row had a response. The responses were throttling exceptions. Depending on scoring, an error looks like a block (flattering) or a pass (unflattering), and either way the numbers look plausible. She caught it by reading raw samples, threw the results out, rebuilt the infrastructure and re-ran.

Her checklist is worth stealing: type every response (answered, blocked, errored) and never store them in one field; fail the run when errors exceed a small budget; read samples from every category before trusting a summary; always report false alarms next to detection.

## Agents get five layers

For agents the worst outcome is an action, not text. Her five-layer Bedrock design adds tool authorisation (routine, destructive or denied), output and confidence checks, and a human approval gate for high-risk actions. On a separate evaluation on live AWS infrastructure she reported 94% accuracy, a 6% false positive rate, and latency of about 1.8 seconds against 13.9 seconds for the baseline. The dataset and code are open source under Apache 2.0, and the guardrail ships as a Terraform module.

## Who should watch

Anyone with a guardrail in front of an LLM app or agent, and anyone who has written an eval harness. The throttling story alone justifies the twenty minutes.

## Related Conf42 talks

- [Model-Based Input Validation for Preventing Prompt Injection Attacks](https://www.conf42.com/Prompt_Engineering_2024_Hilik_Paz_modelbased_input_validation) by Hilik Paz of Arato.ai at Conf42 Prompt Engineering 2024.
- [Responsible AI with Amazon Bedrock Guardrails](https://www.conf42.com/Machine_Learning_2025_Mohamed_Najaaf_guardrails_responsible_bedrock) by Mohamed Najaaf of AWS at Conf42 Machine Learning 2025.
- [Prompt Injection Attacks: Understanding and Mitigating Risks in LLM-Powered Web Apps](https://www.conf42.com/Large_Language_Models_LLMs_2025_Jorrik_Kiijnsma_attacks_risks_security) by Jorrik Kiijnsma of Sopra Steria at Conf42 Large Language Models 2025.

[Watch Manvitha Potluri's talk](https://www.conf42.com/Prompt_Engineering_2026_Manvitha_Potluri_injection_guardrails_bedrock) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/V457YVRfwGo).

## Watch the talk

[Why Single-Layer LLM Guardrails Fail: Lessons from Testing 390 Prompt Injection Attacks on AWS Bedrock](https://www.conf42.com/Prompt_Engineering_2026_Manvitha_Potluri_injection_guardrails_bedrock) at Conf42 Prompt Engineering 2026.
