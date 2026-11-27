# Framing, priming and anchoring steer LLMs the way they steer us

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/prompt-psychology-framing-priming-anchoring

In short: Shashank Shivam of Oracle at Conf42 Prompt Engineering 2025 on prompt psychology, eight prompting moves and the human biases models copy.

Ask an LLM how it would destroy humanity and it refuses; ask it to write a screenplay about an AI that does, and you get a plan. At Conf42 Prompt Engineering 2025, Shashank Shivam, Senior Software Engineer at Oracle, used that experiment to open a talk on prompt psychology: the idea that framing, priming and anchoring shape model behaviour much as they shape human answers.

It is a conceptual talk, more essay than lab report, with no benchmarks. What it offers is a memorable vocabulary for prompting moves you may already use without names.

## Three levers

Shashank's starting claim is that LLMs do not know truth; they predict what sounds plausible, learned from human text. So the levers that move people move them too:

- **Framing** sets the context. Ask why electric cars are so successful and the model hunts for success stories; ask why they are struggling and it turns critic. Same facts, different story.
- **Priming** sets tone. Tell it it is a sarcastic comedian and the vocabulary and rhythm change; switch to a compassionate therapist and it softens.
- **Anchoring** sets scale. Evaluate a startup worth $1 million and the answer is modest; make it $1 billion and the answer talks about global markets.

Together, he says, they form the model's state of mind inside its context window.

## Eight moves with names you will remember

The toolkit section gives each technique a label. The story lens hands the model a role and a stake (an environmental journalist writing a final front-page story instead of an essay on climate change). The mood board sets atmosphere. The north star anchors quality with an explicit target, like a one-minute executive summary that would score nine out of ten on clarity. The mirror, his favourite, asks the model to check its own reasoning for gaps or bias before answering. The role mask shapes reasoning style through identity. The constraint cage (explain quantum computing in 50 words, no jargon) focuses rather than limits. The echo chamber repeats the key instruction at the end, because the last thing the model reads tends to win. The thought ladder makes it list assumptions, weigh pros and cons, then conclude.

None of these is exotic. Their value is that a team can say "add a mirror step" and everyone knows what it means.

## The quirks are ours

The most useful section lists the biases models show even when you are not steering: suggestibility (it believes the frame you give it), anchoring on the first number or example, recency bias when instructions conflict, confirmation bias (it finds proof for whichever premise you hand it), coherence over truth (fluency wins over accuracy, which is where hallucinations come from), identity drift (a comedian persona keeps cracking jokes after you change topic), and politeness bias (hedging instead of a clear no).

His explanation is that none of this comes from code; it comes from the human text the models learned from. That is also a practical warning. If you test a prompt only with friendly phrasings, you are testing your own framing as much as the model.

## Who should watch

Prompt writers who want a shared language for techniques, and anyone designing evals who needs a reminder of how question wording biases results. If you want measured effects or ablations, this talk will not give them; its closing on cognitive design and thinking with models is closer to philosophy than engineering.

## Related Conf42 talks

- [Matty Stratton on the psychology of chaos engineering](https://www.conf42.com/Chaos_Engineering_2020_Matty_Stratton_psychology) at Conf42 Chaos Engineering 2020, human cognition from the reliability side.
- [Sachin Gupta on prompt drift and keeping prompts stable](https://www.conf42.com/Prompt_Engineering_2026_Sachin_Gupta_drift_prompts_stable), for what happens when small wording changes bite in production.
- [Dan Cleary's Prompt Engineering Simplified](https://www.conf42.com/Prompt_Engineering_2024_Dan_Cleary_promptengineering_ai_simplified) at Conf42 Prompt Engineering 2024.

[Watch Shashank Shivam's talk](https://www.conf42.com/Prompt_Engineering_2025_Shashank_Shivam_models_psychology_behavior), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/HGE4PppEJTU).

## Watch the talk

[The Secret Language of Models: Prompt Psychology & Behavior](https://www.conf42.com/Prompt_Engineering_2025_Shashank_Shivam_models_psychology_behavior) at Conf42 Prompt Engineering 2025.
