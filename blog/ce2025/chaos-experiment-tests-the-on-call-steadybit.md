# A chaos experiment that tests your on-call, not just your pods

Conf42 Blog, 2025-02-20, updated 2026-11-09. https://www.conf42.com/blog/ce2025/chaos-experiment-tests-the-on-call-steadybit

In short: Benjamin Wilms of Steadybit at Conf42 Chaos Engineering 2025 on testing socio-technical resilience, from pod redundancy to Datadog and PagerDuty response.

Your redundancy works on paper and your runbook exists in Confluence; neither tells you whether the on-call engineer gets paged within 90 seconds when the gateway falls over. At Conf42 Chaos Engineering 2025, Benjamin Wilms, co-founder and CEO of Steadybit, argued that a system includes the people and processes around the software, and showed a chaos experiment that verifies both halves at once.

Benjamin has been doing chaos engineering for around nine years. This is a vendor talk: the demos run in Steadybit, wired to Datadog and PagerDuty. The method transfers to other tooling, though, and that is the reason to watch.

## A system is more than its services

The talk starts from a definition. Software runs on infrastructure, is built through a pipeline, and is operated by people inside an organisation with its own processes. Benjamin uses the term socio-technical system for the whole thing. Failures can come from any part of it: a misconfiguration, a human error, an unexpected interaction between services, or two teams with mismatched processes.

He is blunt about the goal. A 100% error-free system will never exist; servers crash, networks lag, dependencies break. What you can do is make the system better at handling failure, and check that it really is.

The demo system is an online shop, with services like a bestseller list, checkout, and a hot deals service, each owned by different teams. Even grouped by area, the dependency bubble chart stays busy, which is his point about complexity.

## Find the risk before you run anything

Steadybit's approach has three phases: uncover risk, understand impact, then increase systemic resilience.

The first phase needs no experiment at all. Benjamin groups the shop's Kubernetes deployments and colours them by availability zone. The cluster spans two zones, the bestseller and checkout services are spread across both, and the hot deals service is not. That is a risk found purely from configuration data. Steadybit's advice feature then flags orange items, such as a checkout deployment that should run more instances, with a snippet to fix it.

The second phase verifies the fix. The experiment does a pre-check that all pods are ready, deletes a pod, and expects it back within 60 seconds while the system keeps serving. Steadybit collects Kubernetes events and deployment readiness into one report. Benjamin stresses running these early, in a pre-production environment, rather than starting in production.

## The experiment that pages a human

The third phase is where the talk earns its title. Benjamin takes a scenario from a past incident: a latency spike in the hot deals backend, followed by a total outage of the central gateway. The hypothesis covers people as well as software:

- Monitoring recognises the problem within 90 seconds and alerts the on-call team via PagerDuty.
- The incident is opened and acknowledged within three minutes.
- The system recovers within three minutes and the incident is resolved within four.

The experiment encodes all of it. Steadybit checks with Datadog that the system is healthy first, injects the latency and the gateway outage, then expects Datadog to report an alert, PagerDuty to show a triggered incident, someone to acknowledge it, Datadog to return to OK, and the incident to be resolved. In the recorded run, every step passed, so the technical recovery and the human response both held up.

He adds a rule worth repeating to any team that runs game days: this is not about how fast one person fixes an outage. Benjamin says he does not like finger pointing; the test measures how well the organisation detects and fixes faults and how its processes are coordinated.

## Who should watch

SREs and platform teams who already run basic fault injection and want to extend it to alerting and incident response. The "colour by zone" trick is a nice five-minute audit for any Kubernetes cluster. If you have never run a chaos experiment, the talk is accessible, but you will get more from it once you have.

Related Conf42 talks:

- [Gunnar Grosch on hypothesis-driven resilience modelling](https://www.conf42.com/Chaos_Engineering_2024_Gunnar_Grosch_hypothesis_development_resilience_modeling) at Conf42 Chaos Engineering 2024.
- [Robert Ross on the incident response process](https://www.conf42.com/Chaos_Engineering_2021_Robert_Ross_incident_response_process) at Conf42 Chaos Engineering 2021.
- [Uma Mukkara on continuous resilience](https://www.conf42.com/Chaos_Engineering_2023_Uma_Mukkara_continuous_resilience) at Conf42 Chaos Engineering 2023.

[Watch Benjamin Wilms's talk](https://www.conf42.com/Chaos_Engineering_2025_Benjamin_Wilms_reliable_system_unpredictable) from [Conf42 Chaos Engineering 2025](https://www.conf42.com/ce2025).

## From Steadybit

Steadybit is a chaos engineering platform for running controlled experiments on Kubernetes and cloud systems, with integrations into monitoring and incident tools such as Datadog and PagerDuty, as shown in the talk.

- [Steadybit website](https://steadybit.com/)

[Watch the talk on YouTube](https://youtu.be/I4ONmOzUMD4).

## Watch the talk

[How to Build a Reliable System Under Unpredictable Conditions](https://www.conf42.com/Chaos_Engineering_2025_Benjamin_Wilms_reliable_system_unpredictable) at Conf42 Chaos Engineering 2025.
