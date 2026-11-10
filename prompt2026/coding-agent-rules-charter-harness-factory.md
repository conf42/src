# Charter, harness, factory: who owns each coding agent rule

Conf42 Blog, 2026-09-30, updated 2026-11-09. https://www.conf42.com/prompt2026/coding-agent-rules-charter-harness-factory

In short: Ian Johnson of Parento at Conf42 Prompt Engineering 2026 maps where a coding agent gate can sit and who gets paged when that rule is wrong.

In most teams running coding agents, a new rule lands wherever the person who noticed the problem happens to have commit access. At Conf42 Prompt Engineering 2026, Ian Johnson, Staff Software Engineer at Parento and author of Harness Engineering, gave that mess a map: three contexts (charter, harness, factory), six rungs where a gate can physically sit, and two boundary lines that tell you who owns each one.

This is an org-design talk wearing a prompt engineering badge, and it's better for it.

## Three contexts, one arrow

Ian splits what most people call "the harness" into three layers. The charter says what this project is about: rules, hooks and skills that live in the repository and change constantly. The harness says how a turn happens: tools, context and prompting, changing rarely but with big impact when it does. The factory says how work ships: stages, gates, guards and records, changing least of all.

Dependencies point one way, from factory to harness to charter. The factory hands work to the harness; the harness reads the charter to understand the code base. If the charter configured the harness, one repository would govern the entire fleet. And a harness that knows about the factory can't run on a laptop, which he treats as a design smell you can test for.

The two failure stories in his abstract will feel familiar. Platform ships a harness and finds one team's opinion inside it. Development writes a charter and spends a third of it trying to configure a pipeline it can't reach.

## A ladder that alternates inference and determinism

The middle of the talk is the ladder. In the charter, a gate can be a rule (the agent is told, nothing enforces it) or a hook (a cheap, deterministic script fired on an event). In the harness, it can be a judging phase (an inference call) or a predicate (a boolean check). In the factory, it can be a review stage (inferential, looking at one turn's output) or a stage gate (deterministic, firing on the published diff).

Walking up, you swap between inference and determinism at every step. Ian doesn't say climb to the top. Inferential rules feed forward and deterministic checks feed back, and you want both. Two more things stay deliberately off the ladder: the tool grant, because it withholds a capability, and CI, because it sits outside the work.

His worked example takes one sentence, "every HTTP call goes through libhttp", and shows it living at three addresses with three owners. The same predicate at two boundaries isn't one rule enforced twice, he argues, because each boundary sees different things: the in-harness check sees tool calls and state, the factory sees the whole finished tree, and the charter only sees what's in context for the turn.

## Two lines, and they cross in the harness

The context line asks what a thing governs: a project, a turn or a delivery. The ownership line asks who gets paged when it's wrong. Both agree at the charter (development) and at the factory (platform). They cross inside the harness, which is where your org-design arguments have been happening all along.

He splits the harness component by component. Platform owns the prompt skeleton and contract; development owns what the repository contributes. Platform owns which tools exist; development picks which get a phase. Platform owns the budget ceiling, because that's money. And for policy, the rule that makes shared ownership survivable: platform sets the floor, development tightens and never loosens. A repository that can loosen the floor has no floor, only a default, so every legitimate loosening gets a named escape hatch.

## Honest about the evidence

Ian is upfront that his change-rate diagnostic (a quarter with three factory changes and no charter ones means the distribution is wrong) comes from his own repositories and one production code base, so there's no benchmark. He also says the harness split is where he has changed his mind most. That candour makes the model easier to trust.

## Who should watch

Platform engineers building internal agent tooling, and tech leads tired of the same argument about where a rule belongs. The homework is concrete: publish the floor as one versioned file, switch the factory off and see if a turn still runs, and for your loudest rule, name the rung it actually sits on. If the answer is prose and you expected a gate, that gap is next week's work.

## Related Conf42 talks

- [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal at Conf42 DevSecOps 2026.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar at Conf42 Large Language Models 2026.
- [From Prompts to Review Harnesses: Scaling AI Code Reviews Across 70+ Software Projects](https://www.conf42.com/AI_Agents_2026_Guido_Scheffler_code_review_harness) by Guido Scheffler of CGI at Conf42 AI Agents 2026.

[Watch Ian Johnson's talk](https://www.conf42.com/Prompt_Engineering_2026_Ian_Johnson_gate_whose_it) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/IiggBbE2j-g).

## Watch the talk

[Whose gate is it?](https://www.conf42.com/Prompt_Engineering_2026_Ian_Johnson_gate_whose_it) at Conf42 Prompt Engineering 2026.
