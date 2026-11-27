# What a 47-step mortgage teaches about agentic platforms

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/agentic-ai-mortgage-processing-lessons

In short: Naganarendar Chitturi of Newrez at Conf42 Platform Engineering 2025 on orchestration, events and audit trails for agentic AI in mortgage processing.

A typical mortgage, by Naganarendar Chitturi's count, runs through 47 separate steps, each needing judgement and all tangled in dependencies. At Conf42 Platform Engineering 2025, the Senior Solutions Architect at Newrez used that workflow to explain how to build agentic AI platforms that coordinate those steps, and spent as much time on how they break as on how they work. His first lesson: "Orchestration is everything."

## Agents that handle the case nobody wrote a rule for

His definition of agentic AI is practical. A rule-based system that meets an unfamiliar case, say an applicant whose income comes from cryptocurrency mining, stops and waits for a human. An agent recognises it as an income verification problem, looks for guidance and similar past cases, builds a verification path, and records it so the next one is automatic. His other example: an employer switches payroll providers, the new data format breaks the old process, and dozens of applications from that employer pile up for weeks while someone phones vendors. An agent that recognises and shares the new format clears the whole queue.

## Three foundations

He argues you need all three of these or the platform falls apart:

- **Workflow orchestration.** Teams start with a simple queue where agent A hands off to agent B. Then a property in a flood zone during hurricane season needs inspection, flood insurance and evacuation route checks at once, on different timelines, and the queue locks up. His analogy: the gap between a traffic light and air traffic control.
- **Event-driven communication.** A credit agent broadcasts a credit-score-updated event; risk, pricing and compliance agents react in parallel without knowing about each other. When a property valuation service dies at 2am on a Saturday, requests queue and drain when it returns, instead of becoming Monday's crisis.
- **ML pipeline integration.** Real-time inference inside the process, such as fraud models whose confidence drops trigger extra verification.

Event design is the craft. He estimates a mortgage system may carry 4,000 to over 5,000 event types, and each needs just enough context: an income-verification-completed event carries the verified amount, confidence, method and anomalies, but not the raw bank statements. A bonus: the event stream doubles as a flight recorder you can replay.

## Where it breaks

The reality check is the best section. Legacy integration: loan data on a 1980s mainframe with no APIs and a daily batch file, so you end up building a translation agent that speaks mainframe, which may become your most sophisticated component. State management: applications live 60 days or more, rate locks longer, while values, rates and rules shift, which pushes you toward event sourcing so any agent can rebuild state by replay. Variable load: credit analysis takes 30 seconds for a standard W-2 employee and 20 minutes for a self-employed applicant with stock, crypto and foreign assets, so capacity has to adapt automatically.

## Explainable by design

In a regulated industry, saying the AI did it does not work. He describes decision provenance: when a regulator asks about a loan denial from eight months ago, you pull up the agents involved, the data they used, the rules that fired and the exact model versions in seconds. Data minimisation helps too: the credit agent sees aggregated spending patterns, not full statements; the identity agent discards biometrics after use.

Operationally, he suggests monitoring agents like consultants, not servers: track confidence patterns and the decision reversal rate, meaning how often human underwriters overrule an agent. Long-running applications need versioned agent deployments, where in-flight applications keep their agent version, and configuration pulled at runtime. And turn your most experienced underwriters into agent trainers, not competitors.

## Who should watch

Architects designing multi-agent systems for any long-running, regulated workflow, whether loans, claims or patient care. Expect architecture and failure modes, not framework code.

## Related Conf42 talks

- [Jimmy Caputo on agentic engineering platforms](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) at Conf42 Platform Engineering 2026.
- [Naveen Gowda on automating financial workflows in multi-cloud ecosystems](https://www.conf42.com/Chaos_Engineering_2025_Naveen_Gowda_financial_automation_ecosystems) at Conf42 Chaos Engineering 2025.

[Watch Naganarendar Chitturi's talk](https://www.conf42.com/Platform_Engineering_2025_Naganarendar_Chitturi_mortgage_autonomous_lessons), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/UPhNv3VlkGI).

## Watch the talk

[Building Agentic AI Platforms: Lessons from Autonomous Mortgage Processing at Scale](https://www.conf42.com/Platform_Engineering_2025_Naganarendar_Chitturi_mortgage_autonomous_lessons) at Conf42 Platform Engineering 2025.
