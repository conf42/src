# Twenty models on a service built for one, and other deployment lessons

Conf42 Blog, 2021-07-28. https://www.conf42.com/blog/ml2021/ml-deployment-mistakes-twenty-models-one-service

In short: Marianna Diachuk (Restream) at Conf42 Machine Learning 2021 on five ML deployment mistakes: scaling, solo ownership, silos, no tests and no monitoring

Her first prediction service was built around exactly one model. She ended up deploying more than 20 on it. [Marianna Diachuk](https://www.conf42.com/Machine_Learning_2021_Marianna_Diachuk_Deploying_machine_learning_models), Data Scientist at Restream, used her Conf42 Machine Learning 2021 talk to tell five stories of deployment going wrong, mostly from early in her career at a startup, and the lesson each one cost her. The short version: training and deploying need different mindsets, and data science code needs more tests than ordinary software, not fewer.

It is a talk about practice and teams, not tools: no framework comparisons, no code, just failure modes you will recognise.

## Why is deploying a model a different job from training one?

Training is the part data scientists know: gather data, explore it, engineer features, train, tune, evaluate. It is a researcher's mindset, where you keep improving the model and can inspect any intermediate state in a Jupyter notebook whenever you like.

Deployment flips the goal. You are preserving the model, not improving it: the same input must give the same prediction score every time. And a new set of concerns arrives that research never forced on you: infrastructure and load, integration with the rest of the system, code quality, tests and logging. She points out that many data scientists come from applied maths rather than software engineering, and notebook habits (no logging, because you can just look) do not survive production.

## What goes wrong when you skip planning for scale?

Story one is the 20 models. A startup, tight deadlines, investors in the office, a first project that has to prove itself fast. She and a teammate built a prediction service around a single model, with no thought for a second one. Marianna Diachuk said at Conf42 Machine Learning 2021: "But in reality, I think I deployed more than 20 models using that prediction service and trying to scale that."

It was inefficient and it held the team back, and eventually they threw it away and rebuilt from scratch, while keeping every production model consistent through the migration. Her lessons: plan deployment thoroughly and ask more experienced engineers for help with the architecture; assume you will scale, because even one model means new versions and retraining; and the time spent fixing it now is cheaper than the time it will cost later.

## What happens when one person owns production?

Story two is the vacation. As a new team lead and self-described perfectionist, she kept the deployment service to herself, sure nobody would maintain it as well. Then she spent a holiday in Barcelona in work chats, trying to help the team debug production issues they had never seen, because she had never let them near the service. Lesson: delegate, share deployment services across the team, and remember you are a human being who gets sick and goes on holiday. A team where tasks are synchronised works like a clock even when you are out.

## Why does the backend team need to be in your plan?

Story three is the last night before a three-month roadmap deadline, with data scientists and backend engineers sitting together finishing work nobody had scheduled. The model was one component in a system: the backend sent requests, the model service responded, the backend processed the responses. Nobody had told the backend team they had tasks. Afterwards she always created a Jira task for planning with backend engineers. The broader lesson is to include QA, DevOps and backend people in planning, and to explain what data science work actually is to the whole company, so other teams come to you instead of you chasing them.

## Do data scientists really need tests?

Story four: the prediction service shipped with zero tests. Then a new category appeared in a categorical feature the models had never seen, and things broke. Then a feature that had no missing values in training started arriving with them, and the model returned nothing at all. Each time it meant debugging in production, with no tests and no logs.

Her conclusion turns the usual assumption around. She said that "software engineering doesn't require as much tests as data scientists do," because data science code works on data whose state keeps changing: every feature calculation needs checking, and so does the distribution of the data over time. It is also simply easier to write tests than to fix bugs in production.

## What does no monitoring cost you?

Story five: she checked model metrics only on request. When performance dropped, she wondered whether to change the features or the model, until she learned about data shift. Users changed the order they bought products in, and the model degraded without throwing a single error. She has also seen large companies run models unmonitored for years and fix them only when clients complained.

Her lesson: the model's lifecycle continues after deployment. As she put it, "The model doesn't die when you deploy it. It doesn't cease to exist." Tests can all pass while the model quietly gets worse, so you need monitoring of data and prediction score distributions to catch the logical errors tests miss, and to answer the business when it asks why. Her slides end with the best line of the talk: in production no one can hear you scream.

## Who should watch?

Data scientists about to ship their first model, especially at a startup, and leads building their first ML team. Experienced MLOps engineers will know every lesson already; they may still enjoy the stories.

## Related Conf42 talks

- Karl Weinmeister on [10 things that go wrong with ML projects](https://www.conf42.com/Machine_Learning_2021_Karl_Weinmeister_10_Things_That_Go_Wrong_with_ML_Projects) at Conf42 Machine Learning 2021.
- Hila Fox on [monitoring AI pipelines' output as a product](https://www.conf42.com/Machine_Learning_2021_Hila_Fox_Monitoring_AI_Pipelines_Output_As_Product) at Conf42 Machine Learning 2021.
- Wojtek Kuberski on [detecting silent failures in ML models](https://www.conf42.com/Machine_Learning_2022_Wojtek_Kuberski_detect_silent_failures_ml_models) at Conf42 Machine Learning 2022.

[Watch the talk on YouTube](https://youtu.be/uuj6FO0yo1E).

## From Restream

- Restream, the multistreaming platform where Marianna works: [restre.am](https://restre.am/59bA)

## Watch the talk

[Deploying ML models and all the things that go wrong](https://www.conf42.com/Machine_Learning_2021_Marianna_Diachuk_Deploying_machine_learning_models) at Conf42 Machine Learning 2021.
