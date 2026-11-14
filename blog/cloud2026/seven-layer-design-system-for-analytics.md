# Three-layer design systems break on a million-row table

Conf42 Blog, 2026-04-04, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/seven-layer-design-system-for-analytics

In short: Sonali Priya of LB Networks at Conf42 Cloud Native 2026 on a seven-layer design system for analytics, adding data components, semantics and governance.

Your design system's table component was built for a few hundred rows; your analytics platform hands it a million. At Conf42 Cloud Native 2026, Sonali Priya, Creative Design Director at LB Networks (Local Backhaul Networks), argued that the standard three-layer design system model breaks under enterprise analytics, and proposed a seven-layer model that adds data-aware components, visualization primitives, metric semantics, workflow patterns and governance.

## Five line charts, all slightly different

Sonali opens with three patterns anyone who has worked on an analytics product will recognize. Fragmentation: teams rebuild the same charts and dashboards from scratch, so you end up with five versions of one line chart. Visual drift: with no shared rules for colours, scales, axis labels or thresholds, two dashboards in the same product look as if two companies built them. Governance gaps: nobody owns a metric's definition or a component's versioning, and access control is bolted on later.

## Why tokens, components and patterns are not enough

The classic model (primitives such as tokens, then components, then patterns) works very well for consumer apps. It falls apart on analytics because it ignores data volume. Tables need virtualization, streaming and lazy loading. A chart that is clean at a hundred points is an unreadable smear at a hundred thousand, and the model says nothing about aggregation, sampling or progressive disclosure. Nothing drops in and works with your data pipeline, metric layer and access controls, so teams stitch libraries together and the shared system loses its point.

## The seven layers

1. **Design tokens**, extended for analytics: dataviz palettes (sequential, diverging, categorical), density modes for packed dashboards, and semantic tokens such as threshold exceeded or anomaly detected that encode intent, not just appearance. One definition compiles to CSS, iOS, Android and Figma.
2. **UI components**: buttons, inputs, tabs and so on, built only from tokens and deliberately unaware of data.
3. **Data components**: the virtualized table, query builder, filter panel, metric picker. Stateful by design, with loading, empty, partial and error states, plus saved views and column choices that do not break the shared definition.
4. **Visualization primitives**: scales, legends, grids and tooltips that charts are assembled from, with accessibility built in (colour-blind-safe palettes, pattern fallbacks, screen reader support) and encoded rules for when there is more data than pixels.
5. **Semantics and interpretation**: one definition of each metric, its units, thresholds and targets.
6. **Workflow patterns**: drill-down and drill-across, cross-filtering, saving an exploration as a dashboard, period-over-period comparisons.
7. **Governance**: named owners, versioning, access and sensitivity controls, and a contribution workflow with quality gates.

## Three teams, three definitions of revenue

Layer five is the one Sonali calls the most underappreciated. Her scenario: three teams build three dashboards, each with a metric called revenue, and none calculate it the same way. One includes refunds, one uses net and another gross, one runs daily and another weekly. A semantic layer makes it one definition with one set of thresholds, so when a designer, a data engineer and a product manager say churn rate they mean the same thing.

On governance her line is equally firm: every metric and component gets a named owner, not a team and not a Slack channel, a person. Changing a metric definition is not a bug fix; it is a change to history and needs semantic versioning and a migration path.

## Adopt it from the edges inward

You do not build all seven at once. Start with tokens and governance, the cheapest layers with the highest leverage. Then data components and visualization primitives, where users feel the most pain. Then semantics, which is as much organizational work as technical. Patterns come last: codify a flow once you see three teams repeating it. Measure reuse rates, consistency and time to dashboard, or you cannot tell whether it is working.

## Who should watch

Front-end platform teams, design system maintainers and data product leads on dashboard-heavy products. Consumer-app design system teams can skip the middle layers but will still get value from the governance section.

## Related Conf42 talks

- [Pallav Laskar on design tokens as platform infrastructure](https://www.conf42.com/Platform_Engineering_2025_Pallav_Laskar_design_tokens_multi) at Conf42 Platform Engineering 2025.
- [Elena Shabanova on building a design system on a tight timeline](https://www.conf42.com/Machine_Learning_2024_Elena_Shabanova_building_design_system) at Conf42 Machine Learning 2024.
- [Erwin de Keijzer on Perses, the GitOps-native dashboard tool](https://www.conf42.com/Kube_Native_2024_Erwin_de_Keijzer_gitops_perses_dashboard_visualization) at Conf42 Kube Native 2024.

[Watch Sonali Priya's talk](https://www.conf42.com/Cloud_Native_2026_Sonali_Priya_data_pipelines_processing)

[Watch the talk on YouTube](https://youtu.be/grLK2XWaNPA).

## Watch the talk

[Design Systems for Scalable Cloud-Native Analytics Platforms](https://www.conf42.com/Cloud_Native_2026_Sonali_Priya_data_pipelines_processing) at Conf42 Cloud Native 2026.
