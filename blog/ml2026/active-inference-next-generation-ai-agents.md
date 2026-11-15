# Active inference as a first-principles path to next-generation agents

Conf42 Blog, 2026-01-23, updated 2026-11-09. https://www.conf42.com/blog/ml2026/active-inference-next-generation-ai-agents

In short: QF Network CEO Alex Vyatkin at Conf42 Machine Learning 2026 on active inference and the free energy principle as a basis for adaptive AI agents.

Today's agents are LLMs in a loop, and they still struggle the moment a scenario is genuinely new. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Alex Vyatkin, co-founder and CEO of deep tech startup QF Network, pointed past the hype to a different foundation: active inference, a framework from neuroscience built on Karl Friston's free energy principle, in which agents act to reduce surprise about their world.

He calls it "quite a deep rabbit hole" and means it as an invitation. This is a research-frontier talk: no benchmarks, no product demo, but a clear explanation of the ideas and a reading list to get started.

## The reality check behind the agent boom

Vyatkin opens by taking stock of the year of the agent: lots of new projects, some of them wild, and even talk of Mac Mini shortages from people running agents at home. The market is growing fast. But in his assessment, current agents still fail in novel scenarios, remain hungry for data and compute, and get harder to run as tasks grow more complex, with many projects at risk from unexpected costs. The gap between promised autonomy and delivered autonomy is where he wants engineers to look.

## Agents that minimise surprise

The core idea: an adaptive system survives by minimising variational free energy, a bound on surprise, meaning the mismatch between its internal model of the world and what it senses. It can close that gap two ways. Perception updates the internal model. Action changes the world so it matches the model. In active inference, perception and action are two sides of one loop.

Agents choose policies by minimising expected free energy, which bundles two values. Epistemic value rewards exploring to reduce uncertainty. Pragmatic value rewards reaching preferred states. That gives a principled answer to the exploration-exploitation dilemma, instead of a reward function bolted on afterwards, and Vyatkin argues it produces goal-seeking and curious behaviour from first principles.

## What that buys you, on paper

The claimed advantages are the ones current agents lack. Adaptation to novel scenarios without massive retraining. Much lower data and compute for learning. And explainability: you can inspect an agent's beliefs and the policies it is weighing, which makes governance easier than with a black-box model. He also flags robotics, where controlling a body in a changing environment remains a hard problem.

## Many agents, no central controller

Active inference is multi-scale. Agents keep their own boundaries (Markov blankets in the jargon), share world models, and coordinate through belief propagation and message passing, minimising expected free energy as a team. Orchestration can emerge from collective behaviour with no central controller. Vyatkin stretches this toward enterprise systems with traceable, adaptive workflows and, more speculatively, toward agents that act like researchers testing hypotheses.

## Where to start digging

His resource list is the practical takeaway: the textbook by Parr, Pezzulo and Friston, available free from MIT Press; a forthcoming fundamentals book aimed at engineers; libraries in Julia and Python with example agents; and the Active Inference Institute for courses and community.

## Who should watch

Engineers who suspect LLM-in-a-loop agents are not the end state and want a serious alternative to read about, and anyone in robotics or control looking for a principled take on exploration. If you need something to ship next sprint, this is background reading, not a recipe.

## Related Conf42 talks

- [Beyond text generation: the rise of agentic AI](https://www.conf42.com/Machine_Learning_2025_Naman_Goyal_generation_text_agentic), Naman Goyal (Google DeepMind), Conf42 Machine Learning 2025
- [Prompt engineering for agentic safety assurance in physical AI](https://www.conf42.com/Prompt_Engineering_2026_Vraj_Patel_safety_physical_assurance), Vraj Patel (Apptronik), Conf42 Prompt Engineering 2026
- [Autonomy with guardrails: operating agentic automation in high-risk production systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating), Ajay Athitya Ramanathan (FourthSquare), Conf42 SRE 2026

[Watch Alex Vyatkin's talk](https://www.conf42.com/Machine_Learning_2026_Alex_Vyatkin_orchestrating_technological_generation)

[Watch the talk on YouTube](https://youtu.be/M_AA2Tftvws).

## Watch the talk

[Next-Generation AI Agents: Orchestrating Technological Evolution](https://www.conf42.com/Machine_Learning_2026_Alex_Vyatkin_orchestrating_technological_generation) at Conf42 Machine Learning 2026.
