# No dataset existed for Lebanese Sign Language, so they built one

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/lebanese-sign-language-mlops-no-dataset

In short: Layth Ayache (Achour Holding) at Conf42 MLOps 2026 on 40,000+ Lebanese Sign Language samples and the MLOps behind a model that can say it doesn't know.

There was no Lebanese Sign Language dataset to download, so Layth Ayache's team collected one: more than 40,000 samples, gathered with Deaf community members, volunteers and NGOs. At Conf42 MLOps 2026 on November 19, Layth, Senior AI Systems and Web Engineer and Technical Lead at Achour Holding, talks about the unglamorous MLOps underneath that work.

The abstract is short and pointed, and it names three things. Each one is a lesson that applies far beyond sign language.

## When the benchmark doesn't exist either

Most ML tutorials begin with a dataset and a leaderboard. For many languages, including many sign languages, neither exists. That changes the job. You are the data collector, the labeller, the benchmark author and the model builder, and there is nobody external to check your homework.

Building a dataset with the community it serves also matters for more than sample count. Collecting with Deaf community members and NGOs is how you get signs as they are actually used, rather than a stilted version produced for a camera.

## Reject bad landmark extractions before training sees them

The first MLOps lesson is a data quality gate. Sign recognition pipelines commonly extract landmarks (positions of hands, fingers and body points) from video, and the model learns from those. When extraction fails, for example on a blurry frame or an occluded hand, you get garbage coordinates that look like perfectly valid numbers.

Layth's team rejects bad landmark extractions before they reach training. It is the same principle as validating inputs at an API boundary: once bad data is inside the training set, it is very hard to find again.

## A model that is allowed to say "I don't know"

The second lesson is about behaviour at inference time. A sign recogniser that always returns its best guess will confidently mistranslate anything it has not seen. For an accessibility tool, a confident wrong answer is worse than an honest shrug.

So the models are allowed to abstain. That is a product decision as much as a modelling one, and it is one many teams skip because a model that sometimes refuses looks worse on a demo.

## Reading 98% without fooling yourself

The third lesson is the one every ML engineer should hear at least once a year. The team got a 98% internal result, and the talk is about how to read that number without fooling yourself.

Internal results are measured on data you collected, split in ways you chose. If the same signers appear in training and test sets, or the recording conditions are uniform, a high score can say more about the split than the model. With no external benchmark to compare against, that self-discipline is the only safeguard you have.

## Who should watch

Anyone building ML for a low-resource language, a niche domain, or any problem where you had to make your own dataset. Accessibility and assistive-tech engineers. And anyone who has celebrated a 98% before checking how the test set was built. This is a compact talk about practice, not a sign-language linguistics lecture.

## Related Conf42 talks

- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu, more on gating data before it reaches a model.
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz, on trusting the numbers your evaluation produces.
- [The Fifth Golden Signal: Making Accessibility Observable](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) by Victoria Nduka, accessibility treated as an engineering metric.

[Watch Layth Ayache's talk](https://www.conf42.com/MLOps_2026_Layth_Ayache_dataset_benchmark_sign) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[No Dataset, No Benchmark: MLOps for Lebanese Sign Language](https://www.conf42.com/MLOps_2026_Layth_Ayache_dataset_benchmark_sign) at Conf42 MLOps 2026.
