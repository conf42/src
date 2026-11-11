# Greenfield labeling buys volume, brownfield labeling buys quality

Conf42 Blog, 2022-05-20. https://www.conf42.com/blog/ml2022/greenfield-volume-brownfield-label-quality

In short: Johannes Hotter (Kern) at Conf42 Machine Learning 2022 on weak supervision for new labeling projects and confident learning to find label errors in old ones

Labeling data from scratch and fixing the labels you already have are different jobs, and they call for different tools. At Conf42 Machine Learning 2022, Johannes Hotter, Co-Founder and CEO of [Kern.ai](https://www.kern.ai/), borrowed greenfield and brownfield from IT projects: greenfield labeling takes you from raw data to a working proof of concept (0 to 90%, in his slides) with weak supervision and smart manual sampling, brownfield labeling takes an existing training set from 90 to 95% by hunting down the errors with confident learning.

It's a dense, well-structured talk on data-centric ML, drawing on research at the Hasso Plattner Institute and three years of consulting on AI projects. No product demo; the Kern part is a mention at the end.

## Why is starting from scratch so hard?

A classifier or extractor needs labeled data, say insurance emails tagged with the issue they describe. The two classic options both hurt. Crowd labeling scales globally but struggles with knowledge-intensive or privacy-sensitive tasks. In-house experts have the domain knowledge but don't scale, which makes them expensive and a bottleneck. Hence the push to automate.

## Weak supervision: many wrong-ish heuristics, one better label

Weak supervision combines heuristics that are each imperfect: right 70 or 80% of the time, and only for a subset of records. Run every heuristic over every record, get a matrix of noisy labels, and let a weak supervision algorithm (a family of them, not a single one) synthesise a probabilistic label. The simplest is a majority vote; better ones weigh each heuristic's precision, coverage and conflicts.

The heuristics can be almost anything: a few-line Python labeling function (a headline starting with a digit is clickbait), distant supervision via lookup values, active learning modules trained on what you labeled by hand, zero-shot classifiers from Hugging Face where you supply only label names, inexperienced labelers such as crowd workers or interns, and legacy or third-party systems.

## If you can label automatically, why train a model?

His comparison is useful. Labeling builds an artifact: runtime doesn't matter (run it overnight), it can use data that won't exist at inference time, and it aims for high confidence rather than full coverage. Inference runs in milliseconds and must predict for every record. And a model trained on weakly supervised labels tends to generalise beyond the heuristics.

## Manual labeling still matters, just differently

"Even in greenfield labeling, manual labeling still matters a lot," Johannes Hotter said at Conf42 Machine Learning 2022.

You need it to explore the data, to have reference data that tells you how good your automation is, to measure human performance and subjectivity, and to come up with new heuristics. Each need has a sampling strategy. Random sampling for reference data. Labeling records others have labeled, for inter-annotator agreement. Neural search over embeddings from pretrained transformers for exploration, two ways: diversity sampling, which keeps picking the record most distant from what's already labeled and so surfaces the outliers your deployed model will meet; and clustering, picking a few representative points per cluster so the labels you spend cover the data.

## Brownfield: estimate how wrong your labels are

Real training sets are messy, even well-known public datasets contain mislabeled examples, and relabeling everything isn't an option. Confident learning uses a trained model's predicted probabilities to estimate the joint distribution of true and noisy labels. In his worked example the diagonal sums to 0.75 and the rest to 0.25, so roughly a quarter of the labels may be wrong. Turn the predictions into confidence scores, sort ascending, and review the first 25%: that's where the label errors cluster.

Weak supervision also makes the heuristics debuggable. Filter for records the clickbait function fires on, see where it's wrong, and tighten it to require positive sentiment as well; in his slides precision rises from 83% to 92% while coverage drops from 2.5% to 1.8%. Comparing heuristics with each labeler's annotations exposes bias, for example when one colleague's labels agree with a heuristic at 95% precision and another's at 75%, a sign the two read the label differently.

He ends with open questions: if training data is an integral part of an ML application, how should it be documented and maintained, and will labeling shift from single tasks to broader enrichment of the data?

## Who should watch

ML engineers and data scientists stuck between a pile of unlabeled text and a labeling budget, and teams whose model has plateaued on a training set nobody has audited. The reading list is worth the visit alone: Ratner et al. on data programming (from the founders of Snorkel), Northcutt et al. on confident learning, and open-source vector databases such as Qdrant.

Related Conf42 talks: Rajeshwari Sah on [labeling and annotation quality](https://www.conf42.com/Machine_Learning_2026_Rajeshwari_Sah_labeling_annotation_quality), Aditi Ramaswamy and Anisha Biswaray on [not wasting your data](https://www.conf42.com/Machine_Learning_2022_Aditi_Ramaswamy_Anisha_Biswaray_dont_waste_data), and Wojtek Kuberski on [detecting silent failures in ML models](https://www.conf42.com/Machine_Learning_2022_Wojtek_Kuberski_detect_silent_failures_ml_models), both from the same event.

[Watch Johannes Hotter's talk](https://www.conf42.com/Machine_Learning_2022_Johannes_Hotter_greenfield_brownfield_data_labeling) from [Conf42 Machine Learning 2022](https://www.conf42.com/ml2022).

## From Kern.ai

At the time of the talk Kern.ai was open-sourcing toolkits for data-centric AI that integrate the techniques above, and its team's research on a labeling environment for large-scale, high-quality training data was due at NLDB 2022.

- Kern.ai: [kern.ai](https://www.kern.ai/)

[Watch the talk on YouTube](https://youtu.be/tA6wNYTj0dA).

## Watch the talk

[Greenfield vs. Brownfield Data Labeling to improve AI performance](https://www.conf42.com/Machine_Learning_2022_Johannes_Hotter_greenfield_brownfield_data_labeling) at Conf42 Machine Learning 2022.
