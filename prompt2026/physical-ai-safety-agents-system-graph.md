# Physical AI safety agents should reason over a system graph

Conf42 Blog, 2026-10-06, updated 2026-11-09. https://www.conf42.com/prompt2026/physical-ai-safety-agents-system-graph

In short: Vraj Patel of Apptronik at Conf42 Prompt Engineering 2026 on bounded agents, system graphs and skills for safety assurance in robots and AVs.

Robots and autonomous vehicles keep changing after they ship, and the safety case has to keep up with every new perception model. At Conf42 Prompt Engineering 2026, Vraj Patel, Staff Systems Engineer at Apptronik and formerly at May Mobility, showed how bounded, human-supervised agents can help with continuous safety assurance, as long as they reason over an explicit system graph instead of a loose pile of documents.

His thesis is that a prompt alone isn't enough here. The context has to be engineered first. Vraj presented in his individual professional capacity, and the framework he showed is illustrative rather than a specific employer's system.

## The documents outpace the engineers

Building a humanoid, an autonomous mobile robot or an AV produces engineering docs, safety analyses, prototypes, hypotheses and evidence at a pace that grows as teams lean on tools like Claude and Codex. The material ends up fragmented across tools. An agent pointed at that mess will happily produce plausible safety claims. Vraj's answer is to give it four pillars to stand on: a system graph, skills, tools and data, and governance with approvals.

## Build the graph before the prompt

The system graph starts with the operational design domain (ODD): where the system works, whether a warehouse, a city limit or a construction site, and under which conditions, such as rain or sunlight. From there it maps objects and interactions, hazards (especially to humans), safety goals, requirements, verification criteria and finally claims. Edges carry relations such as "mitigates a hazard" or "is verifiable", so the graph bounds where an agent can wander.

The sources stay whatever teams already use: Jama or Doors for requirements, Draw.io or Miro for architecture, Confluence and Jira for docs, Git for releases. The abstract keeps the model-based systems engineering (MBSE) model as the single source of truth, with frameworks such as ISO 26262, ISO 21448 (SOTIF), UL 4600 and ASPICE as guides.

## Skills with golden cases

Vraj shows a hazard coverage skill as a template: a triggering condition, inputs, the procedure the agent runs, and an output (JSON or Markdown) where every item carries a unique ID. The guideline baked in: never override, never claim safety without human approval. Each skill gets golden cases to evaluate against.

His worked scenario is a person cutting into the path of a moving unit after the perception model is revised. The agent detects what changed in the model, finds the impacted scenarios, hazards and controls, checks coverage and whether other systems are affected, and escalates if the safety scenarios need a rerun. In his words on the slide, the outcome is a traceable question for an engineer, not an autonomous safe-to-release verdict.

## Agents are software that can fail

The point that will land with anyone who has written a safety case: treat the agent workload itself as something that needs its own safety case. Measure evidence validity, false positive rate, classification quality, tool compliance and reviewer acceptance. The abstract names the risks to watch: hallucinated evidence, incomplete context, prompt drift and over-automation.

Human authority is an architectural requirement here. Agents can read and retrieve; they can't write or override without a person signing off, and whoever approves the output owns it. "The AI did it" is not an accountable party.

## Start with one vertical slice

The roadmap is refreshingly modest. Build a small graph for one vertical, connect the sources, ship one skill, evaluate it, harden it, then expand. His three takeaways: engineer the context, package the procedure, and command the action. Traceability from evidence to decision to claim is the core competency the standards ask for anyway.

## Who should watch

Systems and safety engineers in robotics, AVs and other physical AI, plus anyone building agents for regulated engineering workflows. It's an architecture talk with no live demo, and the system graph is the part worth sketching on your own whiteboard.

## Related Conf42 talks

- [Scalable HIL Architecture: Observability-Driven Validation in Software-Defined Vehicles](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) by Sumaiyya Fatima of General Motors at Conf42 Observability 2026.
- [You Can't Rerun Sunlight: Designing ML Data Architectures for Physical AI](https://www.conf42.com/MLOps_2026_An_Phan_physical_sunlight_data) by An Phan of Hippo Harvest at Conf42 MLOps 2026.
- [Human–AI Collaboration for Reliable Embedded Automotive Control Systems](https://www.conf42.com/DevOps_2026_Alagar_Raja_Govindasa_human_automotive_control) by Alagar Raja Govindasa of Dorman Products at Conf42 DevOps 2026.

[Watch Vraj Patel's talk](https://www.conf42.com/Prompt_Engineering_2026_Vraj_Patel_safety_physical_assurance) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/BMnD5wXO0mc).

## Watch the talk

[Prompt Engineering for Agentic Safety Assurance in Physical AI](https://www.conf42.com/Prompt_Engineering_2026_Vraj_Patel_safety_physical_assurance) at Conf42 Prompt Engineering 2026.
