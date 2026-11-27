# ML pilots stall on organisational readiness, not on the models

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/ml-pilots-fail-on-readiness-not-models

In short: Kiran Ramanna (ServiceNow) at Conf42 Machine Learning 2026 on a five-pillar readiness blueprint with stage gates to move ML pilots into production.

Most enterprise ML pilots never become products, and the model is rarely the reason. At Conf42 Machine Learning 2026, Kiran Ramanna, Senior Staff AI Engineer at ServiceNow, laid out an AI Readiness Blueprint: five pillars, five maturity stages and stage gates that stop a team from scaling something the organisation can't yet carry.

It's a framework talk, not a code talk. If you have ever watched three departments run three chatbots against three copies of the same customer table, it will feel uncomfortably familiar.

## Pilot sprawl is a symptom with three causes

Ramanna opens with the industry failure numbers from the slides (a large majority of AI projects failing to deliver value, and most pilots never reaching production) and then pins the failure on organisational preparedness rather than technology. The talk names three root causes: fragmented data, unclear ownership and inconsistent governance.

Those show up as four patterns seen across organisations. Siloed data that leaves models with an incomplete picture. Cross-functional teams with conflicting expectations and nobody clearly accountable. Governance that can't keep pace with deployment ambitions. And pilot sprawl: disconnected experiments multiplying without architectural coherence, which leaves technical debt and a slow erosion of confidence in AI as a whole.

The contrast drawn is simple. A pilot programme has siloed data, ad hoc processes and no path to production. A production-ready organisation has a unified data platform, standardised processes and ML work that is aligned with the business.

## Five pillars, and they lean on each other

The blueprint rests on data preparedness (completeness, accuracy, lineage, accessibility), process adaptability, infrastructure scalability, governance and ethics, and cultural enablement. Governance is drawn as a concern that spans all five rather than a box at the end.

The useful bit is the dependency map. Quality data enables process automation. Infrastructure is what stores and processes that data. Culture underpins adoption of everything else. Put plainly: you can't automate without quality data and you can't scale without infrastructure, so a roadmap that funds a model before the lineage work is a roadmap that will be rewritten.

On process selection the talk gives a crisp test for what to automate first: decision points that are repetitive, outcomes that are measurable, and inputs and outputs that are traceable. That is a short list worth stealing for your next prioritisation meeting.

## Stage gates make "not yet" a normal answer

Organisations move through five maturity stages, from foundational (ad hoc experiments, isolated teams) to optimized (continuous innovation and organisational learning). Between phases of the roadmap (discovery, foundation build, pilot, scale) sit governance checkpoints that check people readiness, process transformation, deployed infrastructure, data quality standards and enforced policies.

The part that makes this humane is the recovery path. Missing a gate leads to targeted capability building, extended timelines with milestones, external partners or a parallel track. The talk is explicit that a failed gate is about building capability before you scale, not a verdict on the team.

## Assessment as a workshop, not an audit

The other move is turning the readiness assessment into collaborative discovery workshops with business sponsors, enterprise architects, engineering leads and data owners in one room. The outputs are concrete: a maturity scorecard, a prioritised gap list, gate criteria and a 90-day action plan (or a monthly or biweekly one, if your organisation moves at that cadence).

Ramanna closes the loop with public case studies mapped onto the pillars and stages, including JPMorgan Chase, Siemens Amberg, Unilever and Mayo Clinic, noting the figures come from published sources.

## Who should watch

Engineering managers, platform leads and staff engineers who keep getting asked to "productionise" a demo that has no owner, no lineage and no governance sign-off. It is also a good share for the business sponsor who keeps funding pilot number seven. If you want Spark tuning or model internals, this one is not for you.

## Related Conf42 talks

- [AI Demos Are Easy. Enterprise AI Is Not](https://www.conf42.com/AI_Agents_2026_Shubham_Jindal_ai_demo_enterprise) by Shubham Jindal (Harness) takes the same gap and looks at it through agents.
- [A Unified Readiness Framework for Mission-Critical AI Agents and Autonomous Platforms](https://www.conf42.com/AI_Agents_2026_Shubham_Sharma_readiness_platform_enterprise) by Shubham Sharma (Microsoft) is another readiness framework to compare against.
- [From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/MLOps_2025_Samuel_Baruffi_poc_bedrock_agentcore) by Samuel Baruffi (AWS) is the hands-on counterpart.

[Watch Kiran Ramanna's talk](https://www.conf42.com/Machine_Learning_2026_Kiran_Ramanna_retraining_lifecycle_models)

[Watch the talk on YouTube](https://youtu.be/XOd4qr4TwHo).

## Watch the talk

[From ML Pilots to Production: An AI Readiness Blueprint for Enterprises](https://www.conf42.com/Machine_Learning_2026_Kiran_Ramanna_retraining_lifecycle_models) at Conf42 Machine Learning 2026.
