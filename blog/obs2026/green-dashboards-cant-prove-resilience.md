# Green dashboards only show the paths you have already tested

Conf42 Blog, 2026-09-10. https://www.conf42.com/blog/obs2026/green-dashboards-cant-prove-resilience

In short: Uma Mukkara of Harness at Conf42 Observability 2026 on why green dashboards can't prove resilience, and a four-step loop to test the untested paths.

Your dashboards can only show the paths your system has actually walked. At Conf42 Observability 2026, [Uma Mukkara](https://www.conf42.com/Observability_2026_Uma_Mukkara_resilience_testing_enterprise), who leads resilience testing at Harness and co-founded LitmusChaos and OpenEBS, argued that the fallback route, the retry path and the DR plan are exactly the ones nobody instrumented, and that the only way to see them is to break things on purpose first.

The keynote is short and practical. It is also a Harness talk: the last section demos Harness Resilience Testing. The first two thirds stand on their own as an argument for any observability team.

## The gap is widening, and he names three accelerants

The premise: the observability system says green, and incidents keep happening anyway. Not one or two, but a steady stream in large organisations. Mukkara blames three accelerants. Systems keep getting more distributed and dynamic, with more dependencies. Releases happen all the time, and AI-assisted coding has pushed some teams to tens of releases a day. And agents are now in the loop, which brings a failure shape of its own.

Observability, in his framing, tells you what is happening. It does not tell you what would happen.

## Four things a dashboard never shows

He lists the blind spots plainly:

- **Single points of failure.** A dashboard shows what is instrumented and exercised. An untested dependency stays invisible until it goes.
- **Timeouts and retries that trigger new paths.** The code has been green for months because that branch never ran.
- **Degraded mode.** If the system has never been degraded, nobody knows what degraded looks like on screen.
- **Recovery.** If you never ran a DR test, you have no idea what your dashboards will say during one.

The uncomfortable part is timing. These are precisely the dashboards you need when a single point of failure trips, timeouts pile up and the system drops into degraded mode or DR.

## A retry storm in a path that never carried traffic

His case study is the pattern most on-call engineers will recognise. Everything is green. A third-party API stops responding, and the system fails over to a redundant path that has never carried traffic, so nobody instrumented it. Retries on the new path turn a partial outage into a full one within the next thirty minutes to an hour, and when the full outage lands, the team is debugging blind because nothing captured that hour.

The fix he prescribes is boring in the best way: find that failover path ahead of time, exercise it in a lower environment, and build the dashboards for it before production needs them.

## Agents can report healthy while doing the wrong thing

The new failure shape is the AI agent. A health check can return 200 OK while the model behind it is slow but not down, and Mukkara's point is that a slow model is as bad as a broken one. A tool call can time out silently while the agent keeps answering 200. His suggestion: inject latency between the model endpoint and the agent and check whether your observability reports the agent's real health, or just its HTTP status.

## The four-step loop

The method fits on an index card:

1. Inventory tested versus untested paths. For every "what happens if this network fails", ask whether you have seen it or assumed it.
2. Run controlled experiments with a small blast radius against the untested ones.
3. Add the missing dashboards and metrics the experiments reveal.
4. Repeat it, quarterly or more often.

For a next step he suggests starting with your most critical service, listing every assumption never observed in production, and putting your agentic systems into degraded mode to see if the dashboards tell the truth.

## What the demo shows

The closing demo covers Harness Resilience Testing, which runs chaos experiments, load tests and DR tests from one place. AI-assisted risk scanners read deployment metadata, logs, configuration and runtime events to flag likely risks before you run anything, and a resilience testing agent recommends and creates the experiments to confirm them.

## Who should watch

SREs and observability owners who have ever had to explain a green dashboard in a postmortem. Platform teams adding AI agents to production will get the most from the agent section, which is short but specific.

## Related Conf42 talks

- [Boosting System Resilience with Exponential Backoff in Distributed Computing](https://www.conf42.com/Rustlang_2024_Suraj_Modi_system_resilience_backoff_computing) by Suraj Modi (Uber), the antidote to the retry storm in Mukkara's case study.
- [When Clusters Collide: The Misadventures of Disaster Recovery in Kubernetes](https://www.conf42.com/Platform_Engineering_2024_Lev_Andelman_clusters_disaster_kubernetes) by Lev Andelman (TeraSky), on what happens when the DR plan meets reality.
- [Enhancing Hypothesis Development Through Resilience Modeling](https://www.conf42.com/Chaos_Engineering_2024_Gunnar_Grosch_hypothesis_development_resilience_modeling) by Gunnar Grosch (AWS), on choosing which experiments to run first.

[Watch Uma Mukkara's keynote](https://www.conf42.com/Observability_2026_Uma_Mukkara_resilience_testing_enterprise) or the [YouTube recording](https://youtu.be/OORwIuqgKV8).

## From Harness

Harness was the Diamond sponsor of Conf42 Observability 2026. The product shown in the talk is Harness Resilience Testing, part of the Harness platform, covering chaos experiments, load tests and DR tests.

- [Harness](https://www.harness.io/): the platform and its Resilience Testing module
- [All Conf42 Observability 2026 talks](https://www.conf42.com/obs2026)

## Watch the talk

[Green Dashboards, Broken Systems: Why Observability Alone Can't Prove Resilience](https://www.conf42.com/Observability_2026_Uma_Mukkara_resilience_testing_enterprise) at Conf42 Observability 2026.
