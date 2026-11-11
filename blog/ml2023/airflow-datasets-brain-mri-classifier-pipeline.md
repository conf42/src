# An Airflow ML pipeline that wakes up when an MRI lands in S3

Conf42 Blog, 2023-05-18. https://www.conf42.com/blog/ml2023/airflow-datasets-brain-mri-classifier-pipeline

In short: Tamara Janina Fingerlin (Astronomer) at Conf42 Machine Learning 2023 on orchestrating data and ML in one Airflow pipeline, from S3 to a fine-tuned ResNet-50.

The slow step in most ML pipelines is the human who copies a file or kicks off the next script. At Conf42 Machine Learning 2023, Tamara Janina Fingerlin, Developer Advocate at Astronomer, built a pipeline with none of those: drop a new brain MRI slice into S3 and Apache Airflow ingests it, records it in DuckDB, fine-tunes a Hugging Face classifier, tests it against a baseline, picks the best model and messages Slack, with each stage triggered by data rather than a clock.

It's a feature tour as much as an ML talk, given by someone who works on Airflow at Astronomer, and the code is public on GitHub as a blueprint. Tamara used to work in neurosurgery, which explains the dataset and the honest disclaimer at the end.

## What is ML orchestration, and why Airflow?

Tamara places ML orchestration where MLOps (machine learning, DevOps and data engineering) overlaps with orchestration: a tool on top of the stack that tells every other tool what to do and when. Airflow is the open source choice she makes the case for, at 12 million downloads a month. Pipelines (DAGs) are plain Python, so they get CI/CD, and the tool is agnostic: anything with an API can be a task, which matters when a new ML tool appears every morning.

The crash course is short. A dag decorator on a function makes a DAG; a task decorator on any Python function, your existing training script included, makes it a task. Operators are prebuilt classes for specific tools, so the API calls happen out of sight.

## How do you schedule on data instead of cron?

Most of the eight DAGs in her project run on Airflow Datasets. A task that updates something, a folder in S3 or a model file, declares it as an outlet; when the task succeeds, it raises a flag across the environment, and any DAG scheduled on that dataset (or a combination) starts. New training data triggers preprocessing; a newly trained model triggers testing.

Two DAGs use the continuous schedule, new in Airflow 2.6 a couple of weeks before the talk: they rerun as soon as they finish, so they're always listening. They wait for new files with S3KeySensorAsync, a deferrable operator that hands the wait to the separate triggerer process and frees the worker slot. "If you have sensors running, always check if there's an asynchronous version," Tamara Janina Fingerlin said at Conf42 Machine Learning 2023.

## Which other Airflow features carry the pipeline?

**Dynamic task mapping.** Copying new files creates one mapped task instance per file at runtime, around 400 in her run, so she can trace exactly which file failed without writing code for a number of files she can't predict.

**Pools as a lock.** DuckDB can't take two writers at once, so every task that writes to it shares an Airflow pool with a single slot. Parallelism problem solved, without touching the database.

**The Astro Python SDK.** Tool-agnostic helpers: a file-list function that moves from S3 to Azure blob storage by changing a connection ID, a SQL transform decorator that runs a query against DuckDB today and Snowflake tomorrow, and a dataframe decorator that turns the resulting table into pandas to pick the best model.

**Custom operators.** Fine-tuning and testing a Hugging Face binary image classifier are wrapped in her own operators: inherit from BaseOperator, define the parameters, put the work in execute. The DAG file stays clean, and the same test operator scores both the baseline and the fine-tuned model.

**Slack callbacks.** An on-success callback posts each test result. One message reported an average test loss of zero alongside worse-than-baseline accuracy, which sent her back to fix the hyperparameters.

## How did the model do?

The data was a small Kaggle set of T2-weighted MRI slices of gliomas and meningiomas, a little over 300 of each, split roughly three to one: 260 gliomas and 247 meningiomas for training, around 80 of each for testing. The model was Microsoft's ResNet-50 from Hugging Face. Out of the box it was about as good as a coin flip: accuracy 0.482, F1 0.360, AUC 0.472. Fine-tuned for 30 epochs, about an hour on her laptop, it reached accuracy 0.845, F1 0.845 and AUC 0.844.

Then the disclaimer, from someone who worked clinically. "Was this clinically useful? Absolutely not," she said: a radiologist reads the whole MRI, never one slice, and diagnosis waits for the biopsy. Her plausible use case is triage, such as flagging small lung CT lesions for a second look.

## Who should watch

Data and ML engineers who run training scripts by hand or on cron and want them chained to the data that feeds them. Next steps she suggests: map hyperparameters with dynamic tasks, push GPU-heavy tasks to the Kubernetes executor or KubernetesPodOperator, and swap DuckDB for a database that takes parallel writes. The demo uses the Astro CLI, which runs Astro Runtime, nearly identical to open source Airflow.

Related talks: [Aliaksandr Sheliutsin on getting more out of Airflow pipelines](https://www.conf42.com/DevOps_2024_Aliaksandr_Sheliutsin_leverage_airflow_pipelines), [Noa Goldman's hitchhiker's guide to MLOps](https://www.conf42.com/Machine_Learning_2023_Noa_Goldman_hitchhiker_guide_mlops_experience) from the same event, and [Tomas Fernandez on taking Jupyter to production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production).

[Watch Tamara Janina Fingerlin's talk](https://www.conf42.com/Machine_Learning_2023_Tamara_Janina_Fingerlin_orchestrating_workflows_apache_airflow) from [Conf42 Machine Learning 2023](https://www.conf42.com/ml2023).

## From Astronomer

The pipeline in the talk is on GitHub at [TJaniF/airflow-ml-pipeline-image-classification](https://github.com/TJaniF/airflow-ml-pipeline-image-classification). It uses the open source Astro Python SDK and Astro CLI, and Tamara points to Astronomer's resources on Airflow with MLflow, Weights & Biases and SageMaker.

- Astronomer: [astronomer.io](https://www.astronomer.io/)

[Watch the talk on YouTube](https://youtu.be/wzA310fy0u8).

## Watch the talk

[Orchestrating data and ML workflows with Apache Airflow](https://www.conf42.com/Machine_Learning_2023_Tamara_Janina_Fingerlin_orchestrating_workflows_apache_airflow) at Conf42 Machine Learning 2023.
