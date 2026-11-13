# Responsibility without control is stress. Tracing narrows the gap

Conf42 Blog, 2020-08-26. https://www.conf42.com/blog/sre2020/service-ownership-tracing-slo-math

In short: Daniel Spoonhower (LightStep) at Conf42 Site Reliability Engineering 2020 on service ownership built on docs, on-call and SLOs, with tracing under each

Microservices and DevOps gave every team control of its own service and left it responsible for a dozen services it can't touch. At Conf42 Site Reliability Engineering 2020, Daniel Spoonhower (Spoons to everyone), CTO and co-founder of LightStep and formerly a software engineer at Google, called that gap the textbook definition of stress, and laid out how service ownership closes it: documentation, on-call and SLOs, each fed by distributed tracing.

## What changed?

The technical stack moved from bare metal to VMs, containers and Kubernetes; applications moved to microservices and serverless; teams adopted agile and DevOps to work independently. He draws it as a feedback loop of control and observation, and argues the control half got far more investment. "It's like we've built this amazing car that goes super fast. We've got a great gas pedal, but we don't have a speedometer," Spoons said at Conf42 Site Reliability Engineering 2020.

The result: a team at the top of the stack answers to users for latency and reliability, but when a service three layers down is slow, it can't roll that back. It can only ask.

## Why tracing, specifically?

A trace is a Gantt chart of one request: time left to right, the stack top to bottom. What matters is that it records the causal relationships between callers and callees, so you know who was responsible for a request at any moment, and where to attribute failures and slowness.

Spoons insists traces are raw material, basically structs; distributed tracing is the art of deriving value from them. His Google example, from the Dapper paper: a weekly MapReduce over a week of web search traces reported what share of latency each service contributed. Teams that ignored it sometimes spent a month on optimisations users never noticed.

## What does ownership mean, and what does it cost?

Teams are responsible for delivering their software: incident response, paying for the infrastructure and storage they use, fixing bugs. In return they move independently. The risks are divergence: more frameworks and tools, higher vendor costs, more training for new hires and internal transfers, and a harder time seeing the whole application. His answer is independence within clear responsibilities and goals, consistent measurement, and two ingredients in every decision: accountability and agency.

## Piece one: documentation people can trust

Start with who the experts are. Use a template, so every service page links to dashboards, logs, traces, alert definitions and playbooks, and so you can run reports over it (who is the expert for too many services?). Track last-modified dates and require audits.

Better still, make it machine-readable and generate dashboard, escalation and deployment pipeline config from it. If the only way into the CI pipeline is through the docs, the docs stay current. And don't ask humans to record what the software knows. At Google, keeping service dependency lists current by hand never worked; LightStep generates dependency diagrams from traces, transitive ones included, annotated with which services contribute to latency.

## Piece two: on-call that doesn't burn people out

On-call is more than incidents: status updates, change management, interrupts, handoffs, postmortems. For pages, his three levers are more actionable alerts, the right team, and fewer pages.

At LightStep, a latency alert carries a link to an example slow trace; in his example, the trace shows sharded work with one shard far slower than the rest. For routing, he credits Luis Mineiro of Zalando (SREcon EMEA 2019): alert on symptoms, then walk the failing trace down through dependencies that also show errors until you reach services whose dependencies are clean, and page those teams.

Traces help postmortems stay blameless too. When two teams argue over whose latency it was, p50 aggregates let each side be right; a trace pairs the slow call with the matching slow response.

## Piece three: SLOs, with the maths done by traces

An SLO is a promise to customers, internal or external, measurable on short timescales. Example: p99 latency under 5 seconds over the last five minutes, which is an indicator, a threshold and a window. Measure over the window, because instantaneous latency shifts with the timescale you look at.

The memorable bit is deriving internal SLOs. If A promises p99 under 5 seconds and a trace shows B dominating A's latency, B inherits roughly the same bound. But B calls C twice in series, so C needs p99 under 2.5 seconds, and since there are two chances to be slow, closer to p99.5 under 2.5 seconds. B also depends on D in general, but not for this request, so the service diagram alone would have set the wrong targets.

## How do you roll this out?

Bottom up. New processes and tools are adopted only when they help application teams, ideally when they're needed to get the job done, so make ownership in the docs a requirement for joining the pipeline. And budget for it: agency needs the right information and the time to act, because "ownership doesn't come for free."

## Who should watch

SRE and platform leads defining ownership for a growing service count, and anyone who has set an internal SLO by gut feel. Related Conf42 talks: [Joey Parsons on service ownership and organisational chaos](https://www.conf42.com/Chaos_Engineering_2021_Joey_Parsons_service_ownership_organizational_chaos), [Michael Haberman on distributed tracing with OpenTelemetry](https://www.conf42.com/JavaScript_2021_Michael_Haberman_distributed_tracing_OpenTelemetry), and [Ricardo Castro on alerting with SLOs and error budget policies](https://www.conf42.com/Site_Reliability_Engineering_2022_Ricardo_Castro_alerting_slos_error_budget_policies).

[Watch Daniel Spoonhower's talk](https://www.conf42.com/Site_Reliability_Engineering_2020_Daniel_Spoons_Spoonhower_service_ownership_distributed_tracing) from [Conf42 Site Reliability Engineering 2020](https://www.conf42.com/sre2020).

## From Lightstep

Spoons described Lightstep as simple observability for deep systems, based on distributed tracing. The talk's examples come from its product: dependency diagrams generated from traces, and alerts annotated with example slow traces.

- Lightstep: [lightstep.com](https://lightstep.com)

[Watch the talk on YouTube](https://youtu.be/azmyU4_7VYI).

## Watch the talk

[Driving Service Ownership with Distributed Tracing](https://www.conf42.com/Site_Reliability_Engineering_2020_Daniel_Spoons_Spoonhower_service_ownership_distributed_tracing) at Conf42 Site Reliability Engineering 2020.
