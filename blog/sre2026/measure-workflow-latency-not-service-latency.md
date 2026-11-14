# Green dashboards, slow humans - measure workflow latency instead

Conf42 Blog, 2026-03-12, updated 2026-11-09. https://www.conf42.com/blog/sre2026/measure-workflow-latency-not-service-latency

In short: Abhimanyu Narwal of Bloomberg at Conf42 SRE 2026 on silent telemetry gaps, workflow SLIs, count invariants and canaries that prove a pipeline is working.

The edge gateway said 100,000 events arrived; the analysis engine showed 90,000; every service was green. At Conf42 Site Reliability Engineering 2026, Abhimanyu Narwal, Engineering Team Lead for security services at Bloomberg, used that gap to argue that the expensive reliability failures are often not outages but the quiet ones that slow humans down, and he left a short checklist for catching them.

He is clear about scope up front: an anonymised case study and a reusable SRE pattern, not a breach story and not a description of Bloomberg's proprietary architecture.

## The fog of war is ambiguity, not panic

The pipeline is a familiar shape: events enter, get processed, results surface in a UI, a human analyst validates them and acts. For a long time it looked perfect. Then an analyst raised a low-severity alert because counts diverged between stages.

Nothing had crashed. The question was whether the gap was expected transformation lag or a visibility hole, and in a security workflow that uncertainty is costly. Management kept asking whether threats were being missed. After a lot of digging the answer was reassuring and annoying in equal measure: processing and safety checks had worked fine, but a telemetry agent had silently failed and dropped logs before they reached the UI. Compute health was 100%. The team's confidence was not.

## The four golden signals answered the wrong question

Latency, traffic, errors and saturation were all fine. They answer whether the system is alive, and miss whether the workflow is explainable. His key distinction: service latency is milliseconds between request and response; workflow latency is the time for a human to go from seeing a signal to confidently acting on it. When telemetry drops, the second one explodes while the first stays flat.

So the team stopped treating this as a logging bug and started treating the whole human workflow like a distributed trace, human validation step included.

## Three SLIs worth stealing

- **End-to-end duration**: p50 and p95 from ingestion to visible in the UI, alerting when it is consistently worse than the workflow needs. That catches slow degradation behind healthy services.
- **Count integrity**: compare counts between stages against an explicit model of expected deltas and lag. His example: 2% divergence for five minutes is normal; 10% for an hour means the invariant is broken.
- **Liveness via canary**: a known-good synthetic event injected continuously and verified at every stage. If you take one thing from the talk, he says, take this.

## Systems should confess their own blind spots

On the design side he proposes what he calls a fifth golden signal for the system to reveal its own coverage gaps. When telemetry is missing, the UI should say so. Treat partial degradation as a first-class state instead of a binary up or down, so reduced coverage shows as reduced coverage rather than a reassuringly normal screen. And make invariants (everything received is eventually surfaced within a known window) observable contracts.

His last tactic is the most human one: if people are a reliability endpoint, measure their friction. Repeated queries, pivots, escalations and reopen rates are proxies. Before the fix, tier-one analysts did not trust the UI and escalated to engineering for manual database queries; that escalation loop was, in his words, the true error rate.

## Who should watch

SREs and observability folks supporting any human-in-the-loop pipeline: security operations, fraud review, moderation, support tooling. The checklist is deliberately small: pick one key workflow, define its invariants, add one synthetic canary, write one workflow SLO. A cheap Monday morning, and you get to stop guessing.

## Related Conf42 talks

- [The Fifth Golden Signal: Making Accessibility Observable](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) by Victoria Nduka, a different argument for extending the golden four.
- [Observability Starts Before the Outage: Synthetic Monitoring for Modern Systems](https://www.conf42.com/Observability_2025_Palak_Bhawsar_synthetic_monitoring_outage) by Palak Bhawsar.
- [Clinical troubleshooting: diagnose production issues with scientific precision](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Dan_Slimmon_clinical_troubleshooting_diagnose) by Dan Slimmon, for working through the fog once you are in it.

[Watch Abhimanyu Narwal's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/Tog5I_8nPFg).

## Watch the talk

[The Failures You Don’t See on Dashboards - A reliability case study in workflow latency and response time](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) at Conf42 Site Reliability Engineering (SRE) 2026.
