# A good prompt has four parts, and most people skip three

Conf42 Blog, 2025-10-22, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/prompt-basics-context-task-constraints

In short: Chetan Prakash Ratnawat of Capgemini at Conf42 Prompt Engineering 2025 with a beginner's tour of prompt structure, core techniques and AI ethics.

Most bad AI output starts with a prompt that only states the task. At Conf42 Prompt Engineering 2025, Chetan Prakash Ratnawat, Senior Manager at Capgemini, gave a ground-floor tour of prompt engineering built around one formula: give the model context, a task, constraints and any extra information, and the quality of the answer follows.

A note on scope before you press play. The talk's title points to insurance workflows, but the recording is a general introduction to prompting; claims triage and underwriting do not come up. Treat it as a first talk on the subject, delivered by someone who has rolled AI tools out to enterprise clients, and you will get what it offers.

## Prompting went from keywords to roles in four years

Chetan opens with a short history. Around 2020, prompts were bags of keywords and you hoped for the best. Then came few-shot prompting, where you hand the model a template or examples to imitate. Role prompts (*act as an analyst*) and chain of thought followed, and now multimodal prompts mix text, images and audio. It is a tidy way to see that each technique was a fix for the previous one being too vague.

He also reminds the audience that the model behind the prompt matters as much as the prompt. His version of garbage in, garbage out runs both ways: a poor model or a poor prompt will waste your time and can hand you biased answers.

## The four-part prompt, with a washing liquid

The most reusable slide is the structure. Chetan's worked example is a marketing brief:

- **Context:** you are the marketing manager for a new product launch in the FMCG sector.
- **Task:** write a short paragraph describing the target audience and the key marketing messages.
- **Constraints:** keep it short and focused on the most important messages.
- **Additional information:** the product is a liquid for washing machines, aimed at urban and semi-urban households.

Compare that with *write an email for me*, which he uses as the bad example alongside *tell me about cybersecurity*. The weak versions are not wrong, just unbounded, so the model fills the gaps with generic filler. His fix for the cybersecurity one is to ask for three common threats and how Microsoft Defender mitigates them. Same topic, a fraction of the guesswork.

He adds a list of "power words" that steer output: act as, summarize, generate, predict, elaborate, simplify. Then the core techniques: role prompting, chain of thought, few-shot and zero-shot. None of this is new to a daily LLM user, but it is laid out in an order that a team new to the tools can follow.

## The failure stories are the better half

Chetan balances the success stories with incidents worth remembering: an airline chatbot that gave a customer misleading information and ended in a legal case, staff pasting confidential code into a public chatbot until the employer blocked it, and a hiring tool that showed bias. He also mentions a financial reporting chatbot from his own client work, where he reports productivity and reporting-accuracy gains and points to his article for the details.

The lesson he draws is procedural. Validate every AI-generated output, label AI-assisted work as such with clients, write retention and data-handling rules down, and train colleagues on them. Governance is the boring part of the talk and probably the part your security team will thank you for.

## Who should watch

Managers, analysts and engineers who are about to roll an AI assistant out to a team and need a shared vocabulary for what a good prompt looks like. If you already write structured system prompts and run evals, you can skip to the failure cases and the governance section. If you came for insurance-specific workflows, they are not in this recording.

## Related Conf42 talks

- [Charlie Reynolds on the art and science of AI communication](https://www.conf42.com/Prompt_Engineering_2024_Charlie_Reynolds_promptengineering_science_art) covers the same basics from another angle, at Conf42 Prompt Engineering 2024.
- [Pravesh Nikhare on rule-based AI for dental insurance claims](https://www.conf42.com/Cloud_Native_2025_Pravesh_Nikhare_insurance_rules_processing) is the insurance workflow story this title hints at, from Conf42 Cloud Native 2025.
- [Eugene Neelou's gentle introduction to LLM security](https://www.conf42.com/Large_Language_Models_LLMs_2024_Eugene_Neelou_gentle_introduction_llm_security) picks up where the data-leak stories end.

[Watch Chetan Prakash Ratnawat's talk](https://www.conf42.com/Prompt_Engineering_2025_Chetan_Prakash_Ratnawat_insurance_transformation_workflows), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/NjEUyVlMX8w).

## Watch the talk

[Prompt Engineering at Scale: Driving AI-Powered Transformation in Insurance Workflows](https://www.conf42.com/Prompt_Engineering_2025_Chetan_Prakash_Ratnawat_insurance_transformation_workflows) at Conf42 Prompt Engineering 2025.
