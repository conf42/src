# Fast campaign dashboards start with small, honest payloads

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/cross-cloud-campaign-analytics-react

In short: Sruthi Erra Hareram at Conf42 JavaScript 2025 on a cross-cloud analytics pipeline that feeds a React dashboard built for speed and trust.

Two dashboards that disagree do more damage than one slow dashboard: people stop trusting both. At Conf42 JavaScript 2025, Sruthi Erra Hareram walked through an end-to-end campaign analytics stack, from a partitioned data lake and Azure Databricks to a React front end, built around one goal: shrink the distance between a marketer's question and a trustworthy answer.

The talk covers the whole path rather than one layer, which is its strength. The JavaScript part only works because of decisions made three hops upstream.

## Every layer optimises for something different

Sruthi's pipeline runs ingest, transform, serve, visualise, and she gives each stage one job. Storage is about cost and durability: a lake partitioned by day and source, lifecycle rules that push cold data to cheaper tiers without breaking lineage, and manifest files that surface missing partitions and record-count mismatches early. Orchestration, here Azure Data Factory, runs parameterised batch and micro-batch pipelines so one pattern covers many feeds, and its alerts name the failing step, the affected partition and a link to the run.

Compute in Azure Databricks owns correctness: columnar tables with constrained schema evolution, deterministic transforms, and attribution and deduplication done there, not in the browser. Aggregates come out at the grain product managers actually use, like daily by geography, channel and creative. Row-level security is applied at query time from identity claims. The serving API caps and compresses payloads and keeps short caches on hot endpoints so a traffic surge doesn't stampede downstream systems.

Why cross-cloud at all? Storage sits where the economics are best, transformation where the managed Spark and governance are, and because the contract to the front end stays fixed, workloads can move later without rewriting the product.

## React patterns for big data on ordinary laptops

On the front end, data state and presentation stay separate. Chart components share one grammar for titles, axes and empty states. Filters for date, geography, channel and creative live in a central store with memoised selectors. Requests carry authentication, retry carefully and are cancelled when the user changes direction. The interface responds to a filter change immediately and the data fills in a moment later, so every click feels acknowledged.

For large data sets: virtualise long tables, send a summary first and fetch detail on intent, run small roll-ups in a Web Worker to keep the main thread free, and debounce rapid filter changes so only the final intent triggers work. Existing Power BI reports are embedded with single sign-on and two-way filter sync, so nobody has to leave the app.

## Charts should state the conclusion

The storytelling advice is the part analysts will steal. A chart title should state the finding, not the category, with benchmarks for context and annotations tying movements to business decisions. Views differ by role: executives get a compact ROI and pacing summary, campaign managers a tactical cross-channel view with a next step, analysts the freedom to slice and export, all from one source of truth.

Performance is treated as a promise: code splitting, server and browser caches with lifetimes matched to data freshness, server-side pagination with prefetch, and tracking of time to interactive, first contentful paint and p95 API latency, with regressions handled as product bugs.

Her closing answers are crisp. Keep joins and heavy aggregation on the server and give the worker only small roll-ups. Enforce tenant filters on the server, never trust client-provided ones.

## Who should watch

Front-end engineers building analytics products, data engineers who hand them APIs, and anyone whose dashboards are slow or contradict each other. It is architecture-level, with no code on screen, but the server-versus-browser split is a checklist you can apply directly.

## Related Conf42 talks

- [Gaurab Patra and Bhagyajit Jagdev on data analytics in the browser with AlaSQL.js](https://www.conf42.com/JavaScript_2022_Gaurab_Patra_Bhagyajit_Jagdev_data_analytics_browser_alasqljs) at Conf42 JavaScript 2022.
- [Rao Marapatla of BreakthroughT1D on a unified API ecosystem for marketing analytics](https://www.conf42.com/Chaos_Engineering_2025_Rao_Marapatla_analytics_marketing_insights) at Conf42 Chaos Engineering 2025.
- [Abhinav Chunchu of Lowe's on adaptive, data-driven user interfaces in JavaScript](https://www.conf42.com/JavaScript_2024_Abhinav_Chunchu_2_adaptiveinterfaces_datadrivenux) at Conf42 JavaScript 2024.

[Watch Sruthi Erra Hareram's talk](https://www.conf42.com/JavaScript_2025_Sruthi_Erra_Hareram_cross_campaign_analytics), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/GIdxSuuEbhg).

## Watch the talk

[Cross-Cloud Campaign Analytics Meets JavaScript: Building Scalable Frontends for Big Data Insights](https://www.conf42.com/JavaScript_2025_Sruthi_Erra_Hareram_cross_campaign_analytics) at Conf42 JavaScript 2025.
