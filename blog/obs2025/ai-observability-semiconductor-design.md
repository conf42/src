# Chip design gets the observability treatment, in seven layers

Conf42 Blog, 2025-05-11, updated 2026-11-09. https://www.conf42.com/blog/obs2025/ai-observability-semiconductor-design

In short: Naveen Desai of Marvell Technology sketches at Conf42 Observability 2025 how AI-driven monitoring could shorten semiconductor design cycles.

Observability usually means pods, queries and p99s. At Conf42 Observability 2025, Naveen Desai, Principal Engineer at Marvell Technology, pointed the same idea at chip development: instrument the design flow, the simulations, the fab and even the chips in the field, then let AI find the patterns. His headline claim is that AI-driven observability can cut semiconductor design cycles by up to 40%. Fair warning: this is a lightning-length overview of a few minutes, a map of the territory rather than a walkthrough of any one technique.

## The problem is schedule, not curiosity

Desai opens with the pain: in his figures, 87% of semiconductor projects run late and over budget, often by several million dollars. In an industry where a slipped tape-out pushes back a product launch, that hits time to market, profitability and how fast the next generation arrives. The pitch for observability here is business-first: faster launches, lower operating cost, and chips that perform better once deployed.

The abstract adds a 22% yield improvement to the 40% cycle-time figure. The talk presents both as the potential of the approach rather than results from a single named project.

## Seven places to put the sensors

The core of the talk is a list of seven areas where monitoring plus AI applies:

1. **Design automation monitoring**: real-time feedback during design so issues surface early, with workloads optimised dynamically for compute efficiency.
2. **Predictive telemetry**: pattern recognition over multidimensional sensor data to detect critical design anomalies and reduce physical testing.
3. **Automated design rule verification**: tools that keep learning from complex design patterns, flagging errors and suggesting context-aware fixes.
4. **Performance and power optimisation**: adaptive frequency scaling and proactive thermal management, which low-power designs live or die by.
5. **Simulation with digital twins**: near-complete test coverage across electrical, thermal and mechanical domains.
6. **Yield optimisation**: manufacturing telemetry across more than a hundred process parameters, with ML spotting defect patterns.
7. **Edge device performance**: telemetry from deployed chips under real-world conditions, used to tune ML performance and battery life.

For software observability people, the shape is familiar. Items 1 to 3 are shift-left testing, item 5 is staging, item 6 is production metrics, and item 7 is real user monitoring for silicon.

## Roll it out like any other platform

The implementation roadmap is three phases: an assessment with gap analysis and measurable KPIs, an integration phase that brings in observability tools with minimal workflow disruption and team training, and an optimisation phase where AI insights refine processes, feed predictive models and spread knowledge across product lines. Desai closes by calling AI-powered observability practical today, not a future concept.

## Who should watch

Engineers in or near hardware (EDA, verification, test, product engineering) who want a compact framing for where AI monitoring fits in their flow, and software observability folks curious how their ideas travel to silicon. If you want implementation detail, pair it with one of the deeper hardware talks below; this one is the table of contents.

## Related Conf42 talks

- Jena Abraham on [Machine Learning Innovations in Hardware Verification for High-Speed Protocol Testing](https://www.conf42.com/Machine_Learning_2025_Jena_Abraham_hardware_verification_innovations), item 3 in depth.
- Ramalinga Reddy Kotapati on [power efficiency in semiconductor design with backside power delivery](https://www.conf42.com/Golang_2025_Ramalinga_Reddy_Kotapati_semiconductor_power_efficiency).
- Vinoth Manamala on [AI-Powered Digital Twins: Revolutionary Patterns for Smart Manufacturing](https://www.conf42.com/Cloud_Native_2025_Vinoth_Manamala_digital_twins_manufacturing).

[Watch Naveen Desai's talk](https://www.conf42.com/Observability_2025_Naveen_Desai_design_semiconductor_40)

[Watch the talk on YouTube](https://youtu.be/_Txiw4hr3pQ).

## Watch the talk

[AI-Powered Observability in Semiconductor Design: Achieving Real-Time Insights and 40% Faster Design Cycles Through Advanced Monitoring and Analytics](https://www.conf42.com/Observability_2025_Naveen_Desai_design_semiconductor_40) at Conf42 Observability 2025.
