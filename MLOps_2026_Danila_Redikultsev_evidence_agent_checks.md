# Self-Signed Evidence: Why Your LLM Agent's Green Checks Prove Nothing

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Danila Redikultsev](https://www.conf42.com/speaker_Danila_Redikultsev) (Senior Software Engineer, AI @ Aeroclub). Page: https://www.conf42.com/MLOps_2026_Danila_Redikultsev_evidence_agent_checks

## Abstract

An LLM support agent finds two orders for the same blender, picks one and calls the refund tool. Code confirms the order is the customer's, recent and under the limit, then pays. The broken blender was in the other order.  Putting the check in code did not help: it trusted an order ID the model chose. I call this self-signed evidence.  I build LLM agents that spend customers' money. In public τ²-bench runs I counted 82 of 1,632 conversations where tools accepted a change to an order the task never asked to change; in at least 21, the model picked the order itself.  You will learn to find the model-written values your checks trust, test a check with a swapped order ID, and run it in shadow before it is allowed to block. For engineers whose agents issue refunds or make bookings.
