# A SageMaker notebook a bank will sign off, built from guardrails

Conf42 Blog, 2021-07-30. https://www.conf42.com/blog/ml2021/sagemaker-guardrails-regulated-ml-environment

In short: Suraj Muraleedharan (AWS) at Conf42 Machine Learning 2021 on private-VPC SageMaker, Service Catalog products and SCP guardrails for regulated ML teams

Data scientists in a bank want a notebook now; the security office wants that notebook to never see the internet. [Suraj Muraleedharan](https://www.conf42.com/Machine_Learning_2021_Suraj_Muraleedharan_ML_environment_regulatory_customers), Senior DevOps Consultant in AWS Professional Services, showed at Conf42 Machine Learning 2021 how to give both sides what they want: Amazon SageMaker in a private VPC with no internet route, guardrails baked into AWS Service Catalog products that app teams launch themselves, and service control policies that make an unencrypted training job fail at the API.

It is an AWS reference architecture talk aimed at banking, insurance, life sciences, healthcare and energy customers, with CloudFormation and SageMaker SDK snippets rather than a live demo.

## What did regulated customers actually ask for?

A way for business data scientists to train on highly sensitive customer and company data, with security as priority number one. He turns that into four requirements:

- **No internet connectivity.** The accounts run private VPCs only.
- **Self service.** Large enterprises have a cloud engineering team owning the platform, but if every notebook goes through them, they become the bottleneck. App teams need to provision ML resources on their own.
- **Centralised governance.** The security office and platform team still decide which guardrails apply.
- **Observability** of the whole thing.

## What does the architecture look like?

A multi-account layout under AWS Organizations: an application account where team Alpha works; a security account, managed by the security office, collecting CloudTrail logs and VPC flow logs; a networking account holding a shared transit gateway to corporate data centres; and a shared services account with AWS CodeArtifact acting as a PyPI mirror.

In the application account, a VPC with three private subnets holds the network interfaces for SageMaker notebooks and Studio. The notebooks themselves live in a SageMaker service account you never see. Every call to AWS services (ECR, S3, STS, KMS, CodeArtifact, the SageMaker API and runtime) goes through VPC endpoints with private DNS. The security group allows only port 443, and only within the VPC's CIDR.

The PyPI mirror answers the obvious complaint. No internet means no pip install from the public index, so CodeArtifact pulls from upstream PyPI into a domain shared across teams, and the platform team controls which packages land there.

## How do you stop a team from launching an open notebook?

That is the core problem, and he states it plainly. Suraj Muraleedharan said at Conf42 Machine Learning 2021: "if I give the application team complete access on provisioning a notebook as per their liking, they can also provision a notebook without using the given VPC".

AWS Service Catalog is the answer. The central team writes a CloudFormation template for a notebook, which becomes a product inside a portfolio. The template hard-codes what matters: direct internet access disabled, root access disabled, a customer managed KMS key for encryption, the VPC's subnets and security groups imported from the network stack, an optional CodeCommit repository. Launch constraints decide which roles may launch it. App teams pick the product and pass parameters such as volume size (one team wants 50 GB, another 25 GB), but cannot remove the guardrails. Studio gets the same treatment with its network access type set to VPC only.

The console view is a short list of products: a Studio user, Studio, a notebook and a full data science environment that brings its own VPC. Click, provision, done. To keep the products themselves under control, he points to the open source Service Catalog Tools from AWS Labs (Service Catalog Factory and Service Catalog Puppet, unrelated to the configuration tool of that name), which validate templates with cfn-nag and CloudFormation RSpec from a git repository and share the products across accounts.

## What if someone calls the API directly?

Service control policies at the organisational unit level catch that. One denies creating AutoML, labeling, processing, training and transform jobs or models whenever the volume KMS key or output KMS key is missing. Another denies processing, training and monitoring jobs when inter-container traffic encryption or network isolation is false. In the notebook code, the SageMaker estimator therefore carries subnets, security group IDs, both KMS keys and the two flags set to true, and the model deploy gets its own KMS key ARN.

Leave one out and the job does not start. As he put it, "my estimator is not going to get deployed. It will give me an error because I'm not allowing someone to run a processing job without ensuring network isolation."

One more policy, applied at the organisation root, opts every account out of letting AWS AI services store and use customer content to improve those services, which regulated customers usually require.

## How do you know it stays compliant?

Preventive controls are the SCPs and IAM policies; detective controls come from AWS Config managed rules, flagging things like a default security group that is not closed. For the running model, CloudWatch shows invocations (45 in his example, with no 4xx or 5xx errors), model latency versus overhead latency, and CPU, memory and disk utilisation for the endpoint on an ml.m5.xlarge instance. Flow logs in the central bucket cover the network, and CloudTrail records every SageMaker API call.

## Who should watch?

Platform and cloud engineering teams in finance, health or any regulated shop who have been asked to let data scientists in without letting the data out. If you already run Service Catalog for EC2 stacks, the talk shows how the same pattern fits SageMaker. The references at the end point to the SageMaker secure environment workshop, the Service Catalog Tools workshop and the AWS whitepaper on machine learning in financial services.

## Related Conf42 talks

- Joshua Arvin Lat on [hacking and securing ML systems and environments](https://www.conf42.com/Machine_Learning_2022_Joshua_Arvin_Lat_hacking_securing_systems_environments) at Conf42 Machine Learning 2022.
- Antje Barth on [automating ML workflows with pipelines](https://www.conf42.com/Machine_Learning_2021_Antje_Barth_Automate_workflows_pipelines) at Conf42 Machine Learning 2021.
- [Compliance as code with Cloud Custodian](https://www.conf42.com/DevSecOps_2021_Ismael_Hommani_Tanguy_Combe_compliance_as_code_cloud_custodian) at Conf42 DevSecOps 2021.

[Watch the talk on YouTube](https://youtu.be/OXIgCFaCD2c).

## From AWS

- Amazon Web Services: [aws.amazon.com](https://aws.amazon.com/)
- Amazon SageMaker: [aws.amazon.com/sagemaker](https://aws.amazon.com/sagemaker/)
- AWS Service Catalog: [aws.amazon.com/servicecatalog](https://aws.amazon.com/servicecatalog/)

## Watch the talk

[Building ML environment for regulatory customers](https://www.conf42.com/Machine_Learning_2021_Suraj_Muraleedharan_ML_environment_regulatory_customers) at Conf42 Machine Learning 2021.
