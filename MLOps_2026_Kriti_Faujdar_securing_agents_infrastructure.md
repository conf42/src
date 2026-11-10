# Securing the AI Stack: From Models to Agents to Infrastructure

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Kriti Faujdar](https://www.conf42.com/speaker_Kriti_Faujdar) (Lead Product Manager @ Yelp). Page: https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure

## Abstract

Training the model is the easy part. Shipping an AI system you'd trust with real data, real tools, and real actions is where teams stall, usually because nobody has a map of where the risks actually live.  In this lightning talk, I'll give you that map: a four-layer defense-in-depth framework for production AI, with the one threat and one fix that matter most at each layer.  Model: indirect prompt injection. Fix: validate every output before it drives an action. Agents: over-permissioned agents. Fix: tool allowlists and approval gates for irreversible actions. Tools and MCP: poisoned or unvetted tool servers. Fix: allowlist, schema-validate, and pin them like dependencies. Infrastructure: poisoned weights and silent exfiltration. Fix: scan models in CI/CD and restrict egress.  Every layer has holes, but stacked together they leave no straight path from attacker to impact.  You'll leave with a 16-question checklist, four per layer, that you can run against your own pipeline this sprint.
