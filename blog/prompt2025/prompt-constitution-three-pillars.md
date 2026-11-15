# A prompt constitution: decompose, guard early, version everything

Conf42 Blog, 2025-10-28, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/prompt-constitution-three-pillars

In short: Preetham Sunilkumar of LPL Financial at Conf42 Prompt Engineering 2025 on a prompt constitution framework with modular chains, guardrails and red teaming.

Change one word in a prompt and an LLM can hand you a different answer, or a dangerous one. At Conf42 Prompt Engineering 2025, Preetham Sunilkumar, Vice President and Software Development Manager at LPL Financial, presented what he calls a prompt constitution: a framework that treats prompts as modular, versioned software with safety built in from the first step.

## Three walls you hit in production

Preetham calls the starting problem the prompting paradox: the same model that looks like a magician pulling a rabbit from a hat can turn chaotic with a small change in wording. Traditional systems are deterministic business logic; LLMs are not. He groups the failures into three walls:

- **Safety:** prompt injection, jailbreaking and biased outputs.
- **Consistency:** two phrasings of the same question (his example: the best way to learn Python versus how a beginner should start with Python) get different, even contradictory answers.
- **Complexity:** prompts stacked on prompts, nested conditions and role play in one block, impossible to reuse or debug. His image is building a skyscraper with sticky notes.

## Pillar one: split the monolithic prompt

The structural integrity pillar breaks one do-everything prompt into a chain of specialists. His example is a customer review. The monolithic version asks the model to read the review, give the sentiment and topics, and write a reply, all at once. It works for a handful of reviews, then accuracy and bias drift as volume grows.

The fix is a router plus three specialists: one for sentiment, one for key topics and concerns, one that drafts the reply from the other two outputs, with evaluation at each stage. The bonus is reuse. Next project needs sentiment analysis? Specialist A is already built.

## Pillar two: guard the input, not just the output

The safety net pillar moves from filtering outputs to guarding before the core model ever sees the request. His banking bot example takes a message that combines a valid billing complaint with a request to hack someone else's account. A pre-processing guardian (another LLM or agent) splits it, passes the billing issue through and declines the rest with a safe response. The harmful part is neutralised before the response generator runs.

## Pillar three: prompts are code

The scalable assembly pillar is the one most teams skip. Keep a catalogue of prompts separate from the engine that runs them, version every change, test at unit and integration level, A/B test versions, and make rollback a one-line change. If a new model version behaves worse than the old one, swap back the same way you would roll back a build.

## Constitution, critique, revision, reinforcement

The framework runs in four steps: define the constitution from organisational values, regulation (FINRA in finance, health rules in healthcare), ethical principles and behaviour guidelines; self-critique each stage's output against it; revise; and feed results back as reinforcement.

The evaluation section is practical. Define the objective first (factual accuracy, reasoning, bias, robustness to adversarial input, multi-turn behaviour, refusals), then generate and label synthetic data for that objective rather than reusing 10 or 15 favourite questions. Red teaming covers threat modelling, adversarial generation, stress testing, vulnerability analysis and hardening. He also points to the EU AI Act's requirements on risk management, data governance, documentation, transparency, human oversight and accuracy, and closes on human in the loop as the feedback mechanism that holds it together.

## Who should watch

Teams moving LLM features from prototype to a regulated production system, especially in finance or healthcare. Platform engineers building prompt registries will find a useful checklist. If you already run versioned prompts with eval suites and input guards, this confirms your design more than it extends it.

## Related Conf42 talks

- [Hilik Paz on model-based input validation against prompt injection](https://www.conf42.com/Prompt_Engineering_2024_Hilik_Paz_modelbased_input_validation), a closer look at the pre-processing guardian idea.
- [Josh Armitage on red teaming AWS](https://www.conf42.com/DevSecOps_2022_Josh_Armitage_red_teaming_aws_practice_preach), the security tradition Preetham borrows from.
- [Morgan Willis on production-ready architectures for AI agents you do not trust](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) at Conf42 AI Agents 2026.

[Watch Preetham Sunilkumar's talk](https://www.conf42.com/Prompt_Engineering_2025_Preetham_Sunilkumar_frameworks_llms_scalable), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/kZBzM_qhIXo).

## Watch the talk

[Revolutionizing Prompt Engineering: Scalable Frameworks for Safer, Smarter LLMs](https://www.conf42.com/Prompt_Engineering_2025_Preetham_Sunilkumar_frameworks_llms_scalable) at Conf42 Prompt Engineering 2025.
