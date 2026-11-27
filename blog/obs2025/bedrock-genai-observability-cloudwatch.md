# Probabilistic apps need observability you switch on yourself

Conf42 Blog, 2025-05-06, updated 2026-11-09. https://www.conf42.com/blog/obs2025/bedrock-genai-observability-cloudwatch

In short: AWS Serverless Hero Hazel Saenz of Caylent shows at Conf42 Observability 2025 how to measure Bedrock-backed serverless apps with CloudWatch and X-Ray.

Send the same prompt to a model a hundred times and you may get a hundred different answers. At Conf42 Observability 2025, Hazel Andrea Saenz Giron, Cloud Software Architect at Caylent and an AWS Serverless Hero from Guatemala, built her talk on that fact: generative AI apps are probabilistic, so the only way to keep quality, speed and cost in balance is to measure every interaction. Her demo shows how to do that on AWS with Amazon Bedrock, Lambda, CloudWatch and X-Ray, including the bit nobody tells you: Bedrock's model invocation logging is off until you turn it on.

## Deterministic habits break on probabilistic systems

Saenz starts with a story every GenAI tinkerer knows: the ad shows a perfect image, your attempt has a character with three mouths. The reason is architectural. Banking and e-commerce systems she built before were deterministic, a pile of ifs where the same input gives the same output. A model returns the most probable answer, which may not be the one this user wanted, and each model behaves differently because it was trained on different data. So model choice becomes a business variable, not a detail.

From there she defines three objectives that pull against each other: quality (no three-mouthed characters), performance (users leave slow apps) and cost (models are expensive, and not every task needs the smartest one).

## The building blocks of a GenAI app

The talk maps a GenAI application into layers: a foundation model hub (your own models or ones reached through the Bedrock API), a data foundation (RAG, fed from ETL jobs, Confluence, Jira, GitHub, PDFs, CSVs, APIs and databases, landing in a Bedrock knowledge base), model adaptation and prompting, GenAI ops for deployment and versioning, integration with existing apps, and governance with a control plan. Bedrock Guardrails sits in the data path to keep sensitive customer data out of answers.

Observability is the thread through all of it. Her argument is that decisions like switching models, rewriting prompts or fixing the data have to be made on numbers, and observability is where the numbers come from.

## Four layers, in this order

Saenz proposes an incremental path:

1. **Component metrics**: invocation errors, latency and utilisation for the infrastructure.
2. **Model metrics and traces**: what happened between the user's request and the answer, step by step.
3. **Guardrail metrics**: how many users tried to pull sensitive data or probe for information they shouldn't get.
4. **User feedback**: the thumbs up, thumbs down signal that tells you whether a different answer each time is a good answer.

## The demo: tokens are your cost meter

The demo uses a small music-expert API from her GitHub repo that you can deploy into your own account. After enabling Bedrock invocation logging to CloudWatch (or an S3 bucket), each request shows which model ran, the question, the answer and the tokens used. Tokens are the useful part: send the same request to two models and you can compare cost and latency directly. X-Ray traces on the Lambda then split total duration from the time spent waiting on the model, so you know whether to tune your code or your model choice.

## Who should watch

Developers on AWS moving a GenAI prototype towards production, and SREs who've inherited one. It's an approachable talk, more about building the right habits than about advanced tracing. If you already instrument LLM calls with OpenTelemetry, the four-layer ordering is still a handy checklist for what you're missing.

## Related Conf42 talks

- Suraj Muraleedharan on [Operational excellence for your LLMs using Amazon Bedrock](https://www.conf42.com/Large_Language_Models_LLMs_2024_Suraj_Muraleedharan_amazon_bedrock_operational).
- Mohamed Najaaf on [Responsible AI with Amazon Bedrock Guardrails](https://www.conf42.com/Machine_Learning_2025_Mohamed_Najaaf_guardrails_responsible_bedrock), the third layer in more detail.
- Hazel Saenz herself on [hexagonal architecture in serverless applications](https://www.conf42.com/Python_2024_Hazel_Andrea_Saenz_Giron_resilient_applications_serverless).

[Watch Hazel Saenz's talk](https://www.conf42.com/Observability_2025_Hazel_Andrea_Saenz_Giron_serverless_bedrock_generative)

[Watch the talk on YouTube](https://youtu.be/rX8yI3FRGYs).

## Watch the talk

[Measuring the Performance of Serverless Applications with Generative Models in Amazon Bedrock](https://www.conf42.com/Observability_2025_Hazel_Andrea_Saenz_Giron_serverless_bedrock_generative) at Conf42 Observability 2025.
