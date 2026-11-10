# Your agent's prompt is one layer, not the whole system

Conf42 Blog, 2026-09-29, updated 2026-11-09. https://www.conf42.com/prompt2026/agent-prompt-is-one-layer-not-the-system

In short: Emerson Braun of Plan A Technologies at Conf42 Prompt Engineering 2026 splits agent reliability into six layers so a fix lands in the right one.

When an agent misbehaves, the first reflex is to open the prompt and add another sentence. At Conf42 Prompt Engineering 2026, Emerson Braun, Staff Engineer and Regional Director at Plan A Technologies, argued that the prompt is only one part of the design, and that a reliable agent needs context, contracts, outputs, retries and evals that live outside it.

His case study is small and relatable: a content pipeline he built for his own posts on X and LinkedIn. Threads published, the blog post went out, the newsletter got scheduled. Then one post was saved as an empty draft. He fixed the prompt, as everyone would, and then realised the prompt wasn't where the bug lived.

## Your agent is perfectly designed to get the result it gets

Emerson borrows the old systems-thinking line that every system is perfectly designed to get the result it gets, and points it at agents. If brand rules, approval policy, "don't post twice", output format and the draft-validate-publish steps all sit in one prompt, then a failure gives you no idea which of those layers broke. Everything is an instruction, and every instruction is a polite guess.

So he splits the work into six layers: context, contract, output, retries, the prompt itself, and evals. Each one gets its own diagnostic question.

## Context is an input, so version it

The first failure he describes is stale context. The agent was told to follow the brand guide and it did, faithfully, using version three, while marketing had shipped version four the week before. The prompt was fine. The input was wrong.

His fix is to treat context like any other input: record which version was loaded, when, and a hash, so you can reconstruct exactly what the agent saw. The question to ask is whether the agent had the right information and whether it was current.

## If the tool allows it, the prompt doesn't forbid it

"Never publish without approval" is a sentence. A publish tool that accepts any call is a capability. When the two disagree, the capability wins. Emerson tiers actions by risk: low-risk reads, searches and classification run alone; reversible actions run within policy limits and with enough record to reconstruct them; high-impact actions such as deletes go to a human. And the human needs the impact and the context of the decision in front of them, not a random ID and an approve button.

## The empty draft was a correct refusal

The empty post turned out to be the model doing the right thing. The draft was requested for another brand's account, the model refused, and the pipeline saved the refusal as an empty draft. The real bug was that nothing checked the output against a contract. Emerson's rule: parse and validate model output the way you'd validate a third-party API, and when it doesn't match, record why.

## Failure is a state, and retries need a key

Retries get the same treatment. A timeout on "publish" followed by a blind retry is how you publish twice. He uses idempotency keys, a state machine that knows what to do after a failure, bounded retries that hand off to a dead letter queue or a person, and recovery that regenerates only the missing part instead of starting from scratch. Automate the recovery decisions, not the retries.

## Shrink the prompt, then judge the purpose

Once the rules move out into code, the prompt shrinks to its core: stable policy, task context, retrieved knowledge and user intent, kept separate. A good test for whether something belongs there: does the failure change when you change the words? If it does, it's a prompt problem. If not, look elsewhere.

His first eval run is the warning shot. Seven drafts, all checks green, and the drafts were still empty or written with the wrong context. The checks measured format, not purpose. He ends with six questions to ask before touching the prompt, one per layer, and a closing challenge: which of your rules lives only in a prompt?

## Who should watch

Anyone running an agent with real side effects (posting, merging, sending, deleting) who keeps patching the system prompt after every incident. It's a short, practical talk built around one honest failure, and the six questions are easy to steal for a postmortem template. If you want the observability half, Emerson points to his earlier Conf42 talk on tracing agents.

## Related Conf42 talks

- [Make Agents Observable: Tracing Decisions, Tool Calls and Recovery](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) by Emerson Braun at Conf42 Observability 2026.
- [A Rule Is a Door: What Changes When You Enforce an AI Agent's Rules in Code](https://www.conf42.com/MLOps_2026_Dylan_Merigaud_rules_agent_code) by Dylan Merigaud at Conf42 MLOps 2026.
- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty and Karthik Akula at Conf42 AI Agents 2026.

[Watch Emerson Braun's talk](https://www.conf42.com/Prompt_Engineering_2026_Emerson_Braun_contracts_context_agent) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/xriFNqUxZlM).

## Watch the talk

[Prompting Is Not the System: Engineering Context, Contracts and Reliable Agent Behavior](https://www.conf42.com/Prompt_Engineering_2026_Emerson_Braun_contracts_context_agent) at Conf42 Prompt Engineering 2026.
