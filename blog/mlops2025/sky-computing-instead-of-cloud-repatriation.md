# Before you repatriate, consider sky computing

Conf42 Blog, 2025-08-27, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/sky-computing-instead-of-cloud-repatriation

In short: Brian Irish (Ditto) at Conf42 MLOps 2025 on sky computing and SkyPilot, an intercloud broker approach to vendor lock-in, egress fees and GPU scarcity.

Plenty of companies hit by a shocking cloud bill are moving workloads back on-prem. Brian Irish, an engineering lead at Ditto with years as an SRE behind him, argues at Conf42 MLOps 2025 that many of them never set up basic cost controls in the first place, and that the better answer is sky computing: treat all clouds as one pool and let a broker place each workload where it runs best.

The talk introduces the idea from Ion Stoica's paper at UC Berkeley, frames it in three pillars of Brian's own, and then shows what it looks like in practice with SkyPilot, the open-source intercloud broker from Berkeley's Sky Computing Lab.

## Repatriation is often a missed cost review

Brian credits the cloud with keeping its promises of on-demand scale, pay-as-you-go pricing and global reach, then lists the drawbacks: vendor lock-in, data gravity and egress charges that surprise everyone. He cites a survey finding that 42% of US organisations are considering or have already moved at least half their cloud workloads back on-premises.

His question is whether those companies planned their cloud usage with cost in mind or just reacted to the invoice. He suspects the latter: no automatic shutdown of dev environments after hours, no spot instances for batch work, no resource quotas. Stepping back to on-prem, he suggests, might not be a step forward.

## Three pillars of sky computing

These are Brian's framing, and he is clear they are his, not the paper's. Abstraction is the glue: Kubernetes, Ray and S3-compatible APIs hide which cloud your data and compute live on, across AWS, GCP and Azure and neoclouds like Lambda Labs and CoreWeave. Automation is the intercloud broker deciding workload placement on price, availability and regulatory needs. He calls it the largest pillar and the hardest to get right. Agility depends on reciprocal peering agreements between providers that make data transfer free or cheap, which would break down egress fees and data gravity.

## SkyPilot is the broker you can use today

SkyPilot is where the talk becomes practical. Brian walks through its claims, which come from the project and its case studies rather than his own benchmarks: a unified interface to many clouds plus Kubernetes and on-prem, big savings from spot orchestration, fast GPU provisioning, faster checkpointing with cached mounts, and no code changes for existing ML workloads. You write one YAML file and run one launch command.

He quotes the Abridge case study, where a team moving off a Slurm cluster got interactive GPU shells with a single launch command, Jupyter notebooks on GPU clusters, managed jobs that restart automatically on failure, and models exposed as FastAPI services for quick evaluation, which Slurm does not offer natively. The distributed training YAML he shows is short: plain PyTorch and Hugging Face, with SkyPilot filling in node counts, GPUs and IP addresses.

## Split the pipeline across clouds

The payoff for ML is placing each stage where it fits best. His example: training on Google Cloud TPUs, inference on AWS Inferentia for lower latency, and preprocessing on Azure because it is often cheaper, with data residency rules respected along the way. That is hard to do by hand and routine with a broker.

He ends with honest obstacles. Universal standards across clouds are unlikely given competitive interests, though Kubernetes, Ray and S3 APIs get you a long way. Hyperscalers have every reason to resist peering agreements that cut egress revenue. Sky computing works with that friction rather than waiting for it to vanish.

## Who should watch

ML platform teams fighting GPU scarcity or single-cloud bills, and SREs asked to evaluate repatriation. It is part concept talk, part SkyPilot introduction, and Brian is upfront that it was his first time recording with OBS, so forgive a glitch or two.

## Related Conf42 talks

- [Lawrence Finn on breaking vendor lock-in with Cloud Sidecar](https://www.conf42.com/Cloud_Native_2021_Lawrence_Finn_multicloud_breaking_cloud_sidecar) at Conf42 Cloud Native 2021.
- [Hari Yerramsetty (Flexport) on cloud cost efficiency](https://www.conf42.com/Chaos_Engineering_2025_Hari_Yerramsetty_cost_optimization_success), the cost controls Brian says teams skip.
- [Arun Pandiyan Perumal (Adobe) on managing multi-cloud complexity with SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Arun_Pandiyan_Perumal_managing_multi_cloud) at Conf42 SRE 2025.

[Watch Brian Irish's talk](https://www.conf42.com/MLOps_2025_Brian_Irish_embracing_sky_computing) and then read the sky computing paper he recommends.

[Watch the talk on YouTube](https://youtu.be/ed-ImXeupi0).

## Watch the talk

[Embracing Sky Computing: Charting a New Course in AI Cloud Infrastructure](https://www.conf42.com/MLOps_2025_Brian_Irish_embracing_sky_computing) at Conf42 MLOps 2025.
