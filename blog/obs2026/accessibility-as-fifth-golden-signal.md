# Put accessibility on the dashboard as a fifth golden signal

Conf42 Blog, 2026-08-31, updated 2026-11-09. https://www.conf42.com/blog/obs2026/accessibility-as-fifth-golden-signal

In short: Victoria Nduka of VictoriaMetrics at Conf42 Observability 2026 turns daily axe-core scans into Prometheus-style metrics and Grafana trends.

Latency, errors, traffic and saturation all exist because they describe what users feel. None of them tells you whether a screen-reader user can get through your sign-up form. At Conf42 Observability 2026, Victoria Nduka, Technical Support Intern at VictoriaMetrics with a background in UX design, made the case for treating accessibility as a fifth golden signal, and showed a small, working pipeline that does it with open source tools.

Yes, Victoria works at VictoriaMetrics. She knows. It's a good conversation starter.

## The four signals are already about UX

Nduka starts with a refresher on Google's four golden signals and lands on a neat observation: every one of them is user experience in engineering clothes. Latency is a laggy page. Errors are a broken action. Saturation is the slowdown before the outage.

Yet the signals are silent about people with disabilities. A fast, error-free site can still be unusable with a keyboard or a screen reader. Accessibility regressions usually surface weeks later through an audit, a bug report or a frustrated user, which is exactly the kind of late discovery the other four signals were invented to prevent.

## Accessibility can't be measured directly, but its indicators can

She's honest that accessibility is subjective. What you can measure are proxies, mostly anchored in WCAG (the W3C's Web Content Accessibility Guidelines):

- **Compliance percentage** against a set of WCAG checkpoints.
- **Quality scores** from tools like Lighthouse, ObservePoint or Siteimprove.
- **Error density**, issues normalised by page count, so a big site and a small one compare fairly.
- **Conformance levels** A, AA and AAA as milestones.

Each of those is a number you can emit on a schedule, which is all an observability pipeline needs.

## A daily axe-core run, stored and graphed

Her implementation is deliberately small. GitHub Actions runs axe-core against her personal three-page website every day, ships results to Graphite, and visualises them in Grafana Cloud. The general shape works with whatever you already run: collect with VictoriaMetrics agent, Prometheus or OpenTelemetry, store in a time series database, graph in Grafana.

The dashboard tracks total violations by page, violations over time, and violations by severity. The first run was humbling: most issues were serious, and most sat on the Works page (grey text on white was one culprit). After fixes, violations fell from 43 to 13, and the Works page line dropped from about 23 to under five. Without the time series, she pointed out, you'd never see that change, and you'd never see the next regression arrive either.

## No universal formula, but a required shape

Nduka declines to prescribe the fifth signal's exact definition, since organisations differ. Her rule is about form: whatever you choose "should have the same shape as the other four golden signals", a measurable rate tracked over time that warns you before a user does. A severity-weighted violation rate is one option; time to remediate, or the share of critical user flows that pass screen-reader tests, are others.

Her suggested next steps are modest: audit whether you get static reports or continuous data, try the pipeline on a small project, and share it with your team before scaling it.

## Who should watch

Frontend and platform engineers who already run Grafana and want a cheap, concrete first step on accessibility. It's an intro-level talk, and a clear one, presented while the speaker was openly under the weather. Accessibility specialists won't learn new WCAG material; the value is the observability framing.

## Related Conf42 talks

- [Michael McAllister on the four golden signals](https://www.conf42.com/Site_Reliability_Engineering_2022_Michael_McAllister_four_golden_signals_monitoring_health_service) (Conf42 SRE 2022): the original four, explained.
- [Taslan A. Graham on automated accessibility testing with Playwright and axe-core](https://www.conf42.com/JavaScript_2023_Taslan_A_Graham_web_accessibility_testing_playwrightjs_axecore) (Conf42 JavaScript 2023): the same scanner, wired into tests.
- [Erissa Duvall's Accessibility Testing 101](https://www.conf42.com/Kube_Native_2023_Erissa_Duvall_accessibility_testing_101) (Conf42 Kube Native 2023).

[Watch Victoria Nduka's talk](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals)

[Watch the talk on YouTube](https://youtu.be/EjywRDCvSnE).

## Watch the talk

[The Fifth Golden Signal: Making Accessibility Observable](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) at Conf42 Observability 2026.
