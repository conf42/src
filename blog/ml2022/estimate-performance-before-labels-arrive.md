# Your loan model's labels arrive in a year, so estimate its accuracy now

Conf42 Blog, 2022-05-19. https://www.conf42.com/blog/ml2022/estimate-performance-before-labels-arrive

In short: Wojtek Kuberski (NannyML) at Conf42 Machine Learning 2022 on catching silent model failures by estimating performance without ground truth

A model that predicts loan defaults within one year gets its first real labels a year after it starts making decisions. Wojtek Kuberski, Co-Founder of NannyML, used his Conf42 Machine Learning 2022 talk to explain what to do in the meantime: estimate the model's performance from its own calibrated confidence, and only then go hunting for the drift that explains a drop.

It is a compact introduction to ML monitoring, built around one running example and two algorithms from NannyML's open source library.

## Data drift or concept drift: which one should scare you?

Kuberski starts from the basics. There is a true pattern in reality, you sample a dataset from it, and your model approximates the pattern. Two things can then go wrong.

Data drift is a change in how the data is sampled: the joint distribution of model inputs, P(x), moves, but the mapping from inputs to target stays put. It may or may not hurt. If the data moves from one region where the model does well to another where it does equally well, nothing breaks.

Concept drift is a change in the pattern itself, P(y|x). The inputs can look identical while the class boundary moves, and then the model has learned something that is no longer true.

"Data drift does not always lead to drop in performance, whereas concept drift tends to almost always lead to drop in performance," Wojtek Kuberski said at Conf42 Machine Learning 2022.

## Why not just alert on drift?

Because with many features, data shifts constantly, and per-feature drift alerts multiply until nobody reads them. Kuberski argues for watching performance directly instead: it is what the model was optimised for in training (ROC AUC in his loan example), and it is the best technical proxy for business impact.

The catch is that you rarely have the ground truth to calculate it. He gives three reasons:

- **Delayed labels.** The loan model runs blind for a year, mispricing loans the whole time if something has gone wrong.
- **Incomplete labels.** You learn whether approved customers paid. You never learn whether the rejected ones would have.
- **Automation use cases.** If a model replaces humans classifying documents, getting full ground truth would defeat the point. Spot-checking 1% with a human helps, but it doesn't give you the full picture.

## How do you estimate performance without targets?

The algorithm he outlines, part of the NannyML library, works from the model's confidence. First, check that the scores really are probabilities, and calibrate them if not, so that a score of 0.6 means a 60% chance of the positive class. Then performance becomes a function of uncertainty. Picture the training data as butterfly wings, each wing a confident cluster of one class, the body the uncertain boundary. If drift pushes production data from the wings towards the body, the model itself expects to do worse. Those calibrated probabilities convert into an expected confusion matrix, and from there into almost any metric: accuracy, precision and so on.

His demo uses the California housing dataset from scikit-learn, turned into a classification problem with a simple model (a random forest, he thinks). The estimated ROC AUC tracks the real one closely.

Note the scope: this estimates the impact of data drift. Pure concept drift, by definition, doesn't show up in the inputs.

## Then find out why

Once estimated performance drops, you go back to the data. Univariate drift detection, feature by feature with the Kolmogorov-Smirnov test or chi-squared, is the most interpretable, but it has two problems: hundreds of features produce a pile of false positives, and it misses subtler changes such as a shift in the correlation between features.

For those, NannyML uses data reconstruction. Fit a dimensionality reduction such as PCA on reference data (keeping, say, 95% of the variance), compress, apply the inverse transform, and measure the mean Euclidean distance between original and reconstructed points. That gives a single reconstruction error to track. A rise means the learned structure no longer fits the data; a fall is rarer but still drift. UMAP or a variational autoencoder work too; a plain autoencoder doesn't, because its latent space doesn't map stably back to the original space.

His toy example is the convincing bit: two datasets whose x and y distributions look the same, so the univariate tests stay silent, while the reconstruction error jumps because the internal structure has changed.

## Who should watch

Anyone running classifiers whose labels arrive late or never, and anyone whose drift dashboard is a wall of red nobody acts on. It is intuition rather than code, so pair it with the library docs if you want to try it.

## Related Conf42 talks

- Hila Fox on [monitoring AI pipelines and treating output as a product](https://www.conf42.com/Machine_Learning_2021_Hila_Fox_Monitoring_AI_Pipelines_Output_As_Product) at Conf42 Machine Learning 2021.
- Sudarshan Kasera on [monitoring drift in models](https://www.conf42.com/Machine_Learning_2026_Sudarshan_Kasera_monitoring_drift_models) at Conf42 Machine Learning 2026.

[Watch Wojtek Kuberski's talk](https://www.conf42.com/Machine_Learning_2022_Wojtek_Kuberski_detect_silent_failures_ml_models)

## From NannyML

The performance estimation and multivariate drift detection shown in the talk ship in NannyML's open source Python library, installable with pip.

- NannyML on GitHub: [github.com/NannyML/nannyml](https://github.com/NannyML/nannyml)
- NannyML documentation: [docs.nannyml.com](https://docs.nannyml.com/)
- NannyML website: [nannyml.com](https://www.nannyml.com)

[Watch the talk on YouTube](https://youtu.be/UUZmYlTdG2A).

## Watch the talk

[How to detect silent failures in ML models](https://www.conf42.com/Machine_Learning_2022_Wojtek_Kuberski_detect_silent_failures_ml_models) at Conf42 Machine Learning 2022.
