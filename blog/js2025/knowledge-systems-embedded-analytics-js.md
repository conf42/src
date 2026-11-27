# Knowledge bases fail when nobody measures how people search them

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/knowledge-systems-embedded-analytics-js

In short: Harshita Dubey of Apex Fintech Solutions at Conf42 JavaScript 2025 on rebuilding a SharePoint knowledge system with embedded analytics and JS microservices.

If finding an answer in the company wiki is harder than asking on Slack, people will ask on Slack. At Conf42 JavaScript 2025, Harshita Dubey of Apex Fintech Solutions told the story of a 24-month effort to turn a static enterprise knowledge system into one that watches how it is used and adapts, built on SharePoint Online with custom JavaScript microservices on top.

It is a short talk, roughly a lightning-length case study, and it is mostly about approach and results rather than code. Think of it as the slide deck you would want before pitching the same project internally.

## Why knowledge systems die quietly

Harshita opens with the claim that more than half of enterprise knowledge systems fail to deliver real value, even at organisations with over 100,000 employees spread across many countries. She names three causes: static architectures that can't keep up with how teams work, content scattered across silos, and a user experience so poor that self-service loses to asking a colleague.

Her team's fix was to treat it as a data-driven product, not an IT project. Embed analytics to see behaviour, mine search patterns for intent, build real-time feedback loops, and stop guessing.

## JavaScript as the adaptive layer

The architecture is deliberately unglamorous. SharePoint Online is the secure base. On top sit JavaScript microservices for analytics, search and personalisation, plus dynamic UI components that respond to user behaviour, context-aware filtering so people see what is relevant to their role, and natural-language search so users can ask questions the way humans do. Three engines carry it: NLP-backed search, a personalisation engine tuned to behaviour and role, and live dashboards that make the whole thing visible.

The governance angle is the part many teams skip. Dashboards tracked engagement, showed where users abandoned searches (a polite way of saying where the content failed them), and surfaced emerging needs before anyone filed a request.

## The numbers she reports

Harshita reports that information retrieval time fell by 33%, self-service resolution rose 22 points from 62% to 84%, onboarding time dropped 21%, support tickets fell 35%, and efficiency gains saved $3.7M a year. The talk does not break down how each figure was measured, so read them as the outcome of this one programme rather than a benchmark.

## Four principles and a roadmap

She distils it into modularity (independent services that grow without breaking each other), analytics first (measure from day one), scalability (assume success and design for it) and user-centric development (tools fail when users aren't part of the build). The roadmap is assess, lay the analytics foundation, add JavaScript-powered intelligence, optimise from feedback, then scale. The lesson she says travels to any stack: invest in microservices and you get flexibility without replatforming.

## Who should watch

Engineers and product owners stuck with an intranet or SharePoint estate that nobody loves, and anyone who needs a short, metrics-led argument for instrumenting internal tools. If you want implementation detail, such as which search stack or how the microservices talk to SharePoint, this talk stays at the architecture level.

## Related Conf42 talks

- [Mahmood Nawaz of LTIMindtree on AI-powered knowledge systems for incident response](https://www.conf42.com/Incident_Management_2025_Mahmood_Nawaz_knowledge_cloud_resilience) at Conf42 Incident Management 2025.
- [Ben Fistein of Semantee.ai on the future of search](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ben_Fistein_future_search) at Conf42 LLMs 2024.
- [Prateek Mittal of Harness on knowledge graphs for AI-first software delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) at Conf42 LLMs 2026.

[Watch Harshita Dubey's talk](https://www.conf42.com/JavaScript_2025_Harshita_Dubey_transforming_knowledge_embedded), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/_gkw2ZYf7VA).

## Watch the talk

[Transforming Knowledge Systems with Embedded Analytics and JavaScript Insights](https://www.conf42.com/JavaScript_2025_Harshita_Dubey_transforming_knowledge_embedded) at Conf42 JavaScript 2025.
