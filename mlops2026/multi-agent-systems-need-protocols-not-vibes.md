# Multi-agent systems need protocols before they need more agents

Conf42 Blog, 2026-11-09. https://www.conf42.com/mlops2026/multi-agent-systems-need-protocols-not-vibes

In short: Daniel Akhabue (Qucoon) at Conf42 MLOps 2026 on typed messages, retries, dead-letter queues and tracing for agents that talk to agents.

Four agents passing free text to each other is a distributed system with no schema, and it fails like one. At Conf42 MLOps 2026 on November 19, Daniel Akhabue, Senior AI Engineer at Qucoon, treats agent-to-agent communication as protocol engineering: typed messages, validation at every hop, retries, dead-letter queues and traces you can actually follow.

The session is built as a hands-on walkthrough. Instead of a slide of boxes and arrows, you build one: a small distributed system with a research agent that gathers information, an analysis agent that processes it, a synthesis agent that writes the report, and a validation agent that checks quality before anything leaves the building.

## The failure modes are old friends

The abstract lists what goes wrong when agents coordinate without rules: inconsistent outputs, silent failures, race conditions, and systems nobody can debug. If you have run microservices, every item on that list will feel familiar. The difference is that the payload is now produced by a model, so the message that arrives at the next agent may be well-formed English and still be garbage as data.

That is the core argument of the talk. Agents are services. Treat the messages between them with the same discipline you would give to an API contract, and a lot of the "AI is unpredictable" pain turns back into ordinary engineering.

## Pydantic is the contract, validation is the bouncer

Daniel's protocol layer starts with structured messages defined in Pydantic, so every agent interaction is type-checked. On top of that sit validation layers designed to catch errors before they cascade. A malformed handoff from the research agent should die at the door of the analysis agent, with a clear error, instead of travelling three steps downstream and turning into a confident, wrong report.

Concurrency gets its own treatment: when several agents run at once, you need proper synchronisation, or you get the race conditions the abstract warns about. Think of it as the agent version of two cron jobs writing the same file.

## Borrow the whole reliability toolbox

The part that should please SREs is how much of the classic distributed-systems kit makes the cut:

- automatic retry logic on agent calls
- dead-letter queues for messages that keep failing
- circuit breakers for agents that are misbehaving
- event-driven architecture for coordination
- semantic versioning for protocol changes, so a new message shape does not break an older agent
- OpenTelemetry for observable agent workflows

Versioning is the sleeper hit here. Prompts and agents change weekly in most teams, and nobody bumps a version number. Once agents exchange typed messages, a protocol change becomes something you can version, test and roll out like any other API change.

## Testing the non-deterministic bits

The talk also covers testing strategies for non-deterministic systems, which is where most multi-agent projects quietly give up. Combined with typed messages and traces, you get a system where a test can assert on structure and behaviour even when the wording of each output changes run to run.

## Who should watch

Engineers who already have one agent in production and a roadmap that says "add three more". Platform and SRE folks who will be paged when those agents start talking to each other. If you are still deciding whether you need agents at all, this is not the starting point; it assumes you are past that question and want blueprints and debugging tools.

## Related Conf42 talks

- [Engineering Production-Grade Multi-Agent Systems in the Cloud](https://www.conf42.com/Cloud_Native_2026_Sandeep_Mannapur_ai_agents_workflows) by Sandeep Mannapur, a cloud-side view of the same problem.
- [Make Agents Observable: Tracing Decisions, Tool Calls and Recovery](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) by Emerson Braun, for the tracing half of Daniel's toolbox.
- [From Monoliths to Microminds: Building Resilient AI Platforms with Multi-Agentic Architecture](https://www.conf42.com/Platform_Engineering_2025_Sidhanta_Panigrahy_microminds_monoliths_multi) by Sidhanta Panigrahy, on the platform around many agents.

[Watch Daniel Akhabue's talk](https://www.conf42.com/MLOps_2026_Daniel_Akhabue_protocol_agent_multi) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Agent Protocol Engineering: Designing Reliable Multi-Agent Systems](https://www.conf42.com/MLOps_2026_Daniel_Akhabue_protocol_agent_multi) at Conf42 MLOps 2026.
