# Security automation starts with knowing how you would attack yourself

Conf42 Blog, 2022-01-26. https://www.conf42.com/blog/python2022/python-scripts-for-cloud-security

In short: Joshua Arvin Lat (NuWorks Interactive Labs) at Conf42 Python 2022 on pragmatic cloud security automation with Python, boto3 and CloudFormation

Copying the best practice from a Stack Overflow comment is not a security strategy; knowing how an attacker would get in is. At Conf42 Python 2022, Joshua Arvin Lat, CTO of NuWorks Interactive Labs, AWS Machine Learning Hero and author of *Machine Learning with Amazon SageMaker Cookbook*, shared the Python habits and AWS patterns he uses for security automation: map the attack chain first, script where tools leave gaps, check data integrity inside the app, scan on change rather than on a calendar, and clone environments as code so scanners never touch production.

## Why start with the attack chain?

Because attacks change with the architecture. His example is a VPC with web servers in public subnets, databases in private ones, and a Kubernetes setup where a Cloud9 control instance sits in a public subnet. That instance is the high-risk entry point, so it is the first thing to review. Attackers are not only outside, either: insiders can do the same damage, which is why he wants defence in depth and regular audits. Once in, an attacker dumps databases, steals passwords to reuse elsewhere, or turns your servers against other systems.

Serverless does not remove the problem; it moves it into your code. Before writing anything custom, use what API Gateway offers, then add a WAF or Lambda@Edge checks that run close to the user before a request reaches the gateway, while still keeping security logic near the Lambda functions themselves.

## Where does Python help?

As glue and as a teaching tool. Nmap is more than a port scanner once you use its scripts, and Python can chain it to other tools or a report generator. He admits that his first version shelled out to bash before he found a Python library that wraps Nmap with a proper API.

The teaching example is a password-protected zip file and a custom brute-force script of around 20 lines. People who think their password is fine change their minds when it falls in under a second. His point: vulnerability management is mostly people and process, and a demo gets your initiatives approved faster than a policy document.

## What makes security scripts easier to live with?

Three small habits. A context manager that prints a start and end label around each block, so a broken script tells you where it broke; noisy, but fast to debug, and easy to silence later. Colourised terminal logs, because a wall of single-colour output hides the line you need. And a small utility class that turns nested configuration dictionaries into dot access, so config lives in a file outside the code and the same scanner runs against staging or production by swapping files. As he puts it, "the last thing you want to do is hard code credentials inside that script."

## How do you spot an attack from inside the app?

With a data integrity layer. An attacker with database access can quietly add a million to an account, and without transaction logging nobody can say how it got there. Instead of after-the-fact audit scripts, he suggests a checker inside the application, using Python and SQLAlchemy, that validates records against expected formulas before and after a transaction and flags mismatches for review. If a transaction takes 0.5 seconds and the check makes it 0.6, he considers that a fair price; it also catches plain developer mistakes.

## Scan on change, and never in production

A scanner run once a month leaves a month-long gap. Amazon Inspector runs automatically when you push a new container image or change an instance, and a Lambda function using boto3 can set it up for every new environment.

For infrastructure as code he splits CloudFormation templates into layers such as network and IAM, tests a change like closing a Redis port in staging, then reuses the same template in production, versioned and auditable. Once a full environment can be rebuilt in 10 to 15 minutes, you can clone one for manual penetration testing, another for automated scans, then delete both. That matters because "sometimes the vulnerability scanners may be harmful and sometimes noisy," Joshua Arvin Lat said at Conf42 Python 2022, and you want them hitting an identical clone, not your customers.

## Who should watch

Python developers who have been handed cloud security without a security team, and AWS users who want practical patterns rather than a framework. It is a tour of techniques with code snippets, not a single end-to-end demo.

## Related Conf42 talks

- David Melamed on [minimum viable security for Python applications](https://www.conf42.com/Python_2022_David_Melamed_minimum_viable_security_applications), from the same event.
- Radu Vunvulea on [COVID-19 as a cloud security catalyst](https://www.conf42.com/Python_2022_Radu_Vunvulea_covid19_cloud_security_catalyst).
- Filipi Pires on [malware hunting](https://www.conf42.com/Python_2022_Filipi_Pires_malware_hunting_attack_weapon).

[Watch Joshua Arvin Lat's talk](https://www.conf42.com/Python_2022_Joshua_Arvin_Lat_pragmatic_security_automation_cloud) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From NuWorks Interactive Labs

NuWorks Interactive Labs is the technology company where Joshua Arvin Lat serves as CTO.

- NuWorks Interactive Labs: [ecommerce.nuworks.ph](https://ecommerce.nuworks.ph)

[Watch the talk on YouTube](https://youtu.be/BbluNK_jOTA).

## Watch the talk

[Pragmatic Security Automation in the Cloud with Python](https://www.conf42.com/Python_2022_Joshua_Arvin_Lat_pragmatic_security_automation_cloud) at Conf42 Python 2022.
