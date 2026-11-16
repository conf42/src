# A/B testing is the data science skill that compounds a career

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/ab-testing-skills-that-grow-data-science-careers

In short: Bhavana Reddy Chadagonda (Intuit) at Conf42 Kube Native 2025 on experiment designs, CUPED variance reduction and the platform behind trustworthy A/B tests.

The fastest way to make a data scientist indispensable is to make them the person who can say whether a launch actually worked. At Conf42 Kube Native 2025, Bhavana Reddy Chadagonda, Staff Data Scientist at Intuit, laid out a field guide to experimentation: which design to pick, how CUPED cuts the sample size you need, the pitfalls that fake a win, and how all of it turns into career progression.

It is part statistics primer, part career talk, with a short section on the cloud-native platform that makes experiments cheap to run. The statistics stay at the level of intuition and business framing; she points to existing resources for the maths.

## Business constraints pick the design, not the other way round

Bhavana walks through the menu. Classic between-subjects A/B tests for feature releases and UI changes. Multivariate and factorial tests when you want interaction effects. Holdouts for effects that take weeks to show up. Switchback experiments that rotate treatment over time, the approach marketplaces like DoorDash, Uber and Lyft use because users on both sides of the market contaminate each other. Geo experiments when user-level randomisation would spill over.

When true randomisation isn't possible, she names the credible fallbacks: difference-in-differences, interrupted time series and synthetic control. The point running through this section is judgement. Knowing when to deviate from pure randomisation is the skill, and it is exactly what interviewers probe.

## Halve the variance, halve the sample

The most practical part of the talk is variance reduction. Required sample size is proportional to variance, so if you cut variance in half you need roughly half the users, which means faster decisions and more experiments per quarter.

She groups the techniques into five buckets: regression adjustment with pre-period covariates (the umbrella CUPED sits under), balanced assignment through blocking or stratification, metric engineering such as per-user aggregation, capping outliers and log transforms, cluster-aware estimation for geo and switchback tests, and the operational hygiene of counting only truly exposed users with event definitions frozen before launch.

CUPED gets a worked example: a test of whether runners are slower with weights attached. Each runner's mile time is already explained largely by how fast they were before the experiment, so adjusting by their baseline strips out the noise and leaves the effect of the weights. Her best practices are the ones people skip: pick covariates highly correlated with the outcome, use only data from before the experiment, and feel free to use more than one.

## If it looks too good, check the plumbing

The pitfalls section is a good pre-launch checklist. Sample ratio mismatch and logging gaps. Randomising on one unit and analysing on another, which inflates variance. Interference between treatment and control. Peeking without adjusting the false positive rate. Metric drift and seasonality. Her rule: if something seems too good to be true, it probably is, so check these before you celebrate.

## The career ladder, spelled out

Bhavana closes with a concrete IC ladder for experimentation specialists. Entry level means solid fundamentals, clean hypotheses, reproducible analysis and clear writing. Mid level means leading multiple tests, mentoring, sequential and Bayesian methods, and standard guardrails. Senior means setting experimentation strategy and partnering with engineering on the platform. Staff and principal shape the system: platform roadmaps, open source contributions and teaching the organisation to learn faster.

The portfolio advice is practical: document real scenarios end to end from hypothesis to recommendation, contribute to statistical libraries, and show iteration instead of one-and-done tests.

## Who should watch

Analysts and early-career data scientists planning their next step, engineers building feature-flag or experimentation platforms who want to know what the statisticians need, and product managers tired of arguing from opinion. Experienced experimenters will know most of it, though the variance-reduction taxonomy is a handy reference.

## Related Conf42 talks

- [A/B testing platform at scale](https://www.conf42.com/Chaos_Engineering_2023_Riteek_Srivastava_ab_testing_platform_at_scale) goes deeper on the platform layer Bhavana sketches.
- [The Art & Science of AB Test Development](https://www.conf42.com/JavaScript_2021_Bill_Coloe_Art_Science_AB_Test_Development) covers the front-end engineering of tests.

[Watch Bhavana Reddy Chadagonda's talk](https://www.conf42.com/Kube_Native_2025_Bhavana_Reddy_Chadagonda_abtesting_experimentation_careers)

[Watch the talk on YouTube](https://youtu.be/TF6Jff_D9UQ).

## Watch the talk

[Data Science Careers via A/B Testing: Scalable Experimentation in Cloud-Native Era](https://www.conf42.com/Kube_Native_2025_Bhavana_Reddy_Chadagonda_abtesting_experimentation_careers) at Conf42 Kube Native 2025.
