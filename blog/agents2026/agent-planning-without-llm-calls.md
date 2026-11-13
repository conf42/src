# Your agent doesn't need an LLM to plan, just a graph and a search

Conf42 Blog, 2026-08-25, updated 2026-11-09. https://www.conf42.com/blog/agents2026/agent-planning-without-llm-calls

In short: Maureese Williams of Disney at Conf42 AI Agents 2026 shows GATS, a tree-search planner that calls the model only for novel states and caches the answer.

Most agent loops ask the language model what to do next at every single step, even for steps they have already solved a hundred times. At Conf42 AI Agents 2026, Maureese Williams, AI Engineer at Disney, presented GATS (Graph-Augmented Tree Search), a planner that runs UCB1 tree search over a state graph the agent builds for itself and treats the LLM as the last resort.

The payoff is a plan you can replay. The search is deterministic, so identical starting conditions give an identical plan, which is something a sampled model call can't promise.

## The default loop has amnesia

Maureese starts with the mundane bit. A twenty-step task means twenty model calls, every run. On the second run of an identical task the agent asks the identical question and gets an answer drawn from a distribution, not a lookup table.

He counts three costs. Dollars scale with plan depth and never amortise. Latency is inference time multiplied by the number of sequential decisions. And the one he cares most about: the plan isn't reproducible, because the artifact you would need to replay it, a record of the decision procedure, never existed. If a plan fails downstream, you often can't reconstruct how you got there.

## Consult what you can prove, then what you measured

The core of GATS is an escalation ladder with three layers:

- **L1, symbolic.** Known preconditions and effects. Applicability is a set-membership test, effects are add and delete sets. Exact, nearly free, and it covers most of an agent's day.
- **L2, learned.** For actions that turn out to be stochastic, a frequency table per state-action pair, built from what was actually observed. A lookup and an increment.
- **L3, generative.** Only for genuinely novel situations does the model propose effects, and the answer is written into the graph under a canonical state key, like a transposition table in a chess engine.

That last detail is where the money goes. Two action sequences that land on the same world state by different routes collapse into one node and share statistics, cached proposals included. A novel situation costs at most one model call, ever. Episode one builds the graph and pays; later episodes mostly search a graph that already exists. Inside skills, such as writing the text of a diff, the model still does the work it is good at. It just never picks the next action.

## The numbers, with the caveats he insists on

The abstract reports a 100-task suite with 100% success, 100% optimal plans and zero model calls at plan time. In the talk he walks through PlanBench domains (Blocks World, Logistics and a harder hybrid) with 30% of the transition information masked so layers two and three actually fire. GATS solved 148 of 150 tasks; a matched control with the same budget of 2,000 expansions per task solved 65. Letting the graph persist across runs cut total model queries by 83% with no change in tasks solved. The abstract adds a sharper result: with a real local Llama 3.2 behind it, a tree-search baseline fell from 87% to under 1% and ReAct to 36%, while GATS held, because it was never calling the model at plan time.

What makes this talk worth trusting is how much time he spends narrowing the claim. Three domains, one frozen split, one masking condition. An internal review after this analysis had already found a stronger classical baseline that closes part of the gap, and he says so on stage rather than letting the slide imply finality.

## The cache saves money, the heuristic finds the goal

The ablation is the part to steal for your own systems. On 30 tasks, the full system solved 25 with 66,713 model queries. Turn off the graph memory and it still solved 25, with the same mean expansion count, but needed 231,404 queries. Turn off the heuristic instead and it solved 12 while spending even more.

So the graph is an efficiency mechanism, not a correctness one. An agent that fails hard tasks needs a better priority function, not a bigger cache. An agent that is reliable but too expensive is where the cache earns its keep. Asking whether a change moved where the system searches or only what searching costs is a useful habit well beyond planners.

## Who should watch

Engineers building agents over a structured action space (file operations, deploy steps, workflow tools) who are paying for the same decision over and over. The architecture needs a catalogue of named actions with preconditions and effects; open-ended chat with no discrete state gives you no graph, and Maureese says so. Everything shown is single-agent; shared graphs across a fleet are future work. The paper is on arXiv and the code is public on GitHub, with a deterministic backend that runs the suite in under a minute.

## Related Conf42 talks

- [You Cannot Fix a Prompt You Cannot See Fail: Debugging the Plan, Not Just the Answer](https://www.conf42.com/Prompt_Engineering_2026_Krishna_Chaitanya_Balusu_debugging_plan_fail) by Krishna Chaitanya Balusu at Conf42 Prompt Engineering 2026.
- [Beyond Sequential Agents: Orchestrating Hierarchical LLM-Based Agents for Complex Task Decomposition](https://www.conf42.com/Large_Language_Models_LLMs_2025_Aleksandr_Khramogin_sequential_agents_hierarchical) by Aleksandr Khramogin at Conf42 Large Language Models 2025.
- [Your Agent Failed Mid-Run. Logs Won't Replay It.](https://www.conf42.com/MLOps_2026_Reza_Amini_agent_replay_logs) by Reza Amini at Conf42 MLOps 2026.

[Watch Maureese Williams's talk](https://www.conf42.com/AI_Agents_2026_Maureese_Williams_planning_search_graph) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/10MCcG6fLYo).

## Watch the talk

[Your Agent Doesn't Need an LLM to Plan](https://www.conf42.com/AI_Agents_2026_Maureese_Williams_planning_search_graph) at Conf42 AI Agents 2026.
