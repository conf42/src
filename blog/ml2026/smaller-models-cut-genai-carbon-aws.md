# The greenest GenAI request is the one served by a smaller model

Conf42 Blog, 2026-02-16, updated 2026-11-09. https://www.conf42.com/blog/ml2026/smaller-models-cut-genai-carbon-aws

In short: Mohamed Najaaf (AWS) at Conf42 Machine Learning 2026 on cutting GenAI's energy use with right-sized models, cheap customisation, efficient silicon and monitoring.

You probably do not need the biggest model on the leaderboard, and your electricity bill and carbon footprint both know it. At Conf42 Machine Learning 2026, Mohamed Najaaf, Solutions Architect at Amazon Web Services, walked through the design choices that shrink the energy cost of generative AI applications, from model selection and customisation to silicon and observability.

To be clear about scope: this is an AWS talk, and the tools and figures are AWS's. The decision order it teaches transfers to any cloud.

## The demand curve is the motivation

Najaaf opens with published research from firms including Deloitte, Gartner and Goldman Sachs: model training size has grown enormously over the last decade, data centre electricity demand climbs steeply from 2022 on, and he cites a Goldman Sachs forecast that about 60% of that new demand would be met by burning fossil fuels, plus a World Economic Forum estimate that the compute needed for AI doubles roughly every hundred days. Whatever your view of the exact numbers, the direction is not in dispute.

## Start with managed services and the right-sized model

The first two levers are architectural. He recommends managed or serverless services (Amazon Bedrock for foundation models behind one API, SageMaker, EKS) so the provider carries the hardware, networking and patching, and AWS's position is that moving workloads off premises into its data centres can cut their carbon footprint by up to 99%.

The more portable lever is model selection. Evaluate against your real criteria (language support, open or proprietary, size, generalist or domain-specific) and pick the lightest model that passes. His example: a use case might not need Claude Opus 4.6 when Claude Haiku 4.5 does the job, and the smaller model is both cheaper and needs fewer resources per inference. Bedrock Evaluations can score candidates on helpfulness, faithfulness, correctness, harmfulness and refusal, plus your own metrics, and you redo it as new model versions ship.

## Customise from the cheap end of the ladder

Najaaf orders customisation by energy cost. Prompt engineering is the cheapest and should come first. Retrieval-augmented generation adds your own data through a vector store. Parameter-efficient fine-tuning touches a subset of weights, full fine-tuning touches all of them, and training from scratch is the most expensive and carbon-heavy option, which few organisations need.

That ladder is a good default for any team: climb only as far as the evaluation results force you.

## Silicon, compression and watching the meters

For training, he points to AWS Trainium, which he says is up to 25% more energy efficient than comparable EC2 instances, with Trainium2 about three times more efficient than the first generation and Trainium3 (announced too late for the slides) about four times better again. For inference that does not need a GPU, Graviton is quoted at up to 60% less energy.

Deployment optimisations do the rest: model compilation for the target hardware, compression and pruning, and distillation, where a large teacher model trains a small student to handle most queries with close to the same quality.

Finally, observability. CloudWatch for Bedrock metrics and guardrails, SageMaker Profiler and the AWS Neuron monitor for training, and NVIDIA's System Management Interface on GPU hosts. Sustainability, in his framing, is a loop: monitor, re-evaluate models as they change, and adjust.

## Who should watch

Teams building on Bedrock or SageMaker who want a checklist that lowers cost and energy at the same time, and architects who need a structured argument for "use the smaller model" in the next design review. If you are not on AWS, the model selection and customisation sections still apply as is.

## Related Conf42 talks

- [Green DevOps: Building Sustainable Software](https://www.conf42.com/DevOps_2024_Neel_Shah_green_sustainable_software) by Neel Shah (Internauts Infotech) widens the lens to the whole delivery pipeline.
- [Energy-Efficient and Cost-Optimized Serverless Computing: Strategies, Challenges, and Future Directions](https://www.conf42.com/Cloud_Native_2025_Neetu_Gangwani_costoptimized_serverless) by Neetu Gangwani (UBS) digs into the serverless side of the same argument.
- [Green Code: Transforming DevOps for a Sustainable Future](https://www.conf42.com/DevSecOps_2024_Clifton_Reddy_green_code_sustainable) by Clifton Reddy (American National) brings it down to the code.

[Watch Mohamed Najaaf's talk](https://www.conf42.com/Machine_Learning_2026_Mohamed_Najaaf_recommendation_ranking_systems)

[Watch the talk on YouTube](https://youtu.be/iKuTx_0EtAk).

## Watch the talk

[Building GenAI That Doesn't Cost the Earth](https://www.conf42.com/Machine_Learning_2026_Mohamed_Najaaf_recommendation_ranking_systems) at Conf42 Machine Learning 2026.
