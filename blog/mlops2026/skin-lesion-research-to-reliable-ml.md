# An AUC of 0.96 that missed more than half the real cases

Conf42 Blog, 2026-11-10, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/skin-lesion-research-to-reliable-ml

In short: Deborah Adedigba (UK Ministry of Defence) at Conf42 MLOps 2026 on what her skin lesion classifier taught her about metrics, validation and negative results.

Two of Deborah Adedigba's skin lesion models scored a precision around 0.95 and an AUC of 0.96 on smartphone photos, with a recall of 0.44. They were usually right when they flagged something, and they missed more than half of the real cases. At Conf42 MLOps 2026, the Data Scientist at the UK Ministry of Defence uses her own MSc dissertation and the journal paper that followed as a case study in the question she wishes she had asked earlier: when a model scores well, what do you need to see before anyone relies on it?

The stakes explain the choice of metric. Citing Globocan, she puts melanoma at around 325,000 new cases and 57,000 deaths a year. Caught early, five-year survival is around 99 percent. Caught after it has spread, around 27 percent. A screening model that misses cases is failing at the one job it has.

## No model won on both datasets

The project compared a custom CNN against transfer learning with ResNet50, VGG16, EfficientNet and Inception-ResNet-V2, built in TensorFlow and Keras on Google Colab and Kaggle GPUs. She used two datasets on purpose: dermoscopic images from ISIC, magnified and fairly standardised, and smartphone photographs with six lesion classes, where image quality and size vary. Melanoma, the target, had just 52 images in the second set.

On dermoscopic images EfficientNet led with about 0.85 accuracy and an AUC of 0.9, ResNet and VGG16 sat around 0.75, and the custom CNN's AUC was 0.52, which she calls a coin flip. On smartphone photos the order changed: ResNet50 was best at around 0.75 accuracy and EfficientNet dropped to 0.61. Had she tested on one dataset, she says, she would have drawn the wrong conclusion about which model to use.

And then the recall. The headline numbers looked fine while the screening failure sat underneath. Her conclusion is that reliable ML needs a set of metrics chosen for the risk, and a single number can hide exactly the failure you care about.

## Two things broke, and both were worth reporting

The first was unstable training. Loss jumped around and accuracy was poor, so she tried undersampling the large classes to fix the imbalance. It backfired: accuracy fell from around 54.7 percent to somewhere between 24 and 40 percent. What turned it around was augmentation, standardised preprocessing, a lower learning rate and SMOTE to synthesise examples of rare classes. She only knew which change did what because she was tracking metrics per experiment.

The second was U-Net. The idea was to segment the lesion so the classifier would ignore hair, rulers and surrounding skin. It did not help, possibly because segmentation removed context the model was using, and she took it out. Her lesson: "every stage should prove its value", and a negative result belongs in the write-up.

## The dissertation's numbers were a hypothesis

She is direct about how far the first results can be trusted. One train and test split, no cross-validation, no external test set, and SMOTE applied before the split, so there was a chance of leakage. None of that makes the work worthless, she says. It makes the result a hypothesis.

The follow-up paper fixed the process. Stratified five-fold cross-validation with repeated seeds. A class-weighted loss so mistakes on rare cases cost more. Accuracy replaced by macro F1 and the Matthews correlation coefficient, which stay honest on skewed data. Augmentation applied to training data only. McNemar's test to check whether two models make different errors, plus an ablation study. Saved weights and out-of-fold predictions instead of results copied by hand. Explanations moved from saliency maps fed into the model to Grad-CAM and Grad-CAM++ heat maps, adapted for CNNs and transformers, to catch a model staring at a ruler.

The ensemble in that paper reached a macro F1 of 0.998. She still does not oversell it, because the external test set is still missing and the heat maps were not validated against a dermatologist. "internally consistent, not independently validated", Deborah Adedigba said at Conf42 MLOps 2026, adding that the paper says so too.

## Five questions before a model goes near users

Her takeaway list is short. Can I rebuild this result from versioned data and code? Is evaluation independent of training data? Do I know where it fails and for whom? Will I know when it degrades? Can a clinician, or whichever expert applies, see why it predicted what it did?

## Who should watch

Data scientists and ML engineers moving from notebooks to anything with consequences, and students about to write up a dissertation with one impressive number in it. It is an honest research retrospective. The model never left a Streamlit demo, so do not expect serving, monitoring or CI detail, and the talk's datasets and figures differ somewhat from the abstract. The before-and-after of the evaluation method is the reason to watch.

## Related Conf42 talks

- [When Bad Data Reaches the Model: Engineering Data Quality Into MLOps at Healthcare Scale](https://www.conf42.com/MLOps_2026_Saiteja_Jonnalagadda_healthcare_quality_data) by Saiteja Jonnalagadda of CVS Health at Conf42 MLOps 2026.
- [MLOps at Scale: Designing Governed AI Pipelines for Healthcare Impact](https://www.conf42.com/MLOps_2025_Nikitha_Edulakanti_mlops_scale_designing) by Nikitha Edulakanti of Fresenius Medical Care at Conf42 MLOps 2025.
- [From Benchmarks to Business Impact: Evaluating Generative AI in Production](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) by Srikanth Devarakonda of Adobe at Conf42 Observability 2026.

[Watch Deborah Adedigba's talk](https://www.conf42.com/MLOps_2026_Deborah_Adedigba_skin_lesion_classification) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Research to Reliable ML: Lessons from a Deep Learning Pipeline for Skin Lesion Classification](https://www.conf42.com/MLOps_2026_Deborah_Adedigba_skin_lesion_classification) at Conf42 MLOps 2026.
