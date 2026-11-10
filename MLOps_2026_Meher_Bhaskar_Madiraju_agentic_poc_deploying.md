# From PoC to Production: Deploying Agentic AI at Enterprise Scale

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Meher Bhaskar Madiraju](https://www.conf42.com/speaker_Meher_Bhaskar_Madiraju) (Senior Data Scientist @ Walmart Global Tech). Page: https://www.conf42.com/MLOps_2026_Meher_Bhaskar_Madiraju_agentic_poc_deploying

## Abstract

Most agentic AI demos never survive contact with production. Brittle prompts, no evaluation harness, no guardrails, no ownership model, and the prototype quietly dies after the demo. This case study walks through taking an agentic AI system from prototype to a production deployment serving merchants across more than 600 retail locations. It covers the architecture (multi-agent orchestration for assortment planning and optimization), the evaluation and data-contract testing that run in CI, the default-deny data governance layer, monitoring and cost/latency tradeoffs in production, and the failure modes that only appear at scale. Attendees leave with a concrete checklist for moving their own agent prototypes into production: what to instrument first, which gates actually caught bugs, and the organizational changes (ownership, on-call, stakeholder trust) that mattered as much as the technology.
