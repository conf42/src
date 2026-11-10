# A customer-facing agent got reliable outside its prompt

Conf42 Blog, 2026-10-13, updated 2026-11-09. https://www.conf42.com/prompt2026/customer-facing-agent-reliability-outside-prompt

In short: Nowlun's Ahmed Gaber and Ahmed Morsi at Conf42 Prompt Engineering 2026 on clean data, code-held rules and staged evals for a freight sales copilot.

The copilot said there was no price for a 40-foot container from Shanghai to Jebel Ali, opened a request to the pricing team, and 35 minutes later a human quoted a rate the system already had. At Conf42 Prompt Engineering 2026, Ahmed Gaber, Director of Product Engineering, and Ahmed Morsi, Product Engineer, both at freight platform Nowlun, walked through a year of running an AI copilot beside their sales team, and why most of its reliability came from the data and the system around the prompt.

The recording is presented by Ahmed Morsi. The short version, in his words: get the data right, build the system, and measure every change.

## The setup: a copilot, not an autopilot

Nowlun customers compare, book and track sea and air freight, and every shipment starts with questions: the price to Jeddah, a Monday booking, a missing container. The copilot reads the ask, searches prices and quotes, drafts the reply and fills in the CRM. A sales rep sends, edits or picks up the phone. When the copilot can't help, it steps back with a reason from a fixed list.

## Part one: the data was the bug

That missing Shanghai price existed three times, saved under different aliases for the port. It happened more than two hundred times in a month. The fix was "one thing, one ID": every spelling becomes an alias on one record, so 14 spellings map to one port code. Don't list spellings in the prompt, he warns; the list is never complete and costs tokens every turn. Searches that missed an existing price dropped from 30% to 4%.

The second habit is that field descriptions are prompts. More than a quarter of their fields had nobody who could say what they meant, so the team wrote a dictionary. The entry for the "comparing" stage now reads "Collecting quotes, not ready to book. Offer to hold the price. Don't push a booking." That sentence lives with the field and travels into tool descriptions and onboarding. Tool calls with a wrong argument fell from 18% to 5%. Before touching the prompt, pricing requests for prices they already had went from more than two hundred a month to thirty, and finding the right price went from eleven minutes to forty seconds.

## Part two: rules live in code when they're costly and checkable

They wrote the search-first rule into the prompt in capitals, and the copilot still opened requests without searching. So the rule moved into the request tool: no search, no request, and the refusal says what to do instead.

Ahmed describes code versus prompt as a dial. Far left, code hides tools until the stage allows them or enforces a sequence. In the middle sits what they call refuse then check: an LLM judge reviews a stated reason, and after two refusals the call goes through, so a wrong judge can't leave the copilot stuck. Further right, hints in tool results. Far right, judgment left to the model.

Writes get stricter checks than words. A hallucinated "we ship coal" saved to the CRM marked a lead as a prohibited commodity, set it to lost and stopped all follow-ups. Now every write tool must carry a sourced quote from the conversation, fuzzy-matched against the thread.

Their 500-plus line prompt turned out to be nine places that never saw each other, holding 70 rules and 24 conflicts. A nine-question decision list now gives each instruction one home, and only rules that hold on every turn in every stage reach the base prompt. On 44 scripted conversations with the same model, passing went from 55% with one big prompt to 70% when split by owner, and to 80% once the conflicts were settled.

## Part three: measure every change

A price search refactor silently dropped the expiry filter; a pricing analyst noticed days later. After that, every change got measured. Step-backs caused by the copilot itself fell from 46% in Q2 to 1% in Q4, leaving the rest as real sales work. Tests are recorded at the first stage they fail, an idea he credits to a talk featuring Hamel Husain on failure funnels, and graded on what the copilot did, what the system actually saved and what it said.

Two stories stand out. Tone: suggestions were about fifteen times longer than reps' typical WhatsApp replies, because the tone rewriter never saw the conversation. And the rare coal-style fabrication showed up 2 times in 1,000 replays at temperature 1, too rare to prove a fix, so they replayed at 1.5 to get 15 in 1,000, then drove it to zero with the source-quote parameter.

## Who should watch

Anyone running an agent that talks to customers or writes to a CRM. It's long and packed with real numbers, and the closing checklist (one ID per thing, code what's costly and checkable, one home per instruction, staged evals, hot replays) is directly usable.

## Related Conf42 talks

- [From Demo to Deployment: Building, Evaluating, and Observing Multimodal Conversational Agents](https://www.conf42.com/DevOps_2026_Gobu_Natarajan_multimodal_agents_conversation) by Gobu Natarajan of Amazon at Conf42 DevOps 2026.
- [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg of Microsoft AI at Conf42 MLOps 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.

[Watch Ahmed Gaber and Ahmed Morsi's talk](https://www.conf42.com/Prompt_Engineering_2026_Ahmed_Gaber_Ahmed_Morsi_agent_front_facing) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/794OxfKswF4).

## Watch the talk

[What Running a front facing AI Agent Taught Us About Prompt Engineering](https://www.conf42.com/Prompt_Engineering_2026_Ahmed_Gaber_Ahmed_Morsi_agent_front_facing) at Conf42 Prompt Engineering 2026.
