# Reliability lives in what changed, not in what broke

Conf42 Blog, 2026-01-18. https://www.conf42.com/blog/devops2026/ai-sre-asks-what-changed-not-what-broke

In short: Spiros Economakis, founder of NOFire AI, at Conf42 DevOps 2026 on using AI to give production a memory and move SRE from firefighting to foresight.

Every incident investigation starts from zero because context doesn't survive change. That is the problem [Spiros Economakis](https://www.conf42.com/DevOps_2026_Spiros_Economakis_sre_experience_ai), Founder and CEO of NOFire AI, put at the centre of his Conf42 DevOps 2026 talk. His answer is to stop asking "what broke?" and start asking what changed, where it landed and what it affected, with AI keeping a persistent memory of production so the question can be answered before customers notice.

Economakis spent over a decade on call for production systems, and the talk is a conceptual one: diagrams and arguments, no product demo. It's worth knowing that he builds a company in this space, so the vision lines up with what NOFire AI works on, though the talk never turns into a pitch.

## Systems now change faster than anyone can model them

The opening is a recognition, not a critique. Most engineering work happens in exceptions, edge cases and half-known systems. AI-generated code and vibe coding mean teams ship faster than ever, so production changes faster than humans can build a stable mental model. AI didn't create the problem, he says; it accelerated it.

His picture of production is three layers: services and infrastructure at the bottom, workflows such as releases, incidents, security and cost in the middle, and teams on top, each owning a slice and nobody seeing the whole. Every incident cuts across those boundaries, every handoff loses context, and the pain lives in the gaps. Customers feel the result: they report problems before monitoring does, and a few engineers who carry the full model of production become single points of failure until they burn out or leave.

## Three traps we already fell into

He names the fixes we've all tried. The visibility trap: more dashboards, metrics and alerts, which add mental load without structure. The correlation trap: smarter-looking pattern matching that helps you react but doesn't tell you why it happened this time. The tooling trap: a new tool or process for every new problem, each solving a slice while adding handoffs and ownership gaps. His summary is that the system became operable but not understandable. If your incident channel has more bots than humans, you know the feeling.

## From raw signals to a memory of change

What's different now, he argues, is that systems can hold meaning rather than emit fragments. Instead of reconstructing understanding after the fact from logs, traces, commits and deploys, AI can keep it close to production: a continuous view of what changed (code, config, dependencies, infrastructure, traffic), where it landed and how behaviour shifted. Every incident adds to that understanding instead of wiping the slate.

That moves reliability earlier. A deployment analysis can run on every PR, using the service's own history: how often it changes, what tends to go wrong after those changes, what is already unstable. Spotting risky changes in the IDE, finding the real cause during an incident, and feeding every outcome back becomes one loop rather than a deploy, an incident, a postmortem and some forgotten tickets.

## Customer experience is the downstream metric

The customer case follows: fewer surprises because risky changes are caught early, faster recovery because engineers act with full context, and more predictable releases. The engineer's job shifts too, from whack-a-mole with alerts to deciding when to ship, when to wait and how to manage risk before users feel it.

He closes on a strong claim. SRE has been optimised for speed (faster detection, faster response, faster RCA), but speed alone doesn't reduce risk; understanding does. He also predicts the talk itself will look different in a year, which is refreshingly honest for a talk about AI.

## Who should watch

SRE leads and engineering managers thinking about where AI belongs in reliability work beyond chatbot-assisted RCA. If you want implementation detail, this is the wrong talk. If you want a clear argument for change-centric reliability, it's a good one.

## Related Conf42 talks

- [When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) by David McNerney and Daniel Raskin at Conf42 Site Reliability Engineering 2026.
- [Feature Flags as Incident Evidence: Safer AI-Assisted RCA Workflows](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) by Ishan Shah at Conf42 Feature Flags 2026.
- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi at Conf42 Site Reliability Engineering 2026.

[Watch Spiros Economakis's talk](https://www.conf42.com/DevOps_2026_Spiros_Economakis_sre_experience_ai) or the [YouTube recording](https://youtu.be/bXyvcbcW7WY).

## Watch the talk

[How AI is redefining SRE and Customer Experience](https://www.conf42.com/DevOps_2026_Spiros_Economakis_sre_experience_ai) at Conf42 DevOps 2026.
