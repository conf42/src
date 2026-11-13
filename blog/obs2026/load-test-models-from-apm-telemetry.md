# Build load-test models from APM data, not planning-meeting guesses

Conf42 Blog, 2026-09-06, updated 2026-11-09. https://www.conf42.com/blog/obs2026/load-test-models-from-apm-telemetry

In short: Vasuki Uday Kiran Vudathala of ServiceNow at Conf42 Observability 2026 derives peak RPS, concurrency and scenario mix from production telemetry.

Load tests rarely fail because the tool is weak; they fail because the workload model was a guess. At Conf42 Observability 2026, Vasuki Uday Kiran Vudathala, Staff Performance Engineer at ServiceNow, showed a six-query method that derives every number in a peak-readiness test from APM telemetry you already collect. His one-line summary: "Peak readiness should be computed, not negotiated."

## A green test on the wrong workload is the dangerous outcome

The familiar ritual: a few weeks before Black Friday or a launch, people sit in a room and agree on round numbers for concurrent users because round numbers feel safe. The test passes. The real peak arrives in a different shape, say browse-heavy instead of checkout-heavy, or a one-minute spike hidden inside an hourly average, and the system falls over anyway.

Vudathala's framing is that a failing test is a gift: it tells you to fix something. A passing test on the wrong model hands you false confidence with a check mark on it. He estimated the manual process at thirteen to twenty-four hours across two to four people, versus under five minutes for one engineer with automation, and was quick to add that speed is the bonus. Traceability is the point.

## Six queries, from a year down to one minute

The method treats observability data as a workload specification. He demonstrated it in New Relic's NRQL and pointed out Dynatrace DQL or anything exposing transaction and session telemetry works the same way.

1. **Peak day.** Count transactions per day over the season, with sessions, response time and errors.
2. **Peak hour.** Bucket that day by hour with p95 latency. This tells you whether the peak is a plateau or a spike, which sets the test duration.
3. **Peak minute.** A one-minute time series to find the worst sixty seconds. In his example that came to about 82 requests per second.
4. **Scenario mix.** What users actually did in the peak hour, cross-checked by transaction volume, top routes and funnel. Homepage-to-browse was 28 percent; checkout-to-payment only 6.
5. **Concurrency.** Average sessions times average session duration in seconds, divided by 3,600.
6. **Session population.** Distinct sessions in the hour, kept separate from concurrency.

His sharpest technical point sits in step three: don't size from an average. Infrastructure fails on the worst minute, not the mean one. He also flagged the boring traps: filter bots and synthetic traffic, watch for sampling, lock the time zone across queries, and on single-page apps use browser interaction events rather than page views.

## Two numbers people mix up

Steps five and six are where teams get burned. In his example, 529 users were active at once, while 4,280 distinct sessions passed through the hour. The first drives how many virtual users hammer the system; the second sizes your test data pool. Configure 4,280 virtual users and you run a test about eight times heavier than reality and spend a week fixing a problem that only exists in the test.

Growth gets the same discipline. Observed peaks come from data; growth multipliers come from your own year-over-year trend (1.2 to 1.3 for 20 to 30 percent growth, more for a big campaign), with a separate safety buffer. Each multiplier stays visible, so anyone can see which part was observed and which was assumed.

## Test the unhappy paths, then check yourself

Session telemetry also shows where journeys drop off, at discovery, at the cart, at payment. Each drop-off is its own scenario, often hitting the weakest part of the stack. In his words: "If you only test the happy paths, we are testing the demos, not our users."

After the real peak, rerun the same queries and compare against the model. That closes the loop and hands you next year's real growth number. He wrapped the method in a Java and Spring Boot tool, the Peak Workload Analyzer, which outputs a dashboard and a JSON report for your load tool, with New Relic and Dynatrace examples.

## Who should watch

Performance engineers, SREs and anyone who has sat in a peak-planning meeting and wondered where the numbers came from. If you don't have session-level APM data yet, the talk doubles as an argument for collecting it.

## Related Conf42 talks

- [Peter De Tender on Azure Load Testing in action](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Peter_De_Tender_azure_load_testing) (Conf42 SRE 2025): somewhere to run the model.
- [Kaye Alvarado on load testing from multiple clients with a pipeline](https://www.conf42.com/DevOps_2024_Kaye_Alvarado_loadtesting_pipeline) (Conf42 DevOps 2024).
- [Adelina Simion and Andy Kuszyk on load testing with F1](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1) (Conf42 Golang 2022).

[Watch Vasuki Uday Kiran Vudathala's talk](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning)

[Watch the talk on YouTube](https://youtu.be/lhZltcdXe6s).

## Watch the talk

[Automating peak readiness: turning observability signals into workload engineering insights](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning) at Conf42 Observability 2026.
