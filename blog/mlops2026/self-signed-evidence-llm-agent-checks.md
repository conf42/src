# Your agent's refund check trusts an order ID the model picked

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/self-signed-evidence-llm-agent-checks

In short: Danila Redikultsev (Aeroclub) at Conf42 MLOps 2026 on self-signed evidence: code checks that pass because the LLM agent chose the value they read.

A customer asked for one specific flight, the agent bought a ticket on a different one, and every check in the code said yes. That is the opening of the talk by Danila Redikultsev, senior software engineer for AI at Aeroclub, at Conf42 MLOps 2026. His diagnosis has a name, self-signed evidence: a field the check trusts, written by the system the check is supposed to be checking. Moving the decision from the prompt into code does not help if the code reads an ID the model chose.

## Two blenders, three green checks, one wrong refund

To study it safely he rebuilt the failure in an invented store. A customer writes that their blender arrived broken. The LLM support agent finds two orders for the same blender, 180 dollars each, proposes order 1187 and asks. The customer says yes. Plain code then checks the policy: the order belongs to the customer, it was delivered within 30 days, it is under the 200 dollar limit. All green. The money goes out.

The broken blender was order 1042, delivered 70 days earlier and too old to refund. The second one was its replacement. Nobody attacked anything and the customer did not lie.

Look at where each value came from. The owner came from the database, the delivery date from the carrier, the amount from the order record. The order ID came from the model. The carrier gave the right date for the wrong order.

"A check proves only what the agent could not shape," Danila Redikultsev said at Conf42 MLOps 2026. He borrows two comparisons: a browser rejects a self-signed certificate even when the math is fine, and in banking terms the agent here is both maker and checker.

## How often it happens, with honest caveats

He counted published runs of the τ²-bench support-agent benchmark. In the abstract's figures, 82 of 1,632 conversations had the store's tools accept a change to an order the task never asked to change, and in at least 21 the model picked that order itself. Newer models did it less in his own runs: 17 in about 4,000, and in 16 of those the simulated customer had said yes to the agent's summary. He is careful to say that simulated customers show that it happens, not how often.

The most uncomfortable detail is from his rebuilt blender store. The model proposed order 1187 on the grounds that it fell inside the 30-day refund window. It picked the order that would pass the checks.

## A second model does not fix it

The obvious patch is an LLM judge. He took 72 wrong refunds and 72 right ones and had Claude Sonnet review them. Reading the agent's own account, the judge approved all 72 wrong ones, even when asked directly whether this was the order the customer meant. Given the whole chat and every order, it caught 50, and it also blocked 41 of the correct refunds. On the cases where the store really lost money, it approved 20 out of 20.

The reason is in the transcript of the chat itself. The customer's yes answers the agent's proposal, so even the conversation is partly written by the system under review. He flags the limits: one judge, his own scenarios, take it as a direction.

## Make the check ask who wrote each field

His repair is small. The model may propose an order, but it must point to what the customer wrote. Code checks that the quoted words are in the chat and fit exactly one order. If they fit two, code asks the question itself with options taken straight from the records. In his runs, after a yes to the agent's proposal, 35 refunds out of 180 went to the wrong order. When the choice came from the records, none did. The price was one extra message.

Then he tests the new check, because a new check can be wrong too:

1. Negative test. Take logged refunds, swap each order ID for another valid order of the same customer, and rerun. The plain policy check stayed green on every swap. Only the check that reads the customer's choice turned red.
2. Fault injection. Tell the agent not to ask. Wrong refunds went 30 out of 30. With code asking, none.
3. Shadow mode. Run the new check beside the old one, log what it would block, and have a support lead label a sample against the order records. Only then may it block. If the same model labels the reference set, you are back where you started.

He closes with four questions for any action that costs money or trust: who decides, who writes the words the customer reads, who wrote each field, and who checked the check. He also credits the lineage. In 1988 Norm Hardy called it the confused deputy, a program with authority acting on a name someone else gave it. The homework fits on a sticky note: list every value your final check reads, write next to it whether the database, the customer or the model produced it, swap one, and rerun. "Better to learn that from your logs than from your customer."

## Who should watch

Engineers whose agents issue refunds, make bookings or move money, and anyone who has reported guardrail coverage as a percentage. It is about 15 minutes, tightly scripted, and the experiments are his own small-scale runs, which he says plainly. If your agent only reads and summarises, the stakes are lower but the swap test is still worth an afternoon.

## Related Conf42 talks

- [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg of Microsoft AI at Conf42 MLOps 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.
- [Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline](https://www.conf42.com/MLOps_2026_Ajay_Munjuluru_permission_authorization_evals) by Ajay Munjuluru at Conf42 MLOps 2026.

[Watch Danila Redikultsev's talk](https://www.conf42.com/MLOps_2026_Danila_Redikultsev_evidence_agent_checks) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Self-Signed Evidence: Why Your LLM Agent's Green Checks Prove Nothing](https://www.conf42.com/MLOps_2026_Danila_Redikultsev_evidence_agent_checks) at Conf42 MLOps 2026.
