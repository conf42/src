# Ad hoc prompts fail in ops; version-controlled templates don't

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/prompt-templates-for-financial-event-streams

In short: Tina Kanth (Microsoft) at Conf42 DevOps 2026 on template-driven prompt engineering for triaging streaming financial events.

Two engineers paste the same error into the same model and get different answers, because only one of them knew which context to add. At Conf42 DevOps 2026, Tina Kanth, a software engineer at Microsoft on the team behind the company's financial engine, argued that this is why ad hoc prompting breaks down in operations, and that the fix is templates: versioned, modular prompts that carry the senior engineer's troubleshooting knowledge into every request.

The setting is a high-throughput financial platform: millions of events, microservices and Spark engines, Cosmos DB and Redis in between, on Azure or AWS. Low outages, high availability, minimum latency and auditability are the non-negotiables.

## The real problem is context, not wording

Kanth's diagnosis starts with fragmentation. Transactions, metrics and application logs live in different tools, so a developer or SRE tracing why a transaction didn't process has to hop between systems. Copilots help, but she is direct that prompt engineering and context engineering go hand in hand and neither substitutes for the other. You can write the best prompt in the world and still get a bad answer if the model lacks the context.

Ad hoc prompts fail in four ways in her account: missing context, inconsistent output from probabilistic models, poor auditability (how do you measure a platform nobody prompts the same way twice?) and latency overhead.

## A template is operational knowledge written down

Her template anatomy has four parts: operational knowledge, policy constraints, event context and schema reference, plus a defined output format.

Operational knowledge is the part that usually lives in a few senior heads: when you see this log message, which fields matter and what is the next action. Writing it into a template is, as she puts it, a great leveller, because a junior engineer's triage then starts from the expert's steps. Policy constraints spell out what the model must not do, which matters a lot with production financial data. The output format has to be machine-actionable so one agent's output can feed the next.

She draws the parallel with GitHub's Spec Kit, which keeps developers inside a project's design guardrails; templates do the same for ops prompts.

## The plumbing around the prompt

The framework she sketches is concrete. Events are ingested, then routed with Semantic Kernel plugins to the right templates. A corpus of docs, designs and code is embedded into a vector database for context injection. An output validator checks results and feeds a dashboard of model effectiveness. The output is an action item, such as replaying orders or deleting duplicates, either automated or sent through an approval process.

Because templates live in source control, every change goes through reviewers and approvers. She recommends modular templates over one big file, and a separate pipeline to re-vectorise documentation as teams update it so the model doesn't work from stale docs.

The abstract cites accuracy gains of 10 to 15 points from this approach; the talk itself spends its time on the architecture and the rollout advice.

## Start with the 80/20 cases

Her rollout advice is pragmatic: pick frequent problems that cause the most toil for on-call engineers, connect to the observability platform, keep fallback mechanisms until performance evaluation is done, and set up a feedback loop, even an informal one at first. Beyond triage she points at compliance checks against the AWS and Azure Well-Architected frameworks and capacity forecasting as extensions.

## Who should watch

SREs and platform engineers building LLM-assisted triage for any high-volume system, not only finance. It is architecture and practice, no live demo. If your team's prompts live in a Slack thread titled "useful prompts", this is the argument for moving them into a repo.

## Related Conf42 talks

- [Autonomous FinOps for Cloud-Native Financial Services](https://www.conf42.com/Kube_Native_2025_Manoj_Kalakoti_finops_costgovernance_autonomous) by Manoj Kalakoti (Apple) covers cost governance at scale.
- [Scalable prompt engineering frameworks for safer LLMs](https://www.conf42.com/Prompt_Engineering_2025_Preetham_Sunilkumar_frameworks_llms_scalable) by Preetham Sunilkumar (LPL Financial) is another financial-services take on structured prompting.
- [Log-Centric Intelligence: Real-Time Compliance Observability](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prem_Anand_observability_logging_compliance) by Prem Anand puts LLMs on top of logs for compliance.

[Watch Tina Kanth's talk](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts)

[Watch the talk on YouTube](https://youtu.be/QNxfOaMrl54).

## Watch the talk

[Real-Time FinOps Intelligence: Template-Driven Prompt Engineering for Streaming Financial Events](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts) at Conf42 DevOps 2026.
