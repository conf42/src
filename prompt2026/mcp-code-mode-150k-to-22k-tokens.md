# Code Mode cut an MCP agent's tool context from 150K to 22K tokens

Conf42 Blog, 2026-10-11, updated 2026-11-09. https://www.conf42.com/prompt2026/mcp-code-mode-150k-to-22k-tokens

In short: Adobe's Nishant Kumar Thakur and Sonam Raj at Conf42 Prompt Engineering 2026 on typed tool stubs for MCP, what they saved and where they broke.

Adobe's production agent was burning 150K tokens on tool definitions before the user typed a word, and picking the right tool only 42% of the time. At Conf42 Prompt Engineering 2026, Nishant Kumar Thakur, Senior Computer Scientist, and Sonam Raj, Computer Scientist, both at Adobe, showed how switching to Code Mode (typed API stubs the model reads like library code) took that to 22K tokens and 80% tool-selection accuracy, then spent a refreshing amount of time on what went wrong.

Same tools, different presentation. That's the whole trick, and the details are where it gets interesting.

## The fixed context tax

Their agent connects to everyday developer tools: Outlook, SharePoint, Jira, Confluence, Slack and a few others. Connect them all through plain MCP schemas and 75% of a 200K context window is gone before anyone says hello. The talk opens with an even bigger number from Cloudflare: describing 2,594 tools took about 1.17 million tokens, nearly six times a 200K window.

The second cost is less obvious. Ask the agent to attach a meeting transcript from Google Drive to a Salesforce lead, and the transcript enters the context on the read, then gets written out again as an argument on the update. You're paying a frontier model to copy and paste.

The third is accuracy. When nearly every service has a search, get and list operation with similar names, the model gets confused. That 42% doesn't show up on your token bill, but it shows up everywhere else.

## Let the model write code against a typed API

The idea, credited to Cloudflare's Code Mode and a similar Anthropic write-up: models have seen far more real code than tool-call JSON, so give them a typed API and let them write a script. The script runs in a sandbox, intermediate data stays in variables, and only the result returns to the model. Tool definitions load on demand through progressive disclosure, so the model explores the available tools like a developer browsing a code base.

On their production agent, with the same tasks and model, prompt tokens before the user's question went from 150K to 22K, an 85% reduction. Tool-selection accuracy went from 42% to 80%. Their explanation is that the model sees fewer similar tools at once and focuses on the typed definitions it needs.

## The demo didn't hit the headline number

The live demo uses Pi, an open source terminal coding agent with Code Mode built in, against dummy Jira, Confluence and Slack MCP servers with 86 tools. With direct tool calls, tool definitions alone took 54K tokens, and one task (review five Jira bugs and two runbooks, post a summary to Slack) reached about 98K. With Code Mode the session started at 1.2K tokens, and the same task landed around 34K: a 65% reduction, "but not quite what we expected", as they put it.

The reason is instructive. One well-behaved script made five MCP calls in parallel, picked only the needed fields and trimmed descriptions to 400 characters. Others returned full Jira issues and complete search results. Code Mode removes the upfront schemas; it doesn't control what comes back.

## Five ways it broke

Nishant's honest section lists the failure modes. The model called methods that didn't exist, so the sandbox returns the closest match and they treat it as a retry. MCP servers changed and generated stubs went stale, so stubs are regenerated at connection time. One big types file per server recreated the schema dump in a new format; the fix was one file per tool. Output bloat needed an explicit instruction to return only necessary fields. And debugging got harder, so every tool call inside the sandbox is logged with arguments and result size.

They're also clear about when not to use it: agents with three tools, setups without a trusted sandbox, and workflows that need human approval at every step. In those cases tool search, which keeps normal tool calling but loads only relevant definitions, is the simpler option.

## Who should watch

Anyone running an agent against more than a handful of MCP servers. The homework is cheap: log prompt tokens just before the user message is added, try Code Mode on one task, and compare with the same model. If that first number is already in the tens of thousands, you have a project.

## Related Conf42 talks

- [Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) by Elizabeth Fuentes Leone of AWS at Conf42 AI Agents 2026.
- [Observing Agentic/MCP Traffic & Keeping Costs Low](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) by Michael Levan of Solo.io at Conf42 DevOps 2026.
- [Beyond the Context Window: Building a "Mental Model" for Your AI Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lior_Schejter_context_agents_reasoning) by Lior Schejter at Conf42 Large Language Models 2026.

[Watch Nishant Kumar Thakur and Sonam Raj's talk](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/YXPBJffFe5o).

## Watch the talk

[From 150K to 22K Tokens: Context Engineering for MCP Tool-Calling](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) at Conf42 Prompt Engineering 2026.
