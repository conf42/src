# Infrastructure as code inherits the bugs of both infrastructure and code

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/iac-pitfalls-defaults-dry-and-state-size

In short: Tim Davis (env0) at Conf42 Site Reliability Engineering 2021 on IaC pitfalls, from framework lock-in and silent defaults to giant Terraform state files

Infrastructure as code has good news and bad news, says Tim Davis, DevOps Advocate at [env0](https://www.env0.com/), and the bad news is that it has nearly every pitfall of infrastructure plus nearly every pitfall of code. In his Conf42 Site Reliability Engineering 2021 talk, an infrastructure engineer turned advocate, by way of VMware, walks through five of them, two on the infrastructure side and three on the code side, each with a concrete fix. The recurring answer is to put infrastructure people and developers in the same conversation, since each side already knows half of the failure modes.

He frames IaC as the developer's answer to clicking through cloud consoles: developers deploying more of their own infrastructure want to write code, the way they do in their day job. And he keeps the purpose in view. Tim Davis said at Conf42 Site Reliability Engineering 2021: "there's no point in delivering infrastructure just for the sake of delivering it."

## Which framework will still fit in a year?

The first infrastructure choice is the framework, and it is partly a code choice too. Terraform uses its own HCL; Pulumi lets you write in languages you already use, such as Go or Node.js. CloudFormation and ARM templates are fine if you are certain you will stay on AWS or Azure. His cautionary tale: your company gets acquired twelve months from now by a 100% Azure or IBM Cloud shop, and those CloudFormation templates do not come with you.

Cloud-agnostic frameworks such as Terraform, Pulumi and Terragrunt do not make migration free (you still change providers and much of the code), but you keep the language, structure and deployment workflow. Terraform, the de facto standard by his account, also has providers for minor clouds, private cloud software, SaaS tools and even F5 hardware, plus an open source community where you can open an issue yourself.

## Why does security have to move left?

In many shops he worked in, security arrived at the end with a pile of firewall requests. With IaC, bring security and networking people into design, and test the security policy every time you build and test the code, so a problem costs one step back instead of five. Scanners such as Terrascan from Accurics and Checkov from Bridgecrew can block a deployment outright, for example an S3 bucket holding sensitive data with a default open policy.

## What happens when a value is blank?

Code pitfall one is defaults. The AWS console wizard makes you fill in every box for an EC2 instance; IaC does not. Leave a field out and the deployment either fails or picks a default, and a default IAM policy may be far less secure than the resource needs. Decide which values are variables, which are hard-coded, and which defaults you accept.

The fix he recommends is Open Policy Agent, policy as code next to infrastructure as code and security as code. Work with security, compliance, infrastructure and developers to define guardrails (allowed regions, instance types, instance counts, no internet-open S3 buckets) and enforce them at deployment time.

## How do you avoid copy-pasting environments?

Don't repeat yourself. Test, dev sandbox and production usually run the same app with different IPs and VPCs. Instead of three copies, inject variables at deploy time, write Terraform modules for the VPC, RDS instance and EC2 pieces and customise them per environment, or use Terragrunt to deploy one codebase to many environments.

## Why is my plan taking two hours?

The last pitfall is state size. The state file is a snapshot of what is deployed, which lets a declarative tool see three instances, read a request for four, and add one. Put VPCs, instances, load balancers and databases in one workspace and every change has to check the whole state against reality. Tim Davis said at Conf42 Site Reliability Engineering 2021: "I've had customers that come and say that their deployment times are upwards of one to 2 hours because they have giant terraform workspaces with one giant state file that takes forever to run against every single time."

The cure is the previous fix: small, modular code means small state, so updating the VPC module checks only the VPC. He adds the catch that modules alone are not enough; your automation has to run per module too.

## Who should watch

Teams starting with IaC, and teams already in deep with a single huge workspace and slow plans. It is an introductory talk with practical checklists, not a demo of the env0 product.

## Related Conf42 talks

- Andrew Kirkpatrick on [self-service Terraform through pull requests](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrew_Kirkpatrick_selfservice_PRbased_Terraform), also at SRE 2021.
- Hila Fish on [Terraform practices](https://www.conf42.com/Cloud_Native_2022_Hila_Fish_terraform_practices) at Conf42 Cloud Native 2022.
- Eran Bibi on [writing thousands of lines of IaC](https://www.conf42.com/DevSecOps_2021_Eran_Bibi_Writing_Thousands_of_Lines_of_IaC) at Conf42 DevSecOps 2021.

[Watch Tim Davis's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Tim_Davis_pitfalls_Infrastructure_as_Code)

## From env0

env0 is an infrastructure as code automation startup, focused on running IaC deployments for teams.

- [env0 website](https://www.env0.com/)

[Watch the talk on YouTube](https://youtu.be/tM0irJwS_zM).

## Watch the talk

[Pitfalls of Infrastructure as Code (And how to avoid them!)](https://www.conf42.com/Site_Reliability_Engineering_2021_Tim_Davis_pitfalls_Infrastructure_as_Code) at Conf42 Site Reliability Engineering 2021.
