# Fifty Claude agents in production: let the AI suggest, code decide

Conf42 Blog, 2026-11-09. https://www.conf42.com/mlops2026/fifty-agents-in-production-what-held-up

In short: Muhammad Haris Farooq (Ruby AI) at Conf42 MLOps 2026 on running 50+ Bedrock agents: judges that see tool output, cache traps, and a 75% cost cut.

Getting one agent to work is the demo. Keeping fifty of them accurate, measurable and affordable is the job. At Conf42 MLOps 2026 on November 19, Muhammad Haris Farooq, AI Lead at Ruby AI, shares the patterns that survived running a platform of 50+ Claude agents on Amazon Bedrock for real customers every day.

The agents research companies and the people in them, then write briefings before sales calls. That is a useful workload to learn from: lots of tool calls, lots of web data, a human on the other end who will notice a wrong fact in front of a prospect. Haris promises real traces and numbers, and the abstract already gives a few of them.

## Let the AI suggest, let the code decide

The first rule is a boundary. Scores, formatting and anything that changes a customer's data stay in normal code. The model proposes; deterministic code disposes. Haris gives two reasons, and both are boring in the best way: it is cheaper, and you can test it.

It is a good antidote to the reflex of asking the model to do everything, including the arithmetic.

## A judge that can't see the evidence will fail the witness

Quality monitoring runs in two tiers: quick code checks on every run, and AI judges on a sample of about 1,500 runs a month. The lesson that comes with it is the most quotable thing in the abstract. A judge that cannot see what the agent saw marks correct answers as wrong. Giving the judge the tool results took one answer's score from 0.2 to 0.95.

If you run LLM-as-judge anywhere, that one number is worth the session. A judge grading an answer without the retrieved context is grading against its own memory, and its memory is not your customer's CRM.

## Prompt caching breaks without telling you

Ruby cut cost per run by about 75%, and a big part of that came from prompt caching. The catch: caching also breaks silently. A date in the system prompt, or tools listed in a different order, is enough to miss the cache, and nothing throws an error. Your bill just goes up.

Haris will show how to catch that, including a limit he measured on live Bedrock. This is the kind of detail you only learn by staring at invoices, so it is nice to have someone else do the staring.

## Parallel where it's independent

The last pattern is speed. Running independent agents in parallel cut the time to research a company from about 32 minutes to 11. Nothing exotic, just the observation that agents with no data dependency on each other should not wait in line.

## Who should watch

Anyone with more than a handful of agents in production, or with a plan to get there this quarter. It is especially useful for teams on Bedrock or using Claude models with prompt caching, and for anyone who has set up an LLM judge and quietly wondered why its scores feel off. Haris promises a short checklist you can apply to your own agents the next day, which is exactly the right size for a talk like this.

## Related Conf42 talks

- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty and Karthik Akula, the cost side of agents from a different angle.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev, more on judges that drift.
- [Less Theater, More Engineering: A Production Claude Code + MCP Agent Pipeline at 80% Accuracy](https://www.conf42.com/AI_Agents_2026_Suneet_Malhotra_mcp_pipeline_accuracy) by Suneet Malhotra, another production Claude story with numbers.

[Watch Muhammad Haris Farooq's talk](https://www.conf42.com/MLOps_2026_Muhammad_Haris_Farooq_agents_patterns_production) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Running 50+ AI agents in production: the patterns that held up](https://www.conf42.com/MLOps_2026_Muhammad_Haris_Farooq_agents_patterns_production) at Conf42 MLOps 2026.
