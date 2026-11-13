# A serverless photo pipeline where thresholds became evidence

Conf42 Blog, 2026-08-29, updated 2026-11-09. https://www.conf42.com/blog/agents2026/photo-pipeline-thresholds-to-agents

In short: Dmytro Hlotenko of Sage at Conf42 AI Agents 2026 rebuilds his 8,000-photo AWS culling pipeline with Strands agents, a blind critic and Step Functions up front.

A hardcoded threshold that rejects a frame for scoring 74 against a cutoff of 80 tells nobody why. At Conf42 AI Agents 2026, Dmytro Hlotenko, Senior Cloud Ops Engineer at Sage and an AWS Community Builder, showed how he kept the fast part of his serverless photo-culling pipeline and replaced every guess in it with an agent that has to argue its case.

It is the sequel to a talk that has travelled through several community events: a pipeline that took 8,000 photos he shot at an AWS Community Day in 2024 and narrowed them to a selection of 1,249, cutting days of manual work to about 40 minutes.

## Version one: his taste, frozen into weights

The original build is a nice piece of AWS plumbing. Dmytro's Sony cameras upload straight over FTP to AWS Transfer Family, an idea he picked up watching press photographers at the Austrian Press Agency. S3 events go to SQS with a dead letter queue, Step Functions orchestrates Lambdas that use LibRaw to work with raw files, Amazon Rekognition scores faces (eyes, mouth, head position), and EXIF data plus correction JSON from DxO PhotoLab feeds a golden set in a Parquet file. A single Claude call looked at 20 similar frames and picked development parameters.

It worked in the conference room. Then he pointed it at Formula 1 archives and studio work, and it threw away nearly everything, because nothing in it knew how to judge a car. In his own diagnosis there were seven holes: one-shot calls, tools welded into code, memory frozen into JSON, no observability, metrics that were just his taste, and fully manual delivery. Rejections were silent. So: Terraform destroy.

## Keep the express line, add a press agency

Version two, sketched on a flight to Abu Dhabi while reading about Strands Agents, does not throw out the old pipeline. Transfer Family, SQS and Step Functions stay as an express line that rejects obvious technical failures in milliseconds, because you don't buy a Ferrari to drive round the building at 20 km/h. The weights still exist, but they now decide how much volume reaches the agents instead of issuing the verdict.

Behind that sit five agents on Amazon Bedrock AgentCore, all built from the same skeleton and differing in only three things: model, skill and tool set. The old Lambdas, Rekognition, LibRaw and ExifTool became MCP tools behind the AgentCore Gateway.

- **Curator** looks at the frame in context. The frame that scored 74 becomes a dark stage that is expected at a conference, a readable face, sharp eyes, accept.
- **Processor** develops the raw file, measures the histogram and highlight clipping, and iterates. In his trace, the first pass showed 12% clipping and the agent adjusted recovery and measured again on the next pass, with Step Functions capping timeouts and reasoning budget.
- **Critic** is blind: it sees the final image and the rubric, never the other agents' reasoning, and decides publish, rework or escalate to a human.
- **Caption** agent sorts photos to sessions using EXIF timestamps, the schedule and a face collection, and marks conflicts as unverified instead of guessing.
- **Feedback** agent compares Dmytro's final picks with what the system decided and proposes skill changes, which arrive as pull requests he reviews.

He picked Strands over Bedrock Agents (configuration, not code) and LangChain (too much abstraction), and he talks openly about mixing models from Claude to Kimi, Nova Lite and NVIDIA Nemotron by cost and job. Skills came from dictating his reasoning over example photos, then deep research into how well-known photographers select.

## What it cost, and what it bought

Dmytro is honest about the trade. Latency per stage went from about a second to 20 to 50 seconds. Costs rose, and determinism is gone. In exchange, accuracy on his archives moved from roughly 80 to 90% to over 95%, every rejection now carries a written motive, and the production run for a conference came to about $50. The metadata the agents leave behind even feeds a Glue, Athena and QuickSight dashboard about the mood of the event.

## Who should watch

Anyone with a mature Step Functions or Lambda workflow that silently encodes one engineer's judgment as numbers. The lesson travels well past photography: find the box that is a guess, keep the deterministic parts where they are fast and right, and make the agent leave evidence. As the abstract puts it, "Last year I automated my hands. This year, my judgment."

## Related Conf42 talks

- [Serverless Workflow Orchestration on AWS](https://www.conf42.com/DevOps_2025_Bharat_Vishal_Tiwary_aws_serverless_workflow) by Bharat Vishal Tiwary at Conf42 DevOps 2025.
- [From PoC to Production: Shipping Enterprise AI Agents with Amazon Bedrock AgentCore](https://www.conf42.com/Remix_2026_Samuel_Baruffi_poc_bedrock_agentcore) by Samuel Baruffi at Conf42 Remix 2026.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev at Conf42 Large Language Models 2026.

[Watch Dmytro Hlotenko's talk](https://www.conf42.com/AI_Agents_2026_Dmytro_Hlotenko_serverless_photos_aws) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/Nbi4urdt7_c).

## Watch the talk

[My Step Functions DAG Was a Lie: Going Agentic on 8,000 Photos](https://www.conf42.com/AI_Agents_2026_Dmytro_Hlotenko_serverless_photos_aws) at Conf42 AI Agents 2026.
