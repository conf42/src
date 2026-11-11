# Put AI inside the release loop, not on a dashboard after the fact

Conf42 Blog, 2026-10-05, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/ai-belongs-in-sdlc-not-dashboard

In short: Amazon's Naveen Goel at Conf42 Feature Flags 2026 on per-PR efficiency checks, gated release waves and bounded AI authority to catch quiet regressions.

A deploy that quietly adds 20% to compute doesn't page anyone; it shows up weeks later on the cloud bill. At Conf42 Feature Flags 2026, Naveen Goel, Senior Program Manager at Amazon with more than two decades in IT delivery, argued that AI belongs inside the software delivery lifecycle as an operator that observes, detects, acts and revalidates, rather than as one more dashboard a human checks after the damage is done. He stresses the views are personal and the worked example isn't tied to any specific company.

## When a slow API is an unlocked front door

The example is a connected-device business, think smart doorbells and cameras, serving around 200,000 requests per second on roughly 10,000 servers. What shows up as a small uptick on a backend dashboard can mean a customer's front door camera isn't working. So Naveen wants reliability defined by the customer promise, not only by CPU, memory and cost graphs.

Traffic is seasonal and time-of-day shaped too. A doorbell sees fewer motion events while people sleep, so capacity needs move through the day.

## Every PR has an efficiency cost

His sharpest point is about money. Long-term capacity is usually reserved, but spikes run on on-demand cloud capacity, which is the expensive kind. If a release raises compute by 15-20% and nobody notices, the bill arrives monthly or quarterly, long after anyone could cheaply fix it. API performance, as he puts it, now hits the P&L directly.

So each change should be judged on efficiency as well as correctness: CPU, memory, IO and latency profiles per PR, with a stated tolerance (5%, 10%, whatever the service can bear, at whichever percentile matters), and predefined actions when a release breaches it. The talk's abstract fills in the pipeline he has in mind: performance-aware code review, payload replay and resource-signature profiling in CI, and anomaly detection that ties a code or payload change to a CPU, memory or IO spike.

## Waves with exit criteria, and agents with job descriptions

The blast-radius advice is the progressive-delivery core of the talk. Release in four or five waves: internal users first (dogfooding), then 1% of customers, then 10%, then everyone, with explicit exit criteria for each gate and a risk and issue register where every item has an owner, whether a person, a team or eventually an AI agent. The abstract describes the same idea as phased canary, cell and region deployment.

Detection should learn normal baselines rather than rely on hard-coded thresholds, then correlate a deviation with the release that caused it. That's what catches the quiet regressions that cost data centre efficiency without ever looking like an outage. He's against the one-agent-does-everything model: one agent detects and escalates, another fixes and revalidates, and the loop continues until the issue is closed. With a hundred-plus microservices and thirty or forty on-call teams, getting the first triage right is half the battle, and that's where he sees faster MTTD and MTTR coming from.

## Bounded authority, not blind trust

The closing takeaway is about how much rope to give. Define what the AI may do on its own before any human is paged: if compute jumps 20% after a release, at least pause the rollout and notify people in parallel to stop the bleeding. Beyond that, it escalates, or fixes only where humans have granted it that authority. The abstract adds the guardrails that make this tolerable: contained blast radius, reversible actions, logged and reviewable decisions, and humans kept in the loop for high-stakes calls.

## Who should watch

Engineering and delivery leaders weighing how far to let automation act during releases, and anyone who has found a performance regression in a monthly invoice. It's a strategy-level talk rather than a technical walkthrough, so the value is in the operating model (efficiency per PR, gated waves, bounded authority) more than in implementation detail.

## Related Conf42 talks

- [From Alerts to Answers: Modern SRE with Observability, AI, and Agentic Ops](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Savi_Grover_alerts_answers_modern) by Savi Grover of Tekskills Inc at Conf42 SRE 2026.
- [AI-Driven Database Tuning in DevOps: Real-World Lessons from Self-Optimizing Systems](https://www.conf42.com/Database_DevOps_2026_Naga_Bellamkonda_alerts_incident_platform) by Naga Bellamkonda of Gartner at Conf42 Database DevOps 2026.
- [Cell-Based Isolation for Multi-Tenant Platforms on Kubernetes](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) by Lahiru De Silva of WSO2 at Conf42 DevSecOps 2026.

[Watch Naveen Goel's talk](https://www.conf42.com/Feature_Flags_2026_Naveen_Goel_infrastructure_ai_sdlc) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/vz6vGSsSMpc).

## Watch the talk

[Self-Optimizing Infrastructure: Putting AI Inside the SDLC at 200K Requests per Second](https://www.conf42.com/Feature_Flags_2026_Naveen_Goel_infrastructure_ai_sdlc) at Conf42 Feature Flags 2026.
