# Your runbooks have a half-life, so let the incidents write them

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/knowledge-half-life-ai-incident-knowledge-systems

In short: Mahmood Nawaz (LTIMindtree) at Conf42 Incident Management 2025 on four-layer AI knowledge systems that surface past fixes while an incident is still open.

The engineer who knows why the queue backs up every second Tuesday is a single point of failure with a notice period. At Conf42 Incident Management 2025, Mahmood Nawaz, Senior Specialist in Data Engineering at LTIMindtree, built a talk around the idea of knowledge half-life: in cloud-native systems, troubleshooting know-how goes stale within months, and the fix is an AI-driven knowledge system that captures what each incident teaches and puts it in front of the next responder.

## Why tribal knowledge stopped scaling

Nawaz's diagnosis has three parts. Cloud providers keep shipping new services and features that change how existing systems behave and create new failure modes. Small changes cascade, so one tweak can mean updates to monitoring, alerting, deploy scripts and procedures. And continuous delivery means the system you documented last quarter has already moved.

Meanwhile, most incident frameworks were designed for slower monolithic systems, and experienced engineers are scarce. Organisations keep paying for training and documentation whose value decays faster each year. That is the treadmill he wants off.

## Four layers

The architecture he proposes stacks four layers:

- **Foundation.** Fast, highly available knowledge storage, built on a vector database for similarity search and an event-driven design so knowledge updates in real time.
- **Processing.** The cognitive core, where NLP extracts structured information from unstructured sources: log files, incident reports and the communication threads where the real diagnosis usually happens.
- **Interaction.** Conversational interfaces for natural-language questions mid-incident, visual timelines and dependency views, explanations pitched to the user's experience level (more detail for new joiners, terse summaries for veterans), and context-aware delivery that surfaces relevant knowledge from active alerts without anyone asking.
- **Integration.** APIs into incident management, monitoring and collaboration tools; workflow automation that extracts and distributes insights when an incident is resolved; and real-time sync so the same knowledge appears everywhere.

The integration layer is the one that decides whether this works. A knowledge base that needs its own tab during an incident is a knowledge base nobody opens during an incident.

## Matching today's incident to last year's

Where the system earns its keep is solution generation. Instead of rediscovering a fix someone already found, machine learning matches the characteristics of the current incident against historical ones and suggests troubleshooting steps that worked before. Each resolved incident feeds back in, so the base gets more complete as more teams contribute. Nawaz calls these network effects, and adds cross-team surfacing: an insight from one team is pushed to others who are likely to hit the same issue.

He presents figures for implementations, including 99.8% processing accuracy for knowledge extraction, a 90% reduction in the time to deliver relevant information compared with manual searching, and a 75% cut in the mental effort engineers need to find and apply it. The talk doesn't detail how these were measured, so treat them as directional.

## Culture is the other half

His closing point is that the technology is necessary but not sufficient. These systems only work in organisations that value knowledge sharing and collaborative problem solving, and the benefits he lists (faster resolution, expertise that survives turnover, operations that scale without proportional headcount) depend on people writing things down in the first place.

## Who should watch

SRE leads and platform teams whose postmortems vanish into a wiki, and anyone sketching an internal RAG assistant for on-call. It is an architecture-level talk without a demo, so expect a blueprint rather than a product walkthrough.

## Related Conf42 talks

- [Building Production-Ready RAG Systems for Enterprise Knowledge Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) by Srinivas Chennupati covers the retrieval plumbing.
- [Transforming Knowledge Systems with Embedded Analytics in Cloud-Native Architectures](https://www.conf42.com/Kube_Native_2025_Harshita_Dubey_knowledge_analytics_architectures) by Harshita Dubey looks at knowledge systems from the analytics side.
- [Postmortem Culture: Learning from Failure](https://www.conf42.com/Chaos_Engineering_2020_Yury_Nino_postmortem_culture) by Yury Niño is about producing the knowledge worth capturing.

[Watch Mahmood Nawaz's talk](https://www.conf42.com/Incident_Management_2025_Mahmood_Nawaz_knowledge_cloud_resilience)

[Watch the talk on YouTube](https://youtu.be/5IkZFSr4J88).

## Watch the talk

[AI-Powered Knowledge Systems for Resilient Cloud Incident Response](https://www.conf42.com/Incident_Management_2025_Mahmood_Nawaz_knowledge_cloud_resilience) at Conf42 Incident Management 2025.
