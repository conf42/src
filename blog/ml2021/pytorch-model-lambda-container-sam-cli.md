# Serving a PyTorch model from Lambda with the SAM CLI, and when not to

Conf42 Blog, 2021-07-29. https://www.conf42.com/blog/ml2021/pytorch-model-lambda-container-sam-cli

In short: Nicola Pietroluongo (AWS) at Conf42 Machine Learning 2021 on serving an ML model as a serverless API with Lambda container images and the AWS SAM CLI

Training the model is the part you planned for; hosting it is the part that eats the sprint. [Nicola Pietroluongo](https://www.conf42.com/Machine_Learning_2021_Nicola_Pietroluongo_Serverless_Deep_Learning), Senior Solutions Architect at AWS, used his Conf42 Machine Learning 2021 talk to show one short answer: package the model and its inference code as a container image, run it on AWS Lambda behind Amazon API Gateway, and let the AWS Serverless Application Model (SAM) CLI generate, test and deploy the lot without writing a line of infrastructure code. He also says plainly where this approach does not fit.

It is a compact, demo-driven talk: one slide of theory, then a terminal session from sam init to a curl request against the live endpoint.

## Why worry about serving at all?

He opens with the line from the 2015 Hidden Technical Debt in Machine Learning Systems paper by D. Sculley and colleagues. Nicola Pietroluongo said at Conf42 Machine Learning 2021 that "only a small fraction of real world machine learning systems is composed of the machine learning code." The rest is configuration, data collection and verification, resource management, monitoring and serving infrastructure. His question is how much of the serving part you can make someone else's problem: where to host predictions at scale, cost-effectively, and how to do it the easiest way.

## Where: Lambda with container images

The where is AWS Lambda, which had recently added support for functions packaged as container images. His slides list the reasons it matters for ML: the same container tooling for Lambda and everything else, images of up to 10 GB (big enough for many models plus their libraries), subsecond automatic scaling, high availability, 140 native service integrations and pay-per-use billing.

## How: a SAM template that does the wiring

The how is AWS SAM, an open source extension of CloudFormation for serverless apps. His template has three parts: the serverless transform, a function resource with an image package type and an API event (a POST to a classify_digit path), and metadata pointing at the Dockerfile, the build context and a tag. Globals set a 50-second timeout, 5,000 MB of memory and binary media types for PNG and JPEG. From those few lines, SAM creates the Lambda function, its execution policy, the API Gateway endpoint and the permissions between them.

The SAM CLI, available on Linux, Windows and macOS, covers the lifecycle: sam init for a preconfigured template, sam build, sam package, sam deploy and sam local for testing on your own machine with a Docker image that mimics Lambda's environment, timeouts and memory limits included.

## What does the demo do?

The terminal session, step by step:

1. **sam init.** Choose an AWS quick start template, image packaging rather than zip, the Python 3.8 base image, and from the ready-made scenarios (Hello World, PyTorch, scikit-learn, TensorFlow, XGBoost) the PyTorch machine learning inference API.
2. **Look around.** The generated project holds a sample model that recognises handwritten digits, the SAM template, a sample training script, a test event and, most importantly, a Dockerfile whose CMD points to a lambda_handler function in the app file. That handler does preprocessing, loads the model, runs inference and returns JSON.
3. **sam build** builds and tags the container locally.
4. **sam local invoke** with the event file, whose body is a base64-encoded image of a handwritten three. The prediction comes back: three.
5. **Create an ECR repository** with the AWS CLI (authenticate for temporary credentials, then create a repository named ml-demo) and copy its URI.
6. **sam deploy guided** asks for a stack name, region and image repository, warns that the API has no authorisation (fine for a demo, not for production), saves the answers to a config file so the next deploy is faster, pushes the image to ECR and creates the stack.

Then a curl POST of the same base64 three against the API Gateway endpoint from the stack output, and the right answer comes back from the cloud.

## When is serverless the wrong call?

This is the bit to remember. Validate the use case and set clear KPIs before you commit. The upside is zero administration, no paying for idle servers and continuous scaling. The downside is in his own conclusion. Nicola Pietroluongo said at Conf42 Machine Learning 2021 that "serverless machine learning solutions are more suited when performances are not a big concern and when you work with batch processing since everything runs independently in parallel."

So read the service quotas first (the 10 GB image cap is the obvious one) and keep testing your assumptions. Latency-critical inference at steady high traffic probably wants a dedicated endpoint; a model that gets called in bursts, or a batch job that fans out, may be a very good fit for Lambda. He positions SAM mainly as a way to prototype and experiment fast.

## Who should watch?

Data scientists who have a working model and no platform team, and backend engineers asked to put someone's PyTorch model behind an HTTP endpoint by Friday. If you already run SageMaker endpoints or KServe, the talk is a quick look at a cheaper option for spiky or batch workloads.

## Related Conf42 talks

- Aditya Lohia on [deploying ML solutions with low latency](https://www.conf42.com/Machine_Learning_2021_Aditya_Lohia_Deploying_ML_solutions_low_latency) at Conf42 Machine Learning 2021.
- Marianna Diachuk on [deploying ML models and what goes wrong](https://www.conf42.com/Machine_Learning_2021_Marianna_Diachuk_Deploying_machine_learning_models) at Conf42 Machine Learning 2021.
- Ron Lyle Dagdag on [ONNX for portable models](https://www.conf42.com/Machine_Learning_2021_Ron_Lyle_Dagdag_Leverage_Power_ONNX) at Conf42 Machine Learning 2021.

[Watch the talk on YouTube](https://youtu.be/REG33BGB3rk).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- AWS Serverless Application Model: [aws.amazon.com/serverless/sam](https://aws.amazon.com/serverless/sam/)
- AWS SAM CLI on GitHub: [github.com/aws/aws-sam-cli](https://github.com/aws/aws-sam-cli)

## Watch the talk

[Serverless Deep Learning](https://www.conf42.com/Machine_Learning_2021_Nicola_Pietroluongo_Serverless_Deep_Learning) at Conf42 Machine Learning 2021.
