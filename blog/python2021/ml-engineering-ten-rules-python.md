# Ten rules for ML engineering, starting with the apples you can't count

Conf42 Blog, 2021-05-28. https://www.conf42.com/blog/python2021/ml-engineering-ten-rules-python

In short: Joshua Arvin Lat (NuWorks Interactive Labs) at Conf42 Python 2021 on ten practices for building ML systems in Python, from coding rules to SageMaker

Most ML projects don't fail on the model; they fail on everything around it. At Conf42 Python 2021, Joshua Arvin Lat, CTO of NuWorks Interactive Labs, AWS Machine Learning Hero and author of the Amazon SageMaker Cookbook, runs through ten practices for designing and building ML systems in Python, from team coding rules to transient training instances and least-privilege model loading.

The examples lean on AWS (SageMaker, Lambda, API Gateway, Fargate), and he says the concepts carry over to other platforms with similar services.

## Why can't you count the apples?

He opens with a game: count the apples on a slide in ten seconds. Eighteen is wrong, twenty is wrong; the answer is that you can't, because you can't see the apples under the top layer. The point is the first rule. Engineers get so focused on their tools that they forget what the business and the customer need, and sometimes the right answer is an existing AI service and ten lines of Python, or no code at all.

## Notebook code and production code are different jobs

Rule two is knowing when to write production-level Python. Exploration in a Jupyter notebook can break the rules; a Flask prediction endpoint that must answer in under a second can't. Rule three is about team standards, set before code review starts. His examples:

- **The 20-line rule**: a function or method past 20 lines gets split into sub-functions.
- **PEP 8**, or a similar guideline set.
- **Avoid try/except blocks** that swallow errors. His scenario: 10,000 transactions in, 9,950 records in the logs, and no way to find the missing 50.

"Having rules allow people and professionals in your team to have some sort of way to accomplish their work," Joshua Arvin Lat said at Conf42 Python 2021. Rule four follows: write testable code, functions you can poke at from a console, even if the team does no automated testing yet.

## When is a convenience library worth it?

Rule five is design patterns and metaprogramming, in the form of an in-house convenience library that wraps the SDKs, much like an ORM wraps SQL, so junior and mid-level engineers don't need the internals. His cost test is blunt: three weeks of library work on a four-week project is a bad trade; two days that speed up the next three weeks is a good one. Rule six is CI/CD for deployment packages, with a manual approval step where an engineering manager reviews results and clicks yes, plus the ability to roll back.

## Build from scratch or use a platform?

The longest section argues for frameworks and ML platforms over home-grown everything. His estimate: building a flexible training setup yourself takes two to three months, learning a platform two to three days, and the home-grown version still lacks a debugger and a model monitor. Custom code also brings custom errors that Stack Overflow can't answer.

He then lists deployment options, from most customisable to most managed: a model on an EC2 instance, in a container on EC2, a SageMaker built-in algorithm and endpoint in about ten lines (handy for a proof of concept), custom containers on SageMaker endpoints, Lambda calling a SageMaker endpoint, API Gateway mapping templates straight to SageMaker with no Lambda in between, Fargate, multi-model and multi-container endpoints, and A/B tests with production variants, for example an 80/20 traffic split between the old and new model. For an endpoint called four times a day, a model inside Lambda (scikit-learn, TensorFlow or Prophet, now also from container images) costs almost nothing.

He also flags model drift: models in production degrade over weeks or months, and a platform's model monitor helps catch it.

## Bias, explainability and tuning without writing the formulas

Rule seven uses SageMaker Clarify for bias metrics such as class imbalance, DPPL and treatment equality, in roughly 10 to 15 lines of code and about ten minutes of waiting, and SHAP values for explainability. His example: of four features, only two actually drive the prediction. Rule eight is automated hyperparameter optimisation, run in parallel in the cloud: many short training jobs at once, and the best model wins, even across model families (a custom Apache MXNet model against the built-in linear learner in a single tuning job).

## Transient instances and models that run code

Rule nine is cost: training instances that run for minutes and shut down, so fine-tuning a Hugging Face BERT model on an expensive instance costs minutes, not hours. Rule ten is security, process plus technology, with the principle of least privilege applied to resources as well as people. His sharpest example: some model libraries can run arbitrary code when loading a model from an untrusted source. Give the container that loads it admin rights and the malicious code gets admin rights too; limit the permissions and you limit the damage.

## Who should watch

ML engineers and data science leads moving from notebooks to systems, especially on AWS. It's a broad checklist rather than a single deep demo; each rule is a pointer to go read more.

## Related Conf42 talks

- Joshua Arvin Lat on [pragmatic ML and ML engineering with Amazon SageMaker](https://www.conf42.com/Machine_Learning_2021_Joshua_Arvin_Lat_Pragmatic_Machine_Learning_and_ML_Engineering_Amazon_SageMake) at Conf42 Machine Learning 2021.
- Tomas Fernandez on [MLOps from Jupyter to production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production).
- Noa Goldman's [hitchhiker's guide to MLOps](https://www.conf42.com/Machine_Learning_2023_Noa_Goldman_hitchhiker_guide_mlops_experience).

[Watch Joshua Arvin Lat's talk](https://www.conf42.com/Python_2021_Joshua_Arvin_Lat_machine_learning_ai__engineering__metaprogramming__deep_learning_data_s) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From NuWorks Interactive Labs

NuWorks Interactive Labs is the technology company where Joshua Arvin Lat serves as CTO.

- NuWorks Interactive Labs: [ecommerce.nuworks.ph](https://ecommerce.nuworks.ph)

[Watch the talk on YouTube](https://youtu.be/KM00eyKDVs4).

## Watch the talk

[Machine Learning Engineering Done Right: Designing and Building Complex Intelligent Systems and Workflows with Python](https://www.conf42.com/Python_2021_Joshua_Arvin_Lat_machine_learning_ai__engineering__metaprogramming__deep_learning_data_s) at Conf42 Python 2021.
