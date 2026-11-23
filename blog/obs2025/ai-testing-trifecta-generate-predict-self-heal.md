# Generate, predict, self-heal - AI's three jobs in testing

Conf42 Blog, 2025-06-04, updated 2026-11-09. https://www.conf42.com/blog/obs2025/ai-testing-trifecta-generate-predict-self-heal

In short: Jyotheeswara Reddy Gottam of Walmart Global Tech at Conf42 Observability 2025 on generative tests, predictive risk analytics and self-healing automation.

Jyotheeswara Reddy Gottam of Walmart Global Tech, who has worked in development and quality engineering for more than 13 years, used his Conf42 Observability 2025 talk to make a case for combining three AI techniques in QA: generative test creation, predictive analytics that point testing at risky code, and self-healing automation that repairs tests when the UI changes. His claim is that the three together do more than any one of them alone.

It is a compact, strategy-level talk. If you want to see a specific tool in action, this is not that; if you need a structure for pitching AI-assisted testing to your organisation, it is.

## The three costs of traditional testing

Jyotheeswara starts with what goes wrong today. Manual test scripting eats engineering time and leaves coverage gaps. Defect detection is reactive, so critical issues reach production, where a P1 damages customer trust and revenue. And automation suites carry a maintenance tax: scripts break with UI changes, and false positives drain both time and confidence in the suite. Everyone who has babysat a flaky end-to-end test knows the third one personally.

## One technique per problem

His "AI testing triangle" pairs each problem with a technique:

- **Generative AI** writes test scripts and finds edge cases human testers often miss, turning days of script writing into minutes and keeping quality consistent across suites rather than only where the experts sit.
- **Predictive analytics** uses historical data, such as where P1 bugs clustered, to flag high-risk modules before deployment and send testing effort there.
- **Self-healing frameworks** detect UI changes that break tests, update the scripts and verify the fix without manual work.

He also shared improvement figures across healthcare, fintech and e-commerce, including test creation time down by about 70% and maintenance hours down sharply. Treat them as the speaker's reported results rather than a benchmark; the talk does not break down the underlying projects.

## Integrate in stages

The implementation advice is the part most teams can use directly. Start with standalone tools and test each AI component on its own. Move to partial integration with limited scope to build confidence. Only then connect everything into one feedback loop where components share data. On the tooling side, he suggests REST APIs between tools, embedding them in CI/CD pipelines, a central metrics store such as Elasticsearch, and unified dashboards in Grafana, Splunk or similar.

His roadmap follows the same shape: pick tools and set baseline metrics, pilot individual components against control groups, connect the feedback loops, then scale across teams and document what worked.

## Keep a human with the veto

The governance section keeps the talk grounded. Jyotheeswara asks for transparency (documented, explainable test generation and auditable predictions), regular validation against human experts, continuous retraining with confidence scores, and QA leads keeping final authority with override capability on every automated action. His closing point: AI should enhance human testers, not replace them.

## Who should watch

QA leads, test automation engineers and engineering managers weighing where AI fits in their testing budget. The connection to observability is the metrics loop: predictive testing runs on the same historical defect and quality data observability teams already collect.

## Related Conf42 talks

- Mike Morgan's [Tackling Flaky Tests](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies), the problem self-healing frameworks aim at.
- Liran Yushinsky's [Who Judges the AI Agent?](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) on testing non-deterministic, AI-generated code.
- Vitali Shchur's [The QA Ownership Mindset](https://www.conf42.com/Chaos_Engineering_2025_Vitali_Shchur_qa_mindset_startup) for the human side of quality.

[Watch Jyotheeswara Reddy Gottam's talk](https://www.conf42.com/Observability_2025_Jyotheeswara_Reddy_Gottam_ai_metrics_testing)

[Watch the talk on YouTube](https://youtu.be/187lGEp3LK4).

## Watch the talk

[The Triple Threat: How AI Technologies Reduce Testing Costs While Improving Quality Metrics](https://www.conf42.com/Observability_2025_Jyotheeswara_Reddy_Gottam_ai_metrics_testing) at Conf42 Observability 2025.
