# Fifty agents in production, and a prompt cache at 0% for months

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/fifty-agents-in-production-what-held-up

In short: Muhammad Haris Farooq (Ruby AI) at Conf42 MLOps 2026 on four patterns for 50+ Claude agents on Bedrock: code decides, visible quality, cost per run, speed.

For months every request succeeded, nothing alerted, and the prompt cache hit rate was 0%. At Conf42 MLOps 2026, Muhammad Haris Farooq, who leads AI engineering at Ruby AI, opens with that bug: prompt caching was switched on, but the code joined the system prompt into one plain string and threw the cache markers away. The fix was a few lines. Finding it took a look at the cost of single runs. The rest of his talk is four patterns that each remove a place where an agent system can be wrong without telling you.

His platform runs more than 50 types of agents on Claude Sonnet and Haiku on Amazon Bedrock, about 3,800 production runs a month, all traced in Langfuse. "They don't fail loudly, they fail quietly, and they still give you something that looks fine," Muhammad Haris Farooq said at Conf42 MLOps 2026.

## Let the AI suggest, let the code decide

Math, formatting and changes to customer data go to code. For deal scores, the model reads the evidence and returns a finding with a citation per factor; a weighted formula does the arithmetic, so when someone asks why a deal is a 62 there is an answer.

Formatting was the expensive surprise. Document agents wrote Markdown, and 36 to 45 percent of their output tokens were headings, bullets and tables. Now the model returns content as JSON and code builds the document. Ruby AI moved 22 of 23 document agents and output tokens fell between 21 and 78 percent per agent. For data changes, the chat assistant proposes a card, the user confirms, and code makes the change.

## A judge that cannot see the tool results marks true answers as false

Quality runs in two layers. Cheap code checks run on every run: output shape, leaked tool text, internal names. AI judges run on a sample: a grounding judge on 20% of runs for about 30 customer-facing agents, and a second judge on 10% that asks one thing, whether the output is about the right company.

The first grounding score for a good analysis was 0.2 out of 1. The judge had seen only the prompt and the answer, so every fact the agent looked up appeared invented. With tool outputs added to the trace, the same answer scored 0.95, with 18 of 19 claims backed up.

Scores also lie in boring ways. A check for leaked IDs fired on every run because signed download links are long random-looking strings. A check that always fires is broken, and a score that never moves is dead. Before trusting a judge the team planted known bad cases, and it caught eight of eight. A later test still found it too lenient.

Then the humbling one: in a model comparison, one model won on every score and had written a whole brief about the wrong company. Someone had to read it. They still read outputs, and they fired every alert once on purpose to confirm it arrives.

## Caching can cost you money

Every model call goes through one place that prices it, cache reads and writes included, and attaches the cost to the run. That alone surfaced an agent making 34 model calls per run. Over a few months the cost of an agent run came down about 75%, a figure Haris flags as measured on staging by running the same deal five times.

Three changes did most of it: collapsing loops of 8 to 12 model rounds into two or three, fixing the silent cache bug, and trimming tool results in code. One tool returned 2,000 to 7,000 tokens of raw data; a small function now passes 300 to 500, and answers got more accurate.

Writing to a five-minute cache costs one and a quarter times the normal input price and reading costs a tenth, so break-even is about 0.28 reads per write. Four agents almost never got a second read in time, and caching was turned off for them.

Bedrock also changed under him. In early October every tool call and tool result counted as a step in the cache lookback, so turns with many parallel tool calls lost the cache. By the end of October a group of parallel calls counted as one step. He maintains a small open source tool, Cache Canary, to retest this. His advice: "Don't trust last quarter's blog post, including mine".

He lists what failed, too. A lower effort setting cost 24 to 64 percent more input because the model made tool calls one by one. A cache warmer logged "warmed" while never getting a hit. Doubling parallel workers looked 64 percent better on one sample and 16 percent worse on three. A newer model's tokenizer produced about 48 percent more tokens with no quality gain.

## Draw the dependency graph before you hide the wait

Researching a new company took about 32 minutes, and the proposal on the table was to text users updates while they waited. The timeline showed 13 agents running one after another. Grouped by real dependencies, seven could run first, then four, then two. The median dropped from 32.5 minutes to about 10.7 and held around 11 over 700 production runs in 45 days. The text feature was never built.

## Who should watch

Anyone running LLM agents for paying customers, particularly on Bedrock with prompt caching enabled and unverified. It is a slide talk with real numbers and a seven-item checklist at the end.

## Related Conf42 talks

- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty (AWS) at Conf42 AI Agents 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.
- [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg of Microsoft AI at Conf42 MLOps 2026.

[Watch Muhammad Haris Farooq's talk](https://www.conf42.com/MLOps_2026_Muhammad_Haris_Farooq_agents_patterns_production) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Running 50+ AI agents in production: the patterns that held up](https://www.conf42.com/MLOps_2026_Muhammad_Haris_Farooq_agents_patterns_production) at Conf42 MLOps 2026.
