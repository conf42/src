# When agents code and ship it, on-call needs simulator time

Conf42 Blog, 2026-08-14. https://www.conf42.com/blog/obs2026/on-call-needs-simulator-time-when-agents-code

In short: Ralph Bird of PagerDuty at Conf42 Observability 2026 on owning incidents in AI-written code, the automation paradox and practice for on-call.

PagerDuty's mantra is "code it, ship it, own it". At Conf42 Observability 2026, Ralph Bird, Principal Machine Learning Engineer at PagerDuty, argued that AI is taking over the first two, and that the third has not gone anywhere. His fix borrows from civil aviation: if agents handle the routine incidents, humans need deliberate simulator time so they are not cold when the big one lands.

## 03:47, and the agent has already failed

The talk opens on a night in the near future. The pager fires at 03:47, a SEV 1, revenue bleeding. The difference from today: an SRE agent has already tried. The easy fixes, a restart or a rollback of the last deploy, are gone. You open a code base you have not read in two years, because an agent wrote it, another agent shipped it, and the minor incidents that used to teach you the system were handled overnight without you. The agent cannot fix this. Can you?

Bird is not a doom merchant about it. He expects more code to mean more incidents, and AI-written code to fail in different ways even with guardrails. He also expects agents to handle minor incidents, and thinks that is good: nobody needs a human to restart something at night if the agent can do it and leave a note in the morning. He also rejects both loud predictions, that it will all be agent ops, or that agents write everything and humans absorb the incident wave. Teams will own more services than they wrote, and that changes what ownership means.

## The automation paradox

The core idea is the automation paradox: the more reliable the automation, the rustier and rarer the humans who can handle what it cannot. When agents take the routine work, engineers lose the cheap practice that routine incidents provided, and meet the gnarly ones with less context, less recent practice and higher stakes.

Bird, a former nuclear safety engineer, walks through industries that already faced this. Top Gun exists because naval aviators came to rely on missiles and lost dogfighting skills. Civil aviation responded to autopilot dependence with recurrent simulator time, manual segments and standardised scenarios based on real faults. NASA trains for everything imaginable. Security teams red team their own systems. The lesson he draws for SRE is simple: reactive incident response is not training, so practice has to be routine, scheduled, realistic and aimed at the faults that actually hurt. There is no point drilling Kubernetes failures if you do not run Kubernetes.

## Know how your tools fail

Practice does not remove black swans, and Bird is honest about that, citing the cascading power outage that took out Portugal, where he lives, and Fukushima. His sharpest example is Aeroflot Flight 593, as he tells it: a pilot let his teenage son take the controls, yanking them disengaged the autopilot, and the pilot did not know his tool worked that way. The parallel for SRE agents: learn how they fail, especially when they fail confidently, because following a confident wrong answer is how you walk down the wrong path at 3 a.m.

For tooling, he wants an SRE agent that is both autopilot (take the routine, well-understood work) and co-pilot (assist on complex incidents while the human stays in command), plus incident history used to guide training. Replacement is not the goal.

## What to do tomorrow morning

The advice is concrete. Use agents to read, not just write: pick an unfamiliar code base in your organisation and have the agent help you understand it. Rehearse in low-stakes settings, with game days, drills, failure Fridays and chaos experiments, and bring the SRE agent into those drills so you learn its failure modes. Prioritise scenarios that scare you: the EC2 instance that dies, the read replica that fails, the Kafka queue that stops. Learn from near misses, not only the bad incidents. And treat ownership of the services you inherited as a conscious choice, using the time agents save to learn them.

## Who should watch

On-call engineers and engineering managers whose teams are adopting coding or SRE agents, and anyone building incident tooling. There is no product demo; it is a culture and practice talk from someone who builds incident response tooling. If you already run game days, watch it for the argument you need to keep funding them.

[Watch Ralph Bird's talk](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse) ([YouTube](https://youtu.be/EEnSxa4_vzo)).

## Related Conf42 talks

- [Human-Governed Automation Loops for Reliable AI at Planet Scale](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Suganya_Nagarajan_human_governed_automation) by Suganya Nagarajan (Amazon), SRE 2026.
- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi (Walmart), SRE 2026.
- [Don't Panic! Effective Incident Response](https://www.conf42.com/DevOps_2025_Daniel_Afonso_incident_response_effective) by Daniel Afonso (PagerDuty), DevOps 2025.

## Watch the talk

[AI Coded It, AI Shipped It, Who Owns It?](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse) at Conf42 Observability 2026.
