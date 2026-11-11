# Send your agent three tools, not twenty-nine

Conf42 Blog, 2026-09-12, updated 2026-11-09. https://www.conf42.com/blog/agents2026/send-the-agent-three-tools-not-twenty-nine

In short: Elizabeth Fuentes Leone (AWS) at Conf42 AI Agents 2026: semantic tool selection with a vector search cuts token spend and wrong tool picks.

Every call your agent makes to the model carries the description of every tool it owns, whether the question needs them or not. At Conf42 AI Agents 2026, Elizabeth Fuentes Leone, Developer Advocate at AWS, showed the fix in a single Jupyter notebook: put the tool descriptions in a vector store, retrieve the top three for each query, and give the model only those.

## Two bills from one design choice

Her framing is a dual problem. The first is cost. With 29 tools, all 29 descriptions are serialised into the context on every invocation, and if the agent has memory, that context keeps growing. A one-line question still pays for the whole toolbox. The second is accuracy: the more similar and generic the tool descriptions, the more often the model picks the wrong one, and a wrong tool means a wrong answer.

Semantic tool selection attacks both at once. The query goes to a FAISS index of tool names and descriptions first, the index returns three candidates, and only those reach the LLM. Her example is a travel assistant asked about a price, which gets back the pricing and comparison tools rather than the hotel search. Her slide put the token saving at almost 85 percent against the traditional approach.

## Two agents, same queries, measured against ground truth

The demo builds the same travel agent twice with the Strands Agents SDK, the open-source, model-agnostic framework that AWS maintains (she runs it against OpenAI to make the point that it works with other providers). The first agent receives all 29 dummy tools on every query. The second runs the semantic search first. Each test query carries the tools that should answer it, so the notebook scores tool choices against ground truth instead of eyeballing them, and Strands' built-in usage metrics report the tokens per call.

She is candid about the results. The token saving is large and obvious. Accuracy improved but is not perfect, because the 29 tools were deliberately simple, with vague descriptions. That turns into one of her takeaways: retrieval can only be as good as the descriptions you index, so write tool descriptions like they matter. They are now search documents.

## Keep the memory, swap the tools

The first version builds a new agent per query, which is fine for benchmarking and useless in production, because each fresh agent forgets the conversation. The second version keeps one agent and uses Strands' tool registry to clear and re-register only the three retrieved tools before each turn. The chat history survives, the context holds only the tools for the current question, and the token count grows only with the history itself. If you use LangChain or LangGraph, she notes, you will need to find the equivalent mechanism in that framework.

## From notebook to managed service

A local FAISS index is right for learning and prototyping, and wrong for running a fleet of agents. For production she points to Amazon Bedrock AgentCore Gateway, a managed service that does the semantic tool search behind an MCP-style interface. You register tools from Lambda functions, external code or MCP servers, and the gateway returns the best matches with no embedding model or index for you to maintain. Her repository includes the infrastructure as code for that setup, and the talk is part of a series on stopping agent hallucinations, so related techniques sit in the same code.

## Who should watch

Anyone whose agent has grown past a dozen tools, or whose token bill grows with every new integration. It is a practical, code-first talk, and the second half is an AWS product pointer, which she flags herself. The pattern itself works with any vector store and any framework that lets you swap tools per turn.

## Related talks

- [From 150K to 22K Tokens: Context Engineering for MCP Tool-Calling](https://www.conf42.com/Prompt_Engineering_2026_Nishant_Kumar_Thakur_Sonam_Raj_mcp_tokens_context) by Nishant Kumar Thakur and Sonam Raj
- [Stop AI Agents from Making Up Facts: Graph-RAG for Reliable Data Retrieval](https://www.conf42.com/MLOps_2026_Elizabeth_Fuentes_Leone_graph_rag_retrieval), another part of her series
- [Beyond the Context Window: Building a "Mental Model" for Your AI Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Lior_Schejter_context_agents_reasoning) by Lior Schejter

[Watch Elizabeth Fuentes Leone's talk](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost)

[Watch the talk on YouTube](https://youtu.be/8Dxg8CmJWsI).

## Watch the talk

[Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) at Conf42 AI Agents 2026.
