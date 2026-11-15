# Let AI suggest the rollback before you let it run the rollback

Conf42 Blog, 2026-01-10, updated 2026-11-09. https://www.conf42.com/blog/devops2026/aiops-from-firefighting-to-prevention

In short: Aravind Sekar of Twilio at Conf42 DevOps 2026 on AIOps for reliability, from alert grouping and predictive scaling to remediation that earns its autonomy.

When a region goes down, every threshold monitor on every host fires at once, and the on-call engineer gets hundreds of pages about one problem. At Conf42 DevOps 2026, Aravind Sekar, director of engineering at Twilio, walked through where AI and ML actually help with that kind of reliability work, and where they still need a human holding the keys. His model is a staged handover: AI recommends a mitigation, a human approves it, and only after that loop has run many times does AI execute on its own.

## Why the old monitoring model buckles

Aravind's diagnosis is about scale. Monoliths became many microservices, dependencies multiplied, and deployments went from monthly or quarterly to several a day, so each outage cascades further and each release is another chance to ship a regression.

Against that, most teams still run threshold-based monitors on 5xx counts, CPU or heap. The results are alert storms, root cause analysis across telemetry volumes no human can read, tribal knowledge that leaves with the people who hold it, and on-call burnout from always fighting the fire instead of preventing the next one.

He also opens with a reminder of stakes, citing the AWS us-east-1 outage of October 20 and an often-quoted estimate of around $5,600 of lost revenue per minute of downtime.

## Where ML genuinely helps

His framework rests on four capabilities: pattern detection, predictive analytics, intelligent automation and augmented insight over large data. In practice that means anomaly detection across all signal types, seasonal awareness (his example is pizza orders on Super Bowl weekend), correlation across metrics, logs and traces, and a push towards causality rather than coincidence.

The build advice is pragmatic:

- stream the right telemetry first; without it nothing else works
- tier the models, with lightweight ones on the stream and heavier ones on aggregates
- keep inference near real time, since a detection 30 minutes late is not useful
- validate models continuously and keep a safe way to roll a model back when false positives rise, the same way fraud models are retrained as fraud changes

## Two quick wins: scaling and paging

Capacity is where Aravind sees an easy return. Teams know a peak is coming, over-provision because scaling up takes minutes, then forget to scale down. Predictive, just-in-time scaling addresses both; he cites 92% SLO adherence and 35% cost reduction for that approach.

The most concrete result is from his own on-call experience. Using PagerDuty's alert grouping, related alerts from many tripped monitors were folded into one incident pointing at the likely area, which he says cut pager noise and alert storms by 60%. He notes that most monitoring and incident tools, from Datadog and Dynatrace to Splunk and BigPanda, now ship similar AIOps features, so phase two often means switching on what you already pay for.

## Remediation on a leash

The remediation section is where the talk is most careful. Many fixes are the generic mitigations from Google's SRE book: roll back the recent deploy, replace the bad host, pull it from the load balancer, limit traffic. Because the set is small, it can be automated. The question is trust.

Aravind's human-AI collaboration loop: AI spots elevated 5xx on a version deployed an hour ago and suggests rolling back; a human agrees and either does it or hands the action to the AI; the outcome is captured and the loop repeats until humans can step out for that class of issue. He is also frank that automated root cause identification is still in its early stages and depends on the quality of the data you feed it.

## Who should watch

Engineering managers and SREs deciding where to start with AIOps, especially if alert storms are the main pain. It is a strategy talk rather than a build tutorial, with a clear phased plan: emit good telemetry, then correlate and map dependencies, then automate and predict, then optimise.

## Related Conf42 talks

- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz zooms in on the alert grouping problem.
- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi shows the LLM side of the suggest-then-act loop.
- [AI-Powered Anomaly Detection and Self-Healing Systems for Resilient and Efficient Supply Chains](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Venkata_Anil_Kumar_Nilisetty_ai_powered_anomaly) by Venkata Anil Kumar Nilisetty applies detection and self-healing to one industry.

[Watch Aravind Sekar's talk](https://www.conf42.com/DevOps_2026_Aravind_Sekar_reliability_prevention_ai)

[Watch the talk on YouTube](https://youtu.be/BkTlfUfygTM).

## Watch the talk

[AI-Powered Reliability: Stop Fighting Fires, Start Preventing Them](https://www.conf42.com/DevOps_2026_Aravind_Sekar_reliability_prevention_ai) at Conf42 DevOps 2026.
