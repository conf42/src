# Sorting 8,000 conference photos with Rekognition, Lambda and $50

Conf42 Blog, 2025-05-07, updated 2026-11-09. https://www.conf42.com/blog/ml2025/serverless-photo-pipeline-8000-event-photos

In short: Dmytro Hlotenko at Conf42 Machine Learning 2025 on the serverless AWS pipeline that culled and edited 8,000 AWS Community Day DACH photos for about $50.

Every event photographer knows the real work starts after the event: thousands of frames, most of them blinks and blur. At Conf42 Machine Learning 2025, Dmytro Hlotenko, cloud architect at APA-IT, AWS Community Builder and AWS user group leader in Vienna, showed the serverless pipeline he built to cull and edit more than 8,000 photos from AWS Community Day DACH 2024. It cost about $50 to run and turned roughly 4,200 usable candidates over to the marketing team.

It is a personal project told by someone who is both a serious photographer and an AWS engineer, which is exactly why the details are good.

## Getting the files off the camera is half the architecture

Hlotenko shot the day on two Sony bodies at once, an Alpha 9 III and an Alpha 7 IV, in RAW. The first trick is the upload path. Sony cameras can push files over FTPS, a feature built for press photographers at sports events, so he pointed them at an AWS Transfer Family endpoint that writes straight into S3. From there it is standard event-driven plumbing: S3 events, EventBridge, SQS with a dead-letter queue, and two Step Functions workflows (one for processing, one for metadata).

One warning he gives with feeling: Transfer Family is not priced like a serverless service. Leaving the endpoint up cost him over $220 before he noticed. Turn it off when the shoot ends.

## Claude could not tell if eyes were open; Rekognition could

The selection logic copies his own cognitive process: is the main face sharp, are the eyes open, is the pose something anyone would post on LinkedIn. His first attempt handed that judgment to Claude 3.5 through Amazon Bedrock with a picture-editor prompt. It failed on the most basic check. People wearing glasses confused it, and it could not reliably tell open eyes from closed.

So he went back to Amazon Rekognition, which returns the boring numbers he actually needed: sharpness, exposure, face confidence, eyes-open scores. He ran his archive of past community-day and meetup photos through it, compared the scores of shots he had kept against shots he had rejected, and stored the resulting thresholds in DynamoDB for the processing Lambda to read. Speakers needed a higher sharpness bar than general crowd shots. No custom training was needed.

He also kept the Rekognition bill small: DetectFaces and DetectLabels for scoring, DetectModerationLabels as a secondary filter, no IndexFaces, jittered calls to stay under API limits, and burst sequences sent as a batch so four near-identical frames did not cost four full analyses.

## RAW editing in a Lambda beats Fargate here

Culling is only half the job; editing takes longer. Hlotenko wanted the highlight and shadow recovery that only 14-bit RAW files allow, since he shot speakers against bright slides without flash. No commercial editor he uses offered an API, so he wrote a Lambda around the open-source LibRaw library, through a Python wrapper, that reads Sony ARW files directly.

Two details stand out. The Lambda first pulls the small JPEG preview embedded in every RAW file, roughly 1,200 pixels wide, and sends that to Rekognition, which is enough to judge a face and much cheaper than the full frame. And at 1.5 GB of memory the Lambda outperformed a comparable container on Fargate, with the first processed image landing in about ten seconds. Claude Haiku on Bedrock does get a job after all: given the metadata and calibration weights, it suggests the editing strategy, and he was happy with its white balance and highlight decisions.

## The numbers

About 15 to 20 relaxed hours to build, against what he estimates as more than 60 hours of manual sorting and editing saved. Roughly $20 on Rekognition and $30 on Lambda, Step Functions, DynamoDB and Transfer Family for the day, which works out to under a cent per picture. Accepted and rejected shots land in separate buckets, because the machine can still be wrong and a human gets the last look.

## Who should watch

Anyone building event-driven pipelines on AWS who wants a real, small, end-to-end example with costs attached. Photographers who code will enjoy the RAW details. If you need a reason to keep a cheap, specialized vision API around instead of throwing a general LLM at every image task, this talk is a good one.

## Related talks

- [Dmytro Hlotenko's follow-up on going agentic on the same 8,000 photos](https://www.conf42.com/AI_Agents_2026_Dmytro_Hlotenko_serverless_photos_aws) at Conf42 AI Agents 2026
- [Samuel Baruffi on a generative AI solution with AWS serverless and Amazon Bedrock](https://www.conf42.com/Platform_Engineering_2024_Samuel_Baruffi_aws_serverless_amazon_bedrock) at Conf42 Platform Engineering 2024
- [Gunnar Grosch on chaos engineering for serverless with AWS FIS](https://www.conf42.com/Chaos_Engineering_2022_Gunnar_Grosch_serverless_aws_fault_injection_simulator) at Conf42 Chaos Engineering 2022

[Watch Dmytro Hlotenko's talk](https://www.conf42.com/Machine_Learning_2025_Dmytro_Hlotenko_photography_community_serverless)

[Watch the talk on YouTube](https://youtu.be/fcFS2Z7UEis).

## Watch the talk

[Reinventing Event Photography: How AWS AI and Serverless Transform Community Moments](https://www.conf42.com/Machine_Learning_2025_Dmytro_Hlotenko_photography_community_serverless) at Conf42 Machine Learning 2025.
