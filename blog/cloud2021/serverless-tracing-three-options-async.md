# Your failing Lambda sends email; is that payments or the lunch bot?

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/serverless-tracing-three-options-async

In short: Aviad Mor (Lumigo) at Conf42 Cloud Native 2021 on tracing asynchronous serverless systems, comparing CloudWatch and X-Ray, home-brewed IDs and platforms

In a serverless app the bug is rarely in the function that alerts. At Conf42 Cloud Native 2021, Aviad Mor, CTO and co-founder of Lumigo, laid out why asynchronous serverless systems are so hard to trace and compared the three ways to do it: AWS CloudWatch and X-Ray out of the box, home-brewed correlation IDs, and dedicated serverless monitoring platforms like the one his company builds.

The comparison is fair to the options that aren't his, which makes the talk useful even if you never buy a monitoring product.

## What makes serverless different to observe?

Mor's definition of serverless is broad: Lambda or other functions as a service, the managed services around them such as DynamoDB and S3, and the third-party SaaS your app calls, like PayPal or Twilio. Going serverless brings three changes. You get nanoservices, lots of tiny independent parts that are usually wired together asynchronously so one overloaded piece doesn't take down the rest. You rely on fully managed services and have less control. And pay-as-you-go means a bug can show up as a spike on the bill.

He is precise about asynchronous: it is not only a Lambda invoking another Lambda asynchronously. A Lambda that writes to DynamoDB synchronously, with a DynamoDB stream triggering a second Lambda, is an asynchronous system even though each call is synchronous. He credits that pattern to Jeremy Daly's site.

## The 2am Saturday walkthrough

The heart of the talk is a scenario. It is 2am on a Saturday and an alert says a Lambda that sends email has stopped working. Do you get up? It depends who calls it. One caller is process payment, where failures cost money. The other is the lunch bot, which reminds developers to go and eat.

Finding out means tracing back through queues and Lambdas by hand, or hoping your architect kept an up-to-date diagram (he shows a real one published by Yan Cui, only part of the system and already dense). Then you need the exposure: one test user, or a VIP customer? Then debugging: matching CloudWatch metrics to logs by timestamp, adding more logging, redeploying, and often finding that the root cause sits further up the chain.

## Three ways to trace it

**CloudWatch and friends.** Metrics, logs, Logs Insights and X-Ray come out of the box with AWS support. The downsides he lists: the pieces are not easily connected, it is complicated to query, asynchronous support is partial, and it shows technical impact but rarely business impact, such as which API was affected.

**Home-brewed.** Generate a correlation ID at the earliest point, for example the Lambda behind API Gateway, pass it through Kinesis, SQS, SNS and DynamoDB streams, and write it to every log line, ideally via your logger. Then search for it in any Elasticsearch-based tool. He suggests not writing it from scratch: AWS Lambda Powertools, or OpenTracing, OpenCensus and OpenTelemetry with Jaeger for timelines. The pros: tailor-made and not cloud specific. The cons: high touch. Every new Lambda, team member and team has to remember to add it, and not every component is covered. He points to Yan Cui's blog post on the approach.

**Serverless monitoring platforms.** Buy instead of build: add a library and an IAM role, and the platform traces automatically, correlates logs and flags issues. The cons, in his own list: another third party to integrate, another screen to watch, and more than tracing if tracing is all you wanted.

## What the platform view shows

The Lumigo demo uses Medtronic's development environment: an automatically drawn transaction from S3 to a Lambda, Kinesis, DynamoDB and another Kinesis, with the input, output, return value and duration of each invocation. Medtronic, he said, has 1 billion invocations and searches by request ID to reach the one that failed. A timeline view shows where latency goes, so you don't spend time optimising a call that took a millisecond or two, and deployment markers show whether a fix stopped the errors.

"Serverless, like we said, changes everything," Mor said at Conf42 Cloud Native 2021, summing up: many moving parts, asynchronous patterns, highly distributed systems, and three families of tools to choose from.

## Who should watch

Teams running AWS Lambda in production who still debug by grepping CloudWatch logs, and anyone deciding between building correlation IDs themselves and buying a tool. The middle section on home-brewed tracing is worth it on its own.

## Related Conf42 talks

- Erez Berkner on [monitoring Kubernetes vs serverless applications](https://www.conf42.com/Cloud_Native_2021_Erez_Berkner_monitoring_kubernetes_serverless_based_applications) at Conf42 Cloud Native 2021.
- Yan Cui on [patterns for efficient serverless](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless) at Conf42 Cloud Native 2024.
- Gunnar Grosch on [AWS Fault Injection Simulator for serverless](https://www.conf42.com/Chaos_Engineering_2022_Gunnar_Grosch_serverless_aws_fault_injection_simulator) at Conf42 Chaos Engineering 2022.

[Watch Aviad Mor's talk](https://www.conf42.com/Cloud_Native_2021_Aviad_Mor_observability_serverless_asynchronous_managed_services)

## From Lumigo

Lumigo is a serverless observability platform, and its own back end runs on serverless too.

- [lumigo.io](https://lumigo.io/?utm_source=conf42)

[Watch the talk on YouTube](https://youtu.be/KllUCYd9QPA).

## Watch the talk

[Observability across serverless asynchronous managed services](https://www.conf42.com/Cloud_Native_2021_Aviad_Mor_observability_serverless_asynchronous_managed_services) at Conf42 Cloud Native 2021.
