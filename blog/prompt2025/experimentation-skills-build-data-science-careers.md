# Experiment design, not dashboards, is the data science career moat

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/experimentation-skills-build-data-science-careers

In short: Bhavana Reddy Chadagonda at Conf42 Prompt Engineering 2025 on picking experiment designs, CUPED variance reduction, A/B testing LLM prompts and career growth.

To find out whether weights slow runners down, don't compare raw mile times; compare each runner to their own baseline. That small example carries much of Bhavana Reddy Chadagonda's talk at Conf42 Prompt Engineering 2025. Bhavana, an independent researcher with over a decade designing and scaling experimentation, argued that experiment design (picking the right method, cutting variance, avoiding the classic traps) is one of the most valuable skills in data science, and now essential for evaluating prompts and LLMs.

She pitches it as a field guide: part methods, part platform, part career advice. The statistics stay practical and the career section is unusually specific.

## Let constraints pick the design

Bhavana's rule is that business constraints choose the experiment design, not the other way round. Her menu: classic A/B tests for features and UI changes; multivariate and factorial designs to learn interaction effects; holdout studies for long-term and network effects that build over weeks or months. When traffic patterns complicate things, switchback experiments rotate the same unit through both variants over time, which suits marketplaces and two-sided platforms. Geo experiments randomise by region when user-level randomisation would spill over.

When randomisation isn't possible at all, she walks through the credible alternatives: difference-in-differences, interrupted time series (look for a level or slope break exactly at the intervention), and synthetic control (build a weighted virtual twin of the treated city or state from untreated ones).

## Statistics as business skills

Rather than re-teach p-values, she ties each concept to why a business should care. Hypothesis testing forces clear success criteria before launch. Communicating uncertainty honestly builds trust, because leaders expect ranges and risk, not perfection. Effect size and power keep you on changes that matter. Multiple-testing discipline protects against false wins when a company runs many experiments a month. Sequential methods support faster, adaptive learning.

## Cut variance, ship faster

The most practical section is variance reduction. Sample size scales with variance, so halving variance roughly halves the sample you need and the time you wait. Her toolkit: regression adjustment with pre-period covariates (the umbrella for CUPED); blocking or stratification at assignment; metric engineering such as winsorising outliers and log-transforming skewed metrics; cluster-aware analysis for geo and switchback tests; and exposure hygiene, counting only eligible, actually exposed users and freezing event definitions before launch.

CUPED gets the runner example. Experiment mile time is driven largely by how fast each runner already was, so using baseline mile time from before the experiment strips out that explainable variance and isolates the effect of the weights. Her best practices: pick covariates highly correlated with the metric, use more than one if they help, make sure they come strictly from before the experiment, and impute missing values. She also points to CUPAC, which swaps the regression for a machine learning model that predicts the baseline.

## Experiments for prompts and models

The section that earns the event slot applies all of this to LLMs: comparing prompt templates, few-shot examples and system instructions; benchmarking models or fine-tuned versions; testing RAG retrieval strategies, chunking and ranking; measuring personalisation; and systematically probing for harmful outputs, bias and hallucination. Online, that means A/B, multivariate or contextual bandits; offline, automated frameworks, synthetic data and LLM-as-judge for faster iteration.

Her warning list is worth pinning up: sample ratio mismatch, logging gaps, a unit of randomisation that differs from the unit of analysis, interference between groups, peeking, metric drift and seasonality. If it seems too good to be true, it probably is.

## The career map

She closes with a portfolio plan (document realistic experiments end to end, contribute to libraries such as statsmodels or PyMC, show business impact) and an IC ladder from solid A/B fundamentals at entry level to shaping the experimentation platform and roadmap at staff level.

## Who should watch

Analysts and data scientists who want to specialise, engineers building experiment-ready systems, and anyone A/B testing prompts with more enthusiasm than statistics. Seasoned experimentation leads will find the methods familiar but the career framing useful for mentoring.

## Related Conf42 talks

- [A/B testing platform at scale](https://www.conf42.com/Chaos_Engineering_2023_Riteek_Srivastava_ab_testing_platform_at_scale) by Riteek Srivastava at Conf42 Chaos Engineering 2023, for the platform side.
- [AI-Driven Testing for Conversational AI: LLM-as-Judge, Generative QA, and Scalable Automation](https://www.conf42.com/Prompt_Engineering_2025_Yash_Panjari_testing_conversational_automation) by Yash Panjari at Conf42 Prompt Engineering 2025.
- [Fast Confidence Estimation for Classification and Regression models](https://www.conf42.com/Machine_Learning_2025_Andrei_Stroganov_Andrei_Visochan_estimation_regression_confidence) by Andrei Stroganov and Andrei Visochan at Conf42 Machine Learning 2025.

[Watch Bhavana Reddy Chadagonda's talk](https://www.conf42.com/Prompt_Engineering_2025_Bhavana_Reddy_Chadagonda_science_testing_experimentation) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/uvS2gARo31k).

## Watch the talk

[Designing Data Science Careers Through A/B Testing and Experimentation Mastery](https://www.conf42.com/Prompt_Engineering_2025_Bhavana_Reddy_Chadagonda_science_testing_experimentation) at Conf42 Prompt Engineering 2025.
