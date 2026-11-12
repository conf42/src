# We let AI agents touch production. Here is what the platform had to give them

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Jose Escrich](https://www.conf42.com/speaker_Jose_Escrich) (CEO @ WHAWIT). Page: https://www.conf42.com/Chaos_Engineering_2026_Jose_Escrich_agents_production_platform

## Abstract

José Escrich's team spent two years building agents that investigate and fix production incidents, then ran them on real on-call rotations at three companies. Most of what broke was not the model; it was the platform. This is the field report.  Key takeaways: - The four primitives an agent needs before it can act safely: read-only telemetry, a registry of signed actions, an approval gate that fits in a page, and a place to write back what it learned. - Why "human in the loop" as the only step kills adoption, and how approval as the last step changed engineer behaviour. - What the Opsgenie sunset forces platform teams to decide in 2027, and how to redesign on-call instead of just migrating it. - The failure modes nobody warned about: privilege creep, cost blow-ups, confidently wrong agents.
