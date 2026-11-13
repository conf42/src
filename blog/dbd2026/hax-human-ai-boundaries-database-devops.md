# AI fixed the migration speed problem, and exposed the trust problem

Conf42 Blog, 2026-05-23, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/hax-human-ai-boundaries-database-devops

In short: Muthu Saravanan (Mind-Pros) at Conf42 Database DevOps 2026 on HAX, a framework for deciding what humans own and what AI does in database delivery.

Muthu Saravanan's story starts with a win. A database team's pipeline was too slow for migrations, they brought in an AI tool, and suddenly migrations, schemas and queries came out faster than ever. At Conf42 Database DevOps 2026, the Director of Experience Design at Mind-Pros explains what that win uncovered: the bottleneck moved from "can we build it?" to "should we build it this way?", and fast output isn't the same thing as trustworthy output.

His answer is HAX (Human and AI Experience), a framework he conceptualised and holds the trademark for. It's a process talk rather than a tooling one: no specific product, no benchmarks, and a clear map of who decides what.

## Experience debt accumulates where nobody looks

Muthu names the new problem experience debt: like technical debt, but more dangerous with AI because it builds up invisibly. A bad schema decision can survive for years; a poorly reviewed migration can cascade into other production systems. He lists three symptoms:

- **Inconsistency creep.** Every engineer prompts differently, assumes differently and validates differently, until the team shares no common engineering language.
- **Amplified data risk.** Generated SQL can be syntactically fine and still bring security holes, index regressions, locking issues or integrity failures.
- **Erosion of trust.** When engineers stop understanding why the AI produced something, they swing to blind trust or total rejection. Both end in failures.

## Humans decide, AI elevates

HAX splits responsibility into two layers. HX covers what stays human because the consequences are long-lived: system architecture (an AI can suggest scaling patterns but knows nothing about acquisition plans or org politics), data modelling (a schema encodes business meaning, and a naming mistake today is a reporting problem for years), governance (classification, access, audit accountability) and critical reasoning during incidents, where people weigh team history, risk tolerance and customer impact.

AX covers where AI adds the most value, in six facets: detect (anomalies, drift), predict (migration risk, capacity growth), scale (index recommendations, connection pooling, pipeline orchestration), synthesize (turning telemetry, logs and change history into usable knowledge), execute (deployments and migrations inside human-set boundaries) and ethics (transparency as part of reliability).

## Accountability first, acceleration second

The delivery method runs six stages across discovery, design and development, and it reverses the usual order where teams adopt tools first and govern later. Discovery is the most human part: interviews, system inventories, risk assessments, with AI summarising raw material. In design, engineers own schemas and architecture while AI runs validation checks, suggests index strategies and scaffolds pipelines; nothing moves without human approval. Muthu's framing is to treat the AI as a junior engineer who does the research but doesn't make the final call. In development the roles flip: AI drives migration execution, schema versioning and deployment automation, and engineers monitor with override authority at each step. Telemetry flows back so the process keeps correcting itself.

The point of the explicit boundaries is ownership. If everyone assumes the AI is responsible, nobody owns the outcome.

## The unglamorous part: shared artifacts

The section most teams can act on tomorrow is knowledge artifacts. Without standard prompt libraries, runbooks and tool-specific interaction patterns (he names ChatGPT and Gemini), every engineer invents their own prompting style and validation logic, which is inconsistency creep by another route. His closing advice follows from that: start where you are, because a shared prompt library and a validation checklist get you further than you'd expect.

## Who should watch

Engineering leads whose teams adopted AI assistants for database work bottom-up and now have five different ways of generating migrations. Engineers looking for implementation detail will find the talk high-level; its value is the vocabulary for an ownership conversation.

## Related Conf42 talks

- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis, trust boundaries from the architecture side.
- [From Acceleration to Assurance: Governing AI Code Assistants in SOX and ICFR Audit Analytics](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants) by Karishma Velisetty, governance for AI assistants under audit.
- [Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou, where the human gate goes in agent workflows.

[Watch Muthu Saravanan's talk](https://www.conf42.com/Database_DevOps_2026_Muthu_Saravanan_alerts_telemetry_platform)

[Watch the talk on YouTube](https://youtu.be/4w9uV6vhQzQ).

## Watch the talk

[Intentional Delivery in AI-Driven Database DevOps](https://www.conf42.com/Database_DevOps_2026_Muthu_Saravanan_alerts_telemetry_platform) at Conf42 Database DevOps 2026.
