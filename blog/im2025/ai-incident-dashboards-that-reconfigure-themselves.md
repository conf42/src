# Incident dashboards should interpret the data, not just show it

Conf42 Blog, 2025-09-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/ai-incident-dashboards-that-reconfigure-themselves

In short: Priyanshi Deshwal (Mode) at Conf42 Incident Management 2025 on AI incident views that rank alerts, pick visuals and write plain-language summaries.

Five people on a bridge call, five different dashboards, everyone squinting at time ranges that don't line up. At Conf42 Incident Management 2025, Priyanshi Deshwal, Senior Software Engineer at Mode (she introduced herself as a frontend engineer at ThoughtSpot, working on data visualisation and analytics products), argued that the classic dashboard is a monitoring tool we keep misusing as a crisis tool, and laid out what an AI-assisted incident view should do instead.

Her framing is a visualisation engineer's, which makes it a useful counterweight to the usual AIOps talk about models and pipelines. The question she keeps returning to is simple: during your last big incident, how much time went into finding the right data rather than acting on it?

## Dashboards were built to watch, not to fight fires

Deshwal's critique of dashboards has three parts. They are reactive by design, showing history and forcing you to reconstruct the present. They overload you: twenty charts refreshing every few seconds while you try to work out which change came first and whether you're looking at a symptom or a cause. And they demand manual work, with someone clicking filters and widening time windows at exactly the moment human error is most expensive.

Underneath that sits the data problem. Logs live in one tool, metrics in another, deployment history somewhere else, and responders swivel between them correlating by hand. Traditional tools sample, add latency and leave blind spots, which is the last thing you want during a high-severity incident.

## From a map to a GPS

The analogy she uses is a good one. A map tells you where the roads are; a GPS reroutes you when traffic builds. AI-powered visual intelligence should do the second job: interpret the data, group related anomalies, and suggest probable root causes with confidence scores, while the layout reconfigures itself so the most relevant metrics bubble up.

She breaks this into three capabilities:

- **Alert prioritisation.** Learn from historical incidents so that instead of triaging 500 alerts by hand, you get a ranked list of the few that matter.
- **Automated visual recommendations.** Pick the right chart for the problem. During a network outage, generate a topology map with affected nodes in red so the blast radius is visible at a glance.
- **Contextual summaries.** Turn technical data into a plain-language summary for stakeholders, so a responder isn't spending a chunk of every hour writing status updates.

Further out she sketches natural-language queries ("show me all error spikes for the checkout service in the last 30 minutes"), voice control and shared interfaces where several teams explore the same data live. The split of work stays clear: the machine crunches data at scale, humans keep judgment and communication.

## Shadow mode before trust

The implementation section is the part to steal. Measure first: time to detection, time to resolution and the number of hand-offs per incident. Unify logs, metrics and alerts into one pipeline, because a model with half the picture gives half an answer. Train on historical incidents, design role-based views (deep detail for SREs, business impact for executives), and treat the AI like a team member who should get smarter after every retrospective.

Her advice on adoption is pragmatic. Fix data quality and naming conventions before blaming the model. Run the AI in shadow mode, making recommendations alongside human decisions, so responders can compare and build confidence. Roll out gradually and bring incident commanders in early. And keep the visualisation layer fast under load, because a dashboard that freezes while everything is on fire is its own incident.

## Who should watch

Engineers building internal incident tooling, observability product teams, and anyone who owns the dashboards their on-call rotation actually opens at 3am. It is a vision-and-roadmap talk rather than a product demo or a code walkthrough, so come for the design principles and the rollout checklist. The closing question is worth taking back to your team: if your next P1 happened tomorrow, what should the screen show you first?

## Related Conf42 talks

- [The Failures You Don't See on Dashboards](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) by Abhimanyu Narwal looks at what green dashboards hide.
- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz goes deeper on the alert-ranking half of the problem.
- Erwin de Keijzer's talk on [Perses, the GitOps-native dashboard visualization tool](https://www.conf42.com/Kube_Native_2024_Erwin_de_Keijzer_gitops_perses_dashboard_visualization), covers dashboards as code.

[Watch Priyanshi Deshwal's talk](https://www.conf42.com/Incident_Management_2025_Priyanshi_Deshwal_visual_interfaces_intelligence)

[Watch the talk on YouTube](https://youtu.be/Ai6fODH9UFw).

## Watch the talk

[Reimagining Incident Response with AI-Powered Visual Interfaces: From Static Dashboards to Real-Time Intelligence](https://www.conf42.com/Incident_Management_2025_Priyanshi_Deshwal_visual_interfaces_intelligence) at Conf42 Incident Management 2025.
