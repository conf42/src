# Carbon is telemetry too - a GreenOps pipeline from open source parts

Conf42 Blog, 2026-09-03, updated 2026-11-09. https://www.conf42.com/blog/obs2026/carbon-is-telemetry-greenops-pipeline

In short: Diana Todea of VictoriaMetrics at Conf42 Observability 2026 turns cloud billing exports into carbon, energy and water metrics with Spruce and Grafana.

Cloud cost is telemetry, and so is the carbon behind it, so it belongs in the same pipeline as your other metrics. At Conf42 Observability 2026, Diana Todea, DevRel Engineer at VictoriaMetrics, showed a home-lab GreenOps pipeline that takes an Azure FOCUS billing export, enriches it with sustainability data using the open source Spruce project, and lands carbon, energy and water metrics in VictoriaMetrics and Grafana.

It's a build-log talk: what she wired together, where it went wrong, and how a bug report turned into a fix from the maintainers. The full pipeline lives in a public GitHub repo, with a companion blog post.

## Observability has a footprint of its own

Todea opens with the uncomfortable part. Collecting, processing, storing and querying telemetry all burn energy, and more data doesn't mean better observability. Before building anything green, cut the hoarding: unnecessary metrics, runaway cardinality, oversized log retention, telemetry nobody reads. Meanwhile, sustainability numbers mostly live in reports rather than in the engineering tools where decisions get made. Her pipeline is an attempt to move them.

## The pipeline, stage by stage

The architecture is short:

1. Export a FOCUS 1.0 cost report from Azure cost management (Spruce also reads AWS reports).
2. Run Spruce over the CSV. It normalises the data into a FOCUS-compatible Parquet dataset and enriches each billing record with environmental attributes from open models.
3. A small Python script converts the Parquet rows into Prometheus metrics.
4. Store them in VictoriaMetrics, explore with its UI, and build the real dashboard in Grafana.

The metric families give a feel for what you get: cloud cost and usage quantity per billing record, estimated operational energy in kilowatt-hours, operational and embodied carbon emissions, water use, and power usage effectiveness, all labelled by provider, service, region, SKU and resource. Her Grafana dashboard combines financial, operational and environmental views on one screen, plus a resource inventory by service and region.

She also spent time in the VictoriaMetrics UI, specifically Cardinality Explorer for label distribution and Query Analyzer for query performance. Sensible, given she'd just told everyone to watch their cardinality.

## The detour: don't simulate what the project already gives you

Her first version skipped the source and used a home-made data simulator. It added complexity and gave her none of the richness of Spruce's real sustainability attributes. Lesson recorded: start from the origin and keep it simple. She chose Azure over AWS because of free-tier limits on the AWS side.

The better story is the open source one. Azure offered two report types and Spruce only supported the legacy one at the time. Todea filed a bug, went back and forth with the maintainers, and they added FOCUS 1.0 support for Azure and improved the docs. That's the contribution path the talk abstract promised, shown rather than described.

## Where it could go next

Her backlog: incremental imports, multi-cloud support, carbon budgets and team-level reporting, VictoriaMetrics recording rules and alerting, carbon or cost anomaly detection, Kubernetes namespace-level attribution, OpenTelemetry integration, and possibly Kepler, the CNCF project that exports per-container and per-pod energy estimates to Prometheus. She was clear these are ideas, not shipped features.

## Who should watch

FinOps and platform folks curious whether carbon data can sit next to their cost dashboards, and anyone looking for an approachable first open source contribution story. It's a home project, so treat it as a reference build rather than a production design.

## Related Conf42 talks

- [Pini Reznik on moving from error budgets to carbon budgets](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pini_Reznik_error_carbon_empowering) (Conf42 SRE 2024): one of the items on Todea's wish list.
- [Neel Shah on Green DevOps](https://www.conf42.com/DevOps_2024_Neel_Shah_green_sustainable_software) (Conf42 DevOps 2024).
- [Ganeshkumar Palanisamy on observability and FinOps at multi-cloud scale](https://www.conf42.com/Observability_2025_Ganeshkumar_Palanisamy_platforms_scale_finops) (Conf42 Observability 2025).

[Watch Diana Todea's talk](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability)

[Watch the talk on YouTube](https://youtu.be/YInhHfUZsLc).

## Watch the talk

[How to build your own green observability pipeline](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) at Conf42 Observability 2026.
