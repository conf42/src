# A knowledge base that measures its own failed searches gets better

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/embedded-analytics-knowledge-management-kubernetes

In short: Harshita Dubey (Apex Fintech Solutions) at Conf42 Kube Native 2025 on turning a SharePoint knowledge base into a Kubernetes-backed system with embedded analytics.

Every company has a knowledge base, and most employees have learned to ask a colleague instead. At Conf42 Kube Native 2025, Harshita Dubey, Senior Technical Program Manager at Apex Fintech Solutions, described how an enterprise kept SharePoint as its content store but wrapped it in Kubernetes-hosted analytics, search and automation services, so the system could see where people got stuck and fix itself.

The case is a large one: a knowledge management system serving 15,000+ employees across global offices. Dubey opened with the claim that over half of enterprise knowledge systems miss their performance goals, and the root causes she listed will sound familiar.

## Why knowledge systems fail

Three causes. Siloed design, where each department builds its own fragmented repository. Outdated, monolithic architecture that cannot adapt to new business or user demands. And poor adoption, because people abandon tools that return irrelevant results or are painful to use. Her conclusion is that this needs an architectural rethink, not a new search box.

## Keep the content, replace everything around it

The contrast she drew is static repository versus containerised ecosystem. SharePoint Online stays as the content source. Around it, containerised services handle analytics, search and automation, and Kubernetes provides scaling, resilience and continuous deployment. Because services are decoupled from the content layer, each can scale or be modernised without disturbing the documents underneath.

The analytics layer has three parts: user behaviour analytics (engagement, click-throughs, navigation paths), search pattern mining (how people query, and where searches fail), and real-time feedback loops that adjust results and recommendations based on what users actually do. Failed searches are the gold here: they tell you exactly which content is missing.

## Smart features and a governance loop

On top of that, Kubernetes-hosted services add natural language search that tries to understand intent beyond keywords, context-aware filtering by role or project, and predictive analytics that anticipates what someone needs before they search. Automation extends to governance: tracking engagement and abandonment to find friction points, surfacing popular and missing topics, and promoting high-value content automatically, without someone curating by hand.

The roadmap runs in four phases: foundation (clusters, microservices, SharePoint API integration), analytics (tracking and early AI recommendations), intelligence (NLP and predictive analytics), and optimisation (automated governance, enterprise-wide scale).

## The results she reported

After full implementation: 33% faster information retrieval, 35% fewer support tickets and a 22% boost in self-service resolution. User satisfaction rose 37.5%, onboarding time fell from 14 weeks to 11, and the transformation delivered $3.7M in tangible gains from efficiency improvements.

Her starter advice is short: instrument everything for observability, modularise analytics as separate services, collect real-time user feedback, let data drive content lifecycles, and define success metrics up front.

## Who should watch

Internal tools teams, IT leaders and program managers who own a sprawling intranet or wiki and want an incremental path that does not start with a content migration. It is a brief case-study talk at the architecture level; it does not go into which NLP or search stack was used.

## Related Conf42 talks

- [Building Production-Ready RAG Systems: Platform Engineering Strategies for Enterprise Knowledge Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) by Srinivas Chennupati (Fannie Mae) is the LLM-era version of the same problem.
- [Shipping with Context: Knowledge Graphs as the Backbone of AI-First Software Delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) by Prateek Mittal (Harness) structures engineering knowledge as a graph.
- [AI-Powered Knowledge Systems for Resilient Cloud Incident Response](https://www.conf42.com/Incident_Management_2025_Mahmood_Nawaz_knowledge_cloud_resilience) by Mahmood Nawaz (LTIMindtree) puts a knowledge system to work during incidents.

[Watch Harshita Dubey's talk](https://www.conf42.com/Kube_Native_2025_Harshita_Dubey_knowledge_analytics_architectures)

[Watch the talk on YouTube](https://youtu.be/N0it3_YmwWI).

## Watch the talk

[Transforming Knowledge Systems with Embedded Analytics in Cloud-Native Architectures](https://www.conf42.com/Kube_Native_2025_Harshita_Dubey_knowledge_analytics_architectures) at Conf42 Kube Native 2025.
